

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.token_qr_request_sofort_create import TokenQrRequestSofortCreate
from .raw_client import AsyncRawTokenQrRequestSofortClient, RawTokenQrRequestSofortClient


OMIT = typing.cast(typing.Any, ...)


class TokenQrRequestSofortClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokenQrRequestSofortClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokenQrRequestSofortClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokenQrRequestSofortClient
        """
        return self._raw_client

    def create_token_qr_request_sofort_for_user(
        self, user_id: int, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenQrRequestSofortCreate:
        """
        Create a request from an SOFORT transaction.

        Parameters
        ----------
        user_id : int


        token : str
            The token passed from a site or read from a QR code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenQrRequestSofortCreate
            Using this call you can create a SOFORT Request assigned to your User by providing the Token of the request.

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
        client.token_qr_request_sofort.create_token_qr_request_sofort_for_user(
            user_id=1,
            token="token",
        )
        """
        _response = self._raw_client.create_token_qr_request_sofort_for_user(
            user_id, token=token, request_options=request_options
        )
        return _response.data


class AsyncTokenQrRequestSofortClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokenQrRequestSofortClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokenQrRequestSofortClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokenQrRequestSofortClient
        """
        return self._raw_client

    async def create_token_qr_request_sofort_for_user(
        self, user_id: int, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenQrRequestSofortCreate:
        """
        Create a request from an SOFORT transaction.

        Parameters
        ----------
        user_id : int


        token : str
            The token passed from a site or read from a QR code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenQrRequestSofortCreate
            Using this call you can create a SOFORT Request assigned to your User by providing the Token of the request.

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
            await client.token_qr_request_sofort.create_token_qr_request_sofort_for_user(
                user_id=1,
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_token_qr_request_sofort_for_user(
            user_id, token=token, request_options=request_options
        )
        return _response.data
