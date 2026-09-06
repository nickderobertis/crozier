

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawInventoryClient, RawInventoryClient
from .types.list_inventory_response import ListInventoryResponse
from .types.update_inventory_request_inventory_type import UpdateInventoryRequestInventoryType
from .types.update_inventory_response import UpdateInventoryResponse


OMIT = typing.cast(typing.Any, ...)


class InventoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInventoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInventoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInventoryClient
        """
        return self._raw_client

    def list(
        self, sku_collection_id: str, sku_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInventoryResponse:
        """
        List the current inventory levels for a particular SKU item.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        sku_collection_id : str
            Unique identifier for a SKU collection. Use the List Collections API to find this ID.

        sku_id : str
            Unique identifier for a SKU

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInventoryResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.inventory.list(
            sku_collection_id="6377a7c4b7a79608c34a46f7",
            sku_id="5e8518516e147040726cc415",
        )
        """
        _response = self._raw_client.list(sku_collection_id, sku_id, request_options=request_options)
        return _response.data

    def update(
        self,
        sku_collection_id: str,
        sku_id: str,
        *,
        inventory_type: UpdateInventoryRequestInventoryType,
        update_quantity: typing.Optional[float] = OMIT,
        quantity: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateInventoryResponse:
        """
        Updates the current inventory levels for a particular SKU item.

        Updates may be given in one or two methods, absolutely or incrementally.
        - Absolute updates are done by setting `quantity` directly.
        - Incremental updates are by specifying the inventory delta in `updateQuantity` which is then added to the `quantity` stored on the server.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        sku_collection_id : str
            Unique identifier for a SKU collection. Use the List Collections API to find this ID.

        sku_id : str
            Unique identifier for a SKU

        inventory_type : UpdateInventoryRequestInventoryType
            infinite or finite

        update_quantity : typing.Optional[float]
            Adds this quantity to currently store quantity. Can be negative.

        quantity : typing.Optional[float]
            Immediately sets quantity to this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateInventoryResponse
            Request was successful

        Examples
        --------
        from fern.inventory import UpdateInventoryRequestInventoryType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.inventory.update(
            sku_collection_id="6377a7c4b7a79608c34a46f7",
            sku_id="5e8518516e147040726cc415",
            inventory_type=UpdateInventoryRequestInventoryType.INFINITE,
        )
        """
        _response = self._raw_client.update(
            sku_collection_id,
            sku_id,
            inventory_type=inventory_type,
            update_quantity=update_quantity,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data


class AsyncInventoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInventoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInventoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInventoryClient
        """
        return self._raw_client

    async def list(
        self, sku_collection_id: str, sku_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListInventoryResponse:
        """
        List the current inventory levels for a particular SKU item.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        sku_collection_id : str
            Unique identifier for a SKU collection. Use the List Collections API to find this ID.

        sku_id : str
            Unique identifier for a SKU

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInventoryResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.inventory.list(
                sku_collection_id="6377a7c4b7a79608c34a46f7",
                sku_id="5e8518516e147040726cc415",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(sku_collection_id, sku_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        sku_collection_id: str,
        sku_id: str,
        *,
        inventory_type: UpdateInventoryRequestInventoryType,
        update_quantity: typing.Optional[float] = OMIT,
        quantity: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateInventoryResponse:
        """
        Updates the current inventory levels for a particular SKU item.

        Updates may be given in one or two methods, absolutely or incrementally.
        - Absolute updates are done by setting `quantity` directly.
        - Incremental updates are by specifying the inventory delta in `updateQuantity` which is then added to the `quantity` stored on the server.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        sku_collection_id : str
            Unique identifier for a SKU collection. Use the List Collections API to find this ID.

        sku_id : str
            Unique identifier for a SKU

        inventory_type : UpdateInventoryRequestInventoryType
            infinite or finite

        update_quantity : typing.Optional[float]
            Adds this quantity to currently store quantity. Can be negative.

        quantity : typing.Optional[float]
            Immediately sets quantity to this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateInventoryResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.inventory import UpdateInventoryRequestInventoryType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.inventory.update(
                sku_collection_id="6377a7c4b7a79608c34a46f7",
                sku_id="5e8518516e147040726cc415",
                inventory_type=UpdateInventoryRequestInventoryType.INFINITE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            sku_collection_id,
            sku_id,
            inventory_type=inventory_type,
            update_quantity=update_quantity,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data
