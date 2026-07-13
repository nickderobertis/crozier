

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.currency_conversion_quote_create import CurrencyConversionQuoteCreate
from ..types.currency_conversion_quote_read import CurrencyConversionQuoteRead
from ..types.currency_conversion_quote_update import CurrencyConversionQuoteUpdate
from ..types.pointer import Pointer
from .raw_client import AsyncRawCurrencyConversionQuoteClient, RawCurrencyConversionQuoteClient


OMIT = typing.cast(typing.Any, ...)


class CurrencyConversionQuoteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCurrencyConversionQuoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCurrencyConversionQuoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCurrencyConversionQuoteClient
        """
        return self._raw_client

    def create_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        amount: Amount,
        counterparty_alias: Pointer,
        currency_source: str,
        currency_target: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyConversionQuoteCreate:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        amount : Amount
            The amount to convert.

        counterparty_alias : Pointer
            The Alias of the party we are transferring the money to.

        currency_source : str
            The currency we are converting.

        currency_target : str
            The currency we are converting towards.

        status : typing.Optional[str]
            The status of the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyConversionQuoteCreate
            Endpoint to create a quote for currency conversions.

        Examples
        --------
        from fern import Amount, FernApi, Pointer

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.currency_conversion_quote.create_currency_conversion_quote_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            amount=Amount(),
            counterparty_alias=Pointer(),
            currency_source="currency_source",
            currency_target="currency_target",
        )
        """
        _response = self._raw_client.create_currency_conversion_quote_for_user_monetary_account(
            user_id,
            monetary_account_id,
            amount=amount,
            counterparty_alias=counterparty_alias,
            currency_source=currency_source,
            currency_target=currency_target,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def read_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyConversionQuoteRead:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyConversionQuoteRead
            Endpoint to create a quote for currency conversions.

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
        client.currency_conversion_quote.read_currency_conversion_quote_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_currency_conversion_quote_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        amount: Amount,
        counterparty_alias: Pointer,
        currency_source: str,
        currency_target: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyConversionQuoteUpdate:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        amount : Amount
            The amount to convert.

        counterparty_alias : Pointer
            The Alias of the party we are transferring the money to.

        currency_source : str
            The currency we are converting.

        currency_target : str
            The currency we are converting towards.

        status : typing.Optional[str]
            The status of the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyConversionQuoteUpdate
            Endpoint to create a quote for currency conversions.

        Examples
        --------
        from fern import Amount, FernApi, Pointer

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.currency_conversion_quote.update_currency_conversion_quote_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
            amount=Amount(),
            counterparty_alias=Pointer(),
            currency_source="currency_source",
            currency_target="currency_target",
        )
        """
        _response = self._raw_client.update_currency_conversion_quote_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            amount=amount,
            counterparty_alias=counterparty_alias,
            currency_source=currency_source,
            currency_target=currency_target,
            status=status,
            request_options=request_options,
        )
        return _response.data


class AsyncCurrencyConversionQuoteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCurrencyConversionQuoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCurrencyConversionQuoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCurrencyConversionQuoteClient
        """
        return self._raw_client

    async def create_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        amount: Amount,
        counterparty_alias: Pointer,
        currency_source: str,
        currency_target: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyConversionQuoteCreate:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        amount : Amount
            The amount to convert.

        counterparty_alias : Pointer
            The Alias of the party we are transferring the money to.

        currency_source : str
            The currency we are converting.

        currency_target : str
            The currency we are converting towards.

        status : typing.Optional[str]
            The status of the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyConversionQuoteCreate
            Endpoint to create a quote for currency conversions.

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi, Pointer

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.currency_conversion_quote.create_currency_conversion_quote_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                amount=Amount(),
                counterparty_alias=Pointer(),
                currency_source="currency_source",
                currency_target="currency_target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_currency_conversion_quote_for_user_monetary_account(
            user_id,
            monetary_account_id,
            amount=amount,
            counterparty_alias=counterparty_alias,
            currency_source=currency_source,
            currency_target=currency_target,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def read_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyConversionQuoteRead:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyConversionQuoteRead
            Endpoint to create a quote for currency conversions.

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
            await client.currency_conversion_quote.read_currency_conversion_quote_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_currency_conversion_quote_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_currency_conversion_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        amount: Amount,
        counterparty_alias: Pointer,
        currency_source: str,
        currency_target: str,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyConversionQuoteUpdate:
        """
        Endpoint to create a quote for currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        amount : Amount
            The amount to convert.

        counterparty_alias : Pointer
            The Alias of the party we are transferring the money to.

        currency_source : str
            The currency we are converting.

        currency_target : str
            The currency we are converting towards.

        status : typing.Optional[str]
            The status of the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyConversionQuoteUpdate
            Endpoint to create a quote for currency conversions.

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi, Pointer

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.currency_conversion_quote.update_currency_conversion_quote_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
                amount=Amount(),
                counterparty_alias=Pointer(),
                currency_source="currency_source",
                currency_target="currency_target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_currency_conversion_quote_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            amount=amount,
            counterparty_alias=counterparty_alias,
            currency_source=currency_source,
            currency_target=currency_target,
            status=status,
            request_options=request_options,
        )
        return _response.data
