

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_result_status import JobResultStatus
from .nested_user import NestedUser


class JobResult(UniversalBaseModel):
    completed: typing.Optional[dt.datetime] = None
    created: typing.Optional[dt.datetime] = None
    data: typing.Optional[typing.Dict[str, typing.Any]] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    interval: typing.Optional[int] = pydantic.Field(default=None)
    """
    Recurrence interval (in minutes)
    """

    job_id: str
    name: str
    obj_type: typing.Optional[str] = None
    scheduled: typing.Optional[dt.datetime] = None
    started: typing.Optional[dt.datetime] = None
    status: typing.Optional[JobResultStatus] = None
    url: typing.Optional[str] = None
    user: typing.Optional[NestedUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
