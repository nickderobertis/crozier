

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBillingAccountClient, RawBillingAccountClient
from .types.get_billing_account_balance_history_response import GetBillingAccountBalanceHistoryResponse
from .types.get_billing_account_response import GetBillingAccountResponse
from .types.get_billing_accounts_response import GetBillingAccountsResponse


class BillingAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBillingAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBillingAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBillingAccountClient
        """
        return self._raw_client

    def get_billing_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBillingAccountsResponse:
        """
        Get Billing Accounts accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillingAccountsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing_account.get_billing_accounts()
        """
        _response = self._raw_client.get_billing_accounts(request_options=request_options)
        return _response.data

    def get_billing_account(
        self, billing_account_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBillingAccountResponse:
        """
        Get Billing Account Information

        Parameters
        ----------
        billing_account_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillingAccountResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing_account.get_billing_account(
            billing_account_uid="00000000-0000-0000-000000000001",
        )
        """
        _response = self._raw_client.get_billing_account(billing_account_uid, request_options=request_options)
        return _response.data

    def get_billing_account_balance_history(
        self,
        billing_account_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBillingAccountBalanceHistoryResponse:
        """
        Get Billing Account Balance history

        Parameters
        ----------
        billing_account_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillingAccountBalanceHistoryResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing_account.get_billing_account_balance_history(
            billing_account_uid="00000000-0000-0000-000000000001",
        )
        """
        _response = self._raw_client.get_billing_account_balance_history(
            billing_account_uid, start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data


class AsyncBillingAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBillingAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBillingAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBillingAccountClient
        """
        return self._raw_client

    async def get_billing_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBillingAccountsResponse:
        """
        Get Billing Accounts accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillingAccountsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing_account.get_billing_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_billing_accounts(request_options=request_options)
        return _response.data

    async def get_billing_account(
        self, billing_account_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBillingAccountResponse:
        """
        Get Billing Account Information

        Parameters
        ----------
        billing_account_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillingAccountResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing_account.get_billing_account(
                billing_account_uid="00000000-0000-0000-000000000001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_billing_account(billing_account_uid, request_options=request_options)
        return _response.data

    async def get_billing_account_balance_history(
        self,
        billing_account_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBillingAccountBalanceHistoryResponse:
        """
        Get Billing Account Balance history

        Parameters
        ----------
        billing_account_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillingAccountBalanceHistoryResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing_account.get_billing_account_balance_history(
                billing_account_uid="00000000-0000-0000-000000000001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_billing_account_balance_history(
            billing_account_uid, start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data
