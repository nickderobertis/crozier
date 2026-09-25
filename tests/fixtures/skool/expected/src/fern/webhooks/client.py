

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.webhook import Webhook
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.create_webhook_request_events_item import CreateWebhookRequestEventsItem


OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebhooksClient
        """
        return self._raw_client

    def list_webhooks(
        self, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Webhook]:
        """
        Retrieve all configured webhooks.

        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Webhook]
            List of webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.list_webhooks(
            session_id="session_id",
        )
        """
        _response = self._raw_client.list_webhooks(session_id=session_id, request_options=request_options)
        return _response.data

    def create_webhook(
        self,
        *,
        session_id: str,
        url: str,
        group: str,
        events: typing.Sequence[CreateWebhookRequestEventsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Create a new webhook to receive real-time notifications for events in your Skool communities.

        Parameters
        ----------
        session_id : str

        url : str
            The URL to receive webhook notifications

        group : str
            The group slug to monitor

        events : typing.Sequence[CreateWebhookRequestEventsItem]
            Events to subscribe to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Webhook created

        Examples
        --------
        from fern.webhooks import CreateWebhookRequestEventsItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.create_webhook(
            session_id="session_id",
            url="url",
            group="group",
            events=[CreateWebhookRequestEventsItem.POST],
        )
        """
        _response = self._raw_client.create_webhook(
            session_id=session_id, url=url, group=group, events=events, request_options=request_options
        )
        return _response.data

    def delete_webhook(
        self, webhook_id: str, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a configured webhook.

        Parameters
        ----------
        webhook_id : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.delete_webhook(
            webhook_id="webhook_id",
            session_id="session_id",
        )
        """
        _response = self._raw_client.delete_webhook(webhook_id, session_id=session_id, request_options=request_options)
        return _response.data


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebhooksClient
        """
        return self._raw_client

    async def list_webhooks(
        self, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Webhook]:
        """
        Retrieve all configured webhooks.

        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Webhook]
            List of webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.list_webhooks(
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_webhooks(session_id=session_id, request_options=request_options)
        return _response.data

    async def create_webhook(
        self,
        *,
        session_id: str,
        url: str,
        group: str,
        events: typing.Sequence[CreateWebhookRequestEventsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Create a new webhook to receive real-time notifications for events in your Skool communities.

        Parameters
        ----------
        session_id : str

        url : str
            The URL to receive webhook notifications

        group : str
            The group slug to monitor

        events : typing.Sequence[CreateWebhookRequestEventsItem]
            Events to subscribe to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Webhook created

        Examples
        --------
        import asyncio

        from fern.webhooks import CreateWebhookRequestEventsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.create_webhook(
                session_id="session_id",
                url="url",
                group="group",
                events=[CreateWebhookRequestEventsItem.POST],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook(
            session_id=session_id, url=url, group=group, events=events, request_options=request_options
        )
        return _response.data

    async def delete_webhook(
        self, webhook_id: str, *, session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a configured webhook.

        Parameters
        ----------
        webhook_id : str

        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.delete_webhook(
                webhook_id="webhook_id",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhook(
            webhook_id, session_id=session_id, request_options=request_options
        )
        return _response.data
