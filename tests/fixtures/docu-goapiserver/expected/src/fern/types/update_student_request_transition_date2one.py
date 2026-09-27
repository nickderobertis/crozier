

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateStudentRequestTransitionDate2One(enum.StrEnum):
    EMPTY = ""

    def visit(self, empty: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateStudentRequestTransitionDate2One.EMPTY:
            return empty()
