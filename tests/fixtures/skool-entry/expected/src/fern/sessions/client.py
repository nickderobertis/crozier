

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

    def create_session(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Session:
        """
        Create an authenticated session for API access. Sessions are required for all other endpoints.

        Parameters
        ----------
        email : str
            Skool account email

        password : str
            Skool account password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Session created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.sessions.create_session(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.create_session(email=email, password=password, request_options=request_options)
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

    async def create_session(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Session:
        """
        Create an authenticated session for API access. Sessions are required for all other endpoints.

        Parameters
        ----------
        email : str
            Skool account email

        password : str
            Skool account password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Session created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sessions.create_session(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_session(
            email=email, password=password, request_options=request_options
        )
        return _response.data
