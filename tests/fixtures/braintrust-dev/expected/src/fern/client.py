

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .acls.client import AclsClient, AsyncAclsClient
    from .ai_secrets.client import AiSecretsClient, AsyncAiSecretsClient
    from .api_keys.client import ApiKeysClient, AsyncApiKeysClient
    from .cross_object.client import AsyncCrossObjectClient, CrossObjectClient
    from .dataset_snapshots.client import AsyncDatasetSnapshotsClient, DatasetSnapshotsClient
    from .datasets.client import AsyncDatasetsClient, DatasetsClient
    from .env_vars.client import AsyncEnvVarsClient, EnvVarsClient
    from .environments.client import AsyncEnvironmentsClient, EnvironmentsClient
    from .eval_status_pages.client import AsyncEvalStatusPagesClient, EvalStatusPagesClient
    from .evals.client import AsyncEvalsClient, EvalsClient
    from .experiments.client import AsyncExperimentsClient, ExperimentsClient
    from .functions.client import AsyncFunctionsClient, FunctionsClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .logs.client import AsyncLogsClient, LogsClient
    from .mcp_servers.client import AsyncMcpServersClient, McpServersClient
    from .organizations.client import AsyncOrganizationsClient, OrganizationsClient
    from .other.client import AsyncOtherClient, OtherClient
    from .project_automations.client import AsyncProjectAutomationsClient, ProjectAutomationsClient
    from .project_scores.client import AsyncProjectScoresClient, ProjectScoresClient
    from .project_tags.client import AsyncProjectTagsClient, ProjectTagsClient
    from .projects.client import AsyncProjectsClient, ProjectsClient
    from .prompts.client import AsyncPromptsClient, PromptsClient
    from .proxy.client import AsyncProxyClient, ProxyClient
    from .roles.client import AsyncRolesClient, RolesClient
    from .service_tokens.client import AsyncServiceTokensClient, ServiceTokensClient
    from .span_iframes.client import AsyncSpanIframesClient, SpanIframesClient
    from .users.client import AsyncUsersClient, UsersClient
    from .views.client import AsyncViewsClient, ViewsClient


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
        self._projects: typing.Optional[ProjectsClient] = None
        self._logs: typing.Optional[LogsClient] = None
        self._experiments: typing.Optional[ExperimentsClient] = None
        self._datasets: typing.Optional[DatasetsClient] = None
        self._prompts: typing.Optional[PromptsClient] = None
        self._roles: typing.Optional[RolesClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._acls: typing.Optional[AclsClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._project_automations: typing.Optional[ProjectAutomationsClient] = None
        self._project_scores: typing.Optional[ProjectScoresClient] = None
        self._project_tags: typing.Optional[ProjectTagsClient] = None
        self._span_iframes: typing.Optional[SpanIframesClient] = None
        self._eval_status_pages: typing.Optional[EvalStatusPagesClient] = None
        self._functions: typing.Optional[FunctionsClient] = None
        self._views: typing.Optional[ViewsClient] = None
        self._organizations: typing.Optional[OrganizationsClient] = None
        self._api_keys: typing.Optional[ApiKeysClient] = None
        self._service_tokens: typing.Optional[ServiceTokensClient] = None
        self._ai_secrets: typing.Optional[AiSecretsClient] = None
        self._env_vars: typing.Optional[EnvVarsClient] = None
        self._mcp_servers: typing.Optional[McpServersClient] = None
        self._dataset_snapshots: typing.Optional[DatasetSnapshotsClient] = None
        self._environments: typing.Optional[EnvironmentsClient] = None
        self._other: typing.Optional[OtherClient] = None
        self._cross_object: typing.Optional[CrossObjectClient] = None
        self._proxy: typing.Optional[ProxyClient] = None
        self._evals: typing.Optional[EvalsClient] = None

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import ProjectsClient

            self._projects = ProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import LogsClient

            self._logs = LogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def experiments(self):
        if self._experiments is None:
            from .experiments.client import ExperimentsClient

            self._experiments = ExperimentsClient(client_wrapper=self._client_wrapper)
        return self._experiments

    @property
    def datasets(self):
        if self._datasets is None:
            from .datasets.client import DatasetsClient

            self._datasets = DatasetsClient(client_wrapper=self._client_wrapper)
        return self._datasets

    @property
    def prompts(self):
        if self._prompts is None:
            from .prompts.client import PromptsClient

            self._prompts = PromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import RolesClient

            self._roles = RolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def acls(self):
        if self._acls is None:
            from .acls.client import AclsClient

            self._acls = AclsClient(client_wrapper=self._client_wrapper)
        return self._acls

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def project_automations(self):
        if self._project_automations is None:
            from .project_automations.client import ProjectAutomationsClient

            self._project_automations = ProjectAutomationsClient(client_wrapper=self._client_wrapper)
        return self._project_automations

    @property
    def project_scores(self):
        if self._project_scores is None:
            from .project_scores.client import ProjectScoresClient

            self._project_scores = ProjectScoresClient(client_wrapper=self._client_wrapper)
        return self._project_scores

    @property
    def project_tags(self):
        if self._project_tags is None:
            from .project_tags.client import ProjectTagsClient

            self._project_tags = ProjectTagsClient(client_wrapper=self._client_wrapper)
        return self._project_tags

    @property
    def span_iframes(self):
        if self._span_iframes is None:
            from .span_iframes.client import SpanIframesClient

            self._span_iframes = SpanIframesClient(client_wrapper=self._client_wrapper)
        return self._span_iframes

    @property
    def eval_status_pages(self):
        if self._eval_status_pages is None:
            from .eval_status_pages.client import EvalStatusPagesClient

            self._eval_status_pages = EvalStatusPagesClient(client_wrapper=self._client_wrapper)
        return self._eval_status_pages

    @property
    def functions(self):
        if self._functions is None:
            from .functions.client import FunctionsClient

            self._functions = FunctionsClient(client_wrapper=self._client_wrapper)
        return self._functions

    @property
    def views(self):
        if self._views is None:
            from .views.client import ViewsClient

            self._views = ViewsClient(client_wrapper=self._client_wrapper)
        return self._views

    @property
    def organizations(self):
        if self._organizations is None:
            from .organizations.client import OrganizationsClient

            self._organizations = OrganizationsClient(client_wrapper=self._client_wrapper)
        return self._organizations

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import ApiKeysClient

            self._api_keys = ApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def service_tokens(self):
        if self._service_tokens is None:
            from .service_tokens.client import ServiceTokensClient

            self._service_tokens = ServiceTokensClient(client_wrapper=self._client_wrapper)
        return self._service_tokens

    @property
    def ai_secrets(self):
        if self._ai_secrets is None:
            from .ai_secrets.client import AiSecretsClient

            self._ai_secrets = AiSecretsClient(client_wrapper=self._client_wrapper)
        return self._ai_secrets

    @property
    def env_vars(self):
        if self._env_vars is None:
            from .env_vars.client import EnvVarsClient

            self._env_vars = EnvVarsClient(client_wrapper=self._client_wrapper)
        return self._env_vars

    @property
    def mcp_servers(self):
        if self._mcp_servers is None:
            from .mcp_servers.client import McpServersClient

            self._mcp_servers = McpServersClient(client_wrapper=self._client_wrapper)
        return self._mcp_servers

    @property
    def dataset_snapshots(self):
        if self._dataset_snapshots is None:
            from .dataset_snapshots.client import DatasetSnapshotsClient

            self._dataset_snapshots = DatasetSnapshotsClient(client_wrapper=self._client_wrapper)
        return self._dataset_snapshots

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import EnvironmentsClient

            self._environments = EnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def other(self):
        if self._other is None:
            from .other.client import OtherClient

            self._other = OtherClient(client_wrapper=self._client_wrapper)
        return self._other

    @property
    def cross_object(self):
        if self._cross_object is None:
            from .cross_object.client import CrossObjectClient

            self._cross_object = CrossObjectClient(client_wrapper=self._client_wrapper)
        return self._cross_object

    @property
    def proxy(self):
        if self._proxy is None:
            from .proxy.client import ProxyClient

            self._proxy = ProxyClient(client_wrapper=self._client_wrapper)
        return self._proxy

    @property
    def evals(self):
        if self._evals is None:
            from .evals.client import EvalsClient

            self._evals = EvalsClient(client_wrapper=self._client_wrapper)
        return self._evals


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
        self._projects: typing.Optional[AsyncProjectsClient] = None
        self._logs: typing.Optional[AsyncLogsClient] = None
        self._experiments: typing.Optional[AsyncExperimentsClient] = None
        self._datasets: typing.Optional[AsyncDatasetsClient] = None
        self._prompts: typing.Optional[AsyncPromptsClient] = None
        self._roles: typing.Optional[AsyncRolesClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._acls: typing.Optional[AsyncAclsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._project_automations: typing.Optional[AsyncProjectAutomationsClient] = None
        self._project_scores: typing.Optional[AsyncProjectScoresClient] = None
        self._project_tags: typing.Optional[AsyncProjectTagsClient] = None
        self._span_iframes: typing.Optional[AsyncSpanIframesClient] = None
        self._eval_status_pages: typing.Optional[AsyncEvalStatusPagesClient] = None
        self._functions: typing.Optional[AsyncFunctionsClient] = None
        self._views: typing.Optional[AsyncViewsClient] = None
        self._organizations: typing.Optional[AsyncOrganizationsClient] = None
        self._api_keys: typing.Optional[AsyncApiKeysClient] = None
        self._service_tokens: typing.Optional[AsyncServiceTokensClient] = None
        self._ai_secrets: typing.Optional[AsyncAiSecretsClient] = None
        self._env_vars: typing.Optional[AsyncEnvVarsClient] = None
        self._mcp_servers: typing.Optional[AsyncMcpServersClient] = None
        self._dataset_snapshots: typing.Optional[AsyncDatasetSnapshotsClient] = None
        self._environments: typing.Optional[AsyncEnvironmentsClient] = None
        self._other: typing.Optional[AsyncOtherClient] = None
        self._cross_object: typing.Optional[AsyncCrossObjectClient] = None
        self._proxy: typing.Optional[AsyncProxyClient] = None
        self._evals: typing.Optional[AsyncEvalsClient] = None

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            self._projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import AsyncLogsClient

            self._logs = AsyncLogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def experiments(self):
        if self._experiments is None:
            from .experiments.client import AsyncExperimentsClient

            self._experiments = AsyncExperimentsClient(client_wrapper=self._client_wrapper)
        return self._experiments

    @property
    def datasets(self):
        if self._datasets is None:
            from .datasets.client import AsyncDatasetsClient

            self._datasets = AsyncDatasetsClient(client_wrapper=self._client_wrapper)
        return self._datasets

    @property
    def prompts(self):
        if self._prompts is None:
            from .prompts.client import AsyncPromptsClient

            self._prompts = AsyncPromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import AsyncRolesClient

            self._roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def acls(self):
        if self._acls is None:
            from .acls.client import AsyncAclsClient

            self._acls = AsyncAclsClient(client_wrapper=self._client_wrapper)
        return self._acls

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def project_automations(self):
        if self._project_automations is None:
            from .project_automations.client import AsyncProjectAutomationsClient

            self._project_automations = AsyncProjectAutomationsClient(client_wrapper=self._client_wrapper)
        return self._project_automations

    @property
    def project_scores(self):
        if self._project_scores is None:
            from .project_scores.client import AsyncProjectScoresClient

            self._project_scores = AsyncProjectScoresClient(client_wrapper=self._client_wrapper)
        return self._project_scores

    @property
    def project_tags(self):
        if self._project_tags is None:
            from .project_tags.client import AsyncProjectTagsClient

            self._project_tags = AsyncProjectTagsClient(client_wrapper=self._client_wrapper)
        return self._project_tags

    @property
    def span_iframes(self):
        if self._span_iframes is None:
            from .span_iframes.client import AsyncSpanIframesClient

            self._span_iframes = AsyncSpanIframesClient(client_wrapper=self._client_wrapper)
        return self._span_iframes

    @property
    def eval_status_pages(self):
        if self._eval_status_pages is None:
            from .eval_status_pages.client import AsyncEvalStatusPagesClient

            self._eval_status_pages = AsyncEvalStatusPagesClient(client_wrapper=self._client_wrapper)
        return self._eval_status_pages

    @property
    def functions(self):
        if self._functions is None:
            from .functions.client import AsyncFunctionsClient

            self._functions = AsyncFunctionsClient(client_wrapper=self._client_wrapper)
        return self._functions

    @property
    def views(self):
        if self._views is None:
            from .views.client import AsyncViewsClient

            self._views = AsyncViewsClient(client_wrapper=self._client_wrapper)
        return self._views

    @property
    def organizations(self):
        if self._organizations is None:
            from .organizations.client import AsyncOrganizationsClient

            self._organizations = AsyncOrganizationsClient(client_wrapper=self._client_wrapper)
        return self._organizations

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import AsyncApiKeysClient

            self._api_keys = AsyncApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def service_tokens(self):
        if self._service_tokens is None:
            from .service_tokens.client import AsyncServiceTokensClient

            self._service_tokens = AsyncServiceTokensClient(client_wrapper=self._client_wrapper)
        return self._service_tokens

    @property
    def ai_secrets(self):
        if self._ai_secrets is None:
            from .ai_secrets.client import AsyncAiSecretsClient

            self._ai_secrets = AsyncAiSecretsClient(client_wrapper=self._client_wrapper)
        return self._ai_secrets

    @property
    def env_vars(self):
        if self._env_vars is None:
            from .env_vars.client import AsyncEnvVarsClient

            self._env_vars = AsyncEnvVarsClient(client_wrapper=self._client_wrapper)
        return self._env_vars

    @property
    def mcp_servers(self):
        if self._mcp_servers is None:
            from .mcp_servers.client import AsyncMcpServersClient

            self._mcp_servers = AsyncMcpServersClient(client_wrapper=self._client_wrapper)
        return self._mcp_servers

    @property
    def dataset_snapshots(self):
        if self._dataset_snapshots is None:
            from .dataset_snapshots.client import AsyncDatasetSnapshotsClient

            self._dataset_snapshots = AsyncDatasetSnapshotsClient(client_wrapper=self._client_wrapper)
        return self._dataset_snapshots

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import AsyncEnvironmentsClient

            self._environments = AsyncEnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def other(self):
        if self._other is None:
            from .other.client import AsyncOtherClient

            self._other = AsyncOtherClient(client_wrapper=self._client_wrapper)
        return self._other

    @property
    def cross_object(self):
        if self._cross_object is None:
            from .cross_object.client import AsyncCrossObjectClient

            self._cross_object = AsyncCrossObjectClient(client_wrapper=self._client_wrapper)
        return self._cross_object

    @property
    def proxy(self):
        if self._proxy is None:
            from .proxy.client import AsyncProxyClient

            self._proxy = AsyncProxyClient(client_wrapper=self._client_wrapper)
        return self._proxy

    @property
    def evals(self):
        if self._evals is None:
            from .evals.client import AsyncEvalsClient

            self._evals = AsyncEvalsClient(client_wrapper=self._client_wrapper)
        return self._evals


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
