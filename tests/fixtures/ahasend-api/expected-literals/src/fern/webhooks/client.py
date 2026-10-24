

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.created_webhook import CreatedWebhook
from ..types.paginated_webhooks_response import PaginatedWebhooksResponse
from ..types.success_response import SuccessResponse
from ..types.webhook import Webhook
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.create_webhook_request_scope import CreateWebhookRequestScope
from .types.update_webhook_request_scope import UpdateWebhookRequestScope


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

    def get_webhooks(
        self,
        account_id: str,
        *,
        enabled: typing.Optional[bool] = None,
        on_reception: typing.Optional[bool] = None,
        on_delivered: typing.Optional[bool] = None,
        on_transient_error: typing.Optional[bool] = None,
        on_failed: typing.Optional[bool] = None,
        on_bounced: typing.Optional[bool] = None,
        on_suppressed: typing.Optional[bool] = None,
        on_opened: typing.Optional[bool] = None,
        on_clicked: typing.Optional[bool] = None,
        on_suppression_created: typing.Optional[bool] = None,
        on_dns_error: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedWebhooksResponse:
        """
        Returns a list of webhooks for the account

        The global read role sees all webhooks. Domain-scoped read roles return
        only webhooks associated with at least one authorized domain.

        **Query Parameters:**
        - `enabled`: Filter by enabled status
        - Event filters: `on_reception`, `on_delivered`, `on_transient_error`, `on_failed`, `on_bounced`, `on_suppressed`, `on_opened`, `on_clicked`, `on_suppression_created`, `on_dns_error`
        - `limit`: Maximum number of items to return (1-100, default: 100)
        - `after`: Pagination cursor for the next page
        - `before`: Pagination cursor for the previous page

        Parameters
        ----------
        account_id : str
            Account ID

        enabled : typing.Optional[bool]
            Filter by enabled status

        on_reception : typing.Optional[bool]
            Filter by reception event trigger

        on_delivered : typing.Optional[bool]
            Filter by delivery event trigger

        on_transient_error : typing.Optional[bool]
            Filter by transient error event trigger

        on_failed : typing.Optional[bool]
            Filter by failure event trigger

        on_bounced : typing.Optional[bool]
            Filter by bounce event trigger

        on_suppressed : typing.Optional[bool]
            Filter by suppression event trigger

        on_opened : typing.Optional[bool]
            Filter by open event trigger

        on_clicked : typing.Optional[bool]
            Filter by click event trigger

        on_suppression_created : typing.Optional[bool]
            Filter by suppression creation event trigger

        on_dns_error : typing.Optional[bool]
            Filter by DNS error event trigger

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedWebhooksResponse
            List of webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.get_webhooks(
            account_id="account_id",
        )
        """
        _response = self._raw_client.get_webhooks(
            account_id,
            enabled=enabled,
            on_reception=on_reception,
            on_delivered=on_delivered,
            on_transient_error=on_transient_error,
            on_failed=on_failed,
            on_bounced=on_bounced,
            on_suppressed=on_suppressed,
            on_opened=on_opened,
            on_clicked=on_clicked,
            on_suppression_created=on_suppression_created,
            on_dns_error=on_dns_error,
            limit=limit,
            after=after,
            before=before,
            request_options=request_options,
        )
        return _response.data

    def create_webhook(
        self,
        account_id: str,
        *,
        name: str,
        url: str,
        scope: CreateWebhookRequestScope,
        idempotency_key: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = OMIT,
        on_reception: typing.Optional[bool] = OMIT,
        on_delivered: typing.Optional[bool] = OMIT,
        on_transient_error: typing.Optional[bool] = OMIT,
        on_failed: typing.Optional[bool] = OMIT,
        on_bounced: typing.Optional[bool] = OMIT,
        on_suppressed: typing.Optional[bool] = OMIT,
        on_opened: typing.Optional[bool] = OMIT,
        on_clicked: typing.Optional[bool] = OMIT,
        on_suppression_created: typing.Optional[bool] = OMIT,
        on_dns_error: typing.Optional[bool] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedWebhook:
        """
        Creates a new webhook for event notifications. A `scoped` webhook
        requires at least one domain and the key must have write permission for
        every supplied domain. A `global` webhook requires
        `webhooks:write:all`; supplied domains are accepted but ignored, and
        the response contains `domains: []`.

        Parameters
        ----------
        account_id : str
            Account ID

        name : str
            Webhook name

        url : str
            Webhook URL

        scope : CreateWebhookRequestScope
            Webhook scope

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        enabled : typing.Optional[bool]
            Whether the webhook is enabled

        on_reception : typing.Optional[bool]
            Trigger on message reception

        on_delivered : typing.Optional[bool]
            Trigger on message delivery

        on_transient_error : typing.Optional[bool]
            Trigger on transient errors

        on_failed : typing.Optional[bool]
            Trigger on permanent failures

        on_bounced : typing.Optional[bool]
            Trigger on bounces

        on_suppressed : typing.Optional[bool]
            Trigger on suppressions

        on_opened : typing.Optional[bool]
            Trigger on opens

        on_clicked : typing.Optional[bool]
            Trigger on clicks

        on_suppression_created : typing.Optional[bool]
            Trigger on suppression creation

        on_dns_error : typing.Optional[bool]
            Trigger on DNS errors

        domains : typing.Optional[typing.Sequence[str]]
            For `scoped`, a non-empty array is required. For `global`, this may
            be omitted, null, empty, or non-empty; supplied values are accepted
            but ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedWebhook
            Webhook created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.create_webhook(
            account_id="account_id",
            idempotency_key="user-12345-create-domain-20240101",
            name="Delivery Webhook",
            url="https://example.com/webhook",
            enabled=True,
            on_delivered=True,
            scope="global",
        )
        """
        _response = self._raw_client.create_webhook(
            account_id,
            name=name,
            url=url,
            scope=scope,
            idempotency_key=idempotency_key,
            enabled=enabled,
            on_reception=on_reception,
            on_delivered=on_delivered,
            on_transient_error=on_transient_error,
            on_failed=on_failed,
            on_bounced=on_bounced,
            on_suppressed=on_suppressed,
            on_opened=on_opened,
            on_clicked=on_clicked,
            on_suppression_created=on_suppression_created,
            on_dns_error=on_dns_error,
            domains=domains,
            request_options=request_options,
        )
        return _response.data

    def get_webhook(
        self, account_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Webhook:
        """
        Returns a specific webhook by ID. Access requires the global read role
        or a read role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Webhook details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.get_webhook(
            account_id="account_id",
            webhook_id="webhook_id",
        )
        """
        _response = self._raw_client.get_webhook(account_id, webhook_id, request_options=request_options)
        return _response.data

    def update_webhook(
        self,
        account_id: str,
        webhook_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        on_reception: typing.Optional[bool] = OMIT,
        on_delivered: typing.Optional[bool] = OMIT,
        on_transient_error: typing.Optional[bool] = OMIT,
        on_failed: typing.Optional[bool] = OMIT,
        on_bounced: typing.Optional[bool] = OMIT,
        on_suppressed: typing.Optional[bool] = OMIT,
        on_opened: typing.Optional[bool] = OMIT,
        on_clicked: typing.Optional[bool] = OMIT,
        on_suppression_created: typing.Optional[bool] = OMIT,
        on_dns_error: typing.Optional[bool] = OMIT,
        scope: typing.Optional[UpdateWebhookRequestScope] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Updates an existing webhook. Omitted or null fields are unchanged.
        Omitted/null `domains` preserves associations, while `[]` clears the
        associations of a resulting-scoped webhook. Moving from global to
        scoped requires a non-empty `domains` array in the same request. Moving
        to global clears associations and ignores supplied domains.

        A domain-scoped key must be authorized for the existing webhook and
        every newly supplied domain; changing to global requires
        `webhooks:write:all`.

        **Note:** The webhook secret is not updatable

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        name : typing.Optional[str]
            Webhook name

        url : typing.Optional[str]
            Webhook URL

        enabled : typing.Optional[bool]
            Whether the webhook is enabled

        on_reception : typing.Optional[bool]
            Trigger on message reception

        on_delivered : typing.Optional[bool]
            Trigger on message delivery

        on_transient_error : typing.Optional[bool]
            Trigger on transient errors

        on_failed : typing.Optional[bool]
            Trigger on permanent failures

        on_bounced : typing.Optional[bool]
            Trigger on bounces

        on_suppressed : typing.Optional[bool]
            Trigger on suppressions

        on_opened : typing.Optional[bool]
            Trigger on opens

        on_clicked : typing.Optional[bool]
            Trigger on clicks

        on_suppression_created : typing.Optional[bool]
            Trigger on suppression creation

        on_dns_error : typing.Optional[bool]
            Trigger on DNS errors

        scope : typing.Optional[UpdateWebhookRequestScope]
            Webhook scope. Omit or send null to keep the current scope.

        domains : typing.Optional[typing.Sequence[str]]
            Omit or send null to leave domain associations unchanged. An array
            replaces associations when the resulting scope is `scoped`; `[]`
            explicitly clears them. Changing a global webhook to `scoped`
            requires a non-empty array in the same request and otherwise
            returns HTTP 400. Changing to `global` clears all associations;
            supplied domains are ignored when the resulting scope is global.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Webhook updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.update_webhook(
            account_id="account_id",
            webhook_id="webhook_id",
        )
        """
        _response = self._raw_client.update_webhook(
            account_id,
            webhook_id,
            name=name,
            url=url,
            enabled=enabled,
            on_reception=on_reception,
            on_delivered=on_delivered,
            on_transient_error=on_transient_error,
            on_failed=on_failed,
            on_bounced=on_bounced,
            on_suppressed=on_suppressed,
            on_opened=on_opened,
            on_clicked=on_clicked,
            on_suppression_created=on_suppression_created,
            on_dns_error=on_dns_error,
            scope=scope,
            domains=domains,
            request_options=request_options,
        )
        return _response.data

    def delete_webhook(
        self, account_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes a webhook. Access requires the global delete role or a delete
        role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Webhook deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.delete_webhook(
            account_id="account_id",
            webhook_id="webhook_id",
        )
        """
        _response = self._raw_client.delete_webhook(account_id, webhook_id, request_options=request_options)
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

    async def get_webhooks(
        self,
        account_id: str,
        *,
        enabled: typing.Optional[bool] = None,
        on_reception: typing.Optional[bool] = None,
        on_delivered: typing.Optional[bool] = None,
        on_transient_error: typing.Optional[bool] = None,
        on_failed: typing.Optional[bool] = None,
        on_bounced: typing.Optional[bool] = None,
        on_suppressed: typing.Optional[bool] = None,
        on_opened: typing.Optional[bool] = None,
        on_clicked: typing.Optional[bool] = None,
        on_suppression_created: typing.Optional[bool] = None,
        on_dns_error: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedWebhooksResponse:
        """
        Returns a list of webhooks for the account

        The global read role sees all webhooks. Domain-scoped read roles return
        only webhooks associated with at least one authorized domain.

        **Query Parameters:**
        - `enabled`: Filter by enabled status
        - Event filters: `on_reception`, `on_delivered`, `on_transient_error`, `on_failed`, `on_bounced`, `on_suppressed`, `on_opened`, `on_clicked`, `on_suppression_created`, `on_dns_error`
        - `limit`: Maximum number of items to return (1-100, default: 100)
        - `after`: Pagination cursor for the next page
        - `before`: Pagination cursor for the previous page

        Parameters
        ----------
        account_id : str
            Account ID

        enabled : typing.Optional[bool]
            Filter by enabled status

        on_reception : typing.Optional[bool]
            Filter by reception event trigger

        on_delivered : typing.Optional[bool]
            Filter by delivery event trigger

        on_transient_error : typing.Optional[bool]
            Filter by transient error event trigger

        on_failed : typing.Optional[bool]
            Filter by failure event trigger

        on_bounced : typing.Optional[bool]
            Filter by bounce event trigger

        on_suppressed : typing.Optional[bool]
            Filter by suppression event trigger

        on_opened : typing.Optional[bool]
            Filter by open event trigger

        on_clicked : typing.Optional[bool]
            Filter by click event trigger

        on_suppression_created : typing.Optional[bool]
            Filter by suppression creation event trigger

        on_dns_error : typing.Optional[bool]
            Filter by DNS error event trigger

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedWebhooksResponse
            List of webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.get_webhooks(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhooks(
            account_id,
            enabled=enabled,
            on_reception=on_reception,
            on_delivered=on_delivered,
            on_transient_error=on_transient_error,
            on_failed=on_failed,
            on_bounced=on_bounced,
            on_suppressed=on_suppressed,
            on_opened=on_opened,
            on_clicked=on_clicked,
            on_suppression_created=on_suppression_created,
            on_dns_error=on_dns_error,
            limit=limit,
            after=after,
            before=before,
            request_options=request_options,
        )
        return _response.data

    async def create_webhook(
        self,
        account_id: str,
        *,
        name: str,
        url: str,
        scope: CreateWebhookRequestScope,
        idempotency_key: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = OMIT,
        on_reception: typing.Optional[bool] = OMIT,
        on_delivered: typing.Optional[bool] = OMIT,
        on_transient_error: typing.Optional[bool] = OMIT,
        on_failed: typing.Optional[bool] = OMIT,
        on_bounced: typing.Optional[bool] = OMIT,
        on_suppressed: typing.Optional[bool] = OMIT,
        on_opened: typing.Optional[bool] = OMIT,
        on_clicked: typing.Optional[bool] = OMIT,
        on_suppression_created: typing.Optional[bool] = OMIT,
        on_dns_error: typing.Optional[bool] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedWebhook:
        """
        Creates a new webhook for event notifications. A `scoped` webhook
        requires at least one domain and the key must have write permission for
        every supplied domain. A `global` webhook requires
        `webhooks:write:all`; supplied domains are accepted but ignored, and
        the response contains `domains: []`.

        Parameters
        ----------
        account_id : str
            Account ID

        name : str
            Webhook name

        url : str
            Webhook URL

        scope : CreateWebhookRequestScope
            Webhook scope

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        enabled : typing.Optional[bool]
            Whether the webhook is enabled

        on_reception : typing.Optional[bool]
            Trigger on message reception

        on_delivered : typing.Optional[bool]
            Trigger on message delivery

        on_transient_error : typing.Optional[bool]
            Trigger on transient errors

        on_failed : typing.Optional[bool]
            Trigger on permanent failures

        on_bounced : typing.Optional[bool]
            Trigger on bounces

        on_suppressed : typing.Optional[bool]
            Trigger on suppressions

        on_opened : typing.Optional[bool]
            Trigger on opens

        on_clicked : typing.Optional[bool]
            Trigger on clicks

        on_suppression_created : typing.Optional[bool]
            Trigger on suppression creation

        on_dns_error : typing.Optional[bool]
            Trigger on DNS errors

        domains : typing.Optional[typing.Sequence[str]]
            For `scoped`, a non-empty array is required. For `global`, this may
            be omitted, null, empty, or non-empty; supplied values are accepted
            but ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedWebhook
            Webhook created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.create_webhook(
                account_id="account_id",
                idempotency_key="user-12345-create-domain-20240101",
                name="Delivery Webhook",
                url="https://example.com/webhook",
                enabled=True,
                on_delivered=True,
                scope="global",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook(
            account_id,
            name=name,
            url=url,
            scope=scope,
            idempotency_key=idempotency_key,
            enabled=enabled,
            on_reception=on_reception,
            on_delivered=on_delivered,
            on_transient_error=on_transient_error,
            on_failed=on_failed,
            on_bounced=on_bounced,
            on_suppressed=on_suppressed,
            on_opened=on_opened,
            on_clicked=on_clicked,
            on_suppression_created=on_suppression_created,
            on_dns_error=on_dns_error,
            domains=domains,
            request_options=request_options,
        )
        return _response.data

    async def get_webhook(
        self, account_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Webhook:
        """
        Returns a specific webhook by ID. Access requires the global read role
        or a read role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Webhook details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.get_webhook(
                account_id="account_id",
                webhook_id="webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhook(account_id, webhook_id, request_options=request_options)
        return _response.data

    async def update_webhook(
        self,
        account_id: str,
        webhook_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        on_reception: typing.Optional[bool] = OMIT,
        on_delivered: typing.Optional[bool] = OMIT,
        on_transient_error: typing.Optional[bool] = OMIT,
        on_failed: typing.Optional[bool] = OMIT,
        on_bounced: typing.Optional[bool] = OMIT,
        on_suppressed: typing.Optional[bool] = OMIT,
        on_opened: typing.Optional[bool] = OMIT,
        on_clicked: typing.Optional[bool] = OMIT,
        on_suppression_created: typing.Optional[bool] = OMIT,
        on_dns_error: typing.Optional[bool] = OMIT,
        scope: typing.Optional[UpdateWebhookRequestScope] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Updates an existing webhook. Omitted or null fields are unchanged.
        Omitted/null `domains` preserves associations, while `[]` clears the
        associations of a resulting-scoped webhook. Moving from global to
        scoped requires a non-empty `domains` array in the same request. Moving
        to global clears associations and ignores supplied domains.

        A domain-scoped key must be authorized for the existing webhook and
        every newly supplied domain; changing to global requires
        `webhooks:write:all`.

        **Note:** The webhook secret is not updatable

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        name : typing.Optional[str]
            Webhook name

        url : typing.Optional[str]
            Webhook URL

        enabled : typing.Optional[bool]
            Whether the webhook is enabled

        on_reception : typing.Optional[bool]
            Trigger on message reception

        on_delivered : typing.Optional[bool]
            Trigger on message delivery

        on_transient_error : typing.Optional[bool]
            Trigger on transient errors

        on_failed : typing.Optional[bool]
            Trigger on permanent failures

        on_bounced : typing.Optional[bool]
            Trigger on bounces

        on_suppressed : typing.Optional[bool]
            Trigger on suppressions

        on_opened : typing.Optional[bool]
            Trigger on opens

        on_clicked : typing.Optional[bool]
            Trigger on clicks

        on_suppression_created : typing.Optional[bool]
            Trigger on suppression creation

        on_dns_error : typing.Optional[bool]
            Trigger on DNS errors

        scope : typing.Optional[UpdateWebhookRequestScope]
            Webhook scope. Omit or send null to keep the current scope.

        domains : typing.Optional[typing.Sequence[str]]
            Omit or send null to leave domain associations unchanged. An array
            replaces associations when the resulting scope is `scoped`; `[]`
            explicitly clears them. Changing a global webhook to `scoped`
            requires a non-empty array in the same request and otherwise
            returns HTTP 400. Changing to `global` clears all associations;
            supplied domains are ignored when the resulting scope is global.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Webhook updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.update_webhook(
                account_id="account_id",
                webhook_id="webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook(
            account_id,
            webhook_id,
            name=name,
            url=url,
            enabled=enabled,
            on_reception=on_reception,
            on_delivered=on_delivered,
            on_transient_error=on_transient_error,
            on_failed=on_failed,
            on_bounced=on_bounced,
            on_suppressed=on_suppressed,
            on_opened=on_opened,
            on_clicked=on_clicked,
            on_suppression_created=on_suppression_created,
            on_dns_error=on_dns_error,
            scope=scope,
            domains=domains,
            request_options=request_options,
        )
        return _response.data

    async def delete_webhook(
        self, account_id: str, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes a webhook. Access requires the global delete role or a delete
        role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        webhook_id : str
            Webhook ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
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
                account_id="account_id",
                webhook_id="webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhook(account_id, webhook_id, request_options=request_options)
        return _response.data
