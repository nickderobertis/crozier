

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompletedRunNotificationOp(enum.StrEnum):
    COMPLETED_RUN = "completed-run"

    def visit(self, completed_run: typing.Callable[[], T_Result]) -> T_Result:
        if self is CompletedRunNotificationOp.COMPLETED_RUN:
            return completed_run()
