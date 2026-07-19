

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FlowImageEssenceParametersAspectRatio(UniversalBaseModel):
    """
    The display aspect ratio. i.e. display_width / display_height
    """

    numerator: int = pydantic.Field()
    """
    numerator
    """

    denominator: int = pydantic.Field()
    """
    denominator
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
