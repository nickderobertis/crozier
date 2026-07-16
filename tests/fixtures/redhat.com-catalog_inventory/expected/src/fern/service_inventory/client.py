

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service_inventories_collection import ServiceInventoriesCollection
from ..types.service_inventory import ServiceInventory
from ..types.tag import Tag
from ..types.tags_collection import TagsCollection
from .raw_client import AsyncRawServiceInventoryClient, RawServiceInventoryClient


OMIT = typing.cast(typing.Any, ...)


class ServiceInventoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServiceInventoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServiceInventoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServiceInventoryClient
        """
        return self._raw_client

    def list_service_inventories(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceInventoriesCollection:
        """
        Returns an array of ServiceInventory objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceInventoriesCollection
            ServiceInventories collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_inventory.list_service_inventories()
        """
        _response = self._raw_client.list_service_inventories(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def show_service_inventory(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceInventory:
        """
        Returns a ServiceInventory object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceInventory
            ServiceInventory info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_inventory.show_service_inventory(
            id="id",
        )
        """
        _response = self._raw_client.show_service_inventory(id, request_options=request_options)
        return _response.data

    def tag_service_inventory(
        self, id: str, *, request: typing.Sequence[Tag], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Tag]:
        """
        Tags a ServiceInventory object

        Parameters
        ----------
        id : str
            ID of the resource

        request : typing.Sequence[Tag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tag]
            ServiceInventory tagged successful

        Examples
        --------
        from fern import FernApi, Tag

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_inventory.tag_service_inventory(
            id="id",
            request=[Tag()],
        )
        """
        _response = self._raw_client.tag_service_inventory(id, request=request, request_options=request_options)
        return _response.data

    def list_service_inventory_tags(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TagsCollection:
        """
        Returns an array of Tag objects

        Parameters
        ----------
        id : str
            ID of the resource

        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagsCollection
            Tags collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_inventory.list_service_inventory_tags(
            id="id",
        )
        """
        _response = self._raw_client.list_service_inventory_tags(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def untag_service_inventory(
        self, id: str, *, request: typing.Sequence[Tag], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Untags a ServiceInventory object

        Parameters
        ----------
        id : str
            ID of the resource

        request : typing.Sequence[Tag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, Tag

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_inventory.untag_service_inventory(
            id="id",
            request=[Tag()],
        )
        """
        _response = self._raw_client.untag_service_inventory(id, request=request, request_options=request_options)
        return _response.data


class AsyncServiceInventoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServiceInventoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServiceInventoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServiceInventoryClient
        """
        return self._raw_client

    async def list_service_inventories(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceInventoriesCollection:
        """
        Returns an array of ServiceInventory objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceInventoriesCollection
            ServiceInventories collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_inventory.list_service_inventories()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_inventories(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def show_service_inventory(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceInventory:
        """
        Returns a ServiceInventory object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceInventory
            ServiceInventory info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_inventory.show_service_inventory(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_service_inventory(id, request_options=request_options)
        return _response.data

    async def tag_service_inventory(
        self, id: str, *, request: typing.Sequence[Tag], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Tag]:
        """
        Tags a ServiceInventory object

        Parameters
        ----------
        id : str
            ID of the resource

        request : typing.Sequence[Tag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tag]
            ServiceInventory tagged successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Tag

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_inventory.tag_service_inventory(
                id="id",
                request=[Tag()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tag_service_inventory(id, request=request, request_options=request_options)
        return _response.data

    async def list_service_inventory_tags(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TagsCollection:
        """
        Returns an array of Tag objects

        Parameters
        ----------
        id : str
            ID of the resource

        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagsCollection
            Tags collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_inventory.list_service_inventory_tags(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_inventory_tags(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def untag_service_inventory(
        self, id: str, *, request: typing.Sequence[Tag], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Untags a ServiceInventory object

        Parameters
        ----------
        id : str
            ID of the resource

        request : typing.Sequence[Tag]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Tag

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_inventory.untag_service_inventory(
                id="id",
                request=[Tag()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.untag_service_inventory(id, request=request, request_options=request_options)
        return _response.data
