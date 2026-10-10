

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.embeddings_response import EmbeddingsResponse
from ..types.http_validation_error import HttpValidationError
from .types.embeddings_body_input import EmbeddingsBodyInput
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEmbeddingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def embeddings_generation(
        self, *, input: EmbeddingsBodyInput, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmbeddingsResponse]:
        """
        Get a vector representation of a given input.

        That vector representation can be easily consumed
        by machine learning models and algorithms.

        Parameters
        ----------
        input : EmbeddingsBodyInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmbeddingsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/embeddings",
            method="POST",
            json={
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=EmbeddingsBodyInput, direction="write"
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
                    EmbeddingsResponse,
                    parse_obj_as(
                        type_=EmbeddingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawEmbeddingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def embeddings_generation(
        self, *, input: EmbeddingsBodyInput, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmbeddingsResponse]:
        """
        Get a vector representation of a given input.

        That vector representation can be easily consumed
        by machine learning models and algorithms.

        Parameters
        ----------
        input : EmbeddingsBodyInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmbeddingsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/embeddings",
            method="POST",
            json={
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=EmbeddingsBodyInput, direction="write"
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
                    EmbeddingsResponse,
                    parse_obj_as(
                        type_=EmbeddingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
