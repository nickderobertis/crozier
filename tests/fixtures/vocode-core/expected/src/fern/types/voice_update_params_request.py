

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .azure_voice_update_params_pitch import AzureVoiceUpdateParamsPitch
from .azure_voice_update_params_rate import AzureVoiceUpdateParamsRate
from .azure_voice_update_params_voice_name import AzureVoiceUpdateParamsVoiceName
from .eleven_labs_voice_update_params_api_key import ElevenLabsVoiceUpdateParamsApiKey
from .eleven_labs_voice_update_params_experimental_input_streaming import (
    ElevenLabsVoiceUpdateParamsExperimentalInputStreaming,
)
from .eleven_labs_voice_update_params_model_id import ElevenLabsVoiceUpdateParamsModelId
from .eleven_labs_voice_update_params_optimize_streaming_latency import (
    ElevenLabsVoiceUpdateParamsOptimizeStreamingLatency,
)
from .eleven_labs_voice_update_params_similarity_boost import ElevenLabsVoiceUpdateParamsSimilarityBoost
from .eleven_labs_voice_update_params_stability import ElevenLabsVoiceUpdateParamsStability
from .eleven_labs_voice_update_params_voice_id import ElevenLabsVoiceUpdateParamsVoiceId
from .play_ht_voice_update_params_api_key import PlayHtVoiceUpdateParamsApiKey
from .play_ht_voice_update_params_api_user_id import PlayHtVoiceUpdateParamsApiUserId
from .play_ht_voice_update_params_experimental_remove_silence import PlayHtVoiceUpdateParamsExperimentalRemoveSilence
from .play_ht_voice_update_params_quality import PlayHtVoiceUpdateParamsQuality
from .play_ht_voice_update_params_speed import PlayHtVoiceUpdateParamsSpeed
from .play_ht_voice_update_params_temperature import PlayHtVoiceUpdateParamsTemperature
from .play_ht_voice_update_params_text_guidance import PlayHtVoiceUpdateParamsTextGuidance
from .play_ht_voice_update_params_top_p import PlayHtVoiceUpdateParamsTopP
from .play_ht_voice_update_params_version import PlayHtVoiceUpdateParamsVersion
from .play_ht_voice_update_params_voice_guidance import PlayHtVoiceUpdateParamsVoiceGuidance
from .play_ht_voice_update_params_voice_id import PlayHtVoiceUpdateParamsVoiceId
from .rime_voice_update_params_model_id import RimeVoiceUpdateParamsModelId
from .rime_voice_update_params_speaker import RimeVoiceUpdateParamsSpeaker
from .rime_voice_update_params_speed_alpha import RimeVoiceUpdateParamsSpeedAlpha
from .vocode_voice_update_params_voice_id import VocodeVoiceUpdateParamsVoiceId


class VoiceUpdateParamsRequest_VoiceAzure(UniversalBaseModel):
    type: typing.Literal["voice_azure"] = "voice_azure"
    voice_name: typing.Optional[AzureVoiceUpdateParamsVoiceName] = None
    pitch: typing.Optional[AzureVoiceUpdateParamsPitch] = None
    rate: typing.Optional[AzureVoiceUpdateParamsRate] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class VoiceUpdateParamsRequest_VoiceElevenLabs(UniversalBaseModel):
    type: typing.Literal["voice_eleven_labs"] = "voice_eleven_labs"
    voice_id: typing.Optional[ElevenLabsVoiceUpdateParamsVoiceId] = None
    stability: typing.Optional[ElevenLabsVoiceUpdateParamsStability] = None
    similarity_boost: typing.Optional[ElevenLabsVoiceUpdateParamsSimilarityBoost] = None
    api_key: typing.Optional[ElevenLabsVoiceUpdateParamsApiKey] = None
    optimize_streaming_latency: typing.Optional[ElevenLabsVoiceUpdateParamsOptimizeStreamingLatency] = None
    model_id: typing.Optional[ElevenLabsVoiceUpdateParamsModelId] = None
    experimental_input_streaming: typing.Optional[ElevenLabsVoiceUpdateParamsExperimentalInputStreaming] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class VoiceUpdateParamsRequest_VoicePlayHt(UniversalBaseModel):
    type: typing.Literal["voice_play_ht"] = "voice_play_ht"
    voice_id: typing.Optional[PlayHtVoiceUpdateParamsVoiceId] = None
    api_user_id: typing.Optional[PlayHtVoiceUpdateParamsApiUserId] = None
    api_key: typing.Optional[PlayHtVoiceUpdateParamsApiKey] = None
    version: typing.Optional[PlayHtVoiceUpdateParamsVersion] = None
    speed: typing.Optional[PlayHtVoiceUpdateParamsSpeed] = None
    quality: typing.Optional[PlayHtVoiceUpdateParamsQuality] = None
    temperature: typing.Optional[PlayHtVoiceUpdateParamsTemperature] = None
    top_p: typing.Optional[PlayHtVoiceUpdateParamsTopP] = None
    text_guidance: typing.Optional[PlayHtVoiceUpdateParamsTextGuidance] = None
    voice_guidance: typing.Optional[PlayHtVoiceUpdateParamsVoiceGuidance] = None
    experimental_remove_silence: typing.Optional[PlayHtVoiceUpdateParamsExperimentalRemoveSilence] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class VoiceUpdateParamsRequest_VoiceRime(UniversalBaseModel):
    type: typing.Literal["voice_rime"] = "voice_rime"
    speaker: typing.Optional[RimeVoiceUpdateParamsSpeaker] = None
    speed_alpha: typing.Optional[RimeVoiceUpdateParamsSpeedAlpha] = None
    model_id: typing.Optional[RimeVoiceUpdateParamsModelId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class VoiceUpdateParamsRequest_VoiceVocode(UniversalBaseModel):
    type: typing.Literal["voice_vocode"] = "voice_vocode"
    voice_id: typing.Optional[VocodeVoiceUpdateParamsVoiceId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


VoiceUpdateParamsRequest = typing_extensions.Annotated[
    typing.Union[
        VoiceUpdateParamsRequest_VoiceAzure,
        VoiceUpdateParamsRequest_VoiceElevenLabs,
        VoiceUpdateParamsRequest_VoicePlayHt,
        VoiceUpdateParamsRequest_VoiceRime,
        VoiceUpdateParamsRequest_VoiceVocode,
    ],
    pydantic.Field(discriminator="type"),
]
