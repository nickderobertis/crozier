

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.webhook_event_type_value import WebhookEventTypeValue
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.create_a_webhook_response import CreateAWebhookResponse
from .types.delete_a_webhook_response import DeleteAWebhookResponse
from .types.list_all_webhooks_response import ListAllWebhooksResponse
from .types.retrieve_a_webhook_response import RetrieveAWebhookResponse
from .types.update_a_webhook_response import UpdateAWebhookResponse


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

    def list_all_webhooks(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllWebhooksResponse:
        """
        View all webhooks associated with a specific company with filtering available via query parameters

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllWebhooksResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.list_all_webhooks()
        """
        _response = self._raw_client.list_all_webhooks(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def create_a_webhook(
        self,
        *,
        events: typing.Sequence[WebhookEventTypeValue],
        target_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAWebhookResponse:
        """
        Creates a webhook for the specified events. Send separate requests if you need to create webhooks for multiple target URLs. Each target URL may only have one active registration.

        Parameters
        ----------
        events : typing.Sequence[WebhookEventTypeValue]
            The event type(s) to trigger the webhook. Note: you can use `*` to receive events for all events, although we don't recommend this path, especially for environments with higher volume.

        target_url : str
            The URL to send the webhook event payload to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAWebhookResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.create_a_webhook(
            events=["*"],
            target_url="targetURL",
        )
        """
        _response = self._raw_client.create_a_webhook(
            events=events, target_url=target_url, request_options=request_options
        )
        return _response.data

    def retrieve_a_webhook(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveAWebhookResponse:
        """
        View the data associated with a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveAWebhookResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.retrieve_a_webhook(
            id="id",
        )
        """
        _response = self._raw_client.retrieve_a_webhook(id, request_options=request_options)
        return _response.data

    def delete_a_webhook(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAWebhookResponse:
        """
        Delete a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAWebhookResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.delete_a_webhook(
            id="id",
        )
        """
        _response = self._raw_client.delete_a_webhook(id, request_options=request_options)
        return _response.data

    def update_a_webhook(
        self,
        id: str,
        *,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        target_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAWebhookResponse:
        """
        Update the data associated with a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        events : typing.Optional[typing.Sequence[str]]
            The type of events that will trigger a notification to the target URL.

        target_url : typing.Optional[str]
            The URL of where the notification gets sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAWebhookResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.update_a_webhook(
            id="id",
        )
        """
        _response = self._raw_client.update_a_webhook(
            id, events=events, target_url=target_url, request_options=request_options
        )
        return _response.data

    def retrieve_webhook_verification_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        View the verification key for webhook security implementations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.retrieve_webhook_verification_key()
        """
        _response = self._raw_client.retrieve_webhook_verification_key(request_options=request_options)
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

    async def list_all_webhooks(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllWebhooksResponse:
        """
        View all webhooks associated with a specific company with filtering available via query parameters

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllWebhooksResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.list_all_webhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_webhooks(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_a_webhook(
        self,
        *,
        events: typing.Sequence[WebhookEventTypeValue],
        target_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAWebhookResponse:
        """
        Creates a webhook for the specified events. Send separate requests if you need to create webhooks for multiple target URLs. Each target URL may only have one active registration.

        Parameters
        ----------
        events : typing.Sequence[WebhookEventTypeValue]
            The event type(s) to trigger the webhook. Note: you can use `*` to receive events for all events, although we don't recommend this path, especially for environments with higher volume.

        target_url : str
            The URL to send the webhook event payload to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAWebhookResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.create_a_webhook(
                events=["*"],
                target_url="targetURL",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_webhook(
            events=events, target_url=target_url, request_options=request_options
        )
        return _response.data

    async def retrieve_a_webhook(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveAWebhookResponse:
        """
        View the data associated with a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveAWebhookResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.retrieve_a_webhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_webhook(id, request_options=request_options)
        return _response.data

    async def delete_a_webhook(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAWebhookResponse:
        """
        Delete a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAWebhookResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.delete_a_webhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_webhook(id, request_options=request_options)
        return _response.data

    async def update_a_webhook(
        self,
        id: str,
        *,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        target_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAWebhookResponse:
        """
        Update the data associated with a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        events : typing.Optional[typing.Sequence[str]]
            The type of events that will trigger a notification to the target URL.

        target_url : typing.Optional[str]
            The URL of where the notification gets sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAWebhookResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.update_a_webhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_webhook(
            id, events=events, target_url=target_url, request_options=request_options
        )
        return _response.data

    async def retrieve_webhook_verification_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        View the verification key for webhook security implementations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.retrieve_webhook_verification_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_webhook_verification_key(request_options=request_options)
        return _response.data
