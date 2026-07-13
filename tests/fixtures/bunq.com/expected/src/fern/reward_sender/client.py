

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.reward_sender_listing import RewardSenderListing
from ..types.reward_sender_read import RewardSenderRead
from .raw_client import AsyncRawRewardSenderClient, RawRewardSenderClient


class RewardSenderClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRewardSenderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRewardSenderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRewardSenderClient
        """
        return self._raw_client

    def list_all_reward_sender_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RewardSenderListing]:
        """
        Used to view Rewards.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RewardSenderListing]
            Used to view Rewards.

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
        client.reward_sender.list_all_reward_sender_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_reward_sender_for_user(user_id, request_options=request_options)
        return _response.data

    def read_reward_sender_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RewardSenderRead:
        """
        Used to view Rewards.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RewardSenderRead
            Used to view Rewards.

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
        client.reward_sender.read_reward_sender_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_reward_sender_for_user(user_id, item_id, request_options=request_options)
        return _response.data


class AsyncRewardSenderClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRewardSenderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRewardSenderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRewardSenderClient
        """
        return self._raw_client

    async def list_all_reward_sender_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RewardSenderListing]:
        """
        Used to view Rewards.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RewardSenderListing]
            Used to view Rewards.

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
            await client.reward_sender.list_all_reward_sender_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_reward_sender_for_user(user_id, request_options=request_options)
        return _response.data

    async def read_reward_sender_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RewardSenderRead:
        """
        Used to view Rewards.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RewardSenderRead
            Used to view Rewards.

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
            await client.reward_sender.read_reward_sender_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_reward_sender_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
