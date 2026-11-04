

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_summary_metrics_with_trends_response_org_data_metrics import (
    InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics,
)
from .insights_get_summary_metrics_with_trends_response_org_data_trends import (
    InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends,
)


class InsightsGetSummaryMetricsWithTrendsResponseOrgData(UniversalBaseModel):
    """
    Aggregated metrics for an org, with trends.
    """

    metrics: InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics = pydantic.Field()
    """
    Metrics for a single org metrics.
    """

    trends: InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends = pydantic.Field()
    """
    Trends for a single org.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
