

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_optional_params_speech_understanding_request import TranscriptOptionalParamsSpeechUnderstandingRequest


class TranscriptOptionalParamsSpeechUnderstanding(UniversalBaseModel):
    """
    Enable speech understanding tasks like translation, speaker identification, and custom formatting
    """

    request: TranscriptOptionalParamsSpeechUnderstandingRequest

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
