

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableWorkflowGroupDeploymentMode(enum.StrEnum):
    """
    Workflow execution mode.
    """

    LIVE = "live"
    DEPLOYED = "deployed"

    def visit(self, live: typing.Callable[[], T_Result], deployed: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2TableWorkflowGroupDeploymentMode.LIVE:
            return live()
        if self is V2TableWorkflowGroupDeploymentMode.DEPLOYED:
            return deployed()
