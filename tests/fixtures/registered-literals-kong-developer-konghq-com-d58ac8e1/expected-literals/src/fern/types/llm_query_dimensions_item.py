

import typing

LlmQueryDimensionsItem = typing.Union[
    typing.Literal[
        "control_plane",
        "control_plane_group",
        "gateway_service",
        "consumer",
        "application",
        "route",
        "ai_provider",
        "ai_response_model",
        "ai_request_model",
        "llm_cache_status",
        "llm_embeddings_provider",
        "llm_embeddings_model",
        "time",
        "realm",
        "status_code",
        "status_code_grouped",
        "ai_plugin",
    ],
    typing.Any,
]
