

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.get_v1shape_request_log import GetV1ShapeRequestLog
from .types.get_v1shape_request_replica import GetV1ShapeRequestReplica
from .types.get_v1shape_response import GetV1ShapeResponse
from .types.post_v1shape_request_log import PostV1ShapeRequestLog
from .types.post_v1shape_request_replica import PostV1ShapeRequestReplica
from .types.post_v1shape_response import PostV1ShapeResponse


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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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

    def get_shape(
        self,
        *,
        table: str,
        offset: str,
        live: typing.Optional[bool] = None,
        live_sse: typing.Optional[bool] = None,
        experimental_live_sse: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        where: typing.Optional[str] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        columns: typing.Optional[str] = None,
        queryable_columns: typing.Optional[str] = None,
        replica: typing.Optional[GetV1ShapeRequestReplica] = None,
        log: typing.Optional[GetV1ShapeRequestLog] = None,
        subset_where: typing.Optional[str] = None,
        subset_params: typing.Optional[str] = None,
        subset_limit: typing.Optional[int] = None,
        subset_offset: typing.Optional[int] = None,
        subset_order_by: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ShapeResponse:
        """
        Load the initial data for a shape and poll for real-time updates.
        
        Define your shape using the `table` and `where` parameters.
        Use `offset` to fetch data from a specific position in the shape
        log and the `live` parameter to consume real-time updates.
        
        Parameters
        ----------
        table : str
            Root table of the shape. Must match a table in your Postgres database.
            
            Can be just a tablename, or can be prefixed by the database schema
            using a `.` delimiter, such as `foo.issues`. If you don't provide
            a schema prefix, then the table is assumed to be in the `public.` schema.
        
        offset : str
            The offset in the shape stream. This is like a cursor that specifies
            the position in the shape log to request data from.
            
            When making an initial request to sync a shape from scratch, you
            **must** set the `offset` to `-1`. Then, when continuing to
            sync data, you should set the `offset` to the last offset you have
            already received, to continue syncing new data from that position
            in the stream.
            
            Alternatively, you can set `offset` to `now` to skip all historical
            data and receive an immediate up-to-date message with the latest
            continuation offset. This is useful when combined with `log=changes_only`
            mode and `replica=full` for applications that don't need historical data.
            
            Note that when `offset` is not `-1` or `now` then you must also provide
            the shape's `handle`.
        
        live : typing.Optional[bool]
            Whether to wait for live updates or not.
            
            When the `live` parameter is omitted or set to `false`, the server
            will always return immediately, with any data it has, followed by an
            up-to-date message.
            
            Once you're up-to-date, you should set the `live` parameter to `true`.
            This puts the server into live mode, where it will hold open the
            connection, waiting for new data arrive.
            
            This allows you to implement a long-polling strategy to consume
            real-time updates.
        
        live_sse : typing.Optional[bool]
            Use Server-Sent Events (SSE) for live updates instead of long polling.
            
            When set to `true` along with `live=true`, the server will use SSE
            to stream updates to the client. SSE provides a persistent connection
            that allows the server to push updates as they happen, which is more
            efficient than long polling.
            
            SSE messages are sent in the standard SSE format with `data:` prefixes.
            The stream includes data messages (shape log entries), control messages
            (up-to-date, must-refetch, etc.), and keep-alive comments sent every
            21 seconds to prevent connection timeout.
            
            **Important**: SSE requires that reverse proxies and CDNs support
            streaming responses without buffering. Configure your proxy accordingly:
            - Nginx: `proxy_buffering off;`
            - Caddy: `flush_interval -1`
            - Apache: `flushpackets=on`
            
            SSE can only be enabled when `live` is also `true`.
        
        experimental_live_sse : typing.Optional[bool]
            Deprecated in favor of `live_sse`. Use `live_sse` instead.
            This parameter will be removed in a future version.
        
        cursor : typing.Optional[str]
            This is a cursor generated by the server during live requests. It helps bust caches for
            responses from previous long-polls.
        
        handle : typing.Optional[str]
            The shape handle returned by the initial shape request.
            
            This is a required parameter when this is not an initial sync request,
            i.e. when offset is not `-1`.
        
        where : typing.Optional[str]
            Optional where clause to filter rows in the `table`.
            
            This should be a valid PostgreSQL WHERE clause using SQL syntax.
            
            For more details on what is supported and what is optimal,
            see the [where clause documentation](https://electric-sql.com/docs/sync/guides/shapes#where-clause).
            
            If this where clause uses a positional parameter, it's value must be provided under `params[n]=`
            query parameter.
        
        params : typing.Optional[typing.Dict[str, typing.Any]]
            Optional params to replace inside the where clause. Uses an "exploded object" syntax (see examples).
            
            These values will be safely interpolated inside the where clause, so you don't need to worry about
            escaping user input when building a where clause.
            
            If where clause mentions a posisional parameter, it becomes required to provide it.
        
        columns : typing.Optional[str]
            Optional list of columns to sync in the rows from the `table`.
            
            This is a projection setting for reducing the data sent to the client.
            If `queryable_columns` is set, `columns` may only include columns from
            that allow-list. If `queryable_columns` is set and `columns` is omitted,
            Electric syncs the queryable columns by default.
            
            They should always include the primary key columns, and should be formed
            as a comma separated list of column names exactly as they are in the database schema.
            
            If the identifier was defined as case sensitive and/or with special characters, then\\
            you must quote it in the `columns` parameter as well.
        
        queryable_columns : typing.Optional[str]
            Optional list of columns that may be referenced by subset WHERE clauses,
            subset ORDER BY clauses, and the `columns` projection.
            
            This is an allow-list for what client-controlled subset requests may query
            or sync. It does not force every listed column to be synced, and it does
            not restrict the main shape WHERE clause.
            
            Queryable columns should always include the primary key columns, and should
            be formed as a comma separated list of column names exactly as they are in
            the database schema.
        
        replica : typing.Optional[GetV1ShapeRequestReplica]
            Modifies the data sent in update and delete change messages.
            
            When `replica=default` (the default) only changed columns are
            included in the `value` of an update message and only the primary
            keys are sent for a delete.
            
            When set to `full` the entire row will be sent for updates and
            deletes. `old_value` will also be present on update messages,
            containing the previous value for changed columns.
            
            Note that insert operations always include the full row,
            in either mode.
        
        log : typing.Optional[GetV1ShapeRequestLog]
            Controls the initial data loading mode for the shape.
            
            When `log=full` (the default), the server creates an initial snapshot
            of all data matching the shape definition and streams it to the client
            before delivering real-time updates.
            
            When `log=changes_only`, the server skips the initial snapshot creation.
            The client will only receive changes that occur after the shape is
            established, without seeing the base data. This is useful for:
            
            - Event streams where historical data isn't needed
            - Applications that fetch their initial state through `subset__*` parameters
            - Reducing initial sync time when combined with `offset=now`
            
            In `changes_only` mode, you can use the client's `requestSnapshot` method
            to fetch subsets of data on-demand while tracking which changes to skip.
        
        subset_where : typing.Optional[str]
            Optional WHERE clause to filter a subset of the shape data.
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
            
            This allows you to fetch a specific portion of the shape's data with
            additional filtering beyond the main shape's WHERE clause. This filter is
            always applied in addition to the main shape's WHERE clause, so it's not possible
            to get data that doesn't match the main shape's WHERE clause.
        
        subset_params : typing.Optional[str]
            Parameters for the subset WHERE clause as a JSON string.
            The JSON should be an object mapping positional parameter numbers to their values,
            for example: `{"1":"value1","2":"value2"}` to replace `$1` and `$2` in the subset WHERE clause.
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
        
        subset_limit : typing.Optional[int]
            Maximum number of rows to return in the subset snapshot.
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
            
            When `limit` or `offset` is specified, `subset__order_by` becomes required.
        
        subset_offset : typing.Optional[int]
            Number of rows to skip in the subset snapshot (for pagination).
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
            
            When `limit` or `offset` is specified, `subset__order_by` becomes required.
        
        subset_order_by : typing.Optional[str]
            ORDER BY clause for the subset snapshot, determining the row ordering. Uses
            same syntax as `ORDER BY` clause in PostgreSQL.
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
            
            This becomes required when using `subset__limit` or `subset__offset`.
        
        secret : typing.Optional[str]
            Secret defined by the [ELECTRIC_SECRET](https://electric-sql.com/docs/api/config#electric-secret)
            configuration variable. This is required unless
            `ELECTRIC_INSECURE` is set to `true`. More details are
            available in the [security guide](https://electric-sql.com/docs/guides/security).
        
        api_secret : typing.Optional[str]
            Deprecated in favor of the `secret` query parameter.
            Will be removed in v2.
        
        if_none_match : typing.Optional[str]
            Re-validate the shape if the etag doesn't match.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        GetV1ShapeResponse
            The shape request was successful.
        
        Examples
        --------
        from fern import FernApi
        
        client = FernApi()
        client.get_shape(
            table="issues",
            offset="-1",
            handle="3833821-1721812114261",
            where="\"title = 'Electric'\"\n",
            columns="id,title,status",
            queryable_columns="id,title,org_id",
            subset_where="status = 'active'",
            subset_params='{"1":"high"}',
            subset_order_by="created_at DESC",
            secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
            api_secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
        )
        """
        _response = self._raw_client.get_shape(
            table=table,
            offset=offset,
            live=live,
            live_sse=live_sse,
            experimental_live_sse=experimental_live_sse,
            cursor=cursor,
            handle=handle,
            where=where,
            params=params,
            columns=columns,
            queryable_columns=queryable_columns,
            replica=replica,
            log=log,
            subset_where=subset_where,
            subset_params=subset_params,
            subset_limit=subset_limit,
            subset_offset=subset_offset,
            subset_order_by=subset_order_by,
            secret=secret,
            api_secret=api_secret,
            if_none_match=if_none_match,
            request_options=request_options,
        )
        return _response.data

    def get_shape_with_subset_post(
        self,
        *,
        table: str,
        offset: str,
        handle: typing.Optional[str] = None,
        where: typing.Optional[str] = None,
        columns: typing.Optional[str] = None,
        queryable_columns: typing.Optional[str] = None,
        replica: typing.Optional[PostV1ShapeRequestReplica] = None,
        log: typing.Optional[PostV1ShapeRequestLog] = None,
        secret: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        post_v1shape_request_where: typing.Optional[str] = OMIT,
        params: typing.Optional[typing.Dict[str, str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        post_v1shape_request_offset: typing.Optional[int] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1ShapeResponse:
        """
        Request a subset snapshot using POST with parameters in the request body.

        **This is the recommended method for subset snapshots.** POST requests send
        subset parameters in the request body as JSON, avoiding URL length limits
        (HTTP 414 errors) that can occur with complex WHERE clauses or many parameters.

        This is particularly important for queries with large parameter lists, such as
        `WHERE id = ANY($1)` with hundreds of IDs (common in join queries).

        In Electric 2.0, GET requests for subset snapshots will be deprecated and
        only POST will be supported.

        The shape definition (`table`, `handle`, `offset`, etc.) is still provided
        as query parameters, while subset parameters (`where`, `params`, `limit`,
        `offset`, `order_by`) are provided in the JSON request body.

        Parameters
        ----------
        table : str
            Root table of the shape. Must match a table in your Postgres database.

        offset : str
            The offset in the shape stream.

        handle : typing.Optional[str]
            The shape handle returned by the initial shape request.
            Required when offset is not `-1`.

        where : typing.Optional[str]
            Optional main shape WHERE clause to filter rows in the `table`.

        columns : typing.Optional[str]
            Optional list of columns to sync in the rows.

        queryable_columns : typing.Optional[str]
            Optional list of columns that may be referenced by subset filters,
            subset ordering, and the columns projection. It does not restrict the
            main shape WHERE clause.

        replica : typing.Optional[PostV1ShapeRequestReplica]
            Modifies the data sent in update and delete change messages.

        log : typing.Optional[PostV1ShapeRequestLog]
            Controls the initial data loading mode for the shape.

        secret : typing.Optional[str]
            Secret defined by the [ELECTRIC_SECRET](https://electric-sql.com/docs/api/config#electric-secret)
            configuration variable. This is required unless
            `ELECTRIC_INSECURE` is set to `true`. More details are
            available in the [security guide](https://electric-sql.com/docs/guides/security).

        api_secret : typing.Optional[str]
            Deprecated in favor of the `secret` query parameter.
            Will be removed in v2.

        post_v1shape_request_where : typing.Optional[str]
            WHERE clause to filter the subset of data.

            This filter is applied in addition to the main shape's WHERE clause.

        params : typing.Optional[typing.Dict[str, str]]
            Parameters for the WHERE clause as an object mapping positional
            parameter numbers to their values.

        limit : typing.Optional[int]
            Maximum number of rows to return in the subset snapshot.

        post_v1shape_request_offset : typing.Optional[int]
            Number of rows to skip in the subset snapshot (for pagination).

        order_by : typing.Optional[str]
            ORDER BY clause for the subset snapshot. Required when using
            `limit` or `offset`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1ShapeResponse
            The subset snapshot request was successful.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_shape_with_subset_post(
            table="table",
            offset="offset",
            secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
            api_secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
            post_v1shape_request_where="status = 'active'",
        )
        """
        _response = self._raw_client.get_shape_with_subset_post(
            table=table,
            offset=offset,
            handle=handle,
            where=where,
            columns=columns,
            queryable_columns=queryable_columns,
            replica=replica,
            log=log,
            secret=secret,
            api_secret=api_secret,
            post_v1shape_request_where=post_v1shape_request_where,
            params=params,
            limit=limit,
            post_v1shape_request_offset=post_v1shape_request_offset,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def delete_shape(
        self,
        *,
        table: str,
        source_id: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes the shape from the Electric sync engine.

        This clears the shape log and forces any clients requesting the shape
        to create a new shape and resync from scratch.

        **NOTE** Delete shape only works if Electric is configured to `allow_shape_deletion`.

        Parameters
        ----------
        table : str
            The name of the table for which to delete the shape.

            Can be qualified by the schema name.

        source_id : typing.Optional[str]
            The ID of the database from which to delete the shape.
            This is required only if Electric manages several databases.

        handle : typing.Optional[str]
            Optional, deletes the current shape if it matches the `handle` provided. If not provided, deletes the current shape.

        secret : typing.Optional[str]
            Secret defined by the [ELECTRIC_SECRET](https://electric-sql.com/docs/api/config#electric-secret)
            configuration variable. This is required unless
            `ELECTRIC_INSECURE` is set to `true`. More details are
            available in the [security guide](https://electric-sql.com/docs/guides/security).

        api_secret : typing.Optional[str]
            Deprecated in favor of the `secret` query parameter.
            Will be removed in v2.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.delete_shape(
            table="issues",
            handle="3833821-1721812114261",
            secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
            api_secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
        )
        """
        _response = self._raw_client.delete_shape(
            table=table,
            source_id=source_id,
            handle=handle,
            secret=secret,
            api_secret=api_secret,
            request_options=request_options,
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

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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

    async def get_shape(
        self,
        *,
        table: str,
        offset: str,
        live: typing.Optional[bool] = None,
        live_sse: typing.Optional[bool] = None,
        experimental_live_sse: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        where: typing.Optional[str] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        columns: typing.Optional[str] = None,
        queryable_columns: typing.Optional[str] = None,
        replica: typing.Optional[GetV1ShapeRequestReplica] = None,
        log: typing.Optional[GetV1ShapeRequestLog] = None,
        subset_where: typing.Optional[str] = None,
        subset_params: typing.Optional[str] = None,
        subset_limit: typing.Optional[int] = None,
        subset_offset: typing.Optional[int] = None,
        subset_order_by: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ShapeResponse:
        """
        Load the initial data for a shape and poll for real-time updates.
        
        Define your shape using the `table` and `where` parameters.
        Use `offset` to fetch data from a specific position in the shape
        log and the `live` parameter to consume real-time updates.
        
        Parameters
        ----------
        table : str
            Root table of the shape. Must match a table in your Postgres database.
            
            Can be just a tablename, or can be prefixed by the database schema
            using a `.` delimiter, such as `foo.issues`. If you don't provide
            a schema prefix, then the table is assumed to be in the `public.` schema.
        
        offset : str
            The offset in the shape stream. This is like a cursor that specifies
            the position in the shape log to request data from.
            
            When making an initial request to sync a shape from scratch, you
            **must** set the `offset` to `-1`. Then, when continuing to
            sync data, you should set the `offset` to the last offset you have
            already received, to continue syncing new data from that position
            in the stream.
            
            Alternatively, you can set `offset` to `now` to skip all historical
            data and receive an immediate up-to-date message with the latest
            continuation offset. This is useful when combined with `log=changes_only`
            mode and `replica=full` for applications that don't need historical data.
            
            Note that when `offset` is not `-1` or `now` then you must also provide
            the shape's `handle`.
        
        live : typing.Optional[bool]
            Whether to wait for live updates or not.
            
            When the `live` parameter is omitted or set to `false`, the server
            will always return immediately, with any data it has, followed by an
            up-to-date message.
            
            Once you're up-to-date, you should set the `live` parameter to `true`.
            This puts the server into live mode, where it will hold open the
            connection, waiting for new data arrive.
            
            This allows you to implement a long-polling strategy to consume
            real-time updates.
        
        live_sse : typing.Optional[bool]
            Use Server-Sent Events (SSE) for live updates instead of long polling.
            
            When set to `true` along with `live=true`, the server will use SSE
            to stream updates to the client. SSE provides a persistent connection
            that allows the server to push updates as they happen, which is more
            efficient than long polling.
            
            SSE messages are sent in the standard SSE format with `data:` prefixes.
            The stream includes data messages (shape log entries), control messages
            (up-to-date, must-refetch, etc.), and keep-alive comments sent every
            21 seconds to prevent connection timeout.
            
            **Important**: SSE requires that reverse proxies and CDNs support
            streaming responses without buffering. Configure your proxy accordingly:
            - Nginx: `proxy_buffering off;`
            - Caddy: `flush_interval -1`
            - Apache: `flushpackets=on`
            
            SSE can only be enabled when `live` is also `true`.
        
        experimental_live_sse : typing.Optional[bool]
            Deprecated in favor of `live_sse`. Use `live_sse` instead.
            This parameter will be removed in a future version.
        
        cursor : typing.Optional[str]
            This is a cursor generated by the server during live requests. It helps bust caches for
            responses from previous long-polls.
        
        handle : typing.Optional[str]
            The shape handle returned by the initial shape request.
            
            This is a required parameter when this is not an initial sync request,
            i.e. when offset is not `-1`.
        
        where : typing.Optional[str]
            Optional where clause to filter rows in the `table`.
            
            This should be a valid PostgreSQL WHERE clause using SQL syntax.
            
            For more details on what is supported and what is optimal,
            see the [where clause documentation](https://electric-sql.com/docs/sync/guides/shapes#where-clause).
            
            If this where clause uses a positional parameter, it's value must be provided under `params[n]=`
            query parameter.
        
        params : typing.Optional[typing.Dict[str, typing.Any]]
            Optional params to replace inside the where clause. Uses an "exploded object" syntax (see examples).
            
            These values will be safely interpolated inside the where clause, so you don't need to worry about
            escaping user input when building a where clause.
            
            If where clause mentions a posisional parameter, it becomes required to provide it.
        
        columns : typing.Optional[str]
            Optional list of columns to sync in the rows from the `table`.
            
            This is a projection setting for reducing the data sent to the client.
            If `queryable_columns` is set, `columns` may only include columns from
            that allow-list. If `queryable_columns` is set and `columns` is omitted,
            Electric syncs the queryable columns by default.
            
            They should always include the primary key columns, and should be formed
            as a comma separated list of column names exactly as they are in the database schema.
            
            If the identifier was defined as case sensitive and/or with special characters, then\\
            you must quote it in the `columns` parameter as well.
        
        queryable_columns : typing.Optional[str]
            Optional list of columns that may be referenced by subset WHERE clauses,
            subset ORDER BY clauses, and the `columns` projection.
            
            This is an allow-list for what client-controlled subset requests may query
            or sync. It does not force every listed column to be synced, and it does
            not restrict the main shape WHERE clause.
            
            Queryable columns should always include the primary key columns, and should
            be formed as a comma separated list of column names exactly as they are in
            the database schema.
        
        replica : typing.Optional[GetV1ShapeRequestReplica]
            Modifies the data sent in update and delete change messages.
            
            When `replica=default` (the default) only changed columns are
            included in the `value` of an update message and only the primary
            keys are sent for a delete.
            
            When set to `full` the entire row will be sent for updates and
            deletes. `old_value` will also be present on update messages,
            containing the previous value for changed columns.
            
            Note that insert operations always include the full row,
            in either mode.
        
        log : typing.Optional[GetV1ShapeRequestLog]
            Controls the initial data loading mode for the shape.
            
            When `log=full` (the default), the server creates an initial snapshot
            of all data matching the shape definition and streams it to the client
            before delivering real-time updates.
            
            When `log=changes_only`, the server skips the initial snapshot creation.
            The client will only receive changes that occur after the shape is
            established, without seeing the base data. This is useful for:
            
            - Event streams where historical data isn't needed
            - Applications that fetch their initial state through `subset__*` parameters
            - Reducing initial sync time when combined with `offset=now`
            
            In `changes_only` mode, you can use the client's `requestSnapshot` method
            to fetch subsets of data on-demand while tracking which changes to skip.
        
        subset_where : typing.Optional[str]
            Optional WHERE clause to filter a subset of the shape data.
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
            
            This allows you to fetch a specific portion of the shape's data with
            additional filtering beyond the main shape's WHERE clause. This filter is
            always applied in addition to the main shape's WHERE clause, so it's not possible
            to get data that doesn't match the main shape's WHERE clause.
        
        subset_params : typing.Optional[str]
            Parameters for the subset WHERE clause as a JSON string.
            The JSON should be an object mapping positional parameter numbers to their values,
            for example: `{"1":"value1","2":"value2"}` to replace `$1` and `$2` in the subset WHERE clause.
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
        
        subset_limit : typing.Optional[int]
            Maximum number of rows to return in the subset snapshot.
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
            
            When `limit` or `offset` is specified, `subset__order_by` becomes required.
        
        subset_offset : typing.Optional[int]
            Number of rows to skip in the subset snapshot (for pagination).
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
            
            When `limit` or `offset` is specified, `subset__order_by` becomes required.
        
        subset_order_by : typing.Optional[str]
            ORDER BY clause for the subset snapshot, determining the row ordering. Uses
            same syntax as `ORDER BY` clause in PostgreSQL.
            
            Presence of this or other `subset__*` parameters in the request makes the server
            return a subset snapshot instead of the regular shape sync.
            
            This becomes required when using `subset__limit` or `subset__offset`.
        
        secret : typing.Optional[str]
            Secret defined by the [ELECTRIC_SECRET](https://electric-sql.com/docs/api/config#electric-secret)
            configuration variable. This is required unless
            `ELECTRIC_INSECURE` is set to `true`. More details are
            available in the [security guide](https://electric-sql.com/docs/guides/security).
        
        api_secret : typing.Optional[str]
            Deprecated in favor of the `secret` query parameter.
            Will be removed in v2.
        
        if_none_match : typing.Optional[str]
            Re-validate the shape if the etag doesn't match.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        GetV1ShapeResponse
            The shape request was successful.
        
        Examples
        --------
        import asyncio
        
        from fern import AsyncFernApi
        
        client = AsyncFernApi()
        
        
        async def main() -> None:
            await client.get_shape(
                table="issues",
                offset="-1",
                handle="3833821-1721812114261",
                where="\"title = 'Electric'\"\n",
                columns="id,title,status",
                queryable_columns="id,title,org_id",
                subset_where="status = 'active'",
                subset_params='{"1":"high"}',
                subset_order_by="created_at DESC",
                secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
                api_secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
            )
        
        
        asyncio.run(main())
        """
        _response = await self._raw_client.get_shape(
            table=table,
            offset=offset,
            live=live,
            live_sse=live_sse,
            experimental_live_sse=experimental_live_sse,
            cursor=cursor,
            handle=handle,
            where=where,
            params=params,
            columns=columns,
            queryable_columns=queryable_columns,
            replica=replica,
            log=log,
            subset_where=subset_where,
            subset_params=subset_params,
            subset_limit=subset_limit,
            subset_offset=subset_offset,
            subset_order_by=subset_order_by,
            secret=secret,
            api_secret=api_secret,
            if_none_match=if_none_match,
            request_options=request_options,
        )
        return _response.data

    async def get_shape_with_subset_post(
        self,
        *,
        table: str,
        offset: str,
        handle: typing.Optional[str] = None,
        where: typing.Optional[str] = None,
        columns: typing.Optional[str] = None,
        queryable_columns: typing.Optional[str] = None,
        replica: typing.Optional[PostV1ShapeRequestReplica] = None,
        log: typing.Optional[PostV1ShapeRequestLog] = None,
        secret: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        post_v1shape_request_where: typing.Optional[str] = OMIT,
        params: typing.Optional[typing.Dict[str, str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        post_v1shape_request_offset: typing.Optional[int] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1ShapeResponse:
        """
        Request a subset snapshot using POST with parameters in the request body.

        **This is the recommended method for subset snapshots.** POST requests send
        subset parameters in the request body as JSON, avoiding URL length limits
        (HTTP 414 errors) that can occur with complex WHERE clauses or many parameters.

        This is particularly important for queries with large parameter lists, such as
        `WHERE id = ANY($1)` with hundreds of IDs (common in join queries).

        In Electric 2.0, GET requests for subset snapshots will be deprecated and
        only POST will be supported.

        The shape definition (`table`, `handle`, `offset`, etc.) is still provided
        as query parameters, while subset parameters (`where`, `params`, `limit`,
        `offset`, `order_by`) are provided in the JSON request body.

        Parameters
        ----------
        table : str
            Root table of the shape. Must match a table in your Postgres database.

        offset : str
            The offset in the shape stream.

        handle : typing.Optional[str]
            The shape handle returned by the initial shape request.
            Required when offset is not `-1`.

        where : typing.Optional[str]
            Optional main shape WHERE clause to filter rows in the `table`.

        columns : typing.Optional[str]
            Optional list of columns to sync in the rows.

        queryable_columns : typing.Optional[str]
            Optional list of columns that may be referenced by subset filters,
            subset ordering, and the columns projection. It does not restrict the
            main shape WHERE clause.

        replica : typing.Optional[PostV1ShapeRequestReplica]
            Modifies the data sent in update and delete change messages.

        log : typing.Optional[PostV1ShapeRequestLog]
            Controls the initial data loading mode for the shape.

        secret : typing.Optional[str]
            Secret defined by the [ELECTRIC_SECRET](https://electric-sql.com/docs/api/config#electric-secret)
            configuration variable. This is required unless
            `ELECTRIC_INSECURE` is set to `true`. More details are
            available in the [security guide](https://electric-sql.com/docs/guides/security).

        api_secret : typing.Optional[str]
            Deprecated in favor of the `secret` query parameter.
            Will be removed in v2.

        post_v1shape_request_where : typing.Optional[str]
            WHERE clause to filter the subset of data.

            This filter is applied in addition to the main shape's WHERE clause.

        params : typing.Optional[typing.Dict[str, str]]
            Parameters for the WHERE clause as an object mapping positional
            parameter numbers to their values.

        limit : typing.Optional[int]
            Maximum number of rows to return in the subset snapshot.

        post_v1shape_request_offset : typing.Optional[int]
            Number of rows to skip in the subset snapshot (for pagination).

        order_by : typing.Optional[str]
            ORDER BY clause for the subset snapshot. Required when using
            `limit` or `offset`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1ShapeResponse
            The subset snapshot request was successful.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_shape_with_subset_post(
                table="table",
                offset="offset",
                secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
                api_secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
                post_v1shape_request_where="status = 'active'",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_shape_with_subset_post(
            table=table,
            offset=offset,
            handle=handle,
            where=where,
            columns=columns,
            queryable_columns=queryable_columns,
            replica=replica,
            log=log,
            secret=secret,
            api_secret=api_secret,
            post_v1shape_request_where=post_v1shape_request_where,
            params=params,
            limit=limit,
            post_v1shape_request_offset=post_v1shape_request_offset,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def delete_shape(
        self,
        *,
        table: str,
        source_id: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes the shape from the Electric sync engine.

        This clears the shape log and forces any clients requesting the shape
        to create a new shape and resync from scratch.

        **NOTE** Delete shape only works if Electric is configured to `allow_shape_deletion`.

        Parameters
        ----------
        table : str
            The name of the table for which to delete the shape.

            Can be qualified by the schema name.

        source_id : typing.Optional[str]
            The ID of the database from which to delete the shape.
            This is required only if Electric manages several databases.

        handle : typing.Optional[str]
            Optional, deletes the current shape if it matches the `handle` provided. If not provided, deletes the current shape.

        secret : typing.Optional[str]
            Secret defined by the [ELECTRIC_SECRET](https://electric-sql.com/docs/api/config#electric-secret)
            configuration variable. This is required unless
            `ELECTRIC_INSECURE` is set to `true`. More details are
            available in the [security guide](https://electric-sql.com/docs/guides/security).

        api_secret : typing.Optional[str]
            Deprecated in favor of the `secret` query parameter.
            Will be removed in v2.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.delete_shape(
                table="issues",
                handle="3833821-1721812114261",
                secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
                api_secret="1U6ItbhoQb4kGUU5wXBLbxvNf",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_shape(
            table=table,
            source_id=source_id,
            handle=handle,
            secret=secret,
            api_secret=api_secret,
            request_options=request_options,
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
