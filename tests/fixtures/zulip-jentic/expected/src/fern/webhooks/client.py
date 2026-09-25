

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.zulip_outgoing_webhooks_response import ZulipOutgoingWebhooksResponse


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

    def zulip_outgoing_webhooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ZulipOutgoingWebhooksResponse:
        """
        Outgoing webhooks allow you to build or set up Zulip integrations which are
        notified when certain types of messages are sent in Zulip.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ZulipOutgoingWebhooksResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.webhooks.zulip_outgoing_webhooks()
        """
        _response = self._raw_client.zulip_outgoing_webhooks(request_options=request_options)
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

    async def zulip_outgoing_webhooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ZulipOutgoingWebhooksResponse:
        """
        Outgoing webhooks allow you to build or set up Zulip integrations which are
        notified when certain types of messages are sent in Zulip.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ZulipOutgoingWebhooksResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.webhooks.zulip_outgoing_webhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.zulip_outgoing_webhooks(request_options=request_options)
        return _response.data
