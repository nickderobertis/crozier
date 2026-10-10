

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.context_filter import ContextFilter
from ..types.open_ai_completion import OpenAiCompletion
from ..types.open_ai_message import OpenAiMessage
from .raw_client import AsyncRawContextualCompletionsClient, RawContextualCompletionsClient


OMIT = typing.cast(typing.Any, ...)


class ContextualCompletionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContextualCompletionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContextualCompletionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContextualCompletionsClient
        """
        return self._raw_client

    def prompt_completion_v1completions_post_stream(
        self,
        *,
        prompt: str,
        system_prompt: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[OpenAiCompletion]:
        """
        We recommend most users use our Chat completions API.

        Given a prompt, the model will return one predicted completion.

        Optionally include a `system_prompt` to influence the way the LLM answers.

        If `use_context`
        is set to `true`, the model will use context coming from the ingested documents
        to create the response. The documents being used can be filtered using the
        `context_filter` and passing the document IDs to be used. Ingested documents IDs
        can be found using `/ingest/list` endpoint. If you want all ingested documents to
        be used, remove `context_filter` altogether.

        When using `'include_sources': true`, the API will return the source Chunks used
        to create the response, which come from the context provided.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        prompt : str

        system_prompt : typing.Optional[str]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        include_sources : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[OpenAiCompletion]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = (
            client.contextual_completions.prompt_completion_v1completions_post_stream(
                prompt="How do you fry an egg?",
                system_prompt="You are a rapper. Always answer with a rap.",
                use_context=False,
                include_sources=False,
            )
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.prompt_completion_v1completions_post_stream(
            prompt=prompt,
            system_prompt=system_prompt,
            use_context=use_context,
            context_filter=context_filter,
            include_sources=include_sources,
            request_options=request_options,
        ) as r:
            yield from r.data

    def prompt_completion(
        self,
        *,
        prompt: str,
        system_prompt: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAiCompletion:
        """
        We recommend most users use our Chat completions API.

        Given a prompt, the model will return one predicted completion.

        Optionally include a `system_prompt` to influence the way the LLM answers.

        If `use_context`
        is set to `true`, the model will use context coming from the ingested documents
        to create the response. The documents being used can be filtered using the
        `context_filter` and passing the document IDs to be used. Ingested documents IDs
        can be found using `/ingest/list` endpoint. If you want all ingested documents to
        be used, remove `context_filter` altogether.

        When using `'include_sources': true`, the API will return the source Chunks used
        to create the response, which come from the context provided.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        prompt : str

        system_prompt : typing.Optional[str]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        include_sources : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiCompletion


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.contextual_completions.prompt_completion(
            prompt="How do you fry an egg?",
            system_prompt="You are a rapper. Always answer with a rap.",
            use_context=False,
            include_sources=False,
        )
        """
        _response = self._raw_client.prompt_completion(
            prompt=prompt,
            system_prompt=system_prompt,
            use_context=use_context,
            context_filter=context_filter,
            include_sources=include_sources,
            request_options=request_options,
        )
        return _response.data

    def chat_completion_v1chat_completions_post_stream(
        self,
        *,
        messages: typing.Sequence[OpenAiMessage],
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[OpenAiCompletion]:
        """
        Given a list of messages comprising a conversation, return a response.

        Optionally include an initial `role: system` message to influence the way
        the LLM answers.

        If `use_context` is set to `true`, the model will use context coming
        from the ingested documents to create the response. The documents being used can
        be filtered using the `context_filter` and passing the document IDs to be used.
        Ingested documents IDs can be found using `/ingest/list` endpoint. If you want
        all ingested documents to be used, remove `context_filter` altogether.

        When using `'include_sources': true`, the API will return the source Chunks used
        to create the response, which come from the context provided.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        messages : typing.Sequence[OpenAiMessage]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        include_sources : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[OpenAiCompletion]


        Examples
        --------
        from fern import ContextFilter, FernApi, OpenAiMessage

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.contextual_completions.chat_completion_v1chat_completions_post_stream(
            messages=[
                OpenAiMessage(
                    role="system",
                    content="You are a rapper. Always answer with a rap.",
                ),
                OpenAiMessage(
                    role="user",
                    content="How do you fry an egg?",
                ),
            ],
            use_context=True,
            context_filter=ContextFilter(
                docs_ids=["c202d5e6-7b69-4869-81cc-dd574ee8ee11"],
            ),
            include_sources=True,
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.chat_completion_v1chat_completions_post_stream(
            messages=messages,
            use_context=use_context,
            context_filter=context_filter,
            include_sources=include_sources,
            request_options=request_options,
        ) as r:
            yield from r.data

    def chat_completion(
        self,
        *,
        messages: typing.Sequence[OpenAiMessage],
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAiCompletion:
        """
        Given a list of messages comprising a conversation, return a response.

        Optionally include an initial `role: system` message to influence the way
        the LLM answers.

        If `use_context` is set to `true`, the model will use context coming
        from the ingested documents to create the response. The documents being used can
        be filtered using the `context_filter` and passing the document IDs to be used.
        Ingested documents IDs can be found using `/ingest/list` endpoint. If you want
        all ingested documents to be used, remove `context_filter` altogether.

        When using `'include_sources': true`, the API will return the source Chunks used
        to create the response, which come from the context provided.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        messages : typing.Sequence[OpenAiMessage]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        include_sources : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiCompletion


        Examples
        --------
        from fern import ContextFilter, FernApi, OpenAiMessage

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.contextual_completions.chat_completion(
            messages=[
                OpenAiMessage(
                    role="system",
                    content="You are a rapper. Always answer with a rap.",
                ),
                OpenAiMessage(
                    role="user",
                    content="How do you fry an egg?",
                ),
            ],
            use_context=True,
            context_filter=ContextFilter(
                docs_ids=["c202d5e6-7b69-4869-81cc-dd574ee8ee11"],
            ),
            include_sources=True,
        )
        """
        _response = self._raw_client.chat_completion(
            messages=messages,
            use_context=use_context,
            context_filter=context_filter,
            include_sources=include_sources,
            request_options=request_options,
        )
        return _response.data


class AsyncContextualCompletionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContextualCompletionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContextualCompletionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContextualCompletionsClient
        """
        return self._raw_client

    async def prompt_completion_v1completions_post_stream(
        self,
        *,
        prompt: str,
        system_prompt: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[OpenAiCompletion]:
        """
        We recommend most users use our Chat completions API.

        Given a prompt, the model will return one predicted completion.

        Optionally include a `system_prompt` to influence the way the LLM answers.

        If `use_context`
        is set to `true`, the model will use context coming from the ingested documents
        to create the response. The documents being used can be filtered using the
        `context_filter` and passing the document IDs to be used. Ingested documents IDs
        can be found using `/ingest/list` endpoint. If you want all ingested documents to
        be used, remove `context_filter` altogether.

        When using `'include_sources': true`, the API will return the source Chunks used
        to create the response, which come from the context provided.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        prompt : str

        system_prompt : typing.Optional[str]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        include_sources : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[OpenAiCompletion]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.contextual_completions.prompt_completion_v1completions_post_stream(
                prompt="How do you fry an egg?",
                system_prompt="You are a rapper. Always answer with a rap.",
                use_context=False,
                include_sources=False,
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.prompt_completion_v1completions_post_stream(
            prompt=prompt,
            system_prompt=system_prompt,
            use_context=use_context,
            context_filter=context_filter,
            include_sources=include_sources,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def prompt_completion(
        self,
        *,
        prompt: str,
        system_prompt: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAiCompletion:
        """
        We recommend most users use our Chat completions API.

        Given a prompt, the model will return one predicted completion.

        Optionally include a `system_prompt` to influence the way the LLM answers.

        If `use_context`
        is set to `true`, the model will use context coming from the ingested documents
        to create the response. The documents being used can be filtered using the
        `context_filter` and passing the document IDs to be used. Ingested documents IDs
        can be found using `/ingest/list` endpoint. If you want all ingested documents to
        be used, remove `context_filter` altogether.

        When using `'include_sources': true`, the API will return the source Chunks used
        to create the response, which come from the context provided.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        prompt : str

        system_prompt : typing.Optional[str]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        include_sources : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiCompletion


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contextual_completions.prompt_completion(
                prompt="How do you fry an egg?",
                system_prompt="You are a rapper. Always answer with a rap.",
                use_context=False,
                include_sources=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prompt_completion(
            prompt=prompt,
            system_prompt=system_prompt,
            use_context=use_context,
            context_filter=context_filter,
            include_sources=include_sources,
            request_options=request_options,
        )
        return _response.data

    async def chat_completion_v1chat_completions_post_stream(
        self,
        *,
        messages: typing.Sequence[OpenAiMessage],
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[OpenAiCompletion]:
        """
        Given a list of messages comprising a conversation, return a response.

        Optionally include an initial `role: system` message to influence the way
        the LLM answers.

        If `use_context` is set to `true`, the model will use context coming
        from the ingested documents to create the response. The documents being used can
        be filtered using the `context_filter` and passing the document IDs to be used.
        Ingested documents IDs can be found using `/ingest/list` endpoint. If you want
        all ingested documents to be used, remove `context_filter` altogether.

        When using `'include_sources': true`, the API will return the source Chunks used
        to create the response, which come from the context provided.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        messages : typing.Sequence[OpenAiMessage]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        include_sources : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[OpenAiCompletion]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ContextFilter, OpenAiMessage

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.contextual_completions.chat_completion_v1chat_completions_post_stream(
                messages=[
                    OpenAiMessage(
                        role="system",
                        content="You are a rapper. Always answer with a rap.",
                    ),
                    OpenAiMessage(
                        role="user",
                        content="How do you fry an egg?",
                    ),
                ],
                use_context=True,
                context_filter=ContextFilter(
                    docs_ids=["c202d5e6-7b69-4869-81cc-dd574ee8ee11"],
                ),
                include_sources=True,
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.chat_completion_v1chat_completions_post_stream(
            messages=messages,
            use_context=use_context,
            context_filter=context_filter,
            include_sources=include_sources,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def chat_completion(
        self,
        *,
        messages: typing.Sequence[OpenAiMessage],
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAiCompletion:
        """
        Given a list of messages comprising a conversation, return a response.

        Optionally include an initial `role: system` message to influence the way
        the LLM answers.

        If `use_context` is set to `true`, the model will use context coming
        from the ingested documents to create the response. The documents being used can
        be filtered using the `context_filter` and passing the document IDs to be used.
        Ingested documents IDs can be found using `/ingest/list` endpoint. If you want
        all ingested documents to be used, remove `context_filter` altogether.

        When using `'include_sources': true`, the API will return the source Chunks used
        to create the response, which come from the context provided.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        messages : typing.Sequence[OpenAiMessage]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        include_sources : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiCompletion


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ContextFilter, OpenAiMessage

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.contextual_completions.chat_completion(
                messages=[
                    OpenAiMessage(
                        role="system",
                        content="You are a rapper. Always answer with a rap.",
                    ),
                    OpenAiMessage(
                        role="user",
                        content="How do you fry an egg?",
                    ),
                ],
                use_context=True,
                context_filter=ContextFilter(
                    docs_ids=["c202d5e6-7b69-4869-81cc-dd574ee8ee11"],
                ),
                include_sources=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chat_completion(
            messages=messages,
            use_context=use_context,
            context_filter=context_filter,
            include_sources=include_sources,
            request_options=request_options,
        )
        return _response.data
