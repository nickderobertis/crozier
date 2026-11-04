

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .game_mode import GameMode


class GameSettings(UniversalBaseModel):
    """
    Settings for a Codosseum game
    """

    allowed_languages: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="allowedLanguages"),
        pydantic.Field(
            alias="allowedLanguages",
            description="Which programming languages are allowed to be used for submissions. If omitted, all languages are allowed.",
        ),
    ] = None
    """
    Which programming languages are allowed to be used for submissions. If omitted, all languages are allowed.
    """

    game_mode: typing_extensions.Annotated[
        typing.Optional[GameMode],
        FieldMetadata(alias="gameMode"),
        pydantic.Field(alias="gameMode", description="Game mode of this game"),
    ] = None
    """
    Game mode of this game
    """

    max_players: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxPlayers"),
        pydantic.Field(alias="maxPlayers", description="Maximum player count for the game"),
    ] = None
    """
    Maximum player count for the game
    """

    time_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="timeLimit"),
        pydantic.Field(alias="timeLimit", description="Time limit for the game, in seconds."),
    ] = None
    """
    Time limit for the game, in seconds.
    """

    max_warmup_time: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxWarmupTime"),
        pydantic.Field(
            alias="maxWarmupTime",
            description="Maximum warmup time for a game in seconds - that is, a timer that starts once 2 or more players have joined the game that delays the starting of the game to allow more players to join.",
        ),
    ] = None
    """
    Maximum warmup time for a game in seconds - that is, a timer that starts once 2 or more players have joined the game that delays the starting of the game to allow more players to join.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
