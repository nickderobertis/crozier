

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KnowledgeSourceSourceIdentifierDeleteError500ErrorCode(enum.StrEnum):
    DELETE_SOURCE_ERROR = "DELETE_SOURCE_ERROR"

    def visit(self, delete_source_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is KnowledgeSourceSourceIdentifierDeleteError500ErrorCode.DELETE_SOURCE_ERROR:
            return delete_source_error()
