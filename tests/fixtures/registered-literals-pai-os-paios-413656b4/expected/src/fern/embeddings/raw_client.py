

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.create_embedding_response import CreateEmbeddingResponse
from .types.create_embedding_request_encoding_format import CreateEmbeddingRequestEncodingFormat
from .types.create_embedding_request_input import CreateEmbeddingRequestInput
from .types.create_embedding_request_model import CreateEmbeddingRequestModel
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEmbeddingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_embedding(
        self,
        *,
        input: CreateEmbeddingRequestInput,
        model: CreateEmbeddingRequestModel,
        encoding_format: typing.Optional[CreateEmbeddingRequestEncodingFormat] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateEmbeddingResponse]:
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
        HttpResponse[CreateEmbeddingResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "embeddings",
            method="POST",
            json={
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CreateEmbeddingRequestInput, direction="write"
                ),
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateEmbeddingRequestModel, direction="write"
                ),
                "encoding_format": encoding_format,
                "dimensions": dimensions,
                "user": user,
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
                    CreateEmbeddingResponse,
                    parse_obj_as(
                        type_=CreateEmbeddingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEmbeddingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_embedding(
        self,
        *,
        input: CreateEmbeddingRequestInput,
        model: CreateEmbeddingRequestModel,
        encoding_format: typing.Optional[CreateEmbeddingRequestEncodingFormat] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        user: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateEmbeddingResponse]:
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
        AsyncHttpResponse[CreateEmbeddingResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "embeddings",
            method="POST",
            json={
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CreateEmbeddingRequestInput, direction="write"
                ),
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateEmbeddingRequestModel, direction="write"
                ),
                "encoding_format": encoding_format,
                "dimensions": dimensions,
                "user": user,
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
                    CreateEmbeddingResponse,
                    parse_obj_as(
                        type_=CreateEmbeddingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
