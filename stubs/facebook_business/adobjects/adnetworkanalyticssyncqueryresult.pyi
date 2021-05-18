from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AdNetworkAnalyticsSyncQueryResult(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        query_id: str = ...
        results: str = ...
    class AggregationPeriod:
        day: str = ...
        total: str = ...
    class Breakdowns:
        ad_server_campaign_id: str = ...
        ad_space: str = ...
        age: str = ...
        app: str = ...
        clicked_view_tag: str = ...
        country: str = ...
        deal: str = ...
        deal_ad: str = ...
        deal_page: str = ...
        delivery_method: str = ...
        display_format: str = ...
        fail_reason: str = ...
        gender: str = ...
        instant_article_id: str = ...
        instant_article_page_id: str = ...
        placement: str = ...
        placement_name: str = ...
        platform: str = ...
        property: str = ...
        sdk_version: str = ...
    class Metrics:
        fb_ad_network_bidding_bid_rate: str = ...
        fb_ad_network_bidding_request: str = ...
        fb_ad_network_bidding_response: str = ...
        fb_ad_network_bidding_revenue: str = ...
        fb_ad_network_bidding_win_rate: str = ...
        fb_ad_network_click: str = ...
        fb_ad_network_cpm: str = ...
        fb_ad_network_ctr: str = ...
        fb_ad_network_filled_request: str = ...
        fb_ad_network_fill_rate: str = ...
        fb_ad_network_imp: str = ...
        fb_ad_network_impression_rate: str = ...
        fb_ad_network_request: str = ...
        fb_ad_network_revenue: str = ...
        fb_ad_network_show_rate: str = ...
        fb_ad_network_video_guarantee_revenue: str = ...
        fb_ad_network_video_mrc: str = ...
        fb_ad_network_video_mrc_rate: str = ...
        fb_ad_network_video_view: str = ...
        fb_ad_network_video_view_rate: str = ...
    class OrderingColumn:
        metric: str = ...
        time: str = ...
        value: str = ...
    class OrderingType:
        ascending: str = ...
        descending: str = ...