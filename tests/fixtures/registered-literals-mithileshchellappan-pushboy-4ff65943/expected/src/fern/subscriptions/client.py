

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_topic_subscribers import PaginatedTopicSubscribers
from ..types.user_topic_subscription import UserTopicSubscription
from .raw_client import AsyncRawSubscriptionsClient, RawSubscriptionsClient


class SubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubscriptionsClient
        """
        return self._raw_client

    def subscribe_a_user_to_a_topic(
        self, user_id: str, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserTopicSubscription:
        """
        Parameters
        ----------
        user_id : str

        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserTopicSubscription
            Subscription created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptions.subscribe_a_user_to_a_topic(
            user_id="user-123",
            topic_id="broadcast",
        )
        """
        _response = self._raw_client.subscribe_a_user_to_a_topic(user_id, topic_id, request_options=request_options)
        return _response.data

    def unsubscribe_a_user_from_a_topic(
        self, user_id: str, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        user_id : str

        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptions.unsubscribe_a_user_from_a_topic(
            user_id="user-123",
            topic_id="broadcast",
        )
        """
        _response = self._raw_client.unsubscribe_a_user_from_a_topic(user_id, topic_id, request_options=request_options)
        return _response.data

    def list_a_users_topic_subscriptions(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserTopicSubscription]:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserTopicSubscription]
            Subscriptions for the user. Unknown users currently return an empty list.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptions.list_a_users_topic_subscriptions(
            user_id="user-123",
        )
        """
        _response = self._raw_client.list_a_users_topic_subscriptions(user_id, request_options=request_options)
        return _response.data

    def list_topic_subscribers(
        self,
        topic_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTopicSubscribers:
        """
        Parameters
        ----------
        topic_id : str

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTopicSubscribers
            Current subscribers ordered by subscription time descending.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptions.list_topic_subscribers(
            topic_id="broadcast",
        )
        """
        _response = self._raw_client.list_topic_subscribers(
            topic_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data


class AsyncSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubscriptionsClient
        """
        return self._raw_client

    async def subscribe_a_user_to_a_topic(
        self, user_id: str, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserTopicSubscription:
        """
        Parameters
        ----------
        user_id : str

        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserTopicSubscription
            Subscription created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptions.subscribe_a_user_to_a_topic(
                user_id="user-123",
                topic_id="broadcast",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subscribe_a_user_to_a_topic(
            user_id, topic_id, request_options=request_options
        )
        return _response.data

    async def unsubscribe_a_user_from_a_topic(
        self, user_id: str, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        user_id : str

        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptions.unsubscribe_a_user_from_a_topic(
                user_id="user-123",
                topic_id="broadcast",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unsubscribe_a_user_from_a_topic(
            user_id, topic_id, request_options=request_options
        )
        return _response.data

    async def list_a_users_topic_subscriptions(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserTopicSubscription]:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserTopicSubscription]
            Subscriptions for the user. Unknown users currently return an empty list.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptions.list_a_users_topic_subscriptions(
                user_id="user-123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_a_users_topic_subscriptions(user_id, request_options=request_options)
        return _response.data

    async def list_topic_subscribers(
        self,
        topic_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTopicSubscribers:
        """
        Parameters
        ----------
        topic_id : str

        cursor : typing.Optional[str]
            Opaque URL-safe cursor returned by the previous page.

        limit : typing.Optional[int]
            Page size. Defaults to 50 and must be between 1 and 200.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTopicSubscribers
            Current subscribers ordered by subscription time descending.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptions.list_topic_subscribers(
                topic_id="broadcast",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_topic_subscribers(
            topic_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data
