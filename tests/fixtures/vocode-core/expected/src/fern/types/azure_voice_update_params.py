

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .azure_voice_update_params_pitch import AzureVoiceUpdateParamsPitch
from .azure_voice_update_params_rate import AzureVoiceUpdateParamsRate
from .azure_voice_update_params_voice_name import AzureVoiceUpdateParamsVoiceName


class AzureVoiceUpdateParams(UniversalBaseModel):
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
