

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WiFiNetwork(UniversalBaseModel):
    ssid: typing.Optional[str] = None
    bssid: typing.Optional[str] = pydantic.Field(default=None)
    """
    MAC address of AP
    """

    channel: typing.Optional[int] = None
    ht: typing.Optional[str] = pydantic.Field(default=None)
    """
    20, 40+, 40-
    """

    rssi: typing.Optional[int] = None
    signal: typing.Optional[int] = None
    auth_mode: typing.Optional[str] = None
    pairwise_cipher: typing.Optional[str] = None
    group_cipher: typing.Optional[str] = None
    phy: typing.Optional[str] = None
    wps: typing.Optional[str] = None
    country: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
