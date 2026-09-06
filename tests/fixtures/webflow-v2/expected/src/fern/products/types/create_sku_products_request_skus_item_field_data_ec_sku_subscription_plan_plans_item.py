

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_sku_products_request_skus_item_field_data_ec_sku_subscription_plan_plans_item_platform import (
    CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanPlansItemPlatform,
)
from .create_sku_products_request_skus_item_field_data_ec_sku_subscription_plan_plans_item_status import (
    CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanPlansItemStatus,
)


class CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanPlansItem(UniversalBaseModel):
    platform: typing.Optional[CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanPlansItemPlatform] = (
        pydantic.Field(default=None)
    )
    """
    The platform of the subscription plan
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the plan
    """

    status: typing.Optional[CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanPlansItemStatus] = (
        pydantic.Field(default=None)
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
