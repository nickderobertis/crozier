

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2LogListItemKind(enum.StrEnum):
    """
    Whether the run executed a workflow or a Chat / Sim-agent job. Job runs appear only when `includeJobRuns=true`.
    """

    WORKFLOW = "workflow"
    JOB = "job"

    def visit(self, workflow: typing.Callable[[], T_Result], job: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2LogListItemKind.WORKFLOW:
            return workflow()
        if self is V2LogListItemKind.JOB:
            return job()
