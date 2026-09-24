

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .point_type import PointType


class Point(UniversalBaseModel):
    type: typing.Optional[PointType] = None
    coordinates: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    This is a simple 2 (or more) numbers vector used to define Geometry Point objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
