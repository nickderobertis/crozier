

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FlowVideoEssenceParametersPixelAspectRatio(UniversalBaseModel):
    """
    The pixel aspect ratio. This is usually 1:1 (i.e. square pixels) for modern video. Some, usually older, video formats use non-square pixels e.g. some Standard Definition video. This is where that may be indicated.
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
