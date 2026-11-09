

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsLlmCacheStatusFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    LLM_CACHE_STATUS = "llm_cache_status"

    def visit(self, llm_cache_status: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsLlmCacheStatusFilterByFieldOneField.LLM_CACHE_STATUS:
            return llm_cache_status()
