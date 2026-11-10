

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductStatusBreakdownRefreshInterval(enum.StrEnum):
    """
    The `refresh_interval` may be `DELAYED` or `STOPPED` even when the success rate is high. This value is only returned for Transactions status breakdowns.
    """

    NORMAL = "NORMAL"
    DELAYED = "DELAYED"
    STOPPED = "STOPPED"

    def visit(
        self,
        normal: typing.Callable[[], T_Result],
        delayed: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProductStatusBreakdownRefreshInterval.NORMAL:
            return normal()
        if self is ProductStatusBreakdownRefreshInterval.DELAYED:
            return delayed()
        if self is ProductStatusBreakdownRefreshInterval.STOPPED:
            return stopped()
