

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .analysis_snapshots.client import AnalysisSnapshotsClient, AsyncAnalysisSnapshotsClient
    from .auth.client import AsyncAuthClient, AuthClient
    from .games.client import AsyncGamesClient, GamesClient
    from .nnue.client import AsyncNnueClient, NnueClient
    from .public_games.client import AsyncPublicGamesClient, PublicGamesClient
    from .rooms.client import AsyncRoomsClient, RoomsClient
    from .user_settings.client import AsyncUserSettingsClient, UserSettingsClient


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
        self._auth: typing.Optional[AuthClient] = None
        self._games: typing.Optional[GamesClient] = None
        self._analysis_snapshots: typing.Optional[AnalysisSnapshotsClient] = None
        self._nnue: typing.Optional[NnueClient] = None
        self._public_games: typing.Optional[PublicGamesClient] = None
        self._user_settings: typing.Optional[UserSettingsClient] = None
        self._rooms: typing.Optional[RoomsClient] = None

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AuthClient

            self._auth = AuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def games(self):
        if self._games is None:
            from .games.client import GamesClient

            self._games = GamesClient(client_wrapper=self._client_wrapper)
        return self._games

    @property
    def analysis_snapshots(self):
        if self._analysis_snapshots is None:
            from .analysis_snapshots.client import AnalysisSnapshotsClient

            self._analysis_snapshots = AnalysisSnapshotsClient(client_wrapper=self._client_wrapper)
        return self._analysis_snapshots

    @property
    def nnue(self):
        if self._nnue is None:
            from .nnue.client import NnueClient

            self._nnue = NnueClient(client_wrapper=self._client_wrapper)
        return self._nnue

    @property
    def public_games(self):
        if self._public_games is None:
            from .public_games.client import PublicGamesClient

            self._public_games = PublicGamesClient(client_wrapper=self._client_wrapper)
        return self._public_games

    @property
    def user_settings(self):
        if self._user_settings is None:
            from .user_settings.client import UserSettingsClient

            self._user_settings = UserSettingsClient(client_wrapper=self._client_wrapper)
        return self._user_settings

    @property
    def rooms(self):
        if self._rooms is None:
            from .rooms.client import RoomsClient

            self._rooms = RoomsClient(client_wrapper=self._client_wrapper)
        return self._rooms


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
        self._auth: typing.Optional[AsyncAuthClient] = None
        self._games: typing.Optional[AsyncGamesClient] = None
        self._analysis_snapshots: typing.Optional[AsyncAnalysisSnapshotsClient] = None
        self._nnue: typing.Optional[AsyncNnueClient] = None
        self._public_games: typing.Optional[AsyncPublicGamesClient] = None
        self._user_settings: typing.Optional[AsyncUserSettingsClient] = None
        self._rooms: typing.Optional[AsyncRoomsClient] = None

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AsyncAuthClient

            self._auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def games(self):
        if self._games is None:
            from .games.client import AsyncGamesClient

            self._games = AsyncGamesClient(client_wrapper=self._client_wrapper)
        return self._games

    @property
    def analysis_snapshots(self):
        if self._analysis_snapshots is None:
            from .analysis_snapshots.client import AsyncAnalysisSnapshotsClient

            self._analysis_snapshots = AsyncAnalysisSnapshotsClient(client_wrapper=self._client_wrapper)
        return self._analysis_snapshots

    @property
    def nnue(self):
        if self._nnue is None:
            from .nnue.client import AsyncNnueClient

            self._nnue = AsyncNnueClient(client_wrapper=self._client_wrapper)
        return self._nnue

    @property
    def public_games(self):
        if self._public_games is None:
            from .public_games.client import AsyncPublicGamesClient

            self._public_games = AsyncPublicGamesClient(client_wrapper=self._client_wrapper)
        return self._public_games

    @property
    def user_settings(self):
        if self._user_settings is None:
            from .user_settings.client import AsyncUserSettingsClient

            self._user_settings = AsyncUserSettingsClient(client_wrapper=self._client_wrapper)
        return self._user_settings

    @property
    def rooms(self):
        if self._rooms is None:
            from .rooms.client import AsyncRoomsClient

            self._rooms = AsyncRoomsClient(client_wrapper=self._client_wrapper)
        return self._rooms
