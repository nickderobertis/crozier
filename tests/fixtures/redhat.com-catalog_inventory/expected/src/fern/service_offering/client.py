

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service_instances_collection import ServiceInstancesCollection
from ..types.service_offering import ServiceOffering
from ..types.service_offering_nodes_collection import ServiceOfferingNodesCollection
from ..types.service_offerings_collection import ServiceOfferingsCollection
from ..types.service_plans_collection import ServicePlansCollection
from ..types.tag import Tag
from .raw_client import AsyncRawServiceOfferingClient, RawServiceOfferingClient
from .types.order_service_offering_response import OrderServiceOfferingResponse


OMIT = typing.cast(typing.Any, ...)


class ServiceOfferingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServiceOfferingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServiceOfferingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServiceOfferingClient
        """
        return self._raw_client

    def list_service_offerings(
        self,
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
        client.service_offering.list_service_offerings()
        """
        _response = self._raw_client.list_service_offerings(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def show_service_offering(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceOffering:
        """
        Returns a ServiceOffering object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceOffering
            ServiceOffering info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_offering.show_service_offering(
            id="id",
        )
        """
        _response = self._raw_client.show_service_offering(id, request_options=request_options)
        return _response.data

    def applied_inventories_tags_for_service_offering(
        self,
        id: str,
        *,
        service_parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Tag]:
        """
        Returns an array of inventories tags

        Parameters
        ----------
        id : str
            ID of the resource

        service_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            The provider specific parameters needed to compute list of used service inventories

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tag]
            Returns an array of inventories tags for the computing result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_offering.applied_inventories_tags_for_service_offering(
            id="id",
        )
        """
        _response = self._raw_client.applied_inventories_tags_for_service_offering(
            id, service_parameters=service_parameters, request_options=request_options
        )
        return _response.data

    def order_service_offering(
        self,
        id: str,
        *,
        provider_control_parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        service_parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrderServiceOfferingResponse:
        """
        Returns a Task id

        Parameters
        ----------
        id : str
            ID of the resource

        provider_control_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            The provider specific parameters needed to provision this service. This might include namespaces, special keys

        service_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            JSON object with provisioning parameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrderServiceOfferingResponse
            Returns a task ID for the order

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_offering.order_service_offering(
            id="id",
        )
        """
        _response = self._raw_client.order_service_offering(
            id,
            provider_control_parameters=provider_control_parameters,
            service_parameters=service_parameters,
            request_options=request_options,
        )
        return _response.data

    def list_service_offering_service_instances(
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
        client.service_offering.list_service_offering_service_instances(
            id="id",
        )
        """
        _response = self._raw_client.list_service_offering_service_instances(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def list_service_offering_service_offering_nodes(
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
        client.service_offering.list_service_offering_service_offering_nodes(
            id="id",
        )
        """
        _response = self._raw_client.list_service_offering_service_offering_nodes(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def list_service_offering_service_plans(
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
        client.service_offering.list_service_offering_service_plans(
            id="id",
        )
        """
        _response = self._raw_client.list_service_offering_service_plans(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data


class AsyncServiceOfferingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServiceOfferingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServiceOfferingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServiceOfferingClient
        """
        return self._raw_client

    async def list_service_offerings(
        self,
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
            await client.service_offering.list_service_offerings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_offerings(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def show_service_offering(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceOffering:
        """
        Returns a ServiceOffering object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceOffering
            ServiceOffering info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_offering.show_service_offering(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_service_offering(id, request_options=request_options)
        return _response.data

    async def applied_inventories_tags_for_service_offering(
        self,
        id: str,
        *,
        service_parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Tag]:
        """
        Returns an array of inventories tags

        Parameters
        ----------
        id : str
            ID of the resource

        service_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            The provider specific parameters needed to compute list of used service inventories

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tag]
            Returns an array of inventories tags for the computing result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_offering.applied_inventories_tags_for_service_offering(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.applied_inventories_tags_for_service_offering(
            id, service_parameters=service_parameters, request_options=request_options
        )
        return _response.data

    async def order_service_offering(
        self,
        id: str,
        *,
        provider_control_parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        service_parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrderServiceOfferingResponse:
        """
        Returns a Task id

        Parameters
        ----------
        id : str
            ID of the resource

        provider_control_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            The provider specific parameters needed to provision this service. This might include namespaces, special keys

        service_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            JSON object with provisioning parameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrderServiceOfferingResponse
            Returns a task ID for the order

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_offering.order_service_offering(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.order_service_offering(
            id,
            provider_control_parameters=provider_control_parameters,
            service_parameters=service_parameters,
            request_options=request_options,
        )
        return _response.data

    async def list_service_offering_service_instances(
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
            await client.service_offering.list_service_offering_service_instances(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_offering_service_instances(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def list_service_offering_service_offering_nodes(
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
            await client.service_offering.list_service_offering_service_offering_nodes(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_offering_service_offering_nodes(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def list_service_offering_service_plans(
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
            await client.service_offering.list_service_offering_service_plans(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_offering_service_plans(
            id, limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data
