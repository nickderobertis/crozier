

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .analytics.client import AnalyticsClient, AsyncAnalyticsClient
    from .chat.client import AsyncChatClient, ChatClient
    from .code.client import AsyncCodeClient, CodeClient
    from .conversation.client import AsyncConversationClient, ConversationClient
    from .document.client import AsyncDocumentClient, DocumentClient
    from .feedback.client import AsyncFeedbackClient, FeedbackClient
    from .guidance.client import AsyncGuidanceClient, GuidanceClient
    from .health.client import AsyncHealthClient, HealthClient
    from .index.client import AsyncIndexClient, IndexClient
    from .mcp.client import AsyncMcpClient, McpClient
    from .query.client import AsyncQueryClient, QueryClient
    from .reindexing.client import AsyncReindexingClient, ReindexingClient
    from .sdks.client import AsyncSdksClient, SdksClient
    from .settings.client import AsyncSettingsClient, SettingsClient
    from .slack_ask_fern.client import AsyncSlackAskFernClient, SlackAskFernClient
    from .slack_scribe.client import AsyncSlackScribeClient, SlackScribeClient
    from .website.client import AsyncWebsiteClient, WebsiteClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



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
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._analytics: typing.Optional[AnalyticsClient] = None
        self._chat: typing.Optional[ChatClient] = None
        self._code: typing.Optional[CodeClient] = None
        self._conversation: typing.Optional[ConversationClient] = None
        self._document: typing.Optional[DocumentClient] = None
        self._feedback: typing.Optional[FeedbackClient] = None
        self._guidance: typing.Optional[GuidanceClient] = None
        self._health: typing.Optional[HealthClient] = None
        self._index: typing.Optional[IndexClient] = None
        self._mcp: typing.Optional[McpClient] = None
        self._query: typing.Optional[QueryClient] = None
        self._reindexing: typing.Optional[ReindexingClient] = None
        self._sdks: typing.Optional[SdksClient] = None
        self._settings: typing.Optional[SettingsClient] = None
        self._slack_ask_fern: typing.Optional[SlackAskFernClient] = None
        self._slack_scribe: typing.Optional[SlackScribeClient] = None
        self._website: typing.Optional[WebsiteClient] = None

    @property
    def analytics(self):
        if self._analytics is None:
            from .analytics.client import AnalyticsClient

            self._analytics = AnalyticsClient(client_wrapper=self._client_wrapper)
        return self._analytics

    @property
    def chat(self):
        if self._chat is None:
            from .chat.client import ChatClient

            self._chat = ChatClient(client_wrapper=self._client_wrapper)
        return self._chat

    @property
    def code(self):
        if self._code is None:
            from .code.client import CodeClient

            self._code = CodeClient(client_wrapper=self._client_wrapper)
        return self._code

    @property
    def conversation(self):
        if self._conversation is None:
            from .conversation.client import ConversationClient

            self._conversation = ConversationClient(client_wrapper=self._client_wrapper)
        return self._conversation

    @property
    def document(self):
        if self._document is None:
            from .document.client import DocumentClient

            self._document = DocumentClient(client_wrapper=self._client_wrapper)
        return self._document

    @property
    def feedback(self):
        if self._feedback is None:
            from .feedback.client import FeedbackClient

            self._feedback = FeedbackClient(client_wrapper=self._client_wrapper)
        return self._feedback

    @property
    def guidance(self):
        if self._guidance is None:
            from .guidance.client import GuidanceClient

            self._guidance = GuidanceClient(client_wrapper=self._client_wrapper)
        return self._guidance

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def index(self):
        if self._index is None:
            from .index.client import IndexClient

            self._index = IndexClient(client_wrapper=self._client_wrapper)
        return self._index

    @property
    def mcp(self):
        if self._mcp is None:
            from .mcp.client import McpClient

            self._mcp = McpClient(client_wrapper=self._client_wrapper)
        return self._mcp

    @property
    def query(self):
        if self._query is None:
            from .query.client import QueryClient

            self._query = QueryClient(client_wrapper=self._client_wrapper)
        return self._query

    @property
    def reindexing(self):
        if self._reindexing is None:
            from .reindexing.client import ReindexingClient

            self._reindexing = ReindexingClient(client_wrapper=self._client_wrapper)
        return self._reindexing

    @property
    def sdks(self):
        if self._sdks is None:
            from .sdks.client import SdksClient

            self._sdks = SdksClient(client_wrapper=self._client_wrapper)
        return self._sdks

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import SettingsClient

            self._settings = SettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def slack_ask_fern(self):
        if self._slack_ask_fern is None:
            from .slack_ask_fern.client import SlackAskFernClient

            self._slack_ask_fern = SlackAskFernClient(client_wrapper=self._client_wrapper)
        return self._slack_ask_fern

    @property
    def slack_scribe(self):
        if self._slack_scribe is None:
            from .slack_scribe.client import SlackScribeClient

            self._slack_scribe = SlackScribeClient(client_wrapper=self._client_wrapper)
        return self._slack_scribe

    @property
    def website(self):
        if self._website is None:
            from .website.client import WebsiteClient

            self._website = WebsiteClient(client_wrapper=self._client_wrapper)
        return self._website


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



        Defaults to FernApiEnvironment.PRODUCTION



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
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._analytics: typing.Optional[AsyncAnalyticsClient] = None
        self._chat: typing.Optional[AsyncChatClient] = None
        self._code: typing.Optional[AsyncCodeClient] = None
        self._conversation: typing.Optional[AsyncConversationClient] = None
        self._document: typing.Optional[AsyncDocumentClient] = None
        self._feedback: typing.Optional[AsyncFeedbackClient] = None
        self._guidance: typing.Optional[AsyncGuidanceClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None
        self._index: typing.Optional[AsyncIndexClient] = None
        self._mcp: typing.Optional[AsyncMcpClient] = None
        self._query: typing.Optional[AsyncQueryClient] = None
        self._reindexing: typing.Optional[AsyncReindexingClient] = None
        self._sdks: typing.Optional[AsyncSdksClient] = None
        self._settings: typing.Optional[AsyncSettingsClient] = None
        self._slack_ask_fern: typing.Optional[AsyncSlackAskFernClient] = None
        self._slack_scribe: typing.Optional[AsyncSlackScribeClient] = None
        self._website: typing.Optional[AsyncWebsiteClient] = None

    @property
    def analytics(self):
        if self._analytics is None:
            from .analytics.client import AsyncAnalyticsClient

            self._analytics = AsyncAnalyticsClient(client_wrapper=self._client_wrapper)
        return self._analytics

    @property
    def chat(self):
        if self._chat is None:
            from .chat.client import AsyncChatClient

            self._chat = AsyncChatClient(client_wrapper=self._client_wrapper)
        return self._chat

    @property
    def code(self):
        if self._code is None:
            from .code.client import AsyncCodeClient

            self._code = AsyncCodeClient(client_wrapper=self._client_wrapper)
        return self._code

    @property
    def conversation(self):
        if self._conversation is None:
            from .conversation.client import AsyncConversationClient

            self._conversation = AsyncConversationClient(client_wrapper=self._client_wrapper)
        return self._conversation

    @property
    def document(self):
        if self._document is None:
            from .document.client import AsyncDocumentClient

            self._document = AsyncDocumentClient(client_wrapper=self._client_wrapper)
        return self._document

    @property
    def feedback(self):
        if self._feedback is None:
            from .feedback.client import AsyncFeedbackClient

            self._feedback = AsyncFeedbackClient(client_wrapper=self._client_wrapper)
        return self._feedback

    @property
    def guidance(self):
        if self._guidance is None:
            from .guidance.client import AsyncGuidanceClient

            self._guidance = AsyncGuidanceClient(client_wrapper=self._client_wrapper)
        return self._guidance

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def index(self):
        if self._index is None:
            from .index.client import AsyncIndexClient

            self._index = AsyncIndexClient(client_wrapper=self._client_wrapper)
        return self._index

    @property
    def mcp(self):
        if self._mcp is None:
            from .mcp.client import AsyncMcpClient

            self._mcp = AsyncMcpClient(client_wrapper=self._client_wrapper)
        return self._mcp

    @property
    def query(self):
        if self._query is None:
            from .query.client import AsyncQueryClient

            self._query = AsyncQueryClient(client_wrapper=self._client_wrapper)
        return self._query

    @property
    def reindexing(self):
        if self._reindexing is None:
            from .reindexing.client import AsyncReindexingClient

            self._reindexing = AsyncReindexingClient(client_wrapper=self._client_wrapper)
        return self._reindexing

    @property
    def sdks(self):
        if self._sdks is None:
            from .sdks.client import AsyncSdksClient

            self._sdks = AsyncSdksClient(client_wrapper=self._client_wrapper)
        return self._sdks

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import AsyncSettingsClient

            self._settings = AsyncSettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def slack_ask_fern(self):
        if self._slack_ask_fern is None:
            from .slack_ask_fern.client import AsyncSlackAskFernClient

            self._slack_ask_fern = AsyncSlackAskFernClient(client_wrapper=self._client_wrapper)
        return self._slack_ask_fern

    @property
    def slack_scribe(self):
        if self._slack_scribe is None:
            from .slack_scribe.client import AsyncSlackScribeClient

            self._slack_scribe = AsyncSlackScribeClient(client_wrapper=self._client_wrapper)
        return self._slack_scribe

    @property
    def website(self):
        if self._website is None:
            from .website.client import AsyncWebsiteClient

            self._website = AsyncWebsiteClient(client_wrapper=self._client_wrapper)
        return self._website


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
