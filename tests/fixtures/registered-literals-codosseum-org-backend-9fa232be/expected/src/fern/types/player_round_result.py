

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .player_round_result_score import PlayerRoundResultScore


class PlayerRoundResult(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the player
    """

    language: str = pydantic.Field()
    """
    Language they used
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Code submitted by the player. Optional.
    """

    byte_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="byteCount"),
        pydantic.Field(alias="byteCount", description="Number of bytes in the solution (relevant for golfing modes)"),
    ]
    """
    Number of bytes in the solution (relevant for golfing modes)
    """

    time_left: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="timeLeft"),
        pydantic.Field(alias="timeLeft", description="time left on the clock (in seconds) when they pressed submit"),
    ]
    """
    time left on the clock (in seconds) when they pressed submit
    """

    score: typing.Optional[PlayerRoundResultScore] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
