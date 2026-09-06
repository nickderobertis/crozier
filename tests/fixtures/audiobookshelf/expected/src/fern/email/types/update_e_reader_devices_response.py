

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.ereader_device_object import EreaderDeviceObject


class UpdateEReaderDevicesResponse(UniversalBaseModel):
    ereader_devices: typing_extensions.Annotated[
        typing.Optional[typing.List[EreaderDeviceObject]],
        FieldMetadata(alias="ereaderDevices"),
        pydantic.Field(alias="ereaderDevices"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
