

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptsRefreshPostError500ErrorCode(enum.StrEnum):
    PROMPTS_CACHE_REFRESH_ERROR = "PROMPTS_CACHE_REFRESH_ERROR"

    def visit(self, prompts_cache_refresh_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptsRefreshPostError500ErrorCode.PROMPTS_CACHE_REFRESH_ERROR:
            return prompts_cache_refresh_error()
