

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListSqlTablesCommandType(enum.StrEnum):
    LIST_SQL_TABLES = "list-sql-tables"

    def visit(self, list_sql_tables: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListSqlTablesCommandType.LIST_SQL_TABLES:
            return list_sql_tables()
