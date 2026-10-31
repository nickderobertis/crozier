

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_review_event import ExtractionReviewEvent
from .extraction_review_status import ExtractionReviewStatus
from .job_id import JobId
from .lineage_document import LineageDocument


class ExtractionReview(UniversalBaseModel):
    """
    Versioned review state that preserves immutable machine output beside corrected output and append-only attributed events. Grounded reviews also extend the machine `lineage@1` graph with confirm and completion activities. Retracting a tip removes that confirmation from the projected graph while the event log keeps the retraction.
    """

    job_id: JobId
    status: ExtractionReviewStatus
    machine_output: typing.Any
    corrected_output: typing.Any
    lineage: typing.Optional[LineageDocument] = None
    version: int
    events: typing.List[ExtractionReviewEvent]
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    completed_at: typing.Optional[dt.datetime] = None
    reviewed_by_actor_id: typing.Optional[str] = None
    viewer_actor_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
