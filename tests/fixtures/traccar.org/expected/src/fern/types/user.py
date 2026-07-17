

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_attributes import UserAttributes


class User(UniversalBaseModel):
    administrator: typing.Optional[bool] = None
    attributes: typing.Optional[UserAttributes] = None
    coordinate_format: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="coordinateFormat"), pydantic.Field(alias="coordinateFormat")
    ] = None
    device_limit: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="deviceLimit"), pydantic.Field(alias="deviceLimit")
    ] = None
    device_readonly: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="deviceReadonly"), pydantic.Field(alias="deviceReadonly")
    ] = None
    disabled: typing.Optional[bool] = None
    email: typing.Optional[str] = None
    expiration_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expirationTime"),
        pydantic.Field(alias="expirationTime", description="in IS0 8601 format. eg. `1963-11-22T18:30:00Z`"),
    ] = None
    """
    in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    """

    id: typing.Optional[int] = None
    latitude: typing.Optional[float] = None
    limit_commands: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="limitCommands"), pydantic.Field(alias="limitCommands")
    ] = None
    longitude: typing.Optional[float] = None
    map_: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="map"), pydantic.Field(alias="map")] = (
        None
    )
    name: typing.Optional[str] = None
    password: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    poi_layer: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="poiLayer"), pydantic.Field(alias="poiLayer")
    ] = None
    readonly: typing.Optional[bool] = None
    twelve_hour_format: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="twelveHourFormat"), pydantic.Field(alias="twelveHourFormat")
    ] = None
    user_limit: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="userLimit"), pydantic.Field(alias="userLimit")
    ] = None
    zoom: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
