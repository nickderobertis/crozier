

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reader_device_model import ReaderDeviceModel


class ReaderDevice(UniversalBaseModel):
    """
    Information about the underlying physical device.
    """

    identifier: str = pydantic.Field()
    """
    A unique identifier of the physical device (e.g. serial number).
    """

    model: ReaderDeviceModel = pydantic.Field()
    """
    Identifier of the model of the device.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
