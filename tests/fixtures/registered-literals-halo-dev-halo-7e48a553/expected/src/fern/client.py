

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .attachment_v1alpha1console.client import AsyncAttachmentV1Alpha1ConsoleClient, AttachmentV1Alpha1ConsoleClient
    from .auth_provider_v1alpha1console.client import (
        AsyncAuthProviderV1Alpha1ConsoleClient,
        AuthProviderV1Alpha1ConsoleClient,
    )
    from .category_v1alpha1console.client import AsyncCategoryV1Alpha1ConsoleClient, CategoryV1Alpha1ConsoleClient
    from .comment_v1alpha1console.client import AsyncCommentV1Alpha1ConsoleClient, CommentV1Alpha1ConsoleClient
    from .indices_v1alpha1console.client import AsyncIndicesV1Alpha1ConsoleClient, IndicesV1Alpha1ConsoleClient
    from .menu_item_v1alpha1console.client import AsyncMenuItemV1Alpha1ConsoleClient, MenuItemV1Alpha1ConsoleClient
    from .menu_v1alpha1console.client import AsyncMenuV1Alpha1ConsoleClient, MenuV1Alpha1ConsoleClient
    from .migration_v1alpha1console.client import AsyncMigrationV1Alpha1ConsoleClient, MigrationV1Alpha1ConsoleClient
    from .notifier_v1alpha1console.client import AsyncNotifierV1Alpha1ConsoleClient, NotifierV1Alpha1ConsoleClient
    from .plugin_v1alpha1console.client import AsyncPluginV1Alpha1ConsoleClient, PluginV1Alpha1ConsoleClient
    from .policy_alpha1console.client import AsyncPolicyAlpha1ConsoleClient, PolicyAlpha1ConsoleClient
    from .post_v1alpha1console.client import AsyncPostV1Alpha1ConsoleClient, PostV1Alpha1ConsoleClient
    from .reply_v1alpha1console.client import AsyncReplyV1Alpha1ConsoleClient, ReplyV1Alpha1ConsoleClient
    from .single_page_v1alpha1console.client import (
        AsyncSinglePageV1Alpha1ConsoleClient,
        SinglePageV1Alpha1ConsoleClient,
    )
    from .system_config_v1alpha1console.client import (
        AsyncSystemConfigV1Alpha1ConsoleClient,
        SystemConfigV1Alpha1ConsoleClient,
    )
    from .system_v1alpha1console.client import AsyncSystemV1Alpha1ConsoleClient, SystemV1Alpha1ConsoleClient
    from .tag_v1alpha1console.client import AsyncTagV1Alpha1ConsoleClient, TagV1Alpha1ConsoleClient
    from .theme_v1alpha1console.client import AsyncThemeV1Alpha1ConsoleClient, ThemeV1Alpha1ConsoleClient
    from .ui_plugin_v1alpha1console.client import AsyncUiPluginV1Alpha1ConsoleClient, UiPluginV1Alpha1ConsoleClient
    from .user_v1alpha1console.client import AsyncUserV1Alpha1ConsoleClient, UserV1Alpha1ConsoleClient


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



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
        self._attachment_v1alpha1console: typing.Optional[AttachmentV1Alpha1ConsoleClient] = None
        self._auth_provider_v1alpha1console: typing.Optional[AuthProviderV1Alpha1ConsoleClient] = None
        self._category_v1alpha1console: typing.Optional[CategoryV1Alpha1ConsoleClient] = None
        self._comment_v1alpha1console: typing.Optional[CommentV1Alpha1ConsoleClient] = None
        self._indices_v1alpha1console: typing.Optional[IndicesV1Alpha1ConsoleClient] = None
        self._menu_item_v1alpha1console: typing.Optional[MenuItemV1Alpha1ConsoleClient] = None
        self._menu_v1alpha1console: typing.Optional[MenuV1Alpha1ConsoleClient] = None
        self._notifier_v1alpha1console: typing.Optional[NotifierV1Alpha1ConsoleClient] = None
        self._plugin_v1alpha1console: typing.Optional[PluginV1Alpha1ConsoleClient] = None
        self._post_v1alpha1console: typing.Optional[PostV1Alpha1ConsoleClient] = None
        self._reply_v1alpha1console: typing.Optional[ReplyV1Alpha1ConsoleClient] = None
        self._single_page_v1alpha1console: typing.Optional[SinglePageV1Alpha1ConsoleClient] = None
        self._system_v1alpha1console: typing.Optional[SystemV1Alpha1ConsoleClient] = None
        self._tag_v1alpha1console: typing.Optional[TagV1Alpha1ConsoleClient] = None
        self._theme_v1alpha1console: typing.Optional[ThemeV1Alpha1ConsoleClient] = None
        self._ui_plugin_v1alpha1console: typing.Optional[UiPluginV1Alpha1ConsoleClient] = None
        self._user_v1alpha1console: typing.Optional[UserV1Alpha1ConsoleClient] = None
        self._system_config_v1alpha1console: typing.Optional[SystemConfigV1Alpha1ConsoleClient] = None
        self._migration_v1alpha1console: typing.Optional[MigrationV1Alpha1ConsoleClient] = None
        self._policy_alpha1console: typing.Optional[PolicyAlpha1ConsoleClient] = None

    @property
    def attachment_v1alpha1console(self):
        if self._attachment_v1alpha1console is None:
            from .attachment_v1alpha1console.client import AttachmentV1Alpha1ConsoleClient

            self._attachment_v1alpha1console = AttachmentV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._attachment_v1alpha1console

    @property
    def auth_provider_v1alpha1console(self):
        if self._auth_provider_v1alpha1console is None:
            from .auth_provider_v1alpha1console.client import AuthProviderV1Alpha1ConsoleClient

            self._auth_provider_v1alpha1console = AuthProviderV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._auth_provider_v1alpha1console

    @property
    def category_v1alpha1console(self):
        if self._category_v1alpha1console is None:
            from .category_v1alpha1console.client import CategoryV1Alpha1ConsoleClient

            self._category_v1alpha1console = CategoryV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._category_v1alpha1console

    @property
    def comment_v1alpha1console(self):
        if self._comment_v1alpha1console is None:
            from .comment_v1alpha1console.client import CommentV1Alpha1ConsoleClient

            self._comment_v1alpha1console = CommentV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._comment_v1alpha1console

    @property
    def indices_v1alpha1console(self):
        if self._indices_v1alpha1console is None:
            from .indices_v1alpha1console.client import IndicesV1Alpha1ConsoleClient

            self._indices_v1alpha1console = IndicesV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._indices_v1alpha1console

    @property
    def menu_item_v1alpha1console(self):
        if self._menu_item_v1alpha1console is None:
            from .menu_item_v1alpha1console.client import MenuItemV1Alpha1ConsoleClient

            self._menu_item_v1alpha1console = MenuItemV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._menu_item_v1alpha1console

    @property
    def menu_v1alpha1console(self):
        if self._menu_v1alpha1console is None:
            from .menu_v1alpha1console.client import MenuV1Alpha1ConsoleClient

            self._menu_v1alpha1console = MenuV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._menu_v1alpha1console

    @property
    def notifier_v1alpha1console(self):
        if self._notifier_v1alpha1console is None:
            from .notifier_v1alpha1console.client import NotifierV1Alpha1ConsoleClient

            self._notifier_v1alpha1console = NotifierV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._notifier_v1alpha1console

    @property
    def plugin_v1alpha1console(self):
        if self._plugin_v1alpha1console is None:
            from .plugin_v1alpha1console.client import PluginV1Alpha1ConsoleClient

            self._plugin_v1alpha1console = PluginV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._plugin_v1alpha1console

    @property
    def post_v1alpha1console(self):
        if self._post_v1alpha1console is None:
            from .post_v1alpha1console.client import PostV1Alpha1ConsoleClient

            self._post_v1alpha1console = PostV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._post_v1alpha1console

    @property
    def reply_v1alpha1console(self):
        if self._reply_v1alpha1console is None:
            from .reply_v1alpha1console.client import ReplyV1Alpha1ConsoleClient

            self._reply_v1alpha1console = ReplyV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._reply_v1alpha1console

    @property
    def single_page_v1alpha1console(self):
        if self._single_page_v1alpha1console is None:
            from .single_page_v1alpha1console.client import SinglePageV1Alpha1ConsoleClient

            self._single_page_v1alpha1console = SinglePageV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._single_page_v1alpha1console

    @property
    def system_v1alpha1console(self):
        if self._system_v1alpha1console is None:
            from .system_v1alpha1console.client import SystemV1Alpha1ConsoleClient

            self._system_v1alpha1console = SystemV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._system_v1alpha1console

    @property
    def tag_v1alpha1console(self):
        if self._tag_v1alpha1console is None:
            from .tag_v1alpha1console.client import TagV1Alpha1ConsoleClient

            self._tag_v1alpha1console = TagV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._tag_v1alpha1console

    @property
    def theme_v1alpha1console(self):
        if self._theme_v1alpha1console is None:
            from .theme_v1alpha1console.client import ThemeV1Alpha1ConsoleClient

            self._theme_v1alpha1console = ThemeV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._theme_v1alpha1console

    @property
    def ui_plugin_v1alpha1console(self):
        if self._ui_plugin_v1alpha1console is None:
            from .ui_plugin_v1alpha1console.client import UiPluginV1Alpha1ConsoleClient

            self._ui_plugin_v1alpha1console = UiPluginV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._ui_plugin_v1alpha1console

    @property
    def user_v1alpha1console(self):
        if self._user_v1alpha1console is None:
            from .user_v1alpha1console.client import UserV1Alpha1ConsoleClient

            self._user_v1alpha1console = UserV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._user_v1alpha1console

    @property
    def system_config_v1alpha1console(self):
        if self._system_config_v1alpha1console is None:
            from .system_config_v1alpha1console.client import SystemConfigV1Alpha1ConsoleClient

            self._system_config_v1alpha1console = SystemConfigV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._system_config_v1alpha1console

    @property
    def migration_v1alpha1console(self):
        if self._migration_v1alpha1console is None:
            from .migration_v1alpha1console.client import MigrationV1Alpha1ConsoleClient

            self._migration_v1alpha1console = MigrationV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._migration_v1alpha1console

    @property
    def policy_alpha1console(self):
        if self._policy_alpha1console is None:
            from .policy_alpha1console.client import PolicyAlpha1ConsoleClient

            self._policy_alpha1console = PolicyAlpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._policy_alpha1console


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



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
        self._attachment_v1alpha1console: typing.Optional[AsyncAttachmentV1Alpha1ConsoleClient] = None
        self._auth_provider_v1alpha1console: typing.Optional[AsyncAuthProviderV1Alpha1ConsoleClient] = None
        self._category_v1alpha1console: typing.Optional[AsyncCategoryV1Alpha1ConsoleClient] = None
        self._comment_v1alpha1console: typing.Optional[AsyncCommentV1Alpha1ConsoleClient] = None
        self._indices_v1alpha1console: typing.Optional[AsyncIndicesV1Alpha1ConsoleClient] = None
        self._menu_item_v1alpha1console: typing.Optional[AsyncMenuItemV1Alpha1ConsoleClient] = None
        self._menu_v1alpha1console: typing.Optional[AsyncMenuV1Alpha1ConsoleClient] = None
        self._notifier_v1alpha1console: typing.Optional[AsyncNotifierV1Alpha1ConsoleClient] = None
        self._plugin_v1alpha1console: typing.Optional[AsyncPluginV1Alpha1ConsoleClient] = None
        self._post_v1alpha1console: typing.Optional[AsyncPostV1Alpha1ConsoleClient] = None
        self._reply_v1alpha1console: typing.Optional[AsyncReplyV1Alpha1ConsoleClient] = None
        self._single_page_v1alpha1console: typing.Optional[AsyncSinglePageV1Alpha1ConsoleClient] = None
        self._system_v1alpha1console: typing.Optional[AsyncSystemV1Alpha1ConsoleClient] = None
        self._tag_v1alpha1console: typing.Optional[AsyncTagV1Alpha1ConsoleClient] = None
        self._theme_v1alpha1console: typing.Optional[AsyncThemeV1Alpha1ConsoleClient] = None
        self._ui_plugin_v1alpha1console: typing.Optional[AsyncUiPluginV1Alpha1ConsoleClient] = None
        self._user_v1alpha1console: typing.Optional[AsyncUserV1Alpha1ConsoleClient] = None
        self._system_config_v1alpha1console: typing.Optional[AsyncSystemConfigV1Alpha1ConsoleClient] = None
        self._migration_v1alpha1console: typing.Optional[AsyncMigrationV1Alpha1ConsoleClient] = None
        self._policy_alpha1console: typing.Optional[AsyncPolicyAlpha1ConsoleClient] = None

    @property
    def attachment_v1alpha1console(self):
        if self._attachment_v1alpha1console is None:
            from .attachment_v1alpha1console.client import AsyncAttachmentV1Alpha1ConsoleClient

            self._attachment_v1alpha1console = AsyncAttachmentV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._attachment_v1alpha1console

    @property
    def auth_provider_v1alpha1console(self):
        if self._auth_provider_v1alpha1console is None:
            from .auth_provider_v1alpha1console.client import AsyncAuthProviderV1Alpha1ConsoleClient

            self._auth_provider_v1alpha1console = AsyncAuthProviderV1Alpha1ConsoleClient(
                client_wrapper=self._client_wrapper
            )
        return self._auth_provider_v1alpha1console

    @property
    def category_v1alpha1console(self):
        if self._category_v1alpha1console is None:
            from .category_v1alpha1console.client import AsyncCategoryV1Alpha1ConsoleClient

            self._category_v1alpha1console = AsyncCategoryV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._category_v1alpha1console

    @property
    def comment_v1alpha1console(self):
        if self._comment_v1alpha1console is None:
            from .comment_v1alpha1console.client import AsyncCommentV1Alpha1ConsoleClient

            self._comment_v1alpha1console = AsyncCommentV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._comment_v1alpha1console

    @property
    def indices_v1alpha1console(self):
        if self._indices_v1alpha1console is None:
            from .indices_v1alpha1console.client import AsyncIndicesV1Alpha1ConsoleClient

            self._indices_v1alpha1console = AsyncIndicesV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._indices_v1alpha1console

    @property
    def menu_item_v1alpha1console(self):
        if self._menu_item_v1alpha1console is None:
            from .menu_item_v1alpha1console.client import AsyncMenuItemV1Alpha1ConsoleClient

            self._menu_item_v1alpha1console = AsyncMenuItemV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._menu_item_v1alpha1console

    @property
    def menu_v1alpha1console(self):
        if self._menu_v1alpha1console is None:
            from .menu_v1alpha1console.client import AsyncMenuV1Alpha1ConsoleClient

            self._menu_v1alpha1console = AsyncMenuV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._menu_v1alpha1console

    @property
    def notifier_v1alpha1console(self):
        if self._notifier_v1alpha1console is None:
            from .notifier_v1alpha1console.client import AsyncNotifierV1Alpha1ConsoleClient

            self._notifier_v1alpha1console = AsyncNotifierV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._notifier_v1alpha1console

    @property
    def plugin_v1alpha1console(self):
        if self._plugin_v1alpha1console is None:
            from .plugin_v1alpha1console.client import AsyncPluginV1Alpha1ConsoleClient

            self._plugin_v1alpha1console = AsyncPluginV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._plugin_v1alpha1console

    @property
    def post_v1alpha1console(self):
        if self._post_v1alpha1console is None:
            from .post_v1alpha1console.client import AsyncPostV1Alpha1ConsoleClient

            self._post_v1alpha1console = AsyncPostV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._post_v1alpha1console

    @property
    def reply_v1alpha1console(self):
        if self._reply_v1alpha1console is None:
            from .reply_v1alpha1console.client import AsyncReplyV1Alpha1ConsoleClient

            self._reply_v1alpha1console = AsyncReplyV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._reply_v1alpha1console

    @property
    def single_page_v1alpha1console(self):
        if self._single_page_v1alpha1console is None:
            from .single_page_v1alpha1console.client import AsyncSinglePageV1Alpha1ConsoleClient

            self._single_page_v1alpha1console = AsyncSinglePageV1Alpha1ConsoleClient(
                client_wrapper=self._client_wrapper
            )
        return self._single_page_v1alpha1console

    @property
    def system_v1alpha1console(self):
        if self._system_v1alpha1console is None:
            from .system_v1alpha1console.client import AsyncSystemV1Alpha1ConsoleClient

            self._system_v1alpha1console = AsyncSystemV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._system_v1alpha1console

    @property
    def tag_v1alpha1console(self):
        if self._tag_v1alpha1console is None:
            from .tag_v1alpha1console.client import AsyncTagV1Alpha1ConsoleClient

            self._tag_v1alpha1console = AsyncTagV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._tag_v1alpha1console

    @property
    def theme_v1alpha1console(self):
        if self._theme_v1alpha1console is None:
            from .theme_v1alpha1console.client import AsyncThemeV1Alpha1ConsoleClient

            self._theme_v1alpha1console = AsyncThemeV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._theme_v1alpha1console

    @property
    def ui_plugin_v1alpha1console(self):
        if self._ui_plugin_v1alpha1console is None:
            from .ui_plugin_v1alpha1console.client import AsyncUiPluginV1Alpha1ConsoleClient

            self._ui_plugin_v1alpha1console = AsyncUiPluginV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._ui_plugin_v1alpha1console

    @property
    def user_v1alpha1console(self):
        if self._user_v1alpha1console is None:
            from .user_v1alpha1console.client import AsyncUserV1Alpha1ConsoleClient

            self._user_v1alpha1console = AsyncUserV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._user_v1alpha1console

    @property
    def system_config_v1alpha1console(self):
        if self._system_config_v1alpha1console is None:
            from .system_config_v1alpha1console.client import AsyncSystemConfigV1Alpha1ConsoleClient

            self._system_config_v1alpha1console = AsyncSystemConfigV1Alpha1ConsoleClient(
                client_wrapper=self._client_wrapper
            )
        return self._system_config_v1alpha1console

    @property
    def migration_v1alpha1console(self):
        if self._migration_v1alpha1console is None:
            from .migration_v1alpha1console.client import AsyncMigrationV1Alpha1ConsoleClient

            self._migration_v1alpha1console = AsyncMigrationV1Alpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._migration_v1alpha1console

    @property
    def policy_alpha1console(self):
        if self._policy_alpha1console is None:
            from .policy_alpha1console.client import AsyncPolicyAlpha1ConsoleClient

            self._policy_alpha1console = AsyncPolicyAlpha1ConsoleClient(client_wrapper=self._client_wrapper)
        return self._policy_alpha1console


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
