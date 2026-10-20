

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RunsCancelStatus(enum.StrEnum):
    """
    Filter runs by status to cancel. Must be one of 'pending', 'running', or 'all'.
    """

    PENDING = "pending"
    RUNNING = "running"
    ALL = "all"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunsCancelStatus.PENDING:
            return pending()
        if self is RunsCancelStatus.RUNNING:
            return running()
        if self is RunsCancelStatus.ALL:
            return all_()
