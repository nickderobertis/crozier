

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .play_ht_voice_quality import PlayHtVoiceQuality
from .play_ht_voice_version import PlayHtVoiceVersion


class PlayHtVoice(UniversalBaseModel):
    id: str
    user_id: str
    voice_id: str
    api_user_id: typing.Optional[str] = None
    api_key: typing.Optional[str] = None
    version: typing.Optional[PlayHtVoiceVersion] = None
    speed: typing.Optional[float] = None
    quality: typing.Optional[PlayHtVoiceQuality] = None
    temperature: typing.Optional[float] = None
    top_p: typing.Optional[float] = None
    text_guidance: typing.Optional[float] = None
    voice_guidance: typing.Optional[float] = None
    experimental_remove_silence: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
