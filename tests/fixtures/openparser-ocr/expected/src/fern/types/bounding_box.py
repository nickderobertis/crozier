

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BoundingBox(UniversalBaseModel):
    """
    Axis-aligned integer page coordinates with exclusive right and bottom edges.
    """

    left: float
    top: float
    right: float
    bottom: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
