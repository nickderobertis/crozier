

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RateLimitConfigUniqueParamsZero(enum.StrEnum):
    IP = "IP"

    def visit(self, ip: typing.Callable[[], T_Result]) -> T_Result:
        if self is RateLimitConfigUniqueParamsZero.IP:
            return ip()
