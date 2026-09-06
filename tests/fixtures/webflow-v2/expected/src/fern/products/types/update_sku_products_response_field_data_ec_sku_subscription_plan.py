

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_sku_products_response_field_data_ec_sku_subscription_plan_interval import (
    UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlanInterval,
)
from .update_sku_products_response_field_data_ec_sku_subscription_plan_plans_item import (
    UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlanPlansItem,
)


class UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlan(UniversalBaseModel):
    """
    [Subscription plan](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#subscription) for the SKU
    """

    interval: typing.Optional[UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlanInterval] = pydantic.Field(
        default=None
    )
    """
    Interval of subscription renewal
    """

    frequency: typing.Optional[float] = pydantic.Field(default=None)
    """
    Frequncy of billing within interval
    """

    trial: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of days of a trial
    """

    plans: typing.Optional[typing.List[UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlanPlansItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
