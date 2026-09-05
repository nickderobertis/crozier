

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .admin.client import AdminClient, AsyncAdminClient
    from .announcements.client import AnnouncementsClient, AsyncAnnouncementsClient
    from .auth.client import AsyncAuthClient, AuthClient
    from .catalog.client import AsyncCatalogClient, CatalogClient
    from .computations.client import AsyncComputationsClient, ComputationsClient
    from .conversations.client import AsyncConversationsClient, ConversationsClient
    from .folders.client import AsyncFoldersClient, FoldersClient
    from .functions.client import AsyncFunctionsClient, FunctionsClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .licenses.client import AsyncLicensesClient, LicensesClient
    from .long_running_tasks.client import AsyncLongRunningTasksClient, LongRunningTasksClient
    from .long_running_tasks_legacy.client import AsyncLongRunningTasksLegacyClient, LongRunningTasksLegacyClient
    from .maintenance.client import AsyncMaintenanceClient, MaintenanceClient
    from .nih_sparc.client import AsyncNihSparcClient, NihSparcClient
    from .notifications.client import AsyncNotificationsClient, NotificationsClient
    from .pricing_plans.client import AsyncPricingPlansClient, PricingPlansClient
    from .products.client import AsyncProductsClient, ProductsClient
    from .projects.client import AsyncProjectsClient, ProjectsClient
    from .statics.client import AsyncStaticsClient, StaticsClient
    from .storage.client import AsyncStorageClient, StorageClient
    from .studies_dispatcher.client import AsyncStudiesDispatcherClient, StudiesDispatcherClient
    from .tags.client import AsyncTagsClient, TagsClient
    from .tasks.client import AsyncTasksClient, TasksClient
    from .trash.client import AsyncTrashClient, TrashClient
    from .usage.client import AsyncUsageClient, UsageClient
    from .users.client import AsyncUsersClient, UsersClient
    from .wallets.client import AsyncWalletsClient, WalletsClient
    from .workspaces.client import AsyncWorkspacesClient, WorkspacesClient


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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._conversations: typing.Optional[ConversationsClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._tags: typing.Optional[TagsClient] = None
        self._products: typing.Optional[ProductsClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._wallets: typing.Optional[WalletsClient] = None
        self._tasks: typing.Optional[TasksClient] = None
        self._announcements: typing.Optional[AnnouncementsClient] = None
        self._catalog: typing.Optional[CatalogClient] = None
        self._computations: typing.Optional[ComputationsClient] = None
        self._projects: typing.Optional[ProjectsClient] = None
        self._folders: typing.Optional[FoldersClient] = None
        self._functions: typing.Optional[FunctionsClient] = None
        self._long_running_tasks: typing.Optional[LongRunningTasksClient] = None
        self._long_running_tasks_legacy: typing.Optional[LongRunningTasksLegacyClient] = None
        self._licenses: typing.Optional[LicensesClient] = None
        self._nih_sparc: typing.Optional[NihSparcClient] = None
        self._notifications: typing.Optional[NotificationsClient] = None
        self._usage: typing.Optional[UsageClient] = None
        self._pricing_plans: typing.Optional[PricingPlansClient] = None
        self._admin: typing.Optional[AdminClient] = None
        self._studies_dispatcher: typing.Optional[StudiesDispatcherClient] = None
        self._statics: typing.Optional[StaticsClient] = None
        self._storage: typing.Optional[StorageClient] = None
        self._trash: typing.Optional[TrashClient] = None
        self._workspaces: typing.Optional[WorkspacesClient] = None
        self._maintenance: typing.Optional[MaintenanceClient] = None

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AuthClient

            self._auth = AuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def conversations(self):
        if self._conversations is None:
            from .conversations.client import ConversationsClient

            self._conversations = ConversationsClient(client_wrapper=self._client_wrapper)
        return self._conversations

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import TagsClient

            self._tags = TagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def products(self):
        if self._products is None:
            from .products.client import ProductsClient

            self._products = ProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def wallets(self):
        if self._wallets is None:
            from .wallets.client import WalletsClient

            self._wallets = WalletsClient(client_wrapper=self._client_wrapper)
        return self._wallets

    @property
    def tasks(self):
        if self._tasks is None:
            from .tasks.client import TasksClient

            self._tasks = TasksClient(client_wrapper=self._client_wrapper)
        return self._tasks

    @property
    def announcements(self):
        if self._announcements is None:
            from .announcements.client import AnnouncementsClient

            self._announcements = AnnouncementsClient(client_wrapper=self._client_wrapper)
        return self._announcements

    @property
    def catalog(self):
        if self._catalog is None:
            from .catalog.client import CatalogClient

            self._catalog = CatalogClient(client_wrapper=self._client_wrapper)
        return self._catalog

    @property
    def computations(self):
        if self._computations is None:
            from .computations.client import ComputationsClient

            self._computations = ComputationsClient(client_wrapper=self._client_wrapper)
        return self._computations

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import ProjectsClient

            self._projects = ProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import FoldersClient

            self._folders = FoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def functions(self):
        if self._functions is None:
            from .functions.client import FunctionsClient

            self._functions = FunctionsClient(client_wrapper=self._client_wrapper)
        return self._functions

    @property
    def long_running_tasks(self):
        if self._long_running_tasks is None:
            from .long_running_tasks.client import LongRunningTasksClient

            self._long_running_tasks = LongRunningTasksClient(client_wrapper=self._client_wrapper)
        return self._long_running_tasks

    @property
    def long_running_tasks_legacy(self):
        if self._long_running_tasks_legacy is None:
            from .long_running_tasks_legacy.client import LongRunningTasksLegacyClient

            self._long_running_tasks_legacy = LongRunningTasksLegacyClient(client_wrapper=self._client_wrapper)
        return self._long_running_tasks_legacy

    @property
    def licenses(self):
        if self._licenses is None:
            from .licenses.client import LicensesClient

            self._licenses = LicensesClient(client_wrapper=self._client_wrapper)
        return self._licenses

    @property
    def nih_sparc(self):
        if self._nih_sparc is None:
            from .nih_sparc.client import NihSparcClient

            self._nih_sparc = NihSparcClient(client_wrapper=self._client_wrapper)
        return self._nih_sparc

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import NotificationsClient

            self._notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def usage(self):
        if self._usage is None:
            from .usage.client import UsageClient

            self._usage = UsageClient(client_wrapper=self._client_wrapper)
        return self._usage

    @property
    def pricing_plans(self):
        if self._pricing_plans is None:
            from .pricing_plans.client import PricingPlansClient

            self._pricing_plans = PricingPlansClient(client_wrapper=self._client_wrapper)
        return self._pricing_plans

    @property
    def admin(self):
        if self._admin is None:
            from .admin.client import AdminClient

            self._admin = AdminClient(client_wrapper=self._client_wrapper)
        return self._admin

    @property
    def studies_dispatcher(self):
        if self._studies_dispatcher is None:
            from .studies_dispatcher.client import StudiesDispatcherClient

            self._studies_dispatcher = StudiesDispatcherClient(client_wrapper=self._client_wrapper)
        return self._studies_dispatcher

    @property
    def statics(self):
        if self._statics is None:
            from .statics.client import StaticsClient

            self._statics = StaticsClient(client_wrapper=self._client_wrapper)
        return self._statics

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import StorageClient

            self._storage = StorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def trash(self):
        if self._trash is None:
            from .trash.client import TrashClient

            self._trash = TrashClient(client_wrapper=self._client_wrapper)
        return self._trash

    @property
    def workspaces(self):
        if self._workspaces is None:
            from .workspaces.client import WorkspacesClient

            self._workspaces = WorkspacesClient(client_wrapper=self._client_wrapper)
        return self._workspaces

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
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



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

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._conversations: typing.Optional[AsyncConversationsClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._tags: typing.Optional[AsyncTagsClient] = None
        self._products: typing.Optional[AsyncProductsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._wallets: typing.Optional[AsyncWalletsClient] = None
        self._tasks: typing.Optional[AsyncTasksClient] = None
        self._announcements: typing.Optional[AsyncAnnouncementsClient] = None
        self._catalog: typing.Optional[AsyncCatalogClient] = None
        self._computations: typing.Optional[AsyncComputationsClient] = None
        self._projects: typing.Optional[AsyncProjectsClient] = None
        self._folders: typing.Optional[AsyncFoldersClient] = None
        self._functions: typing.Optional[AsyncFunctionsClient] = None
        self._long_running_tasks: typing.Optional[AsyncLongRunningTasksClient] = None
        self._long_running_tasks_legacy: typing.Optional[AsyncLongRunningTasksLegacyClient] = None
        self._licenses: typing.Optional[AsyncLicensesClient] = None
        self._nih_sparc: typing.Optional[AsyncNihSparcClient] = None
        self._notifications: typing.Optional[AsyncNotificationsClient] = None
        self._usage: typing.Optional[AsyncUsageClient] = None
        self._pricing_plans: typing.Optional[AsyncPricingPlansClient] = None
        self._admin: typing.Optional[AsyncAdminClient] = None
        self._studies_dispatcher: typing.Optional[AsyncStudiesDispatcherClient] = None
        self._statics: typing.Optional[AsyncStaticsClient] = None
        self._storage: typing.Optional[AsyncStorageClient] = None
        self._trash: typing.Optional[AsyncTrashClient] = None
        self._workspaces: typing.Optional[AsyncWorkspacesClient] = None
        self._maintenance: typing.Optional[AsyncMaintenanceClient] = None

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AsyncAuthClient

            self._auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def conversations(self):
        if self._conversations is None:
            from .conversations.client import AsyncConversationsClient

            self._conversations = AsyncConversationsClient(client_wrapper=self._client_wrapper)
        return self._conversations

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import AsyncTagsClient

            self._tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def products(self):
        if self._products is None:
            from .products.client import AsyncProductsClient

            self._products = AsyncProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def wallets(self):
        if self._wallets is None:
            from .wallets.client import AsyncWalletsClient

            self._wallets = AsyncWalletsClient(client_wrapper=self._client_wrapper)
        return self._wallets

    @property
    def tasks(self):
        if self._tasks is None:
            from .tasks.client import AsyncTasksClient

            self._tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        return self._tasks

    @property
    def announcements(self):
        if self._announcements is None:
            from .announcements.client import AsyncAnnouncementsClient

            self._announcements = AsyncAnnouncementsClient(client_wrapper=self._client_wrapper)
        return self._announcements

    @property
    def catalog(self):
        if self._catalog is None:
            from .catalog.client import AsyncCatalogClient

            self._catalog = AsyncCatalogClient(client_wrapper=self._client_wrapper)
        return self._catalog

    @property
    def computations(self):
        if self._computations is None:
            from .computations.client import AsyncComputationsClient

            self._computations = AsyncComputationsClient(client_wrapper=self._client_wrapper)
        return self._computations

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            self._projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import AsyncFoldersClient

            self._folders = AsyncFoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def functions(self):
        if self._functions is None:
            from .functions.client import AsyncFunctionsClient

            self._functions = AsyncFunctionsClient(client_wrapper=self._client_wrapper)
        return self._functions

    @property
    def long_running_tasks(self):
        if self._long_running_tasks is None:
            from .long_running_tasks.client import AsyncLongRunningTasksClient

            self._long_running_tasks = AsyncLongRunningTasksClient(client_wrapper=self._client_wrapper)
        return self._long_running_tasks

    @property
    def long_running_tasks_legacy(self):
        if self._long_running_tasks_legacy is None:
            from .long_running_tasks_legacy.client import AsyncLongRunningTasksLegacyClient

            self._long_running_tasks_legacy = AsyncLongRunningTasksLegacyClient(client_wrapper=self._client_wrapper)
        return self._long_running_tasks_legacy

    @property
    def licenses(self):
        if self._licenses is None:
            from .licenses.client import AsyncLicensesClient

            self._licenses = AsyncLicensesClient(client_wrapper=self._client_wrapper)
        return self._licenses

    @property
    def nih_sparc(self):
        if self._nih_sparc is None:
            from .nih_sparc.client import AsyncNihSparcClient

            self._nih_sparc = AsyncNihSparcClient(client_wrapper=self._client_wrapper)
        return self._nih_sparc

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import AsyncNotificationsClient

            self._notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def usage(self):
        if self._usage is None:
            from .usage.client import AsyncUsageClient

            self._usage = AsyncUsageClient(client_wrapper=self._client_wrapper)
        return self._usage

    @property
    def pricing_plans(self):
        if self._pricing_plans is None:
            from .pricing_plans.client import AsyncPricingPlansClient

            self._pricing_plans = AsyncPricingPlansClient(client_wrapper=self._client_wrapper)
        return self._pricing_plans

    @property
    def admin(self):
        if self._admin is None:
            from .admin.client import AsyncAdminClient

            self._admin = AsyncAdminClient(client_wrapper=self._client_wrapper)
        return self._admin

    @property
    def studies_dispatcher(self):
        if self._studies_dispatcher is None:
            from .studies_dispatcher.client import AsyncStudiesDispatcherClient

            self._studies_dispatcher = AsyncStudiesDispatcherClient(client_wrapper=self._client_wrapper)
        return self._studies_dispatcher

    @property
    def statics(self):
        if self._statics is None:
            from .statics.client import AsyncStaticsClient

            self._statics = AsyncStaticsClient(client_wrapper=self._client_wrapper)
        return self._statics

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import AsyncStorageClient

            self._storage = AsyncStorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def trash(self):
        if self._trash is None:
            from .trash.client import AsyncTrashClient

            self._trash = AsyncTrashClient(client_wrapper=self._client_wrapper)
        return self._trash

    @property
    def workspaces(self):
        if self._workspaces is None:
            from .workspaces.client import AsyncWorkspacesClient

            self._workspaces = AsyncWorkspacesClient(client_wrapper=self._client_wrapper)
        return self._workspaces

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import AsyncMaintenanceClient

            self._maintenance = AsyncMaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
