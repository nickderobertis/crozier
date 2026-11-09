

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_word import TranscriptWord


class TranscriptParagraph(UniversalBaseModel):
    text: str = pydantic.Field()
    """
    The transcript of the paragraph
    """

    start: int = pydantic.Field()
    """
    The starting time, in milliseconds, of the paragraph
    """

    end: int = pydantic.Field()
    """
    The ending time, in milliseconds, of the paragraph
    """

    confidence: float = pydantic.Field()
    """
    The confidence score for the transcript of this paragraph
    """

    words: typing.List[TranscriptWord] = pydantic.Field()
    """
    An array of words in the paragraph
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
