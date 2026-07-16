

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.post_webhooks_registrations_request_topic import PostWebhooksRegistrationsRequestTopic


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

    def get_webhook_registrations(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get webhook registrations

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
        client.webhooks.get_webhook_registrations()
        """
        _response = self._raw_client.get_webhook_registrations(request_options=request_options)
        return _response.data

    def register_a_webhook(
        self,
        *,
        topic: PostWebhooksRegistrationsRequestTopic,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Register a webhook

        Parameters
        ----------
        topic : PostWebhooksRegistrationsRequestTopic
            Valid values: listings/update, listings/publish, listings/bumps-ran-out, orders/create, orders/update, payments/create, payments/update, app/uninstalled

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.webhooks import PostWebhooksRegistrationsRequestTopic

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.register_a_webhook(
            topic=PostWebhooksRegistrationsRequestTopic.LISTINGS_UPDATE,
            url="url",
        )
        """
        _response = self._raw_client.register_a_webhook(topic=topic, url=url, request_options=request_options)
        return _response.data

    def get_details_of_a_webhook_registration(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get details of a webhook registration

        Parameters
        ----------
        id : str

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
        client.webhooks.get_details_of_a_webhook_registration(
            id="id",
        )
        """
        _response = self._raw_client.get_details_of_a_webhook_registration(id, request_options=request_options)
        return _response.data

    def remove_a_webhook(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove a webhook

        Parameters
        ----------
        id : str

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
        client.webhooks.remove_a_webhook(
            id="id",
        )
        """
        _response = self._raw_client.remove_a_webhook(id, request_options=request_options)
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

    async def get_webhook_registrations(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get webhook registrations

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
            await client.webhooks.get_webhook_registrations()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhook_registrations(request_options=request_options)
        return _response.data

    async def register_a_webhook(
        self,
        *,
        topic: PostWebhooksRegistrationsRequestTopic,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Register a webhook

        Parameters
        ----------
        topic : PostWebhooksRegistrationsRequestTopic
            Valid values: listings/update, listings/publish, listings/bumps-ran-out, orders/create, orders/update, payments/create, payments/update, app/uninstalled

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.webhooks import PostWebhooksRegistrationsRequestTopic

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.register_a_webhook(
                topic=PostWebhooksRegistrationsRequestTopic.LISTINGS_UPDATE,
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_webhook(topic=topic, url=url, request_options=request_options)
        return _response.data

    async def get_details_of_a_webhook_registration(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get details of a webhook registration

        Parameters
        ----------
        id : str

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
            await client.webhooks.get_details_of_a_webhook_registration(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_details_of_a_webhook_registration(id, request_options=request_options)
        return _response.data

    async def remove_a_webhook(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove a webhook

        Parameters
        ----------
        id : str

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
            await client.webhooks.remove_a_webhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_a_webhook(id, request_options=request_options)
        return _response.data
