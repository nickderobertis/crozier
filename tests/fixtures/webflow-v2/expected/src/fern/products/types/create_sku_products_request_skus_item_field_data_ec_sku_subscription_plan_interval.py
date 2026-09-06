

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanInterval(enum.StrEnum):
    """
    Interval of subscription renewal
    """

    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanInterval.DAY:
            return day()
        if self is CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanInterval.WEEK:
            return week()
        if self is CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanInterval.MONTH:
            return month()
        if self is CreateSkuProductsRequestSkusItemFieldDataEcSkuSubscriptionPlanInterval.YEAR:
            return year()
