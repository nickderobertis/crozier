

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemTrends(UniversalBaseModel):
    """
    Trends for a single project, across all branches.
    """

    total_credits_used: float = pydantic.Field()
    """
    The trend value for total credits consumed.
    """

    total_duration_secs: float = pydantic.Field()
    """
    Trend value for total duration.
    """

    total_runs: float = pydantic.Field()
    """
    The trend value for total number of runs.
    """

    success_rate: float = pydantic.Field()
    """
    The trend value for the success rate.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
