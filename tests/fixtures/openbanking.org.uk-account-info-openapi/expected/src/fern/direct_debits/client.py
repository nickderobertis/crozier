

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ob_read_direct_debit2 import ObReadDirectDebit2
from .raw_client import AsyncRawDirectDebitsClient, RawDirectDebitsClient


class DirectDebitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDirectDebitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDirectDebitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDirectDebitsClient
        """
        return self._raw_client

    def get_accounts_account_id_direct_debits(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadDirectDebit2:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadDirectDebit2
            Direct Debits Read

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
        client.direct_debits.get_accounts_account_id_direct_debits(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_direct_debits(account_id, request_options=request_options)
        return _response.data

    def get_direct_debits(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadDirectDebit2:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadDirectDebit2
            Direct Debits Read

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
        client.direct_debits.get_direct_debits()
        """
        _response = self._raw_client.get_direct_debits(request_options=request_options)
        return _response.data


class AsyncDirectDebitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDirectDebitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDirectDebitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDirectDebitsClient
        """
        return self._raw_client

    async def get_accounts_account_id_direct_debits(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadDirectDebit2:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadDirectDebit2
            Direct Debits Read

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
            await client.direct_debits.get_accounts_account_id_direct_debits(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_direct_debits(
            account_id, request_options=request_options
        )
        return _response.data

    async def get_direct_debits(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadDirectDebit2:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadDirectDebit2
            Direct Debits Read

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
            await client.direct_debits.get_direct_debits()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_direct_debits(request_options=request_options)
        return _response.data
