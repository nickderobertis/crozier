

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WiFiStaSettings(UniversalBaseModel):
    enable: typing.Optional[bool] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    SSID
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Wi‑Fi password (empty for open networks)
    """

    static_ip: typing.Optional[bool] = None
    ip: typing.Optional[str] = None
    netmask: typing.Optional[str] = None
    gateway: typing.Optional[str] = None
    dns: typing.Optional[str] = None
    max_power: typing.Optional[float] = pydantic.Field(default=None)
    """
    dBm; resolution 0.5
    """

    max_tx_power: typing.Optional[float] = pydantic.Field(default=None)
    """
    Alias used in responses on some firmware versions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
