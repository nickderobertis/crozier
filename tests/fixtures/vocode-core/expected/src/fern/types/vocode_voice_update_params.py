

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vocode_voice_update_params_voice_id import VocodeVoiceUpdateParamsVoiceId


class VocodeVoiceUpdateParams(UniversalBaseModel):
    voice_id: typing.Optional[VocodeVoiceUpdateParamsVoiceId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
