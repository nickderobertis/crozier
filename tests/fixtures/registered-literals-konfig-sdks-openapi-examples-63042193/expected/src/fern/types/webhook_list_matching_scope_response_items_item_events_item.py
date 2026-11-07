

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookListMatchingScopeResponseItemsItemEventsItem(enum.StrEnum):
    WORKFLOW_COMPLETED = "workflow-completed"
    JOB_COMPLETED = "job-completed"

    def visit(
        self, workflow_completed: typing.Callable[[], T_Result], job_completed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is WebhookListMatchingScopeResponseItemsItemEventsItem.WORKFLOW_COMPLETED:
            return workflow_completed()
        if self is WebhookListMatchingScopeResponseItemsItemEventsItem.JOB_COMPLETED:
            return job_completed()
