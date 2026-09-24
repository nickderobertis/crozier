

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cloud_connection import CloudConnection
from .esp_serial_connection import EspSerialConnection
from .pic_serial_connection import PicSerialConnection
from .rfidusb_connection import RfidusbConnection


class AppConnection(UniversalBaseModel):
    cloud_connection: typing_extensions.Annotated[
        CloudConnection, FieldMetadata(alias="cloudConnection"), pydantic.Field(alias="cloudConnection")
    ]
    esp_serial_connection: typing_extensions.Annotated[
        EspSerialConnection, FieldMetadata(alias="espSerialConnection"), pydantic.Field(alias="espSerialConnection")
    ]
    pic_serial_connection: typing_extensions.Annotated[
        PicSerialConnection, FieldMetadata(alias="picSerialConnection"), pydantic.Field(alias="picSerialConnection")
    ]
    rfid_usb_connection: typing_extensions.Annotated[
        RfidusbConnection, FieldMetadata(alias="rfidUsbConnection"), pydantic.Field(alias="rfidUsbConnection")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
