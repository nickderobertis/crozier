

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
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


class ElevenLabsVoiceUpdateParams(UniversalBaseModel):
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
