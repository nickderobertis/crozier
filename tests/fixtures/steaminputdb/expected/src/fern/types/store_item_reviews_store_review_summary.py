

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreItemReviewsStoreReviewSummary(UniversalBaseModel):
    percent_positive: typing.Optional[int] = None
    review_count: typing.Optional[int] = None
    review_score: typing.Optional[int] = None
    review_score_label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
