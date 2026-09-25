

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_type import EventType
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.create_webhook_request_http_headers_item import CreateWebhookRequestHttpHeadersItem
from .types.create_webhook_response import CreateWebhookResponse
from .types.list_webhook_events_response import ListWebhookEventsResponse
from .types.list_webhooks_response import ListWebhooksResponse
from .types.update_webhook_request_http_headers_item import UpdateWebhookRequestHttpHeadersItem


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
        self,
        *,
        page: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWebhooksResponse:
        """
        Returns a paginated list of all webhooks across your accessible forms and workspaces.

        Parameters
        ----------
        page : typing.Optional[float]
            Page number for pagination (default: 1)

        limit : typing.Optional[float]
            Number of webhooks per page (default: 25, max: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhooksResponse
            List of webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.list_webhooks()
        """
        _response = self._raw_client.list_webhooks(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create_webhook(
        self,
        *,
        form_id: str,
        url: str,
        event_types: typing.Sequence[EventType],
        signing_secret: typing.Optional[str] = OMIT,
        http_headers: typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]] = OMIT,
        external_subscriber: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhookResponse:
        """
        Creates a new webhook for a form to receive form events.

        Parameters
        ----------
        form_id : str
            The ID of the form to create the webhook for

        url : str
            The URL to send webhook events to

        event_types : typing.Sequence[EventType]
            Types of events to receive

        signing_secret : typing.Optional[str]
            Optional secret used to sign webhook payloads

        http_headers : typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]]
            Optional custom HTTP headers to include in webhook requests

        external_subscriber : typing.Optional[str]
            Optional identifier for the external subscriber

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhookResponse
            Webhook created successfully

        Examples
        --------
        from fern import EventType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.create_webhook(
            form_id="formId",
            url="url",
            event_types=[EventType.FORM_RESPONSE],
        )
        """
        _response = self._raw_client.create_webhook(
            form_id=form_id,
            url=url,
            event_types=event_types,
            signing_secret=signing_secret,
            http_headers=http_headers,
            external_subscriber=external_subscriber,
            request_options=request_options,
        )
        return _response.data

    def delete_webhook(self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a webhook. If this is the last webhook for a form, the webhooks integration will also be marked as deleted.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.delete_webhook(
            webhook_id="webhookId",
        )
        """
        _response = self._raw_client.delete_webhook(webhook_id, request_options=request_options)
        return _response.data

    def update_webhook(
        self,
        webhook_id: str,
        *,
        form_id: str,
        url: str,
        event_types: typing.Sequence[EventType],
        is_enabled: bool,
        signing_secret: typing.Optional[str] = OMIT,
        http_headers: typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an existing webhook configuration.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook to update

        form_id : str
            The ID of the form the webhook is for

        url : str
            The URL to send webhook events to

        event_types : typing.Sequence[EventType]
            Types of events to receive

        is_enabled : bool
            Whether the webhook is enabled

        signing_secret : typing.Optional[str]
            Optional secret used to sign webhook payloads

        http_headers : typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]]
            Optional custom HTTP headers to include in webhook requests

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import EventType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.update_webhook(
            webhook_id="webhookId",
            form_id="formId",
            url="url",
            event_types=[EventType.FORM_RESPONSE],
            is_enabled=True,
        )
        """
        _response = self._raw_client.update_webhook(
            webhook_id,
            form_id=form_id,
            url=url,
            event_types=event_types,
            is_enabled=is_enabled,
            signing_secret=signing_secret,
            http_headers=http_headers,
            request_options=request_options,
        )
        return _response.data

    def list_webhook_events(
        self,
        webhook_id: str,
        *,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWebhookEventsResponse:
        """
        Returns a paginated list of webhook delivery events for a specific webhook, including delivery status, response codes, and retry information.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook

        page : typing.Optional[float]
            Page number for pagination (default: 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhookEventsResponse
            List of webhook events

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.list_webhook_events(
            webhook_id="webhookId",
        )
        """
        _response = self._raw_client.list_webhook_events(webhook_id, page=page, request_options=request_options)
        return _response.data

    def retry_webhook_event(
        self, webhook_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retries sending a failed webhook event. This will attempt to deliver the webhook payload again to the configured endpoint.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook

        event_id : str
            The ID of the webhook event to retry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.retry_webhook_event(
            webhook_id="webhookId",
            event_id="eventId",
        )
        """
        _response = self._raw_client.retry_webhook_event(webhook_id, event_id, request_options=request_options)
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
        self,
        *,
        page: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWebhooksResponse:
        """
        Returns a paginated list of all webhooks across your accessible forms and workspaces.

        Parameters
        ----------
        page : typing.Optional[float]
            Page number for pagination (default: 1)

        limit : typing.Optional[float]
            Number of webhooks per page (default: 25, max: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhooksResponse
            List of webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.list_webhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_webhooks(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def create_webhook(
        self,
        *,
        form_id: str,
        url: str,
        event_types: typing.Sequence[EventType],
        signing_secret: typing.Optional[str] = OMIT,
        http_headers: typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]] = OMIT,
        external_subscriber: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhookResponse:
        """
        Creates a new webhook for a form to receive form events.

        Parameters
        ----------
        form_id : str
            The ID of the form to create the webhook for

        url : str
            The URL to send webhook events to

        event_types : typing.Sequence[EventType]
            Types of events to receive

        signing_secret : typing.Optional[str]
            Optional secret used to sign webhook payloads

        http_headers : typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]]
            Optional custom HTTP headers to include in webhook requests

        external_subscriber : typing.Optional[str]
            Optional identifier for the external subscriber

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhookResponse
            Webhook created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EventType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.create_webhook(
                form_id="formId",
                url="url",
                event_types=[EventType.FORM_RESPONSE],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook(
            form_id=form_id,
            url=url,
            event_types=event_types,
            signing_secret=signing_secret,
            http_headers=http_headers,
            external_subscriber=external_subscriber,
            request_options=request_options,
        )
        return _response.data

    async def delete_webhook(self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a webhook. If this is the last webhook for a form, the webhooks integration will also be marked as deleted.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook to delete

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.delete_webhook(
                webhook_id="webhookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhook(webhook_id, request_options=request_options)
        return _response.data

    async def update_webhook(
        self,
        webhook_id: str,
        *,
        form_id: str,
        url: str,
        event_types: typing.Sequence[EventType],
        is_enabled: bool,
        signing_secret: typing.Optional[str] = OMIT,
        http_headers: typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an existing webhook configuration.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook to update

        form_id : str
            The ID of the form the webhook is for

        url : str
            The URL to send webhook events to

        event_types : typing.Sequence[EventType]
            Types of events to receive

        is_enabled : bool
            Whether the webhook is enabled

        signing_secret : typing.Optional[str]
            Optional secret used to sign webhook payloads

        http_headers : typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]]
            Optional custom HTTP headers to include in webhook requests

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EventType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.update_webhook(
                webhook_id="webhookId",
                form_id="formId",
                url="url",
                event_types=[EventType.FORM_RESPONSE],
                is_enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook(
            webhook_id,
            form_id=form_id,
            url=url,
            event_types=event_types,
            is_enabled=is_enabled,
            signing_secret=signing_secret,
            http_headers=http_headers,
            request_options=request_options,
        )
        return _response.data

    async def list_webhook_events(
        self,
        webhook_id: str,
        *,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWebhookEventsResponse:
        """
        Returns a paginated list of webhook delivery events for a specific webhook, including delivery status, response codes, and retry information.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook

        page : typing.Optional[float]
            Page number for pagination (default: 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhookEventsResponse
            List of webhook events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.list_webhook_events(
                webhook_id="webhookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_webhook_events(webhook_id, page=page, request_options=request_options)
        return _response.data

    async def retry_webhook_event(
        self, webhook_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Retries sending a failed webhook event. This will attempt to deliver the webhook payload again to the configured endpoint.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook

        event_id : str
            The ID of the webhook event to retry

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.retry_webhook_event(
                webhook_id="webhookId",
                event_id="eventId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retry_webhook_event(webhook_id, event_id, request_options=request_options)
        return _response.data
