

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_listing import UserListing
from ..types.user_read import UserRead
from .raw_client import AsyncRawUserClient, RawUserClient


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserClient
        """
        return self._raw_client

    def list_all_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[UserListing]:
        """
        Get a collection of all available users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserListing]
            Using this call you can retrieve information of the user you are logged in as. This includes your user id, which is referred to in endpoints.

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
        client.user.list_all_user()
        """
        _response = self._raw_client.list_all_user(request_options=request_options)
        return _response.data

    def read_user(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> UserRead:
        """
        Get a specific user.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRead
            Using this call you can retrieve information of the user you are logged in as. This includes your user id, which is referred to in endpoints.

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
        client.user.read_user(
            item_id=1,
        )
        """
        _response = self._raw_client.read_user(item_id, request_options=request_options)
        return _response.data


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserClient
        """
        return self._raw_client

    async def list_all_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserListing]:
        """
        Get a collection of all available users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserListing]
            Using this call you can retrieve information of the user you are logged in as. This includes your user id, which is referred to in endpoints.

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
            await client.user.list_all_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_user(request_options=request_options)
        return _response.data

    async def read_user(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> UserRead:
        """
        Get a specific user.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRead
            Using this call you can retrieve information of the user you are logged in as. This includes your user id, which is referred to in endpoints.

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
            await client.user.read_user(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_user(item_id, request_options=request_options)
        return _response.data
