

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1webhook import V1Webhook
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.v1webhooks_create_webhook import V1WebhooksCreateWebhook
from .types.v1webhooks_update_webhook import V1WebhooksUpdateWebhook


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
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Webhook]:
        """
        Retrieve all webhooks configured for the account. Webhooks allow you to receive HTTP POST notifications when events occur.

        Parameters
        ----------
        account_id : int
            Account ID

        limit : typing.Optional[int]
            Maximum number of webhooks to return

        offset : typing.Optional[int]
            Number of webhooks to skip

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Webhook]
            Webhooks list retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.list_webhooks(
            account_id=1,
        )
        """
        _response = self._raw_client.list_webhooks(
            account_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def create_webhook(
        self,
        account_id: int,
        *,
        webhook: V1WebhooksCreateWebhook,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Webhook:
        """
        Create a new webhook subscription. Webhooks allow you to receive HTTP POST notifications when events occur in your account.

        **Supported Events:**
        - `hours:created` - When a new time entry is created
        - `hours:updated` - When a time entry is updated
        - `hours:deleted` - When a time entry is deleted
        - `projects:created` - When a new project is created
        - `projects:updated` - When a project is updated
        - `projects:deleted` - When a project is deleted
        - `labels:created` - When a new label is created
        - `labels:updated` - When a label is updated
        - `labels:deleted` - When a label is deleted
        - `forecasts:created` - When a new forecast is created
        - `forecasts:updated` - When a forecast is updated
        - `forecasts:deleted` - When a forecast is deleted

        **Security:**
        When a `secret_token` is provided, each webhook request will include an `X-Signature` header containing an HMAC-SHA256 signature of the request body. You can use this to verify the authenticity of incoming webhook requests.

        Parameters
        ----------
        account_id : int
            Account ID

        webhook : V1WebhooksCreateWebhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Webhook
            Webhook created successfully

        Examples
        --------
        from fern.webhooks import (
            V1WebhooksCreateWebhook,
            V1WebhooksCreateWebhookSubscriptionsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.create_webhook(
            account_id=1,
            webhook=V1WebhooksCreateWebhook(
                url="https://example.com/my-webhook",
                subscriptions=[
                    V1WebhooksCreateWebhookSubscriptionsItem.HOURS_CREATED,
                    V1WebhooksCreateWebhookSubscriptionsItem.HOURS_UPDATED,
                ],
                secret_token="my-secret-token",
                active=True,
            ),
        )
        """
        _response = self._raw_client.create_webhook(account_id, webhook=webhook, request_options=request_options)
        return _response.data

    def show_webhook(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Webhook:
        """
        Retrieve details for a specific webhook.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Webhook
            Webhook details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.show_webhook(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.show_webhook(account_id, id, request_options=request_options)
        return _response.data

    def update_webhook(
        self,
        account_id: int,
        id: int,
        *,
        webhook: V1WebhooksUpdateWebhook,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Webhook:
        """
        Update an existing webhook. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Webhook ID

        webhook : V1WebhooksUpdateWebhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Webhook
            Webhook updated successfully

        Examples
        --------
        from fern.webhooks import (
            V1WebhooksUpdateWebhook,
            V1WebhooksUpdateWebhookSubscriptionsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.update_webhook(
            account_id=1,
            id=1,
            webhook=V1WebhooksUpdateWebhook(
                url="https://example.com/new-webhook",
                subscriptions=[
                    V1WebhooksUpdateWebhookSubscriptionsItem.HOURS_CREATED,
                    V1WebhooksUpdateWebhookSubscriptionsItem.PROJECTS_CREATED,
                ],
                active=False,
            ),
        )
        """
        _response = self._raw_client.update_webhook(account_id, id, webhook=webhook, request_options=request_options)
        return _response.data

    def delete_webhook(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a webhook. This will permanently remove the webhook and stop all future notifications.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Webhook deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.delete_webhook(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.delete_webhook(account_id, id, request_options=request_options)
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
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Webhook]:
        """
        Retrieve all webhooks configured for the account. Webhooks allow you to receive HTTP POST notifications when events occur.

        Parameters
        ----------
        account_id : int
            Account ID

        limit : typing.Optional[int]
            Maximum number of webhooks to return

        offset : typing.Optional[int]
            Number of webhooks to skip

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Webhook]
            Webhooks list retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.list_webhooks(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_webhooks(
            account_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_webhook(
        self,
        account_id: int,
        *,
        webhook: V1WebhooksCreateWebhook,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Webhook:
        """
        Create a new webhook subscription. Webhooks allow you to receive HTTP POST notifications when events occur in your account.

        **Supported Events:**
        - `hours:created` - When a new time entry is created
        - `hours:updated` - When a time entry is updated
        - `hours:deleted` - When a time entry is deleted
        - `projects:created` - When a new project is created
        - `projects:updated` - When a project is updated
        - `projects:deleted` - When a project is deleted
        - `labels:created` - When a new label is created
        - `labels:updated` - When a label is updated
        - `labels:deleted` - When a label is deleted
        - `forecasts:created` - When a new forecast is created
        - `forecasts:updated` - When a forecast is updated
        - `forecasts:deleted` - When a forecast is deleted

        **Security:**
        When a `secret_token` is provided, each webhook request will include an `X-Signature` header containing an HMAC-SHA256 signature of the request body. You can use this to verify the authenticity of incoming webhook requests.

        Parameters
        ----------
        account_id : int
            Account ID

        webhook : V1WebhooksCreateWebhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Webhook
            Webhook created successfully

        Examples
        --------
        import asyncio

        from fern.webhooks import (
            V1WebhooksCreateWebhook,
            V1WebhooksCreateWebhookSubscriptionsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.create_webhook(
                account_id=1,
                webhook=V1WebhooksCreateWebhook(
                    url="https://example.com/my-webhook",
                    subscriptions=[
                        V1WebhooksCreateWebhookSubscriptionsItem.HOURS_CREATED,
                        V1WebhooksCreateWebhookSubscriptionsItem.HOURS_UPDATED,
                    ],
                    secret_token="my-secret-token",
                    active=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook(account_id, webhook=webhook, request_options=request_options)
        return _response.data

    async def show_webhook(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Webhook:
        """
        Retrieve details for a specific webhook.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Webhook
            Webhook details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.show_webhook(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_webhook(account_id, id, request_options=request_options)
        return _response.data

    async def update_webhook(
        self,
        account_id: int,
        id: int,
        *,
        webhook: V1WebhooksUpdateWebhook,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Webhook:
        """
        Update an existing webhook. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Webhook ID

        webhook : V1WebhooksUpdateWebhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Webhook
            Webhook updated successfully

        Examples
        --------
        import asyncio

        from fern.webhooks import (
            V1WebhooksUpdateWebhook,
            V1WebhooksUpdateWebhookSubscriptionsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.update_webhook(
                account_id=1,
                id=1,
                webhook=V1WebhooksUpdateWebhook(
                    url="https://example.com/new-webhook",
                    subscriptions=[
                        V1WebhooksUpdateWebhookSubscriptionsItem.HOURS_CREATED,
                        V1WebhooksUpdateWebhookSubscriptionsItem.PROJECTS_CREATED,
                    ],
                    active=False,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook(
            account_id, id, webhook=webhook, request_options=request_options
        )
        return _response.data

    async def delete_webhook(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a webhook. This will permanently remove the webhook and stop all future notifications.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Webhook deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.delete_webhook(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhook(account_id, id, request_options=request_options)
        return _response.data
