

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.events_remediations_get_response import EventsRemediationsGetResponse
from ..types.sessions_get_response import SessionsGetResponse
from ..types.sessions_session_id_get_response import SessionsSessionIdGetResponse
from .raw_client import AsyncRawSessionsClient, RawSessionsClient


class SessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSessionsClient
        """
        return self._raw_client

    def list_sessions_with_optional_status_filtering_and_pagination(
        self,
        *,
        limit: int,
        offset: int,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionsGetResponse:
        """
        List sessions with optional status filtering and pagination

        Parameters
        ----------
        limit : int
            Max results per page

        offset : int
            Pagination offset

        status : typing.Optional[str]
            Filter by session status (e.g., analysis_complete, failed, investigating)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionsGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sessions.list_sessions_with_optional_status_filtering_and_pagination(
            limit=1,
            offset=1,
        )
        """
        _response = self._raw_client.list_sessions_with_optional_status_filtering_and_pagination(
            limit=limit, offset=offset, status=status, request_options=request_options
        )
        return _response.data

    def get_raw_session_data_for_any_tool_type_remediate_query_recommend_etc(
        self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionsSessionIdGetResponse:
        """
        Get raw session data for any tool type (remediate, query, recommend, etc.)

        Parameters
        ----------
        session_id : str
            Session ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionsSessionIdGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sessions.get_raw_session_data_for_any_tool_type_remediate_query_recommend_etc(
            session_id="sessionId",
        )
        """
        _response = self._raw_client.get_raw_session_data_for_any_tool_type_remediate_query_recommend_etc(
            session_id, request_options=request_options
        )
        return _response.data

    def sse_stream_for_real_time_remediation_session_events_returns_text_event_stream(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventsRemediationsGetResponse:
        """
        SSE stream for real-time remediation session events. Returns text/event-stream.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventsRemediationsGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sessions.sse_stream_for_real_time_remediation_session_events_returns_text_event_stream()
        """
        _response = self._raw_client.sse_stream_for_real_time_remediation_session_events_returns_text_event_stream(
            request_options=request_options
        )
        return _response.data


class AsyncSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSessionsClient
        """
        return self._raw_client

    async def list_sessions_with_optional_status_filtering_and_pagination(
        self,
        *,
        limit: int,
        offset: int,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionsGetResponse:
        """
        List sessions with optional status filtering and pagination

        Parameters
        ----------
        limit : int
            Max results per page

        offset : int
            Pagination offset

        status : typing.Optional[str]
            Filter by session status (e.g., analysis_complete, failed, investigating)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionsGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sessions.list_sessions_with_optional_status_filtering_and_pagination(
                limit=1,
                offset=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sessions_with_optional_status_filtering_and_pagination(
            limit=limit, offset=offset, status=status, request_options=request_options
        )
        return _response.data

    async def get_raw_session_data_for_any_tool_type_remediate_query_recommend_etc(
        self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionsSessionIdGetResponse:
        """
        Get raw session data for any tool type (remediate, query, recommend, etc.)

        Parameters
        ----------
        session_id : str
            Session ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionsSessionIdGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sessions.get_raw_session_data_for_any_tool_type_remediate_query_recommend_etc(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_raw_session_data_for_any_tool_type_remediate_query_recommend_etc(
            session_id, request_options=request_options
        )
        return _response.data

    async def sse_stream_for_real_time_remediation_session_events_returns_text_event_stream(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventsRemediationsGetResponse:
        """
        SSE stream for real-time remediation session events. Returns text/event-stream.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventsRemediationsGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sessions.sse_stream_for_real_time_remediation_session_events_returns_text_event_stream()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.sse_stream_for_real_time_remediation_session_events_returns_text_event_stream(
                request_options=request_options
            )
        )
        return _response.data
