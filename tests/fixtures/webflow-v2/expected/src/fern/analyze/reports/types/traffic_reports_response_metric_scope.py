

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TrafficReportsResponseMetricScope(enum.StrEnum):
    """
    The unit each `count` data point is measured in.
    - `session`: number of sessions.
    - `user`: number of unique users.
    - `pageview`: number of pageviews.
    """

    SESSION = "session"
    USER = "user"
    PAGEVIEW = "pageview"

    def visit(
        self,
        session: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        pageview: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TrafficReportsResponseMetricScope.SESSION:
            return session()
        if self is TrafficReportsResponseMetricScope.USER:
            return user()
        if self is TrafficReportsResponseMetricScope.PAGEVIEW:
            return pageview()
