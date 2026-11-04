

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_summary_metrics_with_trends_response_org_project_data_item_metrics import (
    InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemMetrics,
)
from .insights_get_summary_metrics_with_trends_response_org_project_data_item_trends import (
    InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemTrends,
)


class InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItem(UniversalBaseModel):
    project_name: str = pydantic.Field()
    """
    The name of the project.
    """

    metrics: InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemMetrics = pydantic.Field()
    """
    Metrics for a single project, across all branches.
    """

    trends: InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItemTrends = pydantic.Field()
    """
    Trends for a single project, across all branches.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
