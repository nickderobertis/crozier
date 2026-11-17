

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.document import Document
from ..types.embeddings_list import EmbeddingsList
from ..types.error_response import ErrorResponse
from ..types.model_info import ModelInfo
from ..types.model_info_list import ModelInfoList
from ..types.rerank_result import RerankResult
from .types.embed_request_inputs_item import EmbedRequestInputsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInferenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def embed(
        self,
        *,
        model: str,
        inputs: typing.Sequence[EmbedRequestInputsItem],
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmbeddingsList]:
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
        HttpResponse[EmbeddingsList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "embed",
            method="POST",
            json={
                "model": model,
                "parameters": parameters,
                "inputs": convert_and_respect_annotation_metadata(
                    object_=inputs, annotation=typing.Sequence[EmbedRequestInputsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmbeddingsList,
                    parse_obj_as(
                        type_=EmbeddingsList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[RerankResult]:
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
        HttpResponse[RerankResult]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "rerank",
            method="POST",
            json={
                "model": model,
                "query": query,
                "top_n": top_n,
                "return_documents": return_documents,
                "rank_fields": rank_fields,
                "documents": documents,
                "parameters": parameters,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RerankResult,
                    parse_obj_as(
                        type_=RerankResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_models(
        self,
        *,
        type: typing.Optional[str] = None,
        vector_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ModelInfoList]:
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
        HttpResponse[ModelInfoList]
            The list of available models.
        """
        _response = self._client_wrapper.httpx_client.request(
            "models",
            method="GET",
            params={
                "type": type,
                "vector_type": vector_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelInfoList,
                    parse_obj_as(
                        type_=ModelInfoList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_model(
        self, model_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ModelInfo]:
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
        HttpResponse[ModelInfo]
            The model details.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"models/{encode_path_param(model_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelInfo,
                    parse_obj_as(
                        type_=ModelInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawInferenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def embed(
        self,
        *,
        model: str,
        inputs: typing.Sequence[EmbedRequestInputsItem],
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmbeddingsList]:
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
        AsyncHttpResponse[EmbeddingsList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "embed",
            method="POST",
            json={
                "model": model,
                "parameters": parameters,
                "inputs": convert_and_respect_annotation_metadata(
                    object_=inputs, annotation=typing.Sequence[EmbedRequestInputsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmbeddingsList,
                    parse_obj_as(
                        type_=EmbeddingsList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[RerankResult]:
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
        AsyncHttpResponse[RerankResult]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "rerank",
            method="POST",
            json={
                "model": model,
                "query": query,
                "top_n": top_n,
                "return_documents": return_documents,
                "rank_fields": rank_fields,
                "documents": documents,
                "parameters": parameters,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RerankResult,
                    parse_obj_as(
                        type_=RerankResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_models(
        self,
        *,
        type: typing.Optional[str] = None,
        vector_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ModelInfoList]:
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
        AsyncHttpResponse[ModelInfoList]
            The list of available models.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "models",
            method="GET",
            params={
                "type": type,
                "vector_type": vector_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelInfoList,
                    parse_obj_as(
                        type_=ModelInfoList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_model(
        self, model_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ModelInfo]:
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
        AsyncHttpResponse[ModelInfo]
            The model details.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"models/{encode_path_param(model_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelInfo,
                    parse_obj_as(
                        type_=ModelInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
