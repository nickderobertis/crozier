

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_optional_params_redact_pii_audio_options_override_audio_redaction_method import (
    TranscriptOptionalParamsRedactPiiAudioOptionsOverrideAudioRedactionMethod,
)


class TranscriptOptionalParamsRedactPiiAudioOptions(UniversalBaseModel):
    """
    Specify options for [PII redacted audio](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) files.
    """

    return_redacted_no_speech_audio: typing.Optional[bool] = pydantic.Field(default=None)
    """
    By default, audio redaction provides redacted audio URLs only when speech is detected. However, if your use-case specifically requires redacted audio files even for silent audio files without any dialogue, you can opt to receive these URLs by setting this parameter to `true`.
    """

    override_audio_redaction_method: typing.Optional[
        TranscriptOptionalParamsRedactPiiAudioOptionsOverrideAudioRedactionMethod
    ] = pydantic.Field(default=None)
    """
    Specify the method used to redact audio. By default, redacted audio uses a beep sound. Set to `silence` to replace PII with silence instead of a beep.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
