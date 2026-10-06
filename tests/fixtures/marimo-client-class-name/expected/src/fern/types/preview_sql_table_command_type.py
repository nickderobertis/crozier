

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreviewSqlTableCommandType(enum.StrEnum):
    PREVIEW_SQL_TABLE = "preview-sql-table"

    def visit(self, preview_sql_table: typing.Callable[[], T_Result]) -> T_Result:
        if self is PreviewSqlTableCommandType.PREVIEW_SQL_TABLE:
            return preview_sql_table()
