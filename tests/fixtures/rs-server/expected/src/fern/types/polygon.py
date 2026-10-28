

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .polygon_coordinates_item_item import PolygonCoordinatesItemItem
from .polygon_type import PolygonType


class Polygon(UniversalBaseModel):
    """
    Polygon Model
    """

    bbox: typing.Optional[typing.List[typing.Any]] = None
    type: PolygonType
    coordinates: typing.List[typing.List[PolygonCoordinatesItemItem]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
