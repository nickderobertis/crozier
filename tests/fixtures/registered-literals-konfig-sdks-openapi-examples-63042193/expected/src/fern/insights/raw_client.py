

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
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
from pydantic import ValidationError


class RawInsightsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getprojectsummarymetrics(
        self,
        project_slug: str,
        *,
        reporting_window: typing.Optional[InsightsGetProjectSummaryMetricsRequestReportingWindow] = None,
        branches: typing.Optional[typing.Dict[str, typing.Any]] = None,
        workflow_names: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InsightsGetProjectSummaryMetricsResponse]:
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
        HttpResponse[InsightsGetProjectSummaryMetricsResponse]
            Aggregated summary metrics and trends by workflow and branches
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/pages/{encode_path_param(project_slug)}/summary",
            method="GET",
            params={
                "reporting-window": reporting_window,
                "branches": branches,
                "workflow-names": workflow_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetProjectSummaryMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetProjectSummaryMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[InsightsGetJobTimeseriesDataResponse]:
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
        HttpResponse[InsightsGetJobTimeseriesDataResponse]
            An array of timeseries data, one entry per job.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/time-series/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}/jobs",
            method="GET",
            params={
                "branch": branch,
                "granularity": granularity,
                "start-date": serialize_datetime(start_date) if start_date is not None else None,
                "end-date": serialize_datetime(end_date) if end_date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetJobTimeseriesDataResponse,
                    parse_obj_as(
                        type_=InsightsGetJobTimeseriesDataResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getsummarymetricswithtrends(
        self,
        org_slug: str,
        *,
        reporting_window: typing.Optional[InsightsGetSummaryMetricsWithTrendsRequestReportingWindow] = None,
        project_names: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InsightsGetSummaryMetricsWithTrendsResponse]:
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
        HttpResponse[InsightsGetSummaryMetricsWithTrendsResponse]
            summary metrics with trends for an entire org and it's projects.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(org_slug)}/summary",
            method="GET",
            params={
                "reporting-window": reporting_window,
                "project-names": project_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetSummaryMetricsWithTrendsResponse,
                    parse_obj_as(
                        type_=InsightsGetSummaryMetricsWithTrendsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def listprojectbranches(
        self,
        project_slug: str,
        *,
        workflow_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InsightsListProjectBranchesResponse]:
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
        HttpResponse[InsightsListProjectBranchesResponse]
            A list of branches for a project
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/branches",
            method="GET",
            params={
                "workflow-name": workflow_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsListProjectBranchesResponse,
                    parse_obj_as(
                        type_=InsightsListProjectBranchesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getflakytests(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InsightsGetFlakyTestsResponse]:
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
        HttpResponse[InsightsGetFlakyTestsResponse]
            A list of flaky tests for a project
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/flaky-tests",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetFlakyTestsResponse,
                    parse_obj_as(
                        type_=InsightsGetFlakyTestsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getprojectworkflowmetrics(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        reporting_window: typing.Optional[InsightsGetProjectWorkflowMetricsRequestReportingWindow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InsightsGetProjectWorkflowMetricsResponse]:
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
        HttpResponse[InsightsGetProjectWorkflowMetricsResponse]
            A paginated list of summary metrics by workflow
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows",
            method="GET",
            params={
                "page-token": page_token,
                "all-branches": all_branches,
                "branch": branch,
                "reporting-window": reporting_window,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetProjectWorkflowMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetProjectWorkflowMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[InsightsGetRecentWorkflowRunsResponse]:
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
        HttpResponse[InsightsGetRecentWorkflowRunsResponse]
            A paginated list of recent workflow runs
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}",
            method="GET",
            params={
                "all-branches": all_branches,
                "branch": branch,
                "page-token": page_token,
                "start-date": serialize_datetime(start_date) if start_date is not None else None,
                "end-date": serialize_datetime(end_date) if end_date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetRecentWorkflowRunsResponse,
                    parse_obj_as(
                        type_=InsightsGetRecentWorkflowRunsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[InsightsGetProjectWorkflowJobMetricsResponse]:
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
        HttpResponse[InsightsGetProjectWorkflowJobMetricsResponse]
            A paginated list of summary metrics by workflow job.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}/jobs",
            method="GET",
            params={
                "page-token": page_token,
                "all-branches": all_branches,
                "branch": branch,
                "reporting-window": reporting_window,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetProjectWorkflowJobMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetProjectWorkflowJobMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getworkflowsummarymetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InsightsGetWorkflowSummaryMetricsResponse]:
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
        HttpResponse[InsightsGetWorkflowSummaryMetricsResponse]
            Metrics and trends for a workflow
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}/summary",
            method="GET",
            params={
                "all-branches": all_branches,
                "branch": branch,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetWorkflowSummaryMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetWorkflowSummaryMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getprojectworkflowtestmetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InsightsGetProjectWorkflowTestMetricsResponse]:
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
        HttpResponse[InsightsGetProjectWorkflowTestMetricsResponse]
            A list of test metrics by workflow
        """
        _response = self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}/test-metrics",
            method="GET",
            params={
                "branch": branch,
                "all-branches": all_branches,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetProjectWorkflowTestMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetProjectWorkflowTestMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawInsightsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getprojectsummarymetrics(
        self,
        project_slug: str,
        *,
        reporting_window: typing.Optional[InsightsGetProjectSummaryMetricsRequestReportingWindow] = None,
        branches: typing.Optional[typing.Dict[str, typing.Any]] = None,
        workflow_names: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InsightsGetProjectSummaryMetricsResponse]:
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
        AsyncHttpResponse[InsightsGetProjectSummaryMetricsResponse]
            Aggregated summary metrics and trends by workflow and branches
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/pages/{encode_path_param(project_slug)}/summary",
            method="GET",
            params={
                "reporting-window": reporting_window,
                "branches": branches,
                "workflow-names": workflow_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetProjectSummaryMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetProjectSummaryMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[InsightsGetJobTimeseriesDataResponse]:
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
        AsyncHttpResponse[InsightsGetJobTimeseriesDataResponse]
            An array of timeseries data, one entry per job.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/time-series/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}/jobs",
            method="GET",
            params={
                "branch": branch,
                "granularity": granularity,
                "start-date": serialize_datetime(start_date) if start_date is not None else None,
                "end-date": serialize_datetime(end_date) if end_date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetJobTimeseriesDataResponse,
                    parse_obj_as(
                        type_=InsightsGetJobTimeseriesDataResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getsummarymetricswithtrends(
        self,
        org_slug: str,
        *,
        reporting_window: typing.Optional[InsightsGetSummaryMetricsWithTrendsRequestReportingWindow] = None,
        project_names: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InsightsGetSummaryMetricsWithTrendsResponse]:
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
        AsyncHttpResponse[InsightsGetSummaryMetricsWithTrendsResponse]
            summary metrics with trends for an entire org and it's projects.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(org_slug)}/summary",
            method="GET",
            params={
                "reporting-window": reporting_window,
                "project-names": project_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetSummaryMetricsWithTrendsResponse,
                    parse_obj_as(
                        type_=InsightsGetSummaryMetricsWithTrendsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def listprojectbranches(
        self,
        project_slug: str,
        *,
        workflow_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InsightsListProjectBranchesResponse]:
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
        AsyncHttpResponse[InsightsListProjectBranchesResponse]
            A list of branches for a project
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/branches",
            method="GET",
            params={
                "workflow-name": workflow_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsListProjectBranchesResponse,
                    parse_obj_as(
                        type_=InsightsListProjectBranchesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getflakytests(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InsightsGetFlakyTestsResponse]:
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
        AsyncHttpResponse[InsightsGetFlakyTestsResponse]
            A list of flaky tests for a project
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/flaky-tests",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetFlakyTestsResponse,
                    parse_obj_as(
                        type_=InsightsGetFlakyTestsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getprojectworkflowmetrics(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        reporting_window: typing.Optional[InsightsGetProjectWorkflowMetricsRequestReportingWindow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InsightsGetProjectWorkflowMetricsResponse]:
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
        AsyncHttpResponse[InsightsGetProjectWorkflowMetricsResponse]
            A paginated list of summary metrics by workflow
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows",
            method="GET",
            params={
                "page-token": page_token,
                "all-branches": all_branches,
                "branch": branch,
                "reporting-window": reporting_window,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetProjectWorkflowMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetProjectWorkflowMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[InsightsGetRecentWorkflowRunsResponse]:
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
        AsyncHttpResponse[InsightsGetRecentWorkflowRunsResponse]
            A paginated list of recent workflow runs
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}",
            method="GET",
            params={
                "all-branches": all_branches,
                "branch": branch,
                "page-token": page_token,
                "start-date": serialize_datetime(start_date) if start_date is not None else None,
                "end-date": serialize_datetime(end_date) if end_date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetRecentWorkflowRunsResponse,
                    parse_obj_as(
                        type_=InsightsGetRecentWorkflowRunsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[InsightsGetProjectWorkflowJobMetricsResponse]:
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
        AsyncHttpResponse[InsightsGetProjectWorkflowJobMetricsResponse]
            A paginated list of summary metrics by workflow job.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}/jobs",
            method="GET",
            params={
                "page-token": page_token,
                "all-branches": all_branches,
                "branch": branch,
                "reporting-window": reporting_window,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetProjectWorkflowJobMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetProjectWorkflowJobMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getworkflowsummarymetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        all_branches: typing.Optional[bool] = None,
        branch: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InsightsGetWorkflowSummaryMetricsResponse]:
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
        AsyncHttpResponse[InsightsGetWorkflowSummaryMetricsResponse]
            Metrics and trends for a workflow
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}/summary",
            method="GET",
            params={
                "all-branches": all_branches,
                "branch": branch,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetWorkflowSummaryMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetWorkflowSummaryMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getprojectworkflowtestmetrics(
        self,
        project_slug: str,
        workflow_name: str,
        *,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InsightsGetProjectWorkflowTestMetricsResponse]:
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
        AsyncHttpResponse[InsightsGetProjectWorkflowTestMetricsResponse]
            A list of test metrics by workflow
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"insights/{encode_path_param(project_slug)}/workflows/{encode_path_param(workflow_name)}/test-metrics",
            method="GET",
            params={
                "branch": branch,
                "all-branches": all_branches,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InsightsGetProjectWorkflowTestMetricsResponse,
                    parse_obj_as(
                        type_=InsightsGetProjectWorkflowTestMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
