

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowObjectDeactivated(enum.StrEnum):
    """
    Indicates why the workflow was deactivated.
    """

    ABORTED = "ABORTED"
    FINISHED = "FINISHED"

    def visit(self, aborted: typing.Callable[[], T_Result], finished: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkflowObjectDeactivated.ABORTED:
            return aborted()
        if self is WorkflowObjectDeactivated.FINISHED:
            return finished()
