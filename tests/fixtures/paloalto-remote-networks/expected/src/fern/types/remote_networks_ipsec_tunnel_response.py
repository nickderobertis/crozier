

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RemoteNetworksIpsecTunnelResponse(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    rn name
    """

    pre_shared_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pre Shared Key for the Ipsec Tunnel
    """

    service_ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Service Ip for the provisioned remote network tunnel
    """

    tunnel_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    tunnel id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
