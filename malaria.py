import json
from typing import Dict, Optional, List
import pandas as pd
import typing_json
from environs import Env
from cyksuid import ksuid
from facebook_business.adobjects.customaudience import CustomAudience
from clustering import get_saturated_clusters, res_col, only_target_users
from responses import last_responses, format_synthetic, get_surveyids, get_metadata
from marketing import Marketing, MarketingNameError, CreativeGroup, Location, Cluster


def get_df(cnf):
    surveys = cnf['stratum']['surveys']

    questions = [q['ref']
                 for s in surveys
                 for q in s['target_questions']]

    questions += [s['cluster_question']['ref'] for s in surveys]

    uid = cnf['survey_user']
    shortcodes = [s['shortcode'] for s in surveys]

    surveyids = get_surveyids(shortcodes, uid, cnf['chatbase'])

    responses = last_responses(surveyids,
                               questions,
                               cnf['chatbase'])

    df = pd.DataFrame(list(responses))

    if df.shape[0] == 0:
        raise Exception('No responses were found in the database!')

    # add synthetic district responses
    md = get_metadata(surveyids, cnf['chatbase'])
    md = pd.DataFrame(md)

    # could remove original district questions...
    df = pd.concat([md, df]).reset_index(drop=True)

    return df


def lookup_clusters(saturated, lookup_loc):
    lookup = pd.read_csv(lookup_loc)
    return [d for d in lookup.disthash.unique()
            if d not in saturated]

def unsaturated(df, cnf):
    stratum = cnf['stratum']
    saturated = get_saturated_clusters(df, stratum)
    return lookup_clusters(saturated, cnf['lookup_loc'])

def lookalike(df, cnf):
    df = only_target_users(df, cnf['stratum']['surveys'])
    return df.userid.unique().tolist()

def opt(cnf):
    df = get_df(cnf)
    clusters = unsaturated(df, cnf)
    users = lookalike(df, cnf)
    return clusters, users

def get_conf(env):
    c = {
        'country': env('MALARIA_COUNTRY'),
        'budget': env('MALARIA_BUDGET'),
        'survey_user': env('MALARIA_SURVEY_USER'),
        'lookup_loc': env('MALARIA_DISTRICT_LOOKUP'),
        'chatbase': {
            'db': env('CHATBASE_DATABASE'),
            'user': env('CHATBASE_USER'),
            'host': env('CHATBASE_HOST'),
            'port': env('CHATBASE_PORT'),
            'password': env('CHATBASE_PASSWORD', None),
        }
    }

    with open('config/strata.json') as f:
        s = f.read()
        c['stratum'] = json.loads(s)['strata'][0]

    return c


def load_creatives(path: str, group: str) -> CreativeGroup:
    with open(path) as f:
        s = f.read()

    d = typing_json.loads(s, Dict[str, CreativeGroup])
    return d[group]

def load_cities(path):
    cities = pd.read_csv(path)
    cities = cities[cities.rad >= 1.0]
    return cities


def uniqueness(clusters: List[Cluster]):
    ids = [cl.id for cl in clusters]
    if len(set(ids)) != len(ids):
        raise Exception('Cluster IDs combinations are not unique')

def new_ads(m: Marketing,
            budget: float,
            status: str,
            lookalike_aud: Optional[CustomAudience]) -> None:

    # TODO: get this dynamically somehow
    cities = load_cities('output/cities.csv')
    cluster_vars = ['disthash', 'distname']
    creative_config = 'config/creatives.json'
    creative_group = 'hindi'


    # TODO: clusters tells me which ones are NOT saturated
    # but only from those found in or database,
    # doesn't tell us which codes have 0 values!!!!!!!

    # cities

    # different creative group per cluster?
    cg = load_creatives(creative_config, creative_group)

    # groupby cluster
    locs = [(Cluster(i, n), [Location(r.lat, r.lng, r.rad) for _, r in df.iterrows()])
            for (i, n), df in cities.groupby(cluster_vars)]

    # check uniqueness of clusterids
    uniqueness([cl for cl, _ in locs])

    for cl, ls in locs:
        m.launch_adsets(cl, cg, ls, budget, status, lookalike_aud)


def get_aud(m: Marketing, cnf, create: bool) -> Optional[CustomAudience]:
    name = cnf['stratum']['name']
    try:
        aud = m.get_audience(name)
    except MarketingNameError:
        if create:
            aud = m.create_custom_audience(name, 'Virtual Lab auto-generated audience', [])
        else:
            aud = None
    return aud


def update_audience():
    env = Env()
    cnf = get_conf(env)
    m = Marketing(env)

    df = get_df(cnf)
    users = lookalike(df, cnf)
    aud = get_aud(m, cnf, True)

    m.add_users(aud['id'], users)


def update_ads():
    env = Env()
    cnf = get_conf(env)
    m = Marketing(env)

    # df = get_df(cnf)
    # clusters = unsaturated(df, cnf)

    aud = get_aud(m, cnf, False)
    if aud:
        uid = ksuid.ksuid().encoded.decode('utf-8')
        aud = m.create_lookalike(f'vlab-{uid}', cnf['country'], aud)

    new_ads(m, cnf['budget'], 'ACTIVE', aud)