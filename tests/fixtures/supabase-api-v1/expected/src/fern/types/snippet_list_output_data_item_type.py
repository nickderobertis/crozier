

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SnippetListOutputDataItemType(enum.StrEnum):
    SQL = "sql"

    def visit(self, sql: typing.Callable[[], T_Result]) -> T_Result:
        if self is SnippetListOutputDataItemType.SQL:
            return sql()
