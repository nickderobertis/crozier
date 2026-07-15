

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.response_item import ResponseItem
from .raw_client import AsyncRawBalanceClient, RawBalanceClient


class BalanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBalanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBalanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBalanceClient
        """
        return self._raw_client

    def lookup(
        self, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ResponseItem]:
        """
        Get Account balance and expiry

        Parameters
        ----------
        api_key : str
            The API key, which you can get from bintable.com website.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ResponseItem]
            Balance reponse

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.balance.lookup(
            api_key="api_key",
        )
        """
        _response = self._raw_client.lookup(api_key=api_key, request_options=request_options)
        return _response.data


class AsyncBalanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBalanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBalanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBalanceClient
        """
        return self._raw_client

    async def lookup(
        self, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ResponseItem]:
        """
        Get Account balance and expiry

        Parameters
        ----------
        api_key : str
            The API key, which you can get from bintable.com website.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ResponseItem]
            Balance reponse

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.balance.lookup(
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lookup(api_key=api_key, request_options=request_options)
        return _response.data
