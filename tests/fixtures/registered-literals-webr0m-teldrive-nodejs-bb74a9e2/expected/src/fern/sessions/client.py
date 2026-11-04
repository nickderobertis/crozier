

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cursor import Cursor
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawSessionsClient, RawSessionsClient
from .types.list_sessions_response import ListSessionsResponse


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

    def list_sessions(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSessionsResponse:
        """
        List all TelDrive sessions for the authenticated Telegram account.

        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSessionsResponse
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.sessions.list_sessions()
        """
        _response = self._raw_client.list_sessions(cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    def revoke_session(self, session_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revoke one TelDrive session. Revoking the current session invalidates its bearer token immediately.

        Parameters
        ----------
        session_id : Uuid

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
            token="YOUR_TOKEN",
        )
        client.sessions.revoke_session(
            session_id="sessionId",
        )
        """
        _response = self._raw_client.revoke_session(session_id, request_options=request_options)
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

    async def list_sessions(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSessionsResponse:
        """
        List all TelDrive sessions for the authenticated Telegram account.

        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSessionsResponse
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sessions.list_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sessions(cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    async def revoke_session(
        self, session_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Revoke one TelDrive session. Revoking the current session invalidates its bearer token immediately.

        Parameters
        ----------
        session_id : Uuid

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sessions.revoke_session(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_session(session_id, request_options=request_options)
        return _response.data
