

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.context_filter import ContextFilter
from ..types.summarize_response import SummarizeResponse
from .raw_client import AsyncRawRecipesClient, RawRecipesClient


OMIT = typing.cast(typing.Any, ...)


class RecipesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRecipesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRecipesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRecipesClient
        """
        return self._raw_client

    def summarize(
        self,
        *,
        text: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SummarizeResponse:
        """
        Given a text, the model will return a summary.

        Optionally include `instructions` to influence the way the summary is generated.

        If `use_context`
        is set to `true`, the model will also use the content coming from the ingested
        documents in the summary. The documents being used can
        be filtered by their metadata using the `context_filter`.
        Ingested documents metadata can be found using `/ingest/list` endpoint.
        If you want all ingested documents to be used, remove `context_filter` altogether.

        If `prompt` is set, it will be used as the prompt for the summarization,
        otherwise the default prompt will be used.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        text : typing.Optional[str]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        prompt : typing.Optional[str]

        instructions : typing.Optional[str]

        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SummarizeResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.recipes.summarize()
        """
        _response = self._raw_client.summarize(
            text=text,
            use_context=use_context,
            context_filter=context_filter,
            prompt=prompt,
            instructions=instructions,
            stream=stream,
            request_options=request_options,
        )
        return _response.data


class AsyncRecipesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRecipesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRecipesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRecipesClient
        """
        return self._raw_client

    async def summarize(
        self,
        *,
        text: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SummarizeResponse:
        """
        Given a text, the model will return a summary.

        Optionally include `instructions` to influence the way the summary is generated.

        If `use_context`
        is set to `true`, the model will also use the content coming from the ingested
        documents in the summary. The documents being used can
        be filtered by their metadata using the `context_filter`.
        Ingested documents metadata can be found using `/ingest/list` endpoint.
        If you want all ingested documents to be used, remove `context_filter` altogether.

        If `prompt` is set, it will be used as the prompt for the summarization,
        otherwise the default prompt will be used.

        When using `'stream': true`, the API will return data chunks following [OpenAI's
        streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
        ```
        {"id":"12345","object":"completion.chunk","created":1694268190,
        "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
        "finish_reason":null}]}
        ```

        Parameters
        ----------
        text : typing.Optional[str]

        use_context : typing.Optional[bool]

        context_filter : typing.Optional[ContextFilter]

        prompt : typing.Optional[str]

        instructions : typing.Optional[str]

        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SummarizeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.recipes.summarize()


        asyncio.run(main())
        """
        _response = await self._raw_client.summarize(
            text=text,
            use_context=use_context,
            context_filter=context_filter,
            prompt=prompt,
            instructions=instructions,
            stream=stream,
            request_options=request_options,
        )
        return _response.data
