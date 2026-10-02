

import typing

ResourcesSearchGetError500ErrorCode = typing.Union[
    typing.Literal[
        "INTERNAL_ERROR",
        "DISCOVERY_ERROR",
        "EXECUTION_ERROR",
        "OPENAPI_ERROR",
        "SYNC_ERROR",
        "RESOURCE_KINDS_ERROR",
        "SEARCH_ERROR",
        "LIST_RESOURCES_ERROR",
        "NAMESPACES_ERROR",
        "RESOURCE_ERROR",
        "EVENTS_ERROR",
        "LOGS_ERROR",
        "PROMPTS_LIST_ERROR",
        "PROMPT_GET_ERROR",
        "VISUALIZATION_ERROR",
        "SESSION_RETRIEVAL_ERROR",
        "MIGRATION_ERROR",
        "PROMPTS_CACHE_REFRESH_ERROR",
        "PROMPTS_SOURCE_INGEST_ERROR",
        "USER_MANAGEMENT_ERROR",
    ],
    typing.Any,
]
