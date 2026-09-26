

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskContext(UniversalBaseModel):
    proj_key: str
    user_key: str
    task_type: str
    task_id: str
    task_status: str
    execution_mode: str
    progress: float
    meta: typing.Dict[str, typing.Any]
    created_at: dt.datetime
    started_at: typing.Optional[dt.datetime] = None
    completed_at: typing.Optional[dt.datetime] = None
    start_count: typing.Optional[int] = None
    error_reason: typing.Optional[str] = None
    related_tasks: typing.Optional[typing.List[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
