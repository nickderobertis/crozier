

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batch_child_summary_result import BatchChildSummaryResult
from .job_failure import JobFailure
from .job_id import JobId
from .job_status import JobStatus
from .ocr_output_format import OcrOutputFormat


class BatchChildSummary(UniversalBaseModel):
    client_item_id: str
    job_id: JobId
    file_index: int
    status: JobStatus
    output_format: OcrOutputFormat
    error: typing.Optional[JobFailure] = None
    result: typing.Optional[BatchChildSummaryResult] = pydantic.Field(default=None)
    """
    Terminal child result when `status` is `succeeded`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
