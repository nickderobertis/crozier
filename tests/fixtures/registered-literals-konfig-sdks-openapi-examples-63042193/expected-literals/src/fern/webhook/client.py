

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.webhook_create_outbound_webhook_response import WebhookCreateOutboundWebhookResponse
from ..types.webhook_delete_outbound_webhook_response import WebhookDeleteOutboundWebhookResponse
from ..types.webhook_get_by_id_response import WebhookGetByIdResponse
from ..types.webhook_list_matching_scope_response import WebhookListMatchingScopeResponse
from ..types.webhook_update_outbound_webhook_response import WebhookUpdateOutboundWebhookResponse
from .raw_client import AsyncRawWebhookClient, RawWebhookClient
from .types.webhook_create_outbound_webhook_request_events_item import WebhookCreateOutboundWebhookRequestEventsItem
from .types.webhook_create_outbound_webhook_request_scope import WebhookCreateOutboundWebhookRequestScope
from .types.webhook_list_matching_scope_request_scope_type import WebhookListMatchingScopeRequestScopeType
from .types.webhook_update_outbound_webhook_request_events_item import WebhookUpdateOutboundWebhookRequestEventsItem


OMIT = typing.cast(typing.Any, ...)


class WebhookClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebhookClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebhookClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebhookClient
        """
        return self._raw_client

    def listmatchingscope(
        self,
        *,
        scope_id: str,
        scope_type: WebhookListMatchingScopeRequestScopeType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookListMatchingScopeResponse:
        """
        Get a list of outbound webhooks that match the given scope-type and scope-id

        Parameters
        ----------
        scope_id : str
            ID of the scope being used (at the moment, only project ID is supported)

        scope_type : WebhookListMatchingScopeRequestScopeType
            Type of the scope being used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookListMatchingScopeResponse
            A list of webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhook.listmatchingscope(
            scope_id="scope-id",
            scope_type="project",
        )
        """
        _response = self._raw_client.listmatchingscope(
            scope_id=scope_id, scope_type=scope_type, request_options=request_options
        )
        return _response.data

    def createoutboundwebhook(
        self,
        *,
        name: str,
        events: typing.Sequence[WebhookCreateOutboundWebhookRequestEventsItem],
        url: str,
        verify_tls: bool,
        signing_secret: str,
        scope: WebhookCreateOutboundWebhookRequestScope,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookCreateOutboundWebhookResponse:
        """
        Creates an outbound webhook.

        Parameters
        ----------
        name : str
            Name of the webhook

        events : typing.Sequence[WebhookCreateOutboundWebhookRequestEventsItem]
            Events that will trigger the webhook

        url : str
            URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

        verify_tls : bool
            Whether to enforce TLS certificate verification when delivering the webhook

        signing_secret : str
            Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

        scope : WebhookCreateOutboundWebhookRequestScope
            The scope in which the relevant events that will trigger webhooks

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookCreateOutboundWebhookResponse
            A webhook

        Examples
        --------
        from fern.webhook import WebhookCreateOutboundWebhookRequestScope

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhook.createoutboundwebhook(
            name="name",
            events=["workflow-completed"],
            url="url",
            verify_tls=True,
            signing_secret="signing-secret",
            scope=WebhookCreateOutboundWebhookRequestScope(
                id="id",
                type="project",
            ),
        )
        """
        _response = self._raw_client.createoutboundwebhook(
            name=name,
            events=events,
            url=url,
            verify_tls=verify_tls,
            signing_secret=signing_secret,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    def getbyid(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookGetByIdResponse:
        """
        Get an outbound webhook by id.

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookGetByIdResponse
            A webhook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhook.getbyid(
            webhook_id="webhook-id",
        )
        """
        _response = self._raw_client.getbyid(webhook_id, request_options=request_options)
        return _response.data

    def updateoutboundwebhook(
        self,
        webhook_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        events: typing.Optional[typing.Sequence[WebhookUpdateOutboundWebhookRequestEventsItem]] = OMIT,
        url: typing.Optional[str] = OMIT,
        signing_secret: typing.Optional[str] = OMIT,
        verify_tls: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookUpdateOutboundWebhookResponse:
        """
        Updates an outbound webhook.

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        name : typing.Optional[str]
            Name of the webhook

        events : typing.Optional[typing.Sequence[WebhookUpdateOutboundWebhookRequestEventsItem]]
            Events that will trigger the webhook

        url : typing.Optional[str]
            URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

        signing_secret : typing.Optional[str]
            Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

        verify_tls : typing.Optional[bool]
            Whether to enforce TLS certificate verification when delivering the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookUpdateOutboundWebhookResponse
            A webhook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhook.updateoutboundwebhook(
            webhook_id="webhook-id",
        )
        """
        _response = self._raw_client.updateoutboundwebhook(
            webhook_id,
            name=name,
            events=events,
            url=url,
            signing_secret=signing_secret,
            verify_tls=verify_tls,
            request_options=request_options,
        )
        return _response.data

    def deleteoutboundwebhook(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookDeleteOutboundWebhookResponse:
        """
        Deletes an outbound webhook

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookDeleteOutboundWebhookResponse
            A confirmation message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhook.deleteoutboundwebhook(
            webhook_id="webhook-id",
        )
        """
        _response = self._raw_client.deleteoutboundwebhook(webhook_id, request_options=request_options)
        return _response.data


class AsyncWebhookClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebhookClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebhookClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebhookClient
        """
        return self._raw_client

    async def listmatchingscope(
        self,
        *,
        scope_id: str,
        scope_type: WebhookListMatchingScopeRequestScopeType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookListMatchingScopeResponse:
        """
        Get a list of outbound webhooks that match the given scope-type and scope-id

        Parameters
        ----------
        scope_id : str
            ID of the scope being used (at the moment, only project ID is supported)

        scope_type : WebhookListMatchingScopeRequestScopeType
            Type of the scope being used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookListMatchingScopeResponse
            A list of webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhook.listmatchingscope(
                scope_id="scope-id",
                scope_type="project",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listmatchingscope(
            scope_id=scope_id, scope_type=scope_type, request_options=request_options
        )
        return _response.data

    async def createoutboundwebhook(
        self,
        *,
        name: str,
        events: typing.Sequence[WebhookCreateOutboundWebhookRequestEventsItem],
        url: str,
        verify_tls: bool,
        signing_secret: str,
        scope: WebhookCreateOutboundWebhookRequestScope,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookCreateOutboundWebhookResponse:
        """
        Creates an outbound webhook.

        Parameters
        ----------
        name : str
            Name of the webhook

        events : typing.Sequence[WebhookCreateOutboundWebhookRequestEventsItem]
            Events that will trigger the webhook

        url : str
            URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

        verify_tls : bool
            Whether to enforce TLS certificate verification when delivering the webhook

        signing_secret : str
            Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

        scope : WebhookCreateOutboundWebhookRequestScope
            The scope in which the relevant events that will trigger webhooks

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookCreateOutboundWebhookResponse
            A webhook

        Examples
        --------
        import asyncio

        from fern.webhook import WebhookCreateOutboundWebhookRequestScope

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhook.createoutboundwebhook(
                name="name",
                events=["workflow-completed"],
                url="url",
                verify_tls=True,
                signing_secret="signing-secret",
                scope=WebhookCreateOutboundWebhookRequestScope(
                    id="id",
                    type="project",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createoutboundwebhook(
            name=name,
            events=events,
            url=url,
            verify_tls=verify_tls,
            signing_secret=signing_secret,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    async def getbyid(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookGetByIdResponse:
        """
        Get an outbound webhook by id.

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookGetByIdResponse
            A webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhook.getbyid(
                webhook_id="webhook-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbyid(webhook_id, request_options=request_options)
        return _response.data

    async def updateoutboundwebhook(
        self,
        webhook_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        events: typing.Optional[typing.Sequence[WebhookUpdateOutboundWebhookRequestEventsItem]] = OMIT,
        url: typing.Optional[str] = OMIT,
        signing_secret: typing.Optional[str] = OMIT,
        verify_tls: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookUpdateOutboundWebhookResponse:
        """
        Updates an outbound webhook.

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        name : typing.Optional[str]
            Name of the webhook

        events : typing.Optional[typing.Sequence[WebhookUpdateOutboundWebhookRequestEventsItem]]
            Events that will trigger the webhook

        url : typing.Optional[str]
            URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

        signing_secret : typing.Optional[str]
            Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

        verify_tls : typing.Optional[bool]
            Whether to enforce TLS certificate verification when delivering the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookUpdateOutboundWebhookResponse
            A webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhook.updateoutboundwebhook(
                webhook_id="webhook-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateoutboundwebhook(
            webhook_id,
            name=name,
            events=events,
            url=url,
            signing_secret=signing_secret,
            verify_tls=verify_tls,
            request_options=request_options,
        )
        return _response.data

    async def deleteoutboundwebhook(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookDeleteOutboundWebhookResponse:
        """
        Deletes an outbound webhook

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookDeleteOutboundWebhookResponse
            A confirmation message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhook.deleteoutboundwebhook(
                webhook_id="webhook-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteoutboundwebhook(webhook_id, request_options=request_options)
        return _response.data
