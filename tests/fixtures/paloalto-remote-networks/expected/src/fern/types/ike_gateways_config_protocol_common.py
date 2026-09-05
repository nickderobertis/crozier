

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_gateways_config_protocol_common_fragmentation import IkeGatewaysConfigProtocolCommonFragmentation
from .ike_gateways_config_protocol_common_nat_traversal import IkeGatewaysConfigProtocolCommonNatTraversal


class IkeGatewaysConfigProtocolCommon(UniversalBaseModel):
    fragmentation: typing.Optional[IkeGatewaysConfigProtocolCommonFragmentation] = None
    nat_traversal: typing.Optional[IkeGatewaysConfigProtocolCommonNatTraversal] = None
    passive_mode: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
