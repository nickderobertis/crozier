

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptsGetError500ErrorCode(enum.StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"
    DISCOVERY_ERROR = "DISCOVERY_ERROR"
    EXECUTION_ERROR = "EXECUTION_ERROR"
    OPENAPI_ERROR = "OPENAPI_ERROR"
    SYNC_ERROR = "SYNC_ERROR"
    RESOURCE_KINDS_ERROR = "RESOURCE_KINDS_ERROR"
    SEARCH_ERROR = "SEARCH_ERROR"
    LIST_RESOURCES_ERROR = "LIST_RESOURCES_ERROR"
    NAMESPACES_ERROR = "NAMESPACES_ERROR"
    RESOURCE_ERROR = "RESOURCE_ERROR"
    EVENTS_ERROR = "EVENTS_ERROR"
    LOGS_ERROR = "LOGS_ERROR"
    PROMPTS_LIST_ERROR = "PROMPTS_LIST_ERROR"
    PROMPT_GET_ERROR = "PROMPT_GET_ERROR"
    VISUALIZATION_ERROR = "VISUALIZATION_ERROR"
    SESSION_RETRIEVAL_ERROR = "SESSION_RETRIEVAL_ERROR"
    MIGRATION_ERROR = "MIGRATION_ERROR"
    PROMPTS_CACHE_REFRESH_ERROR = "PROMPTS_CACHE_REFRESH_ERROR"
    PROMPTS_SOURCE_INGEST_ERROR = "PROMPTS_SOURCE_INGEST_ERROR"
    USER_MANAGEMENT_ERROR = "USER_MANAGEMENT_ERROR"

    def visit(
        self,
        internal_error: typing.Callable[[], T_Result],
        discovery_error: typing.Callable[[], T_Result],
        execution_error: typing.Callable[[], T_Result],
        openapi_error: typing.Callable[[], T_Result],
        sync_error: typing.Callable[[], T_Result],
        resource_kinds_error: typing.Callable[[], T_Result],
        search_error: typing.Callable[[], T_Result],
        list_resources_error: typing.Callable[[], T_Result],
        namespaces_error: typing.Callable[[], T_Result],
        resource_error: typing.Callable[[], T_Result],
        events_error: typing.Callable[[], T_Result],
        logs_error: typing.Callable[[], T_Result],
        prompts_list_error: typing.Callable[[], T_Result],
        prompt_get_error: typing.Callable[[], T_Result],
        visualization_error: typing.Callable[[], T_Result],
        session_retrieval_error: typing.Callable[[], T_Result],
        migration_error: typing.Callable[[], T_Result],
        prompts_cache_refresh_error: typing.Callable[[], T_Result],
        prompts_source_ingest_error: typing.Callable[[], T_Result],
        user_management_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PromptsGetError500ErrorCode.INTERNAL_ERROR:
            return internal_error()
        if self is PromptsGetError500ErrorCode.DISCOVERY_ERROR:
            return discovery_error()
        if self is PromptsGetError500ErrorCode.EXECUTION_ERROR:
            return execution_error()
        if self is PromptsGetError500ErrorCode.OPENAPI_ERROR:
            return openapi_error()
        if self is PromptsGetError500ErrorCode.SYNC_ERROR:
            return sync_error()
        if self is PromptsGetError500ErrorCode.RESOURCE_KINDS_ERROR:
            return resource_kinds_error()
        if self is PromptsGetError500ErrorCode.SEARCH_ERROR:
            return search_error()
        if self is PromptsGetError500ErrorCode.LIST_RESOURCES_ERROR:
            return list_resources_error()
        if self is PromptsGetError500ErrorCode.NAMESPACES_ERROR:
            return namespaces_error()
        if self is PromptsGetError500ErrorCode.RESOURCE_ERROR:
            return resource_error()
        if self is PromptsGetError500ErrorCode.EVENTS_ERROR:
            return events_error()
        if self is PromptsGetError500ErrorCode.LOGS_ERROR:
            return logs_error()
        if self is PromptsGetError500ErrorCode.PROMPTS_LIST_ERROR:
            return prompts_list_error()
        if self is PromptsGetError500ErrorCode.PROMPT_GET_ERROR:
            return prompt_get_error()
        if self is PromptsGetError500ErrorCode.VISUALIZATION_ERROR:
            return visualization_error()
        if self is PromptsGetError500ErrorCode.SESSION_RETRIEVAL_ERROR:
            return session_retrieval_error()
        if self is PromptsGetError500ErrorCode.MIGRATION_ERROR:
            return migration_error()
        if self is PromptsGetError500ErrorCode.PROMPTS_CACHE_REFRESH_ERROR:
            return prompts_cache_refresh_error()
        if self is PromptsGetError500ErrorCode.PROMPTS_SOURCE_INGEST_ERROR:
            return prompts_source_ingest_error()
        if self is PromptsGetError500ErrorCode.USER_MANAGEMENT_ERROR:
            return user_management_error()
