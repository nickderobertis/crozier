

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .agents.client import AgentsClient, AsyncAgentsClient
    from .archives.client import ArchivesClient, AsyncArchivesClient
    from .blocks.client import AsyncBlocksClient, BlocksClient
    from .chat.client import AsyncChatClient, ChatClient
    from .client_side_access_tokens.client import AsyncClientSideAccessTokensClient, ClientSideAccessTokensClient
    from .conversations.client import AsyncConversationsClient, ConversationsClient
    from .embeddings.client import AsyncEmbeddingsClient, EmbeddingsClient
    from .feeds.client import AsyncFeedsClient, FeedsClient
    from .folders.client import AsyncFoldersClient, FoldersClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .health.client import AsyncHealthClient, HealthClient
    from .identities.client import AsyncIdentitiesClient, IdentitiesClient
    from .internal_agents.client import AsyncInternalAgentsClient, InternalAgentsClient
    from .internal_blocks.client import AsyncInternalBlocksClient, InternalBlocksClient
    from .internal_runs.client import AsyncInternalRunsClient, InternalRunsClient
    from .internal_templates.client import AsyncInternalTemplatesClient, InternalTemplatesClient
    from .jobs.client import AsyncJobsClient, JobsClient
    from .mcp_servers.client import AsyncMcpServersClient, McpServersClient
    from .messages.client import AsyncMessagesClient, MessagesClient
    from .metadata.client import AsyncMetadataClient, MetadataClient
    from .models.client import AsyncModelsClient, ModelsClient
    from .passages.client import AsyncPassagesClient, PassagesClient
    from .pipelines.client import AsyncPipelinesClient, PipelinesClient
    from .projects.client import AsyncProjectsClient, ProjectsClient
    from .providers.client import AsyncProvidersClient, ProvidersClient
    from .runs.client import AsyncRunsClient, RunsClient
    from .scheduled_messages.client import AsyncScheduledMessagesClient, ScheduledMessagesClient
    from .sources.client import AsyncSourcesClient, SourcesClient
    from .steps.client import AsyncStepsClient, StepsClient
    from .tag.client import AsyncTagClient, TagClient
    from .telemetry.client import AsyncTelemetryClient, TelemetryClient
    from .templates.client import AsyncTemplatesClient, TemplatesClient
    from .tools.client import AsyncToolsClient, ToolsClient
    from .voice.client import AsyncVoiceClient, VoiceClient


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
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._archives: typing.Optional[ArchivesClient] = None
        self._tools: typing.Optional[ToolsClient] = None
        self._sources: typing.Optional[SourcesClient] = None
        self._folders: typing.Optional[FoldersClient] = None
        self._agents: typing.Optional[AgentsClient] = None
        self._conversations: typing.Optional[ConversationsClient] = None
        self._chat: typing.Optional[ChatClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._identities: typing.Optional[IdentitiesClient] = None
        self._internal_agents: typing.Optional[InternalAgentsClient] = None
        self._internal_blocks: typing.Optional[InternalBlocksClient] = None
        self._internal_runs: typing.Optional[InternalRunsClient] = None
        self._internal_templates: typing.Optional[InternalTemplatesClient] = None
        self._models: typing.Optional[ModelsClient] = None
        self._mcp_servers: typing.Optional[McpServersClient] = None
        self._blocks: typing.Optional[BlocksClient] = None
        self._jobs: typing.Optional[JobsClient] = None
        self._health: typing.Optional[HealthClient] = None
        self._providers: typing.Optional[ProvidersClient] = None
        self._runs: typing.Optional[RunsClient] = None
        self._steps: typing.Optional[StepsClient] = None
        self._tag: typing.Optional[TagClient] = None
        self._telemetry: typing.Optional[TelemetryClient] = None
        self._messages: typing.Optional[MessagesClient] = None
        self._passages: typing.Optional[PassagesClient] = None
        self._voice: typing.Optional[VoiceClient] = None
        self._embeddings: typing.Optional[EmbeddingsClient] = None
        self._templates: typing.Optional[TemplatesClient] = None
        self._client_side_access_tokens: typing.Optional[ClientSideAccessTokensClient] = None
        self._projects: typing.Optional[ProjectsClient] = None
        self._metadata: typing.Optional[MetadataClient] = None
        self._scheduled_messages: typing.Optional[ScheduledMessagesClient] = None
        self._feeds: typing.Optional[FeedsClient] = None
        self._pipelines: typing.Optional[PipelinesClient] = None

    @property
    def archives(self):
        if self._archives is None:
            from .archives.client import ArchivesClient

            self._archives = ArchivesClient(client_wrapper=self._client_wrapper)
        return self._archives

    @property
    def tools(self):
        if self._tools is None:
            from .tools.client import ToolsClient

            self._tools = ToolsClient(client_wrapper=self._client_wrapper)
        return self._tools

    @property
    def sources(self):
        if self._sources is None:
            from .sources.client import SourcesClient

            self._sources = SourcesClient(client_wrapper=self._client_wrapper)
        return self._sources

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import FoldersClient

            self._folders = FoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AgentsClient

            self._agents = AgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def conversations(self):
        if self._conversations is None:
            from .conversations.client import ConversationsClient

            self._conversations = ConversationsClient(client_wrapper=self._client_wrapper)
        return self._conversations

    @property
    def chat(self):
        if self._chat is None:
            from .chat.client import ChatClient

            self._chat = ChatClient(client_wrapper=self._client_wrapper)
        return self._chat

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def identities(self):
        if self._identities is None:
            from .identities.client import IdentitiesClient

            self._identities = IdentitiesClient(client_wrapper=self._client_wrapper)
        return self._identities

    @property
    def internal_agents(self):
        if self._internal_agents is None:
            from .internal_agents.client import InternalAgentsClient

            self._internal_agents = InternalAgentsClient(client_wrapper=self._client_wrapper)
        return self._internal_agents

    @property
    def internal_blocks(self):
        if self._internal_blocks is None:
            from .internal_blocks.client import InternalBlocksClient

            self._internal_blocks = InternalBlocksClient(client_wrapper=self._client_wrapper)
        return self._internal_blocks

    @property
    def internal_runs(self):
        if self._internal_runs is None:
            from .internal_runs.client import InternalRunsClient

            self._internal_runs = InternalRunsClient(client_wrapper=self._client_wrapper)
        return self._internal_runs

    @property
    def internal_templates(self):
        if self._internal_templates is None:
            from .internal_templates.client import InternalTemplatesClient

            self._internal_templates = InternalTemplatesClient(client_wrapper=self._client_wrapper)
        return self._internal_templates

    @property
    def models(self):
        if self._models is None:
            from .models.client import ModelsClient

            self._models = ModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def mcp_servers(self):
        if self._mcp_servers is None:
            from .mcp_servers.client import McpServersClient

            self._mcp_servers = McpServersClient(client_wrapper=self._client_wrapper)
        return self._mcp_servers

    @property
    def blocks(self):
        if self._blocks is None:
            from .blocks.client import BlocksClient

            self._blocks = BlocksClient(client_wrapper=self._client_wrapper)
        return self._blocks

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import JobsClient

            self._jobs = JobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def providers(self):
        if self._providers is None:
            from .providers.client import ProvidersClient

            self._providers = ProvidersClient(client_wrapper=self._client_wrapper)
        return self._providers

    @property
    def runs(self):
        if self._runs is None:
            from .runs.client import RunsClient

            self._runs = RunsClient(client_wrapper=self._client_wrapper)
        return self._runs

    @property
    def steps(self):
        if self._steps is None:
            from .steps.client import StepsClient

            self._steps = StepsClient(client_wrapper=self._client_wrapper)
        return self._steps

    @property
    def tag(self):
        if self._tag is None:
            from .tag.client import TagClient

            self._tag = TagClient(client_wrapper=self._client_wrapper)
        return self._tag

    @property
    def telemetry(self):
        if self._telemetry is None:
            from .telemetry.client import TelemetryClient

            self._telemetry = TelemetryClient(client_wrapper=self._client_wrapper)
        return self._telemetry

    @property
    def messages(self):
        if self._messages is None:
            from .messages.client import MessagesClient

            self._messages = MessagesClient(client_wrapper=self._client_wrapper)
        return self._messages

    @property
    def passages(self):
        if self._passages is None:
            from .passages.client import PassagesClient

            self._passages = PassagesClient(client_wrapper=self._client_wrapper)
        return self._passages

    @property
    def voice(self):
        if self._voice is None:
            from .voice.client import VoiceClient

            self._voice = VoiceClient(client_wrapper=self._client_wrapper)
        return self._voice

    @property
    def embeddings(self):
        if self._embeddings is None:
            from .embeddings.client import EmbeddingsClient

            self._embeddings = EmbeddingsClient(client_wrapper=self._client_wrapper)
        return self._embeddings

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import TemplatesClient

            self._templates = TemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates

    @property
    def client_side_access_tokens(self):
        if self._client_side_access_tokens is None:
            from .client_side_access_tokens.client import ClientSideAccessTokensClient

            self._client_side_access_tokens = ClientSideAccessTokensClient(client_wrapper=self._client_wrapper)
        return self._client_side_access_tokens

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import ProjectsClient

            self._projects = ProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import MetadataClient

            self._metadata = MetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def scheduled_messages(self):
        if self._scheduled_messages is None:
            from .scheduled_messages.client import ScheduledMessagesClient

            self._scheduled_messages = ScheduledMessagesClient(client_wrapper=self._client_wrapper)
        return self._scheduled_messages

    @property
    def feeds(self):
        if self._feeds is None:
            from .feeds.client import FeedsClient

            self._feeds = FeedsClient(client_wrapper=self._client_wrapper)
        return self._feeds

    @property
    def pipelines(self):
        if self._pipelines is None:
            from .pipelines.client import PipelinesClient

            self._pipelines = PipelinesClient(client_wrapper=self._client_wrapper)
        return self._pipelines


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
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._archives: typing.Optional[AsyncArchivesClient] = None
        self._tools: typing.Optional[AsyncToolsClient] = None
        self._sources: typing.Optional[AsyncSourcesClient] = None
        self._folders: typing.Optional[AsyncFoldersClient] = None
        self._agents: typing.Optional[AsyncAgentsClient] = None
        self._conversations: typing.Optional[AsyncConversationsClient] = None
        self._chat: typing.Optional[AsyncChatClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._identities: typing.Optional[AsyncIdentitiesClient] = None
        self._internal_agents: typing.Optional[AsyncInternalAgentsClient] = None
        self._internal_blocks: typing.Optional[AsyncInternalBlocksClient] = None
        self._internal_runs: typing.Optional[AsyncInternalRunsClient] = None
        self._internal_templates: typing.Optional[AsyncInternalTemplatesClient] = None
        self._models: typing.Optional[AsyncModelsClient] = None
        self._mcp_servers: typing.Optional[AsyncMcpServersClient] = None
        self._blocks: typing.Optional[AsyncBlocksClient] = None
        self._jobs: typing.Optional[AsyncJobsClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None
        self._providers: typing.Optional[AsyncProvidersClient] = None
        self._runs: typing.Optional[AsyncRunsClient] = None
        self._steps: typing.Optional[AsyncStepsClient] = None
        self._tag: typing.Optional[AsyncTagClient] = None
        self._telemetry: typing.Optional[AsyncTelemetryClient] = None
        self._messages: typing.Optional[AsyncMessagesClient] = None
        self._passages: typing.Optional[AsyncPassagesClient] = None
        self._voice: typing.Optional[AsyncVoiceClient] = None
        self._embeddings: typing.Optional[AsyncEmbeddingsClient] = None
        self._templates: typing.Optional[AsyncTemplatesClient] = None
        self._client_side_access_tokens: typing.Optional[AsyncClientSideAccessTokensClient] = None
        self._projects: typing.Optional[AsyncProjectsClient] = None
        self._metadata: typing.Optional[AsyncMetadataClient] = None
        self._scheduled_messages: typing.Optional[AsyncScheduledMessagesClient] = None
        self._feeds: typing.Optional[AsyncFeedsClient] = None
        self._pipelines: typing.Optional[AsyncPipelinesClient] = None

    @property
    def archives(self):
        if self._archives is None:
            from .archives.client import AsyncArchivesClient

            self._archives = AsyncArchivesClient(client_wrapper=self._client_wrapper)
        return self._archives

    @property
    def tools(self):
        if self._tools is None:
            from .tools.client import AsyncToolsClient

            self._tools = AsyncToolsClient(client_wrapper=self._client_wrapper)
        return self._tools

    @property
    def sources(self):
        if self._sources is None:
            from .sources.client import AsyncSourcesClient

            self._sources = AsyncSourcesClient(client_wrapper=self._client_wrapper)
        return self._sources

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import AsyncFoldersClient

            self._folders = AsyncFoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AsyncAgentsClient

            self._agents = AsyncAgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def conversations(self):
        if self._conversations is None:
            from .conversations.client import AsyncConversationsClient

            self._conversations = AsyncConversationsClient(client_wrapper=self._client_wrapper)
        return self._conversations

    @property
    def chat(self):
        if self._chat is None:
            from .chat.client import AsyncChatClient

            self._chat = AsyncChatClient(client_wrapper=self._client_wrapper)
        return self._chat

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def identities(self):
        if self._identities is None:
            from .identities.client import AsyncIdentitiesClient

            self._identities = AsyncIdentitiesClient(client_wrapper=self._client_wrapper)
        return self._identities

    @property
    def internal_agents(self):
        if self._internal_agents is None:
            from .internal_agents.client import AsyncInternalAgentsClient

            self._internal_agents = AsyncInternalAgentsClient(client_wrapper=self._client_wrapper)
        return self._internal_agents

    @property
    def internal_blocks(self):
        if self._internal_blocks is None:
            from .internal_blocks.client import AsyncInternalBlocksClient

            self._internal_blocks = AsyncInternalBlocksClient(client_wrapper=self._client_wrapper)
        return self._internal_blocks

    @property
    def internal_runs(self):
        if self._internal_runs is None:
            from .internal_runs.client import AsyncInternalRunsClient

            self._internal_runs = AsyncInternalRunsClient(client_wrapper=self._client_wrapper)
        return self._internal_runs

    @property
    def internal_templates(self):
        if self._internal_templates is None:
            from .internal_templates.client import AsyncInternalTemplatesClient

            self._internal_templates = AsyncInternalTemplatesClient(client_wrapper=self._client_wrapper)
        return self._internal_templates

    @property
    def models(self):
        if self._models is None:
            from .models.client import AsyncModelsClient

            self._models = AsyncModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def mcp_servers(self):
        if self._mcp_servers is None:
            from .mcp_servers.client import AsyncMcpServersClient

            self._mcp_servers = AsyncMcpServersClient(client_wrapper=self._client_wrapper)
        return self._mcp_servers

    @property
    def blocks(self):
        if self._blocks is None:
            from .blocks.client import AsyncBlocksClient

            self._blocks = AsyncBlocksClient(client_wrapper=self._client_wrapper)
        return self._blocks

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import AsyncJobsClient

            self._jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def providers(self):
        if self._providers is None:
            from .providers.client import AsyncProvidersClient

            self._providers = AsyncProvidersClient(client_wrapper=self._client_wrapper)
        return self._providers

    @property
    def runs(self):
        if self._runs is None:
            from .runs.client import AsyncRunsClient

            self._runs = AsyncRunsClient(client_wrapper=self._client_wrapper)
        return self._runs

    @property
    def steps(self):
        if self._steps is None:
            from .steps.client import AsyncStepsClient

            self._steps = AsyncStepsClient(client_wrapper=self._client_wrapper)
        return self._steps

    @property
    def tag(self):
        if self._tag is None:
            from .tag.client import AsyncTagClient

            self._tag = AsyncTagClient(client_wrapper=self._client_wrapper)
        return self._tag

    @property
    def telemetry(self):
        if self._telemetry is None:
            from .telemetry.client import AsyncTelemetryClient

            self._telemetry = AsyncTelemetryClient(client_wrapper=self._client_wrapper)
        return self._telemetry

    @property
    def messages(self):
        if self._messages is None:
            from .messages.client import AsyncMessagesClient

            self._messages = AsyncMessagesClient(client_wrapper=self._client_wrapper)
        return self._messages

    @property
    def passages(self):
        if self._passages is None:
            from .passages.client import AsyncPassagesClient

            self._passages = AsyncPassagesClient(client_wrapper=self._client_wrapper)
        return self._passages

    @property
    def voice(self):
        if self._voice is None:
            from .voice.client import AsyncVoiceClient

            self._voice = AsyncVoiceClient(client_wrapper=self._client_wrapper)
        return self._voice

    @property
    def embeddings(self):
        if self._embeddings is None:
            from .embeddings.client import AsyncEmbeddingsClient

            self._embeddings = AsyncEmbeddingsClient(client_wrapper=self._client_wrapper)
        return self._embeddings

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import AsyncTemplatesClient

            self._templates = AsyncTemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates

    @property
    def client_side_access_tokens(self):
        if self._client_side_access_tokens is None:
            from .client_side_access_tokens.client import AsyncClientSideAccessTokensClient

            self._client_side_access_tokens = AsyncClientSideAccessTokensClient(client_wrapper=self._client_wrapper)
        return self._client_side_access_tokens

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            self._projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import AsyncMetadataClient

            self._metadata = AsyncMetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def scheduled_messages(self):
        if self._scheduled_messages is None:
            from .scheduled_messages.client import AsyncScheduledMessagesClient

            self._scheduled_messages = AsyncScheduledMessagesClient(client_wrapper=self._client_wrapper)
        return self._scheduled_messages

    @property
    def feeds(self):
        if self._feeds is None:
            from .feeds.client import AsyncFeedsClient

            self._feeds = AsyncFeedsClient(client_wrapper=self._client_wrapper)
        return self._feeds

    @property
    def pipelines(self):
        if self._pipelines is None:
            from .pipelines.client import AsyncPipelinesClient

            self._pipelines = AsyncPipelinesClient(client_wrapper=self._client_wrapper)
        return self._pipelines


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
