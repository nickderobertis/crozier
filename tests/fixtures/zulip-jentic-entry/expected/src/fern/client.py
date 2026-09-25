

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .authentication.client import AsyncAuthenticationClient, AuthenticationClient
    from .channels.client import AsyncChannelsClient, ChannelsClient
    from .drafts.client import AsyncDraftsClient, DraftsClient
    from .invites.client import AsyncInvitesClient, InvitesClient
    from .messages.client import AsyncMessagesClient, MessagesClient
    from .mobile.client import AsyncMobileClient, MobileClient
    from .navigation_views.client import AsyncNavigationViewsClient, NavigationViewsClient
    from .real_time_events.client import AsyncRealTimeEventsClient, RealTimeEventsClient
    from .reminders.client import AsyncRemindersClient, RemindersClient
    from .scheduled_messages.client import AsyncScheduledMessagesClient, ScheduledMessagesClient
    from .server_and_organizations.client import AsyncServerAndOrganizationsClient, ServerAndOrganizationsClient
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



    subdomain : typing.Optional[str]
        Server URL variable for 'subdomain'. Defaults to 'example'.

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
        subdomain: typing.Optional[str] = None,
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
        if subdomain is not None:
            _subdomain = subdomain if subdomain is not None else "example"
            base_url = "https://{subdomain}.zulipchat.com/api/v1".format(subdomain=_subdomain)
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
        self._authentication: typing.Optional[AuthenticationClient] = None
        self._real_time_events: typing.Optional[RealTimeEventsClient] = None
        self._channels: typing.Optional[ChannelsClient] = None
        self._messages: typing.Optional[MessagesClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._drafts: typing.Optional[DraftsClient] = None
        self._navigation_views: typing.Optional[NavigationViewsClient] = None
        self._reminders: typing.Optional[RemindersClient] = None
        self._scheduled_messages: typing.Optional[ScheduledMessagesClient] = None
        self._mobile: typing.Optional[MobileClient] = None
        self._server_and_organizations: typing.Optional[ServerAndOrganizationsClient] = None
        self._invites: typing.Optional[InvitesClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AuthenticationClient

            self._authentication = AuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def real_time_events(self):
        if self._real_time_events is None:
            from .real_time_events.client import RealTimeEventsClient

            self._real_time_events = RealTimeEventsClient(client_wrapper=self._client_wrapper)
        return self._real_time_events

    @property
    def channels(self):
        if self._channels is None:
            from .channels.client import ChannelsClient

            self._channels = ChannelsClient(client_wrapper=self._client_wrapper)
        return self._channels

    @property
    def messages(self):
        if self._messages is None:
            from .messages.client import MessagesClient

            self._messages = MessagesClient(client_wrapper=self._client_wrapper)
        return self._messages

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def drafts(self):
        if self._drafts is None:
            from .drafts.client import DraftsClient

            self._drafts = DraftsClient(client_wrapper=self._client_wrapper)
        return self._drafts

    @property
    def navigation_views(self):
        if self._navigation_views is None:
            from .navigation_views.client import NavigationViewsClient

            self._navigation_views = NavigationViewsClient(client_wrapper=self._client_wrapper)
        return self._navigation_views

    @property
    def reminders(self):
        if self._reminders is None:
            from .reminders.client import RemindersClient

            self._reminders = RemindersClient(client_wrapper=self._client_wrapper)
        return self._reminders

    @property
    def scheduled_messages(self):
        if self._scheduled_messages is None:
            from .scheduled_messages.client import ScheduledMessagesClient

            self._scheduled_messages = ScheduledMessagesClient(client_wrapper=self._client_wrapper)
        return self._scheduled_messages

    @property
    def mobile(self):
        if self._mobile is None:
            from .mobile.client import MobileClient

            self._mobile = MobileClient(client_wrapper=self._client_wrapper)
        return self._mobile

    @property
    def server_and_organizations(self):
        if self._server_and_organizations is None:
            from .server_and_organizations.client import ServerAndOrganizationsClient

            self._server_and_organizations = ServerAndOrganizationsClient(client_wrapper=self._client_wrapper)
        return self._server_and_organizations

    @property
    def invites(self):
        if self._invites is None:
            from .invites.client import InvitesClient

            self._invites = InvitesClient(client_wrapper=self._client_wrapper)
        return self._invites

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



    subdomain : typing.Optional[str]
        Server URL variable for 'subdomain'. Defaults to 'example'.

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
        subdomain: typing.Optional[str] = None,
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
        if subdomain is not None:
            _subdomain = subdomain if subdomain is not None else "example"
            base_url = "https://{subdomain}.zulipchat.com/api/v1".format(subdomain=_subdomain)
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
        self._authentication: typing.Optional[AsyncAuthenticationClient] = None
        self._real_time_events: typing.Optional[AsyncRealTimeEventsClient] = None
        self._channels: typing.Optional[AsyncChannelsClient] = None
        self._messages: typing.Optional[AsyncMessagesClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._drafts: typing.Optional[AsyncDraftsClient] = None
        self._navigation_views: typing.Optional[AsyncNavigationViewsClient] = None
        self._reminders: typing.Optional[AsyncRemindersClient] = None
        self._scheduled_messages: typing.Optional[AsyncScheduledMessagesClient] = None
        self._mobile: typing.Optional[AsyncMobileClient] = None
        self._server_and_organizations: typing.Optional[AsyncServerAndOrganizationsClient] = None
        self._invites: typing.Optional[AsyncInvitesClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AsyncAuthenticationClient

            self._authentication = AsyncAuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def real_time_events(self):
        if self._real_time_events is None:
            from .real_time_events.client import AsyncRealTimeEventsClient

            self._real_time_events = AsyncRealTimeEventsClient(client_wrapper=self._client_wrapper)
        return self._real_time_events

    @property
    def channels(self):
        if self._channels is None:
            from .channels.client import AsyncChannelsClient

            self._channels = AsyncChannelsClient(client_wrapper=self._client_wrapper)
        return self._channels

    @property
    def messages(self):
        if self._messages is None:
            from .messages.client import AsyncMessagesClient

            self._messages = AsyncMessagesClient(client_wrapper=self._client_wrapper)
        return self._messages

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def drafts(self):
        if self._drafts is None:
            from .drafts.client import AsyncDraftsClient

            self._drafts = AsyncDraftsClient(client_wrapper=self._client_wrapper)
        return self._drafts

    @property
    def navigation_views(self):
        if self._navigation_views is None:
            from .navigation_views.client import AsyncNavigationViewsClient

            self._navigation_views = AsyncNavigationViewsClient(client_wrapper=self._client_wrapper)
        return self._navigation_views

    @property
    def reminders(self):
        if self._reminders is None:
            from .reminders.client import AsyncRemindersClient

            self._reminders = AsyncRemindersClient(client_wrapper=self._client_wrapper)
        return self._reminders

    @property
    def scheduled_messages(self):
        if self._scheduled_messages is None:
            from .scheduled_messages.client import AsyncScheduledMessagesClient

            self._scheduled_messages = AsyncScheduledMessagesClient(client_wrapper=self._client_wrapper)
        return self._scheduled_messages

    @property
    def mobile(self):
        if self._mobile is None:
            from .mobile.client import AsyncMobileClient

            self._mobile = AsyncMobileClient(client_wrapper=self._client_wrapper)
        return self._mobile

    @property
    def server_and_organizations(self):
        if self._server_and_organizations is None:
            from .server_and_organizations.client import AsyncServerAndOrganizationsClient

            self._server_and_organizations = AsyncServerAndOrganizationsClient(client_wrapper=self._client_wrapper)
        return self._server_and_organizations

    @property
    def invites(self):
        if self._invites is None:
            from .invites.client import AsyncInvitesClient

            self._invites = AsyncInvitesClient(client_wrapper=self._client_wrapper)
        return self._invites

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
