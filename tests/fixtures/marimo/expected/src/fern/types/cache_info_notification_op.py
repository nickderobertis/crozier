

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CacheInfoNotificationOp(enum.StrEnum):
    CACHE_INFO = "cache-info"

    def visit(self, cache_info: typing.Callable[[], T_Result]) -> T_Result:
        if self is CacheInfoNotificationOp.CACHE_INFO:
            return cache_info()
