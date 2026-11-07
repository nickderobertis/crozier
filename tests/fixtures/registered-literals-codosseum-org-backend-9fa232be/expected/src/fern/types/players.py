

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .player import Player


class Players(UniversalBaseModel):
    """
    Information about the players in a game
    """

    players: typing.List[Player] = pydantic.Field()
    """
    The names of the players currently in the game
    """

    admin: str = pydantic.Field()
    """
    The name of the player who created the game
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
