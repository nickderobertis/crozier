

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateTableWorkflowGroupRequestDeploymentMode(enum.StrEnum):
    """
    Replacement workflow execution mode.
    """

    LIVE = "live"
    DEPLOYED = "deployed"

    def visit(self, live: typing.Callable[[], T_Result], deployed: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateTableWorkflowGroupRequestDeploymentMode.LIVE:
            return live()
        if self is UpdateTableWorkflowGroupRequestDeploymentMode.DEPLOYED:
            return deployed()
