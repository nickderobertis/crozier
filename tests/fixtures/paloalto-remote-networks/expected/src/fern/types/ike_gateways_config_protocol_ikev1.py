

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_gateways_config_protocol_ikev1dpd import IkeGatewaysConfigProtocolIkev1Dpd


class IkeGatewaysConfigProtocolIkev1(UniversalBaseModel):
    dpd: typing.Optional[IkeGatewaysConfigProtocolIkev1Dpd] = None
    ike_crypto_profile: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
