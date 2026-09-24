

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StaConfig(UniversalBaseModel):
    enable: bool = pydantic.Field()
    """
    Whether to enable the STA mode
    """

    ssid: str = pydantic.Field()
    """
    The SSID for the wifi connection
    """

    password: str = pydantic.Field()
    """
    The password for the wifi connection
    """

    ip: str = pydantic.Field()
    """
    The IP address for the wifi connection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
