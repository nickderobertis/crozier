

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SnippetResponseOutputType(enum.StrEnum):
    SQL = "sql"

    def visit(self, sql: typing.Callable[[], T_Result]) -> T_Result:
        if self is SnippetResponseOutputType.SQL:
            return sql()
