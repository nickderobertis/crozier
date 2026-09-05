

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_networks_configuration_protocol_bgp_peer import RemoteNetworksConfigurationProtocolBgpPeer
from .remote_networks_protocol_bgp import RemoteNetworksProtocolBgp


class RemoteNetworksConfigurationProtocol(UniversalBaseModel):
    """
    setup the protocol when ecmp_load_balancing is disable
    """

    bgp: typing.Optional[RemoteNetworksProtocolBgp] = None
    bgp_peer: typing.Optional[RemoteNetworksConfigurationProtocolBgpPeer] = pydantic.Field(default=None)
    """
    secondary bgp routing as bgp_peer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
