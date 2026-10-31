

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_pipeline_id import ExtractionPipelineId
from .extraction_review_status import ExtractionReviewStatus
from .job_failure import JobFailure
from .job_id import JobId
from .job_operation import JobOperation
from .job_status import JobStatus
from .ocr_output_format import OcrOutputFormat


class JobSummary(UniversalBaseModel):
    """
    Lightweight list row for `GET /jobs`. Omits result bodies, idempotency keys,
    storage object keys, and provider cost fields.
    """

    id: JobId
    operation: JobOperation
    status: JobStatus
    output_format: OcrOutputFormat
    ocr_model: typing.Optional[str] = None
    llm_model: typing.Optional[str] = None
    page_count: int
    created_at: dt.datetime
    updated_at: dt.datetime
    error: typing.Optional[JobFailure] = None
    has_result: bool = pydantic.Field()
    """
    True when `GET /jobs/{id}` includes a terminal `result`.
    """

    url: str = pydantic.Field()
    """
    Path-absolute job resource URL (for example `/jobs/{id}`).
    """

    has_source: typing.Optional[bool] = None
    pipeline_id: typing.Optional[ExtractionPipelineId] = pydantic.Field(default=None)
    """
    Snapshot of the saved extraction pipeline id at admit time, or `null` for parse jobs,
    inline extract config, and other non-pipeline work.
    """

    pipeline_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Snapshot of the saved extraction pipeline version at admit time, or `null` when
    `pipeline_id` is `null`.
    """

    review_status: typing.Optional[ExtractionReviewStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
