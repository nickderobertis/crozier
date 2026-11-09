

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LlmMetricsItem(enum.StrEnum):
    TOTAL_TOKENS = "total_tokens"
    PROMPT_TOKENS = "prompt_tokens"
    COMPLETION_TOKENS = "completion_tokens"
    AI_REQUEST_COUNT = "ai_request_count"
    COST = "cost"
    LLM_CACHE_EMBEDDINGS_LATENCY_AVERAGE = "llm_cache_embeddings_latency_average"
    LLM_CACHE_FETCH_LATENCY_AVERAGE = "llm_cache_fetch_latency_average"
    LLM_LATENCY_AVERAGE = "llm_latency_average"
    LLM_EMBEDDINGS_TOKENS = "llm_embeddings_tokens"
    LLM_EMBEDDINGS_COST = "llm_embeddings_cost"

    def visit(
        self,
        total_tokens: typing.Callable[[], T_Result],
        prompt_tokens: typing.Callable[[], T_Result],
        completion_tokens: typing.Callable[[], T_Result],
        ai_request_count: typing.Callable[[], T_Result],
        cost: typing.Callable[[], T_Result],
        llm_cache_embeddings_latency_average: typing.Callable[[], T_Result],
        llm_cache_fetch_latency_average: typing.Callable[[], T_Result],
        llm_latency_average: typing.Callable[[], T_Result],
        llm_embeddings_tokens: typing.Callable[[], T_Result],
        llm_embeddings_cost: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LlmMetricsItem.TOTAL_TOKENS:
            return total_tokens()
        if self is LlmMetricsItem.PROMPT_TOKENS:
            return prompt_tokens()
        if self is LlmMetricsItem.COMPLETION_TOKENS:
            return completion_tokens()
        if self is LlmMetricsItem.AI_REQUEST_COUNT:
            return ai_request_count()
        if self is LlmMetricsItem.COST:
            return cost()
        if self is LlmMetricsItem.LLM_CACHE_EMBEDDINGS_LATENCY_AVERAGE:
            return llm_cache_embeddings_latency_average()
        if self is LlmMetricsItem.LLM_CACHE_FETCH_LATENCY_AVERAGE:
            return llm_cache_fetch_latency_average()
        if self is LlmMetricsItem.LLM_LATENCY_AVERAGE:
            return llm_latency_average()
        if self is LlmMetricsItem.LLM_EMBEDDINGS_TOKENS:
            return llm_embeddings_tokens()
        if self is LlmMetricsItem.LLM_EMBEDDINGS_COST:
            return llm_embeddings_cost()
