

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.http_sse._api import EventSource
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as, parse_sse_obj
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.internal_server_error import InternalServerError
from .errors.request_timeout_error import RequestTimeoutError
from .types.chat_generation_request_engine import ChatGenerationRequestEngine
from .types.chat_message import ChatMessage
from .types.code_generation_request_engine import CodeGenerationRequestEngine
from .types.code_generation_response import CodeGenerationResponse
from .types.error_response import ErrorResponse
from .types.health_response import HealthResponse
from .types.models_response import ModelsResponse
from .types.video_generation_request_aspect_ratio import VideoGenerationRequestAspectRatio
from .types.video_generation_request_engine import VideoGenerationRequestEngine
from .types.video_rendering_request_aspect_ratio import VideoRenderingRequestAspectRatio
from .types.video_rendering_response import VideoRenderingResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[HealthResponse]:
        """
        Returns the health status of the API and which LLM provider API keys are configured.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HealthResponse]
            Health status
        """
        _response = self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HealthResponse,
                    parse_obj_as(
                        type_=HealthResponse,
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

    def health_v1(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[HealthResponse]:
        """
        Alias for /health.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HealthResponse]
            Health status
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HealthResponse,
                    parse_obj_as(
                        type_=HealthResponse,
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

    def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ModelsResponse]:
        """
        Returns all supported engines with their available model IDs, defaults, and whether the corresponding API key is configured.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ModelsResponse]
            List of engines and their models
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/models",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelsResponse,
                    parse_obj_as(
                        type_=ModelsResponse,
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

    def generate_code(
        self,
        *,
        prompt: typing.Optional[str] = OMIT,
        engine: typing.Optional[CodeGenerationRequestEngine] = OMIT,
        model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CodeGenerationResponse]:
        """
        Generates Manim Python code from a natural-language prompt using the specified LLM engine.

        Parameters
        ----------
        prompt : typing.Optional[str]
            Natural-language description of the animation to generate.

        engine : typing.Optional[CodeGenerationRequestEngine]
            LLM provider to use.

        model : typing.Optional[str]
            Model ID for the chosen engine. Defaults to the engine's recommended model if omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CodeGenerationResponse]
            Successfully generated Manim code
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/code/generation",
            method="POST",
            json={
                "prompt": prompt,
                "engine": engine,
                "model": model,
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
                    CodeGenerationResponse,
                    parse_obj_as(
                        type_=CodeGenerationResponse,
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

    def chat_generation(
        self,
        *,
        messages: typing.Sequence[ChatMessage],
        engine: typing.Optional[ChatGenerationRequestEngine] = OMIT,
        model: typing.Optional[str] = OMIT,
        global_prompt: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        project_title: typing.Optional[str] = OMIT,
        scenes: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        selected_scenes: typing.Optional[typing.Sequence[str]] = OMIT,
        is_for_platform: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Streams Manim code and explanations through a multi-turn conversation. Supports OpenAI, Anthropic, Gemini, Featherless, and LiteLLM engines.

        Parameters
        ----------
        messages : typing.Sequence[ChatMessage]
            Conversation history.

        engine : typing.Optional[ChatGenerationRequestEngine]

        model : typing.Optional[str]
            Model ID override. Defaults to the engine's recommended model.

        global_prompt : typing.Optional[str]
            Additional system-level instruction injected at the beginning.

        user_id : typing.Optional[str]

        project_title : typing.Optional[str]

        scenes : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        selected_scenes : typing.Optional[typing.Sequence[str]]

        is_for_platform : typing.Optional[bool]
            When true, the response uses the Vercel AI data stream format with Transfer-Encoding chunked.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Streaming response with generated content
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/chat/generation",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatMessage], direction="write"
                ),
                "engine": engine,
                "model": model,
                "globalPrompt": global_prompt,
                "userId": user_id,
                "projectTitle": project_title,
                "scenes": scenes,
                "selectedScenes": selected_scenes,
                "isForPlatform": is_for_platform,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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

    @contextlib.contextmanager
    def render_video(
        self,
        *,
        code: str,
        file_class: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        project_name: typing.Optional[str] = OMIT,
        iteration: typing.Optional[int] = OMIT,
        aspect_ratio: typing.Optional[VideoRenderingRequestAspectRatio] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[VideoRenderingResponse]]]:
        """
        Executes Manim Python code and returns a rendered MP4 video URL. Supports streaming progress updates.

        Parameters
        ----------
        code : str
            Manim Python code to render.

        file_class : typing.Optional[str]
            Name of the Manim Scene subclass to render. Defaults to GenScene.

        user_id : typing.Optional[str]
            User identifier used in the output file name.

        project_name : typing.Optional[str]

        iteration : typing.Optional[int]

        aspect_ratio : typing.Optional[VideoRenderingRequestAspectRatio]

        stream : typing.Optional[bool]
            If true, returns a 207 streaming response with per-animation progress.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[VideoRenderingResponse]]]
            Successfully rendered video (non-streaming mode)
        """
        with self._client_wrapper.httpx_client.stream(
            "v1/video/rendering",
            method="POST",
            json={
                "code": code,
                "file_class": file_class,
                "user_id": user_id,
                "project_name": project_name,
                "iteration": iteration,
                "aspect_ratio": aspect_ratio,
                "stream": stream,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[VideoRenderingResponse]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                try:
                                    yield typing.cast(
                                        VideoRenderingResponse,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=VideoRenderingResponse,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
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

    def generate_video(
        self,
        *,
        prompt: str,
        engine: typing.Optional[VideoGenerationRequestEngine] = OMIT,
        model: typing.Optional[str] = OMIT,
        aspect_ratio: typing.Optional[VideoGenerationRequestAspectRatio] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        project_name: typing.Optional[str] = OMIT,
        iteration: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VideoRenderingResponse]:
        """
        Generates Manim code from a prompt, then renders it to a video in one request.

        Parameters
        ----------
        prompt : str
            Natural-language description of the animation to generate and render.

        engine : typing.Optional[VideoGenerationRequestEngine]

        model : typing.Optional[str]

        aspect_ratio : typing.Optional[VideoGenerationRequestAspectRatio]

        user_id : typing.Optional[str]

        project_name : typing.Optional[str]

        iteration : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VideoRenderingResponse]
            Successfully generated and rendered video
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/video/generation",
            method="POST",
            json={
                "prompt": prompt,
                "engine": engine,
                "model": model,
                "aspect_ratio": aspect_ratio,
                "user_id": user_id,
                "project_name": project_name,
                "iteration": iteration,
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
                    VideoRenderingResponse,
                    parse_obj_as(
                        type_=VideoRenderingResponse,
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
            if _response.status_code == 408:
                raise RequestTimeoutError(
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[HealthResponse]:
        """
        Returns the health status of the API and which LLM provider API keys are configured.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HealthResponse]
            Health status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HealthResponse,
                    parse_obj_as(
                        type_=HealthResponse,
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

    async def health_v1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[HealthResponse]:
        """
        Alias for /health.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HealthResponse]
            Health status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HealthResponse,
                    parse_obj_as(
                        type_=HealthResponse,
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

    async def list_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ModelsResponse]:
        """
        Returns all supported engines with their available model IDs, defaults, and whether the corresponding API key is configured.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ModelsResponse]
            List of engines and their models
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/models",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ModelsResponse,
                    parse_obj_as(
                        type_=ModelsResponse,
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

    async def generate_code(
        self,
        *,
        prompt: typing.Optional[str] = OMIT,
        engine: typing.Optional[CodeGenerationRequestEngine] = OMIT,
        model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CodeGenerationResponse]:
        """
        Generates Manim Python code from a natural-language prompt using the specified LLM engine.

        Parameters
        ----------
        prompt : typing.Optional[str]
            Natural-language description of the animation to generate.

        engine : typing.Optional[CodeGenerationRequestEngine]
            LLM provider to use.

        model : typing.Optional[str]
            Model ID for the chosen engine. Defaults to the engine's recommended model if omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CodeGenerationResponse]
            Successfully generated Manim code
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/code/generation",
            method="POST",
            json={
                "prompt": prompt,
                "engine": engine,
                "model": model,
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
                    CodeGenerationResponse,
                    parse_obj_as(
                        type_=CodeGenerationResponse,
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

    async def chat_generation(
        self,
        *,
        messages: typing.Sequence[ChatMessage],
        engine: typing.Optional[ChatGenerationRequestEngine] = OMIT,
        model: typing.Optional[str] = OMIT,
        global_prompt: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        project_title: typing.Optional[str] = OMIT,
        scenes: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        selected_scenes: typing.Optional[typing.Sequence[str]] = OMIT,
        is_for_platform: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Streams Manim code and explanations through a multi-turn conversation. Supports OpenAI, Anthropic, Gemini, Featherless, and LiteLLM engines.

        Parameters
        ----------
        messages : typing.Sequence[ChatMessage]
            Conversation history.

        engine : typing.Optional[ChatGenerationRequestEngine]

        model : typing.Optional[str]
            Model ID override. Defaults to the engine's recommended model.

        global_prompt : typing.Optional[str]
            Additional system-level instruction injected at the beginning.

        user_id : typing.Optional[str]

        project_title : typing.Optional[str]

        scenes : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        selected_scenes : typing.Optional[typing.Sequence[str]]

        is_for_platform : typing.Optional[bool]
            When true, the response uses the Vercel AI data stream format with Transfer-Encoding chunked.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Streaming response with generated content
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/chat/generation",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatMessage], direction="write"
                ),
                "engine": engine,
                "model": model,
                "globalPrompt": global_prompt,
                "userId": user_id,
                "projectTitle": project_title,
                "scenes": scenes,
                "selectedScenes": selected_scenes,
                "isForPlatform": is_for_platform,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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

    @contextlib.asynccontextmanager
    async def render_video(
        self,
        *,
        code: str,
        file_class: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        project_name: typing.Optional[str] = OMIT,
        iteration: typing.Optional[int] = OMIT,
        aspect_ratio: typing.Optional[VideoRenderingRequestAspectRatio] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[VideoRenderingResponse]]]:
        """
        Executes Manim Python code and returns a rendered MP4 video URL. Supports streaming progress updates.

        Parameters
        ----------
        code : str
            Manim Python code to render.

        file_class : typing.Optional[str]
            Name of the Manim Scene subclass to render. Defaults to GenScene.

        user_id : typing.Optional[str]
            User identifier used in the output file name.

        project_name : typing.Optional[str]

        iteration : typing.Optional[int]

        aspect_ratio : typing.Optional[VideoRenderingRequestAspectRatio]

        stream : typing.Optional[bool]
            If true, returns a 207 streaming response with per-animation progress.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[VideoRenderingResponse]]]
            Successfully rendered video (non-streaming mode)
        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/video/rendering",
            method="POST",
            json={
                "code": code,
                "file_class": file_class,
                "user_id": user_id,
                "project_name": project_name,
                "iteration": iteration,
                "aspect_ratio": aspect_ratio,
                "stream": stream,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[VideoRenderingResponse]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                try:
                                    yield typing.cast(
                                        VideoRenderingResponse,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=VideoRenderingResponse,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
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

    async def generate_video(
        self,
        *,
        prompt: str,
        engine: typing.Optional[VideoGenerationRequestEngine] = OMIT,
        model: typing.Optional[str] = OMIT,
        aspect_ratio: typing.Optional[VideoGenerationRequestAspectRatio] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        project_name: typing.Optional[str] = OMIT,
        iteration: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VideoRenderingResponse]:
        """
        Generates Manim code from a prompt, then renders it to a video in one request.

        Parameters
        ----------
        prompt : str
            Natural-language description of the animation to generate and render.

        engine : typing.Optional[VideoGenerationRequestEngine]

        model : typing.Optional[str]

        aspect_ratio : typing.Optional[VideoGenerationRequestAspectRatio]

        user_id : typing.Optional[str]

        project_name : typing.Optional[str]

        iteration : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VideoRenderingResponse]
            Successfully generated and rendered video
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/video/generation",
            method="POST",
            json={
                "prompt": prompt,
                "engine": engine,
                "model": model,
                "aspect_ratio": aspect_ratio,
                "user_id": user_id,
                "project_name": project_name,
                "iteration": iteration,
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
                    VideoRenderingResponse,
                    parse_obj_as(
                        type_=VideoRenderingResponse,
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
            if _response.status_code == 408:
                raise RequestTimeoutError(
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
