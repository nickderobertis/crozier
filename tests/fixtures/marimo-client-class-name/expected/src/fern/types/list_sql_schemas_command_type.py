

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListSqlSchemasCommandType(enum.StrEnum):
    LIST_SQL_SCHEMAS = "list-sql-schemas"

    def visit(self, list_sql_schemas: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListSqlSchemasCommandType.LIST_SQL_SCHEMAS:
            return list_sql_schemas()
