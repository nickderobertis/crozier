

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient


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

    def push(self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Receives a raw Stripe webhook event, verifies its signature using the pipeline's webhook secret, and enqueues it for processing by the active pipeline.

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Event accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.webhooks.push(
            pipeline_id="pipeline_id",
        )
        """
        _response = self._raw_client.push(pipeline_id, request_options=request_options)
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

    async def push(self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Receives a raw Stripe webhook event, verifies its signature using the pipeline's webhook secret, and enqueues it for processing by the active pipeline.

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Event accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.webhooks.push(
                pipeline_id="pipeline_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.push(pipeline_id, request_options=request_options)
        return _response.data
