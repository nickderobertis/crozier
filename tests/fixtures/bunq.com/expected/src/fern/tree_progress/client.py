

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tree_progress_listing import TreeProgressListing
from .raw_client import AsyncRawTreeProgressClient, RawTreeProgressClient


class TreeProgressClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTreeProgressClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTreeProgressClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTreeProgressClient
        """
        return self._raw_client

    def list_all_tree_progress_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TreeProgressListing]:
        """
        See how many trees this user has planted.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TreeProgressListing]
            See how many trees this user has planted.

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
        client.tree_progress.list_all_tree_progress_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_tree_progress_for_user(user_id, request_options=request_options)
        return _response.data


class AsyncTreeProgressClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTreeProgressClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTreeProgressClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTreeProgressClient
        """
        return self._raw_client

    async def list_all_tree_progress_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TreeProgressListing]:
        """
        See how many trees this user has planted.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TreeProgressListing]
            See how many trees this user has planted.

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
            await client.tree_progress.list_all_tree_progress_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_tree_progress_for_user(user_id, request_options=request_options)
        return _response.data
