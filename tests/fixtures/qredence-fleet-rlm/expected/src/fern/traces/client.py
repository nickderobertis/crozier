

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.trace_feedback_response import TraceFeedbackResponse
from .raw_client import AsyncRawTracesClient, RawTracesClient


OMIT = typing.cast(typing.Any, ...)


class TracesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTracesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTracesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTracesClient
        """
        return self._raw_client

    def submit_trace_feedback(
        self,
        session_id: str,
        *,
        trace_id: str,
        value: bool,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TraceFeedbackResponse:
        """
        Record human feedback for an execution trace owned by this Session.

        Parameters
        ----------
        session_id : str

        trace_id : str

        value : bool

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceFeedbackResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.traces.submit_trace_feedback(
            session_id="session_id",
            trace_id="trace_id",
            value=True,
        )
        """
        _response = self._raw_client.submit_trace_feedback(
            session_id, trace_id=trace_id, value=value, comment=comment, request_options=request_options
        )
        return _response.data


class AsyncTracesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTracesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTracesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTracesClient
        """
        return self._raw_client

    async def submit_trace_feedback(
        self,
        session_id: str,
        *,
        trace_id: str,
        value: bool,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TraceFeedbackResponse:
        """
        Record human feedback for an execution trace owned by this Session.

        Parameters
        ----------
        session_id : str

        trace_id : str

        value : bool

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceFeedbackResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.traces.submit_trace_feedback(
                session_id="session_id",
                trace_id="trace_id",
                value=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_trace_feedback(
            session_id, trace_id=trace_id, value=value, comment=comment, request_options=request_options
        )
        return _response.data
