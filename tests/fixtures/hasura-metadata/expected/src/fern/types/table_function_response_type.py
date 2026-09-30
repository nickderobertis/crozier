

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TableFunctionResponseType(enum.StrEnum):
    TABLE = "table"

    def visit(self, table: typing.Callable[[], T_Result]) -> T_Result:
        if self is TableFunctionResponseType.TABLE:
            return table()
