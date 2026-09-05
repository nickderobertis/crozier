

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_delete_webhooks_id import EndpointDeleteWebhooksId
from ..types.endpoint_get_webhooks import EndpointGetWebhooks
from ..types.endpoint_post_webhooks import EndpointPostWebhooks
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.post_webhooks_request_event import PostWebhooksRequestEvent


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

    def get_webhooks(self, *, request_options: typing.Optional[RequestOptions] = None) -> EndpointGetWebhooks:
        """
        Fetch a listing of all webhooks owned by the current user/bubble combination.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetWebhooks
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.get_webhooks()
        """
        _response = self._raw_client.get_webhooks(request_options=request_options)
        return _response.data

    def post_webhooks(
        self,
        *,
        event: PostWebhooksRequestEvent,
        name: str,
        uri: str,
        bubbled: typing.Optional[bool] = OMIT,
        object_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostWebhooks:
        """
        Register a new webhook for the current user/bubble combination. Specify an object_id to only be notified on an event related to that specific Conversation ID, Group ID, or User ID. Your access token must have access to the user being tracked, user you are in the conversation with, or user who created the group. You must be connected with a user in order to keep track of their online status. Alternatively, do not specify an object_id to be notified on all events that are related to conversations you're in, groups you're a member of, or users you are in conversations with. You may only have one webhook for each object_id/event. The webhook URI must reside on your own server. Webhooks do not expire when the access token used to create them expires. However, they will temporarily cease to function if the user who created them deauthorizes access to the application (effectively no longer existing within the bubble), unless/until the user reauthorizes the application using OAuth.

        Parameters
        ----------
        event : PostWebhooksRequestEvent

        name : str

        uri : str

        bubbled : typing.Optional[bool]

        object_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostWebhooks
            Valid Response

        Examples
        --------
        from fern.webhooks import PostWebhooksRequestEvent

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.post_webhooks(
            event=PostWebhooksRequestEvent.CONVERSATION_MESSAGE,
            name="name",
            uri="uri",
        )
        """
        _response = self._raw_client.post_webhooks(
            event=event, name=name, uri=uri, bubbled=bubbled, object_id=object_id, request_options=request_options
        )
        return _response.data

    def delete_webhooks_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointDeleteWebhooksId:
        """
        Delete a webhook that was previously registered by the current user/bubble combination.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointDeleteWebhooksId
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhooks.delete_webhooks_id(
            id=1,
        )
        """
        _response = self._raw_client.delete_webhooks_id(id, request_options=request_options)
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

    async def get_webhooks(self, *, request_options: typing.Optional[RequestOptions] = None) -> EndpointGetWebhooks:
        """
        Fetch a listing of all webhooks owned by the current user/bubble combination.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetWebhooks
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.get_webhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhooks(request_options=request_options)
        return _response.data

    async def post_webhooks(
        self,
        *,
        event: PostWebhooksRequestEvent,
        name: str,
        uri: str,
        bubbled: typing.Optional[bool] = OMIT,
        object_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostWebhooks:
        """
        Register a new webhook for the current user/bubble combination. Specify an object_id to only be notified on an event related to that specific Conversation ID, Group ID, or User ID. Your access token must have access to the user being tracked, user you are in the conversation with, or user who created the group. You must be connected with a user in order to keep track of their online status. Alternatively, do not specify an object_id to be notified on all events that are related to conversations you're in, groups you're a member of, or users you are in conversations with. You may only have one webhook for each object_id/event. The webhook URI must reside on your own server. Webhooks do not expire when the access token used to create them expires. However, they will temporarily cease to function if the user who created them deauthorizes access to the application (effectively no longer existing within the bubble), unless/until the user reauthorizes the application using OAuth.

        Parameters
        ----------
        event : PostWebhooksRequestEvent

        name : str

        uri : str

        bubbled : typing.Optional[bool]

        object_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostWebhooks
            Valid Response

        Examples
        --------
        import asyncio

        from fern.webhooks import PostWebhooksRequestEvent

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.post_webhooks(
                event=PostWebhooksRequestEvent.CONVERSATION_MESSAGE,
                name="name",
                uri="uri",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_webhooks(
            event=event, name=name, uri=uri, bubbled=bubbled, object_id=object_id, request_options=request_options
        )
        return _response.data

    async def delete_webhooks_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointDeleteWebhooksId:
        """
        Delete a webhook that was previously registered by the current user/bubble combination.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointDeleteWebhooksId
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.delete_webhooks_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhooks_id(id, request_options=request_options)
        return _response.data
