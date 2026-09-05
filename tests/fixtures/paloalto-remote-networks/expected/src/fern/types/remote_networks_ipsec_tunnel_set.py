

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_networks_ipsec_tunnel import RemoteNetworksIpsecTunnel


class RemoteNetworksIpsecTunnelSet(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    provide a name to use as a suffix for bulk operations
    """

    remote_networks_ipsec_tunnels: typing.Optional[typing.List[RemoteNetworksIpsecTunnel]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
