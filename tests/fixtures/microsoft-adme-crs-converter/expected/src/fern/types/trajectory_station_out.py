

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .point import Point


class TrajectoryStationOut(UniversalBaseModel):
    azimuth_gn: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="azimuthGN"), pydantic.Field(alias="azimuthGN")
    ] = None
    azimuth_tn: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="azimuthTN"), pydantic.Field(alias="azimuthTN")
    ] = None
    dls: typing.Optional[float] = None
    dx_tn: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dxTN"), pydantic.Field(alias="dxTN")
    ] = None
    dy_tn: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dyTN"), pydantic.Field(alias="dyTN")
    ] = None
    dz: typing.Optional[float] = None
    inclination: typing.Optional[float] = None
    md: typing.Optional[float] = None
    original: typing.Optional[bool] = None
    point: typing.Optional[Point] = None
    wgs84latitude: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="wgs84Latitude"), pydantic.Field(alias="wgs84Latitude")
    ] = None
    wgs84longitude: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="wgs84Longitude"), pydantic.Field(alias="wgs84Longitude")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
