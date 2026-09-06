

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_products_request_sku_field_data_ec_sku_subscription_plan_plans_item_platform import (
    CreateProductsRequestSkuFieldDataEcSkuSubscriptionPlanPlansItemPlatform,
)
from .create_products_request_sku_field_data_ec_sku_subscription_plan_plans_item_status import (
    CreateProductsRequestSkuFieldDataEcSkuSubscriptionPlanPlansItemStatus,
)


class CreateProductsRequestSkuFieldDataEcSkuSubscriptionPlanPlansItem(UniversalBaseModel):
    platform: typing.Optional[CreateProductsRequestSkuFieldDataEcSkuSubscriptionPlanPlansItemPlatform] = pydantic.Field(
        default=None
    )
    """
    The platform of the subscription plan
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the plan
    """

    status: typing.Optional[CreateProductsRequestSkuFieldDataEcSkuSubscriptionPlanPlansItemStatus] = pydantic.Field(
        default=None
    )
    """
    The status of the plan
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
