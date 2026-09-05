

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_networks_ipsec_tunnel_response import RemoteNetworksIpsecTunnelResponse


class RemoteNetworksIpsecTunnelResponseSet(UniversalBaseModel):
    remote_networks_ipsec_tunnel_response_set: typing.Optional[typing.List[RemoteNetworksIpsecTunnelResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
