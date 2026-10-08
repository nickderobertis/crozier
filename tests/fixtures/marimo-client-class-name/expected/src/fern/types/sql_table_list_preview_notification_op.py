

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SqlTableListPreviewNotificationOp(enum.StrEnum):
    SQL_TABLE_LIST_PREVIEW = "sql-table-list-preview"

    def visit(self, sql_table_list_preview: typing.Callable[[], T_Result]) -> T_Result:
        if self is SqlTableListPreviewNotificationOp.SQL_TABLE_LIST_PREVIEW:
            return sql_table_list_preview()
