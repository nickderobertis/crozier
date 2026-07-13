

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.reward_recipient_listing import RewardRecipientListing
from ..types.reward_recipient_read import RewardRecipientRead
from .raw_client import AsyncRawRewardRecipientClient, RawRewardRecipientClient


class RewardRecipientClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRewardRecipientClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRewardRecipientClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRewardRecipientClient
        """
        return self._raw_client

    def list_all_reward_recipient_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RewardRecipientListing]:
        """
        Used to view Rewards.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RewardRecipientListing]
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
        client.reward_recipient.list_all_reward_recipient_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_reward_recipient_for_user(user_id, request_options=request_options)
        return _response.data

    def read_reward_recipient_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RewardRecipientRead:
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
        RewardRecipientRead
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
        client.reward_recipient.read_reward_recipient_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_reward_recipient_for_user(user_id, item_id, request_options=request_options)
        return _response.data


class AsyncRewardRecipientClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRewardRecipientClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRewardRecipientClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRewardRecipientClient
        """
        return self._raw_client

    async def list_all_reward_recipient_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RewardRecipientListing]:
        """
        Used to view Rewards.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RewardRecipientListing]
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
            await client.reward_recipient.list_all_reward_recipient_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_reward_recipient_for_user(user_id, request_options=request_options)
        return _response.data

    async def read_reward_recipient_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RewardRecipientRead:
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
        RewardRecipientRead
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
            await client.reward_recipient.read_reward_recipient_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_reward_recipient_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
