

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.shelf import Shelf
from .raw_client import AsyncRawShelvesClient, RawShelvesClient


class ShelvesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShelvesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShelvesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShelvesClient
        """
        return self._raw_client

    def get_shelf(self, shelf_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Shelf:
        """
        Parameters
        ----------
        shelf_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Shelf
            The shelf.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.shelves.get_shelf(
            shelf_id="shelfId",
        )
        """
        _response = self._raw_client.get_shelf(shelf_id, request_options=request_options)
        return _response.data


class AsyncShelvesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShelvesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShelvesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShelvesClient
        """
        return self._raw_client

    async def get_shelf(self, shelf_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Shelf:
        """
        Parameters
        ----------
        shelf_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Shelf
            The shelf.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.shelves.get_shelf(
                shelf_id="shelfId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_shelf(shelf_id, request_options=request_options)
        return _response.data
