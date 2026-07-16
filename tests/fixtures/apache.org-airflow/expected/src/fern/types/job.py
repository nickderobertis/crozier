

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Job(UniversalBaseModel):
    dag_id: typing.Optional[str] = None
    end_date: typing.Optional[str] = None
    executor_class: typing.Optional[str] = None
    hostname: typing.Optional[str] = None
    id: typing.Optional[int] = None
    job_type: typing.Optional[str] = None
    latest_heartbeat: typing.Optional[str] = None
    start_date: typing.Optional[str] = None
    state: typing.Optional[str] = None
    unixname: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
