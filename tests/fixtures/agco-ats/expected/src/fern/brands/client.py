

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBrandsClient, RawBrandsClient


class BrandsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBrandsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBrandsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBrandsClient
        """
        return self._raw_client

    def brands(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.brands.brands()
        """
        _response = self._raw_client.brands(request_options=request_options)
        return _response.data


class AsyncBrandsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBrandsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBrandsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBrandsClient
        """
        return self._raw_client

    async def brands(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.brands.brands()


        asyncio.run(main())
        """
        _response = await self._raw_client.brands(request_options=request_options)
        return _response.data
