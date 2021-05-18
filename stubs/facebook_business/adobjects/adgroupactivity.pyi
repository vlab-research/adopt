from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject as AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.adobjects.objectparser import ObjectParser as ObjectParser
from facebook_business.api import FacebookRequest as FacebookRequest
from facebook_business.typechecker import TypeChecker as TypeChecker
from typing import Any, Optional

class AdgroupActivity(AbstractCrudObject):
    def __init__(self, fbid: Optional[Any] = ..., parent_id: Optional[Any] = ..., api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        ad_creative_id_new: str = ...
        ad_creative_id_old: str = ...
        asset_feed_id_new: str = ...
        asset_feed_id_old: str = ...
        bid_amount_new: str = ...
        bid_amount_old: str = ...
        bid_info_new: str = ...
        bid_info_old: str = ...
        bid_type_new: str = ...
        bid_type_old: str = ...
        conversion_specs_new: str = ...
        conversion_specs_old: str = ...
        created_time: str = ...
        display_sequence_new: str = ...
        display_sequence_old: str = ...
        engagement_audience_new: str = ...
        engagement_audience_old: str = ...
        event_time: str = ...
        event_type: str = ...
        force_run_status_new: str = ...
        force_run_status_old: str = ...
        friendly_name_new: str = ...
        friendly_name_old: str = ...
        id: str = ...
        is_reviewer_admin_new: str = ...
        is_reviewer_admin_old: str = ...
        objective_new: str = ...
        objective_old: str = ...
        objective_source_new: str = ...
        objective_source_old: str = ...
        priority_new: str = ...
        priority_old: str = ...
        reason_new: str = ...
        reason_old: str = ...
        run_status_new: str = ...
        run_status_old: str = ...
        source_adgroup_id_new: str = ...
        source_adgroup_id_old: str = ...
        start_time_new: str = ...
        start_time_old: str = ...
        stop_time_new: str = ...
        stop_time_old: str = ...
        target_spec_id_new: str = ...
        target_spec_id_old: str = ...
        tracking_pixel_ids_new: str = ...
        tracking_pixel_ids_old: str = ...
        tracking_specs_new: str = ...
        tracking_specs_old: str = ...
        update_time_new: str = ...
        update_time_old: str = ...
        view_tags_new: str = ...
        view_tags_old: str = ...
    class ObjectiveNew:
        app_installs: str = ...
        brand_awareness: str = ...
        canvas_app_engagement: str = ...
        canvas_app_installs: str = ...
        event_responses: str = ...
        lead_generation: str = ...
        link_clicks: str = ...
        local_awareness: str = ...
        messages: str = ...
        mobile_app_engagement: str = ...
        mobile_app_installs: str = ...
        none: str = ...
        offer_claims: str = ...
        page_likes: str = ...
        post_engagement: str = ...
        product_catalog_sales: str = ...
        video_views: str = ...
        website_conversions: str = ...
    class ObjectiveOld:
        app_installs: str = ...
        brand_awareness: str = ...
        canvas_app_engagement: str = ...
        canvas_app_installs: str = ...
        event_responses: str = ...
        lead_generation: str = ...
        link_clicks: str = ...
        local_awareness: str = ...
        messages: str = ...
        mobile_app_engagement: str = ...
        mobile_app_installs: str = ...
        none: str = ...
        offer_claims: str = ...
        page_likes: str = ...
        post_engagement: str = ...
        product_catalog_sales: str = ...
        video_views: str = ...
        website_conversions: str = ...
    def api_get(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...