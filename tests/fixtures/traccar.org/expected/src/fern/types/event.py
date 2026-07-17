

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .event_attributes import EventAttributes


class Event(UniversalBaseModel):
    attributes: typing.Optional[EventAttributes] = None
    device_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="deviceId"), pydantic.Field(alias="deviceId")
    ] = None
    event_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="eventTime"),
        pydantic.Field(alias="eventTime", description="in IS0 8601 format. eg. `1963-11-22T18:30:00Z`"),
    ] = None
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    geofence_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="geofenceId"), pydantic.Field(alias="geofenceId")
    ] = None
    id: typing.Optional[int] = None
    maintenance_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maintenanceId"), pydantic.Field(alias="maintenanceId")
    ] = None
    position_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="positionId"), pydantic.Field(alias="positionId")
    ] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
