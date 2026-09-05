

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feedback_project_logs_item import FeedbackProjectLogsItem
from ..types.feedback_response_schema import FeedbackResponseSchema
from ..types.fetch_limit import FetchLimit
from ..types.fetch_limit_param import FetchLimitParam
from ..types.fetch_pagination_cursor import FetchPaginationCursor
from ..types.fetch_project_logs_events_response import FetchProjectLogsEventsResponse
from ..types.insert_events_response import InsertEventsResponse
from ..types.insert_project_logs_event import InsertProjectLogsEvent
from ..types.max_root_span_id import MaxRootSpanId
from ..types.max_xact_id import MaxXactId
from ..types.project_id_param import ProjectIdParam
from ..types.version import Version
from .raw_client import AsyncRawLogsClient, RawLogsClient


OMIT = typing.cast(typing.Any, ...)


class LogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLogsClient
        """
        return self._raw_client

    def post_project_logs_id_insert(
        self,
        project_id: ProjectIdParam,
        *,
        events: typing.Sequence[InsertProjectLogsEvent],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsertEventsResponse:
        """
        Insert a set of events into the project logs

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        events : typing.Sequence[InsertProjectLogsEvent]
            A list of project logs events to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsertEventsResponse
            Returns the inserted row ids

        Examples
        --------
        from fern import FernApi, InsertProjectLogsEvent

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.logs.post_project_logs_id_insert(
            project_id="project_id",
            events=[InsertProjectLogsEvent()],
        )
        """
        _response = self._raw_client.post_project_logs_id_insert(
            project_id, events=events, request_options=request_options
        )
        return _response.data

    def get_project_logs_id_fetch(
        self,
        project_id: ProjectIdParam,
        *,
        limit: typing.Optional[FetchLimitParam] = None,
        max_xact_id: typing.Optional[MaxXactId] = None,
        max_root_span_id: typing.Optional[MaxRootSpanId] = None,
        version: typing.Optional[Version] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FetchProjectLogsEventsResponse:
        """
        Fetch the events in a project logs. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        limit : typing.Optional[FetchLimitParam]
            limit the number of traces fetched

            Fetch queries may be paginated if the total result size is expected to be large (e.g. project_logs which accumulate over a long time). Note that fetch queries only support pagination in descending time order (from latest to earliest `_xact_id`. Furthermore, later pages may return rows which showed up in earlier pages, except with an earlier `_xact_id`. This happens because pagination occurs over the whole version history of the event log. You will most likely want to exclude any such duplicate, outdated rows (by `id`) from your combined result set.

            The `limit` parameter controls the number of full traces to return. So you may end up with more individual rows than the specified limit if you are fetching events containing traces.

        max_xact_id : typing.Optional[MaxXactId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        max_root_span_id : typing.Optional[MaxRootSpanId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        version : typing.Optional[Version]
            Retrieve a snapshot of events from a past time

            The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FetchProjectLogsEventsResponse
            Returns the fetched rows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.logs.get_project_logs_id_fetch(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_project_logs_id_fetch(
            project_id,
            limit=limit,
            max_xact_id=max_xact_id,
            max_root_span_id=max_root_span_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def post_project_logs_id_fetch(
        self,
        project_id: ProjectIdParam,
        *,
        limit: typing.Optional[FetchLimit] = OMIT,
        cursor: typing.Optional[FetchPaginationCursor] = OMIT,
        max_xact_id: typing.Optional[MaxXactId] = OMIT,
        max_root_span_id: typing.Optional[MaxRootSpanId] = OMIT,
        version: typing.Optional[Version] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FetchProjectLogsEventsResponse:
        """
        Fetch the events in a project logs. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        limit : typing.Optional[FetchLimit]

        cursor : typing.Optional[FetchPaginationCursor]

        max_xact_id : typing.Optional[MaxXactId]

        max_root_span_id : typing.Optional[MaxRootSpanId]

        version : typing.Optional[Version]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FetchProjectLogsEventsResponse
            Returns the fetched rows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.logs.post_project_logs_id_fetch(
            project_id="project_id",
        )
        """
        _response = self._raw_client.post_project_logs_id_fetch(
            project_id,
            limit=limit,
            cursor=cursor,
            max_xact_id=max_xact_id,
            max_root_span_id=max_root_span_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def post_project_logs_id_feedback(
        self,
        project_id: ProjectIdParam,
        *,
        feedback: typing.Sequence[FeedbackProjectLogsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedbackResponseSchema:
        """
        Log feedback for a set of project logs events

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        feedback : typing.Sequence[FeedbackProjectLogsItem]
            A list of project logs feedback items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedbackResponseSchema
            Returns a success status

        Examples
        --------
        from fern import FeedbackProjectLogsItem, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.logs.post_project_logs_id_feedback(
            project_id="project_id",
            feedback=[
                FeedbackProjectLogsItem(
                    id="id",
                )
            ],
        )
        """
        _response = self._raw_client.post_project_logs_id_feedback(
            project_id, feedback=feedback, request_options=request_options
        )
        return _response.data


class AsyncLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLogsClient
        """
        return self._raw_client

    async def post_project_logs_id_insert(
        self,
        project_id: ProjectIdParam,
        *,
        events: typing.Sequence[InsertProjectLogsEvent],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsertEventsResponse:
        """
        Insert a set of events into the project logs

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        events : typing.Sequence[InsertProjectLogsEvent]
            A list of project logs events to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsertEventsResponse
            Returns the inserted row ids

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, InsertProjectLogsEvent

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.logs.post_project_logs_id_insert(
                project_id="project_id",
                events=[InsertProjectLogsEvent()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_project_logs_id_insert(
            project_id, events=events, request_options=request_options
        )
        return _response.data

    async def get_project_logs_id_fetch(
        self,
        project_id: ProjectIdParam,
        *,
        limit: typing.Optional[FetchLimitParam] = None,
        max_xact_id: typing.Optional[MaxXactId] = None,
        max_root_span_id: typing.Optional[MaxRootSpanId] = None,
        version: typing.Optional[Version] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FetchProjectLogsEventsResponse:
        """
        Fetch the events in a project logs. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        limit : typing.Optional[FetchLimitParam]
            limit the number of traces fetched

            Fetch queries may be paginated if the total result size is expected to be large (e.g. project_logs which accumulate over a long time). Note that fetch queries only support pagination in descending time order (from latest to earliest `_xact_id`. Furthermore, later pages may return rows which showed up in earlier pages, except with an earlier `_xact_id`. This happens because pagination occurs over the whole version history of the event log. You will most likely want to exclude any such duplicate, outdated rows (by `id`) from your combined result set.

            The `limit` parameter controls the number of full traces to return. So you may end up with more individual rows than the specified limit if you are fetching events containing traces.

        max_xact_id : typing.Optional[MaxXactId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        max_root_span_id : typing.Optional[MaxRootSpanId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        version : typing.Optional[Version]
            Retrieve a snapshot of events from a past time

            The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FetchProjectLogsEventsResponse
            Returns the fetched rows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.logs.get_project_logs_id_fetch(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_logs_id_fetch(
            project_id,
            limit=limit,
            max_xact_id=max_xact_id,
            max_root_span_id=max_root_span_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def post_project_logs_id_fetch(
        self,
        project_id: ProjectIdParam,
        *,
        limit: typing.Optional[FetchLimit] = OMIT,
        cursor: typing.Optional[FetchPaginationCursor] = OMIT,
        max_xact_id: typing.Optional[MaxXactId] = OMIT,
        max_root_span_id: typing.Optional[MaxRootSpanId] = OMIT,
        version: typing.Optional[Version] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FetchProjectLogsEventsResponse:
        """
        Fetch the events in a project logs. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        limit : typing.Optional[FetchLimit]

        cursor : typing.Optional[FetchPaginationCursor]

        max_xact_id : typing.Optional[MaxXactId]

        max_root_span_id : typing.Optional[MaxRootSpanId]

        version : typing.Optional[Version]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FetchProjectLogsEventsResponse
            Returns the fetched rows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.logs.post_project_logs_id_fetch(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_project_logs_id_fetch(
            project_id,
            limit=limit,
            cursor=cursor,
            max_xact_id=max_xact_id,
            max_root_span_id=max_root_span_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def post_project_logs_id_feedback(
        self,
        project_id: ProjectIdParam,
        *,
        feedback: typing.Sequence[FeedbackProjectLogsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedbackResponseSchema:
        """
        Log feedback for a set of project logs events

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        feedback : typing.Sequence[FeedbackProjectLogsItem]
            A list of project logs feedback items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedbackResponseSchema
            Returns a success status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FeedbackProjectLogsItem

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.logs.post_project_logs_id_feedback(
                project_id="project_id",
                feedback=[
                    FeedbackProjectLogsItem(
                        id="id",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_project_logs_id_feedback(
            project_id, feedback=feedback, request_options=request_options
        )
        return _response.data
