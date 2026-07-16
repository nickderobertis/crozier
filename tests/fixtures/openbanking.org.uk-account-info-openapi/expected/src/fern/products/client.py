

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ob_read_product2 import ObReadProduct2
from .raw_client import AsyncRawProductsClient, RawProductsClient


class ProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProductsClient
        """
        return self._raw_client

    def get_accounts_account_id_product(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadProduct2:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadProduct2
            Products Read

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
        client.products.get_accounts_account_id_product(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_product(account_id, request_options=request_options)
        return _response.data

    def get_products(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadProduct2:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadProduct2
            Products Read

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
        client.products.get_products()
        """
        _response = self._raw_client.get_products(request_options=request_options)
        return _response.data


class AsyncProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProductsClient
        """
        return self._raw_client

    async def get_accounts_account_id_product(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadProduct2:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadProduct2
            Products Read

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
            await client.products.get_accounts_account_id_product(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_product(account_id, request_options=request_options)
        return _response.data

    async def get_products(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadProduct2:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadProduct2
            Products Read

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
            await client.products.get_products()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_products(request_options=request_options)
        return _response.data
