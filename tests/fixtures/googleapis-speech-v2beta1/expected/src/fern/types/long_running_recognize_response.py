

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .speech_recognition_result import SpeechRecognitionResult


class LongRunningRecognizeResponse(UniversalBaseModel):
    """
    The only message returned to the client by the `LongRunningRecognize` method. It contains the result as zero or more sequential SpeechRecognitionResult messages. It is included in the `result.response` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.
    """

    results: typing.Optional[typing.List[SpeechRecognitionResult]] = pydantic.Field(default=None)
    """
    Output only. Sequential list of transcription results corresponding to sequential portions of audio.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
