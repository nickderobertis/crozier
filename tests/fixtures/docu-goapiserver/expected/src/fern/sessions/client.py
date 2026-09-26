

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

    def post_sessions_v3(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Session:
        """
        Authenticate with username and password. A single JSON object is required and unknown properties are rejected. Returns access_token and refresh_token with HTTP 201; V3 has no refresh or logout operation.

        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sessions.post_sessions_v3(
            username="example.user",
            password="<your-password>",
        )
        """
        _response = self._raw_client.post_sessions_v3(
            username=username, password=password, request_options=request_options
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

    async def post_sessions_v3(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Session:
        """
        Authenticate with username and password. A single JSON object is required and unknown properties are rejected. Returns access_token and refresh_token with HTTP 201; V3 has no refresh or logout operation.

        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sessions.post_sessions_v3(
                username="example.user",
                password="<your-password>",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_sessions_v3(
            username=username, password=password, request_options=request_options
        )
        return _response.data
