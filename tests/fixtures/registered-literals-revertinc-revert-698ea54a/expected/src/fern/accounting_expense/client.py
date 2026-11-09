

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accounting_create_or_update_expense_request import AccountingCreateOrUpdateExpenseRequest
from ..types.accounting_create_or_update_expense_response import AccountingCreateOrUpdateExpenseResponse
from ..types.accounting_delete_expense_response import AccountingDeleteExpenseResponse
from ..types.accounting_get_expense_response import AccountingGetExpenseResponse
from ..types.accounting_get_expenses_response import AccountingGetExpensesResponse
from .raw_client import AsyncRawAccountingExpenseClient, RawAccountingExpenseClient


OMIT = typing.cast(typing.Any, ...)


class AccountingExpenseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountingExpenseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountingExpenseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountingExpenseClient
        """
        return self._raw_client

    def accounting_expense_get_expense(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingGetExpenseResponse:
        """
        Get details of an Expense

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetExpenseResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_expense.accounting_expense_get_expense(
            id="id",
        )
        """
        _response = self._raw_client.accounting_expense_get_expense(id, fields=fields, request_options=request_options)
        return _response.data

    def accounting_expense_delete_expense(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingDeleteExpenseResponse:
        """
        Delete Expense

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingDeleteExpenseResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_expense.accounting_expense_delete_expense(
            id="id",
        )
        """
        _response = self._raw_client.accounting_expense_delete_expense(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    def accounting_expense_update_expense(
        self,
        id: str,
        *,
        request: AccountingCreateOrUpdateExpenseRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateExpenseResponse:
        """
        Update Expense

        Parameters
        ----------
        id : str

        request : AccountingCreateOrUpdateExpenseRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateExpenseResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_expense.accounting_expense_update_expense(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.accounting_expense_update_expense(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    def accounting_expense_get_expenses(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingGetExpensesResponse:
        """
        Get all the expenses

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetExpensesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_expense.accounting_expense_get_expenses()
        """
        _response = self._raw_client.accounting_expense_get_expenses(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    def accounting_expense_create_expense(
        self,
        *,
        request: AccountingCreateOrUpdateExpenseRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateExpenseResponse:
        """
        Post Expense

        Parameters
        ----------
        request : AccountingCreateOrUpdateExpenseRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateExpenseResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_expense.accounting_expense_create_expense(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.accounting_expense_create_expense(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data


class AsyncAccountingExpenseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountingExpenseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountingExpenseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountingExpenseClient
        """
        return self._raw_client

    async def accounting_expense_get_expense(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingGetExpenseResponse:
        """
        Get details of an Expense

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetExpenseResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_expense.accounting_expense_get_expense(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_expense_get_expense(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    async def accounting_expense_delete_expense(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountingDeleteExpenseResponse:
        """
        Delete Expense

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingDeleteExpenseResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_expense.accounting_expense_delete_expense(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_expense_delete_expense(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    async def accounting_expense_update_expense(
        self,
        id: str,
        *,
        request: AccountingCreateOrUpdateExpenseRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateExpenseResponse:
        """
        Update Expense

        Parameters
        ----------
        id : str

        request : AccountingCreateOrUpdateExpenseRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateExpenseResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_expense.accounting_expense_update_expense(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_expense_update_expense(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    async def accounting_expense_get_expenses(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingGetExpensesResponse:
        """
        Get all the expenses

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingGetExpensesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_expense.accounting_expense_get_expenses()


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_expense_get_expenses(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def accounting_expense_create_expense(
        self,
        *,
        request: AccountingCreateOrUpdateExpenseRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingCreateOrUpdateExpenseResponse:
        """
        Post Expense

        Parameters
        ----------
        request : AccountingCreateOrUpdateExpenseRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingCreateOrUpdateExpenseResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_expense.accounting_expense_create_expense(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_expense_create_expense(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data
