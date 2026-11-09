

import typing

LlmMetricsItem = typing.Union[
    typing.Literal[
        "total_tokens",
        "prompt_tokens",
        "completion_tokens",
        "ai_request_count",
        "cost",
        "llm_cache_embeddings_latency_average",
        "llm_cache_fetch_latency_average",
        "llm_latency_average",
        "llm_embeddings_tokens",
        "llm_embeddings_cost",
    ],
    typing.Any,
]
