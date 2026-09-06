

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_products_response_items_item_skus_item_field_data_ec_sku_subscription_plan_plans_item_platform import (
    ListProductsResponseItemsItemSkusItemFieldDataEcSkuSubscriptionPlanPlansItemPlatform,
)
from .list_products_response_items_item_skus_item_field_data_ec_sku_subscription_plan_plans_item_status import (
    ListProductsResponseItemsItemSkusItemFieldDataEcSkuSubscriptionPlanPlansItemStatus,
)


class ListProductsResponseItemsItemSkusItemFieldDataEcSkuSubscriptionPlanPlansItem(UniversalBaseModel):
    platform: typing.Optional[ListProductsResponseItemsItemSkusItemFieldDataEcSkuSubscriptionPlanPlansItemPlatform] = (
        pydantic.Field(default=None)
    )
    """
    The platform of the subscription plan
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the plan
    """

    status: typing.Optional[ListProductsResponseItemsItemSkusItemFieldDataEcSkuSubscriptionPlanPlansItemStatus] = (
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
