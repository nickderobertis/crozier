

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
from ..types.context_filter import ContextFilter
from ..types.http_validation_error import HttpValidationError
from ..types.summarize_response import SummarizeResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRecipesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[SummarizeResponse]:
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
        HttpResponse[SummarizeResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/summarize",
            method="POST",
            json={
                "text": text,
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "prompt": prompt,
                "instructions": instructions,
                "stream": stream,
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
                    SummarizeResponse,
                    parse_obj_as(
                        type_=SummarizeResponse,
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


class AsyncRawRecipesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[SummarizeResponse]:
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
        AsyncHttpResponse[SummarizeResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/summarize",
            method="POST",
            json={
                "text": text,
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "prompt": prompt,
                "instructions": instructions,
                "stream": stream,
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
                    SummarizeResponse,
                    parse_obj_as(
                        type_=SummarizeResponse,
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
