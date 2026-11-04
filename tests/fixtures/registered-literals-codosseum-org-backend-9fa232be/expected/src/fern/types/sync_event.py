

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .game_state import GameState


class SyncEvent(UniversalBaseModel):
    """
    Sent to synchronise clock and game state between server and clients.
    """

    state: typing.Optional[GameState] = pydantic.Field(default=None)
    """
    Current game state
    """

    time_left: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="timeLeft"),
        pydantic.Field(
            alias="timeLeft",
            description='Time left in seconds until "next thing" (warmup countdown, round timer, next rount countdown)',
        ),
    ] = None
    """
    Time left in seconds until "next thing" (warmup countdown, round timer, next rount countdown)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
