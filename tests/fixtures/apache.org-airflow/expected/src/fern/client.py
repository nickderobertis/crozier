

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .config.client import AsyncConfigClient, ConfigClient
    from .connection.client import AsyncConnectionClient, ConnectionClient
    from .dag.client import AsyncDagClient, DagClient
    from .dag_run.client import AsyncDagRunClient, DagRunClient
    from .dag_warning.client import AsyncDagWarningClient, DagWarningClient
    from .dataset.client import AsyncDatasetClient, DatasetClient
    from .event_log.client import AsyncEventLogClient, EventLogClient
    from .import_error.client import AsyncImportErrorClient, ImportErrorClient
    from .monitoring.client import AsyncMonitoringClient, MonitoringClient
    from .permission.client import AsyncPermissionClient, PermissionClient
    from .plugin.client import AsyncPluginClient, PluginClient
    from .pool.client import AsyncPoolClient, PoolClient
    from .provider.client import AsyncProviderClient, ProviderClient
    from .role.client import AsyncRoleClient, RoleClient
    from .task_instance.client import AsyncTaskInstanceClient, TaskInstanceClient
    from .user.client import AsyncUserClient, UserClient
    from .variable.client import AsyncVariableClient, VariableClient
    from .x_com.client import AsyncXComClient, XComClient


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



    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            username=username,
            password=password,
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
        self._config: typing.Optional[ConfigClient] = None
        self._connection: typing.Optional[ConnectionClient] = None
        self._dag: typing.Optional[DagClient] = None
        self._dag_warning: typing.Optional[DagWarningClient] = None
        self._dag_run: typing.Optional[DagRunClient] = None
        self._task_instance: typing.Optional[TaskInstanceClient] = None
        self._x_com: typing.Optional[XComClient] = None
        self._dataset: typing.Optional[DatasetClient] = None
        self._event_log: typing.Optional[EventLogClient] = None
        self._monitoring: typing.Optional[MonitoringClient] = None
        self._import_error: typing.Optional[ImportErrorClient] = None
        self._permission: typing.Optional[PermissionClient] = None
        self._plugin: typing.Optional[PluginClient] = None
        self._pool: typing.Optional[PoolClient] = None
        self._provider: typing.Optional[ProviderClient] = None
        self._role: typing.Optional[RoleClient] = None
        self._user: typing.Optional[UserClient] = None
        self._variable: typing.Optional[VariableClient] = None

    @property
    def config(self):
        if self._config is None:
            from .config.client import ConfigClient

            self._config = ConfigClient(client_wrapper=self._client_wrapper)
        return self._config

    @property
    def connection(self):
        if self._connection is None:
            from .connection.client import ConnectionClient

            self._connection = ConnectionClient(client_wrapper=self._client_wrapper)
        return self._connection

    @property
    def dag(self):
        if self._dag is None:
            from .dag.client import DagClient

            self._dag = DagClient(client_wrapper=self._client_wrapper)
        return self._dag

    @property
    def dag_warning(self):
        if self._dag_warning is None:
            from .dag_warning.client import DagWarningClient

            self._dag_warning = DagWarningClient(client_wrapper=self._client_wrapper)
        return self._dag_warning

    @property
    def dag_run(self):
        if self._dag_run is None:
            from .dag_run.client import DagRunClient

            self._dag_run = DagRunClient(client_wrapper=self._client_wrapper)
        return self._dag_run

    @property
    def task_instance(self):
        if self._task_instance is None:
            from .task_instance.client import TaskInstanceClient

            self._task_instance = TaskInstanceClient(client_wrapper=self._client_wrapper)
        return self._task_instance

    @property
    def x_com(self):
        if self._x_com is None:
            from .x_com.client import XComClient

            self._x_com = XComClient(client_wrapper=self._client_wrapper)
        return self._x_com

    @property
    def dataset(self):
        if self._dataset is None:
            from .dataset.client import DatasetClient

            self._dataset = DatasetClient(client_wrapper=self._client_wrapper)
        return self._dataset

    @property
    def event_log(self):
        if self._event_log is None:
            from .event_log.client import EventLogClient

            self._event_log = EventLogClient(client_wrapper=self._client_wrapper)
        return self._event_log

    @property
    def monitoring(self):
        if self._monitoring is None:
            from .monitoring.client import MonitoringClient

            self._monitoring = MonitoringClient(client_wrapper=self._client_wrapper)
        return self._monitoring

    @property
    def import_error(self):
        if self._import_error is None:
            from .import_error.client import ImportErrorClient

            self._import_error = ImportErrorClient(client_wrapper=self._client_wrapper)
        return self._import_error

    @property
    def permission(self):
        if self._permission is None:
            from .permission.client import PermissionClient

            self._permission = PermissionClient(client_wrapper=self._client_wrapper)
        return self._permission

    @property
    def plugin(self):
        if self._plugin is None:
            from .plugin.client import PluginClient

            self._plugin = PluginClient(client_wrapper=self._client_wrapper)
        return self._plugin

    @property
    def pool(self):
        if self._pool is None:
            from .pool.client import PoolClient

            self._pool = PoolClient(client_wrapper=self._client_wrapper)
        return self._pool

    @property
    def provider(self):
        if self._provider is None:
            from .provider.client import ProviderClient

            self._provider = ProviderClient(client_wrapper=self._client_wrapper)
        return self._provider

    @property
    def role(self):
        if self._role is None:
            from .role.client import RoleClient

            self._role = RoleClient(client_wrapper=self._client_wrapper)
        return self._role

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def variable(self):
        if self._variable is None:
            from .variable.client import VariableClient

            self._variable = VariableClient(client_wrapper=self._client_wrapper)
        return self._variable


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



    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            username=username,
            password=password,
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
        self._config: typing.Optional[AsyncConfigClient] = None
        self._connection: typing.Optional[AsyncConnectionClient] = None
        self._dag: typing.Optional[AsyncDagClient] = None
        self._dag_warning: typing.Optional[AsyncDagWarningClient] = None
        self._dag_run: typing.Optional[AsyncDagRunClient] = None
        self._task_instance: typing.Optional[AsyncTaskInstanceClient] = None
        self._x_com: typing.Optional[AsyncXComClient] = None
        self._dataset: typing.Optional[AsyncDatasetClient] = None
        self._event_log: typing.Optional[AsyncEventLogClient] = None
        self._monitoring: typing.Optional[AsyncMonitoringClient] = None
        self._import_error: typing.Optional[AsyncImportErrorClient] = None
        self._permission: typing.Optional[AsyncPermissionClient] = None
        self._plugin: typing.Optional[AsyncPluginClient] = None
        self._pool: typing.Optional[AsyncPoolClient] = None
        self._provider: typing.Optional[AsyncProviderClient] = None
        self._role: typing.Optional[AsyncRoleClient] = None
        self._user: typing.Optional[AsyncUserClient] = None
        self._variable: typing.Optional[AsyncVariableClient] = None

    @property
    def config(self):
        if self._config is None:
            from .config.client import AsyncConfigClient

            self._config = AsyncConfigClient(client_wrapper=self._client_wrapper)
        return self._config

    @property
    def connection(self):
        if self._connection is None:
            from .connection.client import AsyncConnectionClient

            self._connection = AsyncConnectionClient(client_wrapper=self._client_wrapper)
        return self._connection

    @property
    def dag(self):
        if self._dag is None:
            from .dag.client import AsyncDagClient

            self._dag = AsyncDagClient(client_wrapper=self._client_wrapper)
        return self._dag

    @property
    def dag_warning(self):
        if self._dag_warning is None:
            from .dag_warning.client import AsyncDagWarningClient

            self._dag_warning = AsyncDagWarningClient(client_wrapper=self._client_wrapper)
        return self._dag_warning

    @property
    def dag_run(self):
        if self._dag_run is None:
            from .dag_run.client import AsyncDagRunClient

            self._dag_run = AsyncDagRunClient(client_wrapper=self._client_wrapper)
        return self._dag_run

    @property
    def task_instance(self):
        if self._task_instance is None:
            from .task_instance.client import AsyncTaskInstanceClient

            self._task_instance = AsyncTaskInstanceClient(client_wrapper=self._client_wrapper)
        return self._task_instance

    @property
    def x_com(self):
        if self._x_com is None:
            from .x_com.client import AsyncXComClient

            self._x_com = AsyncXComClient(client_wrapper=self._client_wrapper)
        return self._x_com

    @property
    def dataset(self):
        if self._dataset is None:
            from .dataset.client import AsyncDatasetClient

            self._dataset = AsyncDatasetClient(client_wrapper=self._client_wrapper)
        return self._dataset

    @property
    def event_log(self):
        if self._event_log is None:
            from .event_log.client import AsyncEventLogClient

            self._event_log = AsyncEventLogClient(client_wrapper=self._client_wrapper)
        return self._event_log

    @property
    def monitoring(self):
        if self._monitoring is None:
            from .monitoring.client import AsyncMonitoringClient

            self._monitoring = AsyncMonitoringClient(client_wrapper=self._client_wrapper)
        return self._monitoring

    @property
    def import_error(self):
        if self._import_error is None:
            from .import_error.client import AsyncImportErrorClient

            self._import_error = AsyncImportErrorClient(client_wrapper=self._client_wrapper)
        return self._import_error

    @property
    def permission(self):
        if self._permission is None:
            from .permission.client import AsyncPermissionClient

            self._permission = AsyncPermissionClient(client_wrapper=self._client_wrapper)
        return self._permission

    @property
    def plugin(self):
        if self._plugin is None:
            from .plugin.client import AsyncPluginClient

            self._plugin = AsyncPluginClient(client_wrapper=self._client_wrapper)
        return self._plugin

    @property
    def pool(self):
        if self._pool is None:
            from .pool.client import AsyncPoolClient

            self._pool = AsyncPoolClient(client_wrapper=self._client_wrapper)
        return self._pool

    @property
    def provider(self):
        if self._provider is None:
            from .provider.client import AsyncProviderClient

            self._provider = AsyncProviderClient(client_wrapper=self._client_wrapper)
        return self._provider

    @property
    def role(self):
        if self._role is None:
            from .role.client import AsyncRoleClient

            self._role = AsyncRoleClient(client_wrapper=self._client_wrapper)
        return self._role

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def variable(self):
        if self._variable is None:
            from .variable.client import AsyncVariableClient

            self._variable = AsyncVariableClient(client_wrapper=self._client_wrapper)
        return self._variable


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
