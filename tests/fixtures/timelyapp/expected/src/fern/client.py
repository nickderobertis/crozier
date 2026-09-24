

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .bulk_operations.client import AsyncBulkOperationsClient, BulkOperationsClient
    from .clients.client import AsyncClientsClient, ClientsClient
    from .day_properties.client import AsyncDayPropertiesClient, DayPropertiesClient
    from .event_states.client import AsyncEventStatesClient, EventStatesClient
    from .event_timers.client import AsyncEventTimersClient, EventTimersClient
    from .events.client import AsyncEventsClient, EventsClient
    from .forecasts_tasks.client import AsyncForecastsTasksClient, ForecastsTasksClient
    from .o_auth.client import AsyncOAuthClient, OAuthClient
    from .permissions.client import AsyncPermissionsClient, PermissionsClient
    from .projects.client import AsyncProjectsClient, ProjectsClient
    from .reports.client import AsyncReportsClient, ReportsClient
    from .roles.client import AsyncRolesClient, RolesClient
    from .tags.client import AsyncTagsClient, TagsClient
    from .teams.client import AsyncTeamsClient, TeamsClient
    from .user_capacities.client import AsyncUserCapacitiesClient, UserCapacitiesClient
    from .users.client import AsyncUsersClient, UsersClient
    from .webhook_events.client import AsyncWebhookEventsClient, WebhookEventsClient
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
        self._webhook_events: typing.Optional[WebhookEventsClient] = None
        self._bulk_operations: typing.Optional[BulkOperationsClient] = None
        self._clients: typing.Optional[ClientsClient] = None
        self._day_properties: typing.Optional[DayPropertiesClient] = None
        self._forecasts_tasks: typing.Optional[ForecastsTasksClient] = None
        self._events: typing.Optional[EventsClient] = None
        self._event_timers: typing.Optional[EventTimersClient] = None
        self._event_states: typing.Optional[EventStatesClient] = None
        self._tags: typing.Optional[TagsClient] = None
        self._o_auth: typing.Optional[OAuthClient] = None
        self._permissions: typing.Optional[PermissionsClient] = None
        self._projects: typing.Optional[ProjectsClient] = None
        self._reports: typing.Optional[ReportsClient] = None
        self._roles: typing.Optional[RolesClient] = None
        self._teams: typing.Optional[TeamsClient] = None
        self._user_capacities: typing.Optional[UserCapacitiesClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None

    @property
    def webhook_events(self):
        if self._webhook_events is None:
            from .webhook_events.client import WebhookEventsClient

            self._webhook_events = WebhookEventsClient(client_wrapper=self._client_wrapper)
        return self._webhook_events

    @property
    def bulk_operations(self):
        if self._bulk_operations is None:
            from .bulk_operations.client import BulkOperationsClient

            self._bulk_operations = BulkOperationsClient(client_wrapper=self._client_wrapper)
        return self._bulk_operations

    @property
    def clients(self):
        if self._clients is None:
            from .clients.client import ClientsClient

            self._clients = ClientsClient(client_wrapper=self._client_wrapper)
        return self._clients

    @property
    def day_properties(self):
        if self._day_properties is None:
            from .day_properties.client import DayPropertiesClient

            self._day_properties = DayPropertiesClient(client_wrapper=self._client_wrapper)
        return self._day_properties

    @property
    def forecasts_tasks(self):
        if self._forecasts_tasks is None:
            from .forecasts_tasks.client import ForecastsTasksClient

            self._forecasts_tasks = ForecastsTasksClient(client_wrapper=self._client_wrapper)
        return self._forecasts_tasks

    @property
    def events(self):
        if self._events is None:
            from .events.client import EventsClient

            self._events = EventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def event_timers(self):
        if self._event_timers is None:
            from .event_timers.client import EventTimersClient

            self._event_timers = EventTimersClient(client_wrapper=self._client_wrapper)
        return self._event_timers

    @property
    def event_states(self):
        if self._event_states is None:
            from .event_states.client import EventStatesClient

            self._event_states = EventStatesClient(client_wrapper=self._client_wrapper)
        return self._event_states

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import TagsClient

            self._tags = TagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def o_auth(self):
        if self._o_auth is None:
            from .o_auth.client import OAuthClient

            self._o_auth = OAuthClient(client_wrapper=self._client_wrapper)
        return self._o_auth

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import PermissionsClient

            self._permissions = PermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import ProjectsClient

            self._projects = ProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import ReportsClient

            self._reports = ReportsClient(client_wrapper=self._client_wrapper)
        return self._reports

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import RolesClient

            self._roles = RolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def teams(self):
        if self._teams is None:
            from .teams.client import TeamsClient

            self._teams = TeamsClient(client_wrapper=self._client_wrapper)
        return self._teams

    @property
    def user_capacities(self):
        if self._user_capacities is None:
            from .user_capacities.client import UserCapacitiesClient

            self._user_capacities = UserCapacitiesClient(client_wrapper=self._client_wrapper)
        return self._user_capacities

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
        self._webhook_events: typing.Optional[AsyncWebhookEventsClient] = None
        self._bulk_operations: typing.Optional[AsyncBulkOperationsClient] = None
        self._clients: typing.Optional[AsyncClientsClient] = None
        self._day_properties: typing.Optional[AsyncDayPropertiesClient] = None
        self._forecasts_tasks: typing.Optional[AsyncForecastsTasksClient] = None
        self._events: typing.Optional[AsyncEventsClient] = None
        self._event_timers: typing.Optional[AsyncEventTimersClient] = None
        self._event_states: typing.Optional[AsyncEventStatesClient] = None
        self._tags: typing.Optional[AsyncTagsClient] = None
        self._o_auth: typing.Optional[AsyncOAuthClient] = None
        self._permissions: typing.Optional[AsyncPermissionsClient] = None
        self._projects: typing.Optional[AsyncProjectsClient] = None
        self._reports: typing.Optional[AsyncReportsClient] = None
        self._roles: typing.Optional[AsyncRolesClient] = None
        self._teams: typing.Optional[AsyncTeamsClient] = None
        self._user_capacities: typing.Optional[AsyncUserCapacitiesClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None

    @property
    def webhook_events(self):
        if self._webhook_events is None:
            from .webhook_events.client import AsyncWebhookEventsClient

            self._webhook_events = AsyncWebhookEventsClient(client_wrapper=self._client_wrapper)
        return self._webhook_events

    @property
    def bulk_operations(self):
        if self._bulk_operations is None:
            from .bulk_operations.client import AsyncBulkOperationsClient

            self._bulk_operations = AsyncBulkOperationsClient(client_wrapper=self._client_wrapper)
        return self._bulk_operations

    @property
    def clients(self):
        if self._clients is None:
            from .clients.client import AsyncClientsClient

            self._clients = AsyncClientsClient(client_wrapper=self._client_wrapper)
        return self._clients

    @property
    def day_properties(self):
        if self._day_properties is None:
            from .day_properties.client import AsyncDayPropertiesClient

            self._day_properties = AsyncDayPropertiesClient(client_wrapper=self._client_wrapper)
        return self._day_properties

    @property
    def forecasts_tasks(self):
        if self._forecasts_tasks is None:
            from .forecasts_tasks.client import AsyncForecastsTasksClient

            self._forecasts_tasks = AsyncForecastsTasksClient(client_wrapper=self._client_wrapper)
        return self._forecasts_tasks

    @property
    def events(self):
        if self._events is None:
            from .events.client import AsyncEventsClient

            self._events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def event_timers(self):
        if self._event_timers is None:
            from .event_timers.client import AsyncEventTimersClient

            self._event_timers = AsyncEventTimersClient(client_wrapper=self._client_wrapper)
        return self._event_timers

    @property
    def event_states(self):
        if self._event_states is None:
            from .event_states.client import AsyncEventStatesClient

            self._event_states = AsyncEventStatesClient(client_wrapper=self._client_wrapper)
        return self._event_states

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import AsyncTagsClient

            self._tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def o_auth(self):
        if self._o_auth is None:
            from .o_auth.client import AsyncOAuthClient

            self._o_auth = AsyncOAuthClient(client_wrapper=self._client_wrapper)
        return self._o_auth

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import AsyncPermissionsClient

            self._permissions = AsyncPermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            self._projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import AsyncReportsClient

            self._reports = AsyncReportsClient(client_wrapper=self._client_wrapper)
        return self._reports

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import AsyncRolesClient

            self._roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def teams(self):
        if self._teams is None:
            from .teams.client import AsyncTeamsClient

            self._teams = AsyncTeamsClient(client_wrapper=self._client_wrapper)
        return self._teams

    @property
    def user_capacities(self):
        if self._user_capacities is None:
            from .user_capacities.client import AsyncUserCapacitiesClient

            self._user_capacities = AsyncUserCapacitiesClient(client_wrapper=self._client_wrapper)
        return self._user_capacities

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
