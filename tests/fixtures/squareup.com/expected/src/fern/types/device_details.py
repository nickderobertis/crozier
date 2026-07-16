

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeviceDetails(UniversalBaseModel):
    """
    Details about the device that took the payment.
    """

    device_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-issued ID of the device.
    """

    device_installation_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-issued installation ID for the device.
    """

    device_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the device set by the seller.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
