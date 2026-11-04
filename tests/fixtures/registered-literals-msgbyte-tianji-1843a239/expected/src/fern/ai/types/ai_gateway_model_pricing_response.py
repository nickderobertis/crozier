

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ai_gateway_model_pricing_response_providers_item import AiGatewayModelPricingResponseProvidersItem


class AiGatewayModelPricingResponse(UniversalBaseModel):
    providers: typing.List[AiGatewayModelPricingResponseProvidersItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
