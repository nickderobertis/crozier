

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEnrollmentsV3RequestView(enum.StrEnum):
    BASIC = "basic"
    ANALYTICS = "analytics"
    TREND = "trend"

    def visit(
        self,
        basic: typing.Callable[[], T_Result],
        analytics: typing.Callable[[], T_Result],
        trend: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetEnrollmentsV3RequestView.BASIC:
            return basic()
        if self is GetEnrollmentsV3RequestView.ANALYTICS:
            return analytics()
        if self is GetEnrollmentsV3RequestView.TREND:
            return trend()
