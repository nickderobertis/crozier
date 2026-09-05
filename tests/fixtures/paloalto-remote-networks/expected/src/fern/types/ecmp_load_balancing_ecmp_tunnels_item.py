

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecmp_load_balancing_ecmp_tunnels_item_bgp import EcmpLoadBalancingEcmpTunnelsItemBgp
from .ipsec_tunnel import IpsecTunnel


class EcmpLoadBalancingEcmpTunnelsItem(UniversalBaseModel):
    bgp: typing.Optional[EcmpLoadBalancingEcmpTunnelsItemBgp] = None
    ipsec_tunnel: IpsecTunnel
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
