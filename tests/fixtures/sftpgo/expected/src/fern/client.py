

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .admins.client import AdminsClient, AsyncAdminsClient
    from .api_keys.client import ApiKeysClient, AsyncApiKeysClient
    from .connections.client import AsyncConnectionsClient, ConnectionsClient
    from .data_retention.client import AsyncDataRetentionClient, DataRetentionClient
    from .defender.client import AsyncDefenderClient, DefenderClient
    from .event_manager.client import AsyncEventManagerClient, EventManagerClient
    from .events.client import AsyncEventsClient, EventsClient
    from .folders.client import AsyncFoldersClient, FoldersClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .healthcheck.client import AsyncHealthcheckClient, HealthcheckClient
    from .ip_lists.client import AsyncIpListsClient, IpListsClient
    from .maintenance.client import AsyncMaintenanceClient, MaintenanceClient
    from .public_shares.client import AsyncPublicSharesClient, PublicSharesClient
    from .quota.client import AsyncQuotaClient, QuotaClient
    from .roles.client import AsyncRolesClient, RolesClient
    from .token.client import AsyncTokenClient, TokenClient
    from .user_ap_is.client import AsyncUserApIsClient, UserApIsClient
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



    sftpgo_api_key : str
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
        sftpgo_api_key="YOUR_SFTPGO_API_KEY",
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        sftpgo_api_key: str,
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
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            sftpgo_api_key=sftpgo_api_key,
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
        self._healthcheck: typing.Optional[HealthcheckClient] = None
        self._public_shares: typing.Optional[PublicSharesClient] = None
        self._token: typing.Optional[TokenClient] = None
        self._maintenance: typing.Optional[MaintenanceClient] = None
        self._admins: typing.Optional[AdminsClient] = None
        self._connections: typing.Optional[ConnectionsClient] = None
        self._ip_lists: typing.Optional[IpListsClient] = None
        self._defender: typing.Optional[DefenderClient] = None
        self._data_retention: typing.Optional[DataRetentionClient] = None
        self._quota: typing.Optional[QuotaClient] = None
        self._folders: typing.Optional[FoldersClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._roles: typing.Optional[RolesClient] = None
        self._event_manager: typing.Optional[EventManagerClient] = None
        self._events: typing.Optional[EventsClient] = None
        self._api_keys: typing.Optional[ApiKeysClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._user_ap_is: typing.Optional[UserApIsClient] = None

    @property
    def healthcheck(self):
        if self._healthcheck is None:
            from .healthcheck.client import HealthcheckClient

            self._healthcheck = HealthcheckClient(client_wrapper=self._client_wrapper)
        return self._healthcheck

    @property
    def public_shares(self):
        if self._public_shares is None:
            from .public_shares.client import PublicSharesClient

            self._public_shares = PublicSharesClient(client_wrapper=self._client_wrapper)
        return self._public_shares

    @property
    def token(self):
        if self._token is None:
            from .token.client import TokenClient

            self._token = TokenClient(client_wrapper=self._client_wrapper)
        return self._token

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import MaintenanceClient

            self._maintenance = MaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance

    @property
    def admins(self):
        if self._admins is None:
            from .admins.client import AdminsClient

            self._admins = AdminsClient(client_wrapper=self._client_wrapper)
        return self._admins

    @property
    def connections(self):
        if self._connections is None:
            from .connections.client import ConnectionsClient

            self._connections = ConnectionsClient(client_wrapper=self._client_wrapper)
        return self._connections

    @property
    def ip_lists(self):
        if self._ip_lists is None:
            from .ip_lists.client import IpListsClient

            self._ip_lists = IpListsClient(client_wrapper=self._client_wrapper)
        return self._ip_lists

    @property
    def defender(self):
        if self._defender is None:
            from .defender.client import DefenderClient

            self._defender = DefenderClient(client_wrapper=self._client_wrapper)
        return self._defender

    @property
    def data_retention(self):
        if self._data_retention is None:
            from .data_retention.client import DataRetentionClient

            self._data_retention = DataRetentionClient(client_wrapper=self._client_wrapper)
        return self._data_retention

    @property
    def quota(self):
        if self._quota is None:
            from .quota.client import QuotaClient

            self._quota = QuotaClient(client_wrapper=self._client_wrapper)
        return self._quota

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import FoldersClient

            self._folders = FoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import RolesClient

            self._roles = RolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def event_manager(self):
        if self._event_manager is None:
            from .event_manager.client import EventManagerClient

            self._event_manager = EventManagerClient(client_wrapper=self._client_wrapper)
        return self._event_manager

    @property
    def events(self):
        if self._events is None:
            from .events.client import EventsClient

            self._events = EventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import ApiKeysClient

            self._api_keys = ApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def user_ap_is(self):
        if self._user_ap_is is None:
            from .user_ap_is.client import UserApIsClient

            self._user_ap_is = UserApIsClient(client_wrapper=self._client_wrapper)
        return self._user_ap_is


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



    sftpgo_api_key : str
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
        sftpgo_api_key="YOUR_SFTPGO_API_KEY",
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        sftpgo_api_key: str,
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
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            sftpgo_api_key=sftpgo_api_key,
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
        self._healthcheck: typing.Optional[AsyncHealthcheckClient] = None
        self._public_shares: typing.Optional[AsyncPublicSharesClient] = None
        self._token: typing.Optional[AsyncTokenClient] = None
        self._maintenance: typing.Optional[AsyncMaintenanceClient] = None
        self._admins: typing.Optional[AsyncAdminsClient] = None
        self._connections: typing.Optional[AsyncConnectionsClient] = None
        self._ip_lists: typing.Optional[AsyncIpListsClient] = None
        self._defender: typing.Optional[AsyncDefenderClient] = None
        self._data_retention: typing.Optional[AsyncDataRetentionClient] = None
        self._quota: typing.Optional[AsyncQuotaClient] = None
        self._folders: typing.Optional[AsyncFoldersClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._roles: typing.Optional[AsyncRolesClient] = None
        self._event_manager: typing.Optional[AsyncEventManagerClient] = None
        self._events: typing.Optional[AsyncEventsClient] = None
        self._api_keys: typing.Optional[AsyncApiKeysClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._user_ap_is: typing.Optional[AsyncUserApIsClient] = None

    @property
    def healthcheck(self):
        if self._healthcheck is None:
            from .healthcheck.client import AsyncHealthcheckClient

            self._healthcheck = AsyncHealthcheckClient(client_wrapper=self._client_wrapper)
        return self._healthcheck

    @property
    def public_shares(self):
        if self._public_shares is None:
            from .public_shares.client import AsyncPublicSharesClient

            self._public_shares = AsyncPublicSharesClient(client_wrapper=self._client_wrapper)
        return self._public_shares

    @property
    def token(self):
        if self._token is None:
            from .token.client import AsyncTokenClient

            self._token = AsyncTokenClient(client_wrapper=self._client_wrapper)
        return self._token

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import AsyncMaintenanceClient

            self._maintenance = AsyncMaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance

    @property
    def admins(self):
        if self._admins is None:
            from .admins.client import AsyncAdminsClient

            self._admins = AsyncAdminsClient(client_wrapper=self._client_wrapper)
        return self._admins

    @property
    def connections(self):
        if self._connections is None:
            from .connections.client import AsyncConnectionsClient

            self._connections = AsyncConnectionsClient(client_wrapper=self._client_wrapper)
        return self._connections

    @property
    def ip_lists(self):
        if self._ip_lists is None:
            from .ip_lists.client import AsyncIpListsClient

            self._ip_lists = AsyncIpListsClient(client_wrapper=self._client_wrapper)
        return self._ip_lists

    @property
    def defender(self):
        if self._defender is None:
            from .defender.client import AsyncDefenderClient

            self._defender = AsyncDefenderClient(client_wrapper=self._client_wrapper)
        return self._defender

    @property
    def data_retention(self):
        if self._data_retention is None:
            from .data_retention.client import AsyncDataRetentionClient

            self._data_retention = AsyncDataRetentionClient(client_wrapper=self._client_wrapper)
        return self._data_retention

    @property
    def quota(self):
        if self._quota is None:
            from .quota.client import AsyncQuotaClient

            self._quota = AsyncQuotaClient(client_wrapper=self._client_wrapper)
        return self._quota

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import AsyncFoldersClient

            self._folders = AsyncFoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import AsyncRolesClient

            self._roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def event_manager(self):
        if self._event_manager is None:
            from .event_manager.client import AsyncEventManagerClient

            self._event_manager = AsyncEventManagerClient(client_wrapper=self._client_wrapper)
        return self._event_manager

    @property
    def events(self):
        if self._events is None:
            from .events.client import AsyncEventsClient

            self._events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import AsyncApiKeysClient

            self._api_keys = AsyncApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def user_ap_is(self):
        if self._user_ap_is is None:
            from .user_ap_is.client import AsyncUserApIsClient

            self._user_ap_is = AsyncUserApIsClient(client_wrapper=self._client_wrapper)
        return self._user_ap_is


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
