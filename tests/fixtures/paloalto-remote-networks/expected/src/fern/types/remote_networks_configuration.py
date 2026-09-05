

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_networks_configuration_ecmp_load_balancing import RemoteNetworksConfigurationEcmpLoadBalancing
from .remote_networks_configuration_ecmp_tunnels_item import RemoteNetworksConfigurationEcmpTunnelsItem
from .remote_networks_configuration_inbound_access import RemoteNetworksConfigurationInboundAccess
from .remote_networks_configuration_protocol import RemoteNetworksConfigurationProtocol


class RemoteNetworksConfiguration(UniversalBaseModel):
    ecmp_load_balancing: typing.Optional[RemoteNetworksConfigurationEcmpLoadBalancing] = None
    ecmp_tunnels: typing.Optional[typing.List[RemoteNetworksConfigurationEcmpTunnelsItem]] = pydantic.Field(
        default=None
    )
    """
    ecmp_tunnels is required when ecmp_load_balancing is enable
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    uuid of the resource
    """

    inbound_access: typing.Optional[RemoteNetworksConfigurationInboundAccess] = None
    ipsec_tunnel: typing.Optional[str] = pydantic.Field(default=None)
    """
    ipsec_tunnel is required when ecmp_load_balancing is disable
    """

    license_type: str = pydantic.Field()
    """
    New customer will only be on aggregate bandwidth licensing
    """

    name: str = pydantic.Field()
    """
    Alphanumeric string begin with letter: [0-9a-zA-Z._-]
    """

    override_spn_name: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable/disable the ability to override the remote-network's spn-name at site level
    """

    protocol: typing.Optional[RemoteNetworksConfigurationProtocol] = pydantic.Field(default=None)
    """
    setup the protocol when ecmp_load_balancing is disable
    """

    region: str
    secondary_ipsec_tunnel: typing.Optional[str] = pydantic.Field(default=None)
    """
    specify secondary ipsec_tunnel if needed
    """

    spn_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    spn-name is needed when license_type is FWAAS-AGGREGATE
    """

    subnets: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
