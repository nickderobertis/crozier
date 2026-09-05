

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.page_osparc_credits_aggregated_by_service_get import PageOsparcCreditsAggregatedByServiceGet
from ..types.page_service_run_get import PageServiceRunGet
from ..types.services_aggregated_usages_time_period import ServicesAggregatedUsagesTimePeriod
from ..types.services_aggregated_usages_type import ServicesAggregatedUsagesType
from ..types.wallet_id_int import WalletIdInt
from .raw_client import AsyncRawUsageClient, RawUsageClient


class UsageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsageClient
        """
        return self._raw_client

    def list_resource_usage_services(
        self,
        *,
        order_by: typing.Optional[str] = None,
        wallet_id: typing.Optional[WalletIdInt] = None,
        filters: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageServiceRunGet:
        """
        Retrieve finished and currently running user services (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        order_by : typing.Optional[str]

        wallet_id : typing.Optional[WalletIdInt]

        filters : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageServiceRunGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.usage.list_resource_usage_services()
        """
        _response = self._raw_client.list_resource_usage_services(
            order_by=order_by,
            wallet_id=wallet_id,
            filters=filters,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def list_osparc_credits_aggregated_usages(
        self,
        *,
        aggregated_by: ServicesAggregatedUsagesType,
        time_period: ServicesAggregatedUsagesTimePeriod,
        wallet_id: WalletIdInt,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageOsparcCreditsAggregatedByServiceGet:
        """
        Used credits based on aggregate by type, currently supported `services`. (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        aggregated_by : ServicesAggregatedUsagesType

        time_period : ServicesAggregatedUsagesTimePeriod

        wallet_id : WalletIdInt

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageOsparcCreditsAggregatedByServiceGet
            Successful Response

        Examples
        --------
        from fern import FernApi, ServicesAggregatedUsagesType

        client = FernApi()
        client.usage.list_osparc_credits_aggregated_usages(
            aggregated_by=ServicesAggregatedUsagesType.SERVICES,
            time_period=1,
            wallet_id=1,
        )
        """
        _response = self._raw_client.list_osparc_credits_aggregated_usages(
            aggregated_by=aggregated_by,
            time_period=time_period,
            wallet_id=wallet_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def export_resource_usage_services(
        self,
        *,
        order_by: typing.Optional[str] = None,
        wallet_id: typing.Optional[WalletIdInt] = None,
        filters: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Redirects to download CSV link. CSV obtains finished and currently running user services (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        order_by : typing.Optional[str]

        wallet_id : typing.Optional[WalletIdInt]

        filters : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.usage.export_resource_usage_services()
        """
        _response = self._raw_client.export_resource_usage_services(
            order_by=order_by, wallet_id=wallet_id, filters=filters, request_options=request_options
        )
        return _response.data


class AsyncUsageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsageClient
        """
        return self._raw_client

    async def list_resource_usage_services(
        self,
        *,
        order_by: typing.Optional[str] = None,
        wallet_id: typing.Optional[WalletIdInt] = None,
        filters: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageServiceRunGet:
        """
        Retrieve finished and currently running user services (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        order_by : typing.Optional[str]

        wallet_id : typing.Optional[WalletIdInt]

        filters : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageServiceRunGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.usage.list_resource_usage_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_resource_usage_services(
            order_by=order_by,
            wallet_id=wallet_id,
            filters=filters,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def list_osparc_credits_aggregated_usages(
        self,
        *,
        aggregated_by: ServicesAggregatedUsagesType,
        time_period: ServicesAggregatedUsagesTimePeriod,
        wallet_id: WalletIdInt,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageOsparcCreditsAggregatedByServiceGet:
        """
        Used credits based on aggregate by type, currently supported `services`. (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        aggregated_by : ServicesAggregatedUsagesType

        time_period : ServicesAggregatedUsagesTimePeriod

        wallet_id : WalletIdInt

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageOsparcCreditsAggregatedByServiceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ServicesAggregatedUsagesType

        client = AsyncFernApi()


        async def main() -> None:
            await client.usage.list_osparc_credits_aggregated_usages(
                aggregated_by=ServicesAggregatedUsagesType.SERVICES,
                time_period=1,
                wallet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_osparc_credits_aggregated_usages(
            aggregated_by=aggregated_by,
            time_period=time_period,
            wallet_id=wallet_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def export_resource_usage_services(
        self,
        *,
        order_by: typing.Optional[str] = None,
        wallet_id: typing.Optional[WalletIdInt] = None,
        filters: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Redirects to download CSV link. CSV obtains finished and currently running user services (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        order_by : typing.Optional[str]

        wallet_id : typing.Optional[WalletIdInt]

        filters : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.usage.export_resource_usage_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.export_resource_usage_services(
            order_by=order_by, wallet_id=wallet_id, filters=filters, request_options=request_options
        )
        return _response.data
