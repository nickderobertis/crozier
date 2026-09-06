

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TopPagesReportsRequestSortBy(enum.StrEnum):
    """
    The metric used to rank rows in the response, descending. Row-level `sessionCount`, `userCount`, and `pageviewCount` are always all returned regardless of `sortBy`.
    - `session`: rank by session count (default).
    - `user`: rank by unique user count.
    - `pageview`: rank by pageview count.
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
        if self is TopPagesReportsRequestSortBy.SESSION:
            return session()
        if self is TopPagesReportsRequestSortBy.USER:
            return user()
        if self is TopPagesReportsRequestSortBy.PAGEVIEW:
            return pageview()
