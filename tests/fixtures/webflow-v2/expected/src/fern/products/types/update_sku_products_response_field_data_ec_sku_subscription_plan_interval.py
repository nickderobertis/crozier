

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlanInterval(enum.StrEnum):
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
        if self is UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlanInterval.DAY:
            return day()
        if self is UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlanInterval.WEEK:
            return week()
        if self is UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlanInterval.MONTH:
            return month()
        if self is UpdateSkuProductsResponseFieldDataEcSkuSubscriptionPlanInterval.YEAR:
            return year()
