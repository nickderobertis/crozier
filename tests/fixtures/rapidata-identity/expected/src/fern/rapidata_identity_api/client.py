

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRapidataIdentityApiClient, RawRapidataIdentityApiClient


class RapidataIdentityApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRapidataIdentityApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRapidataIdentityApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRapidataIdentityApiClient
        """
        return self._raw_client

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rapidata_identity_api.get()
        """
        _response = self._raw_client.get(request_options=request_options)
        return _response.data


class AsyncRapidataIdentityApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRapidataIdentityApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRapidataIdentityApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRapidataIdentityApiClient
        """
        return self._raw_client

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rapidata_identity_api.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(request_options=request_options)
        return _response.data
