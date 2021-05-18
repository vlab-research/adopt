from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject as AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.adobjects.objectparser import ObjectParser as ObjectParser
from facebook_business.api import FacebookRequest as FacebookRequest
from facebook_business.typechecker import TypeChecker as TypeChecker
from typing import Any, Optional

class AdAsyncRequestSet(AbstractCrudObject):
    def __init__(self, fbid: Optional[Any] = ..., parent_id: Optional[Any] = ..., api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        canceled_count: str = ...
        created_time: str = ...
        error_count: str = ...
        id: str = ...
        in_progress_count: str = ...
        initial_count: str = ...
        is_completed: str = ...
        name: str = ...
        notification_mode: str = ...
        notification_result: str = ...
        notification_status: str = ...
        notification_uri: str = ...
        owner_id: str = ...
        success_count: str = ...
        total_count: str = ...
        updated_time: str = ...
        ad_specs: str = ...
    class NotificationMode:
        off: str = ...
        on_complete: str = ...
    class NotificationStatus:
        not_sent: str = ...
        sending: str = ...
        sent: str = ...
    @classmethod
    def get_endpoint(cls): ...
    def api_create(self, parent_id: Any, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def api_delete(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def api_get(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def api_update(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_requests(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...