

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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

    def configure_webhooks(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Configure webhook endpoints for event notifications.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Configure webhooks successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.configure_webhooks(
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.configure_webhooks(request=request, request_options=request_options)
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

    async def configure_webhooks(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Configure webhook endpoints for event notifications.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Configure webhooks successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.configure_webhooks(
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.configure_webhooks(request=request, request_options=request_options)
        return _response.data
