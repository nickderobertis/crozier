

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CallWindow(enum.StrEnum):
    EARLY = "early"
    STANDARD = "standard"
    LATE = "late"

    def visit(
        self,
        early: typing.Callable[[], T_Result],
        standard: typing.Callable[[], T_Result],
        late: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CallWindow.EARLY:
            return early()
        if self is CallWindow.STANDARD:
            return standard()
        if self is CallWindow.LATE:
            return late()
