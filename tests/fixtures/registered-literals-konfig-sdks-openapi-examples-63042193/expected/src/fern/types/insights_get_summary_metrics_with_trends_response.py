

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_summary_metrics_with_trends_response_org_data import (
    InsightsGetSummaryMetricsWithTrendsResponseOrgData,
)
from .insights_get_summary_metrics_with_trends_response_org_project_data_item import (
    InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItem,
)


class InsightsGetSummaryMetricsWithTrendsResponse(UniversalBaseModel):
    """
    Summary metrics with trends for the entire org, and for each project.
    """

    org_data: InsightsGetSummaryMetricsWithTrendsResponseOrgData = pydantic.Field()
    """
    Aggregated metrics for an org, with trends.
    """

    org_project_data: typing.List[InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItem] = pydantic.Field()
    """
    Metrics for a single project, across all branches
    """

    all_projects: typing.List[str] = pydantic.Field()
    """
    A list of all the project names in the organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
