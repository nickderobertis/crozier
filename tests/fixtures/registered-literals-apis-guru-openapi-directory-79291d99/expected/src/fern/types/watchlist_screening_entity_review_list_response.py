

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor import Cursor
from .entity_watchlist_screening_review import EntityWatchlistScreeningReview
from .request_id import RequestId


class WatchlistScreeningEntityReviewListResponse(UniversalBaseModel):
    """
    Paginated list of entity watchlist screening reviews
    """

    entity_watchlist_screening_reviews: typing.List[EntityWatchlistScreeningReview] = pydantic.Field()
    """
    List of entity watchlist screening reviews
    """

    next_cursor: typing.Optional[Cursor] = None
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
