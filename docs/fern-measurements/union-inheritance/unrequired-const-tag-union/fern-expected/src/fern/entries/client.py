

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEntriesClient, RawEntriesClient
from .types.add_entry_request import AddEntryRequest


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

    def add_entry(self, *, request: AddEntryRequest, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : AddEntryRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, StudioNote

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.entries.add_entry(
            request=StudioNote(
                text="text",
            ),
        )
        """
        _response = self._raw_client.add_entry(request=request, request_options=request_options)
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

    async def add_entry(
        self, *, request: AddEntryRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : AddEntryRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, StudioNote

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.entries.add_entry(
                request=StudioNote(
                    text="text",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_entry(request=request, request_options=request_options)
        return _response.data
