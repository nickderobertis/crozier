

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_speech_understanding_request import TranscriptSpeechUnderstandingRequest
from .transcript_speech_understanding_response import TranscriptSpeechUnderstandingResponse


class TranscriptSpeechUnderstanding(UniversalBaseModel):
    """
    Speech understanding tasks like [Translation](https://www.assemblyai.com/docs/speech-understanding/translation), [Speaker Identification](https://www.assemblyai.com/docs/speech-understanding/speaker-identification), and [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting). See the task-specific docs for available options and configuration.
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
