

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .player_round_result import PlayerRoundResult


class Round(UniversalBaseModel):
    """
    Information about a game round
    """

    challenge: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Challenge for that round
    """

    over: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the round is over, false otherwise
    """

    results: typing.Optional[typing.List[PlayerRoundResult]] = pydantic.Field(default=None)
    """
    (Partial) results of the round, depending on its progress. Ordered from best to worst.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
