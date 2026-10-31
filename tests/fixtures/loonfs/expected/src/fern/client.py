

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .capabilities.client import AsyncCapabilitiesClient, CapabilitiesClient
    from .changes.client import AsyncChangesClient, ChangesClient
    from .commits.client import AsyncCommitsClient, CommitsClient
    from .files.client import AsyncFilesClient, FilesClient
    from .inodes.client import AsyncInodesClient, InodesClient
    from .maintenance.client import AsyncMaintenanceClient, MaintenanceClient
    from .namespaces.client import AsyncNamespacesClient, NamespacesClient
    from .snapshots.client import AsyncSnapshotsClient, SnapshotsClient
    from .trash.client import AsyncTrashClient, TrashClient
    from .uploads.client import AsyncUploadsClient, UploadsClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    actor_id : typing.Optional[str]
    subject_id : typing.Optional[str]
    principal_scope : typing.Optional[str]
    principals : typing.Optional[str]
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
        actor_id="YOUR_ACTOR_ID",
        subject_id="YOUR_SUBJECT_ID",
        principal_scope="YOUR_PRINCIPAL_SCOPE",
        principals="YOUR_PRINCIPALS",
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        actor_id: typing.Optional[str] = None,
        subject_id: typing.Optional[str] = None,
        principal_scope: typing.Optional[str] = None,
        principals: typing.Optional[str] = None,
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
            base_url=base_url,
            actor_id=actor_id,
            subject_id=subject_id,
            principal_scope=principal_scope,
            principals=principals,
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
        self._capabilities: typing.Optional[CapabilitiesClient] = None
        self._namespaces: typing.Optional[NamespacesClient] = None
        self._changes: typing.Optional[ChangesClient] = None
        self._commits: typing.Optional[CommitsClient] = None
        self._files: typing.Optional[FilesClient] = None
        self._trash: typing.Optional[TrashClient] = None
        self._inodes: typing.Optional[InodesClient] = None
        self._snapshots: typing.Optional[SnapshotsClient] = None
        self._uploads: typing.Optional[UploadsClient] = None
        self._maintenance: typing.Optional[MaintenanceClient] = None

    @property
    def capabilities(self):
        if self._capabilities is None:
            from .capabilities.client import CapabilitiesClient

            self._capabilities = CapabilitiesClient(client_wrapper=self._client_wrapper)
        return self._capabilities

    @property
    def namespaces(self):
        if self._namespaces is None:
            from .namespaces.client import NamespacesClient

            self._namespaces = NamespacesClient(client_wrapper=self._client_wrapper)
        return self._namespaces

    @property
    def changes(self):
        if self._changes is None:
            from .changes.client import ChangesClient

            self._changes = ChangesClient(client_wrapper=self._client_wrapper)
        return self._changes

    @property
    def commits(self):
        if self._commits is None:
            from .commits.client import CommitsClient

            self._commits = CommitsClient(client_wrapper=self._client_wrapper)
        return self._commits

    @property
    def files(self):
        if self._files is None:
            from .files.client import FilesClient

            self._files = FilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def trash(self):
        if self._trash is None:
            from .trash.client import TrashClient

            self._trash = TrashClient(client_wrapper=self._client_wrapper)
        return self._trash

    @property
    def inodes(self):
        if self._inodes is None:
            from .inodes.client import InodesClient

            self._inodes = InodesClient(client_wrapper=self._client_wrapper)
        return self._inodes

    @property
    def snapshots(self):
        if self._snapshots is None:
            from .snapshots.client import SnapshotsClient

            self._snapshots = SnapshotsClient(client_wrapper=self._client_wrapper)
        return self._snapshots

    @property
    def uploads(self):
        if self._uploads is None:
            from .uploads.client import UploadsClient

            self._uploads = UploadsClient(client_wrapper=self._client_wrapper)
        return self._uploads

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import MaintenanceClient

            self._maintenance = MaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance


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

    actor_id : typing.Optional[str]
    subject_id : typing.Optional[str]
    principal_scope : typing.Optional[str]
    principals : typing.Optional[str]
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
        actor_id="YOUR_ACTOR_ID",
        subject_id="YOUR_SUBJECT_ID",
        principal_scope="YOUR_PRINCIPAL_SCOPE",
        principals="YOUR_PRINCIPALS",
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        actor_id: typing.Optional[str] = None,
        subject_id: typing.Optional[str] = None,
        principal_scope: typing.Optional[str] = None,
        principals: typing.Optional[str] = None,
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
            base_url=base_url,
            actor_id=actor_id,
            subject_id=subject_id,
            principal_scope=principal_scope,
            principals=principals,
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
        self._capabilities: typing.Optional[AsyncCapabilitiesClient] = None
        self._namespaces: typing.Optional[AsyncNamespacesClient] = None
        self._changes: typing.Optional[AsyncChangesClient] = None
        self._commits: typing.Optional[AsyncCommitsClient] = None
        self._files: typing.Optional[AsyncFilesClient] = None
        self._trash: typing.Optional[AsyncTrashClient] = None
        self._inodes: typing.Optional[AsyncInodesClient] = None
        self._snapshots: typing.Optional[AsyncSnapshotsClient] = None
        self._uploads: typing.Optional[AsyncUploadsClient] = None
        self._maintenance: typing.Optional[AsyncMaintenanceClient] = None

    @property
    def capabilities(self):
        if self._capabilities is None:
            from .capabilities.client import AsyncCapabilitiesClient

            self._capabilities = AsyncCapabilitiesClient(client_wrapper=self._client_wrapper)
        return self._capabilities

    @property
    def namespaces(self):
        if self._namespaces is None:
            from .namespaces.client import AsyncNamespacesClient

            self._namespaces = AsyncNamespacesClient(client_wrapper=self._client_wrapper)
        return self._namespaces

    @property
    def changes(self):
        if self._changes is None:
            from .changes.client import AsyncChangesClient

            self._changes = AsyncChangesClient(client_wrapper=self._client_wrapper)
        return self._changes

    @property
    def commits(self):
        if self._commits is None:
            from .commits.client import AsyncCommitsClient

            self._commits = AsyncCommitsClient(client_wrapper=self._client_wrapper)
        return self._commits

    @property
    def files(self):
        if self._files is None:
            from .files.client import AsyncFilesClient

            self._files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def trash(self):
        if self._trash is None:
            from .trash.client import AsyncTrashClient

            self._trash = AsyncTrashClient(client_wrapper=self._client_wrapper)
        return self._trash

    @property
    def inodes(self):
        if self._inodes is None:
            from .inodes.client import AsyncInodesClient

            self._inodes = AsyncInodesClient(client_wrapper=self._client_wrapper)
        return self._inodes

    @property
    def snapshots(self):
        if self._snapshots is None:
            from .snapshots.client import AsyncSnapshotsClient

            self._snapshots = AsyncSnapshotsClient(client_wrapper=self._client_wrapper)
        return self._snapshots

    @property
    def uploads(self):
        if self._uploads is None:
            from .uploads.client import AsyncUploadsClient

            self._uploads = AsyncUploadsClient(client_wrapper=self._client_wrapper)
        return self._uploads

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import AsyncMaintenanceClient

            self._maintenance = AsyncMaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance
