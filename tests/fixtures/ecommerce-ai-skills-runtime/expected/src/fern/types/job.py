

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_kind import JobKind
from .job_status import JobStatus


class Job(UniversalBaseModel):
    id: str
    tenant_id: str
    idempotency_key: str
    kind: JobKind
    payload: typing.Dict[str, typing.Any]
    status: JobStatus
    available_at: dt.datetime
    lease_until: typing.Optional[dt.datetime] = None
    attempt_count: int
    max_attempts: int
    created_by: str
    result: typing.Optional[typing.Dict[str, typing.Any]] = None
    error: typing.Optional[str] = None
    created_at: dt.datetime
    updated_at: dt.datetime
    completed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
