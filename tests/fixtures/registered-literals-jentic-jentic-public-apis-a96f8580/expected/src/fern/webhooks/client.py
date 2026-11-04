

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.webhook_event_type_value import WebhookEventTypeValue
from ..types.webhooks_create_new_response import WebhooksCreateNewResponse
from ..types.webhooks_delete_specific_response import WebhooksDeleteSpecificResponse
from ..types.webhooks_get_data_response import WebhooksGetDataResponse
from ..types.webhooks_list_all_response import WebhooksListAllResponse
from ..types.webhooks_update_webhook_data_response import WebhooksUpdateWebhookDataResponse
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

    def listall(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhooksListAllResponse:
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
        WebhooksListAllResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.listall()
        """
        _response = self._raw_client.listall(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def createnew(
        self,
        *,
        events: typing.Sequence[WebhookEventTypeValue],
        target_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhooksCreateNewResponse:
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
        WebhooksCreateNewResponse
            200

        Examples
        --------
        from fern import FernApi, WebhookEventTypeValue

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.createnew(
            events=[WebhookEventTypeValue.ALL],
            target_url="targetURL",
        )
        """
        _response = self._raw_client.createnew(events=events, target_url=target_url, request_options=request_options)
        return _response.data

    def getdata(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WebhooksGetDataResponse:
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
        WebhooksGetDataResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.getdata(
            id="id",
        )
        """
        _response = self._raw_client.getdata(id, request_options=request_options)
        return _response.data

    def deletespecific(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhooksDeleteSpecificResponse:
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
        WebhooksDeleteSpecificResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.deletespecific(
            id="id",
        )
        """
        _response = self._raw_client.deletespecific(id, request_options=request_options)
        return _response.data

    def updatewebhookdata(
        self,
        id: str,
        *,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        target_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhooksUpdateWebhookDataResponse:
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
        WebhooksUpdateWebhookDataResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.updatewebhookdata(
            id="id",
        )
        """
        _response = self._raw_client.updatewebhookdata(
            id, events=events, target_url=target_url, request_options=request_options
        )
        return _response.data

    def getverificationkey(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
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
        client.webhooks.getverificationkey()
        """
        _response = self._raw_client.getverificationkey(request_options=request_options)
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

    async def listall(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhooksListAllResponse:
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
        WebhooksListAllResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.listall()


        asyncio.run(main())
        """
        _response = await self._raw_client.listall(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    async def createnew(
        self,
        *,
        events: typing.Sequence[WebhookEventTypeValue],
        target_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhooksCreateNewResponse:
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
        WebhooksCreateNewResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WebhookEventTypeValue

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.createnew(
                events=[WebhookEventTypeValue.ALL],
                target_url="targetURL",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createnew(
            events=events, target_url=target_url, request_options=request_options
        )
        return _response.data

    async def getdata(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhooksGetDataResponse:
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
        WebhooksGetDataResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.getdata(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getdata(id, request_options=request_options)
        return _response.data

    async def deletespecific(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhooksDeleteSpecificResponse:
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
        WebhooksDeleteSpecificResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.deletespecific(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletespecific(id, request_options=request_options)
        return _response.data

    async def updatewebhookdata(
        self,
        id: str,
        *,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        target_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhooksUpdateWebhookDataResponse:
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
        WebhooksUpdateWebhookDataResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.updatewebhookdata(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatewebhookdata(
            id, events=events, target_url=target_url, request_options=request_options
        )
        return _response.data

    async def getverificationkey(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
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
            await client.webhooks.getverificationkey()


        asyncio.run(main())
        """
        _response = await self._raw_client.getverificationkey(request_options=request_options)
        return _response.data
