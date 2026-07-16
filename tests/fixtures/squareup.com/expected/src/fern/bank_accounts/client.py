

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_bank_account_by_v1id_response import GetBankAccountByV1IdResponse
from ..types.get_bank_account_response import GetBankAccountResponse
from ..types.list_bank_accounts_response import ListBankAccountsResponse
from .raw_client import AsyncRawBankAccountsClient, RawBankAccountsClient


class BankAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBankAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBankAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBankAccountsClient
        """
        return self._raw_client

    def list_bank_accounts(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBankAccountsResponse:
        """
        Returns a list of [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) objects linked to a Square account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor returned by a previous call to this endpoint.
            Use it in the next `ListBankAccounts` request to retrieve the next set
            of results.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        limit : typing.Optional[int]
            Upper limit on the number of bank accounts to return in the response.
            Currently, 1000 is the largest supported limit. You can specify a limit
            of up to 1000 bank accounts. This is also the default limit.

        location_id : typing.Optional[str]
            Location ID. You can specify this optional filter
            to retrieve only the linked bank accounts belonging to a specific location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBankAccountsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bank_accounts.list_bank_accounts()
        """
        _response = self._raw_client.list_bank_accounts(
            cursor=cursor, limit=limit, location_id=location_id, request_options=request_options
        )
        return _response.data

    def get_bank_account_by_v1id(
        self, v1bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBankAccountByV1IdResponse:
        """
        Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) identified by V1 bank account ID.

        Parameters
        ----------
        v1bank_account_id : str
            Connect V1 ID of the desired `BankAccount`. For more information, see
            [Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBankAccountByV1IdResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bank_accounts.get_bank_account_by_v1id(
            v1bank_account_id="v1_bank_account_id",
        )
        """
        _response = self._raw_client.get_bank_account_by_v1id(v1bank_account_id, request_options=request_options)
        return _response.data

    def get_bank_account(
        self, bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBankAccountResponse:
        """
        Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount)
        linked to a Square account.

        Parameters
        ----------
        bank_account_id : str
            Square-issued ID of the desired `BankAccount`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBankAccountResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bank_accounts.get_bank_account(
            bank_account_id="bank_account_id",
        )
        """
        _response = self._raw_client.get_bank_account(bank_account_id, request_options=request_options)
        return _response.data


class AsyncBankAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBankAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBankAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBankAccountsClient
        """
        return self._raw_client

    async def list_bank_accounts(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBankAccountsResponse:
        """
        Returns a list of [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) objects linked to a Square account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor returned by a previous call to this endpoint.
            Use it in the next `ListBankAccounts` request to retrieve the next set
            of results.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        limit : typing.Optional[int]
            Upper limit on the number of bank accounts to return in the response.
            Currently, 1000 is the largest supported limit. You can specify a limit
            of up to 1000 bank accounts. This is also the default limit.

        location_id : typing.Optional[str]
            Location ID. You can specify this optional filter
            to retrieve only the linked bank accounts belonging to a specific location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBankAccountsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bank_accounts.list_bank_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_bank_accounts(
            cursor=cursor, limit=limit, location_id=location_id, request_options=request_options
        )
        return _response.data

    async def get_bank_account_by_v1id(
        self, v1bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBankAccountByV1IdResponse:
        """
        Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) identified by V1 bank account ID.

        Parameters
        ----------
        v1bank_account_id : str
            Connect V1 ID of the desired `BankAccount`. For more information, see
            [Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBankAccountByV1IdResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bank_accounts.get_bank_account_by_v1id(
                v1bank_account_id="v1_bank_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bank_account_by_v1id(v1bank_account_id, request_options=request_options)
        return _response.data

    async def get_bank_account(
        self, bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBankAccountResponse:
        """
        Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount)
        linked to a Square account.

        Parameters
        ----------
        bank_account_id : str
            Square-issued ID of the desired `BankAccount`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBankAccountResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bank_accounts.get_bank_account(
                bank_account_id="bank_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bank_account(bank_account_id, request_options=request_options)
        return _response.data
