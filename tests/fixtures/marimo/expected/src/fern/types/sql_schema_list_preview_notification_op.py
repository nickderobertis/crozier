

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SqlSchemaListPreviewNotificationOp(enum.StrEnum):
    SQL_SCHEMA_LIST_PREVIEW = "sql-schema-list-preview"

    def visit(self, sql_schema_list_preview: typing.Callable[[], T_Result]) -> T_Result:
        if self is SqlSchemaListPreviewNotificationOp.SQL_SCHEMA_LIST_PREVIEW:
            return sql_schema_list_preview()
