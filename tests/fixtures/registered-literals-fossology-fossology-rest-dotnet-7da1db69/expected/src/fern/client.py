

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .admin.client import AdminClient, AsyncAdminClient
    from .auth.client import AsyncAuthClient, AuthClient
    from .copyrights.client import AsyncCopyrightsClient, CopyrightsClient
    from .folders.client import AsyncFoldersClient, FoldersClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .info.client import AsyncInfoClient, InfoClient
    from .job.client import AsyncJobClient, JobClient
    from .license.client import AsyncLicenseClient, LicenseClient
    from .maintenance.client import AsyncMaintenanceClient, MaintenanceClient
    from .organize.client import AsyncOrganizeClient, OrganizeClient
    from .overview.client import AsyncOverviewClient, OverviewClient
    from .report.client import AsyncReportClient, ReportClient
    from .search.client import AsyncSearchClient, SearchClient
    from .upload.client import AsyncUploadClient, UploadClient
    from .user.client import AsyncUserClient, UserClient


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
        self._auth: typing.Optional[AuthClient] = None
        self._info: typing.Optional[InfoClient] = None
        self._maintenance: typing.Optional[MaintenanceClient] = None
        self._admin: typing.Optional[AdminClient] = None
        self._license: typing.Optional[LicenseClient] = None
        self._upload: typing.Optional[UploadClient] = None
        self._search: typing.Optional[SearchClient] = None
        self._user: typing.Optional[UserClient] = None
        self._copyrights: typing.Optional[CopyrightsClient] = None
        self._job: typing.Optional[JobClient] = None
        self._folders: typing.Optional[FoldersClient] = None
        self._organize: typing.Optional[OrganizeClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._report: typing.Optional[ReportClient] = None
        self._overview: typing.Optional[OverviewClient] = None

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AuthClient

            self._auth = AuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def info(self):
        if self._info is None:
            from .info.client import InfoClient

            self._info = InfoClient(client_wrapper=self._client_wrapper)
        return self._info

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import MaintenanceClient

            self._maintenance = MaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance

    @property
    def admin(self):
        if self._admin is None:
            from .admin.client import AdminClient

            self._admin = AdminClient(client_wrapper=self._client_wrapper)
        return self._admin

    @property
    def license(self):
        if self._license is None:
            from .license.client import LicenseClient

            self._license = LicenseClient(client_wrapper=self._client_wrapper)
        return self._license

    @property
    def upload(self):
        if self._upload is None:
            from .upload.client import UploadClient

            self._upload = UploadClient(client_wrapper=self._client_wrapper)
        return self._upload

    @property
    def search(self):
        if self._search is None:
            from .search.client import SearchClient

            self._search = SearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def copyrights(self):
        if self._copyrights is None:
            from .copyrights.client import CopyrightsClient

            self._copyrights = CopyrightsClient(client_wrapper=self._client_wrapper)
        return self._copyrights

    @property
    def job(self):
        if self._job is None:
            from .job.client import JobClient

            self._job = JobClient(client_wrapper=self._client_wrapper)
        return self._job

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import FoldersClient

            self._folders = FoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def organize(self):
        if self._organize is None:
            from .organize.client import OrganizeClient

            self._organize = OrganizeClient(client_wrapper=self._client_wrapper)
        return self._organize

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def report(self):
        if self._report is None:
            from .report.client import ReportClient

            self._report = ReportClient(client_wrapper=self._client_wrapper)
        return self._report

    @property
    def overview(self):
        if self._overview is None:
            from .overview.client import OverviewClient

            self._overview = OverviewClient(client_wrapper=self._client_wrapper)
        return self._overview


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
        self._auth: typing.Optional[AsyncAuthClient] = None
        self._info: typing.Optional[AsyncInfoClient] = None
        self._maintenance: typing.Optional[AsyncMaintenanceClient] = None
        self._admin: typing.Optional[AsyncAdminClient] = None
        self._license: typing.Optional[AsyncLicenseClient] = None
        self._upload: typing.Optional[AsyncUploadClient] = None
        self._search: typing.Optional[AsyncSearchClient] = None
        self._user: typing.Optional[AsyncUserClient] = None
        self._copyrights: typing.Optional[AsyncCopyrightsClient] = None
        self._job: typing.Optional[AsyncJobClient] = None
        self._folders: typing.Optional[AsyncFoldersClient] = None
        self._organize: typing.Optional[AsyncOrganizeClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._report: typing.Optional[AsyncReportClient] = None
        self._overview: typing.Optional[AsyncOverviewClient] = None

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AsyncAuthClient

            self._auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def info(self):
        if self._info is None:
            from .info.client import AsyncInfoClient

            self._info = AsyncInfoClient(client_wrapper=self._client_wrapper)
        return self._info

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import AsyncMaintenanceClient

            self._maintenance = AsyncMaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance

    @property
    def admin(self):
        if self._admin is None:
            from .admin.client import AsyncAdminClient

            self._admin = AsyncAdminClient(client_wrapper=self._client_wrapper)
        return self._admin

    @property
    def license(self):
        if self._license is None:
            from .license.client import AsyncLicenseClient

            self._license = AsyncLicenseClient(client_wrapper=self._client_wrapper)
        return self._license

    @property
    def upload(self):
        if self._upload is None:
            from .upload.client import AsyncUploadClient

            self._upload = AsyncUploadClient(client_wrapper=self._client_wrapper)
        return self._upload

    @property
    def search(self):
        if self._search is None:
            from .search.client import AsyncSearchClient

            self._search = AsyncSearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def copyrights(self):
        if self._copyrights is None:
            from .copyrights.client import AsyncCopyrightsClient

            self._copyrights = AsyncCopyrightsClient(client_wrapper=self._client_wrapper)
        return self._copyrights

    @property
    def job(self):
        if self._job is None:
            from .job.client import AsyncJobClient

            self._job = AsyncJobClient(client_wrapper=self._client_wrapper)
        return self._job

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import AsyncFoldersClient

            self._folders = AsyncFoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def organize(self):
        if self._organize is None:
            from .organize.client import AsyncOrganizeClient

            self._organize = AsyncOrganizeClient(client_wrapper=self._client_wrapper)
        return self._organize

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def report(self):
        if self._report is None:
            from .report.client import AsyncReportClient

            self._report = AsyncReportClient(client_wrapper=self._client_wrapper)
        return self._report

    @property
    def overview(self):
        if self._overview is None:
            from .overview.client import AsyncOverviewClient

            self._overview = AsyncOverviewClient(client_wrapper=self._client_wrapper)
        return self._overview


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
