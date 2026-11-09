

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor import Cursor
from .entity_watchlist_program import EntityWatchlistProgram
from .request_id import RequestId


class WatchlistScreeningEntityProgramListResponse(UniversalBaseModel):
    """
    Paginated list of entity watchlist screening programs
    """

    entity_watchlist_programs: typing.List[EntityWatchlistProgram] = pydantic.Field()
    """
    List of entity watchlist screening programs
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
