

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ob_read_scheduled_payment3 import ObReadScheduledPayment3
from .raw_client import AsyncRawScheduledPaymentsClient, RawScheduledPaymentsClient


class ScheduledPaymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScheduledPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScheduledPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScheduledPaymentsClient
        """
        return self._raw_client

    def get_accounts_account_id_scheduled_payments(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadScheduledPayment3:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadScheduledPayment3
            Scheduled Payments Read

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )
        client.scheduled_payments.get_accounts_account_id_scheduled_payments(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_scheduled_payments(
            account_id, request_options=request_options
        )
        return _response.data

    def get_scheduled_payments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadScheduledPayment3:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadScheduledPayment3
            Scheduled Payments Read

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )
        client.scheduled_payments.get_scheduled_payments()
        """
        _response = self._raw_client.get_scheduled_payments(request_options=request_options)
        return _response.data


class AsyncScheduledPaymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScheduledPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScheduledPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScheduledPaymentsClient
        """
        return self._raw_client

    async def get_accounts_account_id_scheduled_payments(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadScheduledPayment3:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadScheduledPayment3
            Scheduled Payments Read

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.scheduled_payments.get_accounts_account_id_scheduled_payments(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_scheduled_payments(
            account_id, request_options=request_options
        )
        return _response.data

    async def get_scheduled_payments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadScheduledPayment3:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadScheduledPayment3
            Scheduled Payments Read

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.scheduled_payments.get_scheduled_payments()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_scheduled_payments(request_options=request_options)
        return _response.data
