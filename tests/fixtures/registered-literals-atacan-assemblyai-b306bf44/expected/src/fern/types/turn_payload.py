

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .word import Word


class TurnPayload(UniversalBaseModel):
    type: str
    turn_order: int = pydantic.Field()
    """
    Order of this turn in the conversation.
    """

    turn_is_formatted: bool = pydantic.Field()
    """
    Whether this turn has been formatted.
    """

    end_of_turn: bool = pydantic.Field()
    """
    Whether this marks the end of a turn.
    """

    transcript: str = pydantic.Field()
    """
    Transcript of all finalized words in the turn.
    """

    end_of_turn_confidence: float = pydantic.Field()
    """
    The confidence score that this is the end of a turn, between 0.0 (low confidence) and 1.0 (high confidence).
    """

    words: typing.List[Word] = pydantic.Field()
    """
    Array of word-level details for this turn.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
