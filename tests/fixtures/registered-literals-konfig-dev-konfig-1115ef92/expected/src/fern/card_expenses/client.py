

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.expandable_expense import ExpandableExpense
from ..types.expense import Expense
from ..types.expense_payment_status import ExpensePaymentStatus
from ..types.expense_status import ExpenseStatus
from ..types.page_expandable_expense import PageExpandableExpense
from .raw_client import AsyncRawCardExpensesClient, RawCardExpensesClient


OMIT = typing.cast(typing.Any, ...)


class CardExpensesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCardExpensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCardExpensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCardExpensesClient
        """
        return self._raw_client

    def list_expenses(
        self,
        *,
        expand: typing.Optional[typing.Sequence[str]] = None,
        user_id: typing.Optional[typing.Sequence[str]] = None,
        parent_expense_id: typing.Optional[typing.Sequence[str]] = None,
        budget_id: typing.Optional[typing.Sequence[str]] = None,
        status: typing.Optional[typing.Sequence[ExpenseStatus]] = None,
        payment_status: typing.Optional[typing.Sequence[ExpensePaymentStatus]] = None,
        purchased_at_start: typing.Optional[dt.datetime] = None,
        purchased_at_end: typing.Optional[dt.datetime] = None,
        load_custom_fields: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageExpandableExpense:
        """
        List expenses under the same account. Admin and bookkeeper have access to any expense, and regular users can only access their own.

        Parameters
        ----------
        expand : typing.Optional[typing.Sequence[str]]
            Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

        user_id : typing.Optional[typing.Sequence[str]]
            Get expenses belong to provided user(s).

        parent_expense_id : typing.Optional[typing.Sequence[str]]
            Get itemized expenses belong to provided parent expenses ID(s).

        budget_id : typing.Optional[typing.Sequence[str]]

        status : typing.Optional[typing.Sequence[ExpenseStatus]]

        payment_status : typing.Optional[typing.Sequence[ExpensePaymentStatus]]

        purchased_at_start : typing.Optional[dt.datetime]

            Shows only expenses with a `purchased_at` on or after this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999

        purchased_at_end : typing.Optional[dt.datetime]

            Shows only expenses with a `purchased_at` on or before this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999

        load_custom_fields : typing.Optional[bool]
            Load custom fields for the expenses.

        cursor : typing.Optional[str]

            The cursor to use for pagination. This is the `next_cursor` value returned from the previous response.

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageExpandableExpense
            listExpenses 200 response

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.card_expenses.list_expenses(
            purchased_at_start=datetime.datetime.fromisoformat(
                "2023-01-01 23:59:59+00:00",
            ),
            purchased_at_end=datetime.datetime.fromisoformat(
                "2023-01-10 23:59:59+00:00",
            ),
        )
        """
        _response = self._raw_client.list_expenses(
            expand=expand,
            user_id=user_id,
            parent_expense_id=parent_expense_id,
            budget_id=budget_id,
            status=status,
            payment_status=payment_status,
            purchased_at_start=purchased_at_start,
            purchased_at_end=purchased_at_end,
            load_custom_fields=load_custom_fields,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def get_expense(
        self,
        expense_id: str,
        *,
        expand: typing.Optional[typing.Sequence[str]] = None,
        load_custom_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpandableExpense:
        """
        Get an expense by its ID.

        Parameters
        ----------
        expense_id : str

        expand : typing.Optional[typing.Sequence[str]]
            Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

        load_custom_fields : typing.Optional[bool]
            Load custom fields for the expense.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpandableExpense
            getExpense 200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.card_expenses.get_expense(
            expense_id="expense_id",
        )
        """
        _response = self._raw_client.get_expense(
            expense_id, expand=expand, load_custom_fields=load_custom_fields, request_options=request_options
        )
        return _response.data

    def update_expense(
        self,
        expense_id: str,
        *,
        memo: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Expense:
        """
        Update an expense. Admin and bookkeeper have access to any expense, and regular users can only access their own.

        Parameters
        ----------
        expense_id : str

        memo : typing.Optional[str]
            Expense memo.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Expense
            updateExpense 200 response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.card_expenses.update_expense(
            expense_id="expense_id",
        )
        """
        _response = self._raw_client.update_expense(expense_id, memo=memo, request_options=request_options)
        return _response.data


class AsyncCardExpensesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCardExpensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCardExpensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCardExpensesClient
        """
        return self._raw_client

    async def list_expenses(
        self,
        *,
        expand: typing.Optional[typing.Sequence[str]] = None,
        user_id: typing.Optional[typing.Sequence[str]] = None,
        parent_expense_id: typing.Optional[typing.Sequence[str]] = None,
        budget_id: typing.Optional[typing.Sequence[str]] = None,
        status: typing.Optional[typing.Sequence[ExpenseStatus]] = None,
        payment_status: typing.Optional[typing.Sequence[ExpensePaymentStatus]] = None,
        purchased_at_start: typing.Optional[dt.datetime] = None,
        purchased_at_end: typing.Optional[dt.datetime] = None,
        load_custom_fields: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageExpandableExpense:
        """
        List expenses under the same account. Admin and bookkeeper have access to any expense, and regular users can only access their own.

        Parameters
        ----------
        expand : typing.Optional[typing.Sequence[str]]
            Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

        user_id : typing.Optional[typing.Sequence[str]]
            Get expenses belong to provided user(s).

        parent_expense_id : typing.Optional[typing.Sequence[str]]
            Get itemized expenses belong to provided parent expenses ID(s).

        budget_id : typing.Optional[typing.Sequence[str]]

        status : typing.Optional[typing.Sequence[ExpenseStatus]]

        payment_status : typing.Optional[typing.Sequence[ExpensePaymentStatus]]

        purchased_at_start : typing.Optional[dt.datetime]

            Shows only expenses with a `purchased_at` on or after this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999

        purchased_at_end : typing.Optional[dt.datetime]

            Shows only expenses with a `purchased_at` on or before this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999

        load_custom_fields : typing.Optional[bool]
            Load custom fields for the expenses.

        cursor : typing.Optional[str]

            The cursor to use for pagination. This is the `next_cursor` value returned from the previous response.

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageExpandableExpense
            listExpenses 200 response

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.card_expenses.list_expenses(
                purchased_at_start=datetime.datetime.fromisoformat(
                    "2023-01-01 23:59:59+00:00",
                ),
                purchased_at_end=datetime.datetime.fromisoformat(
                    "2023-01-10 23:59:59+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_expenses(
            expand=expand,
            user_id=user_id,
            parent_expense_id=parent_expense_id,
            budget_id=budget_id,
            status=status,
            payment_status=payment_status,
            purchased_at_start=purchased_at_start,
            purchased_at_end=purchased_at_end,
            load_custom_fields=load_custom_fields,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def get_expense(
        self,
        expense_id: str,
        *,
        expand: typing.Optional[typing.Sequence[str]] = None,
        load_custom_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpandableExpense:
        """
        Get an expense by its ID.

        Parameters
        ----------
        expense_id : str

        expand : typing.Optional[typing.Sequence[str]]
            Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

        load_custom_fields : typing.Optional[bool]
            Load custom fields for the expense.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpandableExpense
            getExpense 200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.card_expenses.get_expense(
                expense_id="expense_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_expense(
            expense_id, expand=expand, load_custom_fields=load_custom_fields, request_options=request_options
        )
        return _response.data

    async def update_expense(
        self,
        expense_id: str,
        *,
        memo: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Expense:
        """
        Update an expense. Admin and bookkeeper have access to any expense, and regular users can only access their own.

        Parameters
        ----------
        expense_id : str

        memo : typing.Optional[str]
            Expense memo.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Expense
            updateExpense 200 response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.card_expenses.update_expense(
                expense_id="expense_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_expense(expense_id, memo=memo, request_options=request_options)
        return _response.data
