

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.transferwise_quote import TransferwiseQuote
from ..types.transferwise_transfer_create import TransferwiseTransferCreate
from ..types.transferwise_transfer_listing import TransferwiseTransferListing
from ..types.transferwise_transfer_read import TransferwiseTransferRead
from .raw_client import AsyncRawTransferwiseTransferClient, RawTransferwiseTransferClient


OMIT = typing.cast(typing.Any, ...)


class TransferwiseTransferClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransferwiseTransferClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransferwiseTransferClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransferwiseTransferClient
        """
        return self._raw_client

    def list_all_transferwise_transfer_for_user_transferwise_quote(
        self, user_id: int, transferwise_quote_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransferwiseTransferListing]:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransferwiseTransferListing]
            Used to create Transferwise payments.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.transferwise_transfer.list_all_transferwise_transfer_for_user_transferwise_quote(
            user_id=1,
            transferwise_quote_id=1,
        )
        """
        _response = self._raw_client.list_all_transferwise_transfer_for_user_transferwise_quote(
            user_id, transferwise_quote_id, request_options=request_options
        )
        return _response.data

    def create_transferwise_transfer_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        monetary_account_id: str,
        recipient_id: str,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        pay_in_reference: typing.Optional[str] = OMIT,
        quote: typing.Optional[TransferwiseQuote] = OMIT,
        rate: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_transferwise: typing.Optional[str] = OMIT,
        status_transferwise_issue: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        time_delivery_estimate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseTransferCreate:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        monetary_account_id : str
            The id of the monetary account the payment should be made from.

        recipient_id : str
            The id of the target account.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.

        amount_source : typing.Optional[Amount]
            The source amount.

        amount_target : typing.Optional[Amount]
            The target amount.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.

        pay_in_reference : typing.Optional[str]
            The Pay-In reference of the payment.

        quote : typing.Optional[TransferwiseQuote]
            The quote details used to created the payment.

        rate : typing.Optional[str]
            The rate of the payment.

        reference : typing.Optional[str]
            The reference of the payment.

        status : typing.Optional[str]
            The status.

        status_transferwise : typing.Optional[str]
            The status as Transferwise reports it.

        status_transferwise_issue : typing.Optional[str]
            A status to indicatie if Transferwise has an issue with this payment and requires more information.

        sub_status : typing.Optional[str]
            The subStatus.

        time_delivery_estimate : typing.Optional[str]
            The estimated delivery time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseTransferCreate
            Used to create Transferwise payments.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.transferwise_transfer.create_transferwise_transfer_for_user_transferwise_quote(
            user_id=1,
            transferwise_quote_id=1,
            monetary_account_id="monetary_account_id",
            recipient_id="recipient_id",
        )
        """
        _response = self._raw_client.create_transferwise_transfer_for_user_transferwise_quote(
            user_id,
            transferwise_quote_id,
            monetary_account_id=monetary_account_id,
            recipient_id=recipient_id,
            alias=alias,
            amount_source=amount_source,
            amount_target=amount_target,
            counterparty_alias=counterparty_alias,
            pay_in_reference=pay_in_reference,
            quote=quote,
            rate=rate,
            reference=reference,
            status=status,
            status_transferwise=status_transferwise,
            status_transferwise_issue=status_transferwise_issue,
            sub_status=sub_status,
            time_delivery_estimate=time_delivery_estimate,
            request_options=request_options,
        )
        return _response.data

    def read_transferwise_transfer_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseTransferRead:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseTransferRead
            Used to create Transferwise payments.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.transferwise_transfer.read_transferwise_transfer_for_user_transferwise_quote(
            user_id=1,
            transferwise_quote_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_transferwise_transfer_for_user_transferwise_quote(
            user_id, transferwise_quote_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncTransferwiseTransferClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransferwiseTransferClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransferwiseTransferClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransferwiseTransferClient
        """
        return self._raw_client

    async def list_all_transferwise_transfer_for_user_transferwise_quote(
        self, user_id: int, transferwise_quote_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransferwiseTransferListing]:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransferwiseTransferListing]
            Used to create Transferwise payments.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.transferwise_transfer.list_all_transferwise_transfer_for_user_transferwise_quote(
                user_id=1,
                transferwise_quote_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_transferwise_transfer_for_user_transferwise_quote(
            user_id, transferwise_quote_id, request_options=request_options
        )
        return _response.data

    async def create_transferwise_transfer_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        *,
        monetary_account_id: str,
        recipient_id: str,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        pay_in_reference: typing.Optional[str] = OMIT,
        quote: typing.Optional[TransferwiseQuote] = OMIT,
        rate: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_transferwise: typing.Optional[str] = OMIT,
        status_transferwise_issue: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        time_delivery_estimate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseTransferCreate:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        monetary_account_id : str
            The id of the monetary account the payment should be made from.

        recipient_id : str
            The id of the target account.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.

        amount_source : typing.Optional[Amount]
            The source amount.

        amount_target : typing.Optional[Amount]
            The target amount.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.

        pay_in_reference : typing.Optional[str]
            The Pay-In reference of the payment.

        quote : typing.Optional[TransferwiseQuote]
            The quote details used to created the payment.

        rate : typing.Optional[str]
            The rate of the payment.

        reference : typing.Optional[str]
            The reference of the payment.

        status : typing.Optional[str]
            The status.

        status_transferwise : typing.Optional[str]
            The status as Transferwise reports it.

        status_transferwise_issue : typing.Optional[str]
            A status to indicatie if Transferwise has an issue with this payment and requires more information.

        sub_status : typing.Optional[str]
            The subStatus.

        time_delivery_estimate : typing.Optional[str]
            The estimated delivery time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseTransferCreate
            Used to create Transferwise payments.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.transferwise_transfer.create_transferwise_transfer_for_user_transferwise_quote(
                user_id=1,
                transferwise_quote_id=1,
                monetary_account_id="monetary_account_id",
                recipient_id="recipient_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transferwise_transfer_for_user_transferwise_quote(
            user_id,
            transferwise_quote_id,
            monetary_account_id=monetary_account_id,
            recipient_id=recipient_id,
            alias=alias,
            amount_source=amount_source,
            amount_target=amount_target,
            counterparty_alias=counterparty_alias,
            pay_in_reference=pay_in_reference,
            quote=quote,
            rate=rate,
            reference=reference,
            status=status,
            status_transferwise=status_transferwise,
            status_transferwise_issue=status_transferwise_issue,
            sub_status=sub_status,
            time_delivery_estimate=time_delivery_estimate,
            request_options=request_options,
        )
        return _response.data

    async def read_transferwise_transfer_for_user_transferwise_quote(
        self,
        user_id: int,
        transferwise_quote_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseTransferRead:
        """
        Used to create Transferwise payments.

        Parameters
        ----------
        user_id : int


        transferwise_quote_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseTransferRead
            Used to create Transferwise payments.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.transferwise_transfer.read_transferwise_transfer_for_user_transferwise_quote(
                user_id=1,
                transferwise_quote_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_transferwise_transfer_for_user_transferwise_quote(
            user_id, transferwise_quote_id, item_id, request_options=request_options
        )
        return _response.data
