

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_operation import ActionOperation
from .action_status import ActionStatus


class Action(UniversalBaseModel):
    id: str
    tenant_id: str
    idempotency_key: str
    operation: ActionOperation
    payload: typing.Dict[str, typing.Any]
    requested_by: str
    approved_by: typing.Optional[str] = None
    status: ActionStatus
    result: typing.Optional[typing.Dict[str, typing.Any]] = None
    error: typing.Optional[str] = None
    lease_until: typing.Optional[dt.datetime] = None
    attempt_count: int
    last_attempt_at: typing.Optional[dt.datetime] = None
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
