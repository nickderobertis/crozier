

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApConfig(UniversalBaseModel):
    enable: bool = pydantic.Field()
    """
    Whether to enable the AP mode
    """

    ssid: str = pydantic.Field()
    """
    The SSID for the AP mode
    """

    password: str = pydantic.Field()
    """
    The password for the AP mode
    """

    ip: str = pydantic.Field()
    """
    The IP address for the AP mode
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
