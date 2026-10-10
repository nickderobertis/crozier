

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chunks_response import ChunksResponse
from ..types.context_filter import ContextFilter
from .raw_client import AsyncRawContextChunksClient, RawContextChunksClient


OMIT = typing.cast(typing.Any, ...)


class ContextChunksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContextChunksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContextChunksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContextChunksClient
        """
        return self._raw_client

    def chunks_retrieval(
        self,
        *,
        text: str,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        limit: typing.Optional[int] = OMIT,
        prev_next_chunks: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChunksResponse:
        """
        Given a `text`, returns the most relevant chunks from the ingested documents.

        The returned information can be used to generate prompts that can be
        passed to `/completions` or `/chat/completions` APIs. Note: it is usually a very
        fast API, because only the Embeddings model is involved, not the LLM. The
        returned information contains the relevant chunk `text` together with the source
        `document` it is coming from. It also contains a score that can be used to
        compare different results.

        The max number of chunks to be returned is set using the `limit` param.

        Previous and next chunks (pieces of text that appear right before or after in the
        document) can be fetched by using the `prev_next_chunks` field.

        The documents being used can be filtered using the `context_filter` and passing
        the document IDs to be used. Ingested documents IDs can be found using
        `/ingest/list` endpoint. If you want all ingested documents to be used,
        remove `context_filter` altogether.

        Parameters
        ----------
        text : str

        context_filter : typing.Optional[ContextFilter]

        limit : typing.Optional[int]

        prev_next_chunks : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChunksResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.context_chunks.chunks_retrieval(
            text="Q3 2023 sales",
        )
        """
        _response = self._raw_client.chunks_retrieval(
            text=text,
            context_filter=context_filter,
            limit=limit,
            prev_next_chunks=prev_next_chunks,
            request_options=request_options,
        )
        return _response.data


class AsyncContextChunksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContextChunksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContextChunksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContextChunksClient
        """
        return self._raw_client

    async def chunks_retrieval(
        self,
        *,
        text: str,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        limit: typing.Optional[int] = OMIT,
        prev_next_chunks: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChunksResponse:
        """
        Given a `text`, returns the most relevant chunks from the ingested documents.

        The returned information can be used to generate prompts that can be
        passed to `/completions` or `/chat/completions` APIs. Note: it is usually a very
        fast API, because only the Embeddings model is involved, not the LLM. The
        returned information contains the relevant chunk `text` together with the source
        `document` it is coming from. It also contains a score that can be used to
        compare different results.

        The max number of chunks to be returned is set using the `limit` param.

        Previous and next chunks (pieces of text that appear right before or after in the
        document) can be fetched by using the `prev_next_chunks` field.

        The documents being used can be filtered using the `context_filter` and passing
        the document IDs to be used. Ingested documents IDs can be found using
        `/ingest/list` endpoint. If you want all ingested documents to be used,
        remove `context_filter` altogether.

        Parameters
        ----------
        text : str

        context_filter : typing.Optional[ContextFilter]

        limit : typing.Optional[int]

        prev_next_chunks : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChunksResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.context_chunks.chunks_retrieval(
                text="Q3 2023 sales",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chunks_retrieval(
            text=text,
            context_filter=context_filter,
            limit=limit,
            prev_next_chunks=prev_next_chunks,
            request_options=request_options,
        )
        return _response.data
