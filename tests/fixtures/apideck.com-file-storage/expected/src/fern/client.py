

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .drive_groups.client import AsyncDriveGroupsClient, DriveGroupsClient
    from .drives.client import AsyncDrivesClient, DrivesClient
    from .files.client import AsyncFilesClient, FilesClient
    from .folders.client import AsyncFoldersClient, FoldersClient
    from .shared_links.client import AsyncSharedLinksClient, SharedLinksClient
    from .upload_sessions.client import AsyncUploadSessionsClient, UploadSessionsClient


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



    apideck_consumer_id : str
    apideck_app_id : str
    apideck_service_id : typing.Optional[str]
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
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apideck_consumer_id: str,
        apideck_app_id: str,
        apideck_service_id: typing.Optional[str] = None,
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
            apideck_consumer_id=apideck_consumer_id,
            apideck_app_id=apideck_app_id,
            apideck_service_id=apideck_service_id,
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
        self._drive_groups: typing.Optional[DriveGroupsClient] = None
        self._drives: typing.Optional[DrivesClient] = None
        self._files: typing.Optional[FilesClient] = None
        self._folders: typing.Optional[FoldersClient] = None
        self._shared_links: typing.Optional[SharedLinksClient] = None
        self._upload_sessions: typing.Optional[UploadSessionsClient] = None

    @property
    def drive_groups(self):
        if self._drive_groups is None:
            from .drive_groups.client import DriveGroupsClient

            self._drive_groups = DriveGroupsClient(client_wrapper=self._client_wrapper)
        return self._drive_groups

    @property
    def drives(self):
        if self._drives is None:
            from .drives.client import DrivesClient

            self._drives = DrivesClient(client_wrapper=self._client_wrapper)
        return self._drives

    @property
    def files(self):
        if self._files is None:
            from .files.client import FilesClient

            self._files = FilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import FoldersClient

            self._folders = FoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def shared_links(self):
        if self._shared_links is None:
            from .shared_links.client import SharedLinksClient

            self._shared_links = SharedLinksClient(client_wrapper=self._client_wrapper)
        return self._shared_links

    @property
    def upload_sessions(self):
        if self._upload_sessions is None:
            from .upload_sessions.client import UploadSessionsClient

            self._upload_sessions = UploadSessionsClient(client_wrapper=self._client_wrapper)
        return self._upload_sessions


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



    apideck_consumer_id : str
    apideck_app_id : str
    apideck_service_id : typing.Optional[str]
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
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apideck_consumer_id: str,
        apideck_app_id: str,
        apideck_service_id: typing.Optional[str] = None,
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
            apideck_consumer_id=apideck_consumer_id,
            apideck_app_id=apideck_app_id,
            apideck_service_id=apideck_service_id,
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
        self._drive_groups: typing.Optional[AsyncDriveGroupsClient] = None
        self._drives: typing.Optional[AsyncDrivesClient] = None
        self._files: typing.Optional[AsyncFilesClient] = None
        self._folders: typing.Optional[AsyncFoldersClient] = None
        self._shared_links: typing.Optional[AsyncSharedLinksClient] = None
        self._upload_sessions: typing.Optional[AsyncUploadSessionsClient] = None

    @property
    def drive_groups(self):
        if self._drive_groups is None:
            from .drive_groups.client import AsyncDriveGroupsClient

            self._drive_groups = AsyncDriveGroupsClient(client_wrapper=self._client_wrapper)
        return self._drive_groups

    @property
    def drives(self):
        if self._drives is None:
            from .drives.client import AsyncDrivesClient

            self._drives = AsyncDrivesClient(client_wrapper=self._client_wrapper)
        return self._drives

    @property
    def files(self):
        if self._files is None:
            from .files.client import AsyncFilesClient

            self._files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import AsyncFoldersClient

            self._folders = AsyncFoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def shared_links(self):
        if self._shared_links is None:
            from .shared_links.client import AsyncSharedLinksClient

            self._shared_links = AsyncSharedLinksClient(client_wrapper=self._client_wrapper)
        return self._shared_links

    @property
    def upload_sessions(self):
        if self._upload_sessions is None:
            from .upload_sessions.client import AsyncUploadSessionsClient

            self._upload_sessions = AsyncUploadSessionsClient(client_wrapper=self._client_wrapper)
        return self._upload_sessions


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
