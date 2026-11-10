

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor import Cursor
from .entity_watchlist_screening_hit import EntityWatchlistScreeningHit
from .request_id import RequestId


class WatchlistScreeningEntityHitListResponse(UniversalBaseModel):
    """
    Paginated list of entity watchlist screening hits
    """

    entity_watchlist_screening_hits: typing.List[EntityWatchlistScreeningHit] = pydantic.Field()
    """
    List of entity watchlist screening hits
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
