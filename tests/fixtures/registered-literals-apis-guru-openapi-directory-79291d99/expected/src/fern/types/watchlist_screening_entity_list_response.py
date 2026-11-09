

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor import Cursor
from .entity_watchlist_screening import EntityWatchlistScreening
from .request_id import RequestId


class WatchlistScreeningEntityListResponse(UniversalBaseModel):
    """
    Paginated list of entity watchlist screenings
    """

    entity_watchlist_screenings: typing.List[EntityWatchlistScreening] = pydantic.Field()
    """
    List of entity watchlist screening
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
