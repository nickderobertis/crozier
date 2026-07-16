

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReportTrips(UniversalBaseModel):
    average_speed: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="averageSpeed")] = (
        pydantic.Field(default=None)
    )
    """
    in knots
    """

    device_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="deviceId")] = None
    device_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="deviceName")] = None
    distance: typing.Optional[float] = pydantic.Field(default=None)
    """
    in meters
    """

    driver_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="driverName")] = None
    driver_unique_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="driverUniqueId")] = None
    duration: typing.Optional[int] = None
    end_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="endAddress")] = None
    end_lat: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="endLat")] = None
    end_lon: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="endLon")] = None
    end_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="endTime")] = (
        pydantic.Field(default=None)
    )
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    max_speed: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="maxSpeed")] = pydantic.Field(
        default=None
    )
    """
    in knots
    """

    spent_fuel: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="spentFuel")] = pydantic.Field(
        default=None
    )
    """
    in liters
    """

    start_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="startAddress")] = None
    start_lat: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="startLat")] = None
    start_lon: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="startLon")] = None
    start_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="startTime")] = (
        pydantic.Field(default=None)
    )
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
