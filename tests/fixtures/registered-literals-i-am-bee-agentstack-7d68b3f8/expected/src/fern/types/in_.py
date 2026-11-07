

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class In(enum.StrEnum):
    """
    The location of the API key.
    """

    COOKIE = "cookie"
    HEADER = "header"
    QUERY = "query"

    def visit(
        self,
        cookie: typing.Callable[[], T_Result],
        header: typing.Callable[[], T_Result],
        query: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is In.COOKIE:
            return cookie()
        if self is In.HEADER:
            return header()
        if self is In.QUERY:
            return query()
