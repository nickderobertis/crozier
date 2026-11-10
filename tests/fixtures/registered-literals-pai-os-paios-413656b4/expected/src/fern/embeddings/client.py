

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_embedding_response import CreateEmbeddingResponse
from .raw_client import AsyncRawEmbeddingsClient, RawEmbeddingsClient
from .types.create_embedding_request_encoding_format import CreateEmbeddingRequestEncodingFormat
from .types.create_embedding_request_input import CreateEmbeddingRequestInput
from .types.create_embedding_request_model import CreateEmbeddingRequestModel


OMIT = typing.cast(typing.Any, ...)


class EmbeddingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmbeddingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmbeddingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmbeddingsClient
        """
        return self._raw_client

    def create_embedding(
        self,
        *,
        input: CreateEmbeddingRequestInput,
        model: CreateEmbeddingRequestModel,
        encoding_format: typing.Optional[CreateEmbeddingRequestEncodingFormat] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateEmbeddingResponse:
        """
        Parameters
        ----------
        input : CreateEmbeddingRequestInput
            Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input tokens for the model (8192 tokens for `text-embedding-ada-002`), cannot be an empty string, and any array must be 2048 dimensions or less. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

        model : CreateEmbeddingRequestModel
            ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

        encoding_format : typing.Optional[CreateEmbeddingRequestEncodingFormat]
            The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/).

        dimensions : typing.Optional[int]
            The number of dimensions the resulting output embeddings should have. Only supported in `text-embedding-3` and later models.

        user : typing.Optional[str]
            A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateEmbeddingResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.embeddings.create_embedding(
            input="This is a test.",
            model="text-embedding-ada-002",
        )
        """
        _response = self._raw_client.create_embedding(
            input=input,
            model=model,
            encoding_format=encoding_format,
            dimensions=dimensions,
            user=user,
            request_options=request_options,
        )
        return _response.data


class AsyncEmbeddingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmbeddingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmbeddingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmbeddingsClient
        """
        return self._raw_client

    async def create_embedding(
        self,
        *,
        input: CreateEmbeddingRequestInput,
        model: CreateEmbeddingRequestModel,
        encoding_format: typing.Optional[CreateEmbeddingRequestEncodingFormat] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateEmbeddingResponse:
        """
        Parameters
        ----------
        input : CreateEmbeddingRequestInput
            Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input tokens for the model (8192 tokens for `text-embedding-ada-002`), cannot be an empty string, and any array must be 2048 dimensions or less. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

        model : CreateEmbeddingRequestModel
            ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

        encoding_format : typing.Optional[CreateEmbeddingRequestEncodingFormat]
            The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/).

        dimensions : typing.Optional[int]
            The number of dimensions the resulting output embeddings should have. Only supported in `text-embedding-3` and later models.

        user : typing.Optional[str]
            A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateEmbeddingResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.embeddings.create_embedding(
                input="This is a test.",
                model="text-embedding-ada-002",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_embedding(
            input=input,
            model=model,
            encoding_format=encoding_format,
            dimensions=dimensions,
            user=user,
            request_options=request_options,
        )
        return _response.data
