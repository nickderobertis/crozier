

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .multi_line_string_coordinates_item_item import MultiLineStringCoordinatesItemItem
from .multi_line_string_type import MultiLineStringType


class MultiLineString(UniversalBaseModel):
    """
    MultiLineString Model
    """

    bbox: typing.Optional[typing.List[typing.Any]] = None
    type: MultiLineStringType
    coordinates: typing.List[typing.List[MultiLineStringCoordinatesItemItem]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
