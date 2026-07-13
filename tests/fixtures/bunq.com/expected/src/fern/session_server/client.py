

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.session_server_create import SessionServerCreate
from .raw_client import AsyncRawSessionServerClient, RawSessionServerClient


OMIT = typing.cast(typing.Any, ...)


class SessionServerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSessionServerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSessionServerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSessionServerClient
        """
        return self._raw_client

    def create_session_server(
        self, *, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionServerCreate:
        """
        Create a new session for a DeviceServer. Provide the Installation token in the "X-Bunq-Client-Authentication" header. And don't forget to create the "X-Bunq-Client-Signature" header. The response contains a Session token that should be used for as the "X-Bunq-Client-Authentication" header for all future API calls. The ip address making this call needs to match the ip address bound to your API key.

        Parameters
        ----------
        secret : str
            The API key of the user you want to login. If your API key has not been used before, it will be bound to the ip address of this DeviceServer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionServerCreate
            Once you have created an Installation and a DeviceServer with that Installation, then you are ready to start a session! A session expires after the same amount of time you have set for Auto Logout in your user account. By default this is 1 week. If a request is made 30 seconds before a session expires, it will be extended from that moment by your auto logout time, but never by more than 5 minutes.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.session_server.create_session_server(
            secret="secret",
        )
        """
        _response = self._raw_client.create_session_server(secret=secret, request_options=request_options)
        return _response.data


class AsyncSessionServerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSessionServerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSessionServerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSessionServerClient
        """
        return self._raw_client

    async def create_session_server(
        self, *, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionServerCreate:
        """
        Create a new session for a DeviceServer. Provide the Installation token in the "X-Bunq-Client-Authentication" header. And don't forget to create the "X-Bunq-Client-Signature" header. The response contains a Session token that should be used for as the "X-Bunq-Client-Authentication" header for all future API calls. The ip address making this call needs to match the ip address bound to your API key.

        Parameters
        ----------
        secret : str
            The API key of the user you want to login. If your API key has not been used before, it will be bound to the ip address of this DeviceServer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionServerCreate
            Once you have created an Installation and a DeviceServer with that Installation, then you are ready to start a session! A session expires after the same amount of time you have set for Auto Logout in your user account. By default this is 1 week. If a request is made 30 seconds before a session expires, it will be extended from that moment by your auto logout time, but never by more than 5 minutes.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.session_server.create_session_server(
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_session_server(secret=secret, request_options=request_options)
        return _response.data
