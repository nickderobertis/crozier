

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BackgroundTaskStatus(enum.StrEnum):
    RUNNING = "running"

    def visit(self, running: typing.Callable[[], T_Result]) -> T_Result:
        if self is BackgroundTaskStatus.RUNNING:
            return running()
