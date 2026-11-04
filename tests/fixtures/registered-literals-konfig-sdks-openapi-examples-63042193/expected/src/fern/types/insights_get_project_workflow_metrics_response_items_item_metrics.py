

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_project_workflow_metrics_response_items_item_metrics_duration_metrics import (
    InsightsGetProjectWorkflowMetricsResponseItemsItemMetricsDurationMetrics,
)


class InsightsGetProjectWorkflowMetricsResponseItemsItemMetrics(UniversalBaseModel):
    """
    Metrics relating to a workflow's runs.
    """

    total_runs: int = pydantic.Field()
    """
    The total number of runs, including runs that are still on-hold or running.
    """

    successful_runs: int = pydantic.Field()
    """
    The number of successful runs.
    """

    mttr: int = pydantic.Field()
    """
    The mean time to recovery (mean time between failures and their next success) in seconds.
    """

    total_credits_used: int = pydantic.Field()
    """
    The total credits consumed by the workflow in the aggregation window. Note that Insights is not a real time financial reporting tool and should not be used for credit reporting.
    """

    failed_runs: int = pydantic.Field()
    """
    The number of failed runs.
    """

    success_rate: float
    duration_metrics: InsightsGetProjectWorkflowMetricsResponseItemsItemMetricsDurationMetrics = pydantic.Field()
    """
    Metrics relating to the duration of runs for a workflow.
    """

    total_recoveries: int = pydantic.Field()
    """
    The number of recovered workflow executions per day.
    """

    throughput: float = pydantic.Field()
    """
    The average number of runs per day.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
