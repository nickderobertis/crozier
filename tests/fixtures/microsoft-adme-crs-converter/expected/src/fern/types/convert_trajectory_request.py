

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .point import Point
from .trajectory_station_in import TrajectoryStationIn


class ConvertTrajectoryRequest(UniversalBaseModel):
    azimuth_reference: typing_extensions.Annotated[
        str, FieldMetadata(alias="azimuthReference"), pydantic.Field(alias="azimuthReference")
    ]
    input_kind: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inputKind"), pydantic.Field(alias="inputKind")
    ] = None
    input_stations: typing_extensions.Annotated[
        typing.List[TrajectoryStationIn], FieldMetadata(alias="inputStations"), pydantic.Field(alias="inputStations")
    ]
    interpolate: typing.Optional[bool] = None
    method: str
    reference_point: typing_extensions.Annotated[
        typing.Optional[Point], FieldMetadata(alias="referencePoint"), pydantic.Field(alias="referencePoint")
    ] = None
    trajectory_crs: typing_extensions.Annotated[
        str, FieldMetadata(alias="trajectoryCRS"), pydantic.Field(alias="trajectoryCRS")
    ]
    unit_xy: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unitXY"), pydantic.Field(alias="unitXY")
    ] = None
    unit_z: typing_extensions.Annotated[str, FieldMetadata(alias="unitZ"), pydantic.Field(alias="unitZ")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
