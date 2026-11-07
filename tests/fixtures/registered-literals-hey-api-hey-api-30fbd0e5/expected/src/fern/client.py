

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .alias.client import AliasClient, AsyncAliasClient
    from .blobs.client import AsyncBlobsClient, BlobsClient
    from .connections.client import AsyncConnectionsClient, ConnectionsClient
    from .emails.client import AsyncEmailsClient, EmailsClient
    from .env_var_groups.client import AsyncEnvVarGroupsClient, EnvVarGroupsClient
    from .files.client import AsyncFilesClient, FilesClient
    from .me.client import AsyncMeClient, MeClient
    from .orgs.client import AsyncOrgsClient, OrgsClient
    from .sqlite.client import AsyncSqliteClient, SqliteClient
    from .telemetry.client import AsyncTelemetryClient, TelemetryClient
    from .users.client import AsyncUsersClient, UsersClient
    from .val.client import AsyncValClient, ValClient
    from .vals.client import AsyncValsClient, ValsClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



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
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._alias: typing.Optional[AliasClient] = None
        self._me: typing.Optional[MeClient] = None
        self._blobs: typing.Optional[BlobsClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._sqlite: typing.Optional[SqliteClient] = None
        self._emails: typing.Optional[EmailsClient] = None
        self._telemetry: typing.Optional[TelemetryClient] = None
        self._vals: typing.Optional[ValsClient] = None
        self._files: typing.Optional[FilesClient] = None
        self._orgs: typing.Optional[OrgsClient] = None
        self._connections: typing.Optional[ConnectionsClient] = None
        self._val: typing.Optional[ValClient] = None
        self._env_var_groups: typing.Optional[EnvVarGroupsClient] = None

    @property
    def alias(self):
        if self._alias is None:
            from .alias.client import AliasClient

            self._alias = AliasClient(client_wrapper=self._client_wrapper)
        return self._alias

    @property
    def me(self):
        if self._me is None:
            from .me.client import MeClient

            self._me = MeClient(client_wrapper=self._client_wrapper)
        return self._me

    @property
    def blobs(self):
        if self._blobs is None:
            from .blobs.client import BlobsClient

            self._blobs = BlobsClient(client_wrapper=self._client_wrapper)
        return self._blobs

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def sqlite(self):
        if self._sqlite is None:
            from .sqlite.client import SqliteClient

            self._sqlite = SqliteClient(client_wrapper=self._client_wrapper)
        return self._sqlite

    @property
    def emails(self):
        if self._emails is None:
            from .emails.client import EmailsClient

            self._emails = EmailsClient(client_wrapper=self._client_wrapper)
        return self._emails

    @property
    def telemetry(self):
        if self._telemetry is None:
            from .telemetry.client import TelemetryClient

            self._telemetry = TelemetryClient(client_wrapper=self._client_wrapper)
        return self._telemetry

    @property
    def vals(self):
        if self._vals is None:
            from .vals.client import ValsClient

            self._vals = ValsClient(client_wrapper=self._client_wrapper)
        return self._vals

    @property
    def files(self):
        if self._files is None:
            from .files.client import FilesClient

            self._files = FilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def orgs(self):
        if self._orgs is None:
            from .orgs.client import OrgsClient

            self._orgs = OrgsClient(client_wrapper=self._client_wrapper)
        return self._orgs

    @property
    def connections(self):
        if self._connections is None:
            from .connections.client import ConnectionsClient

            self._connections = ConnectionsClient(client_wrapper=self._client_wrapper)
        return self._connections

    @property
    def val(self):
        if self._val is None:
            from .val.client import ValClient

            self._val = ValClient(client_wrapper=self._client_wrapper)
        return self._val

    @property
    def env_var_groups(self):
        if self._env_var_groups is None:
            from .env_var_groups.client import EnvVarGroupsClient

            self._env_var_groups = EnvVarGroupsClient(client_wrapper=self._client_wrapper)
        return self._env_var_groups


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



        Defaults to FernApiEnvironment.PRODUCTION



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
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._alias: typing.Optional[AsyncAliasClient] = None
        self._me: typing.Optional[AsyncMeClient] = None
        self._blobs: typing.Optional[AsyncBlobsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._sqlite: typing.Optional[AsyncSqliteClient] = None
        self._emails: typing.Optional[AsyncEmailsClient] = None
        self._telemetry: typing.Optional[AsyncTelemetryClient] = None
        self._vals: typing.Optional[AsyncValsClient] = None
        self._files: typing.Optional[AsyncFilesClient] = None
        self._orgs: typing.Optional[AsyncOrgsClient] = None
        self._connections: typing.Optional[AsyncConnectionsClient] = None
        self._val: typing.Optional[AsyncValClient] = None
        self._env_var_groups: typing.Optional[AsyncEnvVarGroupsClient] = None

    @property
    def alias(self):
        if self._alias is None:
            from .alias.client import AsyncAliasClient

            self._alias = AsyncAliasClient(client_wrapper=self._client_wrapper)
        return self._alias

    @property
    def me(self):
        if self._me is None:
            from .me.client import AsyncMeClient

            self._me = AsyncMeClient(client_wrapper=self._client_wrapper)
        return self._me

    @property
    def blobs(self):
        if self._blobs is None:
            from .blobs.client import AsyncBlobsClient

            self._blobs = AsyncBlobsClient(client_wrapper=self._client_wrapper)
        return self._blobs

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def sqlite(self):
        if self._sqlite is None:
            from .sqlite.client import AsyncSqliteClient

            self._sqlite = AsyncSqliteClient(client_wrapper=self._client_wrapper)
        return self._sqlite

    @property
    def emails(self):
        if self._emails is None:
            from .emails.client import AsyncEmailsClient

            self._emails = AsyncEmailsClient(client_wrapper=self._client_wrapper)
        return self._emails

    @property
    def telemetry(self):
        if self._telemetry is None:
            from .telemetry.client import AsyncTelemetryClient

            self._telemetry = AsyncTelemetryClient(client_wrapper=self._client_wrapper)
        return self._telemetry

    @property
    def vals(self):
        if self._vals is None:
            from .vals.client import AsyncValsClient

            self._vals = AsyncValsClient(client_wrapper=self._client_wrapper)
        return self._vals

    @property
    def files(self):
        if self._files is None:
            from .files.client import AsyncFilesClient

            self._files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def orgs(self):
        if self._orgs is None:
            from .orgs.client import AsyncOrgsClient

            self._orgs = AsyncOrgsClient(client_wrapper=self._client_wrapper)
        return self._orgs

    @property
    def connections(self):
        if self._connections is None:
            from .connections.client import AsyncConnectionsClient

            self._connections = AsyncConnectionsClient(client_wrapper=self._client_wrapper)
        return self._connections

    @property
    def val(self):
        if self._val is None:
            from .val.client import AsyncValClient

            self._val = AsyncValClient(client_wrapper=self._client_wrapper)
        return self._val

    @property
    def env_var_groups(self):
        if self._env_var_groups is None:
            from .env_var_groups.client import AsyncEnvVarGroupsClient

            self._env_var_groups = AsyncEnvVarGroupsClient(client_wrapper=self._client_wrapper)
        return self._env_var_groups


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
