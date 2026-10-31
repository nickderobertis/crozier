

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.conversation import Conversation
from ..types.model_alias import ModelAlias
from ..types.stream_event import StreamEvent
from .raw_client import AsyncRawConversationsClient, RawConversationsClient


OMIT = typing.cast(typing.Any, ...)


class ConversationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConversationsClient
        """
        return self._raw_client

    def llm_create_conversation(
        self, *, model: typing.Optional[ModelAlias] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Conversation:
        """
        Creates an empty conversation for the caller in the org of the token.

        Parameters
        ----------
        model : typing.Optional[ModelAlias]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            Conversation created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.conversations.llm_create_conversation(
            model="default",
        )
        """
        _response = self._raw_client.llm_create_conversation(model=model, request_options=request_options)
        return _response.data

    def llm_get_conversation(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Conversation:
        """
        The conversation with its messages, oldest first.
        An unknown id and another owner's id both answer 404 with the same body.

        Parameters
        ----------
        id : str
            Conversation id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            The conversation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.conversations.llm_get_conversation(
            id="id",
        )
        """
        _response = self._raw_client.llm_get_conversation(id, request_options=request_options)
        return _response.data

    def llm_send_message(
        self,
        id: str,
        *,
        content: str,
        model: typing.Optional[ModelAlias] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[StreamEvent]:
        """
        Stores the user message and streams the assistant answer as Server-Sent Events.
        - Refusals before the first byte answer with a status code and `application/problem+json`.
        - After the first byte the status stays 200. A failure is an `error` event, then the stream ends.
        - Order of events: zero or more `delta`, then `usage`, then `done`. Or an `error` event at any point.
        - Cancel: the client closes the connection. The server stops the model call and keeps the partial answer.
        - Headers: `Cache-Control: no-store`, `X-Accel-Buffering: no`. A comment line (`: ping`) every 15 s keeps the connection open.

        Parameters
        ----------
        id : str
            Conversation id.

        content : str
            The user message. Plain text. Above the server limit the answer is 413.

        model : typing.Optional[ModelAlias]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[StreamEvent]
            The answer as a `text/event-stream`. Each frame is one `StreamEvent`:
            the SSE `event:` field holds `event`, the `data:` field holds `data` as one line of JSON,
            and the `id:` field holds `<message_id>:<sequence>`. On the wire:

            ```text
            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:1
            event: delta
            data: {"text":"Pulse reads "}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:2
            event: delta
            data: {"text":"/readyz of every service."}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:3
            event: usage
            data: {"input_tokens":412,"output_tokens":9,"model":"default"}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:4
            event: done
            data: {"message_id":"0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10","finish_reason":"stop"}
            ```

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.conversations.llm_send_message(
            id="id",
            content="What does pulse check?",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.llm_send_message(id, content=content, model=model, request_options=request_options) as r:
            yield from r.data


class AsyncConversationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConversationsClient
        """
        return self._raw_client

    async def llm_create_conversation(
        self, *, model: typing.Optional[ModelAlias] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Conversation:
        """
        Creates an empty conversation for the caller in the org of the token.

        Parameters
        ----------
        model : typing.Optional[ModelAlias]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            Conversation created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.conversations.llm_create_conversation(
                model="default",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.llm_create_conversation(model=model, request_options=request_options)
        return _response.data

    async def llm_get_conversation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Conversation:
        """
        The conversation with its messages, oldest first.
        An unknown id and another owner's id both answer 404 with the same body.

        Parameters
        ----------
        id : str
            Conversation id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            The conversation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.conversations.llm_get_conversation(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.llm_get_conversation(id, request_options=request_options)
        return _response.data

    async def llm_send_message(
        self,
        id: str,
        *,
        content: str,
        model: typing.Optional[ModelAlias] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[StreamEvent]:
        """
        Stores the user message and streams the assistant answer as Server-Sent Events.
        - Refusals before the first byte answer with a status code and `application/problem+json`.
        - After the first byte the status stays 200. A failure is an `error` event, then the stream ends.
        - Order of events: zero or more `delta`, then `usage`, then `done`. Or an `error` event at any point.
        - Cancel: the client closes the connection. The server stops the model call and keeps the partial answer.
        - Headers: `Cache-Control: no-store`, `X-Accel-Buffering: no`. A comment line (`: ping`) every 15 s keeps the connection open.

        Parameters
        ----------
        id : str
            Conversation id.

        content : str
            The user message. Plain text. Above the server limit the answer is 413.

        model : typing.Optional[ModelAlias]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[StreamEvent]
            The answer as a `text/event-stream`. Each frame is one `StreamEvent`:
            the SSE `event:` field holds `event`, the `data:` field holds `data` as one line of JSON,
            and the `id:` field holds `<message_id>:<sequence>`. On the wire:

            ```text
            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:1
            event: delta
            data: {"text":"Pulse reads "}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:2
            event: delta
            data: {"text":"/readyz of every service."}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:3
            event: usage
            data: {"input_tokens":412,"output_tokens":9,"model":"default"}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:4
            event: done
            data: {"message_id":"0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10","finish_reason":"stop"}
            ```

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = client.conversations.llm_send_message(
                id="id",
                content="What does pulse check?",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.llm_send_message(
            id, content=content, model=model, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
