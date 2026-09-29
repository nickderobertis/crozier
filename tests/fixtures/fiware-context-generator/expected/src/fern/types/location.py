

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Location_Point(UniversalBaseModel):
    """
    Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
    """

    type: typing.Literal["Point"] = "Point"
    bbox: typing.Optional[typing.List[float]] = None
    coordinates: typing.List[float]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Location_LineString(UniversalBaseModel):
    """
    Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
    """

    type: typing.Literal["LineString"] = "LineString"
    bbox: typing.Optional[typing.List[float]] = None
    coordinates: typing.List[typing.List[float]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Location_Polygon(UniversalBaseModel):
    """
    Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
    """

    type: typing.Literal["Polygon"] = "Polygon"
    bbox: typing.Optional[typing.List[float]] = None
    coordinates: typing.List[typing.List[typing.List[float]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Location_MultiPoint(UniversalBaseModel):
    """
    Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
    """

    type: typing.Literal["MultiPoint"] = "MultiPoint"
    bbox: typing.Optional[typing.List[float]] = None
    coordinates: typing.List[typing.List[float]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Location_MultiLineString(UniversalBaseModel):
    """
    Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
    """

    type: typing.Literal["MultiLineString"] = "MultiLineString"
    bbox: typing.Optional[typing.List[float]] = None
    coordinates: typing.List[typing.List[typing.List[float]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Location_MultiPolygon(UniversalBaseModel):
    """
    Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
    """

    type: typing.Literal["MultiPolygon"] = "MultiPolygon"
    bbox: typing.Optional[typing.List[float]] = None
    coordinates: typing.List[typing.List[typing.List[typing.List[float]]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Location = typing_extensions.Annotated[
    typing.Union[
        Location_Point,
        Location_LineString,
        Location_Polygon,
        Location_MultiPoint,
        Location_MultiLineString,
        Location_MultiPolygon,
    ],
    pydantic.Field(discriminator="type"),
]
