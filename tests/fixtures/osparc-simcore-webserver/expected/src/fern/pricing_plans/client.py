

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_pricing_plan_get import EnvelopePricingPlanGet
from ..types.envelope_pricing_unit_get import EnvelopePricingUnitGet
from ..types.page_pricing_plan_get import PagePricingPlanGet
from .raw_client import AsyncRawPricingPlansClient, RawPricingPlansClient


class PricingPlansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPricingPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPricingPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPricingPlansClient
        """
        return self._raw_client

    def get_pricing_plan_unit(
        self, pricing_plan_id: int, pricing_unit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePricingUnitGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingUnitGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.pricing_plans.get_pricing_plan_unit(
            pricing_plan_id=1,
            pricing_unit_id=1,
        )
        """
        _response = self._raw_client.get_pricing_plan_unit(
            pricing_plan_id, pricing_unit_id, request_options=request_options
        )
        return _response.data

    def list_pricing_plans(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePricingPlanGet:
        """
        To keep the listing lightweight, the pricingUnits field is None.

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagePricingPlanGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.pricing_plans.list_pricing_plans()
        """
        _response = self._raw_client.list_pricing_plans(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def get_pricing_plan(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePricingPlanGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.pricing_plans.get_pricing_plan(
            pricing_plan_id=1,
        )
        """
        _response = self._raw_client.get_pricing_plan(pricing_plan_id, request_options=request_options)
        return _response.data


class AsyncPricingPlansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPricingPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPricingPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPricingPlansClient
        """
        return self._raw_client

    async def get_pricing_plan_unit(
        self, pricing_plan_id: int, pricing_unit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePricingUnitGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingUnitGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.pricing_plans.get_pricing_plan_unit(
                pricing_plan_id=1,
                pricing_unit_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricing_plan_unit(
            pricing_plan_id, pricing_unit_id, request_options=request_options
        )
        return _response.data

    async def list_pricing_plans(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePricingPlanGet:
        """
        To keep the listing lightweight, the pricingUnits field is None.

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagePricingPlanGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.pricing_plans.list_pricing_plans()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_pricing_plans(
            limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_pricing_plan(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePricingPlanGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.pricing_plans.get_pricing_plan(
                pricing_plan_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricing_plan(pricing_plan_id, request_options=request_options)
        return _response.data
