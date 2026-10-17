

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .play_ht_voice_params_quality import PlayHtVoiceParamsQuality
from .play_ht_voice_params_version import PlayHtVoiceParamsVersion


class PlayHtVoiceParams(UniversalBaseModel):
    voice_id: str
    api_user_id: typing.Optional[str] = None
    api_key: typing.Optional[str] = None
    version: typing.Optional[PlayHtVoiceParamsVersion] = None
    speed: typing.Optional[float] = None
    quality: typing.Optional[PlayHtVoiceParamsQuality] = None
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
