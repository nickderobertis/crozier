

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .game_mode import GameMode
from .game_state import GameState
from .player_game_result import PlayerGameResult
from .players import Players


class Game(UniversalBaseModel):
    """
    Information about a game
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Game ID
    """

    state: GameState = pydantic.Field()
    """
    current game state
    """

    time_left: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="timeLeft"),
        pydantic.Field(
            alias="timeLeft",
            description='Time left on the clock for the current game state. If state is "gameOver", this value is absent',
        ),
    ] = None
    """
    Time left on the clock for the current game state. If state is "gameOver", this value is absent
    """

    players: Players
    results: typing.Optional[typing.List[PlayerGameResult]] = pydantic.Field(default=None)
    """
    Game results. This is different from *round results* in that it combines the results from all rounds thus far
    and interprets them according to the game mode being played. Progressive/partial results are given throughout the game,
    even if it is not over yet. Ordered from best (so far) to worst.
    """

    round: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of  the currently active round ("inProgress") or the most recent round ("roundOver", "gameOver"). Absent if state = "warmup"
    """

    allowed_languages: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="allowedLanguages"),
        pydantic.Field(
            alias="allowedLanguages",
            description="Which programming languages are allowed to be used for submissions. If omitted, all languages are allowed.",
        ),
    ]
    """
    Which programming languages are allowed to be used for submissions. If omitted, all languages are allowed.
    """

    game_mode: typing_extensions.Annotated[
        GameMode,
        FieldMetadata(alias="gameMode"),
        pydantic.Field(alias="gameMode", description="Game mode of this game"),
    ]
    """
    Game mode of this game
    """

    max_players: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="maxPlayers"),
        pydantic.Field(alias="maxPlayers", description="Maximum player count for the game"),
    ]
    """
    Maximum player count for the game
    """

    time_limit: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="timeLimit"),
        pydantic.Field(alias="timeLimit", description="Time limit for the game, in seconds."),
    ]
    """
    Time limit for the game, in seconds.
    """

    max_warmup_time: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="maxWarmupTime"),
        pydantic.Field(
            alias="maxWarmupTime",
            description="Maximum warmup time for a game in seconds - that is, a timer that starts once 2 or more players have joined the game that delays the starting of the game to allow more players to join.",
        ),
    ]
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
