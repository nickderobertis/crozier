

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insights_get_project_workflow_test_metrics_response_most_failed_tests_item import (
    InsightsGetProjectWorkflowTestMetricsResponseMostFailedTestsItem,
)
from .insights_get_project_workflow_test_metrics_response_slowest_tests_item import (
    InsightsGetProjectWorkflowTestMetricsResponseSlowestTestsItem,
)
from .insights_get_project_workflow_test_metrics_response_test_runs_item import (
    InsightsGetProjectWorkflowTestMetricsResponseTestRunsItem,
)


class InsightsGetProjectWorkflowTestMetricsResponse(UniversalBaseModel):
    """
    Project level test metrics response
    """

    average_test_count: int = pydantic.Field()
    """
    The average number of tests executed per run
    """

    most_failed_tests: typing.List[InsightsGetProjectWorkflowTestMetricsResponseMostFailedTestsItem] = pydantic.Field()
    """
    Metrics for the most frequently failing tests
    """

    most_failed_tests_extra: int = pydantic.Field()
    """
    The number of tests with the same success rate being omitted from most_failed_tests
    """

    slowest_tests: typing.List[InsightsGetProjectWorkflowTestMetricsResponseSlowestTestsItem] = pydantic.Field()
    """
    Metrics for the slowest running tests
    """

    slowest_tests_extra: int = pydantic.Field()
    """
    The number of tests with the same duration rate being omitted from slowest_tests
    """

    total_test_runs: int = pydantic.Field()
    """
    The total number of test runs
    """

    test_runs: typing.List[InsightsGetProjectWorkflowTestMetricsResponseTestRunsItem] = pydantic.Field()
    """
    Test counts grouped by pipeline number and workflow id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
