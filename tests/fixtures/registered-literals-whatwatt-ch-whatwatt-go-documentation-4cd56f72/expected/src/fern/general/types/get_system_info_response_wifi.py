

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetSystemInfoResponseWifi(UniversalBaseModel):
    ssid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Connected WiFi network name
    """

    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned IP address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
