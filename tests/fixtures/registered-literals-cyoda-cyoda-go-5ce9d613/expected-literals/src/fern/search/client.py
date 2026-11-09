

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.async_search_status_dto import AsyncSearchStatusDto
from ..types.cancel_async_search_dto import CancelAsyncSearchDto
from ..types.entity_result_dto import EntityResultDto
from ..types.paged_entity_results_dto import PagedEntityResultsDto
from .raw_client import AsyncRawSearchClient, RawSearchClient
from .types.search_entities_request_body import SearchEntitiesRequestBody
from .types.submit_async_search_job_request_body import SubmitAsyncSearchJobRequestBody


OMIT = typing.cast(typing.Any, ...)


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchClient
        """
        return self._raw_client

    def submit_async_search_job(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: SubmitAsyncSearchJobRequestBody,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Async search job submitted successfully. Note that the search job will expire after a certain period.

        Examples
        --------
        from fern import ArrayConditionDto, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.submit_async_search_job(
            entity_name="entityName",
            model_version=1,
            request=ArrayConditionDto(
                type="type",
                json_path="jsonPath",
                operator_type="EQUALS",
                value=["value"],
            ),
        )
        """
        _response = self._raw_client.submit_async_search_job(
            entity_name, model_version, request=request, point_in_time=point_in_time, request_options=request_options
        )
        return _response.data

    def get_async_search_results(
        self,
        job_id: str,
        *,
        page_size: typing.Optional[str] = None,
        page_number: typing.Optional[str] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedEntityResultsDto:
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
        PagedEntityResultsDto
            Successfully retrieved page of results

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.get_async_search_results(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_async_search_results(
            job_id,
            page_size=page_size,
            page_number=page_number,
            point_in_time=point_in_time,
            request_options=request_options,
        )
        return _response.data

    def cancel_async_search(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelAsyncSearchDto:
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
        CancelAsyncSearchDto
            Cancellation request processed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.cancel_async_search(
            job_id="jobId",
        )
        """
        _response = self._raw_client.cancel_async_search(job_id, request_options=request_options)
        return _response.data

    def get_async_search_status(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncSearchStatusDto:
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
        AsyncSearchStatusDto
            Successfully retrieved search job status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.get_async_search_status(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_async_search_status(job_id, request_options=request_options)
        return _response.data

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
    ) -> typing.List[EntityResultDto]:
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
        typing.List[EntityResultDto]
            Search executed successfully

        Examples
        --------
        from fern import ArrayConditionDto, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.entities(
            entity_name="entityName",
            model_version=1,
            request=ArrayConditionDto(
                type="type",
                json_path="jsonPath",
                operator_type="EQUALS",
                value=["value"],
            ),
        )
        """
        _response = self._raw_client.entities(
            entity_name,
            model_version,
            request=request,
            point_in_time=point_in_time,
            limit=limit,
            timeout_millis=timeout_millis,
            request_options=request_options,
        )
        return _response.data


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchClient
        """
        return self._raw_client

    async def submit_async_search_job(
        self,
        entity_name: str,
        model_version: int,
        *,
        request: SubmitAsyncSearchJobRequestBody,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
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
        str
            Async search job submitted successfully. Note that the search job will expire after a certain period.

        Examples
        --------
        import asyncio

        from fern import ArrayConditionDto, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.submit_async_search_job(
                entity_name="entityName",
                model_version=1,
                request=ArrayConditionDto(
                    type="type",
                    json_path="jsonPath",
                    operator_type="EQUALS",
                    value=["value"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_async_search_job(
            entity_name, model_version, request=request, point_in_time=point_in_time, request_options=request_options
        )
        return _response.data

    async def get_async_search_results(
        self,
        job_id: str,
        *,
        page_size: typing.Optional[str] = None,
        page_number: typing.Optional[str] = None,
        point_in_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedEntityResultsDto:
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
        PagedEntityResultsDto
            Successfully retrieved page of results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.get_async_search_results(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_async_search_results(
            job_id,
            page_size=page_size,
            page_number=page_number,
            point_in_time=point_in_time,
            request_options=request_options,
        )
        return _response.data

    async def cancel_async_search(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelAsyncSearchDto:
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
        CancelAsyncSearchDto
            Cancellation request processed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.cancel_async_search(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_async_search(job_id, request_options=request_options)
        return _response.data

    async def get_async_search_status(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncSearchStatusDto:
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
        AsyncSearchStatusDto
            Successfully retrieved search job status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.get_async_search_status(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_async_search_status(job_id, request_options=request_options)
        return _response.data

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
    ) -> typing.List[EntityResultDto]:
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
        typing.List[EntityResultDto]
            Search executed successfully

        Examples
        --------
        import asyncio

        from fern import ArrayConditionDto, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.entities(
                entity_name="entityName",
                model_version=1,
                request=ArrayConditionDto(
                    type="type",
                    json_path="jsonPath",
                    operator_type="EQUALS",
                    value=["value"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.entities(
            entity_name,
            model_version,
            request=request,
            point_in_time=point_in_time,
            limit=limit,
            timeout_millis=timeout_millis,
            request_options=request_options,
        )
        return _response.data
