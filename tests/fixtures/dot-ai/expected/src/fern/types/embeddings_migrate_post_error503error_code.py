

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbeddingsMigratePostError503ErrorCode(enum.StrEnum):
    EMBEDDING_SERVICE_UNAVAILABLE = "EMBEDDING_SERVICE_UNAVAILABLE"
    PLUGIN_UNAVAILABLE = "PLUGIN_UNAVAILABLE"

    def visit(
        self,
        embedding_service_unavailable: typing.Callable[[], T_Result],
        plugin_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmbeddingsMigratePostError503ErrorCode.EMBEDDING_SERVICE_UNAVAILABLE:
            return embedding_service_unavailable()
        if self is EmbeddingsMigratePostError503ErrorCode.PLUGIN_UNAVAILABLE:
            return plugin_unavailable()
