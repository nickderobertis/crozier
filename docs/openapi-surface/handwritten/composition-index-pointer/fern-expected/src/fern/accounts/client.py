

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account import Account
from ..types.categorised_account import CategorisedAccount
from .raw_client import AsyncRawAccountsClient, RawAccountsClient


class AccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountsClient
        """
        return self._raw_client

    def get_account(
        self, company_id: str, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Account:
        """
        Parameters
        ----------
        company_id : str

        account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.accounts.get_account(
            company_id="companyId",
            account_id="accountId",
        )
        """
        _response = self._raw_client.get_account(company_id, account_id, request_options=request_options)
        return _response.data

    def list_categorised_accounts(
        self, company_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CategorisedAccount]:
        """
        Parameters
        ----------
        company_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CategorisedAccount]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.accounts.list_categorised_accounts(
            company_id="companyId",
        )
        """
        _response = self._raw_client.list_categorised_accounts(company_id, request_options=request_options)
        return _response.data


class AsyncAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountsClient
        """
        return self._raw_client

    async def get_account(
        self, company_id: str, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Account:
        """
        Parameters
        ----------
        company_id : str

        account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.accounts.get_account(
                company_id="companyId",
                account_id="accountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account(company_id, account_id, request_options=request_options)
        return _response.data

    async def list_categorised_accounts(
        self, company_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CategorisedAccount]:
        """
        Parameters
        ----------
        company_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CategorisedAccount]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.accounts.list_categorised_accounts(
                company_id="companyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_categorised_accounts(company_id, request_options=request_options)
        return _response.data
