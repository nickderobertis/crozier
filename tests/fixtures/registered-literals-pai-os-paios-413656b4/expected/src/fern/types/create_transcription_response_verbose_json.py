

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcription_segment import TranscriptionSegment
from .transcription_word import TranscriptionWord


class CreateTranscriptionResponseVerboseJson(UniversalBaseModel):
    """
    Represents a verbose json transcription response returned by model, based on the provided input.
    """

    language: str = pydantic.Field()
    """
    The language of the input audio.
    """

    duration: str = pydantic.Field()
    """
    The duration of the input audio.
    """

    text: str = pydantic.Field()
    """
    The transcribed text.
    """

    words: typing.Optional[typing.List[TranscriptionWord]] = pydantic.Field(default=None)
    """
    Extracted words and their corresponding timestamps.
    """

    segments: typing.Optional[typing.List[TranscriptionSegment]] = pydantic.Field(default=None)
    """
    Segments of the transcribed text and their corresponding details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
