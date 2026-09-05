

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_gateways_config_authentication import IkeGatewaysConfigAuthentication
from .ike_gateways_config_local_id import IkeGatewaysConfigLocalId
from .ike_gateways_config_peer_address import IkeGatewaysConfigPeerAddress
from .ike_gateways_config_peer_id import IkeGatewaysConfigPeerId
from .ike_gateways_config_protocol import IkeGatewaysConfigProtocol
from .ike_gateways_config_protocol_common import IkeGatewaysConfigProtocolCommon


class IkeGatewaysConfig(UniversalBaseModel):
    authentication: IkeGatewaysConfigAuthentication
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    uuid of the resource
    """

    local_id: typing.Optional[IkeGatewaysConfigLocalId] = None
    name: str = pydantic.Field()
    """
    Alphanumeric string begin with letter: [0-9a-zA-Z._-]
    """

    peer_address: IkeGatewaysConfigPeerAddress
    peer_id: typing.Optional[IkeGatewaysConfigPeerId] = None
    protocol: IkeGatewaysConfigProtocol
    protocol_common: typing.Optional[IkeGatewaysConfigProtocolCommon] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
