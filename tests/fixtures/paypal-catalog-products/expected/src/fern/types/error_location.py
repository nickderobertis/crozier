

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorLocation(enum.StrEnum):
    """
    The location of the field that caused the error. Value is `body`, `path`, or `query`.
    """

    BODY = "body"
    PATH = "path"
    QUERY = "query"

    def visit(
        self,
        body: typing.Callable[[], T_Result],
        path: typing.Callable[[], T_Result],
        query: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorLocation.BODY:
            return body()
        if self is ErrorLocation.PATH:
            return path()
        if self is ErrorLocation.QUERY:
            return query()
