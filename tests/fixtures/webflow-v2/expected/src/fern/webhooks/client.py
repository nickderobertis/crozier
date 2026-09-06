

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.create_webhooks_request_filter import CreateWebhooksRequestFilter
from .types.create_webhooks_request_trigger_type import CreateWebhooksRequestTriggerType
from .types.create_webhooks_response import CreateWebhooksResponse
from .types.get_webhooks_response import GetWebhooksResponse
from .types.list_webhooks_response import ListWebhooksResponse


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

    def list(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ListWebhooksResponse:
        """
        List all App-created Webhooks registered for a given site

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhooksResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.list(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list(site_id, request_options=request_options)
        return _response.data

    def create(
        self,
        site_id: str,
        *,
        trigger_type: typing.Optional[CreateWebhooksRequestTriggerType] = OMIT,
        url: typing.Optional[str] = OMIT,
        filter: typing.Optional[CreateWebhooksRequestFilter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhooksResponse:
        """
        Create a new Webhook.

        Limit of 75 registrations per `triggerType`, per site.

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/data-clients/getting-started).</Note>
        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        trigger_type : typing.Optional[CreateWebhooksRequestTriggerType]
            The type of event that triggered the request. See the the documentation for details on [supported events](/data/reference/all-events).

        url : typing.Optional[str]
            URL to send the Webhook payload to

        filter : typing.Optional[CreateWebhooksRequestFilter]
            Only supported for the `form_submission` trigger type. Filter for the form you want Webhooks to be sent for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhooksResponse
            Request was successful

        Examples
        --------
        from fern.webhooks import CreateWebhooksRequestTriggerType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.create(
            site_id="580e63e98c9a982ac9b8b741",
            trigger_type=CreateWebhooksRequestTriggerType.FORM_SUBMISSION,
            url="https://webhook.site/7f7f7f7f-7f7f-7f7f-7f7f-7f7f7f7f7f7f",
        )
        """
        _response = self._raw_client.create(
            site_id, trigger_type=trigger_type, url=url, filter=filter, request_options=request_options
        )
        return _response.data

    def get(self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetWebhooksResponse:
        """
        Get a specific Webhook instance

        Required scope: `sites:read`

        Parameters
        ----------
        webhook_id : str
            Unique identifier for a Webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.get(
            webhook_id="580e64008c9a982ac9b8b754",
        )
        """
        _response = self._raw_client.get(webhook_id, request_options=request_options)
        return _response.data

    def delete(self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove a Webhook

        Required scope: `sites:read`

        Parameters
        ----------
        webhook_id : str
            Unique identifier for a Webhook

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
        client.webhooks.delete(
            webhook_id="580e64008c9a982ac9b8b754",
        )
        """
        _response = self._raw_client.delete(webhook_id, request_options=request_options)
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

    async def list(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListWebhooksResponse:
        """
        List all App-created Webhooks registered for a given site

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhooksResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.list(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(site_id, request_options=request_options)
        return _response.data

    async def create(
        self,
        site_id: str,
        *,
        trigger_type: typing.Optional[CreateWebhooksRequestTriggerType] = OMIT,
        url: typing.Optional[str] = OMIT,
        filter: typing.Optional[CreateWebhooksRequestFilter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhooksResponse:
        """
        Create a new Webhook.

        Limit of 75 registrations per `triggerType`, per site.

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/data-clients/getting-started).</Note>
        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        trigger_type : typing.Optional[CreateWebhooksRequestTriggerType]
            The type of event that triggered the request. See the the documentation for details on [supported events](/data/reference/all-events).

        url : typing.Optional[str]
            URL to send the Webhook payload to

        filter : typing.Optional[CreateWebhooksRequestFilter]
            Only supported for the `form_submission` trigger type. Filter for the form you want Webhooks to be sent for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhooksResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.webhooks import CreateWebhooksRequestTriggerType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.create(
                site_id="580e63e98c9a982ac9b8b741",
                trigger_type=CreateWebhooksRequestTriggerType.FORM_SUBMISSION,
                url="https://webhook.site/7f7f7f7f-7f7f-7f7f-7f7f-7f7f7f7f7f7f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            site_id, trigger_type=trigger_type, url=url, filter=filter, request_options=request_options
        )
        return _response.data

    async def get(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhooksResponse:
        """
        Get a specific Webhook instance

        Required scope: `sites:read`

        Parameters
        ----------
        webhook_id : str
            Unique identifier for a Webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.get(
                webhook_id="580e64008c9a982ac9b8b754",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(webhook_id, request_options=request_options)
        return _response.data

    async def delete(self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove a Webhook

        Required scope: `sites:read`

        Parameters
        ----------
        webhook_id : str
            Unique identifier for a Webhook

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
            await client.webhooks.delete(
                webhook_id="580e64008c9a982ac9b8b754",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(webhook_id, request_options=request_options)
        return _response.data
