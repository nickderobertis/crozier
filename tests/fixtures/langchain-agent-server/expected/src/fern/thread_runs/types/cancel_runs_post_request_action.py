

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CancelRunsPostRequestAction(enum.StrEnum):
    INTERRUPT = "interrupt"
    ROLLBACK = "rollback"

    def visit(self, interrupt: typing.Callable[[], T_Result], rollback: typing.Callable[[], T_Result]) -> T_Result:
        if self is CancelRunsPostRequestAction.INTERRUPT:
            return interrupt()
        if self is CancelRunsPostRequestAction.ROLLBACK:
            return rollback()
