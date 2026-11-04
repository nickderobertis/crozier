

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_ocs_get_capabilities200response import CoreOcsGetCapabilities200Response
from .raw_client import AsyncRawCoreOcsClient, RawCoreOcsClient


class CoreOcsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreOcsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreOcsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreOcsClient
        """
        return self._raw_client

    def get_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreOcsGetCapabilities200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreOcsGetCapabilities200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_ocs.get_capabilities()
        """
        _response = self._raw_client.get_capabilities(request_options=request_options)
        return _response.data


class AsyncCoreOcsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreOcsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreOcsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreOcsClient
        """
        return self._raw_client

    async def get_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreOcsGetCapabilities200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreOcsGetCapabilities200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_ocs.get_capabilities()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_capabilities(request_options=request_options)
        return _response.data
