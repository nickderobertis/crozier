

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sentiment import Sentiment


class SentimentAnalysisResult(UniversalBaseModel):
    """
    The result of the Sentiment Analysis model
    """

    text: str = pydantic.Field()
    """
    The transcript of the sentence
    """

    start: int = pydantic.Field()
    """
    The starting time, in milliseconds, of the sentence
    """

    end: int = pydantic.Field()
    """
    The ending time, in milliseconds, of the sentence
    """

    sentiment: Sentiment = pydantic.Field()
    """
    The detected sentiment for the sentence, one of POSITIVE, NEUTRAL, NEGATIVE
    """

    confidence: float = pydantic.Field()
    """
    The confidence score for the detected sentiment of the sentence, from 0 to 1
    """

    channel: typing.Optional[str] = pydantic.Field(default=None)
    """
    The channel of this utterance. The left and right channels are channels 1 and 2. Additional channels increment the channel number sequentially.
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
