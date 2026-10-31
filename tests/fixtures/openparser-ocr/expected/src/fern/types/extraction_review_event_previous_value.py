

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_review_event_previous_value_type import ExtractionReviewEventPreviousValueType


class ExtractionReviewEventPreviousValue(UniversalBaseModel):
    version: int
    actor_id: str
    created_at: dt.datetime
    type: ExtractionReviewEventPreviousValueType
    path: str
    previous_value: typing.Optional[typing.Any] = None
    value: typing.Any
    note: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
