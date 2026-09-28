

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audit_action import AuditAction
from .audit_event_action_category import AuditEventActionCategory


class AuditEvent(UniversalBaseModel):
    id: str
    action: AuditAction
    action_category: AuditEventActionCategory
    resource: str
    business_id: typing.Optional[str] = None
    actor_id: typing.Optional[str] = None
    actor_email: typing.Optional[str] = None
    actor_display_name: typing.Optional[str] = None
    details: typing.Dict[str, typing.Any]
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
