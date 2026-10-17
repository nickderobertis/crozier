

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.entry_batch import EntryBatch
from ..types.entry_ids import EntryIds
from .raw_client import AsyncRawEntriesClient, RawEntriesClient


OMIT = typing.cast(typing.Any, ...)


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

    def create_entries(self, *, request: EntryBatch, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : EntryBatch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Entry, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.entries.create_entries(
            request=[
                Entry(
                    amount=1,
                )
            ],
        )
        """
        _response = self._raw_client.create_entries(request=request, request_options=request_options)
        return _response.data

    def void_entries(self, *, request: EntryIds, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : EntryIds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.entries.void_entries(
            request=["string"],
        )
        """
        _response = self._raw_client.void_entries(request=request, request_options=request_options)
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

    async def create_entries(
        self, *, request: EntryBatch, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : EntryBatch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Entry

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.entries.create_entries(
                request=[
                    Entry(
                        amount=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_entries(request=request, request_options=request_options)
        return _response.data

    async def void_entries(self, *, request: EntryIds, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : EntryIds

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.entries.void_entries(
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.void_entries(request=request, request_options=request_options)
        return _response.data
