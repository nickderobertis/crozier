

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_subscribers_subscription_get_subscribers_get_request_limit import (
    GetSubscribersSubscriptionGetSubscribersGetRequestLimit,
)
from ..types.get_subscribers_subscription_get_subscribers_get_request_offset import (
    GetSubscribersSubscriptionGetSubscribersGetRequestOffset,
)
from ..types.get_subscriptions_order import GetSubscriptionsOrder
from ..types.get_subscriptions_subscription_get_subscriptions_get_request_limit import (
    GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit,
)
from ..types.get_subscriptions_subscription_get_subscriptions_get_request_offset import (
    GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset,
)
from ..types.subscribe_response import SubscribeResponse
from ..types.subscribers_response import SubscribersResponse
from ..types.subscriptions_response import SubscriptionsResponse
from ..types.unsubscribe_response import UnsubscribeResponse
from .raw_client import AsyncRawSubscriptionClient, RawSubscriptionClient


OMIT = typing.cast(typing.Any, ...)


class SubscriptionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubscriptionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubscriptionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubscriptionClient
        """
        return self._raw_client

    def subscribe(
        self, *, authorization: str, subscription_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscribeResponse:
        """
        Оформление подписки

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        subscription_id : int
            Айди на кого подписка

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscription.subscribe(
            authorization="Authorization",
            subscription_id=1,
        )
        """
        _response = self._raw_client.subscribe(
            authorization=authorization, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    def unsubscribe(
        self, *, authorization: str, subscription_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> UnsubscribeResponse:
        """
        Отписка от пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        subscription_id : int
            Айди от кого отписка

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnsubscribeResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscription.unsubscribe(
            authorization="Authorization",
            subscription_id=1,
        )
        """
        _response = self._raw_client.unsubscribe(
            authorization=authorization, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    def get_subscriptions(
        self,
        *,
        user_id: int,
        offset: typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset] = None,
        limit: typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit] = None,
        order: typing.Optional[GetSubscriptionsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionsResponse:
        """
        Получение подписчиков пользователя

        Parameters
        ----------
        user_id : int

        offset : typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset]

        limit : typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit]

        order : typing.Optional[GetSubscriptionsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscription.get_subscriptions(
            user_id=1,
        )
        """
        _response = self._raw_client.get_subscriptions(
            user_id=user_id, offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def get_subscribers(
        self,
        *,
        user_id: int,
        offset: typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestOffset] = None,
        limit: typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestLimit] = None,
        order: typing.Optional[GetSubscriptionsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribersResponse:
        """
        Получение подписчиков пользователя

        Parameters
        ----------
        user_id : int

        offset : typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestOffset]

        limit : typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestLimit]

        order : typing.Optional[GetSubscriptionsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscription.get_subscribers(
            user_id=1,
        )
        """
        _response = self._raw_client.get_subscribers(
            user_id=user_id, offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data


class AsyncSubscriptionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubscriptionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubscriptionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubscriptionClient
        """
        return self._raw_client

    async def subscribe(
        self, *, authorization: str, subscription_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscribeResponse:
        """
        Оформление подписки

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        subscription_id : int
            Айди на кого подписка

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscription.subscribe(
                authorization="Authorization",
                subscription_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subscribe(
            authorization=authorization, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    async def unsubscribe(
        self, *, authorization: str, subscription_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> UnsubscribeResponse:
        """
        Отписка от пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        subscription_id : int
            Айди от кого отписка

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnsubscribeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscription.unsubscribe(
                authorization="Authorization",
                subscription_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unsubscribe(
            authorization=authorization, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    async def get_subscriptions(
        self,
        *,
        user_id: int,
        offset: typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset] = None,
        limit: typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit] = None,
        order: typing.Optional[GetSubscriptionsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionsResponse:
        """
        Получение подписчиков пользователя

        Parameters
        ----------
        user_id : int

        offset : typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset]

        limit : typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit]

        order : typing.Optional[GetSubscriptionsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscription.get_subscriptions(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subscriptions(
            user_id=user_id, offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def get_subscribers(
        self,
        *,
        user_id: int,
        offset: typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestOffset] = None,
        limit: typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestLimit] = None,
        order: typing.Optional[GetSubscriptionsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribersResponse:
        """
        Получение подписчиков пользователя

        Parameters
        ----------
        user_id : int

        offset : typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestOffset]

        limit : typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestLimit]

        order : typing.Optional[GetSubscriptionsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribersResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscription.get_subscribers(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subscribers(
            user_id=user_id, offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data
