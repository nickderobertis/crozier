

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .line_string_coordinates_item import LineStringCoordinatesItem
from .multi_line_string_coordinates_item_item import MultiLineStringCoordinatesItemItem
from .multi_point_coordinates_item import MultiPointCoordinatesItem
from .multi_polygon_coordinates_item_item_item import MultiPolygonCoordinatesItemItemItem
from .point_coordinates import PointCoordinates
from .polygon_coordinates_item_item import PolygonCoordinatesItemItem


class GeometryCollectionOutputGeometriesItem_GeometryCollection(UniversalBaseModel):
    type: typing.Literal["GeometryCollection"] = "GeometryCollection"
    bbox: typing.Optional[typing.List[typing.Any]] = None
    geometries: typing.List["GeometryCollectionOutputGeometriesItem"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryCollectionOutputGeometriesItem_LineString(UniversalBaseModel):
    type: typing.Literal["LineString"] = "LineString"
    bbox: typing.Optional[typing.List[typing.Any]] = None
    coordinates: typing.List[LineStringCoordinatesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryCollectionOutputGeometriesItem_MultiLineString(UniversalBaseModel):
    type: typing.Literal["MultiLineString"] = "MultiLineString"
    bbox: typing.Optional[typing.List[typing.Any]] = None
    coordinates: typing.List[typing.List[MultiLineStringCoordinatesItemItem]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryCollectionOutputGeometriesItem_MultiPoint(UniversalBaseModel):
    type: typing.Literal["MultiPoint"] = "MultiPoint"
    bbox: typing.Optional[typing.List[typing.Any]] = None
    coordinates: typing.List[MultiPointCoordinatesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryCollectionOutputGeometriesItem_MultiPolygon(UniversalBaseModel):
    type: typing.Literal["MultiPolygon"] = "MultiPolygon"
    bbox: typing.Optional[typing.List[typing.Any]] = None
    coordinates: typing.List[typing.List[typing.List[MultiPolygonCoordinatesItemItemItem]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryCollectionOutputGeometriesItem_Point(UniversalBaseModel):
    type: typing.Literal["Point"] = "Point"
    bbox: typing.Optional[typing.List[typing.Any]] = None
    coordinates: PointCoordinates

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryCollectionOutputGeometriesItem_Polygon(UniversalBaseModel):
    type: typing.Literal["Polygon"] = "Polygon"
    bbox: typing.Optional[typing.List[typing.Any]] = None
    coordinates: typing.List[typing.List[PolygonCoordinatesItemItem]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GeometryCollectionOutputGeometriesItem = typing_extensions.Annotated[
    typing.Union[
        GeometryCollectionOutputGeometriesItem_GeometryCollection,
        GeometryCollectionOutputGeometriesItem_LineString,
        GeometryCollectionOutputGeometriesItem_MultiLineString,
        GeometryCollectionOutputGeometriesItem_MultiPoint,
        GeometryCollectionOutputGeometriesItem_MultiPolygon,
        GeometryCollectionOutputGeometriesItem_Point,
        GeometryCollectionOutputGeometriesItem_Polygon,
    ],
    pydantic.Field(discriminator="type"),
]
update_forward_refs(
    GeometryCollectionOutputGeometriesItem_GeometryCollection,
    GeometryCollectionOutputGeometriesItem=GeometryCollectionOutputGeometriesItem,
)
