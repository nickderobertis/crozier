

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_speech_understanding_request import TranscriptSpeechUnderstandingRequest
from .transcript_speech_understanding_response import TranscriptSpeechUnderstandingResponse


class TranscriptSpeechUnderstanding(UniversalBaseModel):
    """
    Enable speech understanding tasks like translation, speaker identification, and custom formatting
    """

    request: typing.Optional[TranscriptSpeechUnderstandingRequest] = None
    response: typing.Optional[TranscriptSpeechUnderstandingResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
