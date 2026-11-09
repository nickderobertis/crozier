

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor import Cursor
from .individual_watchlist_program import IndividualWatchlistProgram
from .request_id import RequestId


class WatchlistScreeningIndividualProgramListResponse(UniversalBaseModel):
    """
    Paginated list of individual watchlist screening programs
    """

    next_cursor: typing.Optional[Cursor] = None
    request_id: RequestId
    watchlist_programs: typing.List[IndividualWatchlistProgram] = pydantic.Field()
    """
    List of individual watchlist screening programs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
