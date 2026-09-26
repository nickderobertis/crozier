

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbeddingsMigratePostError500ErrorCode(enum.StrEnum):
    MIGRATION_ERROR = "MIGRATION_ERROR"

    def visit(self, migration_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmbeddingsMigratePostError500ErrorCode.MIGRATION_ERROR:
            return migration_error()
