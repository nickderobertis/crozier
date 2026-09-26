

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_pricing_tier_by_id_response import GetPricingTierByIdResponse
from ..types.get_pricing_tiers_response import GetPricingTiersResponse
from .raw_client import AsyncRawPricingTiersClient, RawPricingTiersClient
from .types.get_pricing_tiers_request_sort_field import GetPricingTiersRequestSortField
from .types.get_pricing_tiers_request_sort_order import GetPricingTiersRequestSortOrder


class PricingTiersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPricingTiersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPricingTiersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPricingTiersClient
        """
        return self._raw_client

    def get_pricing_tiers(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricingTiersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPricingTiersRequestSortField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPricingTiersResponse:
        """
        Schema for a Pricing Tier

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricingTiersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPricingTiersRequestSortField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricingTiersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pricing_tiers.get_pricing_tiers()
        """
        _response = self._raw_client.get_pricing_tiers(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            request_options=request_options,
        )
        return _response.data

    def get_pricing_tiers_id(
        self, id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPricingTierByIdResponse:
        """
        Schema for a Pricing Tier by ID

        Parameters
        ----------
        id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricingTierByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pricing_tiers.get_pricing_tiers_id(
            id=1.1,
        )
        """
        _response = self._raw_client.get_pricing_tiers_id(id, request_options=request_options)
        return _response.data


class AsyncPricingTiersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPricingTiersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPricingTiersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPricingTiersClient
        """
        return self._raw_client

    async def get_pricing_tiers(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricingTiersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPricingTiersRequestSortField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPricingTiersResponse:
        """
        Schema for a Pricing Tier

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricingTiersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPricingTiersRequestSortField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricingTiersResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pricing_tiers.get_pricing_tiers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricing_tiers(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            request_options=request_options,
        )
        return _response.data

    async def get_pricing_tiers_id(
        self, id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPricingTierByIdResponse:
        """
        Schema for a Pricing Tier by ID

        Parameters
        ----------
        id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPricingTierByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pricing_tiers.get_pricing_tiers_id(
                id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricing_tiers_id(id, request_options=request_options)
        return _response.data
