

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_get_industries import EndpointGetIndustries
from .raw_client import AsyncRawIndustriesClient, RawIndustriesClient


class IndustriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIndustriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIndustriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIndustriesClient
        """
        return self._raw_client

    def get_industries(self, *, request_options: typing.Optional[RequestOptions] = None) -> EndpointGetIndustries:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetIndustries
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.industries.get_industries()
        """
        _response = self._raw_client.get_industries(request_options=request_options)
        return _response.data


class AsyncIndustriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIndustriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIndustriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIndustriesClient
        """
        return self._raw_client

    async def get_industries(self, *, request_options: typing.Optional[RequestOptions] = None) -> EndpointGetIndustries:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetIndustries
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.industries.get_industries()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_industries(request_options=request_options)
        return _response.data
