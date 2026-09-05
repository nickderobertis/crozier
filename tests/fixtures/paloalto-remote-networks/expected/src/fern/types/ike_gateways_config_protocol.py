

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_gateways_config_protocol_ikev1 import IkeGatewaysConfigProtocolIkev1
from .ike_gateways_config_protocol_ikev2 import IkeGatewaysConfigProtocolIkev2
from .ike_gateways_config_protocol_version import IkeGatewaysConfigProtocolVersion


class IkeGatewaysConfigProtocol(UniversalBaseModel):
    ikev1: typing.Optional[IkeGatewaysConfigProtocolIkev1] = None
    ikev2: typing.Optional[IkeGatewaysConfigProtocolIkev2] = None
    version: typing.Optional[IkeGatewaysConfigProtocolVersion] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
