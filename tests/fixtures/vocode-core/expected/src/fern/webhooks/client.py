

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_type import EventType
from ..types.http_method import HttpMethod
from ..types.webhook import Webhook
from ..types.webhook_page import WebhookPage
from ..types.webhook_update_params_method import WebhookUpdateParamsMethod
from ..types.webhook_update_params_subscriptions import WebhookUpdateParamsSubscriptions
from ..types.webhook_update_params_url import WebhookUpdateParamsUrl
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient


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

    def get_webhook(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.get_webhook(
            id="id",
        )
        """
        _response = self._raw_client.get_webhook(id=id, request_options=request_options)
        return _response.data

    def list_webhooks(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookPage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.list_webhooks()
        """
        _response = self._raw_client.list_webhooks(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    def create_webhook(
        self,
        *,
        subscriptions: typing.Sequence[EventType],
        url: str,
        method: typing.Optional[HttpMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Parameters
        ----------
        subscriptions : typing.Sequence[EventType]

        url : str

        method : typing.Optional[HttpMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Successful Response

        Examples
        --------
        from fern import EventType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.create_webhook(
            subscriptions=[EventType.EVENT_MESSAGE],
            url="url",
        )
        """
        _response = self._raw_client.create_webhook(
            subscriptions=subscriptions, url=url, method=method, request_options=request_options
        )
        return _response.data

    def update_webhook(
        self,
        *,
        id: str,
        subscriptions: typing.Optional[WebhookUpdateParamsSubscriptions] = OMIT,
        url: typing.Optional[WebhookUpdateParamsUrl] = OMIT,
        method: typing.Optional[WebhookUpdateParamsMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Parameters
        ----------
        id : str

        subscriptions : typing.Optional[WebhookUpdateParamsSubscriptions]

        url : typing.Optional[WebhookUpdateParamsUrl]

        method : typing.Optional[WebhookUpdateParamsMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.update_webhook(
            id="id",
        )
        """
        _response = self._raw_client.update_webhook(
            id=id, subscriptions=subscriptions, url=url, method=method, request_options=request_options
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

    async def get_webhook(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.get_webhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhook(id=id, request_options=request_options)
        return _response.data

    async def list_webhooks(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookPage
            Successful Response

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
        _response = await self._raw_client.list_webhooks(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    async def create_webhook(
        self,
        *,
        subscriptions: typing.Sequence[EventType],
        url: str,
        method: typing.Optional[HttpMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Parameters
        ----------
        subscriptions : typing.Sequence[EventType]

        url : str

        method : typing.Optional[HttpMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EventType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.create_webhook(
                subscriptions=[EventType.EVENT_MESSAGE],
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook(
            subscriptions=subscriptions, url=url, method=method, request_options=request_options
        )
        return _response.data

    async def update_webhook(
        self,
        *,
        id: str,
        subscriptions: typing.Optional[WebhookUpdateParamsSubscriptions] = OMIT,
        url: typing.Optional[WebhookUpdateParamsUrl] = OMIT,
        method: typing.Optional[WebhookUpdateParamsMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Parameters
        ----------
        id : str

        subscriptions : typing.Optional[WebhookUpdateParamsSubscriptions]

        url : typing.Optional[WebhookUpdateParamsUrl]

        method : typing.Optional[WebhookUpdateParamsMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.update_webhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook(
            id=id, subscriptions=subscriptions, url=url, method=method, request_options=request_options
        )
        return _response.data
