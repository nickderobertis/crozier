

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .audio_audio import AudioAudio
from .audio_message_type import AudioMessageType
from .base_message_type import BaseMessageType


class Audio(BaseMessageType):
    audio: AudioAudio
    message_type: typing.Optional[AudioMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `audio` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
