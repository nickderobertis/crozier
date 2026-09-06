

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanPlansItemStatus(enum.StrEnum):
    """
    The status of the plan
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    CANCELED = "canceled"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanPlansItemStatus.ACTIVE:
            return active()
        if self is CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanPlansItemStatus.INACTIVE:
            return inactive()
        if self is CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanPlansItemStatus.CANCELED:
            return canceled()
