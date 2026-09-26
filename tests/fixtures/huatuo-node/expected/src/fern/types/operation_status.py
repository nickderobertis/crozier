

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OperationStatus(enum.StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    STOPPING = "stopping"
    TERMINAL = "terminal"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        stopping: typing.Callable[[], T_Result],
        terminal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OperationStatus.PENDING:
            return pending()
        if self is OperationStatus.RUNNING:
            return running()
        if self is OperationStatus.STOPPING:
            return stopping()
        if self is OperationStatus.TERMINAL:
            return terminal()
