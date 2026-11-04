

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_project_workflow_job_metrics_response_items_item_metrics_duration_metrics import (
    InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetricsDurationMetrics,
)


class InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics(UniversalBaseModel):
    """
    Metrics relating to a workflow job's runs.
    """

    total_runs: int = pydantic.Field()
    """
    The total number of runs, including runs that are still on-hold or running.
    """

    failed_runs: int = pydantic.Field()
    """
    The number of failed runs.
    """

    successful_runs: int = pydantic.Field()
    """
    The number of successful runs.
    """

    duration_metrics: InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetricsDurationMetrics = pydantic.Field()
    """
    Metrics relating to the duration of runs for a workflow job.
    """

    success_rate: float
    total_credits_used: int = pydantic.Field()
    """
    The total credits consumed by the job in the aggregation window. Note that Insights is not a real time financial reporting tool and should not be used for credit reporting.
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
