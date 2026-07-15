

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_webhook_response import CreateWebhookResponse
from ..types.delete_webhook_response import DeleteWebhookResponse
from ..types.delivery_url import DeliveryUrl
from ..types.description import Description
from ..types.execute_webhook_response import ExecuteWebhookResponse
from ..types.get_webhook_event_logs_response import GetWebhookEventLogsResponse
from ..types.get_webhook_response import GetWebhookResponse
from ..types.get_webhooks_response import GetWebhooksResponse
from ..types.resolve_webhook_response import ResolveWebhookResponse
from ..types.status import Status
from ..types.unified_api_id import UnifiedApiId
from ..types.update_webhook_response import UpdateWebhookResponse
from ..types.webhook_event_logs_filter import WebhookEventLogsFilter
from ..types.webhook_event_type import WebhookEventType
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.webhooks_execute_request_body import WebhooksExecuteRequestBody
from .types.webhooks_resolve_request_body import WebhooksResolveRequestBody
from .types.webhooks_short_execute_request_body import WebhooksShortExecuteRequestBody


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

    def event_logs_all(
        self,
        *,
        apideck_app_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[WebhookEventLogsFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWebhookEventLogsResponse:
        """
        List event logs

        Parameters
        ----------
        apideck_app_id : str
            The ID of your Unify application

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[WebhookEventLogsFilter]
            Filter results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookEventLogsResponse
            EventLogs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.event_logs_all(
            apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
        )
        """
        _response = self._raw_client.event_logs_all(
            apideck_app_id=apideck_app_id, cursor=cursor, limit=limit, filter=filter, request_options=request_options
        )
        return _response.data

    def resolve(
        self,
        id: str,
        service_id: str,
        *,
        request: WebhooksResolveRequestBody,
        e: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolveWebhookResponse:
        """
        Resolve a webhook based on lookup_id and then execute it

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the connection lookupId. Signed so we know source came from us

        service_id : str
            Service provider ID.

        request : WebhooksResolveRequestBody

        e : typing.Optional[str]
            The name of downstream event when connector does not supply in body or header

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolveWebhookResponse
            Resolve Webhook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.resolve(
            id="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijk2MDAwYzIzLWI1NmItNGRlOC1iZmEzLTMxNTAzMTE3YzBmNyJ9.rAXnsmZ4O7eF0aDwdflkxAJQwMUfWs5989WfmspNZ6Q",
            service_id="factorialhr",
            e="Employees::Events::EmployeeCreated",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.resolve(id, service_id, request=request, e=e, request_options=request_options)
        return _response.data

    def all_(
        self,
        *,
        apideck_app_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWebhooksResponse:
        """
        List all webhook subscriptions

        Parameters
        ----------
        apideck_app_id : str
            The ID of your Unify application

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.all_(
            apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
        )
        """
        _response = self._raw_client.all_(
            apideck_app_id=apideck_app_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def add(
        self,
        *,
        apideck_app_id: str,
        delivery_url: DeliveryUrl,
        events: typing.Sequence[WebhookEventType],
        status: Status,
        unified_api: UnifiedApiId,
        description: typing.Optional[Description] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhookResponse:
        """
        Create a webhook subscription to receive events

        Parameters
        ----------
        apideck_app_id : str
            The ID of your Unify application

        delivery_url : DeliveryUrl

        events : typing.Sequence[WebhookEventType]
            The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.

        status : Status

        unified_api : UnifiedApiId

        description : typing.Optional[Description]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhookResponse
            Webhooks

        Examples
        --------
        from fern import FernApi, Status, UnifiedApiId, WebhookEventType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.add(
            apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
            delivery_url="https://example.com/my/webhook/endpoint",
            events=[
                WebhookEventType.VAULT_CONNECTION_CREATED,
                WebhookEventType.VAULT_CONNECTION_UPDATED,
            ],
            status=Status.ENABLED,
            unified_api=UnifiedApiId.ACCOUNTING,
        )
        """
        _response = self._raw_client.add(
            apideck_app_id=apideck_app_id,
            delivery_url=delivery_url,
            events=events,
            status=status,
            unified_api=unified_api,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def one(
        self, id: str, *, apideck_app_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookResponse:
        """
        Get the webhook subscription details

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        apideck_app_id : str
            The ID of your Unify application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookResponse
            Webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.one(
            id="id",
            apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
        )
        """
        _response = self._raw_client.one(id, apideck_app_id=apideck_app_id, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, apideck_app_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWebhookResponse:
        """
        Delete a webhook subscription

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        apideck_app_id : str
            The ID of your Unify application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhookResponse
            Webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.delete(
            id="id",
            apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
        )
        """
        _response = self._raw_client.delete(id, apideck_app_id=apideck_app_id, request_options=request_options)
        return _response.data

    def update(
        self,
        id: str,
        *,
        apideck_app_id: str,
        delivery_url: typing.Optional[DeliveryUrl] = OMIT,
        description: typing.Optional[Description] = OMIT,
        events: typing.Optional[typing.Sequence[WebhookEventType]] = OMIT,
        status: typing.Optional[Status] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookResponse:
        """
        Update a webhook subscription

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        apideck_app_id : str
            The ID of your Unify application

        delivery_url : typing.Optional[DeliveryUrl]

        description : typing.Optional[Description]

        events : typing.Optional[typing.Sequence[WebhookEventType]]
            The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.

        status : typing.Optional[Status]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookResponse
            Webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.update(
            id="id",
            apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
        )
        """
        _response = self._raw_client.update(
            id,
            apideck_app_id=apideck_app_id,
            delivery_url=delivery_url,
            description=description,
            events=events,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def execute(
        self,
        id: str,
        service_id: str,
        *,
        request: WebhooksExecuteRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecuteWebhookResponse:
        """
        Execute a webhook

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        service_id : str
            Service provider ID.

        request : WebhooksExecuteRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecuteWebhookResponse
            Execute Webhook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.execute(
            id="id",
            service_id="factorialhr",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.execute(id, service_id, request=request, request_options=request_options)
        return _response.data

    def short_execute(
        self,
        id: str,
        service_id: str,
        *,
        request: WebhooksShortExecuteRequestBody,
        l_id: typing.Optional[str] = None,
        e: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecuteWebhookResponse:
        """
        Execute a webhook

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        service_id : str
            Service provider ID.

        request : WebhooksShortExecuteRequestBody

        l_id : typing.Optional[str]
            Unique identifier to used to look up consumer/connection when receiving connector events from downstream.

        e : typing.Optional[str]
            The name of downstream event when connector does not supply in body or header

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecuteWebhookResponse
            Execute Webhook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.short_execute(
            id="id",
            service_id="factorialhr",
            l_id="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjA3NWUwNmEzLTUwNzUtNDY3Yi1hNTk5LWVkNmM5YTg5NTYyOCJ9._ppKdmBaCB2RHjBTifMNP2xKNeLBfNPim2CiHSUd0Zg",
            e="Employees::Events::EmployeeCreated",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.short_execute(
            id, service_id, request=request, l_id=l_id, e=e, request_options=request_options
        )
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

    async def event_logs_all(
        self,
        *,
        apideck_app_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[WebhookEventLogsFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWebhookEventLogsResponse:
        """
        List event logs

        Parameters
        ----------
        apideck_app_id : str
            The ID of your Unify application

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[WebhookEventLogsFilter]
            Filter results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookEventLogsResponse
            EventLogs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.event_logs_all(
                apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.event_logs_all(
            apideck_app_id=apideck_app_id, cursor=cursor, limit=limit, filter=filter, request_options=request_options
        )
        return _response.data

    async def resolve(
        self,
        id: str,
        service_id: str,
        *,
        request: WebhooksResolveRequestBody,
        e: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolveWebhookResponse:
        """
        Resolve a webhook based on lookup_id and then execute it

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the connection lookupId. Signed so we know source came from us

        service_id : str
            Service provider ID.

        request : WebhooksResolveRequestBody

        e : typing.Optional[str]
            The name of downstream event when connector does not supply in body or header

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolveWebhookResponse
            Resolve Webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.resolve(
                id="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijk2MDAwYzIzLWI1NmItNGRlOC1iZmEzLTMxNTAzMTE3YzBmNyJ9.rAXnsmZ4O7eF0aDwdflkxAJQwMUfWs5989WfmspNZ6Q",
                service_id="factorialhr",
                e="Employees::Events::EmployeeCreated",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve(
            id, service_id, request=request, e=e, request_options=request_options
        )
        return _response.data

    async def all_(
        self,
        *,
        apideck_app_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWebhooksResponse:
        """
        List all webhook subscriptions

        Parameters
        ----------
        apideck_app_id : str
            The ID of your Unify application

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.all_(
                apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            apideck_app_id=apideck_app_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def add(
        self,
        *,
        apideck_app_id: str,
        delivery_url: DeliveryUrl,
        events: typing.Sequence[WebhookEventType],
        status: Status,
        unified_api: UnifiedApiId,
        description: typing.Optional[Description] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhookResponse:
        """
        Create a webhook subscription to receive events

        Parameters
        ----------
        apideck_app_id : str
            The ID of your Unify application

        delivery_url : DeliveryUrl

        events : typing.Sequence[WebhookEventType]
            The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.

        status : Status

        unified_api : UnifiedApiId

        description : typing.Optional[Description]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhookResponse
            Webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Status, UnifiedApiId, WebhookEventType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.add(
                apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
                delivery_url="https://example.com/my/webhook/endpoint",
                events=[
                    WebhookEventType.VAULT_CONNECTION_CREATED,
                    WebhookEventType.VAULT_CONNECTION_UPDATED,
                ],
                status=Status.ENABLED,
                unified_api=UnifiedApiId.ACCOUNTING,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            apideck_app_id=apideck_app_id,
            delivery_url=delivery_url,
            events=events,
            status=status,
            unified_api=unified_api,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self, id: str, *, apideck_app_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookResponse:
        """
        Get the webhook subscription details

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        apideck_app_id : str
            The ID of your Unify application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookResponse
            Webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.one(
                id="id",
                apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, apideck_app_id=apideck_app_id, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, apideck_app_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWebhookResponse:
        """
        Delete a webhook subscription

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        apideck_app_id : str
            The ID of your Unify application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhookResponse
            Webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.delete(
                id="id",
                apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, apideck_app_id=apideck_app_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        id: str,
        *,
        apideck_app_id: str,
        delivery_url: typing.Optional[DeliveryUrl] = OMIT,
        description: typing.Optional[Description] = OMIT,
        events: typing.Optional[typing.Sequence[WebhookEventType]] = OMIT,
        status: typing.Optional[Status] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookResponse:
        """
        Update a webhook subscription

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        apideck_app_id : str
            The ID of your Unify application

        delivery_url : typing.Optional[DeliveryUrl]

        description : typing.Optional[Description]

        events : typing.Optional[typing.Sequence[WebhookEventType]]
            The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.

        status : typing.Optional[Status]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookResponse
            Webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.update(
                id="id",
                apideck_app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id,
            apideck_app_id=apideck_app_id,
            delivery_url=delivery_url,
            description=description,
            events=events,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def execute(
        self,
        id: str,
        service_id: str,
        *,
        request: WebhooksExecuteRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecuteWebhookResponse:
        """
        Execute a webhook

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        service_id : str
            Service provider ID.

        request : WebhooksExecuteRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecuteWebhookResponse
            Execute Webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.execute(
                id="id",
                service_id="factorialhr",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute(id, service_id, request=request, request_options=request_options)
        return _response.data

    async def short_execute(
        self,
        id: str,
        service_id: str,
        *,
        request: WebhooksShortExecuteRequestBody,
        l_id: typing.Optional[str] = None,
        e: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecuteWebhookResponse:
        """
        Execute a webhook

        Parameters
        ----------
        id : str
            JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.

        service_id : str
            Service provider ID.

        request : WebhooksShortExecuteRequestBody

        l_id : typing.Optional[str]
            Unique identifier to used to look up consumer/connection when receiving connector events from downstream.

        e : typing.Optional[str]
            The name of downstream event when connector does not supply in body or header

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecuteWebhookResponse
            Execute Webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.short_execute(
                id="id",
                service_id="factorialhr",
                l_id="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjA3NWUwNmEzLTUwNzUtNDY3Yi1hNTk5LWVkNmM5YTg5NTYyOCJ9._ppKdmBaCB2RHjBTifMNP2xKNeLBfNPim2CiHSUd0Zg",
                e="Employees::Events::EmployeeCreated",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.short_execute(
            id, service_id, request=request, l_id=l_id, e=e, request_options=request_options
        )
        return _response.data
