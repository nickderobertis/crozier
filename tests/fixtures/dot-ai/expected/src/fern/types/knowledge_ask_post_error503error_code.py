

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KnowledgeAskPostError503ErrorCode(enum.StrEnum):
    AI_NOT_CONFIGURED = "AI_NOT_CONFIGURED"
    PLUGIN_UNAVAILABLE = "PLUGIN_UNAVAILABLE"
    VECTOR_DB_UNAVAILABLE = "VECTOR_DB_UNAVAILABLE"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"

    def visit(
        self,
        ai_not_configured: typing.Callable[[], T_Result],
        plugin_unavailable: typing.Callable[[], T_Result],
        vector_db_unavailable: typing.Callable[[], T_Result],
        service_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KnowledgeAskPostError503ErrorCode.AI_NOT_CONFIGURED:
            return ai_not_configured()
        if self is KnowledgeAskPostError503ErrorCode.PLUGIN_UNAVAILABLE:
            return plugin_unavailable()
        if self is KnowledgeAskPostError503ErrorCode.VECTOR_DB_UNAVAILABLE:
            return vector_db_unavailable()
        if self is KnowledgeAskPostError503ErrorCode.SERVICE_UNAVAILABLE:
            return service_unavailable()
