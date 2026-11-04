

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .device import Device


class UserDevice(UniversalBaseModel):
    """
    User device entry with session state.
    """

    active: bool = pydantic.Field()
    """
    Whether the device session is still active.
    """

    current_device: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="currentDevice"),
        pydantic.Field(alias="currentDevice", description="Whether this device matches the current session."),
    ]
    """
    Whether this device matches the current session.
    """

    device: Device

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
