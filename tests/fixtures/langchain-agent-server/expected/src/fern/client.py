

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .a2a.client import A2AClient, AsyncA2AClient
    from .assistants.client import AssistantsClient, AsyncAssistantsClient
    from .crons.client import AsyncCronsClient, CronsClient
    from .mcp.client import AsyncMcpClient, McpClient
    from .stateless_runs.client import AsyncStatelessRunsClient, StatelessRunsClient
    from .store.client import AsyncStoreClient, StoreClient
    from .streaming.client import AsyncStreamingClient, StreamingClient
    from .system.client import AsyncSystemClient, SystemClient
    from .thread_runs.client import AsyncThreadRunsClient, ThreadRunsClient
    from .threads.client import AsyncThreadsClient, ThreadsClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
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
        self._assistants: typing.Optional[AssistantsClient] = None
        self._threads: typing.Optional[ThreadsClient] = None
        self._streaming: typing.Optional[StreamingClient] = None
        self._thread_runs: typing.Optional[ThreadRunsClient] = None
        self._crons: typing.Optional[CronsClient] = None
        self._stateless_runs: typing.Optional[StatelessRunsClient] = None
        self._store: typing.Optional[StoreClient] = None
        self._a2a: typing.Optional[A2AClient] = None
        self._mcp: typing.Optional[McpClient] = None
        self._system: typing.Optional[SystemClient] = None

    @property
    def assistants(self):
        if self._assistants is None:
            from .assistants.client import AssistantsClient

            self._assistants = AssistantsClient(client_wrapper=self._client_wrapper)
        return self._assistants

    @property
    def threads(self):
        if self._threads is None:
            from .threads.client import ThreadsClient

            self._threads = ThreadsClient(client_wrapper=self._client_wrapper)
        return self._threads

    @property
    def streaming(self):
        if self._streaming is None:
            from .streaming.client import StreamingClient

            self._streaming = StreamingClient(client_wrapper=self._client_wrapper)
        return self._streaming

    @property
    def thread_runs(self):
        if self._thread_runs is None:
            from .thread_runs.client import ThreadRunsClient

            self._thread_runs = ThreadRunsClient(client_wrapper=self._client_wrapper)
        return self._thread_runs

    @property
    def crons(self):
        if self._crons is None:
            from .crons.client import CronsClient

            self._crons = CronsClient(client_wrapper=self._client_wrapper)
        return self._crons

    @property
    def stateless_runs(self):
        if self._stateless_runs is None:
            from .stateless_runs.client import StatelessRunsClient

            self._stateless_runs = StatelessRunsClient(client_wrapper=self._client_wrapper)
        return self._stateless_runs

    @property
    def store(self):
        if self._store is None:
            from .store.client import StoreClient

            self._store = StoreClient(client_wrapper=self._client_wrapper)
        return self._store

    @property
    def a2a(self):
        if self._a2a is None:
            from .a2a.client import A2AClient

            self._a2a = A2AClient(client_wrapper=self._client_wrapper)
        return self._a2a

    @property
    def mcp(self):
        if self._mcp is None:
            from .mcp.client import McpClient

            self._mcp = McpClient(client_wrapper=self._client_wrapper)
        return self._mcp

    @property
    def system(self):
        if self._system is None:
            from .system.client import SystemClient

            self._system = SystemClient(client_wrapper=self._client_wrapper)
        return self._system


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
    base_url : str
        The base url to use for requests from the client.

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

    client = AsyncFernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
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
        self._assistants: typing.Optional[AsyncAssistantsClient] = None
        self._threads: typing.Optional[AsyncThreadsClient] = None
        self._streaming: typing.Optional[AsyncStreamingClient] = None
        self._thread_runs: typing.Optional[AsyncThreadRunsClient] = None
        self._crons: typing.Optional[AsyncCronsClient] = None
        self._stateless_runs: typing.Optional[AsyncStatelessRunsClient] = None
        self._store: typing.Optional[AsyncStoreClient] = None
        self._a2a: typing.Optional[AsyncA2AClient] = None
        self._mcp: typing.Optional[AsyncMcpClient] = None
        self._system: typing.Optional[AsyncSystemClient] = None

    @property
    def assistants(self):
        if self._assistants is None:
            from .assistants.client import AsyncAssistantsClient

            self._assistants = AsyncAssistantsClient(client_wrapper=self._client_wrapper)
        return self._assistants

    @property
    def threads(self):
        if self._threads is None:
            from .threads.client import AsyncThreadsClient

            self._threads = AsyncThreadsClient(client_wrapper=self._client_wrapper)
        return self._threads

    @property
    def streaming(self):
        if self._streaming is None:
            from .streaming.client import AsyncStreamingClient

            self._streaming = AsyncStreamingClient(client_wrapper=self._client_wrapper)
        return self._streaming

    @property
    def thread_runs(self):
        if self._thread_runs is None:
            from .thread_runs.client import AsyncThreadRunsClient

            self._thread_runs = AsyncThreadRunsClient(client_wrapper=self._client_wrapper)
        return self._thread_runs

    @property
    def crons(self):
        if self._crons is None:
            from .crons.client import AsyncCronsClient

            self._crons = AsyncCronsClient(client_wrapper=self._client_wrapper)
        return self._crons

    @property
    def stateless_runs(self):
        if self._stateless_runs is None:
            from .stateless_runs.client import AsyncStatelessRunsClient

            self._stateless_runs = AsyncStatelessRunsClient(client_wrapper=self._client_wrapper)
        return self._stateless_runs

    @property
    def store(self):
        if self._store is None:
            from .store.client import AsyncStoreClient

            self._store = AsyncStoreClient(client_wrapper=self._client_wrapper)
        return self._store

    @property
    def a2a(self):
        if self._a2a is None:
            from .a2a.client import AsyncA2AClient

            self._a2a = AsyncA2AClient(client_wrapper=self._client_wrapper)
        return self._a2a

    @property
    def mcp(self):
        if self._mcp is None:
            from .mcp.client import AsyncMcpClient

            self._mcp = AsyncMcpClient(client_wrapper=self._client_wrapper)
        return self._mcp

    @property
    def system(self):
        if self._system is None:
            from .system.client import AsyncSystemClient

            self._system = AsyncSystemClient(client_wrapper=self._client_wrapper)
        return self._system
