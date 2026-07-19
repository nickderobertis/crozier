

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .flow_core import FlowCore
from .flow_video_essence_parameters import FlowVideoEssenceParameters
from .flow_video_format import FlowVideoFormat


class FlowVideo(FlowCore):
    """
    Describes a video Flow
    """

    format: FlowVideoFormat = pydantic.Field()
    """
    The primary content type URN for the Flow.
    """

    essence_parameters: FlowVideoEssenceParameters = pydantic.Field()
    """
    Describes the parameters of the essence inside this video Flow
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
