

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
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.c3test_result import C3TestResult
from ..types.execution_metadata import ExecutionMetadata
from ..types.family_name import FamilyName
from ..types.http_validation_error import HttpValidationError
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTestExecutionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def end_test_execution(
        self,
        *,
        ci_link: str,
        test_results: typing.Sequence[C3TestResult],
        c3link: typing.Optional[str] = OMIT,
        checkbox_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/test-executions/end-test",
            method="PUT",
            json={
                "ci_link": ci_link,
                "c3_link": c3link,
                "checkbox_version": checkbox_version,
                "test_results": convert_and_respect_annotation_metadata(
                    object_=test_results, annotation=typing.Sequence[C3TestResult], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def get_test_results(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TestResultResponse]]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TestResultResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/test-results",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TestResultResponse],
                    parse_obj_as(
                        type_=typing.List[TestResultResponse],
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

    def post_results(
        self,
        id: int,
        *,
        request: typing.Sequence[TestResultRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : int

        request : typing.Sequence[TestResultRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/test-results",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[TestResultRequest], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def post_link(
        self, id: int, *, label: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TestExecutionRelevantLinkResponse]:
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
        HttpResponse[TestExecutionRelevantLinkResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/links",
            method="POST",
            json={
                "label": label,
                "url": url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestExecutionRelevantLinkResponse,
                    parse_obj_as(
                        type_=TestExecutionRelevantLinkResponse,
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

    def delete_link(
        self, id: int, link_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        link_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/links/{encode_path_param(link_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def get_rerun_requests(
        self,
        *,
        family: typing.Optional[FamilyName] = None,
        limit: typing.Optional[int] = None,
        environment: typing.Optional[str] = None,
        environment_architecture: typing.Optional[str] = None,
        build_architecture: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[PendingRerun]]:
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
        HttpResponse[typing.List[PendingRerun]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/test-executions/reruns",
            method="GET",
            params={
                "family": family,
                "limit": limit,
                "environment": environment,
                "environment_architecture": environment_architecture,
                "build_architecture": build_architecture,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PendingRerun],
                    parse_obj_as(
                        type_=typing.List[PendingRerun],
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

    def create_rerun_requests(
        self,
        *,
        silent: typing.Optional[bool] = None,
        test_execution_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        test_executions_filters: typing.Optional[TestExecutionRerunFilters] = OMIT,
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[PendingRerun]]]:
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
        HttpResponse[typing.Optional[typing.List[PendingRerun]]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/test-executions/reruns",
            method="POST",
            params={
                "silent": silent,
            },
            json={
                "test_execution_ids": test_execution_ids,
                "test_results_filters": convert_and_respect_annotation_metadata(
                    object_=test_results_filters, annotation=typing.Optional[TestResultSearchFilters], direction="write"
                ),
                "test_executions_filters": convert_and_respect_annotation_metadata(
                    object_=test_executions_filters,
                    annotation=typing.Optional[TestExecutionRerunFilters],
                    direction="write",
                ),
                "priority": priority,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[PendingRerun]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[PendingRerun]],
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

    def delete_rerun_requests(
        self,
        *,
        test_execution_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        test_executions_filters: typing.Optional[TestExecutionRerunFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/test-executions/reruns",
            method="DELETE",
            json={
                "test_execution_ids": test_execution_ids,
                "test_results_filters": convert_and_respect_annotation_metadata(
                    object_=test_results_filters, annotation=typing.Optional[TestResultSearchFilters], direction="write"
                ),
                "test_executions_filters": convert_and_respect_annotation_metadata(
                    object_=test_executions_filters,
                    annotation=typing.Optional[TestExecutionRerunFilters],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def get_rerun_details(
        self,
        *,
        family: FamilyName,
        priority: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RerunDetailsResponse]:
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
        HttpResponse[RerunDetailsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/test-executions/reruns/details",
            method="GET",
            params={
                "family": family,
                "priority": priority,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RerunDetailsResponse,
                    parse_obj_as(
                        type_=RerunDetailsResponse,
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

    def get_test_execution(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TestExecutionResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestExecutionResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestExecutionResponse,
                    parse_obj_as(
                        type_=TestExecutionResponse,
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

    def patch_test_execution(
        self,
        id: int,
        *,
        c3link: typing.Optional[str] = OMIT,
        ci_link: typing.Optional[str] = OMIT,
        status: typing.Optional[TestExecutionsPatchRequestStatus] = OMIT,
        execution_metadata: typing.Optional[ExecutionMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TestExecutionResponse]:
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
        HttpResponse[TestExecutionResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}",
            method="PATCH",
            json={
                "c3_link": c3link,
                "ci_link": ci_link,
                "status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=typing.Optional[TestExecutionsPatchRequestStatus], direction="write"
                ),
                "execution_metadata": execution_metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestExecutionResponse,
                    parse_obj_as(
                        type_=TestExecutionResponse,
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
    ) -> HttpResponse[TestExecutionSearchResponse]:
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
        HttpResponse[TestExecutionSearchResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/test-executions",
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
                "test_execution_statuses": test_execution_statuses,
                "reviewer_ids": convert_and_respect_annotation_metadata(
                    object_=reviewer_ids,
                    annotation=typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds],
                    direction="write",
                ),
                "assignee_ids": convert_and_respect_annotation_metadata(
                    object_=assignee_ids,
                    annotation=typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds],
                    direction="write",
                ),
                "rerun_is_requested": rerun_is_requested,
                "execution_is_latest": execution_is_latest,
                "test_result": convert_and_respect_annotation_metadata(
                    object_=test_result,
                    annotation=typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestTestResult],
                    direction="write",
                ),
                "event_names": convert_and_respect_annotation_metadata(
                    object_=event_names,
                    annotation=typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestEventNames],
                    direction="write",
                ),
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
                    TestExecutionSearchResponse,
                    parse_obj_as(
                        type_=TestExecutionSearchResponse,
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

    def start_test_execution(
        self,
        *,
        request: StartTestExecutionV1TestExecutionsStartTestPutRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request : StartTestExecutionV1TestExecutionsStartTestPutRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/test-executions/start-test",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=StartTestExecutionV1TestExecutionsStartTestPutRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def get_status_update(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TestEventResponse]]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TestEventResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/status_update",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TestEventResponse],
                    parse_obj_as(
                        type_=typing.List[TestEventResponse],
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

    def post_status_update(
        self,
        id: int,
        *,
        events: typing.Sequence[TestEventResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : int

        events : typing.Sequence[TestEventResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/status_update",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[TestEventResponse], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def put_status_update(
        self,
        id: int,
        *,
        events: typing.Sequence[TestEventResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : int

        events : typing.Sequence[TestEventResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/status_update",
            method="PUT",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[TestEventResponse], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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


class AsyncRawTestExecutionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def end_test_execution(
        self,
        *,
        ci_link: str,
        test_results: typing.Sequence[C3TestResult],
        c3link: typing.Optional[str] = OMIT,
        checkbox_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/test-executions/end-test",
            method="PUT",
            json={
                "ci_link": ci_link,
                "c3_link": c3link,
                "checkbox_version": checkbox_version,
                "test_results": convert_and_respect_annotation_metadata(
                    object_=test_results, annotation=typing.Sequence[C3TestResult], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def get_test_results(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TestResultResponse]]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TestResultResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/test-results",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TestResultResponse],
                    parse_obj_as(
                        type_=typing.List[TestResultResponse],
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

    async def post_results(
        self,
        id: int,
        *,
        request: typing.Sequence[TestResultRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : int

        request : typing.Sequence[TestResultRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/test-results",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[TestResultRequest], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def post_link(
        self, id: int, *, label: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TestExecutionRelevantLinkResponse]:
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
        AsyncHttpResponse[TestExecutionRelevantLinkResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/links",
            method="POST",
            json={
                "label": label,
                "url": url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestExecutionRelevantLinkResponse,
                    parse_obj_as(
                        type_=TestExecutionRelevantLinkResponse,
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

    async def delete_link(
        self, id: int, link_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        link_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/links/{encode_path_param(link_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def get_rerun_requests(
        self,
        *,
        family: typing.Optional[FamilyName] = None,
        limit: typing.Optional[int] = None,
        environment: typing.Optional[str] = None,
        environment_architecture: typing.Optional[str] = None,
        build_architecture: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[PendingRerun]]:
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
        AsyncHttpResponse[typing.List[PendingRerun]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/test-executions/reruns",
            method="GET",
            params={
                "family": family,
                "limit": limit,
                "environment": environment,
                "environment_architecture": environment_architecture,
                "build_architecture": build_architecture,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PendingRerun],
                    parse_obj_as(
                        type_=typing.List[PendingRerun],
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

    async def create_rerun_requests(
        self,
        *,
        silent: typing.Optional[bool] = None,
        test_execution_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        test_executions_filters: typing.Optional[TestExecutionRerunFilters] = OMIT,
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[PendingRerun]]]:
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
        AsyncHttpResponse[typing.Optional[typing.List[PendingRerun]]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/test-executions/reruns",
            method="POST",
            params={
                "silent": silent,
            },
            json={
                "test_execution_ids": test_execution_ids,
                "test_results_filters": convert_and_respect_annotation_metadata(
                    object_=test_results_filters, annotation=typing.Optional[TestResultSearchFilters], direction="write"
                ),
                "test_executions_filters": convert_and_respect_annotation_metadata(
                    object_=test_executions_filters,
                    annotation=typing.Optional[TestExecutionRerunFilters],
                    direction="write",
                ),
                "priority": priority,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[PendingRerun]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[PendingRerun]],
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

    async def delete_rerun_requests(
        self,
        *,
        test_execution_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        test_executions_filters: typing.Optional[TestExecutionRerunFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/test-executions/reruns",
            method="DELETE",
            json={
                "test_execution_ids": test_execution_ids,
                "test_results_filters": convert_and_respect_annotation_metadata(
                    object_=test_results_filters, annotation=typing.Optional[TestResultSearchFilters], direction="write"
                ),
                "test_executions_filters": convert_and_respect_annotation_metadata(
                    object_=test_executions_filters,
                    annotation=typing.Optional[TestExecutionRerunFilters],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def get_rerun_details(
        self,
        *,
        family: FamilyName,
        priority: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RerunDetailsResponse]:
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
        AsyncHttpResponse[RerunDetailsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/test-executions/reruns/details",
            method="GET",
            params={
                "family": family,
                "priority": priority,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RerunDetailsResponse,
                    parse_obj_as(
                        type_=RerunDetailsResponse,
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

    async def get_test_execution(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TestExecutionResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestExecutionResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestExecutionResponse,
                    parse_obj_as(
                        type_=TestExecutionResponse,
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

    async def patch_test_execution(
        self,
        id: int,
        *,
        c3link: typing.Optional[str] = OMIT,
        ci_link: typing.Optional[str] = OMIT,
        status: typing.Optional[TestExecutionsPatchRequestStatus] = OMIT,
        execution_metadata: typing.Optional[ExecutionMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TestExecutionResponse]:
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
        AsyncHttpResponse[TestExecutionResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}",
            method="PATCH",
            json={
                "c3_link": c3link,
                "ci_link": ci_link,
                "status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=typing.Optional[TestExecutionsPatchRequestStatus], direction="write"
                ),
                "execution_metadata": execution_metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestExecutionResponse,
                    parse_obj_as(
                        type_=TestExecutionResponse,
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
    ) -> AsyncHttpResponse[TestExecutionSearchResponse]:
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
        AsyncHttpResponse[TestExecutionSearchResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/test-executions",
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
                "test_execution_statuses": test_execution_statuses,
                "reviewer_ids": convert_and_respect_annotation_metadata(
                    object_=reviewer_ids,
                    annotation=typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds],
                    direction="write",
                ),
                "assignee_ids": convert_and_respect_annotation_metadata(
                    object_=assignee_ids,
                    annotation=typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds],
                    direction="write",
                ),
                "rerun_is_requested": rerun_is_requested,
                "execution_is_latest": execution_is_latest,
                "test_result": convert_and_respect_annotation_metadata(
                    object_=test_result,
                    annotation=typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestTestResult],
                    direction="write",
                ),
                "event_names": convert_and_respect_annotation_metadata(
                    object_=event_names,
                    annotation=typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestEventNames],
                    direction="write",
                ),
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
                    TestExecutionSearchResponse,
                    parse_obj_as(
                        type_=TestExecutionSearchResponse,
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

    async def start_test_execution(
        self,
        *,
        request: StartTestExecutionV1TestExecutionsStartTestPutRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        request : StartTestExecutionV1TestExecutionsStartTestPutRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/test-executions/start-test",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=StartTestExecutionV1TestExecutionsStartTestPutRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def get_status_update(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TestEventResponse]]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TestEventResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/status_update",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TestEventResponse],
                    parse_obj_as(
                        type_=typing.List[TestEventResponse],
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

    async def post_status_update(
        self,
        id: int,
        *,
        events: typing.Sequence[TestEventResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : int

        events : typing.Sequence[TestEventResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/status_update",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[TestEventResponse], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def put_status_update(
        self,
        id: int,
        *,
        events: typing.Sequence[TestEventResponse],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : int

        events : typing.Sequence[TestEventResponse]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/test-executions/{encode_path_param(id)}/status_update",
            method="PUT",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[TestEventResponse], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
