

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSkuProductsRequestSkuFieldDataEcSkuSubscriptionPlanPlansItemPlatform(enum.StrEnum):
    """
    The platform of the subscription plan
    """

    STRIPE = "stripe"

    def visit(self, stripe: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateSkuProductsRequestSkuFieldDataEcSkuSubscriptionPlanPlansItemPlatform.STRIPE:
            return stripe()
