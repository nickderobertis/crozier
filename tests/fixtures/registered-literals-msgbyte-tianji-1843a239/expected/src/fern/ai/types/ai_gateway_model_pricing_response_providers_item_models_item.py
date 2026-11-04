

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ai_gateway_model_pricing_response_providers_item_models_item_cost import (
    AiGatewayModelPricingResponseProvidersItemModelsItemCost,
)
from .ai_gateway_model_pricing_response_providers_item_models_item_limit import (
    AiGatewayModelPricingResponseProvidersItemModelsItemLimit,
)
from .ai_gateway_model_pricing_response_providers_item_models_item_modalities import (
    AiGatewayModelPricingResponseProvidersItemModelsItemModalities,
)


class AiGatewayModelPricingResponseProvidersItemModelsItem(UniversalBaseModel):
    id: str
    name: str
    attachment: typing.Optional[bool] = None
    reasoning: typing.Optional[bool] = None
    temperature: typing.Optional[bool] = None
    tool_call: typing.Optional[bool] = None
    knowledge: typing.Optional[str] = None
    release_date: typing.Optional[str] = None
    last_updated: typing.Optional[str] = None
    modalities: typing.Optional[AiGatewayModelPricingResponseProvidersItemModelsItemModalities] = None
    open_weights: typing.Optional[bool] = None
    cost: typing.Optional[AiGatewayModelPricingResponseProvidersItemModelsItemCost] = None
    limit: typing.Optional[AiGatewayModelPricingResponseProvidersItemModelsItemLimit] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
