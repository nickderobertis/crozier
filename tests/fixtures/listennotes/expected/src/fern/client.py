

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .directory_api.client import AsyncDirectoryApiClient, DirectoryApiClient
    from .insights_api.client import AsyncInsightsApiClient, InsightsApiClient
    from .playlist_api.client import AsyncPlaylistApiClient, PlaylistApiClient
    from .podcaster_api.client import AsyncPodcasterApiClient, PodcasterApiClient
    from .search_api.client import AsyncSearchApiClient, SearchApiClient


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



    listen_api_key : str
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
        listen_api_key="YOUR_LISTEN_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        listen_api_key: str,
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
            listen_api_key=listen_api_key,
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
        self._directory_api: typing.Optional[DirectoryApiClient] = None
        self._playlist_api: typing.Optional[PlaylistApiClient] = None
        self._insights_api: typing.Optional[InsightsApiClient] = None
        self._podcaster_api: typing.Optional[PodcasterApiClient] = None
        self._search_api: typing.Optional[SearchApiClient] = None

    @property
    def directory_api(self):
        if self._directory_api is None:
            from .directory_api.client import DirectoryApiClient

            self._directory_api = DirectoryApiClient(client_wrapper=self._client_wrapper)
        return self._directory_api

    @property
    def playlist_api(self):
        if self._playlist_api is None:
            from .playlist_api.client import PlaylistApiClient

            self._playlist_api = PlaylistApiClient(client_wrapper=self._client_wrapper)
        return self._playlist_api

    @property
    def insights_api(self):
        if self._insights_api is None:
            from .insights_api.client import InsightsApiClient

            self._insights_api = InsightsApiClient(client_wrapper=self._client_wrapper)
        return self._insights_api

    @property
    def podcaster_api(self):
        if self._podcaster_api is None:
            from .podcaster_api.client import PodcasterApiClient

            self._podcaster_api = PodcasterApiClient(client_wrapper=self._client_wrapper)
        return self._podcaster_api

    @property
    def search_api(self):
        if self._search_api is None:
            from .search_api.client import SearchApiClient

            self._search_api = SearchApiClient(client_wrapper=self._client_wrapper)
        return self._search_api


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



    listen_api_key : str
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
        listen_api_key="YOUR_LISTEN_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        listen_api_key: str,
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
            listen_api_key=listen_api_key,
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
        self._directory_api: typing.Optional[AsyncDirectoryApiClient] = None
        self._playlist_api: typing.Optional[AsyncPlaylistApiClient] = None
        self._insights_api: typing.Optional[AsyncInsightsApiClient] = None
        self._podcaster_api: typing.Optional[AsyncPodcasterApiClient] = None
        self._search_api: typing.Optional[AsyncSearchApiClient] = None

    @property
    def directory_api(self):
        if self._directory_api is None:
            from .directory_api.client import AsyncDirectoryApiClient

            self._directory_api = AsyncDirectoryApiClient(client_wrapper=self._client_wrapper)
        return self._directory_api

    @property
    def playlist_api(self):
        if self._playlist_api is None:
            from .playlist_api.client import AsyncPlaylistApiClient

            self._playlist_api = AsyncPlaylistApiClient(client_wrapper=self._client_wrapper)
        return self._playlist_api

    @property
    def insights_api(self):
        if self._insights_api is None:
            from .insights_api.client import AsyncInsightsApiClient

            self._insights_api = AsyncInsightsApiClient(client_wrapper=self._client_wrapper)
        return self._insights_api

    @property
    def podcaster_api(self):
        if self._podcaster_api is None:
            from .podcaster_api.client import AsyncPodcasterApiClient

            self._podcaster_api = AsyncPodcasterApiClient(client_wrapper=self._client_wrapper)
        return self._podcaster_api

    @property
    def search_api(self):
        if self._search_api is None:
            from .search_api.client import AsyncSearchApiClient

            self._search_api = AsyncSearchApiClient(client_wrapper=self._client_wrapper)
        return self._search_api


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
