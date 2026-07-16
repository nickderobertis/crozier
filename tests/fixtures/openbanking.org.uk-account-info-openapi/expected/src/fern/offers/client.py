

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ob_read_offer1 import ObReadOffer1
from .raw_client import AsyncRawOffersClient, RawOffersClient


class OffersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOffersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOffersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOffersClient
        """
        return self._raw_client

    def get_accounts_account_id_offers(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadOffer1:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadOffer1
            Offers Read

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
        client.offers.get_accounts_account_id_offers(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_offers(account_id, request_options=request_options)
        return _response.data

    def get_offers(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadOffer1:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadOffer1
            Offers Read

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
        client.offers.get_offers()
        """
        _response = self._raw_client.get_offers(request_options=request_options)
        return _response.data


class AsyncOffersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOffersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOffersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOffersClient
        """
        return self._raw_client

    async def get_accounts_account_id_offers(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadOffer1:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadOffer1
            Offers Read

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
            await client.offers.get_accounts_account_id_offers(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_offers(account_id, request_options=request_options)
        return _response.data

    async def get_offers(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadOffer1:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadOffer1
            Offers Read

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
            await client.offers.get_offers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_offers(request_options=request_options)
        return _response.data
