

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.transferwise_user_create import TransferwiseUserCreate
from ..types.transferwise_user_listing import TransferwiseUserListing
from .raw_client import AsyncRawTransferwiseUserClient, RawTransferwiseUserClient


OMIT = typing.cast(typing.Any, ...)


class TransferwiseUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransferwiseUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransferwiseUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransferwiseUserClient
        """
        return self._raw_client

    def list_all_transferwise_user_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransferwiseUserListing]:
        """
        Used to manage Transferwise users.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransferwiseUserListing]
            Used to manage Transferwise users.

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
        client.transferwise_user.list_all_transferwise_user_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_transferwise_user_for_user(user_id, request_options=request_options)
        return _response.data

    def create_transferwise_user_for_user(
        self,
        user_id: int,
        *,
        oauth_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseUserCreate:
        """
        Used to manage Transferwise users.

        Parameters
        ----------
        user_id : int


        oauth_code : typing.Optional[str]
            The OAuth code returned by Transferwise we should be using to gain access to the user's Transferwise account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseUserCreate
            Used to manage Transferwise users.

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
        client.transferwise_user.create_transferwise_user_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.create_transferwise_user_for_user(
            user_id, oauth_code=oauth_code, request_options=request_options
        )
        return _response.data


class AsyncTransferwiseUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransferwiseUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransferwiseUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransferwiseUserClient
        """
        return self._raw_client

    async def list_all_transferwise_user_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransferwiseUserListing]:
        """
        Used to manage Transferwise users.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransferwiseUserListing]
            Used to manage Transferwise users.

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
            await client.transferwise_user.list_all_transferwise_user_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_transferwise_user_for_user(user_id, request_options=request_options)
        return _response.data

    async def create_transferwise_user_for_user(
        self,
        user_id: int,
        *,
        oauth_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseUserCreate:
        """
        Used to manage Transferwise users.

        Parameters
        ----------
        user_id : int


        oauth_code : typing.Optional[str]
            The OAuth code returned by Transferwise we should be using to gain access to the user's Transferwise account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseUserCreate
            Used to manage Transferwise users.

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
            await client.transferwise_user.create_transferwise_user_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transferwise_user_for_user(
            user_id, oauth_code=oauth_code, request_options=request_options
        )
        return _response.data
