

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.queue_presentation import QueuePresentation
from .raw_client import AsyncRawMessagingClient, RawMessagingClient


OMIT = typing.cast(typing.Any, ...)


class MessagingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMessagingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMessagingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMessagingClient
        """
        return self._raw_client

    def get_default_queue(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueuePresentation:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueuePresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.messaging.get_default_queue(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_default_queue(organization_id, request_options=request_options)
        return _response.data

    def patch_default_queue(
        self,
        organization_id: str,
        *,
        active: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        purge_queue: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        active : typing.Optional[bool]
            If this value is set to false the queue will be deleted.

        id : typing.Optional[str]

        purge_queue : typing.Optional[bool]
            Set this value to true if you want to purge the queue.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.messaging.patch_default_queue(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.patch_default_queue(
            organization_id, active=active, id=id, purge_queue=purge_queue, request_options=request_options
        )
        return _response.data

    def enqueue_custom_message(
        self,
        organization_id: str,
        *,
        data: typing.Dict[str, str],
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Enqueue a custom organisation message with custom data.

        Parameters
        ----------
        organization_id : str
            The organisation namespace

        data : typing.Dict[str, str]
            Custom data in a map. You may use JSON content

        name : str
            The name of the message (organisation specific)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.messaging.enqueue_custom_message(
            organization_id="organizationId",
            data={"key": "value"},
            name="<event name>",
        )
        """
        _response = self._raw_client.enqueue_custom_message(
            organization_id, data=data, name=name, request_options=request_options
        )
        return _response.data


class AsyncMessagingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMessagingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMessagingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMessagingClient
        """
        return self._raw_client

    async def get_default_queue(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueuePresentation:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueuePresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messaging.get_default_queue(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_default_queue(organization_id, request_options=request_options)
        return _response.data

    async def patch_default_queue(
        self,
        organization_id: str,
        *,
        active: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        purge_queue: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        active : typing.Optional[bool]
            If this value is set to false the queue will be deleted.

        id : typing.Optional[str]

        purge_queue : typing.Optional[bool]
            Set this value to true if you want to purge the queue.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messaging.patch_default_queue(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_default_queue(
            organization_id, active=active, id=id, purge_queue=purge_queue, request_options=request_options
        )
        return _response.data

    async def enqueue_custom_message(
        self,
        organization_id: str,
        *,
        data: typing.Dict[str, str],
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Enqueue a custom organisation message with custom data.

        Parameters
        ----------
        organization_id : str
            The organisation namespace

        data : typing.Dict[str, str]
            Custom data in a map. You may use JSON content

        name : str
            The name of the message (organisation specific)

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messaging.enqueue_custom_message(
                organization_id="organizationId",
                data={"key": "value"},
                name="<event name>",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enqueue_custom_message(
            organization_id, data=data, name=name, request_options=request_options
        )
        return _response.data
