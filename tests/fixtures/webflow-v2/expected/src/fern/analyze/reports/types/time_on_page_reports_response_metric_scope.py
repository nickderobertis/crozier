

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TimeOnPageReportsResponseMetricScope(enum.StrEnum):
    """
    The unit each `averageSeconds` value is averaged over.
    - `session`: average time on page per session.
    - `user`: average time on page per unique user.
    - `pageview`: average time on page per pageview.
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
        if self is TimeOnPageReportsResponseMetricScope.SESSION:
            return session()
        if self is TimeOnPageReportsResponseMetricScope.USER:
            return user()
        if self is TimeOnPageReportsResponseMetricScope.PAGEVIEW:
            return pageview()
