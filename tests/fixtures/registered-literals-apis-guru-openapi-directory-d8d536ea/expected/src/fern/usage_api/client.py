

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.billing_cycle_usage_response import BillingCycleUsageResponse
from ..types.billing_cycles_response import BillingCyclesResponse
from ..types.daily_usage_response import DailyUsageResponse
from .raw_client import AsyncRawUsageApiClient, RawUsageApiClient


class UsageApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsageApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsageApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsageApiClient
        """
        return self._raw_client

    def get_billing_usage_by_billing_cycle(
        self, billing_cycle: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BillingCycleUsageResponse:
        """
        An endpoint to obtain information on API usage for a specific billing cycle.

        Parameters
        ----------
        billing_cycle : str
            The date obtainable from the /billingCycles endpoint which is used as an identifier for the specific billing cycle you wish to obtain information on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCycleUsageResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usage_api.get_billing_usage_by_billing_cycle(
            billing_cycle="2023-01-25to2023-02-25",
        )
        """
        _response = self._raw_client.get_billing_usage_by_billing_cycle(billing_cycle, request_options=request_options)
        return _response.data

    def get_billing_cycles(self, *, request_options: typing.Optional[RequestOptions] = None) -> BillingCyclesResponse:
        """
        An endpoint to obtain information on the previous 12 billing cycles.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCyclesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usage_api.get_billing_cycles()
        """
        _response = self._raw_client.get_billing_cycles(request_options=request_options)
        return _response.data

    def get_daily_usage_by_date(
        self, date: dt.date, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyUsageResponse:
        """
        An endpoint to obtain information on API usage for a specific day.

        Parameters
        ----------
        date : dt.date
            The specific date for which you wish to obtain information on API usage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyUsageResponse
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usage_api.get_daily_usage_by_date(
            date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.get_daily_usage_by_date(date, request_options=request_options)
        return _response.data


class AsyncUsageApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsageApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsageApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsageApiClient
        """
        return self._raw_client

    async def get_billing_usage_by_billing_cycle(
        self, billing_cycle: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BillingCycleUsageResponse:
        """
        An endpoint to obtain information on API usage for a specific billing cycle.

        Parameters
        ----------
        billing_cycle : str
            The date obtainable from the /billingCycles endpoint which is used as an identifier for the specific billing cycle you wish to obtain information on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCycleUsageResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usage_api.get_billing_usage_by_billing_cycle(
                billing_cycle="2023-01-25to2023-02-25",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_billing_usage_by_billing_cycle(
            billing_cycle, request_options=request_options
        )
        return _response.data

    async def get_billing_cycles(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BillingCyclesResponse:
        """
        An endpoint to obtain information on the previous 12 billing cycles.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCyclesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usage_api.get_billing_cycles()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_billing_cycles(request_options=request_options)
        return _response.data

    async def get_daily_usage_by_date(
        self, date: dt.date, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyUsageResponse:
        """
        An endpoint to obtain information on API usage for a specific day.

        Parameters
        ----------
        date : dt.date
            The specific date for which you wish to obtain information on API usage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyUsageResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usage_api.get_daily_usage_by_date(
                date=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_daily_usage_by_date(date, request_options=request_options)
        return _response.data
