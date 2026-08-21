

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HttpVersion(enum.StrEnum):
    HTTP11 = "http1.1"
    HTTP2 = "http2"

    def visit(self, http11: typing.Callable[[], T_Result], http2: typing.Callable[[], T_Result]) -> T_Result:
        if self is HttpVersion.HTTP11:
            return http11()
        if self is HttpVersion.HTTP2:
            return http2()
