

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.compact_resource import CompactResource
from .types.compact_response_method_public_body_input import CompactResponseMethodPublicBodyInput
from .types.create_response_body_input import CreateResponseBodyInput
from .types.create_response_body_reasoning import CreateResponseBodyReasoning
from .types.create_response_body_service_tier import CreateResponseBodyServiceTier
from .types.create_response_body_stream_options import CreateResponseBodyStreamOptions
from .types.create_response_body_text import CreateResponseBodyText
from .types.create_response_body_tool_choice import CreateResponseBodyToolChoice
from .types.create_response_body_truncation import CreateResponseBodyTruncation
from .types.include_enum import IncludeEnum
from .types.response_resource import ResponseResource
from .types.responses_tool_param import ResponsesToolParam


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



    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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

    client = FernApi(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            token=token,
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

    def create_response(
        self,
        *,
        model: typing.Optional[str] = OMIT,
        input: typing.Optional[CreateResponseBodyInput] = OMIT,
        previous_response_id: typing.Optional[str] = OMIT,
        include: typing.Optional[typing.Sequence[IncludeEnum]] = OMIT,
        tools: typing.Optional[typing.Sequence[ResponsesToolParam]] = OMIT,
        tool_choice: typing.Optional[CreateResponseBodyToolChoice] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        text: typing.Optional[CreateResponseBodyText] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        presence_penalty: typing.Optional[float] = OMIT,
        frequency_penalty: typing.Optional[float] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        stream_options: typing.Optional[CreateResponseBodyStreamOptions] = OMIT,
        background: typing.Optional[bool] = OMIT,
        max_output_tokens: typing.Optional[int] = OMIT,
        max_tool_calls: typing.Optional[int] = OMIT,
        reasoning: typing.Optional[CreateResponseBodyReasoning] = OMIT,
        safety_identifier: typing.Optional[str] = OMIT,
        prompt_cache_key: typing.Optional[str] = OMIT,
        truncation: typing.Optional[CreateResponseBodyTruncation] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        store: typing.Optional[bool] = OMIT,
        service_tier: typing.Optional[CreateResponseBodyServiceTier] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseResource:
        """
        Creates a response.

        Parameters
        ----------
        model : typing.Optional[str]
            The model to use for this request, e.g. 'gpt-5.2'.

        input : typing.Optional[CreateResponseBodyInput]
            Context to provide to the model for the scope of this request. May either be a string or an array of input items. If a string is provided, it is interpreted as a user message.

        previous_response_id : typing.Optional[str]
            The ID of the response to use as the prior turn for this request.

        include : typing.Optional[typing.Sequence[IncludeEnum]]

        tools : typing.Optional[typing.Sequence[ResponsesToolParam]]
            A list of tools that the model may call while generating the response.

        tool_choice : typing.Optional[CreateResponseBodyToolChoice]
            Controls which tool the model should use, if any.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Set of 16 key-value pairs that can be attached to an object. This can be         useful for storing additional information about the object in a structured         format, and querying for objects via API or the dashboard.
                    Keys are strings with a maximum length of 64 characters. Values are strings         with a maximum length of 512 characters.

        text : typing.Optional[CreateResponseBodyText]
            Configuration options for text output.

        temperature : typing.Optional[float]
            Sampling temperature to use, between 0 and 2. Higher values make the output more random.

        top_p : typing.Optional[float]
            Nucleus sampling parameter, between 0 and 1. The model considers only the tokens with the top cumulative probability.

        presence_penalty : typing.Optional[float]
            Penalizes new tokens based on whether they appear in the text so far.

        frequency_penalty : typing.Optional[float]
            Penalizes new tokens based on their frequency in the text so far.

        parallel_tool_calls : typing.Optional[bool]
            Whether the model may call multiple tools in parallel.

        stream : typing.Optional[bool]
            Whether to stream response events as server-sent events.

        stream_options : typing.Optional[CreateResponseBodyStreamOptions]
            Options that control streamed response behavior.

        background : typing.Optional[bool]
            Whether to run the request in the background and return immediately.

        max_output_tokens : typing.Optional[int]
            The maximum number of tokens the model may generate for this response.

        max_tool_calls : typing.Optional[int]
            The maximum number of tool calls the model may make while generating the response.

        reasoning : typing.Optional[CreateResponseBodyReasoning]
            Configuration options for reasoning behavior.

        safety_identifier : typing.Optional[str]
            A stable identifier used for safety monitoring and abuse detection.

        prompt_cache_key : typing.Optional[str]
            A key to use when reading from or writing to the prompt cache.

        truncation : typing.Optional[CreateResponseBodyTruncation]
            Controls how the service truncates the input when it exceeds the model context window.

        instructions : typing.Optional[str]
            Additional instructions to guide the model for this request.

        store : typing.Optional[bool]
            Whether to store the response so it can be retrieved later.

        service_tier : typing.Optional[CreateResponseBodyServiceTier]
            The service tier to use for this request.

        top_logprobs : typing.Optional[int]
            The number of most likely tokens to return at each position, along with their log probabilities.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseResource
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_response()
        """
        _response = self._raw_client.create_response(
            model=model,
            input=input,
            previous_response_id=previous_response_id,
            include=include,
            tools=tools,
            tool_choice=tool_choice,
            metadata=metadata,
            text=text,
            temperature=temperature,
            top_p=top_p,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            parallel_tool_calls=parallel_tool_calls,
            stream=stream,
            stream_options=stream_options,
            background=background,
            max_output_tokens=max_output_tokens,
            max_tool_calls=max_tool_calls,
            reasoning=reasoning,
            safety_identifier=safety_identifier,
            prompt_cache_key=prompt_cache_key,
            truncation=truncation,
            instructions=instructions,
            store=store,
            service_tier=service_tier,
            top_logprobs=top_logprobs,
            request_options=request_options,
        )
        return _response.data

    def compact_response(
        self,
        *,
        model: str,
        input: typing.Optional[CompactResponseMethodPublicBodyInput] = OMIT,
        previous_response_id: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        prompt_cache_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompactResource:
        """
        Compact a conversation. Returns a compacted response object.

        Parameters
        ----------
        model : str
            Model ID used to generate the response, like `gpt-5` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](/docs/models) to browse and compare available models.

        input : typing.Optional[CompactResponseMethodPublicBodyInput]
            Text, image, or file inputs to the model, used to generate a response

        previous_response_id : typing.Optional[str]
            The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

        instructions : typing.Optional[str]
            A system (or developer) message inserted into the model's context.
            When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

        prompt_cache_key : typing.Optional[str]
            A key to use when reading from or writing to the prompt cache.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompactResource
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.compact_response(
            model="model",
        )
        """
        _response = self._raw_client.compact_response(
            model=model,
            input=input,
            previous_response_id=previous_response_id,
            instructions=instructions,
            prompt_cache_key=prompt_cache_key,
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



    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

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

    client = AsyncFernApi(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
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
            token=token,
            headers=headers,
            async_token=async_token,
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

    async def create_response(
        self,
        *,
        model: typing.Optional[str] = OMIT,
        input: typing.Optional[CreateResponseBodyInput] = OMIT,
        previous_response_id: typing.Optional[str] = OMIT,
        include: typing.Optional[typing.Sequence[IncludeEnum]] = OMIT,
        tools: typing.Optional[typing.Sequence[ResponsesToolParam]] = OMIT,
        tool_choice: typing.Optional[CreateResponseBodyToolChoice] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        text: typing.Optional[CreateResponseBodyText] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        presence_penalty: typing.Optional[float] = OMIT,
        frequency_penalty: typing.Optional[float] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        stream_options: typing.Optional[CreateResponseBodyStreamOptions] = OMIT,
        background: typing.Optional[bool] = OMIT,
        max_output_tokens: typing.Optional[int] = OMIT,
        max_tool_calls: typing.Optional[int] = OMIT,
        reasoning: typing.Optional[CreateResponseBodyReasoning] = OMIT,
        safety_identifier: typing.Optional[str] = OMIT,
        prompt_cache_key: typing.Optional[str] = OMIT,
        truncation: typing.Optional[CreateResponseBodyTruncation] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        store: typing.Optional[bool] = OMIT,
        service_tier: typing.Optional[CreateResponseBodyServiceTier] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseResource:
        """
        Creates a response.

        Parameters
        ----------
        model : typing.Optional[str]
            The model to use for this request, e.g. 'gpt-5.2'.

        input : typing.Optional[CreateResponseBodyInput]
            Context to provide to the model for the scope of this request. May either be a string or an array of input items. If a string is provided, it is interpreted as a user message.

        previous_response_id : typing.Optional[str]
            The ID of the response to use as the prior turn for this request.

        include : typing.Optional[typing.Sequence[IncludeEnum]]

        tools : typing.Optional[typing.Sequence[ResponsesToolParam]]
            A list of tools that the model may call while generating the response.

        tool_choice : typing.Optional[CreateResponseBodyToolChoice]
            Controls which tool the model should use, if any.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Set of 16 key-value pairs that can be attached to an object. This can be         useful for storing additional information about the object in a structured         format, and querying for objects via API or the dashboard.
                    Keys are strings with a maximum length of 64 characters. Values are strings         with a maximum length of 512 characters.

        text : typing.Optional[CreateResponseBodyText]
            Configuration options for text output.

        temperature : typing.Optional[float]
            Sampling temperature to use, between 0 and 2. Higher values make the output more random.

        top_p : typing.Optional[float]
            Nucleus sampling parameter, between 0 and 1. The model considers only the tokens with the top cumulative probability.

        presence_penalty : typing.Optional[float]
            Penalizes new tokens based on whether they appear in the text so far.

        frequency_penalty : typing.Optional[float]
            Penalizes new tokens based on their frequency in the text so far.

        parallel_tool_calls : typing.Optional[bool]
            Whether the model may call multiple tools in parallel.

        stream : typing.Optional[bool]
            Whether to stream response events as server-sent events.

        stream_options : typing.Optional[CreateResponseBodyStreamOptions]
            Options that control streamed response behavior.

        background : typing.Optional[bool]
            Whether to run the request in the background and return immediately.

        max_output_tokens : typing.Optional[int]
            The maximum number of tokens the model may generate for this response.

        max_tool_calls : typing.Optional[int]
            The maximum number of tool calls the model may make while generating the response.

        reasoning : typing.Optional[CreateResponseBodyReasoning]
            Configuration options for reasoning behavior.

        safety_identifier : typing.Optional[str]
            A stable identifier used for safety monitoring and abuse detection.

        prompt_cache_key : typing.Optional[str]
            A key to use when reading from or writing to the prompt cache.

        truncation : typing.Optional[CreateResponseBodyTruncation]
            Controls how the service truncates the input when it exceeds the model context window.

        instructions : typing.Optional[str]
            Additional instructions to guide the model for this request.

        store : typing.Optional[bool]
            Whether to store the response so it can be retrieved later.

        service_tier : typing.Optional[CreateResponseBodyServiceTier]
            The service tier to use for this request.

        top_logprobs : typing.Optional[int]
            The number of most likely tokens to return at each position, along with their log probabilities.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseResource
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_response()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_response(
            model=model,
            input=input,
            previous_response_id=previous_response_id,
            include=include,
            tools=tools,
            tool_choice=tool_choice,
            metadata=metadata,
            text=text,
            temperature=temperature,
            top_p=top_p,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            parallel_tool_calls=parallel_tool_calls,
            stream=stream,
            stream_options=stream_options,
            background=background,
            max_output_tokens=max_output_tokens,
            max_tool_calls=max_tool_calls,
            reasoning=reasoning,
            safety_identifier=safety_identifier,
            prompt_cache_key=prompt_cache_key,
            truncation=truncation,
            instructions=instructions,
            store=store,
            service_tier=service_tier,
            top_logprobs=top_logprobs,
            request_options=request_options,
        )
        return _response.data

    async def compact_response(
        self,
        *,
        model: str,
        input: typing.Optional[CompactResponseMethodPublicBodyInput] = OMIT,
        previous_response_id: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        prompt_cache_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompactResource:
        """
        Compact a conversation. Returns a compacted response object.

        Parameters
        ----------
        model : str
            Model ID used to generate the response, like `gpt-5` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](/docs/models) to browse and compare available models.

        input : typing.Optional[CompactResponseMethodPublicBodyInput]
            Text, image, or file inputs to the model, used to generate a response

        previous_response_id : typing.Optional[str]
            The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

        instructions : typing.Optional[str]
            A system (or developer) message inserted into the model's context.
            When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

        prompt_cache_key : typing.Optional[str]
            A key to use when reading from or writing to the prompt cache.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompactResource
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.compact_response(
                model="model",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compact_response(
            model=model,
            input=input,
            previous_response_id=previous_response_id,
            instructions=instructions,
            prompt_cache_key=prompt_cache_key,
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
