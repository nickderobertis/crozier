

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_last_turn_state import SessionLastTurnState


class SessionLastTurnDetails(UniversalBaseModel):
    """
    The session's most recent turn; null until the first turn.
    """

    id: str = pydantic.Field()
    """
    Id of the last turn.
    """

    state: SessionLastTurnState

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
