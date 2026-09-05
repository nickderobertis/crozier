

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_gateways_config_peer_id_type import IkeGatewaysConfigPeerIdType


class IkeGatewaysConfigPeerId(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Peer ID string
    """

    type: typing.Optional[IkeGatewaysConfigPeerIdType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
