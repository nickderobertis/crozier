

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PlayerCodeRevealEvent(UniversalBaseModel):
    """
    Fired when the submitted code of a player becomes available to the consumer of the event stream.
    Players see opponents' code as soon as they have submitted their code themselves.
    Everyone else sees the players' solutions after the round has ended.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Player name
    """

    lang: typing.Optional[str] = pydantic.Field(default=None)
    """
    Language used
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Code they submitted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
