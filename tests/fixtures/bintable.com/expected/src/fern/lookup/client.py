

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.response_item import ResponseItem
from .raw_client import AsyncRawLookupClient, RawLookupClient


class LookupClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLookupClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLookupClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLookupClient
        """
        return self._raw_client

    def bin_lookup(
        self, bin: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ResponseItem]:
        """
        By passing in the appropriate BIN, you can lookup for
        card meta data in bintable.com API

        Parameters
        ----------
        bin : str
            pass the required BIN code

        api_key : str
            The API key, which you can get from bintable.com website.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ResponseItem]
            BIN data response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.lookup.bin_lookup(
            bin="bin",
            api_key="api_key",
        )
        """
        _response = self._raw_client.bin_lookup(bin, api_key=api_key, request_options=request_options)
        return _response.data


class AsyncLookupClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLookupClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLookupClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLookupClient
        """
        return self._raw_client

    async def bin_lookup(
        self, bin: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ResponseItem]:
        """
        By passing in the appropriate BIN, you can lookup for
        card meta data in bintable.com API

        Parameters
        ----------
        bin : str
            pass the required BIN code

        api_key : str
            The API key, which you can get from bintable.com website.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ResponseItem]
            BIN data response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.lookup.bin_lookup(
                bin="bin",
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bin_lookup(bin, api_key=api_key, request_options=request_options)
        return _response.data
