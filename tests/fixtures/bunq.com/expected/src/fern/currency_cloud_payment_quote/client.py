

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.currency_cloud_payment_quote_create import CurrencyCloudPaymentQuoteCreate
from ..types.pointer import Pointer
from .raw_client import AsyncRawCurrencyCloudPaymentQuoteClient, RawCurrencyCloudPaymentQuoteClient


OMIT = typing.cast(typing.Any, ...)


class CurrencyCloudPaymentQuoteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCurrencyCloudPaymentQuoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCurrencyCloudPaymentQuoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCurrencyCloudPaymentQuoteClient
        """
        return self._raw_client

    def create_currency_cloud_payment_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        pointers: typing.Sequence[Pointer],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyCloudPaymentQuoteCreate:
        """
        Endpoint for managing currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        pointers : typing.Sequence[Pointer]
            The points we want to know the fees for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyCloudPaymentQuoteCreate
            Endpoint for managing currency conversions.

        Examples
        --------
        from fern import FernApi, Pointer

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.currency_cloud_payment_quote.create_currency_cloud_payment_quote_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            pointers=[Pointer()],
        )
        """
        _response = self._raw_client.create_currency_cloud_payment_quote_for_user_monetary_account(
            user_id, monetary_account_id, pointers=pointers, request_options=request_options
        )
        return _response.data


class AsyncCurrencyCloudPaymentQuoteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCurrencyCloudPaymentQuoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCurrencyCloudPaymentQuoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCurrencyCloudPaymentQuoteClient
        """
        return self._raw_client

    async def create_currency_cloud_payment_quote_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        pointers: typing.Sequence[Pointer],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrencyCloudPaymentQuoteCreate:
        """
        Endpoint for managing currency conversions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        pointers : typing.Sequence[Pointer]
            The points we want to know the fees for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrencyCloudPaymentQuoteCreate
            Endpoint for managing currency conversions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Pointer

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.currency_cloud_payment_quote.create_currency_cloud_payment_quote_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                pointers=[Pointer()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_currency_cloud_payment_quote_for_user_monetary_account(
            user_id, monetary_account_id, pointers=pointers, request_options=request_options
        )
        return _response.data
