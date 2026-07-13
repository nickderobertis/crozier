

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.transferwise_quote_create import TransferwiseQuoteCreate
from ..types.transferwise_quote_read import TransferwiseQuoteRead
from .raw_client import AsyncRawTransferwiseQuoteClient, RawTransferwiseQuoteClient


OMIT = typing.cast(typing.Any, ...)


class TransferwiseQuoteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransferwiseQuoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransferwiseQuoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransferwiseQuoteClient
        """
        return self._raw_client

    def create_transferwise_quote_for_user(
        self,
        user_id: int,
        *,
        currency_source: str,
        currency_target: str,
        amount_fee: typing.Optional[Amount] = OMIT,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        created: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        quote_id: typing.Optional[str] = OMIT,
        rate: typing.Optional[str] = OMIT,
        time_delivery_estimate: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseQuoteCreate:
        """
        Used to get quotes from Transferwise. These can be used to initiate payments.

        Parameters
        ----------
        user_id : int


        currency_source : str
            The source currency.

        currency_target : str
            The target currency.

        amount_fee : typing.Optional[Amount]
            The fee amount.

        amount_source : typing.Optional[Amount]
            The source amount.

        amount_target : typing.Optional[Amount]
            The target amount.

        created : typing.Optional[str]
            The timestamp of the quote's creation.

        id : typing.Optional[int]
            The id of the quote.

        quote_id : typing.Optional[str]
            The quote id Transferwise needs.

        rate : typing.Optional[str]
            The rate.

        time_delivery_estimate : typing.Optional[str]
            The estimated delivery time.

        time_expiry : typing.Optional[str]
            The expiration timestamp of the quote.

        updated : typing.Optional[str]
            The timestamp of the quote's last update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseQuoteCreate
            Used to get quotes from Transferwise. These can be used to initiate payments.

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
        client.transferwise_quote.create_transferwise_quote_for_user(
            user_id=1,
            currency_source="currency_source",
            currency_target="currency_target",
        )
        """
        _response = self._raw_client.create_transferwise_quote_for_user(
            user_id,
            currency_source=currency_source,
            currency_target=currency_target,
            amount_fee=amount_fee,
            amount_source=amount_source,
            amount_target=amount_target,
            created=created,
            id=id,
            quote_id=quote_id,
            rate=rate,
            time_delivery_estimate=time_delivery_estimate,
            time_expiry=time_expiry,
            updated=updated,
            request_options=request_options,
        )
        return _response.data

    def read_transferwise_quote_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransferwiseQuoteRead:
        """
        Used to get quotes from Transferwise. These can be used to initiate payments.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseQuoteRead
            Used to get quotes from Transferwise. These can be used to initiate payments.

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
        client.transferwise_quote.read_transferwise_quote_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_transferwise_quote_for_user(user_id, item_id, request_options=request_options)
        return _response.data


class AsyncTransferwiseQuoteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransferwiseQuoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransferwiseQuoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransferwiseQuoteClient
        """
        return self._raw_client

    async def create_transferwise_quote_for_user(
        self,
        user_id: int,
        *,
        currency_source: str,
        currency_target: str,
        amount_fee: typing.Optional[Amount] = OMIT,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        created: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        quote_id: typing.Optional[str] = OMIT,
        rate: typing.Optional[str] = OMIT,
        time_delivery_estimate: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseQuoteCreate:
        """
        Used to get quotes from Transferwise. These can be used to initiate payments.

        Parameters
        ----------
        user_id : int


        currency_source : str
            The source currency.

        currency_target : str
            The target currency.

        amount_fee : typing.Optional[Amount]
            The fee amount.

        amount_source : typing.Optional[Amount]
            The source amount.

        amount_target : typing.Optional[Amount]
            The target amount.

        created : typing.Optional[str]
            The timestamp of the quote's creation.

        id : typing.Optional[int]
            The id of the quote.

        quote_id : typing.Optional[str]
            The quote id Transferwise needs.

        rate : typing.Optional[str]
            The rate.

        time_delivery_estimate : typing.Optional[str]
            The estimated delivery time.

        time_expiry : typing.Optional[str]
            The expiration timestamp of the quote.

        updated : typing.Optional[str]
            The timestamp of the quote's last update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseQuoteCreate
            Used to get quotes from Transferwise. These can be used to initiate payments.

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
            await client.transferwise_quote.create_transferwise_quote_for_user(
                user_id=1,
                currency_source="currency_source",
                currency_target="currency_target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transferwise_quote_for_user(
            user_id,
            currency_source=currency_source,
            currency_target=currency_target,
            amount_fee=amount_fee,
            amount_source=amount_source,
            amount_target=amount_target,
            created=created,
            id=id,
            quote_id=quote_id,
            rate=rate,
            time_delivery_estimate=time_delivery_estimate,
            time_expiry=time_expiry,
            updated=updated,
            request_options=request_options,
        )
        return _response.data

    async def read_transferwise_quote_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransferwiseQuoteRead:
        """
        Used to get quotes from Transferwise. These can be used to initiate payments.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseQuoteRead
            Used to get quotes from Transferwise. These can be used to initiate payments.

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
            await client.transferwise_quote.read_transferwise_quote_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_transferwise_quote_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
