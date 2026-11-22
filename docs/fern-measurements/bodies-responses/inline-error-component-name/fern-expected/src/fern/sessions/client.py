

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.session import Session
from .raw_client import AsyncRawSessionsClient, RawSessionsClient


OMIT = typing.cast(typing.Any, ...)


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

    def update_session(
        self,
        session_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Parameters
        ----------
        session_id : str

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Updated.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sessions.update_session(
            session_id="sessionId",
        )
        """
        _response = self._raw_client.update_session(session_id, title=title, request_options=request_options)
        return _response.data

    def resume_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Session:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Resumed.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sessions.resume_session(
            session_id="sessionId",
        )
        """
        _response = self._raw_client.resume_session(session_id, request_options=request_options)
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

    async def update_session(
        self,
        session_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Parameters
        ----------
        session_id : str

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Updated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sessions.update_session(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_session(session_id, title=title, request_options=request_options)
        return _response.data

    async def resume_session(
        self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Session:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Resumed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sessions.resume_session(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume_session(session_id, request_options=request_options)
        return _response.data
