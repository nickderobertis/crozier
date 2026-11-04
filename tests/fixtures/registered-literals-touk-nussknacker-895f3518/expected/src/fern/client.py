

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .activities.client import ActivitiesClient, AsyncActivitiesClient
    from .app.client import AppClient, AsyncAppClient
    from .components.client import AsyncComponentsClient, ComponentsClient
    from .deployments.client import AsyncDeploymentsClient, DeploymentsClient
    from .dictionary.client import AsyncDictionaryClient, DictionaryClient
    from .live_data.client import AsyncLiveDataClient, LiveDataClient
    from .migrations.client import AsyncMigrationsClient, MigrationsClient
    from .nodes.client import AsyncNodesClient, NodesClient
    from .notifications.client import AsyncNotificationsClient, NotificationsClient
    from .scenario_labels.client import AsyncScenarioLabelsClient, ScenarioLabelsClient
    from .statistics.client import AsyncStatisticsClient, StatisticsClient
    from .testing.client import AsyncTestingClient, TestingClient
    from .user.client import AsyncUserClient, UserClient
    from .version_control.client import AsyncVersionControlClient, VersionControlClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    nu_impersonate_user_identity : typing.Optional[str]
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
        nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        nu_impersonate_user_identity: typing.Optional[str] = None,
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
            base_url=base_url,
            nu_impersonate_user_identity=nu_impersonate_user_identity,
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
        self._components: typing.Optional[ComponentsClient] = None
        self._deployments: typing.Optional[DeploymentsClient] = None
        self._app: typing.Optional[AppClient] = None
        self._dictionary: typing.Optional[DictionaryClient] = None
        self._migrations: typing.Optional[MigrationsClient] = None
        self._nodes: typing.Optional[NodesClient] = None
        self._notifications: typing.Optional[NotificationsClient] = None
        self._scenario_labels: typing.Optional[ScenarioLabelsClient] = None
        self._statistics: typing.Optional[StatisticsClient] = None
        self._user: typing.Optional[UserClient] = None
        self._version_control: typing.Optional[VersionControlClient] = None
        self._activities: typing.Optional[ActivitiesClient] = None
        self._live_data: typing.Optional[LiveDataClient] = None
        self._testing: typing.Optional[TestingClient] = None

    @property
    def components(self):
        if self._components is None:
            from .components.client import ComponentsClient

            self._components = ComponentsClient(client_wrapper=self._client_wrapper)
        return self._components

    @property
    def deployments(self):
        if self._deployments is None:
            from .deployments.client import DeploymentsClient

            self._deployments = DeploymentsClient(client_wrapper=self._client_wrapper)
        return self._deployments

    @property
    def app(self):
        if self._app is None:
            from .app.client import AppClient

            self._app = AppClient(client_wrapper=self._client_wrapper)
        return self._app

    @property
    def dictionary(self):
        if self._dictionary is None:
            from .dictionary.client import DictionaryClient

            self._dictionary = DictionaryClient(client_wrapper=self._client_wrapper)
        return self._dictionary

    @property
    def migrations(self):
        if self._migrations is None:
            from .migrations.client import MigrationsClient

            self._migrations = MigrationsClient(client_wrapper=self._client_wrapper)
        return self._migrations

    @property
    def nodes(self):
        if self._nodes is None:
            from .nodes.client import NodesClient

            self._nodes = NodesClient(client_wrapper=self._client_wrapper)
        return self._nodes

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import NotificationsClient

            self._notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def scenario_labels(self):
        if self._scenario_labels is None:
            from .scenario_labels.client import ScenarioLabelsClient

            self._scenario_labels = ScenarioLabelsClient(client_wrapper=self._client_wrapper)
        return self._scenario_labels

    @property
    def statistics(self):
        if self._statistics is None:
            from .statistics.client import StatisticsClient

            self._statistics = StatisticsClient(client_wrapper=self._client_wrapper)
        return self._statistics

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def version_control(self):
        if self._version_control is None:
            from .version_control.client import VersionControlClient

            self._version_control = VersionControlClient(client_wrapper=self._client_wrapper)
        return self._version_control

    @property
    def activities(self):
        if self._activities is None:
            from .activities.client import ActivitiesClient

            self._activities = ActivitiesClient(client_wrapper=self._client_wrapper)
        return self._activities

    @property
    def live_data(self):
        if self._live_data is None:
            from .live_data.client import LiveDataClient

            self._live_data = LiveDataClient(client_wrapper=self._client_wrapper)
        return self._live_data

    @property
    def testing(self):
        if self._testing is None:
            from .testing.client import TestingClient

            self._testing = TestingClient(client_wrapper=self._client_wrapper)
        return self._testing


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

    nu_impersonate_user_identity : typing.Optional[str]
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
        nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        nu_impersonate_user_identity: typing.Optional[str] = None,
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
            base_url=base_url,
            nu_impersonate_user_identity=nu_impersonate_user_identity,
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
        self._components: typing.Optional[AsyncComponentsClient] = None
        self._deployments: typing.Optional[AsyncDeploymentsClient] = None
        self._app: typing.Optional[AsyncAppClient] = None
        self._dictionary: typing.Optional[AsyncDictionaryClient] = None
        self._migrations: typing.Optional[AsyncMigrationsClient] = None
        self._nodes: typing.Optional[AsyncNodesClient] = None
        self._notifications: typing.Optional[AsyncNotificationsClient] = None
        self._scenario_labels: typing.Optional[AsyncScenarioLabelsClient] = None
        self._statistics: typing.Optional[AsyncStatisticsClient] = None
        self._user: typing.Optional[AsyncUserClient] = None
        self._version_control: typing.Optional[AsyncVersionControlClient] = None
        self._activities: typing.Optional[AsyncActivitiesClient] = None
        self._live_data: typing.Optional[AsyncLiveDataClient] = None
        self._testing: typing.Optional[AsyncTestingClient] = None

    @property
    def components(self):
        if self._components is None:
            from .components.client import AsyncComponentsClient

            self._components = AsyncComponentsClient(client_wrapper=self._client_wrapper)
        return self._components

    @property
    def deployments(self):
        if self._deployments is None:
            from .deployments.client import AsyncDeploymentsClient

            self._deployments = AsyncDeploymentsClient(client_wrapper=self._client_wrapper)
        return self._deployments

    @property
    def app(self):
        if self._app is None:
            from .app.client import AsyncAppClient

            self._app = AsyncAppClient(client_wrapper=self._client_wrapper)
        return self._app

    @property
    def dictionary(self):
        if self._dictionary is None:
            from .dictionary.client import AsyncDictionaryClient

            self._dictionary = AsyncDictionaryClient(client_wrapper=self._client_wrapper)
        return self._dictionary

    @property
    def migrations(self):
        if self._migrations is None:
            from .migrations.client import AsyncMigrationsClient

            self._migrations = AsyncMigrationsClient(client_wrapper=self._client_wrapper)
        return self._migrations

    @property
    def nodes(self):
        if self._nodes is None:
            from .nodes.client import AsyncNodesClient

            self._nodes = AsyncNodesClient(client_wrapper=self._client_wrapper)
        return self._nodes

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import AsyncNotificationsClient

            self._notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def scenario_labels(self):
        if self._scenario_labels is None:
            from .scenario_labels.client import AsyncScenarioLabelsClient

            self._scenario_labels = AsyncScenarioLabelsClient(client_wrapper=self._client_wrapper)
        return self._scenario_labels

    @property
    def statistics(self):
        if self._statistics is None:
            from .statistics.client import AsyncStatisticsClient

            self._statistics = AsyncStatisticsClient(client_wrapper=self._client_wrapper)
        return self._statistics

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def version_control(self):
        if self._version_control is None:
            from .version_control.client import AsyncVersionControlClient

            self._version_control = AsyncVersionControlClient(client_wrapper=self._client_wrapper)
        return self._version_control

    @property
    def activities(self):
        if self._activities is None:
            from .activities.client import AsyncActivitiesClient

            self._activities = AsyncActivitiesClient(client_wrapper=self._client_wrapper)
        return self._activities

    @property
    def live_data(self):
        if self._live_data is None:
            from .live_data.client import AsyncLiveDataClient

            self._live_data = AsyncLiveDataClient(client_wrapper=self._client_wrapper)
        return self._live_data

    @property
    def testing(self):
        if self._testing is None:
            from .testing.client import AsyncTestingClient

            self._testing = AsyncTestingClient(client_wrapper=self._client_wrapper)
        return self._testing
