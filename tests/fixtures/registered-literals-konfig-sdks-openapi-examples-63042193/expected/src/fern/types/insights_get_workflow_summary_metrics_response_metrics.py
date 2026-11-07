

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_workflow_summary_metrics_response_metrics_duration_metrics import (
    InsightsGetWorkflowSummaryMetricsResponseMetricsDurationMetrics,
)


class InsightsGetWorkflowSummaryMetricsResponseMetrics(UniversalBaseModel):
    """
    Metrics aggregated across a workflow for a given time window.
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
    completed_runs: int = pydantic.Field()
    """
    The number of runs that ran to completion within the aggregation window
    """

    window_start: dt.datetime = pydantic.Field()
    """
    The timestamp of the first build within the requested reporting window.
    """

    duration_metrics: InsightsGetWorkflowSummaryMetricsResponseMetricsDurationMetrics = pydantic.Field()
    """
    Metrics relating to the duration of runs for a workflow.
    """

    window_end: dt.datetime = pydantic.Field()
    """
    The timestamp of the last build within the requested reporting window.
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
