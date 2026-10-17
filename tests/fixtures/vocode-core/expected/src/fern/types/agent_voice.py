

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .play_ht_voice_quality import PlayHtVoiceQuality
from .play_ht_voice_version import PlayHtVoiceVersion
from .rime_voice_model_id import RimeVoiceModelId
from .vocode_voice_voice_id import VocodeVoiceVoiceId


class AgentVoice_VoiceAzure(UniversalBaseModel):
    type: typing.Literal["voice_azure"] = "voice_azure"
    id: str
    user_id: str
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


class AgentVoice_VoiceElevenLabs(UniversalBaseModel):
    type: typing.Literal["voice_eleven_labs"] = "voice_eleven_labs"
    id: str
    user_id: str
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


class AgentVoice_VoicePlayHt(UniversalBaseModel):
    type: typing.Literal["voice_play_ht"] = "voice_play_ht"
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


class AgentVoice_VoiceRime(UniversalBaseModel):
    type: typing.Literal["voice_rime"] = "voice_rime"
    id: str
    user_id: str
    speaker: str
    speed_alpha: typing.Optional[float] = None
    model_id: typing.Optional[RimeVoiceModelId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AgentVoice_VoiceVocode(UniversalBaseModel):
    type: typing.Literal["voice_vocode"] = "voice_vocode"
    id: str
    user_id: str
    voice_id: VocodeVoiceVoiceId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AgentVoice = typing_extensions.Annotated[
    typing.Union[
        AgentVoice_VoiceAzure,
        AgentVoice_VoiceElevenLabs,
        AgentVoice_VoicePlayHt,
        AgentVoice_VoiceRime,
        AgentVoice_VoiceVocode,
    ],
    pydantic.Field(discriminator="type"),
]
