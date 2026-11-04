

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ai_gateway_model_pricing_response_providers_item_models_item import (
    AiGatewayModelPricingResponseProvidersItemModelsItem,
)


class AiGatewayModelPricingResponseProvidersItem(UniversalBaseModel):
    id: str
    name: str
    api: typing.Optional[str] = None
    doc: typing.Optional[str] = None
    models: typing.List[AiGatewayModelPricingResponseProvidersItemModelsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
