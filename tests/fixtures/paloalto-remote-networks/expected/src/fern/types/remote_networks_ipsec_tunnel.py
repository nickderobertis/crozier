

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ecmp_load_balancing import EcmpLoadBalancing
from .ipsec_tunnel import IpsecTunnel
from .remote_networks_ipsec_tunnel_bgp import RemoteNetworksIpsecTunnelBgp


class RemoteNetworksIpsecTunnel(UniversalBaseModel):
    bgp: typing.Optional[RemoteNetworksIpsecTunnelBgp] = None
    ecmp_load_balancing: typing_extensions.Annotated[
        typing.Optional[EcmpLoadBalancing],
        FieldMetadata(alias="ecmp-load-balancing"),
        pydantic.Field(alias="ecmp-load-balancing"),
    ] = None
    ipsec_termination_node: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ipsec-termination-node"),
        pydantic.Field(alias="ipsec-termination-node", description="ipsec termination node"),
    ] = None
    """
    ipsec termination node
    """

    name: str = pydantic.Field()
    """
    Alphanumeric string begin with letter: [0-9a-zA-Z._-]
    """

    primary_tunnel: typing.Optional[IpsecTunnel] = None
    region: str
    secondary_tunnel: typing.Optional[IpsecTunnel] = None
    subnets: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
