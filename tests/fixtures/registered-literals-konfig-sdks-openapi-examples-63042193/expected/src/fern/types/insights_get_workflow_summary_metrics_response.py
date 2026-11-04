

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_workflow_summary_metrics_response_metrics import InsightsGetWorkflowSummaryMetricsResponseMetrics
from .insights_get_workflow_summary_metrics_response_trends import InsightsGetWorkflowSummaryMetricsResponseTrends


class InsightsGetWorkflowSummaryMetricsResponse(UniversalBaseModel):
    """
    Workflow level aggregated metrics and trends response
    """

    metrics: InsightsGetWorkflowSummaryMetricsResponseMetrics = pydantic.Field()
    """
    Metrics aggregated across a workflow for a given time window.
    """

    trends: InsightsGetWorkflowSummaryMetricsResponseTrends = pydantic.Field()
    """
    Trends for aggregated metrics across a workflow for a given time window.
    """

    workflow_names: typing.List[str] = pydantic.Field()
    """
    A list of all the workflow names for a given project.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
