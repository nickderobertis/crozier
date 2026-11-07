

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_project_summary_metrics_response_project_data import (
    InsightsGetProjectSummaryMetricsResponseProjectData,
)
from .insights_get_project_summary_metrics_response_project_workflow_branch_data_item import (
    InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItem,
)
from .insights_get_project_summary_metrics_response_project_workflow_data_item import (
    InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem,
)


class InsightsGetProjectSummaryMetricsResponse(UniversalBaseModel):
    org_id: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The unique ID of the organization
    """

    project_id: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The unique ID of the project
    """

    project_data: typing.Optional[InsightsGetProjectSummaryMetricsResponseProjectData] = pydantic.Field(default=None)
    """
    Metrics and trends data aggregated for a given project.
    """

    project_workflow_data: typing.Optional[
        typing.List[InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem]
    ] = pydantic.Field(default=None)
    """
    A list of metrics and trends data for workflows for a given project.
    """

    project_workflow_branch_data: typing.Optional[
        typing.List[InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItem]
    ] = pydantic.Field(default=None)
    """
    A list of metrics and trends data for branches for a given project.
    """

    all_branches: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of all the branches for a given project.
    """

    all_workflows: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of all the workflows for a given project.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
