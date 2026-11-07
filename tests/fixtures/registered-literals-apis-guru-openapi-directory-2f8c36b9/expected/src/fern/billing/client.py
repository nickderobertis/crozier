

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.billing_position import BillingPosition
from ..types.service_costs import ServiceCosts
from .raw_client import AsyncRawBillingClient, RawBillingClient


class BillingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBillingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBillingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBillingClient
        """
        return self._raw_client

    def get_sum_for_organization(
        self,
        organization_id: str,
        *,
        from_date: typing.Optional[dt.datetime] = None,
        to_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceCosts:
        """
        Parameters
        ----------
        organization_id : str
            The organization to compute the billing information for

        from_date : typing.Optional[dt.datetime]
            Billing start date

        to_date : typing.Optional[dt.datetime]
            Billing end date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceCosts
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.billing.get_sum_for_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_sum_for_organization(
            organization_id, from_date=from_date, to_date=to_date, request_options=request_options
        )
        return _response.data

    def get_positions_for_organization(
        self,
        organization_id: str,
        *,
        from_date: typing.Optional[dt.datetime] = None,
        to_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BillingPosition]:
        """
        Parameters
        ----------
        organization_id : str
            The organization to compute the billing information for

        from_date : typing.Optional[dt.datetime]
            Billing start date

        to_date : typing.Optional[dt.datetime]
            Billing end date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BillingPosition]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.billing.get_positions_for_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_positions_for_organization(
            organization_id, from_date=from_date, to_date=to_date, request_options=request_options
        )
        return _response.data


class AsyncBillingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBillingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBillingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBillingClient
        """
        return self._raw_client

    async def get_sum_for_organization(
        self,
        organization_id: str,
        *,
        from_date: typing.Optional[dt.datetime] = None,
        to_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceCosts:
        """
        Parameters
        ----------
        organization_id : str
            The organization to compute the billing information for

        from_date : typing.Optional[dt.datetime]
            Billing start date

        to_date : typing.Optional[dt.datetime]
            Billing end date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceCosts
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.billing.get_sum_for_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sum_for_organization(
            organization_id, from_date=from_date, to_date=to_date, request_options=request_options
        )
        return _response.data

    async def get_positions_for_organization(
        self,
        organization_id: str,
        *,
        from_date: typing.Optional[dt.datetime] = None,
        to_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BillingPosition]:
        """
        Parameters
        ----------
        organization_id : str
            The organization to compute the billing information for

        from_date : typing.Optional[dt.datetime]
            Billing start date

        to_date : typing.Optional[dt.datetime]
            Billing end date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BillingPosition]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.billing.get_positions_for_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_positions_for_organization(
            organization_id, from_date=from_date, to_date=to_date, request_options=request_options
        )
        return _response.data
