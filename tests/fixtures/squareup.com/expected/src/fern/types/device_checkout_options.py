

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tip_settings import TipSettings


class DeviceCheckoutOptions(UniversalBaseModel):
    """ """

    device_id: str = pydantic.Field()
    """
    The unique ID of the device intended for this `TerminalCheckout`.
    A list of `DeviceCode` objects can be retrieved from the /v2/devices/codes endpoint.
    Match a `DeviceCode.device_id` value with `device_id` to get the associated device code.
    """

    skip_receipt_screen: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Instructs the device to skip the receipt screen. Defaults to false.
    """

    tip_settings: typing.Optional[TipSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
