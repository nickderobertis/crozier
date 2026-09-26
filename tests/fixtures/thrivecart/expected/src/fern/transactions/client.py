

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTransactionsClient, RawTransactionsClient
from .types.get_transaction_response import GetTransactionResponse
from .types.list_transactions_response import ListTransactionsResponse
from .types.refund_transaction_response import RefundTransactionResponse


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

    def list_transactions(
        self,
        *,
        product_id: typing.Optional[int] = OMIT,
        email: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        page: typing.Optional[int] = OMIT,
        per_page: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTransactionsResponse:
        """
        Retrieve a list of transactions. Can be filtered by product, customer, or type.

        Parameters
        ----------
        product_id : typing.Optional[int]
            Filter by product ID

        email : typing.Optional[str]
            Filter by customer email

        type : typing.Optional[str]
            Filter by transaction type

        page : typing.Optional[int]

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTransactionsResponse
            List of transactions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transactions.list_transactions()
        """
        _response = self._raw_client.list_transactions(
            product_id=product_id, email=email, type=type, page=page, per_page=per_page, request_options=request_options
        )
        return _response.data

    def get_transaction(
        self, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTransactionResponse:
        """
        Retrieve details of a single transaction.

        Parameters
        ----------
        transaction_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTransactionResponse
            Transaction details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transactions.get_transaction(
            transaction_id="transaction_id",
        )
        """
        _response = self._raw_client.get_transaction(transaction_id, request_options=request_options)
        return _response.data

    def refund_transaction(
        self,
        transaction_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefundTransactionResponse:
        """
        Issue a refund for a specific transaction.

        Parameters
        ----------
        transaction_id : str

        amount : typing.Optional[float]
            Amount to refund. Omit for full refund.

        reason : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefundTransactionResponse
            Refund result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.transactions.refund_transaction(
            transaction_id="transaction_id",
        )
        """
        _response = self._raw_client.refund_transaction(
            transaction_id, amount=amount, reason=reason, request_options=request_options
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

    async def list_transactions(
        self,
        *,
        product_id: typing.Optional[int] = OMIT,
        email: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        page: typing.Optional[int] = OMIT,
        per_page: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTransactionsResponse:
        """
        Retrieve a list of transactions. Can be filtered by product, customer, or type.

        Parameters
        ----------
        product_id : typing.Optional[int]
            Filter by product ID

        email : typing.Optional[str]
            Filter by customer email

        type : typing.Optional[str]
            Filter by transaction type

        page : typing.Optional[int]

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTransactionsResponse
            List of transactions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.list_transactions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_transactions(
            product_id=product_id, email=email, type=type, page=page, per_page=per_page, request_options=request_options
        )
        return _response.data

    async def get_transaction(
        self, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTransactionResponse:
        """
        Retrieve details of a single transaction.

        Parameters
        ----------
        transaction_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTransactionResponse
            Transaction details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.get_transaction(
                transaction_id="transaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_transaction(transaction_id, request_options=request_options)
        return _response.data

    async def refund_transaction(
        self,
        transaction_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefundTransactionResponse:
        """
        Issue a refund for a specific transaction.

        Parameters
        ----------
        transaction_id : str

        amount : typing.Optional[float]
            Amount to refund. Omit for full refund.

        reason : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefundTransactionResponse
            Refund result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.refund_transaction(
                transaction_id="transaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refund_transaction(
            transaction_id, amount=amount, reason=reason, request_options=request_options
        )
        return _response.data
