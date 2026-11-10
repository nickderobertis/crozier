

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_word import TranscriptWord


class TranscriptUtterance(UniversalBaseModel):
    confidence: float = pydantic.Field()
    """
    The confidence score for the transcript of this utterance
    """

    start: int = pydantic.Field()
    """
    The starting time, in milliseconds, of the utterance in the audio file
    """

    end: int = pydantic.Field()
    """
    The ending time, in milliseconds, of the utterance in the audio file
    """

    text: str = pydantic.Field()
    """
    The text for this utterance
    """

    words: typing.List[TranscriptWord] = pydantic.Field()
    """
    The words in the utterance.
    """

    channel: typing.Optional[str] = pydantic.Field(default=None)
    """
    The channel of this utterance. The left and right channels are channels 1 and 2. Additional channels increment the channel number sequentially.
    """

    speaker: str = pydantic.Field()
    """
    The speaker of this utterance, where each speaker is assigned a sequential capital letter - e.g. "A" for Speaker A, "B" for Speaker B, etc.
    """

    speaker_confidence: typing.Optional[float] = pydantic.Field(default=None)
    """
    The confidence score for the speaker label of this utterance, between 0 and 1. Only present when `speaker_options.include_speaker_confidence` is `true`.
    """

    translated_texts: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Translations keyed by language code (e.g., `{"es": "Texto traducido", "de": "Übersetzter Text"}`). Only present when `match_original_utterance` is enabled with translation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
