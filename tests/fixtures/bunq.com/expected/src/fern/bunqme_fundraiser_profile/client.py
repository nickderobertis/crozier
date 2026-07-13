

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bunq_me_fundraiser_profile_user_listing import BunqMeFundraiserProfileUserListing
from ..types.bunq_me_fundraiser_profile_user_read import BunqMeFundraiserProfileUserRead
from .raw_client import AsyncRawBunqmeFundraiserProfileClient, RawBunqmeFundraiserProfileClient


class BunqmeFundraiserProfileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBunqmeFundraiserProfileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBunqmeFundraiserProfileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBunqmeFundraiserProfileClient
        """
        return self._raw_client

    def list_all_bunqme_fundraiser_profile_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BunqMeFundraiserProfileUserListing]:
        """
        bunq.me public profile of the user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BunqMeFundraiserProfileUserListing]
            bunq.me public profile of the user.

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
        client.bunqme_fundraiser_profile.list_all_bunqme_fundraiser_profile_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_bunqme_fundraiser_profile_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    def read_bunqme_fundraiser_profile_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BunqMeFundraiserProfileUserRead:
        """
        bunq.me public profile of the user.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeFundraiserProfileUserRead
            bunq.me public profile of the user.

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
        client.bunqme_fundraiser_profile.read_bunqme_fundraiser_profile_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_bunqme_fundraiser_profile_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncBunqmeFundraiserProfileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBunqmeFundraiserProfileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBunqmeFundraiserProfileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBunqmeFundraiserProfileClient
        """
        return self._raw_client

    async def list_all_bunqme_fundraiser_profile_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BunqMeFundraiserProfileUserListing]:
        """
        bunq.me public profile of the user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BunqMeFundraiserProfileUserListing]
            bunq.me public profile of the user.

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
            await client.bunqme_fundraiser_profile.list_all_bunqme_fundraiser_profile_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_bunqme_fundraiser_profile_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def read_bunqme_fundraiser_profile_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BunqMeFundraiserProfileUserRead:
        """
        bunq.me public profile of the user.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeFundraiserProfileUserRead
            bunq.me public profile of the user.

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
            await client.bunqme_fundraiser_profile.read_bunqme_fundraiser_profile_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_bunqme_fundraiser_profile_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
