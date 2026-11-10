

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor import Cursor
from .request_id import RequestId
from .watchlist_screening_hit import WatchlistScreeningHit


class WatchlistScreeningIndividualHitListResponse(UniversalBaseModel):
    """
    Paginated list of individual watchlist screening hits
    """

    next_cursor: typing.Optional[Cursor] = None
    request_id: RequestId
    watchlist_screening_hits: typing.List[WatchlistScreeningHit] = pydantic.Field()
    """
    List of individual watchlist screening hits
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
