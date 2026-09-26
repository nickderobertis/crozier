

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .deployment.client import AsyncDeploymentClient, DeploymentClient
    from .documentation.client import AsyncDocumentationClient, DocumentationClient
    from .embeddings.client import AsyncEmbeddingsClient, EmbeddingsClient
    from .intelligence.client import AsyncIntelligenceClient, IntelligenceClient
    from .knowledge.client import AsyncKnowledgeClient, KnowledgeClient
    from .management.client import AsyncManagementClient, ManagementClient
    from .mcp_protocol.client import AsyncMcpProtocolClient, McpProtocolClient
    from .observability.client import AsyncObservabilityClient, ObservabilityClient
    from .operations.client import AsyncOperationsClient, OperationsClient
    from .project_setup.client import AsyncProjectSetupClient, ProjectSetupClient
    from .prompts.client import AsyncPromptsClient, PromptsClient
    from .resources.client import AsyncResourcesClient, ResourcesClient
    from .sessions.client import AsyncSessionsClient, SessionsClient
    from .system.client import AsyncSystemClient, SystemClient
    from .tools.client import AsyncToolsClient, ToolsClient
    from .troubleshooting.client import AsyncTroubleshootingClient, TroubleshootingClient
    from .users.client import AsyncUsersClient, UsersClient
    from .visualization.client import AsyncVisualizationClient, VisualizationClient


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
        self._mcp_protocol: typing.Optional[McpProtocolClient] = None
        self._intelligence: typing.Optional[IntelligenceClient] = None
        self._knowledge: typing.Optional[KnowledgeClient] = None
        self._management: typing.Optional[ManagementClient] = None
        self._operations: typing.Optional[OperationsClient] = None
        self._project_setup: typing.Optional[ProjectSetupClient] = None
        self._deployment: typing.Optional[DeploymentClient] = None
        self._troubleshooting: typing.Optional[TroubleshootingClient] = None
        self._system: typing.Optional[SystemClient] = None
        self._tools: typing.Optional[ToolsClient] = None
        self._documentation: typing.Optional[DocumentationClient] = None
        self._resources: typing.Optional[ResourcesClient] = None
        self._observability: typing.Optional[ObservabilityClient] = None
        self._prompts: typing.Optional[PromptsClient] = None
        self._visualization: typing.Optional[VisualizationClient] = None
        self._sessions: typing.Optional[SessionsClient] = None
        self._embeddings: typing.Optional[EmbeddingsClient] = None
        self._users: typing.Optional[UsersClient] = None

    @property
    def mcp_protocol(self):
        if self._mcp_protocol is None:
            from .mcp_protocol.client import McpProtocolClient

            self._mcp_protocol = McpProtocolClient(client_wrapper=self._client_wrapper)
        return self._mcp_protocol

    @property
    def intelligence(self):
        if self._intelligence is None:
            from .intelligence.client import IntelligenceClient

            self._intelligence = IntelligenceClient(client_wrapper=self._client_wrapper)
        return self._intelligence

    @property
    def knowledge(self):
        if self._knowledge is None:
            from .knowledge.client import KnowledgeClient

            self._knowledge = KnowledgeClient(client_wrapper=self._client_wrapper)
        return self._knowledge

    @property
    def management(self):
        if self._management is None:
            from .management.client import ManagementClient

            self._management = ManagementClient(client_wrapper=self._client_wrapper)
        return self._management

    @property
    def operations(self):
        if self._operations is None:
            from .operations.client import OperationsClient

            self._operations = OperationsClient(client_wrapper=self._client_wrapper)
        return self._operations

    @property
    def project_setup(self):
        if self._project_setup is None:
            from .project_setup.client import ProjectSetupClient

            self._project_setup = ProjectSetupClient(client_wrapper=self._client_wrapper)
        return self._project_setup

    @property
    def deployment(self):
        if self._deployment is None:
            from .deployment.client import DeploymentClient

            self._deployment = DeploymentClient(client_wrapper=self._client_wrapper)
        return self._deployment

    @property
    def troubleshooting(self):
        if self._troubleshooting is None:
            from .troubleshooting.client import TroubleshootingClient

            self._troubleshooting = TroubleshootingClient(client_wrapper=self._client_wrapper)
        return self._troubleshooting

    @property
    def system(self):
        if self._system is None:
            from .system.client import SystemClient

            self._system = SystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def tools(self):
        if self._tools is None:
            from .tools.client import ToolsClient

            self._tools = ToolsClient(client_wrapper=self._client_wrapper)
        return self._tools

    @property
    def documentation(self):
        if self._documentation is None:
            from .documentation.client import DocumentationClient

            self._documentation = DocumentationClient(client_wrapper=self._client_wrapper)
        return self._documentation

    @property
    def resources(self):
        if self._resources is None:
            from .resources.client import ResourcesClient

            self._resources = ResourcesClient(client_wrapper=self._client_wrapper)
        return self._resources

    @property
    def observability(self):
        if self._observability is None:
            from .observability.client import ObservabilityClient

            self._observability = ObservabilityClient(client_wrapper=self._client_wrapper)
        return self._observability

    @property
    def prompts(self):
        if self._prompts is None:
            from .prompts.client import PromptsClient

            self._prompts = PromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def visualization(self):
        if self._visualization is None:
            from .visualization.client import VisualizationClient

            self._visualization = VisualizationClient(client_wrapper=self._client_wrapper)
        return self._visualization

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import SessionsClient

            self._sessions = SessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def embeddings(self):
        if self._embeddings is None:
            from .embeddings.client import EmbeddingsClient

            self._embeddings = EmbeddingsClient(client_wrapper=self._client_wrapper)
        return self._embeddings

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users


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
        self._mcp_protocol: typing.Optional[AsyncMcpProtocolClient] = None
        self._intelligence: typing.Optional[AsyncIntelligenceClient] = None
        self._knowledge: typing.Optional[AsyncKnowledgeClient] = None
        self._management: typing.Optional[AsyncManagementClient] = None
        self._operations: typing.Optional[AsyncOperationsClient] = None
        self._project_setup: typing.Optional[AsyncProjectSetupClient] = None
        self._deployment: typing.Optional[AsyncDeploymentClient] = None
        self._troubleshooting: typing.Optional[AsyncTroubleshootingClient] = None
        self._system: typing.Optional[AsyncSystemClient] = None
        self._tools: typing.Optional[AsyncToolsClient] = None
        self._documentation: typing.Optional[AsyncDocumentationClient] = None
        self._resources: typing.Optional[AsyncResourcesClient] = None
        self._observability: typing.Optional[AsyncObservabilityClient] = None
        self._prompts: typing.Optional[AsyncPromptsClient] = None
        self._visualization: typing.Optional[AsyncVisualizationClient] = None
        self._sessions: typing.Optional[AsyncSessionsClient] = None
        self._embeddings: typing.Optional[AsyncEmbeddingsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None

    @property
    def mcp_protocol(self):
        if self._mcp_protocol is None:
            from .mcp_protocol.client import AsyncMcpProtocolClient

            self._mcp_protocol = AsyncMcpProtocolClient(client_wrapper=self._client_wrapper)
        return self._mcp_protocol

    @property
    def intelligence(self):
        if self._intelligence is None:
            from .intelligence.client import AsyncIntelligenceClient

            self._intelligence = AsyncIntelligenceClient(client_wrapper=self._client_wrapper)
        return self._intelligence

    @property
    def knowledge(self):
        if self._knowledge is None:
            from .knowledge.client import AsyncKnowledgeClient

            self._knowledge = AsyncKnowledgeClient(client_wrapper=self._client_wrapper)
        return self._knowledge

    @property
    def management(self):
        if self._management is None:
            from .management.client import AsyncManagementClient

            self._management = AsyncManagementClient(client_wrapper=self._client_wrapper)
        return self._management

    @property
    def operations(self):
        if self._operations is None:
            from .operations.client import AsyncOperationsClient

            self._operations = AsyncOperationsClient(client_wrapper=self._client_wrapper)
        return self._operations

    @property
    def project_setup(self):
        if self._project_setup is None:
            from .project_setup.client import AsyncProjectSetupClient

            self._project_setup = AsyncProjectSetupClient(client_wrapper=self._client_wrapper)
        return self._project_setup

    @property
    def deployment(self):
        if self._deployment is None:
            from .deployment.client import AsyncDeploymentClient

            self._deployment = AsyncDeploymentClient(client_wrapper=self._client_wrapper)
        return self._deployment

    @property
    def troubleshooting(self):
        if self._troubleshooting is None:
            from .troubleshooting.client import AsyncTroubleshootingClient

            self._troubleshooting = AsyncTroubleshootingClient(client_wrapper=self._client_wrapper)
        return self._troubleshooting

    @property
    def system(self):
        if self._system is None:
            from .system.client import AsyncSystemClient

            self._system = AsyncSystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def tools(self):
        if self._tools is None:
            from .tools.client import AsyncToolsClient

            self._tools = AsyncToolsClient(client_wrapper=self._client_wrapper)
        return self._tools

    @property
    def documentation(self):
        if self._documentation is None:
            from .documentation.client import AsyncDocumentationClient

            self._documentation = AsyncDocumentationClient(client_wrapper=self._client_wrapper)
        return self._documentation

    @property
    def resources(self):
        if self._resources is None:
            from .resources.client import AsyncResourcesClient

            self._resources = AsyncResourcesClient(client_wrapper=self._client_wrapper)
        return self._resources

    @property
    def observability(self):
        if self._observability is None:
            from .observability.client import AsyncObservabilityClient

            self._observability = AsyncObservabilityClient(client_wrapper=self._client_wrapper)
        return self._observability

    @property
    def prompts(self):
        if self._prompts is None:
            from .prompts.client import AsyncPromptsClient

            self._prompts = AsyncPromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def visualization(self):
        if self._visualization is None:
            from .visualization.client import AsyncVisualizationClient

            self._visualization = AsyncVisualizationClient(client_wrapper=self._client_wrapper)
        return self._visualization

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import AsyncSessionsClient

            self._sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def embeddings(self):
        if self._embeddings is None:
            from .embeddings.client import AsyncEmbeddingsClient

            self._embeddings = AsyncEmbeddingsClient(client_wrapper=self._client_wrapper)
        return self._embeddings

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
