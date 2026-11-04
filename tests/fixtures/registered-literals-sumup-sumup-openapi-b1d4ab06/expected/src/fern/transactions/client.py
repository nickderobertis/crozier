

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.entry_mode import EntryMode
from ..types.payment_type import PaymentType
from ..types.transaction_full import TransactionFull
from .raw_client import AsyncRawTransactionsClient, RawTransactionsClient
from .types.list_transactions_v21request_order import ListTransactionsV21RequestOrder
from .types.list_transactions_v21request_statuses_item import ListTransactionsV21RequestStatusesItem
from .types.list_transactions_v21request_types_item import ListTransactionsV21RequestTypesItem
from .types.list_transactions_v21response import ListTransactionsV21Response


OMIT = typing.cast(typing.Any, ...)


class TransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransactionsClient
        """
        return self._raw_client

    def refund_transaction(
        self,
        merchant_code: str,
        transaction_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Refunds an identified transaction either in full or partially.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        transaction_id : str
            Unique identifier of the transaction.

        amount : typing.Optional[float]
            Amount to be refunded. Eligible amount can't exceed the amount of the transaction and varies based on country and currency. If you do not specify a value, the system performs a full refund of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The transaction was refunded in full or partially based on the request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transactions.refund_transaction(
            merchant_code="MH4H92C7",
            transaction_id="4ffb8dfc-7f2b-413d-a497-2ad00766585e",
            amount=5.0,
        )
        """
        _response = self._raw_client.refund_transaction(
            merchant_code, transaction_id, amount=amount, request_options=request_options
        )
        return _response.data

    def get_transaction_v21(
        self,
        merchant_code: str,
        *,
        id: typing.Optional[str] = None,
        transaction_code: typing.Optional[str] = None,
        foreign_transaction_id: typing.Optional[str] = None,
        client_transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionFull:
        """
        Retrieves the full details of an identified transaction. The transaction resource is identified by a query parameter and *one* of following parameters is required:
        - `id`
        - `transaction_code`
        - `foreign_transaction_id`
        - `client_transaction_id`

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        id : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction ID (the `id` parameter in the transaction resource).

        transaction_code : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction code.

        foreign_transaction_id : typing.Optional[str]
            External transaction identifier supplied by the client.

        client_transaction_id : typing.Optional[str]
            Client-supplied identifier of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionFull
            Returns the requested transaction resource.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transactions.get_transaction_v21(
            merchant_code="MH4H92C7",
            id="410fc44a-5956-44e1-b5cc-19c6f8d727a4",
            transaction_code="TEENSK4W2K",
            foreign_transaction_id="J13253253x1",
            client_transaction_id="urn:sumup:pos:sale:MNKKNGST:1D4E3B2D-111D-48D7-9AF0-832DAEF63DD7;2",
        )
        """
        _response = self._raw_client.get_transaction_v21(
            merchant_code,
            id=id,
            transaction_code=transaction_code,
            foreign_transaction_id=foreign_transaction_id,
            client_transaction_id=client_transaction_id,
            request_options=request_options,
        )
        return _response.data

    def list_transactions_v21(
        self,
        merchant_code: str,
        *,
        transaction_code: typing.Optional[str] = None,
        order: typing.Optional[ListTransactionsV21RequestOrder] = None,
        limit: typing.Optional[int] = None,
        users: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        statuses: typing.Optional[
            typing.Union[
                ListTransactionsV21RequestStatusesItem, typing.Sequence[ListTransactionsV21RequestStatusesItem]
            ]
        ] = None,
        payment_types: typing.Optional[typing.Union[PaymentType, typing.Sequence[PaymentType]]] = None,
        entry_modes: typing.Optional[typing.Union[EntryMode, typing.Sequence[EntryMode]]] = None,
        types: typing.Optional[
            typing.Union[ListTransactionsV21RequestTypesItem, typing.Sequence[ListTransactionsV21RequestTypesItem]]
        ] = None,
        changes_since: typing.Optional[dt.datetime] = None,
        newest_time: typing.Optional[dt.datetime] = None,
        newest_ref: typing.Optional[str] = None,
        oldest_time: typing.Optional[dt.datetime] = None,
        oldest_ref: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTransactionsV21Response:
        """
        Lists detailed history of all transactions associated with the merchant profile.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        transaction_code : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction code.

        order : typing.Optional[ListTransactionsV21RequestOrder]
            Specifies the order in which the returned results are displayed.

        limit : typing.Optional[int]
            Specifies the maximum number of results per page. Value must be a positive integer and if not specified, will return 10 results.

        users : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filters the returned results by user email.

        statuses : typing.Optional[typing.Union[ListTransactionsV21RequestStatusesItem, typing.Sequence[ListTransactionsV21RequestStatusesItem]]]
            Filters the returned results by the specified list of final statuses of the transactions.

        payment_types : typing.Optional[typing.Union[PaymentType, typing.Sequence[PaymentType]]]
            Filters the returned results by the specified list of payment types used for the transactions.

        entry_modes : typing.Optional[typing.Union[EntryMode, typing.Sequence[EntryMode]]]
            Filters the returned results by the specified list of entry modes.

        types : typing.Optional[typing.Union[ListTransactionsV21RequestTypesItem, typing.Sequence[ListTransactionsV21RequestTypesItem]]]
            Filters the returned results by the specified list of transaction types.

        changes_since : typing.Optional[dt.datetime]
            Filters the results by the latest modification time of resources and returns only transactions that are modified *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        newest_time : typing.Optional[dt.datetime]
            Filters the results by the creation time of resources and returns only transactions that are created *before* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        newest_ref : typing.Optional[str]
            Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *smaller* than the specified value. This parameters supersedes the `newest_time` parameter (if both are provided in the request).

        oldest_time : typing.Optional[dt.datetime]
            Filters the results by the creation time of resources and returns only transactions that are created *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        oldest_ref : typing.Optional[str]
            Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *greater* than the specified value. This parameters supersedes the `oldest_time` parameter (if both are provided in the request).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTransactionsV21Response
            Returns a page of transaction history items.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transactions.list_transactions_v21(
            merchant_code="MH4H92C7",
            transaction_code="TEENSK4W2K",
            limit=10,
            changes_since=datetime.datetime.fromisoformat(
                "2019-08-28 09:00:00+00:00",
            ),
            newest_time=datetime.datetime.fromisoformat(
                "2019-08-29 09:00:00+00:00",
            ),
            newest_ref="090df9bf-93b7-40f1-8181-fbdb236568a1",
            oldest_time=datetime.datetime.fromisoformat(
                "2019-08-28 09:00:00+00:00",
            ),
            oldest_ref="090df9bf-93b7-40f1-8181-fbdb236568a1",
        )
        """
        _response = self._raw_client.list_transactions_v21(
            merchant_code,
            transaction_code=transaction_code,
            order=order,
            limit=limit,
            users=users,
            statuses=statuses,
            payment_types=payment_types,
            entry_modes=entry_modes,
            types=types,
            changes_since=changes_since,
            newest_time=newest_time,
            newest_ref=newest_ref,
            oldest_time=oldest_time,
            oldest_ref=oldest_ref,
            request_options=request_options,
        )
        return _response.data


class AsyncTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransactionsClient
        """
        return self._raw_client

    async def refund_transaction(
        self,
        merchant_code: str,
        transaction_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Refunds an identified transaction either in full or partially.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        transaction_id : str
            Unique identifier of the transaction.

        amount : typing.Optional[float]
            Amount to be refunded. Eligible amount can't exceed the amount of the transaction and varies based on country and currency. If you do not specify a value, the system performs a full refund of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The transaction was refunded in full or partially based on the request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.refund_transaction(
                merchant_code="MH4H92C7",
                transaction_id="4ffb8dfc-7f2b-413d-a497-2ad00766585e",
                amount=5.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refund_transaction(
            merchant_code, transaction_id, amount=amount, request_options=request_options
        )
        return _response.data

    async def get_transaction_v21(
        self,
        merchant_code: str,
        *,
        id: typing.Optional[str] = None,
        transaction_code: typing.Optional[str] = None,
        foreign_transaction_id: typing.Optional[str] = None,
        client_transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransactionFull:
        """
        Retrieves the full details of an identified transaction. The transaction resource is identified by a query parameter and *one* of following parameters is required:
        - `id`
        - `transaction_code`
        - `foreign_transaction_id`
        - `client_transaction_id`

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        id : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction ID (the `id` parameter in the transaction resource).

        transaction_code : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction code.

        foreign_transaction_id : typing.Optional[str]
            External transaction identifier supplied by the client.

        client_transaction_id : typing.Optional[str]
            Client-supplied identifier of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransactionFull
            Returns the requested transaction resource.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.get_transaction_v21(
                merchant_code="MH4H92C7",
                id="410fc44a-5956-44e1-b5cc-19c6f8d727a4",
                transaction_code="TEENSK4W2K",
                foreign_transaction_id="J13253253x1",
                client_transaction_id="urn:sumup:pos:sale:MNKKNGST:1D4E3B2D-111D-48D7-9AF0-832DAEF63DD7;2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_transaction_v21(
            merchant_code,
            id=id,
            transaction_code=transaction_code,
            foreign_transaction_id=foreign_transaction_id,
            client_transaction_id=client_transaction_id,
            request_options=request_options,
        )
        return _response.data

    async def list_transactions_v21(
        self,
        merchant_code: str,
        *,
        transaction_code: typing.Optional[str] = None,
        order: typing.Optional[ListTransactionsV21RequestOrder] = None,
        limit: typing.Optional[int] = None,
        users: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        statuses: typing.Optional[
            typing.Union[
                ListTransactionsV21RequestStatusesItem, typing.Sequence[ListTransactionsV21RequestStatusesItem]
            ]
        ] = None,
        payment_types: typing.Optional[typing.Union[PaymentType, typing.Sequence[PaymentType]]] = None,
        entry_modes: typing.Optional[typing.Union[EntryMode, typing.Sequence[EntryMode]]] = None,
        types: typing.Optional[
            typing.Union[ListTransactionsV21RequestTypesItem, typing.Sequence[ListTransactionsV21RequestTypesItem]]
        ] = None,
        changes_since: typing.Optional[dt.datetime] = None,
        newest_time: typing.Optional[dt.datetime] = None,
        newest_ref: typing.Optional[str] = None,
        oldest_time: typing.Optional[dt.datetime] = None,
        oldest_ref: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTransactionsV21Response:
        """
        Lists detailed history of all transactions associated with the merchant profile.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        transaction_code : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction code.

        order : typing.Optional[ListTransactionsV21RequestOrder]
            Specifies the order in which the returned results are displayed.

        limit : typing.Optional[int]
            Specifies the maximum number of results per page. Value must be a positive integer and if not specified, will return 10 results.

        users : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filters the returned results by user email.

        statuses : typing.Optional[typing.Union[ListTransactionsV21RequestStatusesItem, typing.Sequence[ListTransactionsV21RequestStatusesItem]]]
            Filters the returned results by the specified list of final statuses of the transactions.

        payment_types : typing.Optional[typing.Union[PaymentType, typing.Sequence[PaymentType]]]
            Filters the returned results by the specified list of payment types used for the transactions.

        entry_modes : typing.Optional[typing.Union[EntryMode, typing.Sequence[EntryMode]]]
            Filters the returned results by the specified list of entry modes.

        types : typing.Optional[typing.Union[ListTransactionsV21RequestTypesItem, typing.Sequence[ListTransactionsV21RequestTypesItem]]]
            Filters the returned results by the specified list of transaction types.

        changes_since : typing.Optional[dt.datetime]
            Filters the results by the latest modification time of resources and returns only transactions that are modified *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        newest_time : typing.Optional[dt.datetime]
            Filters the results by the creation time of resources and returns only transactions that are created *before* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        newest_ref : typing.Optional[str]
            Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *smaller* than the specified value. This parameters supersedes the `newest_time` parameter (if both are provided in the request).

        oldest_time : typing.Optional[dt.datetime]
            Filters the results by the creation time of resources and returns only transactions that are created *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        oldest_ref : typing.Optional[str]
            Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *greater* than the specified value. This parameters supersedes the `oldest_time` parameter (if both are provided in the request).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTransactionsV21Response
            Returns a page of transaction history items.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.list_transactions_v21(
                merchant_code="MH4H92C7",
                transaction_code="TEENSK4W2K",
                limit=10,
                changes_since=datetime.datetime.fromisoformat(
                    "2019-08-28 09:00:00+00:00",
                ),
                newest_time=datetime.datetime.fromisoformat(
                    "2019-08-29 09:00:00+00:00",
                ),
                newest_ref="090df9bf-93b7-40f1-8181-fbdb236568a1",
                oldest_time=datetime.datetime.fromisoformat(
                    "2019-08-28 09:00:00+00:00",
                ),
                oldest_ref="090df9bf-93b7-40f1-8181-fbdb236568a1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_transactions_v21(
            merchant_code,
            transaction_code=transaction_code,
            order=order,
            limit=limit,
            users=users,
            statuses=statuses,
            payment_types=payment_types,
            entry_modes=entry_modes,
            types=types,
            changes_since=changes_since,
            newest_time=newest_time,
            newest_ref=newest_ref,
            oldest_time=oldest_time,
            oldest_ref=oldest_ref,
            request_options=request_options,
        )
        return _response.data
