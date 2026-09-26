

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViolationOutSeverity(enum.StrEnum):
    HARD_BLOCK = "hard_block"
    WARNING = "warning"
    ADVISORY = "advisory"

    def visit(
        self,
        hard_block: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        advisory: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ViolationOutSeverity.HARD_BLOCK:
            return hard_block()
        if self is ViolationOutSeverity.WARNING:
            return warning()
        if self is ViolationOutSeverity.ADVISORY:
            return advisory()
