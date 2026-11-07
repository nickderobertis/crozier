

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowGetJobsResponseItemsItemType(enum.StrEnum):
    """
    The type of job.
    """

    BUILD = "build"
    APPROVAL = "approval"

    def visit(self, build: typing.Callable[[], T_Result], approval: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkflowGetJobsResponseItemsItemType.BUILD:
            return build()
        if self is WorkflowGetJobsResponseItemsItemType.APPROVAL:
            return approval()
