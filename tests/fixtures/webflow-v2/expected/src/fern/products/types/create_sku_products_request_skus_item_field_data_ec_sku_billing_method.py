

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSkuProductsRequestSkusItemFieldDataEcSkuBillingMethod(enum.StrEnum):
    """
    [Billing method](https://help.webflow.com/hc/en-us/articles/33961432087955-Add-and-manage-products-and-categories#billing-methods)for the SKU
    """

    ONE_TIME = "one-time"
    SUBSCRIPTION = "subscription"

    def visit(self, one_time: typing.Callable[[], T_Result], subscription: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSkuProductsRequestSkusItemFieldDataEcSkuBillingMethod.ONE_TIME:
            return one_time()
        if self is CreateSkuProductsRequestSkusItemFieldDataEcSkuBillingMethod.SUBSCRIPTION:
            return subscription()
