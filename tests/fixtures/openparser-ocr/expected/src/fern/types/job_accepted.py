

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_accepted_operation import JobAcceptedOperation
from .job_id import JobId
from .job_status import JobStatus
from .ocr_output_format import OcrOutputFormat


class JobAccepted(UniversalBaseModel):
    id: JobId
    operation: JobAcceptedOperation
    status: JobStatus
    output_format: OcrOutputFormat
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
