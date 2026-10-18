

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rime_voice_update_params_model_id import RimeVoiceUpdateParamsModelId
from .rime_voice_update_params_speaker import RimeVoiceUpdateParamsSpeaker
from .rime_voice_update_params_speed_alpha import RimeVoiceUpdateParamsSpeedAlpha


class RimeVoiceUpdateParams(UniversalBaseModel):
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
