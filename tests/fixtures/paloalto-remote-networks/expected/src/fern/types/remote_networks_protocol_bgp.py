

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_networks_protocol_bgp_peering_type import RemoteNetworksProtocolBgpPeeringType


class RemoteNetworksProtocolBgp(UniversalBaseModel):
    do_not_export_routes: typing.Optional[bool] = None
    enable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    To setup bgp protocol, enable need to set as true
    """

    local_ip_address: typing.Optional[str] = None
    originate_default_route: typing.Optional[bool] = None
    peer_as: typing.Optional[str] = None
    peer_ip_address: typing.Optional[str] = None
    peering_type: typing.Optional[RemoteNetworksProtocolBgpPeeringType] = pydantic.Field(default=None)
    """
    Exchange Routes: exchange-v4-over-v4 stands for Exchange IPv4 routes over IPv4 peering. exchange-v4-v6-over-v4 stands for Exchange both IPv4 and IPv6 routes over IPv4 peering. exchange-v4-over-v4-v6-over-v6 stands for Exchange IPv4 routes over IPv4 peer and IPv6 route over IPv6 peer. exchange-v6-over-v6 stands for Exchange IPv6 routes over IPv6 peering.
    """

    secret: typing.Optional[str] = None
    summarize_mobile_user_routes: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
