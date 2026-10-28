

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .line_string_coordinates_item import LineStringCoordinatesItem
from .line_string_type import LineStringType


class LineString(UniversalBaseModel):
    """
    LineString Model
    """

    bbox: typing.Optional[typing.List[typing.Any]] = None
    type: LineStringType
    coordinates: typing.List[LineStringCoordinatesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
