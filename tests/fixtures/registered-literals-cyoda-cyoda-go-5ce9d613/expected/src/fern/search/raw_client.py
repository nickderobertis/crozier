

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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.request_timeout_error import RequestTimeoutError
from ..types.async_search_status_dto import AsyncSearchStatusDto
from ..types.cancel_async_search_dto import CancelAsyncSearchDto
from ..types.entity_result_dto import EntityResultDto
from ..types.paged_entity_results_dto import PagedEntityResultsDto
from ..types.problem_detail_dto import ProblemDetailDto
from .types.search_entities_request_body import SearchEntitiesRequestBody
from .types.submit_async_search_job_request_body import SubmitAsyncSearchJobRequestBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def submit_async_search_job(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: SubmitAsyncSearchJobRequestBody,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Submits an asynchronous search job for creating a persistent search result set for large datasets.

        This endpoint initiates an asynchronous search operation that:
        1. Validates the search criteria against the specified entity model
        2. Creates a persistent search result set of matching entities
        3. Returns a UUID that can be used to:
           - Monitor the search job progress (/search/async/{jobId}/status)
           - Retrieve paginated results (/search/async/{jobId})
           - Cancel the search job if needed (/search/async/{jobId}/cancel)

        Search jobs are temporary and have a limited lifetime:
        - Each search job has an automatic expiration date
        - Expired search jobs are automatically deleted by the system
        - The expiration date can be retrieved using GET /search/async/{jobId}/status
        - Plan to retrieve your data before the search job expires

        The search job runs in the background, allowing handling of large datasets
        without timeout concerns.

        If no request body is provided or an empty request body is sent, all entities of the specified model and version will be included in the search results.

        Query Structure:
        The search condition is a tree of predicates that can include:
        1. Simple conditions - search within entity data using JSONPath
        2. Lifecycle conditions - search based on entity lifecycle (state, creationDate, previousTransition)
        3. Group conditions - combine multiple conditions with AND/OR operators

        Operator Types (Predicates)
        Available Operations:

        1. Basic Comparison
        - EQUALS: Exact match
        - NOT_EQUAL: Non-matching values
        - IS_NULL, NOT_NULL: Null checks
        - GREATER_THAN, LESS_THAN: Numeric/date comparisons
        - GREATER_OR_EQUAL, LESS_OR_EQUAL: Inclusive comparisons
        - BETWEEN, BETWEEN_INCLUSIVE: Range checks

        2. String Operations (Case-Sensitive)
        - CONTAINS: Substring match
        - NOT_CONTAINS: Negative substring match
        - STARTS_WITH, NOT_STARTS_WITH: Prefix matching
        - ENDS_WITH, NOT_ENDS_WITH: Suffix matching
        - MATCHES_PATTERN: Regular expression match
        - LIKE: SQL-style pattern matching

        3. Case-Insensitive String Operations
        - IEQUALS, INOT_EQUAL: Case-insensitive equality
        - ICONTAINS, INOT_CONTAINS: Case-insensitive substring
        - ISTARTS_WITH, INOT_STARTS_WITH: Case-insensitive prefix
        - IENDS_WITH, INOT_ENDS_WITH: Case-insensitive suffix

        4. State Tracking
        - IS_UNCHANGED: Field hasn't changed
        - IS_CHANGED: Field has changed

        Parameters
        ----------
        entity_name : str
            Name of the entity model to search

        model_version : int
            Version of the entity model

        request : SubmitAsyncSearchJobRequestBody

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for the report, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Async search job submitted successfully. Note that the search job will expire after a certain period.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"search/async/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=SubmitAsyncSearchJobRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_async_search_results(
        self,
        job_id: str,
        *,
        page_size: typing.Optional[str] = None,
        page_number: typing.Optional[str] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagedEntityResultsDto]:
        """
        Retrieves a page of results from a previously submitted async search job.
        To find out how many entities were found, call the search job status endpoint.

        By default results are ordered by entity id ascending. Pass one or more `sort` keys to order by scalar data or meta fields; entity id is always the final tiebreaker.

        The results are returned in a paginated format, with:
        - Configurable page size (default: 10)
        - Zero-based page numbering
        - Optional point-in-time specification for the data being retrieved

        Parameters
        ----------
        job_id : str
            UUID of the search job to retrieve results from

        page_size : typing.Optional[str]
            Number of results per page

        page_number : typing.Optional[str]
            Zero-based page number

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for loading the entities, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the point-in-time of the report if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagedEntityResultsDto]
            Successfully retrieved page of results
        """
        _response = self._client_wrapper.httpx_client.request(
            f"search/async/{encode_path_param(job_id)}",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNumber": page_number,
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedEntityResultsDto,
                    parse_obj_as(
                        type_=PagedEntityResultsDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def cancel_async_search(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelAsyncSearchDto]:
        """
        Attempts to cancel a running async search job. The operation:
        - Only succeeds if the search job is in RUNNING state
        - Returns the cancellation result and final status
        - Invalidates the search job entry if cancellation succeeds

        Parameters
        ----------
        job_id : str
            UUID of the search job to cancel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CancelAsyncSearchDto]
            Cancellation request processed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"search/async/{encode_path_param(job_id)}/cancel",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelAsyncSearchDto,
                    parse_obj_as(
                        type_=CancelAsyncSearchDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_async_search_status(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AsyncSearchStatusDto]:
        """
        Retrieves the current status of an async search job. The response includes:
        - Current status (one of: RUNNING, FAILED, CANCELLED, SUCCESSFUL, NOT_FOUND)
        - Number of entities collected
        - Calculation time
        - Creation timestamp
        - Finish timestamp (if completed)
        - Expiration date

        Note: The NOT_FOUND status occurs in rare race conditions where the search job exists when the endpoint is called but is deleted during data retrieval.

        Parameters
        ----------
        job_id : str
            UUID of the search job to check status for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AsyncSearchStatusDto]
            Successfully retrieved search job status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"search/async/{encode_path_param(job_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncSearchStatusDto,
                    parse_obj_as(
                        type_=AsyncSearchStatusDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def entities(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: SearchEntitiesRequestBody,
        point_in_time: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[str] = None,
        timeout_millis: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[EntityResultDto]]:
        """
        Executes a direct, in-memory search for entities without creating a persistent search job. This endpoint:
        - Returns results immediately as a streaming response
        - Is optimized for smaller result sets
        - Has configurable timeout and result limits
        - Supports point-in-time querying

        By default results are ordered by entity id ascending. Pass one or more `sort` keys to order by scalar data or meta fields; entity id is always the final tiebreaker.

        If no request body is provided or an empty request body is sent, all entities of the specified model and version
        will be returned (subject to the limit parameter).

        Best suited for:
        - Interactive searches requiring immediate results
        - Queries expected to return limited number of entities
        - UI components with real-time search functionality

        Limitations:
        - Maximum result limit: 10000 entities (this will silently limit the result to 10000)
        - Default result limit: 1000 entities
        - Default timeout: 60000 milliseconds

        Parameters
        ----------
        entity_name : str
            Name of the entity model to search

        model_version : int
            Version of the entity model

        request : SearchEntitiesRequestBody

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for searching the entities, in ISO 8601 format. Defaults to the consistency time of the system if not provided.

        limit : typing.Optional[str]
            The maximum number of rows to return. You can specify a limit of up to 10000 and defaults to 1000 if not provided.

        timeout_millis : typing.Optional[str]
            The maximum time to wait for the query to complete, in milliseconds, and defaults to 60000 if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[EntityResultDto]]
            Search executed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"search/direct/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "limit": limit,
                "timeoutMillis": timeout_millis,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=SearchEntitiesRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[EntityResultDto],
                    parse_obj_as(
                        type_=typing.List[EntityResultDto],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 408:
                raise RequestTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetailDto,
                        parse_obj_as(
                            type_=ProblemDetailDto,
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


class AsyncRawSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def submit_async_search_job(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: SubmitAsyncSearchJobRequestBody,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Submits an asynchronous search job for creating a persistent search result set for large datasets.

        This endpoint initiates an asynchronous search operation that:
        1. Validates the search criteria against the specified entity model
        2. Creates a persistent search result set of matching entities
        3. Returns a UUID that can be used to:
           - Monitor the search job progress (/search/async/{jobId}/status)
           - Retrieve paginated results (/search/async/{jobId})
           - Cancel the search job if needed (/search/async/{jobId}/cancel)

        Search jobs are temporary and have a limited lifetime:
        - Each search job has an automatic expiration date
        - Expired search jobs are automatically deleted by the system
        - The expiration date can be retrieved using GET /search/async/{jobId}/status
        - Plan to retrieve your data before the search job expires

        The search job runs in the background, allowing handling of large datasets
        without timeout concerns.

        If no request body is provided or an empty request body is sent, all entities of the specified model and version will be included in the search results.

        Query Structure:
        The search condition is a tree of predicates that can include:
        1. Simple conditions - search within entity data using JSONPath
        2. Lifecycle conditions - search based on entity lifecycle (state, creationDate, previousTransition)
        3. Group conditions - combine multiple conditions with AND/OR operators

        Operator Types (Predicates)
        Available Operations:

        1. Basic Comparison
        - EQUALS: Exact match
        - NOT_EQUAL: Non-matching values
        - IS_NULL, NOT_NULL: Null checks
        - GREATER_THAN, LESS_THAN: Numeric/date comparisons
        - GREATER_OR_EQUAL, LESS_OR_EQUAL: Inclusive comparisons
        - BETWEEN, BETWEEN_INCLUSIVE: Range checks

        2. String Operations (Case-Sensitive)
        - CONTAINS: Substring match
        - NOT_CONTAINS: Negative substring match
        - STARTS_WITH, NOT_STARTS_WITH: Prefix matching
        - ENDS_WITH, NOT_ENDS_WITH: Suffix matching
        - MATCHES_PATTERN: Regular expression match
        - LIKE: SQL-style pattern matching

        3. Case-Insensitive String Operations
        - IEQUALS, INOT_EQUAL: Case-insensitive equality
        - ICONTAINS, INOT_CONTAINS: Case-insensitive substring
        - ISTARTS_WITH, INOT_STARTS_WITH: Case-insensitive prefix
        - IENDS_WITH, INOT_ENDS_WITH: Case-insensitive suffix

        4. State Tracking
        - IS_UNCHANGED: Field hasn't changed
        - IS_CHANGED: Field has changed

        Parameters
        ----------
        entity_name : str
            Name of the entity model to search

        model_version : int
            Version of the entity model

        request : SubmitAsyncSearchJobRequestBody

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for the report, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the current consistency time of the system if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Async search job submitted successfully. Note that the search job will expire after a certain period.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"search/async/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=SubmitAsyncSearchJobRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_async_search_results(
        self,
        job_id: str,
        *,
        page_size: typing.Optional[str] = None,
        page_number: typing.Optional[str] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagedEntityResultsDto]:
        """
        Retrieves a page of results from a previously submitted async search job.
        To find out how many entities were found, call the search job status endpoint.

        By default results are ordered by entity id ascending. Pass one or more `sort` keys to order by scalar data or meta fields; entity id is always the final tiebreaker.

        The results are returned in a paginated format, with:
        - Configurable page size (default: 10)
        - Zero-based page numbering
        - Optional point-in-time specification for the data being retrieved

        Parameters
        ----------
        job_id : str
            UUID of the search job to retrieve results from

        page_size : typing.Optional[str]
            Number of results per page

        page_number : typing.Optional[str]
            Zero-based page number

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for loading the entities, in ISO 8601 format (e.g., '2035-01-01T12:00:00Z'). Defaults to the point-in-time of the report if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagedEntityResultsDto]
            Successfully retrieved page of results
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"search/async/{encode_path_param(job_id)}",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNumber": page_number,
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedEntityResultsDto,
                    parse_obj_as(
                        type_=PagedEntityResultsDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def cancel_async_search(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelAsyncSearchDto]:
        """
        Attempts to cancel a running async search job. The operation:
        - Only succeeds if the search job is in RUNNING state
        - Returns the cancellation result and final status
        - Invalidates the search job entry if cancellation succeeds

        Parameters
        ----------
        job_id : str
            UUID of the search job to cancel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CancelAsyncSearchDto]
            Cancellation request processed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"search/async/{encode_path_param(job_id)}/cancel",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelAsyncSearchDto,
                    parse_obj_as(
                        type_=CancelAsyncSearchDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_async_search_status(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AsyncSearchStatusDto]:
        """
        Retrieves the current status of an async search job. The response includes:
        - Current status (one of: RUNNING, FAILED, CANCELLED, SUCCESSFUL, NOT_FOUND)
        - Number of entities collected
        - Calculation time
        - Creation timestamp
        - Finish timestamp (if completed)
        - Expiration date

        Note: The NOT_FOUND status occurs in rare race conditions where the search job exists when the endpoint is called but is deleted during data retrieval.

        Parameters
        ----------
        job_id : str
            UUID of the search job to check status for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsyncSearchStatusDto]
            Successfully retrieved search job status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"search/async/{encode_path_param(job_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncSearchStatusDto,
                    parse_obj_as(
                        type_=AsyncSearchStatusDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def entities(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: SearchEntitiesRequestBody,
        point_in_time: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[str] = None,
        timeout_millis: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[EntityResultDto]]:
        """
        Executes a direct, in-memory search for entities without creating a persistent search job. This endpoint:
        - Returns results immediately as a streaming response
        - Is optimized for smaller result sets
        - Has configurable timeout and result limits
        - Supports point-in-time querying

        By default results are ordered by entity id ascending. Pass one or more `sort` keys to order by scalar data or meta fields; entity id is always the final tiebreaker.

        If no request body is provided or an empty request body is sent, all entities of the specified model and version
        will be returned (subject to the limit parameter).

        Best suited for:
        - Interactive searches requiring immediate results
        - Queries expected to return limited number of entities
        - UI components with real-time search functionality

        Limitations:
        - Maximum result limit: 10000 entities (this will silently limit the result to 10000)
        - Default result limit: 1000 entities
        - Default timeout: 60000 milliseconds

        Parameters
        ----------
        entity_name : str
            Name of the entity model to search

        model_version : int
            Version of the entity model

        request : SearchEntitiesRequestBody

        point_in_time : typing.Optional[dt.datetime]
            The point-in-time for searching the entities, in ISO 8601 format. Defaults to the consistency time of the system if not provided.

        limit : typing.Optional[str]
            The maximum number of rows to return. You can specify a limit of up to 10000 and defaults to 1000 if not provided.

        timeout_millis : typing.Optional[str]
            The maximum time to wait for the query to complete, in milliseconds, and defaults to 60000 if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[EntityResultDto]]
            Search executed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"search/direct/{encode_path_param(entity_name)}/{encode_path_param(model_version)}",
            method="POST",
            params={
                "pointInTime": serialize_datetime(point_in_time) if point_in_time is not None else None,
                "limit": limit,
                "timeoutMillis": timeout_millis,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=SearchEntitiesRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[EntityResultDto],
                    parse_obj_as(
                        type_=typing.List[EntityResultDto],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 408:
                raise RequestTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetailDto,
                        parse_obj_as(
                            type_=ProblemDetailDto,
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
