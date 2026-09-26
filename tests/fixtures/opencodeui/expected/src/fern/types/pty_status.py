

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PtyStatus(enum.StrEnum):
    RUNNING = "running"
    EXITED = "exited"

    def visit(self, running: typing.Callable[[], T_Result], exited: typing.Callable[[], T_Result]) -> T_Result:
        if self is PtyStatus.RUNNING:
            return running()
        if self is PtyStatus.EXITED:
            return exited()
