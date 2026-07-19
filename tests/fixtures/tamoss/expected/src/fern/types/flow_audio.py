

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .flow_audio_essence_parameters import FlowAudioEssenceParameters
from .flow_audio_format import FlowAudioFormat
from .flow_core import FlowCore


class FlowAudio(FlowCore):
    """
    Describes an audio Flow
    """

    format: FlowAudioFormat = pydantic.Field()
    """
    The primary content type URN for the Flow.
    """

    essence_parameters: FlowAudioEssenceParameters = pydantic.Field()
    """
    Describes the parameters of the essence inside this audio Flow
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
