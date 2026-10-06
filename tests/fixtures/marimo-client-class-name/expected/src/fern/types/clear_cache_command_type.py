

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ClearCacheCommandType(enum.StrEnum):
    CLEAR_CACHE = "clear-cache"

    def visit(self, clear_cache: typing.Callable[[], T_Result]) -> T_Result:
        if self is ClearCacheCommandType.CLEAR_CACHE:
            return clear_cache()
