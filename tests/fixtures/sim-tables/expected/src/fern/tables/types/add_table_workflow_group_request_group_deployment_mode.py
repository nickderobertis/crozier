

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AddTableWorkflowGroupRequestGroupDeploymentMode(enum.StrEnum):
    """
    Workflow state used for cell runs.
    """

    LIVE = "live"
    DEPLOYED = "deployed"

    def visit(self, live: typing.Callable[[], T_Result], deployed: typing.Callable[[], T_Result]) -> T_Result:
        if self is AddTableWorkflowGroupRequestGroupDeploymentMode.LIVE:
            return live()
        if self is AddTableWorkflowGroupRequestGroupDeploymentMode.DEPLOYED:
            return deployed()
