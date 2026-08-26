

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoSqlErrorType(enum.StrEnum):
    SQL_ERROR = "sql-error"

    def visit(self, sql_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoSqlErrorType.SQL_ERROR:
            return sql_error()
