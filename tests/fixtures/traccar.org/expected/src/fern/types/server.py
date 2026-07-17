

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .server_attributes import ServerAttributes


class Server(UniversalBaseModel):
    attributes: typing.Optional[ServerAttributes] = None
    bing_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bingKey"), pydantic.Field(alias="bingKey")
    ] = None
    coordinate_format: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="coordinateFormat"), pydantic.Field(alias="coordinateFormat")
    ] = None
    device_readonly: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="deviceReadonly"), pydantic.Field(alias="deviceReadonly")
    ] = None
    force_settings: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="forceSettings"), pydantic.Field(alias="forceSettings")
    ] = None
    id: typing.Optional[int] = None
    latitude: typing.Optional[float] = None
    limit_commands: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="limitCommands"), pydantic.Field(alias="limitCommands")
    ] = None
    longitude: typing.Optional[float] = None
    map_: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="map"), pydantic.Field(alias="map")] = (
        None
    )
    map_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mapUrl"), pydantic.Field(alias="mapUrl")
    ] = None
    poi_layer: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="poiLayer"), pydantic.Field(alias="poiLayer")
    ] = None
    readonly: typing.Optional[bool] = None
    registration: typing.Optional[bool] = None
    twelve_hour_format: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="twelveHourFormat"), pydantic.Field(alias="twelveHourFormat")
    ] = None
    version: typing.Optional[str] = None
    zoom: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
