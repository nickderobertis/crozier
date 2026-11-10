

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Word(UniversalBaseModel):
    text: str = pydantic.Field()
    """
    The transcribed word.
    """

    start: int = pydantic.Field()
    """
    Start time in milliseconds relative to the beginning of the audio stream.
    """

    end: int = pydantic.Field()
    """
    End time in milliseconds relative to the beginning of the audio stream.
    """

    confidence: float = pydantic.Field()
    """
    Confidence score for the word (0.0 to 1.0).
    """

    word_is_final: bool = pydantic.Field()
    """
    Whether the word is final.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
