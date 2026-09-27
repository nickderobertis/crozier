

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Protocol(enum.StrEnum):
    """
    protocol matcher
    """

    HTTP11 = "HTTP_1_1"
    HTTP2 = "HTTP_2"
    HTTP3 = "HTTP_3"

    def visit(
        self,
        http11: typing.Callable[[], T_Result],
        http2: typing.Callable[[], T_Result],
        http3: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Protocol.HTTP11:
            return http11()
        if self is Protocol.HTTP2:
            return http2()
        if self is Protocol.HTTP3:
            return http3()
