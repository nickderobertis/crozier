

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.transferwise_currency_listing import TransferwiseCurrencyListing
from .raw_client import AsyncRawTransferwiseCurrencyClient, RawTransferwiseCurrencyClient


class TransferwiseCurrencyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransferwiseCurrencyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransferwiseCurrencyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransferwiseCurrencyClient
        """
        return self._raw_client

    def list_all_transferwise_currency_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransferwiseCurrencyListing]:
        """
        Used to get a list of supported currencies for Transferwise.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransferwiseCurrencyListing]
            Used to get a list of supported currencies for Transferwise.

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
        client.transferwise_currency.list_all_transferwise_currency_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_transferwise_currency_for_user(user_id, request_options=request_options)
        return _response.data


class AsyncTransferwiseCurrencyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransferwiseCurrencyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransferwiseCurrencyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransferwiseCurrencyClient
        """
        return self._raw_client

    async def list_all_transferwise_currency_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransferwiseCurrencyListing]:
        """
        Used to get a list of supported currencies for Transferwise.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransferwiseCurrencyListing]
            Used to get a list of supported currencies for Transferwise.

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
            await client.transferwise_currency.list_all_transferwise_currency_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_transferwise_currency_for_user(
            user_id, request_options=request_options
        )
        return _response.data
