

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delivery_partners_response import DeliveryPartnersResponse
from ..types.delivery_partners_sorting_options import DeliveryPartnersSortingOptions
from ..types.list_delivery_partners_filter import ListDeliveryPartnersFilter
from ..types.pagination_filter import PaginationFilter
from .raw_client import AsyncRawDeliveryPartnersClient, RawDeliveryPartnersClient


class DeliveryPartnersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeliveryPartnersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeliveryPartnersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeliveryPartnersClient
        """
        return self._raw_client

    def retrieve_multiple_delivery_partners(
        self,
        *,
        filter: typing.Optional[ListDeliveryPartnersFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[DeliveryPartnersSortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeliveryPartnersResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListDeliveryPartnersFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[DeliveryPartnersSortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeliveryPartnersResponse
            A list of Delivery Partners

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delivery_partners.retrieve_multiple_delivery_partners()
        """
        _response = self._raw_client.retrieve_multiple_delivery_partners(
            filter=filter, page=page, sort=sort, request_options=request_options
        )
        return _response.data


class AsyncDeliveryPartnersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeliveryPartnersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeliveryPartnersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeliveryPartnersClient
        """
        return self._raw_client

    async def retrieve_multiple_delivery_partners(
        self,
        *,
        filter: typing.Optional[ListDeliveryPartnersFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[DeliveryPartnersSortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeliveryPartnersResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListDeliveryPartnersFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[DeliveryPartnersSortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeliveryPartnersResponse
            A list of Delivery Partners

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delivery_partners.retrieve_multiple_delivery_partners()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_multiple_delivery_partners(
            filter=filter, page=page, sort=sort, request_options=request_options
        )
        return _response.data
