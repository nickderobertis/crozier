

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatementType(enum.StrEnum):
    """
    The data type.
    """

    STATEMENT = "statement"

    def visit(self, statement: typing.Callable[[], T_Result]) -> T_Result:
        if self is StatementType.STATEMENT:
            return statement()
