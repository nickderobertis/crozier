

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InsightsGetProjectSummaryMetricsResponseProjectDataTrends(UniversalBaseModel):
    """
    Metric trends aggregated across all workflows and branches for a project.
    """

    total_runs: float = pydantic.Field()
    """
    The trend value for total number of runs.
    """

    total_duration_secs: float = pydantic.Field()
    """
    Trend value for total duration.
    """

    total_credits_used: float = pydantic.Field()
    """
    The trend value for total credits consumed.
    """

    success_rate: float = pydantic.Field()
    """
    The trend value for the success rate.
    """

    throughput: float = pydantic.Field()
    """
    Trend value for the average number of runs per day.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
