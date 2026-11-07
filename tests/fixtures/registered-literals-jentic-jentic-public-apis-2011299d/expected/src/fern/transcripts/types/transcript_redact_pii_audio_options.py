

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_redact_pii_audio_options_override_audio_redaction_method import (
    TranscriptRedactPiiAudioOptionsOverrideAudioRedactionMethod,
)


class TranscriptRedactPiiAudioOptions(UniversalBaseModel):
    """
    The options for PII-redacted audio, if redact_pii_audio is enabled.
    See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more information.
    """

    return_redacted_no_speech_audio: typing.Optional[bool] = pydantic.Field(default=None)
    """
    By default, audio redaction provides redacted audio URLs only when speech is detected. However, if your use-case specifically requires redacted audio files even for silent audio files without any dialogue, you can opt to receive these URLs by setting this parameter to `true`.
    """

    override_audio_redaction_method: typing.Optional[TranscriptRedactPiiAudioOptionsOverrideAudioRedactionMethod] = (
        pydantic.Field(default=None)
    )
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
