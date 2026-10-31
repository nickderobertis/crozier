

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.chat_message import ChatMessage
from .types.chat_request_format import ChatRequestFormat
from .types.chat_request_keep_alive import ChatRequestKeepAlive
from .types.chat_response import ChatResponse
from .types.create_request_license import CreateRequestLicense
from .types.embed_request_input import EmbedRequestInput
from .types.embed_response import EmbedResponse
from .types.generate_request_format import GenerateRequestFormat
from .types.generate_request_keep_alive import GenerateRequestKeepAlive
from .types.generate_response import GenerateResponse
from .types.list_response import ListResponse
from .types.model_options import ModelOptions
from .types.ps_response import PsResponse
from .types.show_response import ShowResponse
from .types.status_response import StatusResponse
from .types.think_value import ThinkValue
from .types.tool_definition import ToolDefinition
from .types.version_response import VersionResponse


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

    def generate(
        self,
        *,
        model: str,
        prompt: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[str]] = OMIT,
        format: typing.Optional[GenerateRequestFormat] = OMIT,
        system: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        think: typing.Optional[ThinkValue] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        keep_alive: typing.Optional[GenerateRequestKeepAlive] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateResponse:
        """
        Generates a response for the provided prompt

        Parameters
        ----------
        model : str
            Model name

        prompt : typing.Optional[str]
            Text for the model to generate a response from

        suffix : typing.Optional[str]
            Used for fill-in-the-middle models, text that appears after the user prompt and before the model response

        images : typing.Optional[typing.Sequence[str]]

        format : typing.Optional[GenerateRequestFormat]
            Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object.

        system : typing.Optional[str]
            System prompt for the model to generate a response from

        stream : typing.Optional[bool]
            When true, returns a stream of partial responses

        think : typing.Optional[ThinkValue]

        raw : typing.Optional[bool]
            When true, returns the raw response from the model without any prompt templating

        keep_alive : typing.Optional[GenerateRequestKeepAlive]
            Model keep-alive duration (for example `5m` or `0` to unload immediately)

        options : typing.Optional[ModelOptions]

        logprobs : typing.Optional[bool]
            Whether to return log probabilities of the output tokens

        top_logprobs : typing.Optional[int]
            Number of most likely tokens to return at each token position when logprobs are enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateResponse
            Generation responses

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate(
            model="gemma4",
            prompt="Why is the sky blue?",
        )
        """
        _response = self._raw_client.generate(
            model=model,
            prompt=prompt,
            suffix=suffix,
            images=images,
            format=format,
            system=system,
            stream=stream,
            think=think,
            raw=raw,
            keep_alive=keep_alive,
            options=options,
            logprobs=logprobs,
            top_logprobs=top_logprobs,
            request_options=request_options,
        )
        return _response.data

    def chat(
        self,
        *,
        model: str,
        messages: typing.Sequence[ChatMessage],
        tools: typing.Optional[typing.Sequence[ToolDefinition]] = OMIT,
        format: typing.Optional[ChatRequestFormat] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        think: typing.Optional[ThinkValue] = OMIT,
        keep_alive: typing.Optional[ChatRequestKeepAlive] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatResponse:
        """
        Generate the next chat message in a conversation between a user and an assistant.

        Parameters
        ----------
        model : str
            Model name

        messages : typing.Sequence[ChatMessage]
            Chat history as an array of message objects (each with a role and content)

        tools : typing.Optional[typing.Sequence[ToolDefinition]]
            Optional list of function tools the model may call during the chat

        format : typing.Optional[ChatRequestFormat]
            Format to return a response in. Can be `json` or a JSON schema

        options : typing.Optional[ModelOptions]

        stream : typing.Optional[bool]

        think : typing.Optional[ThinkValue]

        keep_alive : typing.Optional[ChatRequestKeepAlive]
            Model keep-alive duration (for example `5m` or `0` to unload immediately)

        logprobs : typing.Optional[bool]
            Whether to return log probabilities of the output tokens

        top_logprobs : typing.Optional[int]
            Number of most likely tokens to return at each token position when logprobs are enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatResponse
            Chat response

        Examples
        --------
        from fern import ChatMessage, ChatMessageRole, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat(
            model="model",
            messages=[
                ChatMessage(
                    role=ChatMessageRole.SYSTEM,
                    content="content",
                )
            ],
        )
        """
        _response = self._raw_client.chat(
            model=model,
            messages=messages,
            tools=tools,
            format=format,
            options=options,
            stream=stream,
            think=think,
            keep_alive=keep_alive,
            logprobs=logprobs,
            top_logprobs=top_logprobs,
            request_options=request_options,
        )
        return _response.data

    def embed(
        self,
        *,
        model: str,
        input: EmbedRequestInput,
        truncate: typing.Optional[bool] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        keep_alive: typing.Optional[str] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbedResponse:
        """
        Creates vector embeddings representing the input text

        Parameters
        ----------
        model : str
            Model name

        input : EmbedRequestInput
            Text or array of texts to generate embeddings for

        truncate : typing.Optional[bool]
            If true, truncate inputs that exceed the context window. If false, returns an error.

        dimensions : typing.Optional[int]
            Number of dimensions to generate embeddings for

        keep_alive : typing.Optional[str]
            Model keep-alive duration

        options : typing.Optional[ModelOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbedResponse
            Vector embeddings for the input text

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.embed(
            model="embeddinggemma",
            input="Generate embeddings for this text",
        )
        """
        _response = self._raw_client.embed(
            model=model,
            input=input,
            truncate=truncate,
            dimensions=dimensions,
            keep_alive=keep_alive,
            options=options,
            request_options=request_options,
        )
        return _response.data

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListResponse:
        """
        Fetch a list of models and their details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponse
            List available models

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def ps(self, *, request_options: typing.Optional[RequestOptions] = None) -> PsResponse:
        """
        Retrieve a list of models that are currently running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PsResponse
            Models currently loaded into memory

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ps()
        """
        _response = self._raw_client.ps(request_options=request_options)
        return _response.data

    def show(
        self,
        *,
        model: str,
        verbose: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShowResponse:
        """
        Parameters
        ----------
        model : str
            Model name to show

        verbose : typing.Optional[bool]
            If true, includes large verbose fields in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShowResponse
            Model information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.show(
            model="gemma4",
        )
        """
        _response = self._raw_client.show(model=model, verbose=verbose, request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        model: str,
        from_: typing.Optional[str] = OMIT,
        template: typing.Optional[str] = OMIT,
        renderer: typing.Optional[str] = OMIT,
        parser: typing.Optional[str] = OMIT,
        files: typing.Optional[typing.Dict[str, str]] = OMIT,
        draft_files: typing.Optional[typing.Dict[str, str]] = OMIT,
        license: typing.Optional[CreateRequestLicense] = OMIT,
        system: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        messages: typing.Optional[typing.Sequence[ChatMessage]] = OMIT,
        quantize: typing.Optional[str] = OMIT,
        draft_quantize: typing.Optional[str] = OMIT,
        requires: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusResponse:
        """
        Parameters
        ----------
        model : str
            Name for the model to create

        from_ : typing.Optional[str]
            Existing model to create from

        template : typing.Optional[str]
            Prompt template to use for the model

        renderer : typing.Optional[str]
            Name of the renderer for the model

        parser : typing.Optional[str]
            Name of the parser for the model

        files : typing.Optional[typing.Dict[str, str]]
            Source file names mapped to their SHA-256 digests. Split GGUF models must include each shard under its original split filename.

        draft_files : typing.Optional[typing.Dict[str, str]]
            Draft source file names mapped to their SHA-256 digests

        license : typing.Optional[CreateRequestLicense]
            License string or list of licenses for the model

        system : typing.Optional[str]
            System prompt to embed in the model

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value parameters for the model

        messages : typing.Optional[typing.Sequence[ChatMessage]]
            Message history to use for the model

        quantize : typing.Optional[str]
            Quantization level to apply during import (e.g. `nvfp4`)

        draft_quantize : typing.Optional[str]
            Quantization level to apply to draft weights during import

        requires : typing.Optional[str]
            Minimum Ollama version required by the model

        stream : typing.Optional[bool]
            Stream status updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Stream of create status updates

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create(
            model="mario",
            from_="gemma4",
            system="You are Mario from Super Mario Bros.",
        )
        """
        _response = self._raw_client.create(
            model=model,
            from_=from_,
            template=template,
            renderer=renderer,
            parser=parser,
            files=files,
            draft_files=draft_files,
            license=license,
            system=system,
            parameters=parameters,
            messages=messages,
            quantize=quantize,
            draft_quantize=draft_quantize,
            requires=requires,
            stream=stream,
            request_options=request_options,
        )
        return _response.data

    def create_blob(
        self,
        digest: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        digest : str
            SHA256 digest identifier, prefixed with `sha256:`

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.create_blob(digest, request=request, request_options=request_options)
        return _response.data

    def head_blob(
        self, digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        digest : str
            SHA256 digest identifier, prefixed with `sha256:`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.head_blob(
            digest="digest",
        )
        """
        _response = self._raw_client.head_blob(digest, request_options=request_options)
        return _response.headers

    def copy(self, *, source: str, destination: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        source : str
            Existing model name to copy from

        destination : str
            New model name to create

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copy(
            source="gemma4",
            destination="gemma4-backup",
        )
        """
        _response = self._raw_client.copy(source=source, destination=destination, request_options=request_options)
        return _response.data

    def pull(
        self,
        *,
        model: str,
        insecure: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusResponse:
        """
        Parameters
        ----------
        model : str
            Name of the model to download

        insecure : typing.Optional[bool]
            Allow downloading over insecure connections

        stream : typing.Optional[bool]
            Stream progress updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Pull status updates.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pull(
            model="gemma4",
        )
        """
        _response = self._raw_client.pull(
            model=model, insecure=insecure, stream=stream, request_options=request_options
        )
        return _response.data

    def push(
        self,
        *,
        model: str,
        insecure: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusResponse:
        """
        Parameters
        ----------
        model : str
            Name of the model to publish

        insecure : typing.Optional[bool]
            Allow publishing over insecure connections

        stream : typing.Optional[bool]
            Stream progress updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Push status updates.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.push(
            model="my-username/my-model",
        )
        """
        _response = self._raw_client.push(
            model=model, insecure=insecure, stream=stream, request_options=request_options
        )
        return _response.data

    def delete(self, *, model: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        model : str
            Model name to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete(
            model="gemma4",
        )
        """
        _response = self._raw_client.delete(model=model, request_options=request_options)
        return _response.data

    def version(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionResponse:
        """
        Retrieve the version of the Ollama

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionResponse
            Version information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.version()
        """
        _response = self._raw_client.version(request_options=request_options)
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

    async def generate(
        self,
        *,
        model: str,
        prompt: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[str]] = OMIT,
        format: typing.Optional[GenerateRequestFormat] = OMIT,
        system: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        think: typing.Optional[ThinkValue] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        keep_alive: typing.Optional[GenerateRequestKeepAlive] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateResponse:
        """
        Generates a response for the provided prompt

        Parameters
        ----------
        model : str
            Model name

        prompt : typing.Optional[str]
            Text for the model to generate a response from

        suffix : typing.Optional[str]
            Used for fill-in-the-middle models, text that appears after the user prompt and before the model response

        images : typing.Optional[typing.Sequence[str]]

        format : typing.Optional[GenerateRequestFormat]
            Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object.

        system : typing.Optional[str]
            System prompt for the model to generate a response from

        stream : typing.Optional[bool]
            When true, returns a stream of partial responses

        think : typing.Optional[ThinkValue]

        raw : typing.Optional[bool]
            When true, returns the raw response from the model without any prompt templating

        keep_alive : typing.Optional[GenerateRequestKeepAlive]
            Model keep-alive duration (for example `5m` or `0` to unload immediately)

        options : typing.Optional[ModelOptions]

        logprobs : typing.Optional[bool]
            Whether to return log probabilities of the output tokens

        top_logprobs : typing.Optional[int]
            Number of most likely tokens to return at each token position when logprobs are enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateResponse
            Generation responses

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate(
                model="gemma4",
                prompt="Why is the sky blue?",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate(
            model=model,
            prompt=prompt,
            suffix=suffix,
            images=images,
            format=format,
            system=system,
            stream=stream,
            think=think,
            raw=raw,
            keep_alive=keep_alive,
            options=options,
            logprobs=logprobs,
            top_logprobs=top_logprobs,
            request_options=request_options,
        )
        return _response.data

    async def chat(
        self,
        *,
        model: str,
        messages: typing.Sequence[ChatMessage],
        tools: typing.Optional[typing.Sequence[ToolDefinition]] = OMIT,
        format: typing.Optional[ChatRequestFormat] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        think: typing.Optional[ThinkValue] = OMIT,
        keep_alive: typing.Optional[ChatRequestKeepAlive] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatResponse:
        """
        Generate the next chat message in a conversation between a user and an assistant.

        Parameters
        ----------
        model : str
            Model name

        messages : typing.Sequence[ChatMessage]
            Chat history as an array of message objects (each with a role and content)

        tools : typing.Optional[typing.Sequence[ToolDefinition]]
            Optional list of function tools the model may call during the chat

        format : typing.Optional[ChatRequestFormat]
            Format to return a response in. Can be `json` or a JSON schema

        options : typing.Optional[ModelOptions]

        stream : typing.Optional[bool]

        think : typing.Optional[ThinkValue]

        keep_alive : typing.Optional[ChatRequestKeepAlive]
            Model keep-alive duration (for example `5m` or `0` to unload immediately)

        logprobs : typing.Optional[bool]
            Whether to return log probabilities of the output tokens

        top_logprobs : typing.Optional[int]
            Number of most likely tokens to return at each token position when logprobs are enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatResponse
            Chat response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ChatMessage, ChatMessageRole

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat(
                model="model",
                messages=[
                    ChatMessage(
                        role=ChatMessageRole.SYSTEM,
                        content="content",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chat(
            model=model,
            messages=messages,
            tools=tools,
            format=format,
            options=options,
            stream=stream,
            think=think,
            keep_alive=keep_alive,
            logprobs=logprobs,
            top_logprobs=top_logprobs,
            request_options=request_options,
        )
        return _response.data

    async def embed(
        self,
        *,
        model: str,
        input: EmbedRequestInput,
        truncate: typing.Optional[bool] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        keep_alive: typing.Optional[str] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbedResponse:
        """
        Creates vector embeddings representing the input text

        Parameters
        ----------
        model : str
            Model name

        input : EmbedRequestInput
            Text or array of texts to generate embeddings for

        truncate : typing.Optional[bool]
            If true, truncate inputs that exceed the context window. If false, returns an error.

        dimensions : typing.Optional[int]
            Number of dimensions to generate embeddings for

        keep_alive : typing.Optional[str]
            Model keep-alive duration

        options : typing.Optional[ModelOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbedResponse
            Vector embeddings for the input text

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.embed(
                model="embeddinggemma",
                input="Generate embeddings for this text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.embed(
            model=model,
            input=input,
            truncate=truncate,
            dimensions=dimensions,
            keep_alive=keep_alive,
            options=options,
            request_options=request_options,
        )
        return _response.data

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListResponse:
        """
        Fetch a list of models and their details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponse
            List available models

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def ps(self, *, request_options: typing.Optional[RequestOptions] = None) -> PsResponse:
        """
        Retrieve a list of models that are currently running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PsResponse
            Models currently loaded into memory

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ps()


        asyncio.run(main())
        """
        _response = await self._raw_client.ps(request_options=request_options)
        return _response.data

    async def show(
        self,
        *,
        model: str,
        verbose: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShowResponse:
        """
        Parameters
        ----------
        model : str
            Model name to show

        verbose : typing.Optional[bool]
            If true, includes large verbose fields in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShowResponse
            Model information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.show(
                model="gemma4",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show(model=model, verbose=verbose, request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        model: str,
        from_: typing.Optional[str] = OMIT,
        template: typing.Optional[str] = OMIT,
        renderer: typing.Optional[str] = OMIT,
        parser: typing.Optional[str] = OMIT,
        files: typing.Optional[typing.Dict[str, str]] = OMIT,
        draft_files: typing.Optional[typing.Dict[str, str]] = OMIT,
        license: typing.Optional[CreateRequestLicense] = OMIT,
        system: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        messages: typing.Optional[typing.Sequence[ChatMessage]] = OMIT,
        quantize: typing.Optional[str] = OMIT,
        draft_quantize: typing.Optional[str] = OMIT,
        requires: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusResponse:
        """
        Parameters
        ----------
        model : str
            Name for the model to create

        from_ : typing.Optional[str]
            Existing model to create from

        template : typing.Optional[str]
            Prompt template to use for the model

        renderer : typing.Optional[str]
            Name of the renderer for the model

        parser : typing.Optional[str]
            Name of the parser for the model

        files : typing.Optional[typing.Dict[str, str]]
            Source file names mapped to their SHA-256 digests. Split GGUF models must include each shard under its original split filename.

        draft_files : typing.Optional[typing.Dict[str, str]]
            Draft source file names mapped to their SHA-256 digests

        license : typing.Optional[CreateRequestLicense]
            License string or list of licenses for the model

        system : typing.Optional[str]
            System prompt to embed in the model

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value parameters for the model

        messages : typing.Optional[typing.Sequence[ChatMessage]]
            Message history to use for the model

        quantize : typing.Optional[str]
            Quantization level to apply during import (e.g. `nvfp4`)

        draft_quantize : typing.Optional[str]
            Quantization level to apply to draft weights during import

        requires : typing.Optional[str]
            Minimum Ollama version required by the model

        stream : typing.Optional[bool]
            Stream status updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Stream of create status updates

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create(
                model="mario",
                from_="gemma4",
                system="You are Mario from Super Mario Bros.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            model=model,
            from_=from_,
            template=template,
            renderer=renderer,
            parser=parser,
            files=files,
            draft_files=draft_files,
            license=license,
            system=system,
            parameters=parameters,
            messages=messages,
            quantize=quantize,
            draft_quantize=draft_quantize,
            requires=requires,
            stream=stream,
            request_options=request_options,
        )
        return _response.data

    async def create_blob(
        self,
        digest: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        digest : str
            SHA256 digest identifier, prefixed with `sha256:`

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.create_blob(digest, request=request, request_options=request_options)
        return _response.data

    async def head_blob(
        self, digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        digest : str
            SHA256 digest identifier, prefixed with `sha256:`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.head_blob(
                digest="digest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_blob(digest, request_options=request_options)
        return _response.headers

    async def copy(
        self, *, source: str, destination: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        source : str
            Existing model name to copy from

        destination : str
            New model name to create

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copy(
                source="gemma4",
                destination="gemma4-backup",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.copy(source=source, destination=destination, request_options=request_options)
        return _response.data

    async def pull(
        self,
        *,
        model: str,
        insecure: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusResponse:
        """
        Parameters
        ----------
        model : str
            Name of the model to download

        insecure : typing.Optional[bool]
            Allow downloading over insecure connections

        stream : typing.Optional[bool]
            Stream progress updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Pull status updates.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pull(
                model="gemma4",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pull(
            model=model, insecure=insecure, stream=stream, request_options=request_options
        )
        return _response.data

    async def push(
        self,
        *,
        model: str,
        insecure: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusResponse:
        """
        Parameters
        ----------
        model : str
            Name of the model to publish

        insecure : typing.Optional[bool]
            Allow publishing over insecure connections

        stream : typing.Optional[bool]
            Stream progress updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Push status updates.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.push(
                model="my-username/my-model",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.push(
            model=model, insecure=insecure, stream=stream, request_options=request_options
        )
        return _response.data

    async def delete(self, *, model: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        model : str
            Model name to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete(
                model="gemma4",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(model=model, request_options=request_options)
        return _response.data

    async def version(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionResponse:
        """
        Retrieve the version of the Ollama

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionResponse
            Version information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.version()


        asyncio.run(main())
        """
        _response = await self._raw_client.version(request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
