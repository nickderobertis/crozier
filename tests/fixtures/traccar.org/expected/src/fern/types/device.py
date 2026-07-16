

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .device_attributes import DeviceAttributes


class Device(UniversalBaseModel):
    attributes: typing.Optional[DeviceAttributes] = None
    category: typing.Optional[str] = None
    contact: typing.Optional[str] = None
    disabled: typing.Optional[bool] = None
    geofence_ids: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="geofenceIds")] = (
        None
    )
    group_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupId")] = None
    id: typing.Optional[int] = None
    last_update: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="lastUpdate")] = (
        pydantic.Field(default=None)
    )
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    model: typing.Optional[str] = None
    name: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    position_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="positionId")] = None
    status: typing.Optional[str] = None
    unique_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uniqueId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
