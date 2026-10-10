

import contextlib
import json
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
from ..types.open_ai_completion import OpenAiCompletion
from ..types.open_ai_message import OpenAiMessage
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContextualCompletionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def prompt_completion_v1completions_post_stream(
        self,
        *,
        prompt: str,
        system_prompt: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[OpenAiCompletion]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[OpenAiCompletion]]]

        """
        with self._client_wrapper.httpx_client.stream(
            "v1/completions",
            method="POST",
            json={
                "prompt": prompt,
                "system_prompt": system_prompt,
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "include_sources": include_sources,
                "stream": True,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[OpenAiCompletion]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            for _text in _response.iter_lines():
                                try:
                                    if len(_text) == 0:
                                        continue
                                    yield typing.cast(
                                        OpenAiCompletion,
                                        parse_obj_as(
                                            type_=OpenAiCompletion,
                                            object_=json.loads(_text),
                                        ),
                                    )
                                except Exception:
                                    pass
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def prompt_completion(
        self,
        *,
        prompt: str,
        system_prompt: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OpenAiCompletion]:
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
        HttpResponse[OpenAiCompletion]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/completions",
            method="POST",
            json={
                "prompt": prompt,
                "system_prompt": system_prompt,
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "include_sources": include_sources,
                "stream": False,
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
                    OpenAiCompletion,
                    parse_obj_as(
                        type_=OpenAiCompletion,
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

    @contextlib.contextmanager
    def chat_completion_v1chat_completions_post_stream(
        self,
        *,
        messages: typing.Sequence[OpenAiMessage],
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[OpenAiCompletion]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[OpenAiCompletion]]]

        """
        with self._client_wrapper.httpx_client.stream(
            "v1/chat/completions",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[OpenAiMessage], direction="write"
                ),
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "include_sources": include_sources,
                "stream": True,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[OpenAiCompletion]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            for _text in _response.iter_lines():
                                try:
                                    if len(_text) == 0:
                                        continue
                                    yield typing.cast(
                                        OpenAiCompletion,
                                        parse_obj_as(
                                            type_=OpenAiCompletion,
                                            object_=json.loads(_text),
                                        ),
                                    )
                                except Exception:
                                    pass
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def chat_completion(
        self,
        *,
        messages: typing.Sequence[OpenAiMessage],
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OpenAiCompletion]:
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
        HttpResponse[OpenAiCompletion]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/chat/completions",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[OpenAiMessage], direction="write"
                ),
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "include_sources": include_sources,
                "stream": False,
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
                    OpenAiCompletion,
                    parse_obj_as(
                        type_=OpenAiCompletion,
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


class AsyncRawContextualCompletionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def prompt_completion_v1completions_post_stream(
        self,
        *,
        prompt: str,
        system_prompt: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[OpenAiCompletion]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[OpenAiCompletion]]]

        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/completions",
            method="POST",
            json={
                "prompt": prompt,
                "system_prompt": system_prompt,
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "include_sources": include_sources,
                "stream": True,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[OpenAiCompletion]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            async for _text in _response.aiter_lines():
                                try:
                                    if len(_text) == 0:
                                        continue
                                    yield typing.cast(
                                        OpenAiCompletion,
                                        parse_obj_as(
                                            type_=OpenAiCompletion,
                                            object_=json.loads(_text),
                                        ),
                                    )
                                except Exception:
                                    pass
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def prompt_completion(
        self,
        *,
        prompt: str,
        system_prompt: typing.Optional[str] = OMIT,
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OpenAiCompletion]:
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
        AsyncHttpResponse[OpenAiCompletion]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/completions",
            method="POST",
            json={
                "prompt": prompt,
                "system_prompt": system_prompt,
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "include_sources": include_sources,
                "stream": False,
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
                    OpenAiCompletion,
                    parse_obj_as(
                        type_=OpenAiCompletion,
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

    @contextlib.asynccontextmanager
    async def chat_completion_v1chat_completions_post_stream(
        self,
        *,
        messages: typing.Sequence[OpenAiMessage],
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[OpenAiCompletion]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[OpenAiCompletion]]]

        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/chat/completions",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[OpenAiMessage], direction="write"
                ),
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "include_sources": include_sources,
                "stream": True,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[OpenAiCompletion]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            async for _text in _response.aiter_lines():
                                try:
                                    if len(_text) == 0:
                                        continue
                                    yield typing.cast(
                                        OpenAiCompletion,
                                        parse_obj_as(
                                            type_=OpenAiCompletion,
                                            object_=json.loads(_text),
                                        ),
                                    )
                                except Exception:
                                    pass
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def chat_completion(
        self,
        *,
        messages: typing.Sequence[OpenAiMessage],
        use_context: typing.Optional[bool] = OMIT,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        include_sources: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OpenAiCompletion]:
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
        AsyncHttpResponse[OpenAiCompletion]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/chat/completions",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[OpenAiMessage], direction="write"
                ),
                "use_context": use_context,
                "context_filter": convert_and_respect_annotation_metadata(
                    object_=context_filter, annotation=typing.Optional[ContextFilter], direction="write"
                ),
                "include_sources": include_sources,
                "stream": False,
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
                    OpenAiCompletion,
                    parse_obj_as(
                        type_=OpenAiCompletion,
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
