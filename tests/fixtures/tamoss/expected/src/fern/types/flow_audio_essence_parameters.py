

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flow_audio_essence_parameters_codec_parameters import FlowAudioEssenceParametersCodecParameters
from .flow_audio_essence_parameters_unc_parameters import FlowAudioEssenceParametersUncParameters


class FlowAudioEssenceParameters(UniversalBaseModel):
    """
    Describes the parameters of the essence inside this audio Flow
    """

    sample_rate: int = pydantic.Field()
    """
    The fixed number of samples per second.
    """

    channels: int = pydantic.Field()
    """
    The channel count.
    """

    bit_depth: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of significant bits used to represent the audio sample. The minumum number of bytes then equals `round_up(bit_depth / 8)`. If codec is `audio/x-raw-int` bit_depth must be set. If codec is `audio/x-raw-float` bit_depth must be set to 32 or 64
    """

    codec_parameters: typing.Optional[FlowAudioEssenceParametersCodecParameters] = None
    unc_parameters: typing.Optional[FlowAudioEssenceParametersUncParameters] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
