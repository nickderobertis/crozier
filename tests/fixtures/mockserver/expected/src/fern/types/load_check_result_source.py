

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadCheckResultSource(enum.StrEnum):
    STATUS = "STATUS"
    HEADER = "HEADER"
    BODY_JSONPATH = "BODY_JSONPATH"

    def visit(
        self,
        status: typing.Callable[[], T_Result],
        header: typing.Callable[[], T_Result],
        body_jsonpath: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadCheckResultSource.STATUS:
            return status()
        if self is LoadCheckResultSource.HEADER:
            return header()
        if self is LoadCheckResultSource.BODY_JSONPATH:
            return body_jsonpath()
