

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_networks_configuration_ecmp_tunnels_item_protocol import RemoteNetworksConfigurationEcmpTunnelsItemProtocol


class RemoteNetworksConfigurationEcmpTunnelsItem(UniversalBaseModel):
    ipsec_tunnel: str
    name: str
    protocol: RemoteNetworksConfigurationEcmpTunnelsItemProtocol

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
