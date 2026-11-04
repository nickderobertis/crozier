

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .game_get_games_response_games_item import GameGetGamesResponseGamesItem


class GameGetGamesResponse(UniversalBaseModel):
    games: typing.List[GameGetGamesResponseGamesItem]
    has_next_page: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasNextPage"), pydantic.Field(alias="hasNextPage")
    ]
    next_offset: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="nextOffset"), pydantic.Field(alias="nextOffset")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
