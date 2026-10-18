

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1GetSecurityAdvisorsRequestLintType(enum.StrEnum):
    SQL = "sql"

    def visit(self, sql: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1GetSecurityAdvisorsRequestLintType.SQL:
            return sql()
