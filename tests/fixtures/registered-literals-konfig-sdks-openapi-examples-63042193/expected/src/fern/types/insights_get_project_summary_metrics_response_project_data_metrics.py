

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InsightsGetProjectSummaryMetricsResponseProjectDataMetrics(UniversalBaseModel):
    """
    Metrics aggregated across all workflows and branches for a project.
    """

    total_runs: int = pydantic.Field()
    """
    The total number of runs, including runs that are still on-hold or running.
    """

    total_duration_secs: int = pydantic.Field()
    """
    Total duration, in seconds.
    """

    total_credits_used: int = pydantic.Field()
    """
    The total credits consumed over the current timeseries interval.
    """

    success_rate: float
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
