

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.document import Document
from ..types.embeddings_list import EmbeddingsList
from ..types.model_info import ModelInfo
from ..types.model_info_list import ModelInfoList
from ..types.rerank_result import RerankResult
from .raw_client import AsyncRawInferenceClient, RawInferenceClient
from .types.embed_request_inputs_item import EmbedRequestInputsItem


OMIT = typing.cast(typing.Any, ...)


class InferenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInferenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInferenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInferenceClient
        """
        return self._raw_client

    def embed(
        self,
        *,
        model: str,
        inputs: typing.Sequence[EmbedRequestInputsItem],
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbeddingsList:
        """
        Generate vector embeddings for input data. This endpoint uses Pinecone's [hosted embedding models](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models).

        Parameters
        ----------
        model : str
            The [model](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) to use for embedding generation.

        inputs : typing.Sequence[EmbedRequestInputsItem]
            List of inputs to generate embeddings for.

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Additional model-specific parameters. Refer to the [model guide](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) for available model parameters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbeddingsList
            OK

        Examples
        --------
        from fern.inference import EmbedRequestInputsItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.inference.embed(
            model="multilingual-e5-large",
            inputs=[EmbedRequestInputsItem()],
        )
        """
        _response = self._raw_client.embed(
            model=model, inputs=inputs, parameters=parameters, request_options=request_options
        )
        return _response.data

    def rerank(
        self,
        *,
        model: str,
        query: str,
        documents: typing.Sequence[Document],
        top_n: typing.Optional[int] = OMIT,
        return_documents: typing.Optional[bool] = OMIT,
        rank_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RerankResult:
        """
        Rerank results according to their relevance to a query.

        For guidance and examples, see [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

        Parameters
        ----------
        model : str
            The [model](https://docs.pinecone.io/guides/search/rerank-results#reranking-models) to use for reranking.

        query : str
            The query to rerank documents against.

        documents : typing.Sequence[Document]
            The documents to rerank.

        top_n : typing.Optional[int]
            The number of results to return sorted by relevance. Defaults to the number of inputs.

        return_documents : typing.Optional[bool]
            Whether to return the documents in the response.

        rank_fields : typing.Optional[typing.Sequence[str]]
            The field(s) to consider for reranking. If not provided, the default is `["text"]`.

            The number of fields supported is [model-specific](https://docs.pinecone.io/guides/search/rerank-results#reranking-models).

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Additional model-specific parameters. Refer to the [model guide](https://docs.pinecone.io/guides/search/rerank-results#reranking-models) for available model parameters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RerankResult
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.inference.rerank(
            model="bge-reranker-v2-m3",
            query="What is the capital of France?",
            documents=[
                {
                    "id": "1",
                    "text": "Paris is the capital of France.",
                    "title": "France",
                    "url": "https://example.com",
                }
            ],
        )
        """
        _response = self._raw_client.rerank(
            model=model,
            query=query,
            documents=documents,
            top_n=top_n,
            return_documents=return_documents,
            rank_fields=rank_fields,
            parameters=parameters,
            request_options=request_options,
        )
        return _response.data

    def list_models(
        self,
        *,
        type: typing.Optional[str] = None,
        vector_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelInfoList:
        """
        List the embedding and reranking models hosted by Pinecone.

        You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

        Parameters
        ----------
        type : typing.Optional[str]
            Filter models by type ('embed' or 'rerank').

        vector_type : typing.Optional[str]
            Filter embedding models by vector type ('dense' or 'sparse'). Only relevant when `type=embed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelInfoList
            The list of available models.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.inference.list_models(
            type="embed",
            vector_type="sparse",
        )
        """
        _response = self._raw_client.list_models(type=type, vector_type=vector_type, request_options=request_options)
        return _response.data

    def get_model(self, model_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ModelInfo:
        """
        Get a description of a model hosted by Pinecone.

        You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

        Parameters
        ----------
        model_name : str
            The name of the model to look up.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelInfo
            The model details.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.inference.get_model(
            model_name="multilingual-e5-large",
        )
        """
        _response = self._raw_client.get_model(model_name, request_options=request_options)
        return _response.data


class AsyncInferenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInferenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInferenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInferenceClient
        """
        return self._raw_client

    async def embed(
        self,
        *,
        model: str,
        inputs: typing.Sequence[EmbedRequestInputsItem],
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbeddingsList:
        """
        Generate vector embeddings for input data. This endpoint uses Pinecone's [hosted embedding models](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models).

        Parameters
        ----------
        model : str
            The [model](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) to use for embedding generation.

        inputs : typing.Sequence[EmbedRequestInputsItem]
            List of inputs to generate embeddings for.

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Additional model-specific parameters. Refer to the [model guide](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) for available model parameters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbeddingsList
            OK

        Examples
        --------
        import asyncio

        from fern.inference import EmbedRequestInputsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.inference.embed(
                model="multilingual-e5-large",
                inputs=[EmbedRequestInputsItem()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.embed(
            model=model, inputs=inputs, parameters=parameters, request_options=request_options
        )
        return _response.data

    async def rerank(
        self,
        *,
        model: str,
        query: str,
        documents: typing.Sequence[Document],
        top_n: typing.Optional[int] = OMIT,
        return_documents: typing.Optional[bool] = OMIT,
        rank_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RerankResult:
        """
        Rerank results according to their relevance to a query.

        For guidance and examples, see [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

        Parameters
        ----------
        model : str
            The [model](https://docs.pinecone.io/guides/search/rerank-results#reranking-models) to use for reranking.

        query : str
            The query to rerank documents against.

        documents : typing.Sequence[Document]
            The documents to rerank.

        top_n : typing.Optional[int]
            The number of results to return sorted by relevance. Defaults to the number of inputs.

        return_documents : typing.Optional[bool]
            Whether to return the documents in the response.

        rank_fields : typing.Optional[typing.Sequence[str]]
            The field(s) to consider for reranking. If not provided, the default is `["text"]`.

            The number of fields supported is [model-specific](https://docs.pinecone.io/guides/search/rerank-results#reranking-models).

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Additional model-specific parameters. Refer to the [model guide](https://docs.pinecone.io/guides/search/rerank-results#reranking-models) for available model parameters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RerankResult
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.inference.rerank(
                model="bge-reranker-v2-m3",
                query="What is the capital of France?",
                documents=[
                    {
                        "id": "1",
                        "text": "Paris is the capital of France.",
                        "title": "France",
                        "url": "https://example.com",
                    }
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rerank(
            model=model,
            query=query,
            documents=documents,
            top_n=top_n,
            return_documents=return_documents,
            rank_fields=rank_fields,
            parameters=parameters,
            request_options=request_options,
        )
        return _response.data

    async def list_models(
        self,
        *,
        type: typing.Optional[str] = None,
        vector_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelInfoList:
        """
        List the embedding and reranking models hosted by Pinecone.

        You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

        Parameters
        ----------
        type : typing.Optional[str]
            Filter models by type ('embed' or 'rerank').

        vector_type : typing.Optional[str]
            Filter embedding models by vector type ('dense' or 'sparse'). Only relevant when `type=embed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelInfoList
            The list of available models.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.inference.list_models(
                type="embed",
                vector_type="sparse",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_models(
            type=type, vector_type=vector_type, request_options=request_options
        )
        return _response.data

    async def get_model(self, model_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ModelInfo:
        """
        Get a description of a model hosted by Pinecone.

        You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

        Parameters
        ----------
        model_name : str
            The name of the model to look up.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelInfo
            The model details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.inference.get_model(
                model_name="multilingual-e5-large",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_model(model_name, request_options=request_options)
        return _response.data
