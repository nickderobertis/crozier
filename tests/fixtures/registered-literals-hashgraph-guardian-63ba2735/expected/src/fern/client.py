

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .accounts.client import AccountsClient, AsyncAccountsClient
    from .ai_suggestions.client import AiSuggestionsClient, AsyncAiSuggestionsClient
    from .analytics.client import AnalyticsClient, AsyncAnalyticsClient
    from .artifacts.client import ArtifactsClient, AsyncArtifactsClient
    from .branding.client import AsyncBrandingClient, BrandingClient
    from .contracts.client import AsyncContractsClient, ContractsClient
    from .demo.client import AsyncDemoClient, DemoClient
    from .external.client import AsyncExternalClient, ExternalClient
    from .ipfs.client import AsyncIpfsClient, IpfsClient
    from .logs.client import AsyncLogsClient, LogsClient
    from .map_.client import AsyncMapClient, MapClient
    from .maps.client import AsyncMapsClient, MapsClient
    from .metrics.client import AsyncMetricsClient, MetricsClient
    from .modules.client import AsyncModulesClient, ModulesClient
    from .notifications.client import AsyncNotificationsClient, NotificationsClient
    from .policies.client import AsyncPoliciesClient, PoliciesClient
    from .profiles.client import AsyncProfilesClient, ProfilesClient
    from .projects.client import AsyncProjectsClient, ProjectsClient
    from .record.client import AsyncRecordClient, RecordClient
    from .schema.client import AsyncSchemaClient, SchemaClient
    from .schemas.client import AsyncSchemasClient, SchemasClient
    from .settings.client import AsyncSettingsClient, SettingsClient
    from .suggestions.client import AsyncSuggestionsClient, SuggestionsClient
    from .tags.client import AsyncTagsClient, TagsClient
    from .tasks.client import AsyncTasksClient, TasksClient
    from .themes.client import AsyncThemesClient, ThemesClient
    from .tokens.client import AsyncTokensClient, TokensClient
    from .tools.client import AsyncToolsClient, ToolsClient
    from .trustchains.client import AsyncTrustchainsClient, TrustchainsClient
    from .wizard.client import AsyncWizardClient, WizardClient


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
        self._accounts: typing.Optional[AccountsClient] = None
        self._analytics: typing.Optional[AnalyticsClient] = None
        self._artifacts: typing.Optional[ArtifactsClient] = None
        self._contracts: typing.Optional[ContractsClient] = None
        self._demo: typing.Optional[DemoClient] = None
        self._external: typing.Optional[ExternalClient] = None
        self._ipfs: typing.Optional[IpfsClient] = None
        self._logs: typing.Optional[LogsClient] = None
        self._maps: typing.Optional[MapsClient] = None
        self._map_: typing.Optional[MapClient] = None
        self._metrics: typing.Optional[MetricsClient] = None
        self._modules: typing.Optional[ModulesClient] = None
        self._tools: typing.Optional[ToolsClient] = None
        self._profiles: typing.Optional[ProfilesClient] = None
        self._policies: typing.Optional[PoliciesClient] = None
        self._schema: typing.Optional[SchemaClient] = None
        self._schemas: typing.Optional[SchemasClient] = None
        self._settings: typing.Optional[SettingsClient] = None
        self._tags: typing.Optional[TagsClient] = None
        self._tasks: typing.Optional[TasksClient] = None
        self._tokens: typing.Optional[TokensClient] = None
        self._themes: typing.Optional[ThemesClient] = None
        self._trustchains: typing.Optional[TrustchainsClient] = None
        self._wizard: typing.Optional[WizardClient] = None
        self._branding: typing.Optional[BrandingClient] = None
        self._suggestions: typing.Optional[SuggestionsClient] = None
        self._notifications: typing.Optional[NotificationsClient] = None
        self._projects: typing.Optional[ProjectsClient] = None
        self._record: typing.Optional[RecordClient] = None
        self._ai_suggestions: typing.Optional[AiSuggestionsClient] = None

    @property
    def accounts(self):
        if self._accounts is None:
            from .accounts.client import AccountsClient

            self._accounts = AccountsClient(client_wrapper=self._client_wrapper)
        return self._accounts

    @property
    def analytics(self):
        if self._analytics is None:
            from .analytics.client import AnalyticsClient

            self._analytics = AnalyticsClient(client_wrapper=self._client_wrapper)
        return self._analytics

    @property
    def artifacts(self):
        if self._artifacts is None:
            from .artifacts.client import ArtifactsClient

            self._artifacts = ArtifactsClient(client_wrapper=self._client_wrapper)
        return self._artifacts

    @property
    def contracts(self):
        if self._contracts is None:
            from .contracts.client import ContractsClient

            self._contracts = ContractsClient(client_wrapper=self._client_wrapper)
        return self._contracts

    @property
    def demo(self):
        if self._demo is None:
            from .demo.client import DemoClient

            self._demo = DemoClient(client_wrapper=self._client_wrapper)
        return self._demo

    @property
    def external(self):
        if self._external is None:
            from .external.client import ExternalClient

            self._external = ExternalClient(client_wrapper=self._client_wrapper)
        return self._external

    @property
    def ipfs(self):
        if self._ipfs is None:
            from .ipfs.client import IpfsClient

            self._ipfs = IpfsClient(client_wrapper=self._client_wrapper)
        return self._ipfs

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import LogsClient

            self._logs = LogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def maps(self):
        if self._maps is None:
            from .maps.client import MapsClient

            self._maps = MapsClient(client_wrapper=self._client_wrapper)
        return self._maps

    @property
    def map_(self):
        if self._map_ is None:
            from .map_.client import MapClient

            self._map_ = MapClient(client_wrapper=self._client_wrapper)
        return self._map_

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import MetricsClient

            self._metrics = MetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def modules(self):
        if self._modules is None:
            from .modules.client import ModulesClient

            self._modules = ModulesClient(client_wrapper=self._client_wrapper)
        return self._modules

    @property
    def tools(self):
        if self._tools is None:
            from .tools.client import ToolsClient

            self._tools = ToolsClient(client_wrapper=self._client_wrapper)
        return self._tools

    @property
    def profiles(self):
        if self._profiles is None:
            from .profiles.client import ProfilesClient

            self._profiles = ProfilesClient(client_wrapper=self._client_wrapper)
        return self._profiles

    @property
    def policies(self):
        if self._policies is None:
            from .policies.client import PoliciesClient

            self._policies = PoliciesClient(client_wrapper=self._client_wrapper)
        return self._policies

    @property
    def schema(self):
        if self._schema is None:
            from .schema.client import SchemaClient

            self._schema = SchemaClient(client_wrapper=self._client_wrapper)
        return self._schema

    @property
    def schemas(self):
        if self._schemas is None:
            from .schemas.client import SchemasClient

            self._schemas = SchemasClient(client_wrapper=self._client_wrapper)
        return self._schemas

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import SettingsClient

            self._settings = SettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import TagsClient

            self._tags = TagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def tasks(self):
        if self._tasks is None:
            from .tasks.client import TasksClient

            self._tasks = TasksClient(client_wrapper=self._client_wrapper)
        return self._tasks

    @property
    def tokens(self):
        if self._tokens is None:
            from .tokens.client import TokensClient

            self._tokens = TokensClient(client_wrapper=self._client_wrapper)
        return self._tokens

    @property
    def themes(self):
        if self._themes is None:
            from .themes.client import ThemesClient

            self._themes = ThemesClient(client_wrapper=self._client_wrapper)
        return self._themes

    @property
    def trustchains(self):
        if self._trustchains is None:
            from .trustchains.client import TrustchainsClient

            self._trustchains = TrustchainsClient(client_wrapper=self._client_wrapper)
        return self._trustchains

    @property
    def wizard(self):
        if self._wizard is None:
            from .wizard.client import WizardClient

            self._wizard = WizardClient(client_wrapper=self._client_wrapper)
        return self._wizard

    @property
    def branding(self):
        if self._branding is None:
            from .branding.client import BrandingClient

            self._branding = BrandingClient(client_wrapper=self._client_wrapper)
        return self._branding

    @property
    def suggestions(self):
        if self._suggestions is None:
            from .suggestions.client import SuggestionsClient

            self._suggestions = SuggestionsClient(client_wrapper=self._client_wrapper)
        return self._suggestions

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import NotificationsClient

            self._notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import ProjectsClient

            self._projects = ProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def record(self):
        if self._record is None:
            from .record.client import RecordClient

            self._record = RecordClient(client_wrapper=self._client_wrapper)
        return self._record

    @property
    def ai_suggestions(self):
        if self._ai_suggestions is None:
            from .ai_suggestions.client import AiSuggestionsClient

            self._ai_suggestions = AiSuggestionsClient(client_wrapper=self._client_wrapper)
        return self._ai_suggestions


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
        self._accounts: typing.Optional[AsyncAccountsClient] = None
        self._analytics: typing.Optional[AsyncAnalyticsClient] = None
        self._artifacts: typing.Optional[AsyncArtifactsClient] = None
        self._contracts: typing.Optional[AsyncContractsClient] = None
        self._demo: typing.Optional[AsyncDemoClient] = None
        self._external: typing.Optional[AsyncExternalClient] = None
        self._ipfs: typing.Optional[AsyncIpfsClient] = None
        self._logs: typing.Optional[AsyncLogsClient] = None
        self._maps: typing.Optional[AsyncMapsClient] = None
        self._map_: typing.Optional[AsyncMapClient] = None
        self._metrics: typing.Optional[AsyncMetricsClient] = None
        self._modules: typing.Optional[AsyncModulesClient] = None
        self._tools: typing.Optional[AsyncToolsClient] = None
        self._profiles: typing.Optional[AsyncProfilesClient] = None
        self._policies: typing.Optional[AsyncPoliciesClient] = None
        self._schema: typing.Optional[AsyncSchemaClient] = None
        self._schemas: typing.Optional[AsyncSchemasClient] = None
        self._settings: typing.Optional[AsyncSettingsClient] = None
        self._tags: typing.Optional[AsyncTagsClient] = None
        self._tasks: typing.Optional[AsyncTasksClient] = None
        self._tokens: typing.Optional[AsyncTokensClient] = None
        self._themes: typing.Optional[AsyncThemesClient] = None
        self._trustchains: typing.Optional[AsyncTrustchainsClient] = None
        self._wizard: typing.Optional[AsyncWizardClient] = None
        self._branding: typing.Optional[AsyncBrandingClient] = None
        self._suggestions: typing.Optional[AsyncSuggestionsClient] = None
        self._notifications: typing.Optional[AsyncNotificationsClient] = None
        self._projects: typing.Optional[AsyncProjectsClient] = None
        self._record: typing.Optional[AsyncRecordClient] = None
        self._ai_suggestions: typing.Optional[AsyncAiSuggestionsClient] = None

    @property
    def accounts(self):
        if self._accounts is None:
            from .accounts.client import AsyncAccountsClient

            self._accounts = AsyncAccountsClient(client_wrapper=self._client_wrapper)
        return self._accounts

    @property
    def analytics(self):
        if self._analytics is None:
            from .analytics.client import AsyncAnalyticsClient

            self._analytics = AsyncAnalyticsClient(client_wrapper=self._client_wrapper)
        return self._analytics

    @property
    def artifacts(self):
        if self._artifacts is None:
            from .artifacts.client import AsyncArtifactsClient

            self._artifacts = AsyncArtifactsClient(client_wrapper=self._client_wrapper)
        return self._artifacts

    @property
    def contracts(self):
        if self._contracts is None:
            from .contracts.client import AsyncContractsClient

            self._contracts = AsyncContractsClient(client_wrapper=self._client_wrapper)
        return self._contracts

    @property
    def demo(self):
        if self._demo is None:
            from .demo.client import AsyncDemoClient

            self._demo = AsyncDemoClient(client_wrapper=self._client_wrapper)
        return self._demo

    @property
    def external(self):
        if self._external is None:
            from .external.client import AsyncExternalClient

            self._external = AsyncExternalClient(client_wrapper=self._client_wrapper)
        return self._external

    @property
    def ipfs(self):
        if self._ipfs is None:
            from .ipfs.client import AsyncIpfsClient

            self._ipfs = AsyncIpfsClient(client_wrapper=self._client_wrapper)
        return self._ipfs

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import AsyncLogsClient

            self._logs = AsyncLogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def maps(self):
        if self._maps is None:
            from .maps.client import AsyncMapsClient

            self._maps = AsyncMapsClient(client_wrapper=self._client_wrapper)
        return self._maps

    @property
    def map_(self):
        if self._map_ is None:
            from .map_.client import AsyncMapClient

            self._map_ = AsyncMapClient(client_wrapper=self._client_wrapper)
        return self._map_

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import AsyncMetricsClient

            self._metrics = AsyncMetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def modules(self):
        if self._modules is None:
            from .modules.client import AsyncModulesClient

            self._modules = AsyncModulesClient(client_wrapper=self._client_wrapper)
        return self._modules

    @property
    def tools(self):
        if self._tools is None:
            from .tools.client import AsyncToolsClient

            self._tools = AsyncToolsClient(client_wrapper=self._client_wrapper)
        return self._tools

    @property
    def profiles(self):
        if self._profiles is None:
            from .profiles.client import AsyncProfilesClient

            self._profiles = AsyncProfilesClient(client_wrapper=self._client_wrapper)
        return self._profiles

    @property
    def policies(self):
        if self._policies is None:
            from .policies.client import AsyncPoliciesClient

            self._policies = AsyncPoliciesClient(client_wrapper=self._client_wrapper)
        return self._policies

    @property
    def schema(self):
        if self._schema is None:
            from .schema.client import AsyncSchemaClient

            self._schema = AsyncSchemaClient(client_wrapper=self._client_wrapper)
        return self._schema

    @property
    def schemas(self):
        if self._schemas is None:
            from .schemas.client import AsyncSchemasClient

            self._schemas = AsyncSchemasClient(client_wrapper=self._client_wrapper)
        return self._schemas

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import AsyncSettingsClient

            self._settings = AsyncSettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import AsyncTagsClient

            self._tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def tasks(self):
        if self._tasks is None:
            from .tasks.client import AsyncTasksClient

            self._tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        return self._tasks

    @property
    def tokens(self):
        if self._tokens is None:
            from .tokens.client import AsyncTokensClient

            self._tokens = AsyncTokensClient(client_wrapper=self._client_wrapper)
        return self._tokens

    @property
    def themes(self):
        if self._themes is None:
            from .themes.client import AsyncThemesClient

            self._themes = AsyncThemesClient(client_wrapper=self._client_wrapper)
        return self._themes

    @property
    def trustchains(self):
        if self._trustchains is None:
            from .trustchains.client import AsyncTrustchainsClient

            self._trustchains = AsyncTrustchainsClient(client_wrapper=self._client_wrapper)
        return self._trustchains

    @property
    def wizard(self):
        if self._wizard is None:
            from .wizard.client import AsyncWizardClient

            self._wizard = AsyncWizardClient(client_wrapper=self._client_wrapper)
        return self._wizard

    @property
    def branding(self):
        if self._branding is None:
            from .branding.client import AsyncBrandingClient

            self._branding = AsyncBrandingClient(client_wrapper=self._client_wrapper)
        return self._branding

    @property
    def suggestions(self):
        if self._suggestions is None:
            from .suggestions.client import AsyncSuggestionsClient

            self._suggestions = AsyncSuggestionsClient(client_wrapper=self._client_wrapper)
        return self._suggestions

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import AsyncNotificationsClient

            self._notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            self._projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def record(self):
        if self._record is None:
            from .record.client import AsyncRecordClient

            self._record = AsyncRecordClient(client_wrapper=self._client_wrapper)
        return self._record

    @property
    def ai_suggestions(self):
        if self._ai_suggestions is None:
            from .ai_suggestions.client import AsyncAiSuggestionsClient

            self._ai_suggestions = AsyncAiSuggestionsClient(client_wrapper=self._client_wrapper)
        return self._ai_suggestions


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
