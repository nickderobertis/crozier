

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_payment_service_provider_read import UserPaymentServiceProviderRead
from .raw_client import AsyncRawUserPaymentServiceProviderClient, RawUserPaymentServiceProviderClient


class UserPaymentServiceProviderClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserPaymentServiceProviderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserPaymentServiceProviderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserPaymentServiceProviderClient
        """
        return self._raw_client

    def read_user_payment_service_provider(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserPaymentServiceProviderRead:
        """
        Used to view UserPaymentServiceProvider for session creation.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPaymentServiceProviderRead
            Used to view UserPaymentServiceProvider for session creation.

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
        client.user_payment_service_provider.read_user_payment_service_provider(
            item_id=1,
        )
        """
        _response = self._raw_client.read_user_payment_service_provider(item_id, request_options=request_options)
        return _response.data


class AsyncUserPaymentServiceProviderClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserPaymentServiceProviderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserPaymentServiceProviderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserPaymentServiceProviderClient
        """
        return self._raw_client

    async def read_user_payment_service_provider(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserPaymentServiceProviderRead:
        """
        Used to view UserPaymentServiceProvider for session creation.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPaymentServiceProviderRead
            Used to view UserPaymentServiceProvider for session creation.

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
            await client.user_payment_service_provider.read_user_payment_service_provider(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_user_payment_service_provider(item_id, request_options=request_options)
        return _response.data
