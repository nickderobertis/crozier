

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebhookEventsClient, RawWebhookEventsClient


class WebhookEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebhookEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebhookEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebhookEventsClient
        """
        return self._raw_client

    def webhook_event_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        This is a documentation-only endpoint describing the webhook event payloads.

        When you subscribe to webhook events, Timely will send HTTP POST requests to your configured URL with the following payloads:

        | Event | Payload Schema |
        |-------|----------------|
        | `hours:created` | Hour |
        | `hours:updated` | Hour |
        | `hours:deleted` | Hour |
        | `projects:created` | Project |
        | `projects:updated` | Project |
        | `projects:deleted` | Project |
        | `labels:created` | Label |
        | `labels:updated` | Label |
        | `labels:deleted` | Label |
        | `forecasts:created` | Forecast |
        | `forecasts:updated` | Forecast |
        | `forecasts:deleted` | Forecast |

        See the webhook events below for the exact payload schemas.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhook_events.webhook_event_types()
        """
        _response = self._raw_client.webhook_event_types(request_options=request_options)
        return _response.data


class AsyncWebhookEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebhookEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebhookEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebhookEventsClient
        """
        return self._raw_client

    async def webhook_event_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        This is a documentation-only endpoint describing the webhook event payloads.

        When you subscribe to webhook events, Timely will send HTTP POST requests to your configured URL with the following payloads:

        | Event | Payload Schema |
        |-------|----------------|
        | `hours:created` | Hour |
        | `hours:updated` | Hour |
        | `hours:deleted` | Hour |
        | `projects:created` | Project |
        | `projects:updated` | Project |
        | `projects:deleted` | Project |
        | `labels:created` | Label |
        | `labels:updated` | Label |
        | `labels:deleted` | Label |
        | `forecasts:created` | Forecast |
        | `forecasts:updated` | Forecast |
        | `forecasts:deleted` | Forecast |

        See the webhook events below for the exact payload schemas.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhook_events.webhook_event_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.webhook_event_types(request_options=request_options)
        return _response.data
