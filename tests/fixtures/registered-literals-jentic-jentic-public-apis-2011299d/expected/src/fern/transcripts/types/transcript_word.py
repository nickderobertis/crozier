

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranscriptWord(UniversalBaseModel):
    confidence: float = pydantic.Field()
    """
    The confidence score for the transcript of this word
    """

    start: int = pydantic.Field()
    """
    The starting time, in milliseconds, for the word
    """

    end: int = pydantic.Field()
    """
    The ending time, in milliseconds, for the word
    """

    text: str = pydantic.Field()
    """
    The text of the word
    """

    channel: typing.Optional[str] = pydantic.Field(default=None)
    """
    The channel of the word. The left and right channels are channels 1 and 2. Additional channels increment the channel number sequentially.
    """

    speaker: typing.Optional[str] = pydantic.Field(default=None)
    """
    The speaker of the word if [Speaker Diarization](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization) is enabled, else null
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
