

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.chat_generation_request_engine import ChatGenerationRequestEngine
from .types.chat_message import ChatMessage
from .types.code_generation_request_engine import CodeGenerationRequestEngine
from .types.code_generation_response import CodeGenerationResponse
from .types.health_response import HealthResponse
from .types.models_response import ModelsResponse
from .types.video_generation_request_aspect_ratio import VideoGenerationRequestAspectRatio
from .types.video_generation_request_engine import VideoGenerationRequestEngine
from .types.video_rendering_request_aspect_ratio import VideoRenderingRequestAspectRatio
from .types.video_rendering_response import VideoRenderingResponse


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Returns the health status of the API and which LLM provider API keys are configured.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            Health status

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.health()
        """
        _response = self._raw_client.health(request_options=request_options)
        return _response.data

    def health_v1(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Alias for /health.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            Health status

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.health_v1()
        """
        _response = self._raw_client.health_v1(request_options=request_options)
        return _response.data

    def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> ModelsResponse:
        """
        Returns all supported engines with their available model IDs, defaults, and whether the corresponding API key is configured.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelsResponse
            List of engines and their models

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_models()
        """
        _response = self._raw_client.list_models(request_options=request_options)
        return _response.data

    def generate_code(
        self,
        *,
        prompt: typing.Optional[str] = OMIT,
        engine: typing.Optional[CodeGenerationRequestEngine] = OMIT,
        model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CodeGenerationResponse:
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
        CodeGenerationResponse
            Successfully generated Manim code

        Examples
        --------
        from fern import CodeGenerationRequestEngine, FernApi

        client = FernApi()
        client.generate_code(
            prompt="Draw a blue circle and animate its creation.",
            engine=CodeGenerationRequestEngine.OPENAI,
            model="gpt-4o",
        )
        """
        _response = self._raw_client.generate_code(
            prompt=prompt, engine=engine, model=model, request_options=request_options
        )
        return _response.data

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
    ) -> str:
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
        str
            Streaming response with generated content

        Examples
        --------
        from fern import ChatMessage, ChatMessageRole, FernApi

        client = FernApi()
        client.chat_generation(
            messages=[
                ChatMessage(
                    role=ChatMessageRole.USER,
                    content="content",
                ),
                ChatMessage(
                    role=ChatMessageRole.USER,
                    content="content",
                ),
            ],
        )
        """
        _response = self._raw_client.chat_generation(
            messages=messages,
            engine=engine,
            model=model,
            global_prompt=global_prompt,
            user_id=user_id,
            project_title=project_title,
            scenes=scenes,
            selected_scenes=selected_scenes,
            is_for_platform=is_for_platform,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Iterator[VideoRenderingResponse]:
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
        typing.Iterator[VideoRenderingResponse]
            Successfully rendered video (non-streaming mode)

        Examples
        --------
        from fern import FernApi, VideoRenderingRequestAspectRatio

        client = FernApi()
        response = client.render_video(
            code="from manim import *\nclass GenScene(Scene):\n    def construct(self):\n        self.play(Create(Circle()))",
            file_class="GenScene",
            aspect_ratio=VideoRenderingRequestAspectRatio.SIXTEEN9,
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.render_video(
            code=code,
            file_class=file_class,
            user_id=user_id,
            project_name=project_name,
            iteration=iteration,
            aspect_ratio=aspect_ratio,
            stream=stream,
            request_options=request_options,
        ) as r:
            yield from r.data

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
    ) -> VideoRenderingResponse:
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
        VideoRenderingResponse
            Successfully generated and rendered video

        Examples
        --------
        from fern import (
            FernApi,
            VideoGenerationRequestAspectRatio,
            VideoGenerationRequestEngine,
        )

        client = FernApi()
        client.generate_video(
            prompt="Animate a bouncing ball with gravity.",
            engine=VideoGenerationRequestEngine.OPENAI,
            aspect_ratio=VideoGenerationRequestAspectRatio.SIXTEEN9,
        )
        """
        _response = self._raw_client.generate_video(
            prompt=prompt,
            engine=engine,
            model=model,
            aspect_ratio=aspect_ratio,
            user_id=user_id,
            project_name=project_name,
            iteration=iteration,
            request_options=request_options,
        )
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Returns the health status of the API and which LLM provider API keys are configured.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            Health status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.health()


        asyncio.run(main())
        """
        _response = await self._raw_client.health(request_options=request_options)
        return _response.data

    async def health_v1(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Alias for /health.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            Health status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.health_v1()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_v1(request_options=request_options)
        return _response.data

    async def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> ModelsResponse:
        """
        Returns all supported engines with their available model IDs, defaults, and whether the corresponding API key is configured.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelsResponse
            List of engines and their models

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_models(request_options=request_options)
        return _response.data

    async def generate_code(
        self,
        *,
        prompt: typing.Optional[str] = OMIT,
        engine: typing.Optional[CodeGenerationRequestEngine] = OMIT,
        model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CodeGenerationResponse:
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
        CodeGenerationResponse
            Successfully generated Manim code

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CodeGenerationRequestEngine

        client = AsyncFernApi()


        async def main() -> None:
            await client.generate_code(
                prompt="Draw a blue circle and animate its creation.",
                engine=CodeGenerationRequestEngine.OPENAI,
                model="gpt-4o",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_code(
            prompt=prompt, engine=engine, model=model, request_options=request_options
        )
        return _response.data

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
    ) -> str:
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
        str
            Streaming response with generated content

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ChatMessage, ChatMessageRole

        client = AsyncFernApi()


        async def main() -> None:
            await client.chat_generation(
                messages=[
                    ChatMessage(
                        role=ChatMessageRole.USER,
                        content="content",
                    ),
                    ChatMessage(
                        role=ChatMessageRole.USER,
                        content="content",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chat_generation(
            messages=messages,
            engine=engine,
            model=model,
            global_prompt=global_prompt,
            user_id=user_id,
            project_title=project_title,
            scenes=scenes,
            selected_scenes=selected_scenes,
            is_for_platform=is_for_platform,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.AsyncIterator[VideoRenderingResponse]:
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
        typing.AsyncIterator[VideoRenderingResponse]
            Successfully rendered video (non-streaming mode)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, VideoRenderingRequestAspectRatio

        client = AsyncFernApi()


        async def main() -> None:
            response = client.render_video(
                code="from manim import *\nclass GenScene(Scene):\n    def construct(self):\n        self.play(Create(Circle()))",
                file_class="GenScene",
                aspect_ratio=VideoRenderingRequestAspectRatio.SIXTEEN9,
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.render_video(
            code=code,
            file_class=file_class,
            user_id=user_id,
            project_name=project_name,
            iteration=iteration,
            aspect_ratio=aspect_ratio,
            stream=stream,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

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
    ) -> VideoRenderingResponse:
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
        VideoRenderingResponse
            Successfully generated and rendered video

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            VideoGenerationRequestAspectRatio,
            VideoGenerationRequestEngine,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.generate_video(
                prompt="Animate a bouncing ball with gravity.",
                engine=VideoGenerationRequestEngine.OPENAI,
                aspect_ratio=VideoGenerationRequestAspectRatio.SIXTEEN9,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_video(
            prompt=prompt,
            engine=engine,
            model=model,
            aspect_ratio=aspect_ratio,
            user_id=user_id,
            project_name=project_name,
            iteration=iteration,
            request_options=request_options,
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
