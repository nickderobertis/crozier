

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_job_timeseries_data_response_items_item_metrics_duration_metrics import (
    InsightsGetJobTimeseriesDataResponseItemsItemMetricsDurationMetrics,
)


class InsightsGetJobTimeseriesDataResponseItemsItemMetrics(UniversalBaseModel):
    """
    Metrics relating to a workflow's runs.
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

    throughput: float = pydantic.Field()
    """
    The average number of runs per day.
    """

    median_credits_used: int = pydantic.Field()
    """
    The median credits consumed over the current timeseries interval.
    """

    total_credits_used: int = pydantic.Field()
    """
    The total credits consumed over the current timeseries interval.
    """

    duration_metrics: InsightsGetJobTimeseriesDataResponseItemsItemMetricsDurationMetrics = pydantic.Field()
    """
    Metrics relating to the duration of runs for a workflow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
