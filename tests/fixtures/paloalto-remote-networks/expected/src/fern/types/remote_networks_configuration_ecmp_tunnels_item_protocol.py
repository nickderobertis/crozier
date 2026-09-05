

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_networks_protocol_bgp import RemoteNetworksProtocolBgp


class RemoteNetworksConfigurationEcmpTunnelsItemProtocol(UniversalBaseModel):
    bgp: typing.Optional[RemoteNetworksProtocolBgp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
