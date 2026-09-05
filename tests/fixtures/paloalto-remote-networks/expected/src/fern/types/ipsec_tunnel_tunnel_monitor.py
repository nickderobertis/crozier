

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IpsecTunnelTunnelMonitor(UniversalBaseModel):
    destination_ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Destination IP to send ICMP probe
    """

    enable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable tunnel monitoring on this tunnel
    """

    proxy_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Which proxy-id (or proxy-id-v6) the monitoring traffic will use
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
