

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .multi_polygon_coordinates_item_item_item import MultiPolygonCoordinatesItemItemItem
from .multi_polygon_type import MultiPolygonType


class MultiPolygon(UniversalBaseModel):
    """
    MultiPolygon Model
    """

    bbox: typing.Optional[typing.List[typing.Any]] = None
    type: MultiPolygonType
    coordinates: typing.List[typing.List[typing.List[MultiPolygonCoordinatesItemItemItem]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
