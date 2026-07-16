

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .attributes.client import AsyncAttributesClient, AttributesClient
    from .calendars.client import AsyncCalendarsClient, CalendarsClient
    from .commands.client import AsyncCommandsClient, CommandsClient
    from .devices.client import AsyncDevicesClient, DevicesClient
    from .drivers.client import AsyncDriversClient, DriversClient
    from .events.client import AsyncEventsClient, EventsClient
    from .geofences.client import AsyncGeofencesClient, GeofencesClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .maintenance.client import AsyncMaintenanceClient, MaintenanceClient
    from .notifications.client import AsyncNotificationsClient, NotificationsClient
    from .permissions.client import AsyncPermissionsClient, PermissionsClient
    from .positions.client import AsyncPositionsClient, PositionsClient
    from .reports.client import AsyncReportsClient, ReportsClient
    from .server.client import AsyncServerClient, ServerClient
    from .session.client import AsyncSessionClient, SessionClient
    from .statistics.client import AsyncStatisticsClient, StatisticsClient
    from .users.client import AsyncUsersClient, UsersClient


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

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
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
        )
        self._attributes: typing.Optional[AttributesClient] = None
        self._calendars: typing.Optional[CalendarsClient] = None
        self._commands: typing.Optional[CommandsClient] = None
        self._devices: typing.Optional[DevicesClient] = None
        self._drivers: typing.Optional[DriversClient] = None
        self._events: typing.Optional[EventsClient] = None
        self._geofences: typing.Optional[GeofencesClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._maintenance: typing.Optional[MaintenanceClient] = None
        self._notifications: typing.Optional[NotificationsClient] = None
        self._permissions: typing.Optional[PermissionsClient] = None
        self._positions: typing.Optional[PositionsClient] = None
        self._reports: typing.Optional[ReportsClient] = None
        self._server: typing.Optional[ServerClient] = None
        self._session: typing.Optional[SessionClient] = None
        self._statistics: typing.Optional[StatisticsClient] = None
        self._users: typing.Optional[UsersClient] = None

    @property
    def attributes(self):
        if self._attributes is None:
            from .attributes.client import AttributesClient

            self._attributes = AttributesClient(client_wrapper=self._client_wrapper)
        return self._attributes

    @property
    def calendars(self):
        if self._calendars is None:
            from .calendars.client import CalendarsClient

            self._calendars = CalendarsClient(client_wrapper=self._client_wrapper)
        return self._calendars

    @property
    def commands(self):
        if self._commands is None:
            from .commands.client import CommandsClient

            self._commands = CommandsClient(client_wrapper=self._client_wrapper)
        return self._commands

    @property
    def devices(self):
        if self._devices is None:
            from .devices.client import DevicesClient

            self._devices = DevicesClient(client_wrapper=self._client_wrapper)
        return self._devices

    @property
    def drivers(self):
        if self._drivers is None:
            from .drivers.client import DriversClient

            self._drivers = DriversClient(client_wrapper=self._client_wrapper)
        return self._drivers

    @property
    def events(self):
        if self._events is None:
            from .events.client import EventsClient

            self._events = EventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def geofences(self):
        if self._geofences is None:
            from .geofences.client import GeofencesClient

            self._geofences = GeofencesClient(client_wrapper=self._client_wrapper)
        return self._geofences

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import MaintenanceClient

            self._maintenance = MaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import NotificationsClient

            self._notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import PermissionsClient

            self._permissions = PermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def positions(self):
        if self._positions is None:
            from .positions.client import PositionsClient

            self._positions = PositionsClient(client_wrapper=self._client_wrapper)
        return self._positions

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import ReportsClient

            self._reports = ReportsClient(client_wrapper=self._client_wrapper)
        return self._reports

    @property
    def server(self):
        if self._server is None:
            from .server.client import ServerClient

            self._server = ServerClient(client_wrapper=self._client_wrapper)
        return self._server

    @property
    def session(self):
        if self._session is None:
            from .session.client import SessionClient

            self._session = SessionClient(client_wrapper=self._client_wrapper)
        return self._session

    @property
    def statistics(self):
        if self._statistics is None:
            from .statistics.client import StatisticsClient

            self._statistics = StatisticsClient(client_wrapper=self._client_wrapper)
        return self._statistics

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users


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

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            username=username,
            password=password,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._attributes: typing.Optional[AsyncAttributesClient] = None
        self._calendars: typing.Optional[AsyncCalendarsClient] = None
        self._commands: typing.Optional[AsyncCommandsClient] = None
        self._devices: typing.Optional[AsyncDevicesClient] = None
        self._drivers: typing.Optional[AsyncDriversClient] = None
        self._events: typing.Optional[AsyncEventsClient] = None
        self._geofences: typing.Optional[AsyncGeofencesClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._maintenance: typing.Optional[AsyncMaintenanceClient] = None
        self._notifications: typing.Optional[AsyncNotificationsClient] = None
        self._permissions: typing.Optional[AsyncPermissionsClient] = None
        self._positions: typing.Optional[AsyncPositionsClient] = None
        self._reports: typing.Optional[AsyncReportsClient] = None
        self._server: typing.Optional[AsyncServerClient] = None
        self._session: typing.Optional[AsyncSessionClient] = None
        self._statistics: typing.Optional[AsyncStatisticsClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None

    @property
    def attributes(self):
        if self._attributes is None:
            from .attributes.client import AsyncAttributesClient

            self._attributes = AsyncAttributesClient(client_wrapper=self._client_wrapper)
        return self._attributes

    @property
    def calendars(self):
        if self._calendars is None:
            from .calendars.client import AsyncCalendarsClient

            self._calendars = AsyncCalendarsClient(client_wrapper=self._client_wrapper)
        return self._calendars

    @property
    def commands(self):
        if self._commands is None:
            from .commands.client import AsyncCommandsClient

            self._commands = AsyncCommandsClient(client_wrapper=self._client_wrapper)
        return self._commands

    @property
    def devices(self):
        if self._devices is None:
            from .devices.client import AsyncDevicesClient

            self._devices = AsyncDevicesClient(client_wrapper=self._client_wrapper)
        return self._devices

    @property
    def drivers(self):
        if self._drivers is None:
            from .drivers.client import AsyncDriversClient

            self._drivers = AsyncDriversClient(client_wrapper=self._client_wrapper)
        return self._drivers

    @property
    def events(self):
        if self._events is None:
            from .events.client import AsyncEventsClient

            self._events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def geofences(self):
        if self._geofences is None:
            from .geofences.client import AsyncGeofencesClient

            self._geofences = AsyncGeofencesClient(client_wrapper=self._client_wrapper)
        return self._geofences

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import AsyncMaintenanceClient

            self._maintenance = AsyncMaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import AsyncNotificationsClient

            self._notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import AsyncPermissionsClient

            self._permissions = AsyncPermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def positions(self):
        if self._positions is None:
            from .positions.client import AsyncPositionsClient

            self._positions = AsyncPositionsClient(client_wrapper=self._client_wrapper)
        return self._positions

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import AsyncReportsClient

            self._reports = AsyncReportsClient(client_wrapper=self._client_wrapper)
        return self._reports

    @property
    def server(self):
        if self._server is None:
            from .server.client import AsyncServerClient

            self._server = AsyncServerClient(client_wrapper=self._client_wrapper)
        return self._server

    @property
    def session(self):
        if self._session is None:
            from .session.client import AsyncSessionClient

            self._session = AsyncSessionClient(client_wrapper=self._client_wrapper)
        return self._session

    @property
    def statistics(self):
        if self._statistics is None:
            from .statistics.client import AsyncStatisticsClient

            self._statistics = AsyncStatisticsClient(client_wrapper=self._client_wrapper)
        return self._statistics

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
