

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CacheClearedNotificationOp(enum.StrEnum):
    CACHE_CLEARED = "cache-cleared"

    def visit(self, cache_cleared: typing.Callable[[], T_Result]) -> T_Result:
        if self is CacheClearedNotificationOp.CACHE_CLEARED:
            return cache_cleared()
