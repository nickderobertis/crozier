

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.receipt import Receipt
from .raw_client import AsyncRawReceiptsClient, RawReceiptsClient


class ReceiptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReceiptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReceiptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReceiptsClient
        """
        return self._raw_client

    def get_receipt(
        self,
        transaction_id: str,
        *,
        mid: str,
        tx_event_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Receipt:
        """
        Retrieves receipt specific data for a transaction.

        Parameters
        ----------
        transaction_id : str
            SumUp unique transaction ID or transaction code, e.g. TS7HDYLSKD.

        mid : str
            Short unique identifier for the merchant.

        tx_event_id : typing.Optional[int]
            Unique identifier of the transaction event to include on the receipt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            Returns receipt details for the requested transaction.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.receipts.get_receipt(
            transaction_id="410fc44a-5956-44e1-b5cc-19c6f8d727a4",
            mid="MH4H92C7",
            tx_event_id=9567461191,
        )
        """
        _response = self._raw_client.get_receipt(
            transaction_id, mid=mid, tx_event_id=tx_event_id, request_options=request_options
        )
        return _response.data


class AsyncReceiptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReceiptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReceiptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReceiptsClient
        """
        return self._raw_client

    async def get_receipt(
        self,
        transaction_id: str,
        *,
        mid: str,
        tx_event_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Receipt:
        """
        Retrieves receipt specific data for a transaction.

        Parameters
        ----------
        transaction_id : str
            SumUp unique transaction ID or transaction code, e.g. TS7HDYLSKD.

        mid : str
            Short unique identifier for the merchant.

        tx_event_id : typing.Optional[int]
            Unique identifier of the transaction event to include on the receipt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            Returns receipt details for the requested transaction.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.receipts.get_receipt(
                transaction_id="410fc44a-5956-44e1-b5cc-19c6f8d727a4",
                mid="MH4H92C7",
                tx_event_id=9567461191,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_receipt(
            transaction_id, mid=mid, tx_event_id=tx_event_id, request_options=request_options
        )
        return _response.data
