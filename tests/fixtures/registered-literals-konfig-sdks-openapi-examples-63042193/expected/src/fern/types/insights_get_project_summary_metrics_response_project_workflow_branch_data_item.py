

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_project_summary_metrics_response_project_workflow_branch_data_item_metrics import (
    InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics,
)
from .insights_get_project_summary_metrics_response_project_workflow_branch_data_item_trends import (
    InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemTrends,
)


class InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItem(UniversalBaseModel):
    workflow_name: str = pydantic.Field()
    """
    The name of the workflow.
    """

    branch: str = pydantic.Field()
    """
    The VCS branch of a workflow's trigger.
    """

    metrics: InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics = pydantic.Field()
    """
    Metrics aggregated across a workflow or branchfor a project.
    """

    trends: InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemTrends = pydantic.Field()
    """
    Trends aggregated across a workflow or branch for a project.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
