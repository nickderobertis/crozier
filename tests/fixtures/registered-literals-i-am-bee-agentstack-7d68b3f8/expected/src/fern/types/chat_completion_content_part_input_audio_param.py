

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_audio import InputAudio


class ChatCompletionContentPartInputAudioParam(UniversalBaseModel):
    """
    Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).
    """

    input_audio: InputAudio

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
