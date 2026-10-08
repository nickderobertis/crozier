

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SqlTablePreviewNotificationOp(enum.StrEnum):
    SQL_TABLE_PREVIEW = "sql-table-preview"

    def visit(self, sql_table_preview: typing.Callable[[], T_Result]) -> T_Result:
        if self is SqlTablePreviewNotificationOp.SQL_TABLE_PREVIEW:
            return sql_table_preview()
