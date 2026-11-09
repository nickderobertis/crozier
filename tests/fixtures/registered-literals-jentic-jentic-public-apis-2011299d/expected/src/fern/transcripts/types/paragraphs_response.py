

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_paragraph import TranscriptParagraph


class ParagraphsResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique identifier of your transcript
    """

    confidence: float = pydantic.Field()
    """
    The confidence score for the transcript
    """

    audio_duration: float = pydantic.Field()
    """
    The duration of the audio file in seconds
    """

    paragraphs: typing.List[TranscriptParagraph] = pydantic.Field()
    """
    An array of paragraphs in the transcript
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
