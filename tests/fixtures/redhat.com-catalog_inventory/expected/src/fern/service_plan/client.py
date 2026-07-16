

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service_plan import ServicePlan
from ..types.service_plans_collection import ServicePlansCollection
from .raw_client import AsyncRawServicePlanClient, RawServicePlanClient


class ServicePlanClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServicePlanClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServicePlanClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServicePlanClient
        """
        return self._raw_client

    def list_service_plans(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServicePlansCollection:
        """
        Returns an array of ServicePlan objects

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
        ServicePlansCollection
            ServicePlans collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_plan.list_service_plans()
        """
        _response = self._raw_client.list_service_plans(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def show_service_plan(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ServicePlan:
        """
        Returns a ServicePlan object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServicePlan
            ServicePlan info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service_plan.show_service_plan(
            id="id",
        )
        """
        _response = self._raw_client.show_service_plan(id, request_options=request_options)
        return _response.data


class AsyncServicePlanClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServicePlanClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServicePlanClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServicePlanClient
        """
        return self._raw_client

    async def list_service_plans(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServicePlansCollection:
        """
        Returns an array of ServicePlan objects

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
            await client.service_plan.list_service_plans()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_plans(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def show_service_plan(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServicePlan:
        """
        Returns a ServicePlan object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServicePlan
            ServicePlan info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service_plan.show_service_plan(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_service_plan(id, request_options=request_options)
        return _response.data
