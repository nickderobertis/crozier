

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .play_ht_voice_params_quality import PlayHtVoiceParamsQuality
from .play_ht_voice_params_version import PlayHtVoiceParamsVersion
from .rime_voice_params_model_id import RimeVoiceParamsModelId
from .vocode_voice_params_voice_id import VocodeVoiceParamsVoiceId


class AgentParamsVoiceOne_VoiceAzure(UniversalBaseModel):
    type: typing.Literal["voice_azure"] = "voice_azure"
    voice_name: str
    pitch: typing.Optional[int] = None
    rate: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentParamsVoiceOne_VoiceElevenLabs(UniversalBaseModel):
    type: typing.Literal["voice_eleven_labs"] = "voice_eleven_labs"
    voice_id: str
    stability: typing.Optional[float] = None
    similarity_boost: typing.Optional[float] = None
    api_key: typing.Optional[str] = None
    optimize_streaming_latency: typing.Optional[int] = None
    model_id: typing.Optional[str] = None
    experimental_input_streaming: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentParamsVoiceOne_VoicePlayHt(UniversalBaseModel):
    type: typing.Literal["voice_play_ht"] = "voice_play_ht"
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


class AgentParamsVoiceOne_VoiceRime(UniversalBaseModel):
    type: typing.Literal["voice_rime"] = "voice_rime"
    speaker: str
    speed_alpha: typing.Optional[float] = None
    model_id: typing.Optional[RimeVoiceParamsModelId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentParamsVoiceOne_VoiceVocode(UniversalBaseModel):
    type: typing.Literal["voice_vocode"] = "voice_vocode"
    voice_id: VocodeVoiceParamsVoiceId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AgentParamsVoiceOne = typing_extensions.Annotated[
    typing.Union[
        AgentParamsVoiceOne_VoiceAzure,
        AgentParamsVoiceOne_VoiceElevenLabs,
        AgentParamsVoiceOne_VoicePlayHt,
        AgentParamsVoiceOne_VoiceRime,
        AgentParamsVoiceOne_VoiceVocode,
    ],
    pydantic.Field(discriminator="type"),
]
