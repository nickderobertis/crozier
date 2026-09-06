

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .store_item_reviews_store_review_summary import StoreItemReviewsStoreReviewSummary


class StoreItemReviews(UniversalBaseModel):
    summary_filtered: typing.Optional[StoreItemReviewsStoreReviewSummary] = None
    summary_language_specific: typing.Optional[StoreItemReviewsStoreReviewSummary] = None
    summary_unfiltered: typing.Optional[StoreItemReviewsStoreReviewSummary] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
