

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ob_read_standing_order6 import ObReadStandingOrder6
from .raw_client import AsyncRawStandingOrdersClient, RawStandingOrdersClient


class StandingOrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStandingOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStandingOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStandingOrdersClient
        """
        return self._raw_client

    def get_accounts_account_id_standing_orders(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadStandingOrder6:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadStandingOrder6
            Standing Orders Read

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
        client.standing_orders.get_accounts_account_id_standing_orders(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_standing_orders(
            account_id, request_options=request_options
        )
        return _response.data

    def get_standing_orders(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadStandingOrder6:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadStandingOrder6
            Standing Orders Read

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
        client.standing_orders.get_standing_orders()
        """
        _response = self._raw_client.get_standing_orders(request_options=request_options)
        return _response.data


class AsyncStandingOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStandingOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStandingOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStandingOrdersClient
        """
        return self._raw_client

    async def get_accounts_account_id_standing_orders(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadStandingOrder6:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadStandingOrder6
            Standing Orders Read

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
            await client.standing_orders.get_accounts_account_id_standing_orders(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_standing_orders(
            account_id, request_options=request_options
        )
        return _response.data

    async def get_standing_orders(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadStandingOrder6:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadStandingOrder6
            Standing Orders Read

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
            await client.standing_orders.get_standing_orders()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_standing_orders(request_options=request_options)
        return _response.data
