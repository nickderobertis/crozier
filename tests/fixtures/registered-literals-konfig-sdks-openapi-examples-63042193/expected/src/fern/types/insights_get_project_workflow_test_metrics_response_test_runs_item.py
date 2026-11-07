

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_project_workflow_test_metrics_response_test_runs_item_test_counts import (
    InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts,
)


class InsightsGetProjectWorkflowTestMetricsResponseTestRunsItem(UniversalBaseModel):
    pipeline_number: int = pydantic.Field()
    """
    The number of the pipeline associated with the provided test counts
    """

    workflow_id: typing.Any
    success_rate: float = pydantic.Field()
    """
    The success rate calculated from test counts
    """

    test_counts: InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts = pydantic.Field()
    """
    Test counts for a given pipeline number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
