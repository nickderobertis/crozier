

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.server_error import ServerError
from ..types.server_error_create import ServerErrorCreate
from .raw_client import AsyncRawServerErrorClient, RawServerErrorClient


OMIT = typing.cast(typing.Any, ...)


class ServerErrorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServerErrorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServerErrorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServerErrorClient
        """
        return self._raw_client

    def create_server_error(
        self, *, request: ServerError, request_options: typing.Optional[RequestOptions] = None
    ) -> ServerErrorCreate:
        """
        An endpoint that will always throw an error.

        Parameters
        ----------
        request : ServerError

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServerErrorCreate
            An endpoint that will always throw an error.

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
        client.server_error.create_server_error(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_server_error(request=request, request_options=request_options)
        return _response.data


class AsyncServerErrorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServerErrorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServerErrorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServerErrorClient
        """
        return self._raw_client

    async def create_server_error(
        self, *, request: ServerError, request_options: typing.Optional[RequestOptions] = None
    ) -> ServerErrorCreate:
        """
        An endpoint that will always throw an error.

        Parameters
        ----------
        request : ServerError

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServerErrorCreate
            An endpoint that will always throw an error.

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
            await client.server_error.create_server_error(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_server_error(request=request, request_options=request_options)
        return _response.data
