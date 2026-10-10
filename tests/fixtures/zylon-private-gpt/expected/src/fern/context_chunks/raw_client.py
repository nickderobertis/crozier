

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
from ..types.chunks_response import ChunksResponse
from ..types.context_filter import ContextFilter
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContextChunksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def chunks_retrieval(
        self,
        *,
        text: str,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        limit: typing.Optional[int] = OMIT,
        prev_next_chunks: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChunksResponse]:
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
        HttpResponse[ChunksResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/chunks",
            method="POST",
            json={
                "text": text,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "limit": limit,
                "prev_next_chunks": prev_next_chunks,
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
                    ChunksResponse,
                    parse_obj_as(
                        type_=ChunksResponse,
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


class AsyncRawContextChunksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def chunks_retrieval(
        self,
        *,
        text: str,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        limit: typing.Optional[int] = OMIT,
        prev_next_chunks: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChunksResponse]:
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
        AsyncHttpResponse[ChunksResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/chunks",
            method="POST",
            json={
                "text": text,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "limit": limit,
                "prev_next_chunks": prev_next_chunks,
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
                    ChunksResponse,
                    parse_obj_as(
                        type_=ChunksResponse,
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
