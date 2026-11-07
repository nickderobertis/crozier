

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_project_summary_metrics_response_project_data_metrics import (
    InsightsGetProjectSummaryMetricsResponseProjectDataMetrics,
)
from .insights_get_project_summary_metrics_response_project_data_trends import (
    InsightsGetProjectSummaryMetricsResponseProjectDataTrends,
)


class InsightsGetProjectSummaryMetricsResponseProjectData(UniversalBaseModel):
    """
    Metrics and trends data aggregated for a given project.
    """

    metrics: InsightsGetProjectSummaryMetricsResponseProjectDataMetrics = pydantic.Field()
    """
    Metrics aggregated across all workflows and branches for a project.
    """

    trends: InsightsGetProjectSummaryMetricsResponseProjectDataTrends = pydantic.Field()
    """
    Metric trends aggregated across all workflows and branches for a project.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
