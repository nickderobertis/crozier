

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.session import Session
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

    def get_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Session:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            The session.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sessions.get_session(
            session_id="sessionId",
        )
        """
        _response = self._raw_client.get_session(session_id, request_options=request_options)
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

    async def get_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Session:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            The session.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sessions.get_session(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_session(session_id, request_options=request_options)
        return _response.data
