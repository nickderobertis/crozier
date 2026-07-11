

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.item import Item
from .raw_client import AsyncRawItemsClient, RawItemsClient
from .types.items_create_batch_request_item import ItemsCreateBatchRequestItem


OMIT = typing.cast(typing.Any, ...)


class ItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawItemsClient
        """
        return self._raw_client

    def createbatch(
        self,
        *,
        request: typing.Sequence[ItemsCreateBatchRequestItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Item]:
        """
        Parameters
        ----------
        request : typing.Sequence[ItemsCreateBatchRequestItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Item]


        Examples
        --------
        from fern.items import ItemsCreateBatchRequestItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.items.createbatch(
            request=[
                ItemsCreateBatchRequestItem(
                    name="name",
                )
            ],
        )
        """
        _response = self._raw_client.createbatch(request=request, request_options=request_options)
        return _response.data


class AsyncItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawItemsClient
        """
        return self._raw_client

    async def createbatch(
        self,
        *,
        request: typing.Sequence[ItemsCreateBatchRequestItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Item]:
        """
        Parameters
        ----------
        request : typing.Sequence[ItemsCreateBatchRequestItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Item]


        Examples
        --------
        import asyncio

        from fern.items import ItemsCreateBatchRequestItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.items.createbatch(
                request=[
                    ItemsCreateBatchRequestItem(
                        name="name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createbatch(request=request, request_options=request_options)
        return _response.data
