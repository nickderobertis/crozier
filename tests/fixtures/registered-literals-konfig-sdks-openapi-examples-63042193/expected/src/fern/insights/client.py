

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.insights_get_flaky_tests_response import InsightsGetFlakyTestsResponse
from ..types.insights_get_job_timeseries_data_response import InsightsGetJobTimeseriesDataResponse
from ..types.insights_get_project_summary_metrics_response import InsightsGetProjectSummaryMetricsResponse
from ..types.insights_get_project_workflow_job_metrics_response import InsightsGetProjectWorkflowJobMetricsResponse
from ..types.insights_get_project_workflow_metrics_response import InsightsGetProjectWorkflowMetricsResponse
from ..types.insights_get_project_workflow_test_metrics_response import InsightsGetProjectWorkflowTestMetricsResponse
from ..types.insights_get_recent_workflow_runs_response import InsightsGetRecentWorkflowRunsResponse
from ..types.insights_get_summary_metrics_with_trends_response import InsightsGetSummaryMetricsWithTrendsResponse
from ..types.insights_get_workflow_summary_metrics_response import InsightsGetWorkflowSummaryMetricsResponse
from ..types.insights_list_project_branches_response import InsightsListProjectBranchesResponse
from .raw_client import AsyncRawInsightsClient, RawInsightsClient
from .types.insights_get_job_timeseries_data_request_granularity import InsightsGetJobTimeseriesDataRequestGranularity
from .types.insights_get_project_summary_metrics_request_reporting_window import (
    InsightsGetProjectSummaryMetricsRequestReportingWindow,
)
from .types.insights_get_project_workflow_job_metrics_request_reporting_window import (
    InsightsGetProjectWorkflowJobMetricsRequestReportingWindow,
)
from .types.insights_get_project_workflow_metrics_request_reporting_window import (
    InsightsGetProjectWorkflowMetricsRequestReportingWindow,
)
from .types.insights_get_summary_metrics_with_trends_request_reporting_window import (
    InsightsGetSummaryMetricsWithTrendsRequestReportingWindow,
)


class InsightsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInsightsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInsightsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInsightsClient
        """
        return self._raw_client

    def getprojectsummarymetrics(
        self,
        project_slug: str,
        *,
        reporting_window: typing.Optional[InsightsGetProjectSummaryMetricsRequestReportingWindow] = None,
        branches: typing.Optional[typing.Dict[str, typing.Any]] = None,
        workflow_names: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetProjectSummaryMetricsResponse:
        """
        Get summary metrics and trends for a project at workflow and branch level.
                     Workflow runs going back at most 90 days are included in the aggregation window.
                     Trends are only supported upto last 30 days.
                     Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        reporting_window : typing.Optional[InsightsGetProjectSummaryMetricsRequestReportingWindow]
            The time window used to calculate summary metrics. If not provided, defaults to last-90-days

        branches : typing.Optional[typing.Dict[str, typing.Any]]
            The names of VCS branches to include in branch-level workflow metrics.

        workflow_names : typing.Optional[typing.Dict[str, typing.Any]]
            The names of workflows to include in workflow-level metrics.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetProjectSummaryMetricsResponse
            Aggregated summary metrics and trends by workflow and branches

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.getprojectsummarymetrics(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.getprojectsummarymetrics(
            project_slug,
            reporting_window=reporting_window,
            branches=branches,
            workflow_names=workflow_names,
            request_options=request_options,
        )
        return _response.data

    def getjobtimeseriesdata(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        branch: typing.Optional[str] = None,
        granularity: typing.Optional[InsightsGetJobTimeseriesDataRequestGranularity] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetJobTimeseriesDataResponse:
        """
        Get timeseries data for all jobs within a workflow. Hourly granularity data is only retained for 48 hours while daily granularity data is retained for 90 days.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        granularity : typing.Optional[InsightsGetJobTimeseriesDataRequestGranularity]
            The granularity for which to query timeseries data.

        start_date : typing.Optional[dt.datetime]
            Include only executions that started at or after this date. This must be specified if an end-date is provided.

        end_date : typing.Optional[dt.datetime]
            Include only executions that started before this date. This date can be at most 90 days after the start-date.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetJobTimeseriesDataResponse
            An array of timeseries data, one entry per job.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.getjobtimeseriesdata(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            workflow_name="build-and-test",
            start_date=datetime.datetime.fromisoformat(
                "2020-08-21 13:26:29+00:00",
            ),
            end_date=datetime.datetime.fromisoformat(
                "2020-09-04 13:26:29+00:00",
            ),
        )
        """
        _response = self._raw_client.getjobtimeseriesdata(
            project_slug,
            workflow_name,
            branch=branch,
            granularity=granularity,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    def getsummarymetricswithtrends(
        self,
        org_slug: str,
        *,
        reporting_window: typing.Optional[InsightsGetSummaryMetricsWithTrendsRequestReportingWindow] = None,
        project_names: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetSummaryMetricsWithTrendsResponse:
        """
        Gets aggregated summary metrics with trends for the entire org.
                      Also gets aggregated metrics and trends for each project belonging to the org.

        Parameters
        ----------
        org_slug : str
            Org slug in the form `vcs-slug/org-name`. The `/` characters may be URL-escaped.

        reporting_window : typing.Optional[InsightsGetSummaryMetricsWithTrendsRequestReportingWindow]
            The time window used to calculate summary metrics. If not provided, defaults to last-90-days

        project_names : typing.Optional[typing.Dict[str, typing.Any]]
            List of project names.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetSummaryMetricsWithTrendsResponse
            summary metrics with trends for an entire org and it's projects.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.getsummarymetricswithtrends(
            org_slug="gh/CircleCI-Public",
        )
        """
        _response = self._raw_client.getsummarymetricswithtrends(
            org_slug, reporting_window=reporting_window, project_names=project_names, request_options=request_options
        )
        return _response.data

    def listprojectbranches(
        self,
        project_slug: str,
        *,
        workflow_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsListProjectBranchesResponse:
        """
        Get a list of all branches for a specified project. The list will only contain branches currently available within Insights. The maximum number of branches returned by this endpoint is 5,000.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : typing.Optional[str]
            The name of a workflow. If not passed we will scope the API call to the project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsListProjectBranchesResponse
            A list of branches for a project

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.listprojectbranches(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            workflow_name="build-and-test",
        )
        """
        _response = self._raw_client.listprojectbranches(
            project_slug, workflow_name=workflow_name, request_options=request_options
        )
        return _response.data

    def getflakytests(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InsightsGetFlakyTestsResponse:
        """
        Get a list of flaky tests for a given project. Flaky tests are branch agnostic.
                     A flaky test is a test that passed and failed in the same commit.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetFlakyTestsResponse
            A list of flaky tests for a project

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.getflakytests(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.getflakytests(project_slug, request_options=request_options)
        return _response.data

    def getprojectworkflowmetrics(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        reporting_window: typing.Optional[InsightsGetProjectWorkflowMetricsRequestReportingWindow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetProjectWorkflowMetricsResponse:
        """
        Get summary metrics for a project's workflows.  Workflow runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours.  Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        reporting_window : typing.Optional[InsightsGetProjectWorkflowMetricsRequestReportingWindow]
            The time window used to calculate summary metrics. If not provided, defaults to last-90-days

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetProjectWorkflowMetricsResponse
            A paginated list of summary metrics by workflow

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.getprojectworkflowmetrics(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.getprojectworkflowmetrics(
            project_slug,
            page_token=page_token,
            all_branches=all_branches,
            branch=branch,
            reporting_window=reporting_window,
            request_options=request_options,
        )
        return _response.data

    def getrecentworkflowruns(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetRecentWorkflowRunsResponse:
        """
        Get recent runs of a workflow. Runs going back at most 90 days are returned. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        start_date : typing.Optional[dt.datetime]
            Include only executions that started at or after this date. This must be specified if an end-date is provided.

        end_date : typing.Optional[dt.datetime]
            Include only executions that started before this date. This date can be at most 90 days after the start-date.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetRecentWorkflowRunsResponse
            A paginated list of recent workflow runs

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.getrecentworkflowruns(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            workflow_name="build-and-test",
            start_date=datetime.datetime.fromisoformat(
                "2020-08-21 13:26:29+00:00",
            ),
            end_date=datetime.datetime.fromisoformat(
                "2020-09-04 13:26:29+00:00",
            ),
        )
        """
        _response = self._raw_client.getrecentworkflowruns(
            project_slug,
            workflow_name,
            all_branches=all_branches,
            branch=branch,
            page_token=page_token,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    def getprojectworkflowjobmetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        page_token: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        reporting_window: typing.Optional[InsightsGetProjectWorkflowJobMetricsRequestReportingWindow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetProjectWorkflowJobMetricsResponse:
        """
        Get summary metrics for a project workflow's jobs. Job runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        reporting_window : typing.Optional[InsightsGetProjectWorkflowJobMetricsRequestReportingWindow]
            The time window used to calculate summary metrics. If not provided, defaults to last-90-days

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetProjectWorkflowJobMetricsResponse
            A paginated list of summary metrics by workflow job.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.getprojectworkflowjobmetrics(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            workflow_name="build-and-test",
        )
        """
        _response = self._raw_client.getprojectworkflowjobmetrics(
            project_slug,
            workflow_name,
            page_token=page_token,
            all_branches=all_branches,
            branch=branch,
            reporting_window=reporting_window,
            request_options=request_options,
        )
        return _response.data

    def getworkflowsummarymetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetWorkflowSummaryMetricsResponse:
        """
        Get the metrics and trends for a particular workflow on a single branch or all branches

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetWorkflowSummaryMetricsResponse
            Metrics and trends for a workflow

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.getworkflowsummarymetrics(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            workflow_name="build-and-test",
        )
        """
        _response = self._raw_client.getworkflowsummarymetrics(
            project_slug, workflow_name, all_branches=all_branches, branch=branch, request_options=request_options
        )
        return _response.data

    def getprojectworkflowtestmetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetProjectWorkflowTestMetricsResponse:
        """
        Get test metrics for a project's workflows. Currently tests metrics are calculated based on 10 most recent workflow runs.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetProjectWorkflowTestMetricsResponse
            A list of test metrics by workflow

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.insights.getprojectworkflowtestmetrics(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            workflow_name="build-and-test",
        )
        """
        _response = self._raw_client.getprojectworkflowtestmetrics(
            project_slug, workflow_name, branch=branch, all_branches=all_branches, request_options=request_options
        )
        return _response.data


class AsyncInsightsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInsightsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInsightsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInsightsClient
        """
        return self._raw_client

    async def getprojectsummarymetrics(
        self,
        project_slug: str,
        *,
        reporting_window: typing.Optional[InsightsGetProjectSummaryMetricsRequestReportingWindow] = None,
        branches: typing.Optional[typing.Dict[str, typing.Any]] = None,
        workflow_names: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetProjectSummaryMetricsResponse:
        """
        Get summary metrics and trends for a project at workflow and branch level.
                     Workflow runs going back at most 90 days are included in the aggregation window.
                     Trends are only supported upto last 30 days.
                     Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        reporting_window : typing.Optional[InsightsGetProjectSummaryMetricsRequestReportingWindow]
            The time window used to calculate summary metrics. If not provided, defaults to last-90-days

        branches : typing.Optional[typing.Dict[str, typing.Any]]
            The names of VCS branches to include in branch-level workflow metrics.

        workflow_names : typing.Optional[typing.Dict[str, typing.Any]]
            The names of workflows to include in workflow-level metrics.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetProjectSummaryMetricsResponse
            Aggregated summary metrics and trends by workflow and branches

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.getprojectsummarymetrics(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getprojectsummarymetrics(
            project_slug,
            reporting_window=reporting_window,
            branches=branches,
            workflow_names=workflow_names,
            request_options=request_options,
        )
        return _response.data

    async def getjobtimeseriesdata(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        branch: typing.Optional[str] = None,
        granularity: typing.Optional[InsightsGetJobTimeseriesDataRequestGranularity] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetJobTimeseriesDataResponse:
        """
        Get timeseries data for all jobs within a workflow. Hourly granularity data is only retained for 48 hours while daily granularity data is retained for 90 days.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        granularity : typing.Optional[InsightsGetJobTimeseriesDataRequestGranularity]
            The granularity for which to query timeseries data.

        start_date : typing.Optional[dt.datetime]
            Include only executions that started at or after this date. This must be specified if an end-date is provided.

        end_date : typing.Optional[dt.datetime]
            Include only executions that started before this date. This date can be at most 90 days after the start-date.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetJobTimeseriesDataResponse
            An array of timeseries data, one entry per job.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.getjobtimeseriesdata(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                workflow_name="build-and-test",
                start_date=datetime.datetime.fromisoformat(
                    "2020-08-21 13:26:29+00:00",
                ),
                end_date=datetime.datetime.fromisoformat(
                    "2020-09-04 13:26:29+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getjobtimeseriesdata(
            project_slug,
            workflow_name,
            branch=branch,
            granularity=granularity,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    async def getsummarymetricswithtrends(
        self,
        org_slug: str,
        *,
        reporting_window: typing.Optional[InsightsGetSummaryMetricsWithTrendsRequestReportingWindow] = None,
        project_names: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetSummaryMetricsWithTrendsResponse:
        """
        Gets aggregated summary metrics with trends for the entire org.
                      Also gets aggregated metrics and trends for each project belonging to the org.

        Parameters
        ----------
        org_slug : str
            Org slug in the form `vcs-slug/org-name`. The `/` characters may be URL-escaped.

        reporting_window : typing.Optional[InsightsGetSummaryMetricsWithTrendsRequestReportingWindow]
            The time window used to calculate summary metrics. If not provided, defaults to last-90-days

        project_names : typing.Optional[typing.Dict[str, typing.Any]]
            List of project names.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetSummaryMetricsWithTrendsResponse
            summary metrics with trends for an entire org and it's projects.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.getsummarymetricswithtrends(
                org_slug="gh/CircleCI-Public",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getsummarymetricswithtrends(
            org_slug, reporting_window=reporting_window, project_names=project_names, request_options=request_options
        )
        return _response.data

    async def listprojectbranches(
        self,
        project_slug: str,
        *,
        workflow_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsListProjectBranchesResponse:
        """
        Get a list of all branches for a specified project. The list will only contain branches currently available within Insights. The maximum number of branches returned by this endpoint is 5,000.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : typing.Optional[str]
            The name of a workflow. If not passed we will scope the API call to the project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsListProjectBranchesResponse
            A list of branches for a project

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.listprojectbranches(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                workflow_name="build-and-test",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listprojectbranches(
            project_slug, workflow_name=workflow_name, request_options=request_options
        )
        return _response.data

    async def getflakytests(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InsightsGetFlakyTestsResponse:
        """
        Get a list of flaky tests for a given project. Flaky tests are branch agnostic.
                     A flaky test is a test that passed and failed in the same commit.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetFlakyTestsResponse
            A list of flaky tests for a project

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.getflakytests(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getflakytests(project_slug, request_options=request_options)
        return _response.data

    async def getprojectworkflowmetrics(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        reporting_window: typing.Optional[InsightsGetProjectWorkflowMetricsRequestReportingWindow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetProjectWorkflowMetricsResponse:
        """
        Get summary metrics for a project's workflows.  Workflow runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours.  Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        reporting_window : typing.Optional[InsightsGetProjectWorkflowMetricsRequestReportingWindow]
            The time window used to calculate summary metrics. If not provided, defaults to last-90-days

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetProjectWorkflowMetricsResponse
            A paginated list of summary metrics by workflow

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.getprojectworkflowmetrics(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getprojectworkflowmetrics(
            project_slug,
            page_token=page_token,
            all_branches=all_branches,
            branch=branch,
            reporting_window=reporting_window,
            request_options=request_options,
        )
        return _response.data

    async def getrecentworkflowruns(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetRecentWorkflowRunsResponse:
        """
        Get recent runs of a workflow. Runs going back at most 90 days are returned. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        start_date : typing.Optional[dt.datetime]
            Include only executions that started at or after this date. This must be specified if an end-date is provided.

        end_date : typing.Optional[dt.datetime]
            Include only executions that started before this date. This date can be at most 90 days after the start-date.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetRecentWorkflowRunsResponse
            A paginated list of recent workflow runs

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.getrecentworkflowruns(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                workflow_name="build-and-test",
                start_date=datetime.datetime.fromisoformat(
                    "2020-08-21 13:26:29+00:00",
                ),
                end_date=datetime.datetime.fromisoformat(
                    "2020-09-04 13:26:29+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrecentworkflowruns(
            project_slug,
            workflow_name,
            all_branches=all_branches,
            branch=branch,
            page_token=page_token,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    async def getprojectworkflowjobmetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        page_token: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        reporting_window: typing.Optional[InsightsGetProjectWorkflowJobMetricsRequestReportingWindow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetProjectWorkflowJobMetricsResponse:
        """
        Get summary metrics for a project workflow's jobs. Job runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        reporting_window : typing.Optional[InsightsGetProjectWorkflowJobMetricsRequestReportingWindow]
            The time window used to calculate summary metrics. If not provided, defaults to last-90-days

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetProjectWorkflowJobMetricsResponse
            A paginated list of summary metrics by workflow job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.getprojectworkflowjobmetrics(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                workflow_name="build-and-test",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getprojectworkflowjobmetrics(
            project_slug,
            workflow_name,
            page_token=page_token,
            all_branches=all_branches,
            branch=branch,
            reporting_window=reporting_window,
            request_options=request_options,
        )
        return _response.data

    async def getworkflowsummarymetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetWorkflowSummaryMetricsResponse:
        """
        Get the metrics and trends for a particular workflow on a single branch or all branches

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetWorkflowSummaryMetricsResponse
            Metrics and trends for a workflow

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.getworkflowsummarymetrics(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                workflow_name="build-and-test",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getworkflowsummarymetrics(
            project_slug, workflow_name, all_branches=all_branches, branch=branch, request_options=request_options
        )
        return _response.data

    async def getprojectworkflowtestmetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsightsGetProjectWorkflowTestMetricsResponse:
        """
        Get test metrics for a project's workflows. Currently tests metrics are calculated based on 10 most recent workflow runs.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        workflow_name : str
            The name of the workflow.

        branch : typing.Optional[str]
            The name of a vcs branch. If not passed we will scope the API call to the default branch.

        all_branches : typing.Optional[bool]
            Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsightsGetProjectWorkflowTestMetricsResponse
            A list of test metrics by workflow

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.insights.getprojectworkflowtestmetrics(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                workflow_name="build-and-test",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getprojectworkflowtestmetrics(
            project_slug, workflow_name, branch=branch, all_branches=all_branches, request_options=request_options
        )
        return _response.data
