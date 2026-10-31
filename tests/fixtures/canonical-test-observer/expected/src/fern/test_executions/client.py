

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.c3test_result import C3TestResult
from ..types.execution_metadata import ExecutionMetadata
from ..types.family_name import FamilyName
from ..types.pending_rerun import PendingRerun
from ..types.rerun_details_response import RerunDetailsResponse
from ..types.test_event_response import TestEventResponse
from ..types.test_execution_relevant_link_response import TestExecutionRelevantLinkResponse
from ..types.test_execution_rerun_filters import TestExecutionRerunFilters
from ..types.test_execution_response import TestExecutionResponse
from ..types.test_execution_search_response import TestExecutionSearchResponse
from ..types.test_execution_status import TestExecutionStatus
from ..types.test_result_request import TestResultRequest
from ..types.test_result_response import TestResultResponse
from ..types.test_result_search_filters import TestResultSearchFilters
from .raw_client import AsyncRawTestExecutionsClient, RawTestExecutionsClient
from .types.search_test_executions_v1test_executions_get_request_assignee_ids import (
    SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds,
)
from .types.search_test_executions_v1test_executions_get_request_event_names import (
    SearchTestExecutionsV1TestExecutionsGetRequestEventNames,
)
from .types.search_test_executions_v1test_executions_get_request_reviewer_ids import (
    SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds,
)
from .types.search_test_executions_v1test_executions_get_request_test_result import (
    SearchTestExecutionsV1TestExecutionsGetRequestTestResult,
)
from .types.start_test_execution_v1test_executions_start_test_put_request import (
    StartTestExecutionV1TestExecutionsStartTestPutRequest,
)
from .types.test_executions_patch_request_status import TestExecutionsPatchRequestStatus


OMIT = typing.cast(typing.Any, ...)


class TestExecutionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestExecutionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestExecutionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestExecutionsClient
        """
        return self._raw_client

    def end_test_execution(
        self,
        *,
        ci_link: str,
        test_results: typing.Sequence[C3TestResult],
        c3link: typing.Optional[str] = OMIT,
        checkbox_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        ci_link : str

        test_results : typing.Sequence[C3TestResult]

        c3link : typing.Optional[str]

        checkbox_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import C3TestResult, C3TestResultStatus, FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.end_test_execution(
            ci_link="ci_link",
            test_results=[
                C3TestResult(
                    name="name",
                    status=C3TestResultStatus.PASS,
                    category="category",
                    comment="comment",
                    io_log="io_log",
                )
            ],
        )
        """
        _response = self._raw_client.end_test_execution(
            ci_link=ci_link,
            test_results=test_results,
            c3link=c3link,
            checkbox_version=checkbox_version,
            request_options=request_options,
        )
        return _response.data

    def get_test_results(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TestResultResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestResultResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.get_test_results(
            id=1,
        )
        """
        _response = self._raw_client.get_test_results(id, request_options=request_options)
        return _response.data

    def post_results(
        self,
        id: int,
        *,
        request: typing.Sequence[TestResultRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : int

        request : typing.Sequence[TestResultRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, TestResultRequest, TestResultStatus

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.post_results(
            id=1,
            request=[
                TestResultRequest(
                    name="name",
                    status=TestResultStatus.PASSED,
                )
            ],
        )
        """
        _response = self._raw_client.post_results(id, request=request, request_options=request_options)
        return _response.data

    def post_link(
        self, id: int, *, label: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TestExecutionRelevantLinkResponse:
        """
        Parameters
        ----------
        id : int

        label : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestExecutionRelevantLinkResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.post_link(
            id=1,
            label="label",
            url="url",
        )
        """
        _response = self._raw_client.post_link(id, label=label, url=url, request_options=request_options)
        return _response.data

    def delete_link(self, id: int, link_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        link_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.delete_link(
            id=1,
            link_id=1,
        )
        """
        _response = self._raw_client.delete_link(id, link_id, request_options=request_options)
        return _response.data

    def get_rerun_requests(
        self,
        *,
        family: typing.Optional[FamilyName] = None,
        limit: typing.Optional[int] = None,
        environment: typing.Optional[str] = None,
        environment_architecture: typing.Optional[str] = None,
        build_architecture: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PendingRerun]:
        """
        Parameters
        ----------
        family : typing.Optional[FamilyName]

        limit : typing.Optional[int]
            Maximum number of rerun requests to return

        environment : typing.Optional[str]

        environment_architecture : typing.Optional[str]

        build_architecture : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PendingRerun]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.get_rerun_requests()
        """
        _response = self._raw_client.get_rerun_requests(
            family=family,
            limit=limit,
            environment=environment,
            environment_architecture=environment_architecture,
            build_architecture=build_architecture,
            request_options=request_options,
        )
        return _response.data

    def create_rerun_requests(
        self,
        *,
        silent: typing.Optional[bool] = None,
        test_execution_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        test_executions_filters: typing.Optional[TestExecutionRerunFilters] = OMIT,
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[PendingRerun]]:
        """
        Parameters
        ----------
        silent : typing.Optional[bool]
            If true, omit returning created reruns in the response body. Speeds up bulk operations, as the rerun schema contains a lot of information and returning many reruns can be slow. Required when creating reruns with test_results_filters or test_executions_filters.

        test_execution_ids : typing.Optional[typing.Sequence[int]]

        test_results_filters : typing.Optional[TestResultSearchFilters]

        test_executions_filters : typing.Optional[TestExecutionRerunFilters]

        priority : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[PendingRerun]]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.create_rerun_requests()
        """
        _response = self._raw_client.create_rerun_requests(
            silent=silent,
            test_execution_ids=test_execution_ids,
            test_results_filters=test_results_filters,
            test_executions_filters=test_executions_filters,
            priority=priority,
            request_options=request_options,
        )
        return _response.data

    def delete_rerun_requests(
        self,
        *,
        test_execution_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        test_executions_filters: typing.Optional[TestExecutionRerunFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        test_execution_ids : typing.Optional[typing.Sequence[int]]

        test_results_filters : typing.Optional[TestResultSearchFilters]

        test_executions_filters : typing.Optional[TestExecutionRerunFilters]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.delete_rerun_requests()
        """
        _response = self._raw_client.delete_rerun_requests(
            test_execution_ids=test_execution_ids,
            test_results_filters=test_results_filters,
            test_executions_filters=test_executions_filters,
            request_options=request_options,
        )
        return _response.data

    def get_rerun_details(
        self,
        *,
        family: FamilyName,
        priority: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RerunDetailsResponse:
        """
        Parameters
        ----------
        family : FamilyName

        priority : typing.Optional[int]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RerunDetailsResponse
            Successful Response

        Examples
        --------
        from fern import FamilyName, FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.get_rerun_details(
            family=FamilyName.SNAP,
        )
        """
        _response = self._raw_client.get_rerun_details(
            family=family, priority=priority, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def get_test_execution(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestExecutionResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestExecutionResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.get_test_execution(
            id=1,
        )
        """
        _response = self._raw_client.get_test_execution(id, request_options=request_options)
        return _response.data

    def patch_test_execution(
        self,
        id: int,
        *,
        c3link: typing.Optional[str] = OMIT,
        ci_link: typing.Optional[str] = OMIT,
        status: typing.Optional[TestExecutionsPatchRequestStatus] = OMIT,
        execution_metadata: typing.Optional[ExecutionMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestExecutionResponse:
        """
        Parameters
        ----------
        id : int

        c3link : typing.Optional[str]

        ci_link : typing.Optional[str]

        status : typing.Optional[TestExecutionsPatchRequestStatus]

        execution_metadata : typing.Optional[ExecutionMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestExecutionResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.patch_test_execution(
            id=1,
        )
        """
        _response = self._raw_client.patch_test_execution(
            id,
            c3link=c3link,
            ci_link=ci_link,
            status=status,
            execution_metadata=execution_metadata,
            request_options=request_options,
        )
        return _response.data

    def search_test_executions(
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
        test_execution_statuses: typing.Optional[typing.Sequence[TestExecutionStatus]] = None,
        reviewer_ids: typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds] = None,
        assignee_ids: typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds] = None,
        rerun_is_requested: typing.Optional[bool] = None,
        execution_is_latest: typing.Optional[bool] = None,
        test_result: typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestTestResult] = None,
        event_names: typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestEventNames] = None,
        from_date: typing.Optional[dt.datetime] = None,
        until_date: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_metadata: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestExecutionSearchResponse:
        """
        Search test executions with optional test result context.

        Returns one item per matching test execution with paginated results.
        The test_results field contains all filtered test results for that execution.

        Use test_result=none to find executions without results,
        test_result=any to find executions with results,
        or test_result={id} to filter by specific test result IDs.
        If test_result is omitted, executions are not filtered by result
        presence at all.

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

        test_execution_statuses : typing.Optional[typing.Sequence[TestExecutionStatus]]
            Filter by test execution statuses

        reviewer_ids : typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds]
            Filter by reviewer user ids

        assignee_ids : typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds]
            DEPRECATED: Use reviewer_ids instead

        rerun_is_requested : typing.Optional[bool]
            Filter by whether a rerun has been requested for the test execution

        execution_is_latest : typing.Optional[bool]
            Filter by whether the test execution is the latest in its environment/artefact/test plan combination

        test_result : typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestTestResult]
            Filter by test result presence: 'any' (executions with results), 'none' (executions without results), or specific test result ID(s). If omitted, executions are not filtered by result presence, so executions with zero results (e.g. NOT_STARTED, ENDED_PREMATURELY) are included.

        event_names : typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestEventNames]
            Filter by event log: 'any' (executions with any events), 'none' (executions without events), or specific event name(s)

        from_date : typing.Optional[dt.datetime]
            Filter executions updated on or after this datetime

        until_date : typing.Optional[dt.datetime]
            Filter executions updated on or before this datetime

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
        TestExecutionSearchResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.search_test_executions()
        """
        _response = self._raw_client.search_test_executions(
            families=families,
            artefacts=artefacts,
            artefact_versions=artefact_versions,
            artefact_stages=artefact_stages,
            artefact_tracks=artefact_tracks,
            artefact_is_archived=artefact_is_archived,
            environments=environments,
            test_plans=test_plans,
            test_execution_statuses=test_execution_statuses,
            reviewer_ids=reviewer_ids,
            assignee_ids=assignee_ids,
            rerun_is_requested=rerun_is_requested,
            execution_is_latest=execution_is_latest,
            test_result=test_result,
            event_names=event_names,
            from_date=from_date,
            until_date=until_date,
            limit=limit,
            offset=offset,
            execution_metadata=execution_metadata,
            request_options=request_options,
        )
        return _response.data

    def start_test_execution(
        self,
        *,
        request: StartTestExecutionV1TestExecutionsStartTestPutRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        request : StartTestExecutionV1TestExecutionsStartTestPutRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern.test_executions import (
            StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap,
        )

        from fern import FernApi, SnapStage

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.start_test_execution(
            request=StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap(
                name="name",
                version="version",
                arch="arch",
                environment="environment",
                test_plan="test_plan",
                revision=1,
                track="track",
                store="store",
                execution_stage=SnapStage.EDGE,
            ),
        )
        """
        _response = self._raw_client.start_test_execution(request=request, request_options=request_options)
        return _response.data

    def get_status_update(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TestEventResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestEventResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.get_status_update(
            id=1,
        )
        """
        _response = self._raw_client.get_status_update(id, request_options=request_options)
        return _response.data

    def post_status_update(
        self,
        id: int,
        *,
        events: typing.Sequence[TestEventResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : int

        events : typing.Sequence[TestEventResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import datetime

        from fern import FernApi, TestEventResponse

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.post_status_update(
            id=1,
            events=[
                TestEventResponse(
                    event_name="event_name",
                    timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    detail="detail",
                )
            ],
        )
        """
        _response = self._raw_client.post_status_update(id, events=events, request_options=request_options)
        return _response.data

    def put_status_update(
        self,
        id: int,
        *,
        events: typing.Sequence[TestEventResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : int

        events : typing.Sequence[TestEventResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import datetime

        from fern import FernApi, TestEventResponse

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_executions.put_status_update(
            id=1,
            events=[
                TestEventResponse(
                    event_name="event_name",
                    timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    detail="detail",
                )
            ],
        )
        """
        _response = self._raw_client.put_status_update(id, events=events, request_options=request_options)
        return _response.data


class AsyncTestExecutionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestExecutionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestExecutionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestExecutionsClient
        """
        return self._raw_client

    async def end_test_execution(
        self,
        *,
        ci_link: str,
        test_results: typing.Sequence[C3TestResult],
        c3link: typing.Optional[str] = OMIT,
        checkbox_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        ci_link : str

        test_results : typing.Sequence[C3TestResult]

        c3link : typing.Optional[str]

        checkbox_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, C3TestResult, C3TestResultStatus

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_executions.end_test_execution(
                ci_link="ci_link",
                test_results=[
                    C3TestResult(
                        name="name",
                        status=C3TestResultStatus.PASS,
                        category="category",
                        comment="comment",
                        io_log="io_log",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.end_test_execution(
            ci_link=ci_link,
            test_results=test_results,
            c3link=c3link,
            checkbox_version=checkbox_version,
            request_options=request_options,
        )
        return _response.data

    async def get_test_results(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TestResultResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestResultResponse]
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
            await client.test_executions.get_test_results(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_test_results(id, request_options=request_options)
        return _response.data

    async def post_results(
        self,
        id: int,
        *,
        request: typing.Sequence[TestResultRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : int

        request : typing.Sequence[TestResultRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TestResultRequest, TestResultStatus

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_executions.post_results(
                id=1,
                request=[
                    TestResultRequest(
                        name="name",
                        status=TestResultStatus.PASSED,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_results(id, request=request, request_options=request_options)
        return _response.data

    async def post_link(
        self, id: int, *, label: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TestExecutionRelevantLinkResponse:
        """
        Parameters
        ----------
        id : int

        label : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestExecutionRelevantLinkResponse
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
            await client.test_executions.post_link(
                id=1,
                label="label",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_link(id, label=label, url=url, request_options=request_options)
        return _response.data

    async def delete_link(
        self, id: int, link_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

        link_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

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
            await client.test_executions.delete_link(
                id=1,
                link_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_link(id, link_id, request_options=request_options)
        return _response.data

    async def get_rerun_requests(
        self,
        *,
        family: typing.Optional[FamilyName] = None,
        limit: typing.Optional[int] = None,
        environment: typing.Optional[str] = None,
        environment_architecture: typing.Optional[str] = None,
        build_architecture: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PendingRerun]:
        """
        Parameters
        ----------
        family : typing.Optional[FamilyName]

        limit : typing.Optional[int]
            Maximum number of rerun requests to return

        environment : typing.Optional[str]

        environment_architecture : typing.Optional[str]

        build_architecture : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PendingRerun]
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
            await client.test_executions.get_rerun_requests()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_rerun_requests(
            family=family,
            limit=limit,
            environment=environment,
            environment_architecture=environment_architecture,
            build_architecture=build_architecture,
            request_options=request_options,
        )
        return _response.data

    async def create_rerun_requests(
        self,
        *,
        silent: typing.Optional[bool] = None,
        test_execution_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        test_executions_filters: typing.Optional[TestExecutionRerunFilters] = OMIT,
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[PendingRerun]]:
        """
        Parameters
        ----------
        silent : typing.Optional[bool]
            If true, omit returning created reruns in the response body. Speeds up bulk operations, as the rerun schema contains a lot of information and returning many reruns can be slow. Required when creating reruns with test_results_filters or test_executions_filters.

        test_execution_ids : typing.Optional[typing.Sequence[int]]

        test_results_filters : typing.Optional[TestResultSearchFilters]

        test_executions_filters : typing.Optional[TestExecutionRerunFilters]

        priority : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[PendingRerun]]
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
            await client.test_executions.create_rerun_requests()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_rerun_requests(
            silent=silent,
            test_execution_ids=test_execution_ids,
            test_results_filters=test_results_filters,
            test_executions_filters=test_executions_filters,
            priority=priority,
            request_options=request_options,
        )
        return _response.data

    async def delete_rerun_requests(
        self,
        *,
        test_execution_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        test_executions_filters: typing.Optional[TestExecutionRerunFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        test_execution_ids : typing.Optional[typing.Sequence[int]]

        test_results_filters : typing.Optional[TestResultSearchFilters]

        test_executions_filters : typing.Optional[TestExecutionRerunFilters]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
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
            await client.test_executions.delete_rerun_requests()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_rerun_requests(
            test_execution_ids=test_execution_ids,
            test_results_filters=test_results_filters,
            test_executions_filters=test_executions_filters,
            request_options=request_options,
        )
        return _response.data

    async def get_rerun_details(
        self,
        *,
        family: FamilyName,
        priority: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RerunDetailsResponse:
        """
        Parameters
        ----------
        family : FamilyName

        priority : typing.Optional[int]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RerunDetailsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FamilyName

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_executions.get_rerun_details(
                family=FamilyName.SNAP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_rerun_details(
            family=family, priority=priority, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_test_execution(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestExecutionResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestExecutionResponse
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
            await client.test_executions.get_test_execution(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_test_execution(id, request_options=request_options)
        return _response.data

    async def patch_test_execution(
        self,
        id: int,
        *,
        c3link: typing.Optional[str] = OMIT,
        ci_link: typing.Optional[str] = OMIT,
        status: typing.Optional[TestExecutionsPatchRequestStatus] = OMIT,
        execution_metadata: typing.Optional[ExecutionMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestExecutionResponse:
        """
        Parameters
        ----------
        id : int

        c3link : typing.Optional[str]

        ci_link : typing.Optional[str]

        status : typing.Optional[TestExecutionsPatchRequestStatus]

        execution_metadata : typing.Optional[ExecutionMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestExecutionResponse
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
            await client.test_executions.patch_test_execution(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_test_execution(
            id,
            c3link=c3link,
            ci_link=ci_link,
            status=status,
            execution_metadata=execution_metadata,
            request_options=request_options,
        )
        return _response.data

    async def search_test_executions(
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
        test_execution_statuses: typing.Optional[typing.Sequence[TestExecutionStatus]] = None,
        reviewer_ids: typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds] = None,
        assignee_ids: typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds] = None,
        rerun_is_requested: typing.Optional[bool] = None,
        execution_is_latest: typing.Optional[bool] = None,
        test_result: typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestTestResult] = None,
        event_names: typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestEventNames] = None,
        from_date: typing.Optional[dt.datetime] = None,
        until_date: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_metadata: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestExecutionSearchResponse:
        """
        Search test executions with optional test result context.

        Returns one item per matching test execution with paginated results.
        The test_results field contains all filtered test results for that execution.

        Use test_result=none to find executions without results,
        test_result=any to find executions with results,
        or test_result={id} to filter by specific test result IDs.
        If test_result is omitted, executions are not filtered by result
        presence at all.

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

        test_execution_statuses : typing.Optional[typing.Sequence[TestExecutionStatus]]
            Filter by test execution statuses

        reviewer_ids : typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds]
            Filter by reviewer user ids

        assignee_ids : typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds]
            DEPRECATED: Use reviewer_ids instead

        rerun_is_requested : typing.Optional[bool]
            Filter by whether a rerun has been requested for the test execution

        execution_is_latest : typing.Optional[bool]
            Filter by whether the test execution is the latest in its environment/artefact/test plan combination

        test_result : typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestTestResult]
            Filter by test result presence: 'any' (executions with results), 'none' (executions without results), or specific test result ID(s). If omitted, executions are not filtered by result presence, so executions with zero results (e.g. NOT_STARTED, ENDED_PREMATURELY) are included.

        event_names : typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestEventNames]
            Filter by event log: 'any' (executions with any events), 'none' (executions without events), or specific event name(s)

        from_date : typing.Optional[dt.datetime]
            Filter executions updated on or after this datetime

        until_date : typing.Optional[dt.datetime]
            Filter executions updated on or before this datetime

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
        TestExecutionSearchResponse
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
            await client.test_executions.search_test_executions()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_test_executions(
            families=families,
            artefacts=artefacts,
            artefact_versions=artefact_versions,
            artefact_stages=artefact_stages,
            artefact_tracks=artefact_tracks,
            artefact_is_archived=artefact_is_archived,
            environments=environments,
            test_plans=test_plans,
            test_execution_statuses=test_execution_statuses,
            reviewer_ids=reviewer_ids,
            assignee_ids=assignee_ids,
            rerun_is_requested=rerun_is_requested,
            execution_is_latest=execution_is_latest,
            test_result=test_result,
            event_names=event_names,
            from_date=from_date,
            until_date=until_date,
            limit=limit,
            offset=offset,
            execution_metadata=execution_metadata,
            request_options=request_options,
        )
        return _response.data

    async def start_test_execution(
        self,
        *,
        request: StartTestExecutionV1TestExecutionsStartTestPutRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        request : StartTestExecutionV1TestExecutionsStartTestPutRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern.test_executions import (
            StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap,
        )

        from fern import AsyncFernApi, SnapStage

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_executions.start_test_execution(
                request=StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap(
                    name="name",
                    version="version",
                    arch="arch",
                    environment="environment",
                    test_plan="test_plan",
                    revision=1,
                    track="track",
                    store="store",
                    execution_stage=SnapStage.EDGE,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_test_execution(request=request, request_options=request_options)
        return _response.data

    async def get_status_update(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TestEventResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestEventResponse]
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
            await client.test_executions.get_status_update(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status_update(id, request_options=request_options)
        return _response.data

    async def post_status_update(
        self,
        id: int,
        *,
        events: typing.Sequence[TestEventResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : int

        events : typing.Sequence[TestEventResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, TestEventResponse

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_executions.post_status_update(
                id=1,
                events=[
                    TestEventResponse(
                        event_name="event_name",
                        timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        detail="detail",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_status_update(id, events=events, request_options=request_options)
        return _response.data

    async def put_status_update(
        self,
        id: int,
        *,
        events: typing.Sequence[TestEventResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : int

        events : typing.Sequence[TestEventResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, TestEventResponse

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_executions.put_status_update(
                id=1,
                events=[
                    TestEventResponse(
                        event_name="event_name",
                        timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        detail="detail",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_status_update(id, events=events, request_options=request_options)
        return _response.data
