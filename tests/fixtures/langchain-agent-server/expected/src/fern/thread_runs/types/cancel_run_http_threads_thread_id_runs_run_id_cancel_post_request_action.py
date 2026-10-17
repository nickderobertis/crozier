

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction(enum.StrEnum):
    INTERRUPT = "interrupt"
    ROLLBACK = "rollback"

    def visit(self, interrupt: typing.Callable[[], T_Result], rollback: typing.Callable[[], T_Result]) -> T_Result:
        if self is CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction.INTERRUPT:
            return interrupt()
        if self is CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction.ROLLBACK:
            return rollback()
