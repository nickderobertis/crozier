

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .apis_v1components_observation_scope import ApisV1ComponentsObservationScope
from .job_status import JobStatus
from .job_terminal import JobTerminal


class Job(UniversalBaseModel):
    container_id: typing.Optional[str] = None
    created_at: dt.datetime
    duration_seconds: int
    ended_at: typing.Optional[dt.datetime] = None
    hostname: str
    request_id: str
    result_url: typing.Optional[str] = None
    scope: ApisV1ComponentsObservationScope
    started_at: typing.Optional[dt.datetime] = None
    status: JobStatus
    terminal: typing.Optional[JobTerminal] = None
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
