

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemMetrics(UniversalBaseModel):
    """
    Metrics for a single project, across all branches.
    """

    total_credits_used: int = pydantic.Field()
    """
    The total credits consumed over the current timeseries interval.
    """

    total_duration_secs: int = pydantic.Field()
    """
    Total duration, in seconds.
    """

    total_runs: int = pydantic.Field()
    """
    The total number of runs, including runs that are still on-hold or running.
    """

    success_rate: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
