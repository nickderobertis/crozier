

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEntriesClient, RawEntriesClient


class EntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntriesClient
        """
        return self._raw_client

    def post_entry(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            ledger_mode="YOUR_LEDGER_MODE",
            retry_budget="YOUR_RETRY_BUDGET",
            book="YOUR_BOOK",
            base_url="https://yourhost.com/path/to/api",
        )
        client.entries.post_entry()
        """
        _response = self._raw_client.post_entry(request_options=request_options)
        return _response.data

    def void_entry(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            ledger_mode="YOUR_LEDGER_MODE",
            retry_budget="YOUR_RETRY_BUDGET",
            book="YOUR_BOOK",
            base_url="https://yourhost.com/path/to/api",
        )
        client.entries.void_entry()
        """
        _response = self._raw_client.void_entry(request_options=request_options)
        return _response.data

    def reconcile_entries(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            ledger_mode="YOUR_LEDGER_MODE",
            retry_budget="YOUR_RETRY_BUDGET",
            book="YOUR_BOOK",
            base_url="https://yourhost.com/path/to/api",
        )
        client.entries.reconcile_entries()
        """
        _response = self._raw_client.reconcile_entries(request_options=request_options)
        return _response.data


class AsyncEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntriesClient
        """
        return self._raw_client

    async def post_entry(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            ledger_mode="YOUR_LEDGER_MODE",
            retry_budget="YOUR_RETRY_BUDGET",
            book="YOUR_BOOK",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.entries.post_entry()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_entry(request_options=request_options)
        return _response.data

    async def void_entry(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            ledger_mode="YOUR_LEDGER_MODE",
            retry_budget="YOUR_RETRY_BUDGET",
            book="YOUR_BOOK",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.entries.void_entry()


        asyncio.run(main())
        """
        _response = await self._raw_client.void_entry(request_options=request_options)
        return _response.data

    async def reconcile_entries(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            ledger_mode="YOUR_LEDGER_MODE",
            retry_budget="YOUR_RETRY_BUDGET",
            book="YOUR_BOOK",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.entries.reconcile_entries()


        asyncio.run(main())
        """
        _response = await self._raw_client.reconcile_entries(request_options=request_options)
        return _response.data
