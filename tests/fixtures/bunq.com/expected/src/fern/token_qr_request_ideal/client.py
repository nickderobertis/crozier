

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.token_qr_request_ideal_create import TokenQrRequestIdealCreate
from .raw_client import AsyncRawTokenQrRequestIdealClient, RawTokenQrRequestIdealClient


OMIT = typing.cast(typing.Any, ...)


class TokenQrRequestIdealClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokenQrRequestIdealClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokenQrRequestIdealClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokenQrRequestIdealClient
        """
        return self._raw_client

    def create_token_qr_request_ideal_for_user(
        self, user_id: int, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenQrRequestIdealCreate:
        """
        Create a request from an ideal transaction.

        Parameters
        ----------
        user_id : int


        token : str
            The token passed from a site or read from a QR code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenQrRequestIdealCreate
            Using this call you create a request for payment from an external token provided with an ideal transaction. Make sure your iDEAL payments are compliant with the iDEAL standards, by following the following manual: https:/www.bunq.com/terms-idealstandards. It's very important to keep these points in mind when you are using the endpoint to make iDEAL payments from your application.

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
        client.token_qr_request_ideal.create_token_qr_request_ideal_for_user(
            user_id=1,
            token="token",
        )
        """
        _response = self._raw_client.create_token_qr_request_ideal_for_user(
            user_id, token=token, request_options=request_options
        )
        return _response.data


class AsyncTokenQrRequestIdealClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokenQrRequestIdealClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokenQrRequestIdealClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokenQrRequestIdealClient
        """
        return self._raw_client

    async def create_token_qr_request_ideal_for_user(
        self, user_id: int, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenQrRequestIdealCreate:
        """
        Create a request from an ideal transaction.

        Parameters
        ----------
        user_id : int


        token : str
            The token passed from a site or read from a QR code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenQrRequestIdealCreate
            Using this call you create a request for payment from an external token provided with an ideal transaction. Make sure your iDEAL payments are compliant with the iDEAL standards, by following the following manual: https:/www.bunq.com/terms-idealstandards. It's very important to keep these points in mind when you are using the endpoint to make iDEAL payments from your application.

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
            await client.token_qr_request_ideal.create_token_qr_request_ideal_for_user(
                user_id=1,
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_token_qr_request_ideal_for_user(
            user_id, token=token, request_options=request_options
        )
        return _response.data
