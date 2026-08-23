

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_status import JobStatus
from .job_type import JobType
from .link import Link


class JobInfo(UniversalBaseModel):
    process_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="processID"), pydantic.Field(alias="processID")
    ] = None
    type: JobType
    job_id: typing_extensions.Annotated[str, FieldMetadata(alias="jobID"), pydantic.Field(alias="jobID")]
    status: JobStatus
    message: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    started: typing.Optional[dt.datetime] = None
    finished: typing.Optional[dt.datetime] = None
    updated: typing.Optional[dt.datetime] = None
    progress: typing.Optional[int] = None
    links: typing.Optional[typing.List[Link]] = None
    traceback: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
