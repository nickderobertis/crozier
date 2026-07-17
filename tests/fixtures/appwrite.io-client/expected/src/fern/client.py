

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .account.client import AccountClient, AsyncAccountClient
    from .avatars.client import AsyncAvatarsClient, AvatarsClient
    from .database.client import AsyncDatabaseClient, DatabaseClient
    from .functions.client import AsyncFunctionsClient, FunctionsClient
    from .locale.client import AsyncLocaleClient, LocaleClient
    from .storage.client import AsyncStorageClient, StorageClient
    from .teams.client import AsyncTeamsClient, TeamsClient


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



    appwrite_locale : str
    appwrite_project : str
    api_key : str
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
        appwrite_locale="YOUR_APPWRITE_LOCALE",
        appwrite_project="YOUR_APPWRITE_PROJECT",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        appwrite_locale: str,
        appwrite_project: str,
        api_key: str,
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
            appwrite_locale=appwrite_locale,
            appwrite_project=appwrite_project,
            api_key=api_key,
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
        self._account: typing.Optional[AccountClient] = None
        self._avatars: typing.Optional[AvatarsClient] = None
        self._database: typing.Optional[DatabaseClient] = None
        self._functions: typing.Optional[FunctionsClient] = None
        self._locale: typing.Optional[LocaleClient] = None
        self._storage: typing.Optional[StorageClient] = None
        self._teams: typing.Optional[TeamsClient] = None

    @property
    def account(self):
        if self._account is None:
            from .account.client import AccountClient

            self._account = AccountClient(client_wrapper=self._client_wrapper)
        return self._account

    @property
    def avatars(self):
        if self._avatars is None:
            from .avatars.client import AvatarsClient

            self._avatars = AvatarsClient(client_wrapper=self._client_wrapper)
        return self._avatars

    @property
    def database(self):
        if self._database is None:
            from .database.client import DatabaseClient

            self._database = DatabaseClient(client_wrapper=self._client_wrapper)
        return self._database

    @property
    def functions(self):
        if self._functions is None:
            from .functions.client import FunctionsClient

            self._functions = FunctionsClient(client_wrapper=self._client_wrapper)
        return self._functions

    @property
    def locale(self):
        if self._locale is None:
            from .locale.client import LocaleClient

            self._locale = LocaleClient(client_wrapper=self._client_wrapper)
        return self._locale

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import StorageClient

            self._storage = StorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def teams(self):
        if self._teams is None:
            from .teams.client import TeamsClient

            self._teams = TeamsClient(client_wrapper=self._client_wrapper)
        return self._teams


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



    appwrite_locale : str
    appwrite_project : str
    api_key : str
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
        appwrite_locale="YOUR_APPWRITE_LOCALE",
        appwrite_project="YOUR_APPWRITE_PROJECT",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        appwrite_locale: str,
        appwrite_project: str,
        api_key: str,
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
            appwrite_locale=appwrite_locale,
            appwrite_project=appwrite_project,
            api_key=api_key,
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
        self._account: typing.Optional[AsyncAccountClient] = None
        self._avatars: typing.Optional[AsyncAvatarsClient] = None
        self._database: typing.Optional[AsyncDatabaseClient] = None
        self._functions: typing.Optional[AsyncFunctionsClient] = None
        self._locale: typing.Optional[AsyncLocaleClient] = None
        self._storage: typing.Optional[AsyncStorageClient] = None
        self._teams: typing.Optional[AsyncTeamsClient] = None

    @property
    def account(self):
        if self._account is None:
            from .account.client import AsyncAccountClient

            self._account = AsyncAccountClient(client_wrapper=self._client_wrapper)
        return self._account

    @property
    def avatars(self):
        if self._avatars is None:
            from .avatars.client import AsyncAvatarsClient

            self._avatars = AsyncAvatarsClient(client_wrapper=self._client_wrapper)
        return self._avatars

    @property
    def database(self):
        if self._database is None:
            from .database.client import AsyncDatabaseClient

            self._database = AsyncDatabaseClient(client_wrapper=self._client_wrapper)
        return self._database

    @property
    def functions(self):
        if self._functions is None:
            from .functions.client import AsyncFunctionsClient

            self._functions = AsyncFunctionsClient(client_wrapper=self._client_wrapper)
        return self._functions

    @property
    def locale(self):
        if self._locale is None:
            from .locale.client import AsyncLocaleClient

            self._locale = AsyncLocaleClient(client_wrapper=self._client_wrapper)
        return self._locale

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import AsyncStorageClient

            self._storage = AsyncStorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def teams(self):
        if self._teams is None:
            from .teams.client import AsyncTeamsClient

            self._teams = AsyncTeamsClient(client_wrapper=self._client_wrapper)
        return self._teams


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
