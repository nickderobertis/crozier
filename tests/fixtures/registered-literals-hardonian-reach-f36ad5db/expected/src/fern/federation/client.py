

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.federation_status import FederationStatus
from .raw_client import AsyncRawFederationClient, RawFederationClient


class FederationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFederationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFederationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFederationClient
        """
        return self._raw_client

    def get_federation_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> FederationStatus:
        """
        Retrieve status of all federation nodes

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FederationStatus
            Federation status

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.federation.get_federation_status()
        """
        _response = self._raw_client.get_federation_status(request_options=request_options)
        return _response.data


class AsyncFederationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFederationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFederationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFederationClient
        """
        return self._raw_client

    async def get_federation_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FederationStatus:
        """
        Retrieve status of all federation nodes

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FederationStatus
            Federation status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.federation.get_federation_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_federation_status(request_options=request_options)
        return _response.data
