

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accounting_create_or_update_account_request import AccountingCreateOrUpdateAccountRequest
from ..types.accounting_create_or_update_account_response import AccountingCreateOrUpdateAccountResponse
from ..types.accounting_delete_account_response import AccountingDeleteAccountResponse
from ..types.accounting_get_account_response import AccountingGetAccountResponse
from ..types.accounting_get_accounts_response import AccountingGetAccountsResponse
from .raw_client import AsyncRawAccountingAccountClient, RawAccountingAccountClient


OMIT = typing.cast(typing.Any, ...)


class AccountingAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountingAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountingAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountingAccountClient
        """
        return self._raw_client

    def accounting_account_get_account(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingGetAccountResponse:
        """
        Get details of an account

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetAccountResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_account.accounting_account_get_account(
            id="id",
        )
        """
        _response = self._raw_client.accounting_account_get_account(id, fields=fields, request_options=request_options)
        return _response.data

    def accounting_account_delete_account(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingDeleteAccountResponse:
        """
        Delete account

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingDeleteAccountResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_account.accounting_account_delete_account(
            id="id",
        )
        """
        _response = self._raw_client.accounting_account_delete_account(id, request_options=request_options)
        return _response.data

    def accounting_account_update_account(
        self,
        id: str,
        *,
        request: AccountingCreateOrUpdateAccountRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateAccountResponse:
        """
        Update Account

        Parameters
        ----------
        id : str

        request : AccountingCreateOrUpdateAccountRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateAccountResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_account.accounting_account_update_account(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.accounting_account_update_account(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    def accounting_account_get_accounts(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingGetAccountsResponse:
        """
        Get all the accounts

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetAccountsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_account.accounting_account_get_accounts()
        """
        _response = self._raw_client.accounting_account_get_accounts(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    def accounting_account_create_account(
        self,
        *,
        request: AccountingCreateOrUpdateAccountRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateAccountResponse:
        """
        Post Account

        Parameters
        ----------
        request : AccountingCreateOrUpdateAccountRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateAccountResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_account.accounting_account_create_account(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.accounting_account_create_account(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data


class AsyncAccountingAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountingAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountingAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountingAccountClient
        """
        return self._raw_client

    async def accounting_account_get_account(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingGetAccountResponse:
        """
        Get details of an account

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetAccountResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_account.accounting_account_get_account(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_account_get_account(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    async def accounting_account_delete_account(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingDeleteAccountResponse:
        """
        Delete account

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingDeleteAccountResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_account.accounting_account_delete_account(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_account_delete_account(id, request_options=request_options)
        return _response.data

    async def accounting_account_update_account(
        self,
        id: str,
        *,
        request: AccountingCreateOrUpdateAccountRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateAccountResponse:
        """
        Update Account

        Parameters
        ----------
        id : str

        request : AccountingCreateOrUpdateAccountRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateAccountResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_account.accounting_account_update_account(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_account_update_account(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    async def accounting_account_get_accounts(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingGetAccountsResponse:
        """
        Get all the accounts

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetAccountsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_account.accounting_account_get_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_account_get_accounts(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def accounting_account_create_account(
        self,
        *,
        request: AccountingCreateOrUpdateAccountRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateAccountResponse:
        """
        Post Account

        Parameters
        ----------
        request : AccountingCreateOrUpdateAccountRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateAccountResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_account.accounting_account_create_account(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_account_create_account(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data
