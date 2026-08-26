

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValidateSqlResultNotificationOp(enum.StrEnum):
    VALIDATE_SQL_RESULT = "validate-sql-result"

    def visit(self, validate_sql_result: typing.Callable[[], T_Result]) -> T_Result:
        if self is ValidateSqlResultNotificationOp.VALIDATE_SQL_RESULT:
            return validate_sql_result()
