

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.family_name import FamilyName
from ..types.http_validation_error import HttpValidationError
from ..types.test_execution_status import TestExecutionStatus
from ..types.test_result_search_response_with_context import TestResultSearchResponseWithContext
from ..types.test_result_status import TestResultStatus
from .types.search_test_results_v1test_results_get_request_assignee_ids import (
    SearchTestResultsV1TestResultsGetRequestAssigneeIds,
)
from .types.search_test_results_v1test_results_get_request_issues import SearchTestResultsV1TestResultsGetRequestIssues
from .types.search_test_results_v1test_results_get_request_reviewer_ids import (
    SearchTestResultsV1TestResultsGetRequestReviewerIds,
)
from pydantic import ValidationError


class RawTestResultsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[TestResultSearchResponseWithContext]:
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
        HttpResponse[TestResultSearchResponseWithContext]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/test-results",
            method="GET",
            params={
                "families": families,
                "artefacts": artefacts,
                "artefact_versions": artefact_versions,
                "artefact_stages": artefact_stages,
                "artefact_tracks": artefact_tracks,
                "artefact_is_archived": artefact_is_archived,
                "environments": environments,
                "test_plans": test_plans,
                "test_cases": test_cases,
                "template_ids": template_ids,
                "issues": convert_and_respect_annotation_metadata(
                    object_=issues,
                    annotation=typing.Optional[SearchTestResultsV1TestResultsGetRequestIssues],
                    direction="write",
                ),
                "test_result_statuses": test_result_statuses,
                "test_execution_statuses": test_execution_statuses,
                "reviewer_ids": convert_and_respect_annotation_metadata(
                    object_=reviewer_ids,
                    annotation=typing.Optional[SearchTestResultsV1TestResultsGetRequestReviewerIds],
                    direction="write",
                ),
                "assignee_ids": convert_and_respect_annotation_metadata(
                    object_=assignee_ids,
                    annotation=typing.Optional[SearchTestResultsV1TestResultsGetRequestAssigneeIds],
                    direction="write",
                ),
                "rerun_is_requested": rerun_is_requested,
                "execution_is_latest": execution_is_latest,
                "from_date": serialize_datetime(from_date) if from_date is not None else None,
                "until_date": serialize_datetime(until_date) if until_date is not None else None,
                "limit": limit,
                "offset": offset,
                "execution_metadata": execution_metadata,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestResultSearchResponseWithContext,
                    parse_obj_as(
                        type_=TestResultSearchResponseWithContext,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTestResultsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[TestResultSearchResponseWithContext]:
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
        AsyncHttpResponse[TestResultSearchResponseWithContext]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/test-results",
            method="GET",
            params={
                "families": families,
                "artefacts": artefacts,
                "artefact_versions": artefact_versions,
                "artefact_stages": artefact_stages,
                "artefact_tracks": artefact_tracks,
                "artefact_is_archived": artefact_is_archived,
                "environments": environments,
                "test_plans": test_plans,
                "test_cases": test_cases,
                "template_ids": template_ids,
                "issues": convert_and_respect_annotation_metadata(
                    object_=issues,
                    annotation=typing.Optional[SearchTestResultsV1TestResultsGetRequestIssues],
                    direction="write",
                ),
                "test_result_statuses": test_result_statuses,
                "test_execution_statuses": test_execution_statuses,
                "reviewer_ids": convert_and_respect_annotation_metadata(
                    object_=reviewer_ids,
                    annotation=typing.Optional[SearchTestResultsV1TestResultsGetRequestReviewerIds],
                    direction="write",
                ),
                "assignee_ids": convert_and_respect_annotation_metadata(
                    object_=assignee_ids,
                    annotation=typing.Optional[SearchTestResultsV1TestResultsGetRequestAssigneeIds],
                    direction="write",
                ),
                "rerun_is_requested": rerun_is_requested,
                "execution_is_latest": execution_is_latest,
                "from_date": serialize_datetime(from_date) if from_date is not None else None,
                "until_date": serialize_datetime(until_date) if until_date is not None else None,
                "limit": limit,
                "offset": offset,
                "execution_metadata": execution_metadata,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestResultSearchResponseWithContext,
                    parse_obj_as(
                        type_=TestResultSearchResponseWithContext,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
