

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValidateSqlCommandType(enum.StrEnum):
    VALIDATE_SQL = "validate-sql"

    def visit(self, validate_sql: typing.Callable[[], T_Result]) -> T_Result:
        if self is ValidateSqlCommandType.VALIDATE_SQL:
            return validate_sql()
