

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flow_audio_essence_parameters_unc_parameters_unc_type import FlowAudioEssenceParametersUncParametersUncType


class FlowAudioEssenceParametersUncParameters(UniversalBaseModel):
    unc_type: FlowAudioEssenceParametersUncParametersUncType = pydantic.Field()
    """
    The uncompressed audio multi-channel representation type. If codec is `audio/x-raw-int` or `audio/x-raw-float`, unc_type must be set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
