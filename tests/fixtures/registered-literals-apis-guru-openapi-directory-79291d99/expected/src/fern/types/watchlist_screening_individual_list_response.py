

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor import Cursor
from .request_id import RequestId
from .watchlist_screening_individual import WatchlistScreeningIndividual


class WatchlistScreeningIndividualListResponse(UniversalBaseModel):
    """
    Paginated list of individual watchlist screenings.
    """

    next_cursor: typing.Optional[Cursor] = None
    request_id: RequestId
    watchlist_screenings: typing.List[WatchlistScreeningIndividual] = pydantic.Field()
    """
    List of individual watchlist screenings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
