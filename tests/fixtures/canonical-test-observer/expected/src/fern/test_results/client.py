

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.family_name import FamilyName
from ..types.test_execution_status import TestExecutionStatus
from ..types.test_result_search_response_with_context import TestResultSearchResponseWithContext
from ..types.test_result_status import TestResultStatus
from .raw_client import AsyncRawTestResultsClient, RawTestResultsClient
from .types.search_test_results_v1test_results_get_request_assignee_ids import (
    SearchTestResultsV1TestResultsGetRequestAssigneeIds,
)
from .types.search_test_results_v1test_results_get_request_issues import SearchTestResultsV1TestResultsGetRequestIssues
from .types.search_test_results_v1test_results_get_request_reviewer_ids import (
    SearchTestResultsV1TestResultsGetRequestReviewerIds,
)


class TestResultsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestResultsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestResultsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestResultsClient
        """
        return self._raw_client

    def search_test_results(
        self,
        *,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        artefacts: typing.Optional[typing.Sequence[str]] = None,
        artefact_versions: typing.Optional[typing.Sequence[str]] = None,
        artefact_stages: typing.Optional[typing.Sequence[str]] = None,
        artefact_tracks: typing.Optional[typing.Sequence[str]] = None,
        artefact_is_archived: typing.Optional[bool] = None,
        environments: typing.Optional[typing.Sequence[str]] = None,
        test_plans: typing.Optional[typing.Sequence[str]] = None,
        test_cases: typing.Optional[typing.Sequence[str]] = None,
        template_ids: typing.Optional[typing.Sequence[str]] = None,
        issues: typing.Optional[SearchTestResultsV1TestResultsGetRequestIssues] = None,
        test_result_statuses: typing.Optional[typing.Sequence[TestResultStatus]] = None,
        test_execution_statuses: typing.Optional[typing.Sequence[TestExecutionStatus]] = None,
        reviewer_ids: typing.Optional[SearchTestResultsV1TestResultsGetRequestReviewerIds] = None,
        assignee_ids: typing.Optional[SearchTestResultsV1TestResultsGetRequestAssigneeIds] = None,
        rerun_is_requested: typing.Optional[bool] = None,
        execution_is_latest: typing.Optional[bool] = None,
        from_date: typing.Optional[dt.datetime] = None,
        until_date: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_metadata: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestResultSearchResponseWithContext:
        """
        Search test results across artefacts using flexible filters.

        Returns one item per matching test result with execution, artefact, and build context.

        Parameters
        ----------
        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families (e.g., charm,snap)

        artefacts : typing.Optional[typing.Sequence[str]]
            Filter by artefact names

        artefact_versions : typing.Optional[typing.Sequence[str]]
            Filter by artefact versions

        artefact_stages : typing.Optional[typing.Sequence[str]]
            Filter by artefact stages

        artefact_tracks : typing.Optional[typing.Sequence[str]]
            Filter by artefact tracks

        artefact_is_archived : typing.Optional[bool]
            Filter by whether the artefact is archived

        environments : typing.Optional[typing.Sequence[str]]
            Filter by environment names

        test_plans : typing.Optional[typing.Sequence[str]]
            Filter by test plan names

        test_cases : typing.Optional[typing.Sequence[str]]
            Filter by test case names

        template_ids : typing.Optional[typing.Sequence[str]]
            Filter by template IDs

        issues : typing.Optional[SearchTestResultsV1TestResultsGetRequestIssues]
            Filter by issue IDs

        test_result_statuses : typing.Optional[typing.Sequence[TestResultStatus]]
            Filter by test result statuses

        test_execution_statuses : typing.Optional[typing.Sequence[TestExecutionStatus]]
            Filter by test execution statuses

        reviewer_ids : typing.Optional[SearchTestResultsV1TestResultsGetRequestReviewerIds]
            Filter by reviewer user ids

        assignee_ids : typing.Optional[SearchTestResultsV1TestResultsGetRequestAssigneeIds]
            DEPRECATED: Use reviewer_ids instead

        rerun_is_requested : typing.Optional[bool]
            Filter by whether a rerun has been requested for the test execution

        execution_is_latest : typing.Optional[bool]
            Filter by whether the test execution is the latest in its environment/artifact/test plan combination

        from_date : typing.Optional[dt.datetime]
            Filter results from this timestamp

        until_date : typing.Optional[dt.datetime]
            Filter results until this timestamp

        limit : typing.Optional[int]
            Maximum number of results to return

        offset : typing.Optional[int]
            Number of results to skip for pagination

        execution_metadata : typing.Optional[typing.Sequence[str]]
            Filter by execution metadata (base64 encoded category:value pairs).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestResultSearchResponseWithContext
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_results.search_test_results()
        """
        _response = self._raw_client.search_test_results(
            families=families,
            artefacts=artefacts,
            artefact_versions=artefact_versions,
            artefact_stages=artefact_stages,
            artefact_tracks=artefact_tracks,
            artefact_is_archived=artefact_is_archived,
            environments=environments,
            test_plans=test_plans,
            test_cases=test_cases,
            template_ids=template_ids,
            issues=issues,
            test_result_statuses=test_result_statuses,
            test_execution_statuses=test_execution_statuses,
            reviewer_ids=reviewer_ids,
            assignee_ids=assignee_ids,
            rerun_is_requested=rerun_is_requested,
            execution_is_latest=execution_is_latest,
            from_date=from_date,
            until_date=until_date,
            limit=limit,
            offset=offset,
            execution_metadata=execution_metadata,
            request_options=request_options,
        )
        return _response.data


class AsyncTestResultsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestResultsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestResultsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestResultsClient
        """
        return self._raw_client

    async def search_test_results(
        self,
        *,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        artefacts: typing.Optional[typing.Sequence[str]] = None,
        artefact_versions: typing.Optional[typing.Sequence[str]] = None,
        artefact_stages: typing.Optional[typing.Sequence[str]] = None,
        artefact_tracks: typing.Optional[typing.Sequence[str]] = None,
        artefact_is_archived: typing.Optional[bool] = None,
        environments: typing.Optional[typing.Sequence[str]] = None,
        test_plans: typing.Optional[typing.Sequence[str]] = None,
        test_cases: typing.Optional[typing.Sequence[str]] = None,
        template_ids: typing.Optional[typing.Sequence[str]] = None,
        issues: typing.Optional[SearchTestResultsV1TestResultsGetRequestIssues] = None,
        test_result_statuses: typing.Optional[typing.Sequence[TestResultStatus]] = None,
        test_execution_statuses: typing.Optional[typing.Sequence[TestExecutionStatus]] = None,
        reviewer_ids: typing.Optional[SearchTestResultsV1TestResultsGetRequestReviewerIds] = None,
        assignee_ids: typing.Optional[SearchTestResultsV1TestResultsGetRequestAssigneeIds] = None,
        rerun_is_requested: typing.Optional[bool] = None,
        execution_is_latest: typing.Optional[bool] = None,
        from_date: typing.Optional[dt.datetime] = None,
        until_date: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_metadata: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestResultSearchResponseWithContext:
        """
        Search test results across artefacts using flexible filters.

        Returns one item per matching test result with execution, artefact, and build context.

        Parameters
        ----------
        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families (e.g., charm,snap)

        artefacts : typing.Optional[typing.Sequence[str]]
            Filter by artefact names

        artefact_versions : typing.Optional[typing.Sequence[str]]
            Filter by artefact versions

        artefact_stages : typing.Optional[typing.Sequence[str]]
            Filter by artefact stages

        artefact_tracks : typing.Optional[typing.Sequence[str]]
            Filter by artefact tracks

        artefact_is_archived : typing.Optional[bool]
            Filter by whether the artefact is archived

        environments : typing.Optional[typing.Sequence[str]]
            Filter by environment names

        test_plans : typing.Optional[typing.Sequence[str]]
            Filter by test plan names

        test_cases : typing.Optional[typing.Sequence[str]]
            Filter by test case names

        template_ids : typing.Optional[typing.Sequence[str]]
            Filter by template IDs

        issues : typing.Optional[SearchTestResultsV1TestResultsGetRequestIssues]
            Filter by issue IDs

        test_result_statuses : typing.Optional[typing.Sequence[TestResultStatus]]
            Filter by test result statuses

        test_execution_statuses : typing.Optional[typing.Sequence[TestExecutionStatus]]
            Filter by test execution statuses

        reviewer_ids : typing.Optional[SearchTestResultsV1TestResultsGetRequestReviewerIds]
            Filter by reviewer user ids

        assignee_ids : typing.Optional[SearchTestResultsV1TestResultsGetRequestAssigneeIds]
            DEPRECATED: Use reviewer_ids instead

        rerun_is_requested : typing.Optional[bool]
            Filter by whether a rerun has been requested for the test execution

        execution_is_latest : typing.Optional[bool]
            Filter by whether the test execution is the latest in its environment/artifact/test plan combination

        from_date : typing.Optional[dt.datetime]
            Filter results from this timestamp

        until_date : typing.Optional[dt.datetime]
            Filter results until this timestamp

        limit : typing.Optional[int]
            Maximum number of results to return

        offset : typing.Optional[int]
            Number of results to skip for pagination

        execution_metadata : typing.Optional[typing.Sequence[str]]
            Filter by execution metadata (base64 encoded category:value pairs).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestResultSearchResponseWithContext
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_results.search_test_results()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_test_results(
            families=families,
            artefacts=artefacts,
            artefact_versions=artefact_versions,
            artefact_stages=artefact_stages,
            artefact_tracks=artefact_tracks,
            artefact_is_archived=artefact_is_archived,
            environments=environments,
            test_plans=test_plans,
            test_cases=test_cases,
            template_ids=template_ids,
            issues=issues,
            test_result_statuses=test_result_statuses,
            test_execution_statuses=test_execution_statuses,
            reviewer_ids=reviewer_ids,
            assignee_ids=assignee_ids,
            rerun_is_requested=rerun_is_requested,
            execution_is_latest=execution_is_latest,
            from_date=from_date,
            until_date=until_date,
            limit=limit,
            offset=offset,
            execution_metadata=execution_metadata,
            request_options=request_options,
        )
        return _response.data
