

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .account.client import AccountClient, AsyncAccountClient
    from .administration.client import AdministrationClient, AsyncAdministrationClient
    from .api_keys.client import ApiKeysClient, AsyncApiKeysClient
    from .authentication.client import AsyncAuthenticationClient, AuthenticationClient
    from .bots.client import AsyncBotsClient, BotsClient
    from .channels.client import AsyncChannelsClient, ChannelsClient
    from .events.client import AsyncEventsClient, EventsClient
    from .files.client import AsyncFilesClient, FilesClient
    from .folders.client import AsyncFoldersClient, FoldersClient
    from .jobs.client import AsyncJobsClient, JobsClient
    from .periodic_jobs.client import AsyncPeriodicJobsClient, PeriodicJobsClient
    from .public_shares.client import AsyncPublicSharesClient, PublicSharesClient
    from .rclone.client import AsyncRcloneClient, RcloneClient
    from .sessions.client import AsyncSessionsClient, SessionsClient
    from .shares.client import AsyncSharesClient, SharesClient
    from .storage.client import AsyncStorageClient, StorageClient
    from .system.client import AsyncSystemClient, SystemClient
    from .uploads.client import AsyncUploadsClient, UploadsClient
    from .users.client import AsyncUsersClient, UsersClient


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



    api_key : str
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
        api_key="YOUR_API_KEY",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            api_key=api_key,
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
        self._files: typing.Optional[FilesClient] = None
        self._public_shares: typing.Optional[PublicSharesClient] = None
        self._system: typing.Optional[SystemClient] = None
        self._authentication: typing.Optional[AuthenticationClient] = None
        self._account: typing.Optional[AccountClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._administration: typing.Optional[AdministrationClient] = None
        self._api_keys: typing.Optional[ApiKeysClient] = None
        self._sessions: typing.Optional[SessionsClient] = None
        self._channels: typing.Optional[ChannelsClient] = None
        self._bots: typing.Optional[BotsClient] = None
        self._events: typing.Optional[EventsClient] = None
        self._folders: typing.Optional[FoldersClient] = None
        self._uploads: typing.Optional[UploadsClient] = None
        self._shares: typing.Optional[SharesClient] = None
        self._jobs: typing.Optional[JobsClient] = None
        self._periodic_jobs: typing.Optional[PeriodicJobsClient] = None
        self._storage: typing.Optional[StorageClient] = None
        self._rclone: typing.Optional[RcloneClient] = None

    @property
    def files(self):
        if self._files is None:
            from .files.client import FilesClient

            self._files = FilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def public_shares(self):
        if self._public_shares is None:
            from .public_shares.client import PublicSharesClient

            self._public_shares = PublicSharesClient(client_wrapper=self._client_wrapper)
        return self._public_shares

    @property
    def system(self):
        if self._system is None:
            from .system.client import SystemClient

            self._system = SystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AuthenticationClient

            self._authentication = AuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def account(self):
        if self._account is None:
            from .account.client import AccountClient

            self._account = AccountClient(client_wrapper=self._client_wrapper)
        return self._account

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def administration(self):
        if self._administration is None:
            from .administration.client import AdministrationClient

            self._administration = AdministrationClient(client_wrapper=self._client_wrapper)
        return self._administration

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import ApiKeysClient

            self._api_keys = ApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import SessionsClient

            self._sessions = SessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def channels(self):
        if self._channels is None:
            from .channels.client import ChannelsClient

            self._channels = ChannelsClient(client_wrapper=self._client_wrapper)
        return self._channels

    @property
    def bots(self):
        if self._bots is None:
            from .bots.client import BotsClient

            self._bots = BotsClient(client_wrapper=self._client_wrapper)
        return self._bots

    @property
    def events(self):
        if self._events is None:
            from .events.client import EventsClient

            self._events = EventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import FoldersClient

            self._folders = FoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def uploads(self):
        if self._uploads is None:
            from .uploads.client import UploadsClient

            self._uploads = UploadsClient(client_wrapper=self._client_wrapper)
        return self._uploads

    @property
    def shares(self):
        if self._shares is None:
            from .shares.client import SharesClient

            self._shares = SharesClient(client_wrapper=self._client_wrapper)
        return self._shares

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import JobsClient

            self._jobs = JobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def periodic_jobs(self):
        if self._periodic_jobs is None:
            from .periodic_jobs.client import PeriodicJobsClient

            self._periodic_jobs = PeriodicJobsClient(client_wrapper=self._client_wrapper)
        return self._periodic_jobs

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import StorageClient

            self._storage = StorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def rclone(self):
        if self._rclone is None:
            from .rclone.client import RcloneClient

            self._rclone = RcloneClient(client_wrapper=self._client_wrapper)
        return self._rclone


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



    api_key : str
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
        api_key="YOUR_API_KEY",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            api_key=api_key,
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
        self._files: typing.Optional[AsyncFilesClient] = None
        self._public_shares: typing.Optional[AsyncPublicSharesClient] = None
        self._system: typing.Optional[AsyncSystemClient] = None
        self._authentication: typing.Optional[AsyncAuthenticationClient] = None
        self._account: typing.Optional[AsyncAccountClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._administration: typing.Optional[AsyncAdministrationClient] = None
        self._api_keys: typing.Optional[AsyncApiKeysClient] = None
        self._sessions: typing.Optional[AsyncSessionsClient] = None
        self._channels: typing.Optional[AsyncChannelsClient] = None
        self._bots: typing.Optional[AsyncBotsClient] = None
        self._events: typing.Optional[AsyncEventsClient] = None
        self._folders: typing.Optional[AsyncFoldersClient] = None
        self._uploads: typing.Optional[AsyncUploadsClient] = None
        self._shares: typing.Optional[AsyncSharesClient] = None
        self._jobs: typing.Optional[AsyncJobsClient] = None
        self._periodic_jobs: typing.Optional[AsyncPeriodicJobsClient] = None
        self._storage: typing.Optional[AsyncStorageClient] = None
        self._rclone: typing.Optional[AsyncRcloneClient] = None

    @property
    def files(self):
        if self._files is None:
            from .files.client import AsyncFilesClient

            self._files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def public_shares(self):
        if self._public_shares is None:
            from .public_shares.client import AsyncPublicSharesClient

            self._public_shares = AsyncPublicSharesClient(client_wrapper=self._client_wrapper)
        return self._public_shares

    @property
    def system(self):
        if self._system is None:
            from .system.client import AsyncSystemClient

            self._system = AsyncSystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AsyncAuthenticationClient

            self._authentication = AsyncAuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def account(self):
        if self._account is None:
            from .account.client import AsyncAccountClient

            self._account = AsyncAccountClient(client_wrapper=self._client_wrapper)
        return self._account

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def administration(self):
        if self._administration is None:
            from .administration.client import AsyncAdministrationClient

            self._administration = AsyncAdministrationClient(client_wrapper=self._client_wrapper)
        return self._administration

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import AsyncApiKeysClient

            self._api_keys = AsyncApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import AsyncSessionsClient

            self._sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def channels(self):
        if self._channels is None:
            from .channels.client import AsyncChannelsClient

            self._channels = AsyncChannelsClient(client_wrapper=self._client_wrapper)
        return self._channels

    @property
    def bots(self):
        if self._bots is None:
            from .bots.client import AsyncBotsClient

            self._bots = AsyncBotsClient(client_wrapper=self._client_wrapper)
        return self._bots

    @property
    def events(self):
        if self._events is None:
            from .events.client import AsyncEventsClient

            self._events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import AsyncFoldersClient

            self._folders = AsyncFoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def uploads(self):
        if self._uploads is None:
            from .uploads.client import AsyncUploadsClient

            self._uploads = AsyncUploadsClient(client_wrapper=self._client_wrapper)
        return self._uploads

    @property
    def shares(self):
        if self._shares is None:
            from .shares.client import AsyncSharesClient

            self._shares = AsyncSharesClient(client_wrapper=self._client_wrapper)
        return self._shares

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import AsyncJobsClient

            self._jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def periodic_jobs(self):
        if self._periodic_jobs is None:
            from .periodic_jobs.client import AsyncPeriodicJobsClient

            self._periodic_jobs = AsyncPeriodicJobsClient(client_wrapper=self._client_wrapper)
        return self._periodic_jobs

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import AsyncStorageClient

            self._storage = AsyncStorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def rclone(self):
        if self._rclone is None:
            from .rclone.client import AsyncRcloneClient

            self._rclone = AsyncRcloneClient(client_wrapper=self._client_wrapper)
        return self._rclone


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
