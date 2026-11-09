

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .assistants.client import AssistantsClient, AsyncAssistantsClient
    from .audio.client import AsyncAudioClient, AudioClient
    from .chat.client import AsyncChatClient, ChatClient
    from .completions.client import AsyncCompletionsClient, CompletionsClient
    from .embeddings.client import AsyncEmbeddingsClient, EmbeddingsClient
    from .files.client import AsyncFilesClient, FilesClient
    from .fine_tuning.client import AsyncFineTuningClient, FineTuningClient
    from .images.client import AsyncImagesClient, ImagesClient
    from .models.client import AsyncModelsClient, ModelsClient
    from .moderations.client import AsyncModerationsClient, ModerationsClient


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



    token : typing.Union[str, typing.Callable[[], str]]
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
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._chat: typing.Optional[ChatClient] = None
        self._completions: typing.Optional[CompletionsClient] = None
        self._images: typing.Optional[ImagesClient] = None
        self._embeddings: typing.Optional[EmbeddingsClient] = None
        self._audio: typing.Optional[AudioClient] = None
        self._files: typing.Optional[FilesClient] = None
        self._fine_tuning: typing.Optional[FineTuningClient] = None
        self._models: typing.Optional[ModelsClient] = None
        self._moderations: typing.Optional[ModerationsClient] = None
        self._assistants: typing.Optional[AssistantsClient] = None

    @property
    def chat(self):
        if self._chat is None:
            from .chat.client import ChatClient

            self._chat = ChatClient(client_wrapper=self._client_wrapper)
        return self._chat

    @property
    def completions(self):
        if self._completions is None:
            from .completions.client import CompletionsClient

            self._completions = CompletionsClient(client_wrapper=self._client_wrapper)
        return self._completions

    @property
    def images(self):
        if self._images is None:
            from .images.client import ImagesClient

            self._images = ImagesClient(client_wrapper=self._client_wrapper)
        return self._images

    @property
    def embeddings(self):
        if self._embeddings is None:
            from .embeddings.client import EmbeddingsClient

            self._embeddings = EmbeddingsClient(client_wrapper=self._client_wrapper)
        return self._embeddings

    @property
    def audio(self):
        if self._audio is None:
            from .audio.client import AudioClient

            self._audio = AudioClient(client_wrapper=self._client_wrapper)
        return self._audio

    @property
    def files(self):
        if self._files is None:
            from .files.client import FilesClient

            self._files = FilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def fine_tuning(self):
        if self._fine_tuning is None:
            from .fine_tuning.client import FineTuningClient

            self._fine_tuning = FineTuningClient(client_wrapper=self._client_wrapper)
        return self._fine_tuning

    @property
    def models(self):
        if self._models is None:
            from .models.client import ModelsClient

            self._models = ModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def moderations(self):
        if self._moderations is None:
            from .moderations.client import ModerationsClient

            self._moderations = ModerationsClient(client_wrapper=self._client_wrapper)
        return self._moderations

    @property
    def assistants(self):
        if self._assistants is None:
            from .assistants.client import AssistantsClient

            self._assistants = AssistantsClient(client_wrapper=self._client_wrapper)
        return self._assistants


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



    token : typing.Union[str, typing.Callable[[], str]]
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
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._chat: typing.Optional[AsyncChatClient] = None
        self._completions: typing.Optional[AsyncCompletionsClient] = None
        self._images: typing.Optional[AsyncImagesClient] = None
        self._embeddings: typing.Optional[AsyncEmbeddingsClient] = None
        self._audio: typing.Optional[AsyncAudioClient] = None
        self._files: typing.Optional[AsyncFilesClient] = None
        self._fine_tuning: typing.Optional[AsyncFineTuningClient] = None
        self._models: typing.Optional[AsyncModelsClient] = None
        self._moderations: typing.Optional[AsyncModerationsClient] = None
        self._assistants: typing.Optional[AsyncAssistantsClient] = None

    @property
    def chat(self):
        if self._chat is None:
            from .chat.client import AsyncChatClient

            self._chat = AsyncChatClient(client_wrapper=self._client_wrapper)
        return self._chat

    @property
    def completions(self):
        if self._completions is None:
            from .completions.client import AsyncCompletionsClient

            self._completions = AsyncCompletionsClient(client_wrapper=self._client_wrapper)
        return self._completions

    @property
    def images(self):
        if self._images is None:
            from .images.client import AsyncImagesClient

            self._images = AsyncImagesClient(client_wrapper=self._client_wrapper)
        return self._images

    @property
    def embeddings(self):
        if self._embeddings is None:
            from .embeddings.client import AsyncEmbeddingsClient

            self._embeddings = AsyncEmbeddingsClient(client_wrapper=self._client_wrapper)
        return self._embeddings

    @property
    def audio(self):
        if self._audio is None:
            from .audio.client import AsyncAudioClient

            self._audio = AsyncAudioClient(client_wrapper=self._client_wrapper)
        return self._audio

    @property
    def files(self):
        if self._files is None:
            from .files.client import AsyncFilesClient

            self._files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def fine_tuning(self):
        if self._fine_tuning is None:
            from .fine_tuning.client import AsyncFineTuningClient

            self._fine_tuning = AsyncFineTuningClient(client_wrapper=self._client_wrapper)
        return self._fine_tuning

    @property
    def models(self):
        if self._models is None:
            from .models.client import AsyncModelsClient

            self._models = AsyncModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def moderations(self):
        if self._moderations is None:
            from .moderations.client import AsyncModerationsClient

            self._moderations = AsyncModerationsClient(client_wrapper=self._client_wrapper)
        return self._moderations

    @property
    def assistants(self):
        if self._assistants is None:
            from .assistants.client import AsyncAssistantsClient

            self._assistants = AsyncAssistantsClient(client_wrapper=self._client_wrapper)
        return self._assistants


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
