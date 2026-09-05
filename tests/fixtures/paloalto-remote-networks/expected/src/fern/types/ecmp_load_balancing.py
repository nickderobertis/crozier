

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecmp_load_balancing_ecmp_load_balancing_enabled import EcmpLoadBalancingEcmpLoadBalancingEnabled
from .ecmp_load_balancing_ecmp_tunnels_item import EcmpLoadBalancingEcmpTunnelsItem


class EcmpLoadBalancing(UniversalBaseModel):
    ecmp_load_balancing_enabled: typing.Optional[EcmpLoadBalancingEcmpLoadBalancingEnabled] = None
    ecmp_tunnels: typing.Optional[typing.List[EcmpLoadBalancingEcmpTunnelsItem]] = pydantic.Field(default=None)
    """
    ecmp_tunnels is required when ecmp_load_balancing is enable
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
