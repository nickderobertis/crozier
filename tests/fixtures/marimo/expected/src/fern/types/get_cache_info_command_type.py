

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetCacheInfoCommandType(enum.StrEnum):
    GET_CACHE_INFO = "get-cache-info"

    def visit(self, get_cache_info: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCacheInfoCommandType.GET_CACHE_INFO:
            return get_cache_info()
