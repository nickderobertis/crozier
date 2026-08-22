

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProxyErrorErrorType(enum.StrEnum):
    PROXY_ERROR = "proxy_error"

    def visit(self, proxy_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProxyErrorErrorType.PROXY_ERROR:
            return proxy_error()
