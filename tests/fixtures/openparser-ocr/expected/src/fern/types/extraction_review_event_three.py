

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_review_event_three_type import ExtractionReviewEventThreeType


class ExtractionReviewEventThree(UniversalBaseModel):
    version: int
    actor_id: str
    created_at: dt.datetime
    type: ExtractionReviewEventThreeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
