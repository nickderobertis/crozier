

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_legal_name_listing import UserLegalNameListing
from .raw_client import AsyncRawLegalNameClient, RawLegalNameClient


class LegalNameClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLegalNameClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLegalNameClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLegalNameClient
        """
        return self._raw_client

    def list_all_legal_name_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserLegalNameListing]:
        """
        Endpoint for getting available legal names that can be used by the user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserLegalNameListing]
            Endpoint for getting available legal names that can be used by the user.

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
        client.legal_name.list_all_legal_name_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_legal_name_for_user(user_id, request_options=request_options)
        return _response.data


class AsyncLegalNameClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLegalNameClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLegalNameClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLegalNameClient
        """
        return self._raw_client

    async def list_all_legal_name_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserLegalNameListing]:
        """
        Endpoint for getting available legal names that can be used by the user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserLegalNameListing]
            Endpoint for getting available legal names that can be used by the user.

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
            await client.legal_name.list_all_legal_name_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_legal_name_for_user(user_id, request_options=request_options)
        return _response.data
