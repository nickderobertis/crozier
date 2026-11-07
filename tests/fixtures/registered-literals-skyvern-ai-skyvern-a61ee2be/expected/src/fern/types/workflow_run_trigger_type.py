

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowRunTriggerType(enum.StrEnum):
    """
    How a workflow run was initiated.

    - manual: User clicked "Run" in the UI
    - mcp: First-party MCP client request
    - api: Direct API call to the run endpoint
    - scheduled: Triggered by a cron schedule
    - webhook: Triggered by an external system via the webhook endpoint
    """

    MANUAL = "manual"
    MCP = "mcp"
    API = "api"
    SCHEDULED = "scheduled"
    WEBHOOK = "webhook"

    def visit(
        self,
        manual: typing.Callable[[], T_Result],
        mcp: typing.Callable[[], T_Result],
        api: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        webhook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowRunTriggerType.MANUAL:
            return manual()
        if self is WorkflowRunTriggerType.MCP:
            return mcp()
        if self is WorkflowRunTriggerType.API:
            return api()
        if self is WorkflowRunTriggerType.SCHEDULED:
            return scheduled()
        if self is WorkflowRunTriggerType.WEBHOOK:
            return webhook()
