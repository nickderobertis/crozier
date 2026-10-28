

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .multi_point_coordinates_item import MultiPointCoordinatesItem
from .multi_point_type import MultiPointType


class MultiPoint(UniversalBaseModel):
    """
    MultiPoint Model
    """

    bbox: typing.Optional[typing.List[typing.Any]] = None
    type: MultiPointType
    coordinates: typing.List[MultiPointCoordinatesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
