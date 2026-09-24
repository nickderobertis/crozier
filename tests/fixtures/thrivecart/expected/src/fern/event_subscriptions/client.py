

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEventSubscriptionsClient, RawEventSubscriptionsClient
from .types.create_event_subscription_request_event import CreateEventSubscriptionRequestEvent
from .types.create_event_subscription_response import CreateEventSubscriptionResponse
from .types.delete_event_subscription_response import DeleteEventSubscriptionResponse


OMIT = typing.cast(typing.Any, ...)


class EventSubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventSubscriptionsClient
        """
        return self._raw_client

    def create_event_subscription(
        self,
        *,
        event: CreateEventSubscriptionRequestEvent,
        target_url: str,
        product_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateEventSubscriptionResponse:
        """
        Create a webhook-style event subscription. Unlike standard webhooks, event subscriptions always receive JSON and can target specific events.

        Parameters
        ----------
        event : CreateEventSubscriptionRequestEvent
            Event type to subscribe to. Use '*' for all events.

        target_url : str
            URL to receive the event notifications

        product_id : typing.Optional[int]
            Optional: limit to a specific product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateEventSubscriptionResponse
            Subscription created

        Examples
        --------
        from fern.event_subscriptions import CreateEventSubscriptionRequestEvent

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_subscriptions.create_event_subscription(
            event=CreateEventSubscriptionRequestEvent.ALL,
            target_url="target_url",
        )
        """
        _response = self._raw_client.create_event_subscription(
            event=event, target_url=target_url, product_id=product_id, request_options=request_options
        )
        return _response.data

    def delete_event_subscription(
        self, *, subscription_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteEventSubscriptionResponse:
        """
        Remove an existing event subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteEventSubscriptionResponse
            Subscription removed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_subscriptions.delete_event_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.delete_event_subscription(
            subscription_id=subscription_id, request_options=request_options
        )
        return _response.data


class AsyncEventSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventSubscriptionsClient
        """
        return self._raw_client

    async def create_event_subscription(
        self,
        *,
        event: CreateEventSubscriptionRequestEvent,
        target_url: str,
        product_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateEventSubscriptionResponse:
        """
        Create a webhook-style event subscription. Unlike standard webhooks, event subscriptions always receive JSON and can target specific events.

        Parameters
        ----------
        event : CreateEventSubscriptionRequestEvent
            Event type to subscribe to. Use '*' for all events.

        target_url : str
            URL to receive the event notifications

        product_id : typing.Optional[int]
            Optional: limit to a specific product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateEventSubscriptionResponse
            Subscription created

        Examples
        --------
        import asyncio

        from fern.event_subscriptions import CreateEventSubscriptionRequestEvent

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_subscriptions.create_event_subscription(
                event=CreateEventSubscriptionRequestEvent.ALL,
                target_url="target_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_event_subscription(
            event=event, target_url=target_url, product_id=product_id, request_options=request_options
        )
        return _response.data

    async def delete_event_subscription(
        self, *, subscription_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteEventSubscriptionResponse:
        """
        Remove an existing event subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteEventSubscriptionResponse
            Subscription removed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_subscriptions.delete_event_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_event_subscription(
            subscription_id=subscription_id, request_options=request_options
        )
        return _response.data
