

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_audio_param_format import ChatCompletionAudioParamFormat
from .chat_completion_audio_param_voice import ChatCompletionAudioParamVoice


class ChatCompletionAudioParam(UniversalBaseModel):
    """
    Parameters for audio output.

    Required when audio output is requested with
    `modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).
    """

    format: ChatCompletionAudioParamFormat
    voice: ChatCompletionAudioParamVoice

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
