

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batch_child_page import BatchChildPage
from .batch_summary_counts import BatchSummaryCounts
from .extraction_pipeline_id import ExtractionPipelineId
from .extraction_review_status import ExtractionReviewStatus
from .job_failure import JobFailure
from .job_id import JobId
from .job_operation import JobOperation
from .job_progress import JobProgress
from .job_related_extractions_item import JobRelatedExtractionsItem
from .job_result import JobResult
from .job_status import JobStatus
from .ocr_output_format import OcrOutputFormat


class Job(UniversalBaseModel):
    id: JobId
    operation: JobOperation
    status: JobStatus
    output_format: OcrOutputFormat
    created_at: dt.datetime
    updated_at: dt.datetime
    completed_at: typing.Optional[dt.datetime] = None
    progress: typing.Optional[JobProgress] = None
    error: typing.Optional[JobFailure] = None
    result: typing.Optional[JobResult] = pydantic.Field(default=None)
    """
    Terminal result for single-item parse or extract jobs.
    """

    summary: typing.Optional[BatchSummaryCounts] = None
    children: typing.Optional[BatchChildPage] = None
    has_source: typing.Optional[bool] = None
    source_media_type: typing.Optional[str] = None
    source_parse_job_id: typing.Optional[JobId] = None
    related_extractions: typing.Optional[typing.List[JobRelatedExtractionsItem]] = None
    extraction_schema: typing.Optional[typing.Dict[str, typing.Any]] = None
    ocr_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    OCR model used at admit time when recorded. Omitted when unknown. Jobs do not
    expose a durable OCR options snapshot.
    """

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
