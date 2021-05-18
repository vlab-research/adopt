from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from typing import Any, Optional

class AudiencePermissionForActions(AbstractObject):
    def __init__(self, api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        can_edit: str = ...
        can_see_insight: str = ...
        can_share: str = ...
        subtype_supports_lookalike: str = ...
        supports_recipient_lookalike: str = ...