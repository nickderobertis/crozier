

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcription_segment import TranscriptionSegment


class CreateTranslationResponseVerboseJson(UniversalBaseModel):
    language: str = pydantic.Field()
    """
    The language of the output translation (always `english`).
    """

    duration: str = pydantic.Field()
    """
    The duration of the input audio.
    """

    text: str = pydantic.Field()
    """
    The translated text.
    """

    segments: typing.Optional[typing.List[TranscriptionSegment]] = pydantic.Field(default=None)
    """
    Segments of the translated text and their corresponding details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
