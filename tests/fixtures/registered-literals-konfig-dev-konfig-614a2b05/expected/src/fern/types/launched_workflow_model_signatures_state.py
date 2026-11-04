

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LaunchedWorkflowModelSignaturesState(enum.StrEnum):
    """
    The state of the signatures.
    """

    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETE = "complete"
    NOT_APPLICABLE = "not_applicable"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        not_applicable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LaunchedWorkflowModelSignaturesState.NOT_STARTED:
            return not_started()
        if self is LaunchedWorkflowModelSignaturesState.IN_PROGRESS:
            return in_progress()
        if self is LaunchedWorkflowModelSignaturesState.COMPLETE:
            return complete()
        if self is LaunchedWorkflowModelSignaturesState.NOT_APPLICABLE:
            return not_applicable()
