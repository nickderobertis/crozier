

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.customer_limit_listing import CustomerLimitListing
from .raw_client import AsyncRawLimitClient, RawLimitClient


class LimitClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLimitClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLimitClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLimitClient
        """
        return self._raw_client

    def list_all_limit_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CustomerLimitListing]:
        """
        Get all limits for the authenticated user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CustomerLimitListing]
            Show the limits for the authenticated user.

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
        client.limit.list_all_limit_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_limit_for_user(user_id, request_options=request_options)
        return _response.data


class AsyncLimitClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLimitClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLimitClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLimitClient
        """
        return self._raw_client

    async def list_all_limit_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CustomerLimitListing]:
        """
        Get all limits for the authenticated user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CustomerLimitListing]
            Show the limits for the authenticated user.

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
            await client.limit.list_all_limit_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_limit_for_user(user_id, request_options=request_options)
        return _response.data
