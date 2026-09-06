

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSkuProductsRequestSkuFieldDataEcSkuSubscriptionPlanInterval(enum.StrEnum):
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
        if self is UpdateSkuProductsRequestSkuFieldDataEcSkuSubscriptionPlanInterval.DAY:
            return day()
        if self is UpdateSkuProductsRequestSkuFieldDataEcSkuSubscriptionPlanInterval.WEEK:
            return week()
        if self is UpdateSkuProductsRequestSkuFieldDataEcSkuSubscriptionPlanInterval.MONTH:
            return month()
        if self is UpdateSkuProductsRequestSkuFieldDataEcSkuSubscriptionPlanInterval.YEAR:
            return year()
