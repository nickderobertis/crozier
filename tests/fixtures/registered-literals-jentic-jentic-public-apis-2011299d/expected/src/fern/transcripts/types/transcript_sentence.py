

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_word import TranscriptWord


class TranscriptSentence(UniversalBaseModel):
    text: str = pydantic.Field()
    """
    The transcript of the sentence
    """

    start: int = pydantic.Field()
    """
    The starting time, in milliseconds, for the sentence
    """

    end: int = pydantic.Field()
    """
    The ending time, in milliseconds, for the sentence
    """

    confidence: float = pydantic.Field()
    """
    The confidence score for the transcript of this sentence
    """

    words: typing.List[TranscriptWord] = pydantic.Field()
    """
    An array of words in the sentence
    """

    channel: typing.Optional[str] = pydantic.Field(default=None)
    """
    The channel of the sentence. The left and right channels are channels 1 and 2. Additional channels increment the channel number sequentially.
    """

    speaker: typing.Optional[str] = pydantic.Field(default=None)
    """
    The speaker of the sentence if [Speaker Diarization](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization) is enabled, else null
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
