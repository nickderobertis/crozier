

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .flow_core import FlowCore
from .flow_image_essence_parameters import FlowImageEssenceParameters
from .flow_image_format import FlowImageFormat


class FlowImage(FlowCore):
    """
    Describes a still image Flow, for use by thumbnail tracks etc
    """

    format: FlowImageFormat = pydantic.Field()
    """
    The primary content type URN for the Flow.
    """

    essence_parameters: FlowImageEssenceParameters = pydantic.Field()
    """
    Describes the parameters of the essence inside this image Flow
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
