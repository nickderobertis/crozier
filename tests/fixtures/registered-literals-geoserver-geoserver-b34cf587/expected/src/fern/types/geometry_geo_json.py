

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class GeometryGeoJson_Point(UniversalBaseModel):
    type: typing.Literal["Point"] = "Point"
    coordinates: typing.List[float]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryGeoJson_MultiPoint(UniversalBaseModel):
    type: typing.Literal["MultiPoint"] = "MultiPoint"
    coordinates: typing.List[typing.List[float]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryGeoJson_LineString(UniversalBaseModel):
    type: typing.Literal["LineString"] = "LineString"
    coordinates: typing.List[typing.List[float]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryGeoJson_MultiLineString(UniversalBaseModel):
    type: typing.Literal["MultiLineString"] = "MultiLineString"
    coordinates: typing.List[typing.List[typing.List[float]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryGeoJson_Polygon(UniversalBaseModel):
    type: typing.Literal["Polygon"] = "Polygon"
    coordinates: typing.List[typing.List[typing.List[float]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryGeoJson_MultiPolygon(UniversalBaseModel):
    type: typing.Literal["MultiPolygon"] = "MultiPolygon"
    coordinates: typing.List[typing.List[typing.List[typing.List[float]]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GeometryGeoJson_GeometryCollection(UniversalBaseModel):
    type: typing.Literal["GeometryCollection"] = "GeometryCollection"
    geometries: typing.List["GeometryGeoJson"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GeometryGeoJson = typing_extensions.Annotated[
    typing.Union[
        GeometryGeoJson_Point,
        GeometryGeoJson_MultiPoint,
        GeometryGeoJson_LineString,
        GeometryGeoJson_MultiLineString,
        GeometryGeoJson_Polygon,
        GeometryGeoJson_MultiPolygon,
        GeometryGeoJson_GeometryCollection,
    ],
    pydantic.Field(discriminator="type"),
]
update_forward_refs(GeometryGeoJson_GeometryCollection, GeometryGeoJson=GeometryGeoJson)
