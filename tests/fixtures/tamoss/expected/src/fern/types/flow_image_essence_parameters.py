

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flow_image_essence_parameters_aspect_ratio import FlowImageEssenceParametersAspectRatio


class FlowImageEssenceParameters(UniversalBaseModel):
    """
    Describes the parameters of the essence inside this image Flow
    """

    frame_width: int = pydantic.Field()
    """
    The width of the picture in pixels.
    """

    frame_height: int = pydantic.Field()
    """
    The height of the picture in pixels.
    """

    aspect_ratio: typing.Optional[FlowImageEssenceParametersAspectRatio] = pydantic.Field(default=None)
    """
    The display aspect ratio. i.e. display_width / display_height
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
