

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.all_queries import AllQueries
from .types.get_queries_query_id_count_response import GetQueriesQueryIdCountResponse
from .types.post_queries_response import PostQueriesResponse
from .types.query import Query
from .types.query_criteria_group import QueryCriteriaGroup
from .types.query_field import QueryField
from .types.query_object_type import QueryObjectType
from .types.query_run_list import QueryRunList


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_a_list_of_a_recent_shared_and_study_top_queries_for_the_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AllQueries:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AllQueries
            Successfully operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_a_list_of_a_recent_shared_and_study_top_queries_for_the_current_user()
        """
        _response = self._raw_client.get_a_list_of_a_recent_shared_and_study_top_queries_for_the_current_user(
            request_options=request_options
        )
        return _response.data

    def post_queries(
        self,
        *,
        type: QueryObjectType,
        fields: typing.Sequence[QueryField],
        criteria: typing.Optional[QueryCriteriaGroup] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostQueriesResponse:
        """
        Create a new query and return the QueryID. If the same query (fields and criteria) already exists, the same QueryID will be returned instead of a new one being created.

        Parameters
        ----------
        type : QueryObjectType

        fields : typing.Sequence[QueryField]

        criteria : typing.Optional[QueryCriteriaGroup]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostQueriesResponse
            Query successfully created

        Examples
        --------
        from fern import FernApi, QueryField, QueryObjectType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.post_queries(
            type=QueryObjectType.CANDIDATES,
            fields=[
                QueryField(
                    module="candidate_parameters",
                    category="Identifiers",
                    field="CandID",
                )
            ],
        )
        """
        _response = self._raw_client.post_queries(
            type=type, fields=fields, criteria=criteria, request_options=request_options
        )
        return _response.data

    def get_a_list_of_a_recent_query_runs_for_the_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryRunList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryRunList
            Successfully operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_a_list_of_a_recent_query_runs_for_the_current_user()
        """
        _response = self._raw_client.get_a_list_of_a_recent_query_runs_for_the_current_user(
            request_options=request_options
        )
        return _response.data

    def get_queries_query_id(self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Query:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Query
            The Query was successfully retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_queries_query_id(
            query_id=1,
        )
        """
        _response = self._raw_client.get_queries_query_id(query_id, request_options=request_options)
        return _response.data

    def patch_queries_query_id(
        self,
        query_id: int,
        *,
        share: typing.Optional[bool] = None,
        star: typing.Optional[bool] = None,
        adminname: typing.Optional[str] = None,
        dashboardname: typing.Optional[str] = None,
        loginpagename: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        share : typing.Optional[bool]
            if true, the query will be shared. If false, it will be unshared

        star : typing.Optional[bool]
            if true, the query will be shared. If false, it will be unshared

        adminname : typing.Optional[str]
            The admin name to pin the query as. If the empty string, will be unpinned.

        dashboardname : typing.Optional[str]
            The admin name to pin the query to the dashboard as. If the empty string, will be unpinned.

        loginpagename : typing.Optional[str]
            The admin name to pin the query to the login page as. If the empty string, will be unpinned.

        name : typing.Optional[str]
            The name to set for the query for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.patch_queries_query_id(
            query_id=1,
        )
        """
        _response = self._raw_client.patch_queries_query_id(
            query_id,
            share=share,
            star=star,
            adminname=adminname,
            dashboardname=dashboardname,
            loginpagename=loginpagename,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def get_queries_query_id_run(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryRunList:
        """
        Return a list of summarizing previous runs of this query

        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryRunList
            Successfully operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_queries_query_id_run(
            query_id=1,
        )
        """
        _response = self._raw_client.get_queries_query_id_run(query_id, request_options=request_options)
        return _response.data

    def post_queries_query_id_run(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Run the query QueryID and returns the results.

        This endpoint will result in a new query run being generated, which will be returned in the queries of the user on the /queries endpoint.

        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The query was able to be successfully run

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.post_queries_query_id_run(
            query_id=1,
        )
        """
        with self._raw_client.post_queries_query_id_run(query_id, request_options=request_options) as r:
            yield from r.data

    def get_queries_query_id_count(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetQueriesQueryIdCountResponse:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQueriesQueryIdCountResponse
            A count of the number of candidate matches that would be returned if the query were to be run by the current user right now.

            This endpoint does *not* result in a new query run being generated or run the query, it only returns the count of how many candidates would match if the query *were* to be run.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_queries_query_id_count(
            query_id=1,
        )
        """
        _response = self._raw_client.get_queries_query_id_count(query_id, request_options=request_options)
        return _response.data

    def get_queries_query_id_run_query_run_id(
        self, query_id: int, query_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        query_run_id : int
            the identifier of a previous run for this QueryID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_queries_query_id_run_query_run_id(
            query_id=1,
            query_run_id=1,
        )
        """
        _response = self._raw_client.get_queries_query_id_run_query_run_id(
            query_id, query_run_id, request_options=request_options
        )
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_a_list_of_a_recent_shared_and_study_top_queries_for_the_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AllQueries:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AllQueries
            Successfully operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_a_list_of_a_recent_shared_and_study_top_queries_for_the_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_a_recent_shared_and_study_top_queries_for_the_current_user(
            request_options=request_options
        )
        return _response.data

    async def post_queries(
        self,
        *,
        type: QueryObjectType,
        fields: typing.Sequence[QueryField],
        criteria: typing.Optional[QueryCriteriaGroup] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostQueriesResponse:
        """
        Create a new query and return the QueryID. If the same query (fields and criteria) already exists, the same QueryID will be returned instead of a new one being created.

        Parameters
        ----------
        type : QueryObjectType

        fields : typing.Sequence[QueryField]

        criteria : typing.Optional[QueryCriteriaGroup]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostQueriesResponse
            Query successfully created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, QueryField, QueryObjectType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.post_queries(
                type=QueryObjectType.CANDIDATES,
                fields=[
                    QueryField(
                        module="candidate_parameters",
                        category="Identifiers",
                        field="CandID",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_queries(
            type=type, fields=fields, criteria=criteria, request_options=request_options
        )
        return _response.data

    async def get_a_list_of_a_recent_query_runs_for_the_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryRunList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryRunList
            Successfully operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_a_list_of_a_recent_query_runs_for_the_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_a_recent_query_runs_for_the_current_user(
            request_options=request_options
        )
        return _response.data

    async def get_queries_query_id(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Query:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Query
            The Query was successfully retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_queries_query_id(
                query_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queries_query_id(query_id, request_options=request_options)
        return _response.data

    async def patch_queries_query_id(
        self,
        query_id: int,
        *,
        share: typing.Optional[bool] = None,
        star: typing.Optional[bool] = None,
        adminname: typing.Optional[str] = None,
        dashboardname: typing.Optional[str] = None,
        loginpagename: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        share : typing.Optional[bool]
            if true, the query will be shared. If false, it will be unshared

        star : typing.Optional[bool]
            if true, the query will be shared. If false, it will be unshared

        adminname : typing.Optional[str]
            The admin name to pin the query as. If the empty string, will be unpinned.

        dashboardname : typing.Optional[str]
            The admin name to pin the query to the dashboard as. If the empty string, will be unpinned.

        loginpagename : typing.Optional[str]
            The admin name to pin the query to the login page as. If the empty string, will be unpinned.

        name : typing.Optional[str]
            The name to set for the query for this user.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.patch_queries_query_id(
                query_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_queries_query_id(
            query_id,
            share=share,
            star=star,
            adminname=adminname,
            dashboardname=dashboardname,
            loginpagename=loginpagename,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def get_queries_query_id_run(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryRunList:
        """
        Return a list of summarizing previous runs of this query

        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryRunList
            Successfully operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_queries_query_id_run(
                query_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queries_query_id_run(query_id, request_options=request_options)
        return _response.data

    async def post_queries_query_id_run(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Run the query QueryID and returns the results.

        This endpoint will result in a new query run being generated, which will be returned in the queries of the user on the /queries endpoint.

        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The query was able to be successfully run

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.post_queries_query_id_run(
                query_id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.post_queries_query_id_run(query_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_queries_query_id_count(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetQueriesQueryIdCountResponse:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQueriesQueryIdCountResponse
            A count of the number of candidate matches that would be returned if the query were to be run by the current user right now.

            This endpoint does *not* result in a new query run being generated or run the query, it only returns the count of how many candidates would match if the query *were* to be run.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_queries_query_id_count(
                query_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queries_query_id_count(query_id, request_options=request_options)
        return _response.data

    async def get_queries_query_id_run_query_run_id(
        self, query_id: int, query_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        query_run_id : int
            the identifier of a previous run for this QueryID.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_queries_query_id_run_query_run_id(
                query_id=1,
                query_run_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queries_query_id_run_query_run_id(
            query_id, query_run_id, request_options=request_options
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
