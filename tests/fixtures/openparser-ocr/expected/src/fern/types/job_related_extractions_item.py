

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_id import JobId
from .job_status import JobStatus


class JobRelatedExtractionsItem(UniversalBaseModel):
    id: JobId
    status: JobStatus
    created_at: dt.datetime
    updated_at: dt.datetime
    llm_model: typing.Optional[str] = None
    has_result: bool
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
