

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateStudentRequestWithdrawalDateEstimatedOne(enum.StrEnum):
    EMPTY = ""

    def visit(self, empty: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateStudentRequestWithdrawalDateEstimatedOne.EMPTY:
            return empty()
