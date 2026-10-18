

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawA2AClient, RawA2AClient
from .types.post_a2a_request_jsonrpc import PostA2ARequestJsonrpc
from .types.post_a2a_request_method import PostA2ARequestMethod
from .types.post_a2a_request_params import PostA2ARequestParams
from .types.post_a2a_response import PostA2AResponse


OMIT = typing.cast(typing.Any, ...)


class A2AClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawA2AClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawA2AClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawA2AClient
        """
        return self._raw_client

    def post_a2a(
        self,
        assistant_id: str,
        *,
        accept: str,
        jsonrpc: PostA2ARequestJsonrpc,
        id: str,
        method: PostA2ARequestMethod,
        params: typing.Optional[PostA2ARequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostA2AResponse:
        """
        Communicate with an assistant using the Agent-to-Agent (A2A) Protocol over JSON-RPC 2.0.
        This endpoint accepts a JSON-RPC envelope and dispatches based on `method`.

        **Supported Methods:**
        - `message/send`: Send a message and wait for the final Task result.
        - `message/stream`: Send a message and receive Server-Sent Events (SSE) JSON-RPC responses.
        - `tasks/get`: Fetch the current state of a Task by ID.
        - `tasks/cancel`: Request cancellation (currently not supported; returns an error).

        **LangGraph Mapping:**
        - `message.contextId` maps to LangGraph `thread_id`.

        **Notes:**
        - Only `text` and `data` parts are supported; `file` parts are not.
        - If `message.contextId` is omitted, a new context is created.
        - Text parts require the assistant input schema to include a `messages` field.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to communicate with

        accept : str
            For `message/stream`, must include `text/event-stream`. For all other methods, use `application/json`.

        jsonrpc : PostA2ARequestJsonrpc
            JSON-RPC version

        id : str
            Request identifier

        method : PostA2ARequestMethod
            The method to invoke

        params : typing.Optional[PostA2ARequestParams]
            Method parameters; shape depends on the method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostA2AResponse
            JSON-RPC response for non-streaming methods. For `message/stream`, the response is an SSE stream of JSON-RPC envelopes.

        Examples
        --------
        from fern.a2a import (
            PostA2ARequestParamsMessage,
            PostA2ARequestParamsMessageMessage,
            PostA2ARequestParamsMessageMessagePartsItem_Data,
            PostA2ARequestParamsMessageMessagePartsItem_Text,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.a2a.post_a2a(
            assistant_id="assistant_id",
            accept="Accept",
            jsonrpc="2.0",
            id="1",
            method="message/send",
            params=PostA2ARequestParamsMessage(
                message=PostA2ARequestParamsMessageMessage(
                    role="user",
                    parts=[
                        PostA2ARequestParamsMessageMessagePartsItem_Text(
                            text="Hello from A2A",
                        ),
                        PostA2ARequestParamsMessageMessagePartsItem_Data(
                            data={"locale": "en-US"},
                        ),
                    ],
                    message_id="msg-1",
                    context_id="f5bd2a40-74b6-4f7a-b649-ea3f09890003",
                ),
            ),
        )
        """
        _response = self._raw_client.post_a2a(
            assistant_id,
            accept=accept,
            jsonrpc=jsonrpc,
            id=id,
            method=method,
            params=params,
            request_options=request_options,
        )
        return _response.data


class AsyncA2AClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawA2AClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawA2AClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawA2AClient
        """
        return self._raw_client

    async def post_a2a(
        self,
        assistant_id: str,
        *,
        accept: str,
        jsonrpc: PostA2ARequestJsonrpc,
        id: str,
        method: PostA2ARequestMethod,
        params: typing.Optional[PostA2ARequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostA2AResponse:
        """
        Communicate with an assistant using the Agent-to-Agent (A2A) Protocol over JSON-RPC 2.0.
        This endpoint accepts a JSON-RPC envelope and dispatches based on `method`.

        **Supported Methods:**
        - `message/send`: Send a message and wait for the final Task result.
        - `message/stream`: Send a message and receive Server-Sent Events (SSE) JSON-RPC responses.
        - `tasks/get`: Fetch the current state of a Task by ID.
        - `tasks/cancel`: Request cancellation (currently not supported; returns an error).

        **LangGraph Mapping:**
        - `message.contextId` maps to LangGraph `thread_id`.

        **Notes:**
        - Only `text` and `data` parts are supported; `file` parts are not.
        - If `message.contextId` is omitted, a new context is created.
        - Text parts require the assistant input schema to include a `messages` field.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to communicate with

        accept : str
            For `message/stream`, must include `text/event-stream`. For all other methods, use `application/json`.

        jsonrpc : PostA2ARequestJsonrpc
            JSON-RPC version

        id : str
            Request identifier

        method : PostA2ARequestMethod
            The method to invoke

        params : typing.Optional[PostA2ARequestParams]
            Method parameters; shape depends on the method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostA2AResponse
            JSON-RPC response for non-streaming methods. For `message/stream`, the response is an SSE stream of JSON-RPC envelopes.

        Examples
        --------
        import asyncio

        from fern.a2a import (
            PostA2ARequestParamsMessage,
            PostA2ARequestParamsMessageMessage,
            PostA2ARequestParamsMessageMessagePartsItem_Data,
            PostA2ARequestParamsMessageMessagePartsItem_Text,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.a2a.post_a2a(
                assistant_id="assistant_id",
                accept="Accept",
                jsonrpc="2.0",
                id="1",
                method="message/send",
                params=PostA2ARequestParamsMessage(
                    message=PostA2ARequestParamsMessageMessage(
                        role="user",
                        parts=[
                            PostA2ARequestParamsMessageMessagePartsItem_Text(
                                text="Hello from A2A",
                            ),
                            PostA2ARequestParamsMessageMessagePartsItem_Data(
                                data={"locale": "en-US"},
                            ),
                        ],
                        message_id="msg-1",
                        context_id="f5bd2a40-74b6-4f7a-b649-ea3f09890003",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_a2a(
            assistant_id,
            accept=accept,
            jsonrpc=jsonrpc,
            id=id,
            method=method,
            params=params,
            request_options=request_options,
        )
        return _response.data
