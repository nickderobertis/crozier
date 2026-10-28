

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_transaction_method import BulkTransactionMethod
from ..types.bulk_transaction_model import BulkTransactionModel
from .raw_client import AsyncRawCatalogBulkTransactionExtensionClient, RawCatalogBulkTransactionExtensionClient


OMIT = typing.cast(typing.Any, ...)


class CatalogBulkTransactionExtensionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogBulkTransactionExtensionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogBulkTransactionExtensionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogBulkTransactionExtensionClient
        """
        return self._raw_client

    def bulk_create_item(
        self,
        collection_id: str,
        *,
        items: typing.Dict[str, typing.Any],
        method: typing.Optional[BulkTransactionMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkTransactionModel:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str

        items : typing.Dict[str, typing.Any]

        method : typing.Optional[BulkTransactionMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkTransactionModel
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_bulk_transaction_extension.bulk_create_item(
            collection_id="collection_id",
            items={"key": "value"},
        )
        """
        _response = self._raw_client.bulk_create_item(
            collection_id, items=items, method=method, request_options=request_options
        )
        return _response.data


class AsyncCatalogBulkTransactionExtensionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogBulkTransactionExtensionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogBulkTransactionExtensionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogBulkTransactionExtensionClient
        """
        return self._raw_client

    async def bulk_create_item(
        self,
        collection_id: str,
        *,
        items: typing.Dict[str, typing.Any],
        method: typing.Optional[BulkTransactionMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkTransactionModel:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str

        items : typing.Dict[str, typing.Any]

        method : typing.Optional[BulkTransactionMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkTransactionModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.catalog_bulk_transaction_extension.bulk_create_item(
                collection_id="collection_id",
                items={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_create_item(
            collection_id, items=items, method=method, request_options=request_options
        )
        return _response.data
