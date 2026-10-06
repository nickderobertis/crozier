

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawHealthClient, RawHealthClient


class HealthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthClient
        """
        return self._raw_client

    def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The service is up.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ledger_mode="YOUR_LEDGER_MODE",
            retry_budget="YOUR_RETRY_BUDGET",
            book="YOUR_BOOK",
            base_url="https://yourhost.com/path/to/api",
        )
        client.health.get_health()
        """
        _response = self._raw_client.get_health(request_options=request_options)
        return _response.data


class AsyncHealthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthClient
        """
        return self._raw_client

    async def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The service is up.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ledger_mode="YOUR_LEDGER_MODE",
            retry_budget="YOUR_RETRY_BUDGET",
            book="YOUR_BOOK",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health.get_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_health(request_options=request_options)
        return _response.data
