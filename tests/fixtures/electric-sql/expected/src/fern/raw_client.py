

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .errors.bad_request_error import BadRequestError
from .errors.conflict_error import ConflictError
from .errors.content_too_large_error import ContentTooLargeError
from .errors.not_found_error import NotFoundError
from .errors.too_many_requests_error import TooManyRequestsError
from .types.conflict_error_body_item import ConflictErrorBodyItem
from .types.get_v1shape_request_log import GetV1ShapeRequestLog
from .types.get_v1shape_request_replica import GetV1ShapeRequestReplica
from .types.get_v1shape_response import GetV1ShapeResponse
from .types.post_v1shape_request_log import PostV1ShapeRequestLog
from .types.post_v1shape_request_replica import PostV1ShapeRequestReplica
from .types.post_v1shape_response import PostV1ShapeResponse
from .types.too_many_requests_error_body import TooManyRequestsErrorBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[GetV1ShapeResponse]:
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
        HttpResponse[GetV1ShapeResponse]
            The shape request was successful.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/shape",
            method="GET",
            params={
                "table": table,
                "offset": offset,
                "live": live,
                "live_sse": live_sse,
                "experimental_live_sse": experimental_live_sse,
                "cursor": cursor,
                "handle": handle,
                "where": where,
                "params": params,
                "columns": columns,
                "queryable_columns": queryable_columns,
                "replica": replica,
                "log": log,
                "subset__where": subset_where,
                "subset__params": subset_params,
                "subset__limit": subset_limit,
                "subset__offset": subset_offset,
                "subset__order_by": subset_order_by,
                "secret": secret,
                "api_secret": api_secret,
            },
            headers={
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1ShapeResponse,
                    parse_obj_as(
                        type_=GetV1ShapeResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.List[ConflictErrorBodyItem],
                        parse_obj_as(
                            type_=typing.List[ConflictErrorBodyItem],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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
    ) -> HttpResponse[PostV1ShapeResponse]:
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
        HttpResponse[PostV1ShapeResponse]
            The subset snapshot request was successful.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/shape",
            method="POST",
            params={
                "table": table,
                "offset": offset,
                "handle": handle,
                "where": where,
                "columns": columns,
                "queryable_columns": queryable_columns,
                "replica": replica,
                "log": log,
                "secret": secret,
                "api_secret": api_secret,
            },
            json={
                "where": post_v1shape_request_where,
                "params": params,
                "limit": limit,
                "offset": post_v1shape_request_offset,
                "order_by": order_by,
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
                    PostV1ShapeResponse,
                    parse_obj_as(
                        type_=PostV1ShapeResponse,
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
            if _response.status_code == 413:
                raise ContentTooLargeError(
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

    def delete_shape(
        self,
        *,
        table: str,
        source_id: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/shape",
            method="DELETE",
            params={
                "table": table,
                "source_id": source_id,
                "handle": handle,
                "secret": secret,
                "api_secret": api_secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[GetV1ShapeResponse]:
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
        AsyncHttpResponse[GetV1ShapeResponse]
            The shape request was successful.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/shape",
            method="GET",
            params={
                "table": table,
                "offset": offset,
                "live": live,
                "live_sse": live_sse,
                "experimental_live_sse": experimental_live_sse,
                "cursor": cursor,
                "handle": handle,
                "where": where,
                "params": params,
                "columns": columns,
                "queryable_columns": queryable_columns,
                "replica": replica,
                "log": log,
                "subset__where": subset_where,
                "subset__params": subset_params,
                "subset__limit": subset_limit,
                "subset__offset": subset_offset,
                "subset__order_by": subset_order_by,
                "secret": secret,
                "api_secret": api_secret,
            },
            headers={
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1ShapeResponse,
                    parse_obj_as(
                        type_=GetV1ShapeResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.List[ConflictErrorBodyItem],
                        parse_obj_as(
                            type_=typing.List[ConflictErrorBodyItem],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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
    ) -> AsyncHttpResponse[PostV1ShapeResponse]:
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
        AsyncHttpResponse[PostV1ShapeResponse]
            The subset snapshot request was successful.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/shape",
            method="POST",
            params={
                "table": table,
                "offset": offset,
                "handle": handle,
                "where": where,
                "columns": columns,
                "queryable_columns": queryable_columns,
                "replica": replica,
                "log": log,
                "secret": secret,
                "api_secret": api_secret,
            },
            json={
                "where": post_v1shape_request_where,
                "params": params,
                "limit": limit,
                "offset": post_v1shape_request_offset,
                "order_by": order_by,
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
                    PostV1ShapeResponse,
                    parse_obj_as(
                        type_=PostV1ShapeResponse,
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
            if _response.status_code == 413:
                raise ContentTooLargeError(
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

    async def delete_shape(
        self,
        *,
        table: str,
        source_id: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        api_secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/shape",
            method="DELETE",
            params={
                "table": table,
                "source_id": source_id,
                "handle": handle,
                "secret": secret,
                "api_secret": api_secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
