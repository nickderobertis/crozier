

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audit_log_action_types import AuditLogActionTypes
from .audit_log_object_change_response import AuditLogObjectChangeResponse
from .snowflake_type import SnowflakeType


class AuditLogEntryResponse(UniversalBaseModel):
    id: SnowflakeType
    action_type: AuditLogActionTypes
    user_id: typing.Optional[SnowflakeType] = None
    target_id: typing.Optional[SnowflakeType] = None
    changes: typing.Optional[typing.List[AuditLogObjectChangeResponse]] = None
    options: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    reason: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
