

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadCheckSource(enum.StrEnum):
    """
    where to read the observed value from: the response status code, a response header (headerName), or a JSONPath over the response body (jsonPath)
    """

    STATUS = "STATUS"
    HEADER = "HEADER"
    BODY_JSONPATH = "BODY_JSONPATH"

    def visit(
        self,
        status: typing.Callable[[], T_Result],
        header: typing.Callable[[], T_Result],
        body_jsonpath: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadCheckSource.STATUS:
            return status()
        if self is LoadCheckSource.HEADER:
            return header()
        if self is LoadCheckSource.BODY_JSONPATH:
            return body_jsonpath()
