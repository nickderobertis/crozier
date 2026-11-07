

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_sentence import TranscriptSentence


class SentencesResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique identifier for the transcript
    """

    confidence: float = pydantic.Field()
    """
    The confidence score for the transcript
    """

    audio_duration: float = pydantic.Field()
    """
    The duration of the audio file in seconds
    """

    sentences: typing.List[TranscriptSentence] = pydantic.Field()
    """
    An array of sentences in the transcript
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
