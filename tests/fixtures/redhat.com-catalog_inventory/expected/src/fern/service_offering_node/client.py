

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service_offering_node import ServiceOfferingNode
from ..types.service_offering_nodes_collection import ServiceOfferingNodesCollection
from .raw_client import AsyncRawServiceOfferingNodeClient, RawServiceOfferingNodeClient


class ServiceOfferingNodeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServiceOfferingNodeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServiceOfferingNodeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServiceOfferingNodeClient
        """
        return self._raw_client

    def list_service_offering_nodes(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceOfferingNodesCollection:
        """
        Returns an array of ServiceOfferingNode objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Any]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceOfferingNodesCollection
            ServiceOfferingNodes collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_offering_node.list_service_offering_nodes()
        """
        _response = self._raw_client.list_service_offering_nodes(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def show_service_offering_node(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceOfferingNode:
        """
        Returns a ServiceOfferingNode object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceOfferingNode
            ServiceOfferingNode info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_offering_node.show_service_offering_node(
            id="id",
        )
        """
        _response = self._raw_client.show_service_offering_node(id, request_options=request_options)
        return _response.data


class AsyncServiceOfferingNodeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServiceOfferingNodeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServiceOfferingNodeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServiceOfferingNodeClient
        """
        return self._raw_client

    async def list_service_offering_nodes(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceOfferingNodesCollection:
        """
        Returns an array of ServiceOfferingNode objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Any]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceOfferingNodesCollection
            ServiceOfferingNodes collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_offering_node.list_service_offering_nodes()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_offering_nodes(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def show_service_offering_node(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceOfferingNode:
        """
        Returns a ServiceOfferingNode object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceOfferingNode
            ServiceOfferingNode info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_offering_node.show_service_offering_node(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_service_offering_node(id, request_options=request_options)
        return _response.data
