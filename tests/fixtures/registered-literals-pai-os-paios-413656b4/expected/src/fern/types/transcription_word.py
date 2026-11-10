

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranscriptionWord(UniversalBaseModel):
    word: str = pydantic.Field()
    """
    The text content of the word.
    """

    start: float = pydantic.Field()
    """
    Start time of the word in seconds.
    """

    end: float = pydantic.Field()
    """
    End time of the word in seconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
