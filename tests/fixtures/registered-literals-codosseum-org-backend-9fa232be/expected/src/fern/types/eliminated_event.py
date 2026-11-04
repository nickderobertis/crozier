

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EliminatedEvent(UniversalBaseModel):
    """
    Sent to a player if they have been eliminated from the game. This is not relevant for all game modes.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Message detailing elimination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
