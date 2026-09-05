

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .apps.client import AppsClient, AsyncAppsClient
    from .audiences.client import AsyncAudiencesClient, AudiencesClient
    from .autocompletes.client import AsyncAutocompletesClient, AutocompletesClient
    from .conversations.client import AsyncConversationsClient, ConversationsClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .industries.client import AsyncIndustriesClient, IndustriesClient
    from .markdown.client import AsyncMarkdownClient, MarkdownClient
    from .messages.client import AsyncMessagesClient, MessagesClient
    from .positions.client import AsyncPositionsClient, PositionsClient
    from .users.client import AsyncUsersClient, UsersClient
    from .webhooks.client import AsyncWebhooksClient, WebhooksClient


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
        self._apps: typing.Optional[AppsClient] = None
        self._audiences: typing.Optional[AudiencesClient] = None
        self._autocompletes: typing.Optional[AutocompletesClient] = None
        self._conversations: typing.Optional[ConversationsClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._industries: typing.Optional[IndustriesClient] = None
        self._markdown: typing.Optional[MarkdownClient] = None
        self._messages: typing.Optional[MessagesClient] = None
        self._positions: typing.Optional[PositionsClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None

    @property
    def apps(self):
        if self._apps is None:
            from .apps.client import AppsClient

            self._apps = AppsClient(client_wrapper=self._client_wrapper)
        return self._apps

    @property
    def audiences(self):
        if self._audiences is None:
            from .audiences.client import AudiencesClient

            self._audiences = AudiencesClient(client_wrapper=self._client_wrapper)
        return self._audiences

    @property
    def autocompletes(self):
        if self._autocompletes is None:
            from .autocompletes.client import AutocompletesClient

            self._autocompletes = AutocompletesClient(client_wrapper=self._client_wrapper)
        return self._autocompletes

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
    def industries(self):
        if self._industries is None:
            from .industries.client import IndustriesClient

            self._industries = IndustriesClient(client_wrapper=self._client_wrapper)
        return self._industries

    @property
    def markdown(self):
        if self._markdown is None:
            from .markdown.client import MarkdownClient

            self._markdown = MarkdownClient(client_wrapper=self._client_wrapper)
        return self._markdown

    @property
    def messages(self):
        if self._messages is None:
            from .messages.client import MessagesClient

            self._messages = MessagesClient(client_wrapper=self._client_wrapper)
        return self._messages

    @property
    def positions(self):
        if self._positions is None:
            from .positions.client import PositionsClient

            self._positions = PositionsClient(client_wrapper=self._client_wrapper)
        return self._positions

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient

            self._webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks


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
        self._apps: typing.Optional[AsyncAppsClient] = None
        self._audiences: typing.Optional[AsyncAudiencesClient] = None
        self._autocompletes: typing.Optional[AsyncAutocompletesClient] = None
        self._conversations: typing.Optional[AsyncConversationsClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._industries: typing.Optional[AsyncIndustriesClient] = None
        self._markdown: typing.Optional[AsyncMarkdownClient] = None
        self._messages: typing.Optional[AsyncMessagesClient] = None
        self._positions: typing.Optional[AsyncPositionsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None

    @property
    def apps(self):
        if self._apps is None:
            from .apps.client import AsyncAppsClient

            self._apps = AsyncAppsClient(client_wrapper=self._client_wrapper)
        return self._apps

    @property
    def audiences(self):
        if self._audiences is None:
            from .audiences.client import AsyncAudiencesClient

            self._audiences = AsyncAudiencesClient(client_wrapper=self._client_wrapper)
        return self._audiences

    @property
    def autocompletes(self):
        if self._autocompletes is None:
            from .autocompletes.client import AsyncAutocompletesClient

            self._autocompletes = AsyncAutocompletesClient(client_wrapper=self._client_wrapper)
        return self._autocompletes

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
    def industries(self):
        if self._industries is None:
            from .industries.client import AsyncIndustriesClient

            self._industries = AsyncIndustriesClient(client_wrapper=self._client_wrapper)
        return self._industries

    @property
    def markdown(self):
        if self._markdown is None:
            from .markdown.client import AsyncMarkdownClient

            self._markdown = AsyncMarkdownClient(client_wrapper=self._client_wrapper)
        return self._markdown

    @property
    def messages(self):
        if self._messages is None:
            from .messages.client import AsyncMessagesClient

            self._messages = AsyncMessagesClient(client_wrapper=self._client_wrapper)
        return self._messages

    @property
    def positions(self):
        if self._positions is None:
            from .positions.client import AsyncPositionsClient

            self._positions = AsyncPositionsClient(client_wrapper=self._client_wrapper)
        return self._positions

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient

            self._webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
