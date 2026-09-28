

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTableDispatchRequestLimitType(enum.StrEnum):
    """
    Unit constrained by the run cap.
    """

    ROWS = "rows"

    def visit(self, rows: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateTableDispatchRequestLimitType.ROWS:
            return rows()
