

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .player_game_result import PlayerGameResult


class GameOverEvent(UniversalBaseModel):
    """
    Fired after the last round of a game is over. Contains final results of the game (may vary depending on game mode)
    """

    final_results: typing_extensions.Annotated[
        typing.Optional[typing.List[PlayerGameResult]],
        FieldMetadata(alias="finalResults"),
        pydantic.Field(alias="finalResults"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
