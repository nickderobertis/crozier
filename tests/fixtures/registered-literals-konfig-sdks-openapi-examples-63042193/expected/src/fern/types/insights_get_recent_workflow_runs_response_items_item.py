

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_recent_workflow_runs_response_items_item_status import (
    InsightsGetRecentWorkflowRunsResponseItemsItemStatus,
)


class InsightsGetRecentWorkflowRunsResponseItemsItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique ID of the workflow.
    """

    branch: str = pydantic.Field()
    """
    The VCS branch of a Workflow's trigger.
    """

    duration: int = pydantic.Field()
    """
    The duration in seconds of a run.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date and time the workflow was created.
    """

    stopped_at: dt.datetime = pydantic.Field()
    """
    The date and time the workflow stopped.
    """

    credits_used: int = pydantic.Field()
    """
    The number of credits used during execution. Note that Insights is not a real time financial reporting tool and should not be used for credit reporting.
    """

    status: InsightsGetRecentWorkflowRunsResponseItemsItemStatus = pydantic.Field()
    """
    Workflow status.
    """

    is_approval: bool = pydantic.Field()
    """
    Describes if the job is an approval job or not. Approval jobs are intermediary jobs that are created to pause the workflow until approved.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
