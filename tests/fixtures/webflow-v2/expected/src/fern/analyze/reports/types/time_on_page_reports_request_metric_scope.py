

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TimeOnPageReportsRequestMetricScope(enum.StrEnum):
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
        if self is TimeOnPageReportsRequestMetricScope.SESSION:
            return session()
        if self is TimeOnPageReportsRequestMetricScope.USER:
            return user()
        if self is TimeOnPageReportsRequestMetricScope.PAGEVIEW:
            return pageview()
