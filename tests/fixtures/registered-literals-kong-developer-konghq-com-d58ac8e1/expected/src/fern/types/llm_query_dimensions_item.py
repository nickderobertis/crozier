

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LlmQueryDimensionsItem(enum.StrEnum):
    CONTROL_PLANE = "control_plane"
    CONTROL_PLANE_GROUP = "control_plane_group"
    GATEWAY_SERVICE = "gateway_service"
    CONSUMER = "consumer"
    APPLICATION = "application"
    ROUTE = "route"
    AI_PROVIDER = "ai_provider"
    AI_RESPONSE_MODEL = "ai_response_model"
    AI_REQUEST_MODEL = "ai_request_model"
    LLM_CACHE_STATUS = "llm_cache_status"
    LLM_EMBEDDINGS_PROVIDER = "llm_embeddings_provider"
    LLM_EMBEDDINGS_MODEL = "llm_embeddings_model"
    TIME = "time"
    REALM = "realm"
    STATUS_CODE = "status_code"
    STATUS_CODE_GROUPED = "status_code_grouped"
    AI_PLUGIN = "ai_plugin"

    def visit(
        self,
        control_plane: typing.Callable[[], T_Result],
        control_plane_group: typing.Callable[[], T_Result],
        gateway_service: typing.Callable[[], T_Result],
        consumer: typing.Callable[[], T_Result],
        application: typing.Callable[[], T_Result],
        route: typing.Callable[[], T_Result],
        ai_provider: typing.Callable[[], T_Result],
        ai_response_model: typing.Callable[[], T_Result],
        ai_request_model: typing.Callable[[], T_Result],
        llm_cache_status: typing.Callable[[], T_Result],
        llm_embeddings_provider: typing.Callable[[], T_Result],
        llm_embeddings_model: typing.Callable[[], T_Result],
        time: typing.Callable[[], T_Result],
        realm: typing.Callable[[], T_Result],
        status_code: typing.Callable[[], T_Result],
        status_code_grouped: typing.Callable[[], T_Result],
        ai_plugin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LlmQueryDimensionsItem.CONTROL_PLANE:
            return control_plane()
        if self is LlmQueryDimensionsItem.CONTROL_PLANE_GROUP:
            return control_plane_group()
        if self is LlmQueryDimensionsItem.GATEWAY_SERVICE:
            return gateway_service()
        if self is LlmQueryDimensionsItem.CONSUMER:
            return consumer()
        if self is LlmQueryDimensionsItem.APPLICATION:
            return application()
        if self is LlmQueryDimensionsItem.ROUTE:
            return route()
        if self is LlmQueryDimensionsItem.AI_PROVIDER:
            return ai_provider()
        if self is LlmQueryDimensionsItem.AI_RESPONSE_MODEL:
            return ai_response_model()
        if self is LlmQueryDimensionsItem.AI_REQUEST_MODEL:
            return ai_request_model()
        if self is LlmQueryDimensionsItem.LLM_CACHE_STATUS:
            return llm_cache_status()
        if self is LlmQueryDimensionsItem.LLM_EMBEDDINGS_PROVIDER:
            return llm_embeddings_provider()
        if self is LlmQueryDimensionsItem.LLM_EMBEDDINGS_MODEL:
            return llm_embeddings_model()
        if self is LlmQueryDimensionsItem.TIME:
            return time()
        if self is LlmQueryDimensionsItem.REALM:
            return realm()
        if self is LlmQueryDimensionsItem.STATUS_CODE:
            return status_code()
        if self is LlmQueryDimensionsItem.STATUS_CODE_GROUPED:
            return status_code_grouped()
        if self is LlmQueryDimensionsItem.AI_PLUGIN:
            return ai_plugin()
