

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReportStops(UniversalBaseModel):
    address: typing.Optional[str] = None
    device_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="deviceId"), pydantic.Field(alias="deviceId")
    ] = None
    device_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="deviceName"), pydantic.Field(alias="deviceName")
    ] = None
    duration: typing.Optional[int] = None
    end_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="endTime"),
        pydantic.Field(alias="endTime", description="in IS0 8601 format. eg. `1963-11-22T18:30:00Z`"),
    ] = None
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    engine_hours: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="engineHours"), pydantic.Field(alias="engineHours")
    ] = None
    lat: typing.Optional[float] = None
    lon: typing.Optional[float] = None
    spent_fuel: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="spentFuel"),
        pydantic.Field(alias="spentFuel", description="in liters"),
    ] = None
    """
    in liters
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="in IS0 8601 format. eg. `1963-11-22T18:30:00Z`"),
    ] = None
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
