

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service_instances_collection import ServiceInstancesCollection
from ..types.service_inventories_collection import ServiceInventoriesCollection
from ..types.service_offering_nodes_collection import ServiceOfferingNodesCollection
from ..types.service_offerings_collection import ServiceOfferingsCollection
from ..types.service_plans_collection import ServicePlansCollection
from ..types.source import Source
from ..types.sources_collection import SourcesCollection
from ..types.tasks_collection import TasksCollection
from .raw_client import AsyncRawSourceClient, RawSourceClient


class SourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourceClient
        """
        return self._raw_client

    def list_sources(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourcesCollection:
        """
        Returns an array of Source objects

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
        SourcesCollection
            Sources collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.source.list_sources()
        """
        _response = self._raw_client.list_sources(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def show_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Source:
        """
        Returns a Source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Source
            Source info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.source.show_source(
            id="id",
        )
        """
        _response = self._raw_client.show_source(id, request_options=request_options)
        return _response.data

    def incremental_refresh_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Incremental Refresh a source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.source.incremental_refresh_source(
            id="id",
        )
        """
        _response = self._raw_client.incremental_refresh_source(id, request_options=request_options)
        return _response.data

    def refresh_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Refresh a source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.source.refresh_source(
            id="id",
        )
        """
        _response = self._raw_client.refresh_source(id, request_options=request_options)
        return _response.data

    def list_source_service_instances(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceInstancesCollection:
        """
        Returns an array of ServiceInstance objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        ServiceInstancesCollection
            ServiceInstances collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.source.list_source_service_instances(
            id="id",
        )
        """
        _response = self._raw_client.list_source_service_instances(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def list_source_service_inventories(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceInventoriesCollection:
        """
        Returns an array of ServiceInventory objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        ServiceInventoriesCollection
            ServiceInventories collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.source.list_source_service_inventories(
            id="id",
        )
        """
        _response = self._raw_client.list_source_service_inventories(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def list_source_service_offering_nodes(
        self,
        id: str,
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
        id : str
            ID of the resource

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
        client.source.list_source_service_offering_nodes(
            id="id",
        )
        """
        _response = self._raw_client.list_source_service_offering_nodes(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def list_source_service_offerings(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceOfferingsCollection:
        """
        Returns an array of ServiceOffering objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        ServiceOfferingsCollection
            ServiceOfferings collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.source.list_source_service_offerings(
            id="id",
        )
        """
        _response = self._raw_client.list_source_service_offerings(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def list_source_service_plans(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServicePlansCollection:
        """
        Returns an array of ServicePlan objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        ServicePlansCollection
            ServicePlans collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.source.list_source_service_plans(
            id="id",
        )
        """
        _response = self._raw_client.list_source_service_plans(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def list_source_tasks(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TasksCollection:
        """
        Returns an array of Task objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        TasksCollection
            Tasks collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.source.list_source_tasks(
            id="id",
        )
        """
        _response = self._raw_client.list_source_tasks(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data


class AsyncSourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourceClient
        """
        return self._raw_client

    async def list_sources(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourcesCollection:
        """
        Returns an array of Source objects

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
        SourcesCollection
            Sources collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.source.list_sources()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sources(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def show_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Source:
        """
        Returns a Source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Source
            Source info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.source.show_source(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_source(id, request_options=request_options)
        return _response.data

    async def incremental_refresh_source(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Incremental Refresh a source object

        Parameters
        ----------
        id : str
            ID of the resource

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.source.incremental_refresh_source(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.incremental_refresh_source(id, request_options=request_options)
        return _response.data

    async def refresh_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Refresh a source object

        Parameters
        ----------
        id : str
            ID of the resource

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.source.refresh_source(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_source(id, request_options=request_options)
        return _response.data

    async def list_source_service_instances(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceInstancesCollection:
        """
        Returns an array of ServiceInstance objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        ServiceInstancesCollection
            ServiceInstances collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.source.list_source_service_instances(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_service_instances(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def list_source_service_inventories(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceInventoriesCollection:
        """
        Returns an array of ServiceInventory objects

        Parameters
        ----------
        id : str
            ID of the resource

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
            await client.source.list_source_service_inventories(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_service_inventories(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def list_source_service_offering_nodes(
        self,
        id: str,
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
        id : str
            ID of the resource

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
            await client.source.list_source_service_offering_nodes(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_service_offering_nodes(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def list_source_service_offerings(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceOfferingsCollection:
        """
        Returns an array of ServiceOffering objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        ServiceOfferingsCollection
            ServiceOfferings collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.source.list_source_service_offerings(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_service_offerings(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def list_source_service_plans(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServicePlansCollection:
        """
        Returns an array of ServicePlan objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        ServicePlansCollection
            ServicePlans collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.source.list_source_service_plans(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_service_plans(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def list_source_tasks(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TasksCollection:
        """
        Returns an array of Task objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        TasksCollection
            Tasks collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.source.list_source_tasks(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_tasks(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data
