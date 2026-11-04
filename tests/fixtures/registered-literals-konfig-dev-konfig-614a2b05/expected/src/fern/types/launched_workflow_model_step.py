

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LaunchedWorkflowModelStep(enum.StrEnum):
    """
    The step the workflow is currently on.
    """

    REVIEW = "Review"
    SIGN = "Sign"
    ARCHIVE = "Archive"
    COMPLETE = "Complete"

    def visit(
        self,
        review: typing.Callable[[], T_Result],
        sign: typing.Callable[[], T_Result],
        archive: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LaunchedWorkflowModelStep.REVIEW:
            return review()
        if self is LaunchedWorkflowModelStep.SIGN:
            return sign()
        if self is LaunchedWorkflowModelStep.ARCHIVE:
            return archive()
        if self is LaunchedWorkflowModelStep.COMPLETE:
            return complete()
