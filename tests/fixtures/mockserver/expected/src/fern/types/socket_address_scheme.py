

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SocketAddressScheme(enum.StrEnum):
    HTTP = "HTTP"
    HTTPS = "HTTPS"

    def visit(self, http: typing.Callable[[], T_Result], https: typing.Callable[[], T_Result]) -> T_Result:
        if self is SocketAddressScheme.HTTP:
            return http()
        if self is SocketAddressScheme.HTTPS:
            return https()
