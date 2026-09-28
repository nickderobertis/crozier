

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .admin_sessions.client import AdminSessionsClient, AsyncAdminSessionsClient
    from .admins.client import AdminsClient, AsyncAdminsClient
    from .analytics.client import AnalyticsClient, AsyncAnalyticsClient
    from .apikeys.client import ApikeysClient, AsyncApikeysClient
    from .apps_sessions.client import AppsSessionsClient, AsyncAppsSessionsClient
    from .auth_modules.client import AsyncAuthModulesClient, AuthModulesClient
    from .backends.client import AsyncBackendsClient, BackendsClient
    from .certificates.client import AsyncCertificatesClient, CertificatesClient
    from .cluster.client import AsyncClusterClient, ClusterClient
    from .data_exporters.client import AsyncDataExportersClient, DataExportersClient
    from .entities.client import AsyncEntitiesClient, EntitiesClient
    from .error_templates.client import AsyncErrorTemplatesClient, ErrorTemplatesClient
    from .events.client import AsyncEventsClient, EventsClient
    from .experimental.client import AsyncExperimentalClient, ExperimentalClient
    from .forms.client import AsyncFormsClient, FormsClient
    from .frontends.client import AsyncFrontendsClient, FrontendsClient
    from .globalconfig.client import AsyncGlobalconfigClient, GlobalconfigClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .import_export.client import AsyncImportExportClient, ImportExportClient
    from .infos.client import AsyncInfosClient, InfosClient
    from .jwt_verifiers.client import AsyncJwtVerifiersClient, JwtVerifiersClient
    from .lines.client import AsyncLinesClient, LinesClient
    from .live.client import AsyncLiveClient, LiveClient
    from .organizations.client import AsyncOrganizationsClient, OrganizationsClient
    from .pki.client import AsyncPkiClient, PkiClient
    from .plugins.client import AsyncPluginsClient, PluginsClient
    from .privateapps.client import AsyncPrivateappsClient, PrivateappsClient
    from .route_compositions.client import AsyncRouteCompositionsClient, RouteCompositionsClient
    from .routes.client import AsyncRoutesClient, RoutesClient
    from .scripts.client import AsyncScriptsClient, ScriptsClient
    from .services.client import AsyncServicesClient, ServicesClient
    from .snowmonkey.client import AsyncSnowmonkeyClient, SnowmonkeyClient
    from .tcp.client import AsyncTcpClient, TcpClient
    from .teams.client import AsyncTeamsClient, TeamsClient
    from .templates.client import AsyncTemplatesClient, TemplatesClient
    from .tunnels.client import AsyncTunnelsClient, TunnelsClient
    from .version.client import AsyncVersionClient, VersionClient


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
        self._privateapps: typing.Optional[PrivateappsClient] = None
        self._infos: typing.Optional[InfosClient] = None
        self._version: typing.Optional[VersionClient] = None
        self._templates: typing.Optional[TemplatesClient] = None
        self._tcp: typing.Optional[TcpClient] = None
        self._admins: typing.Optional[AdminsClient] = None
        self._apikeys: typing.Optional[ApikeysClient] = None
        self._routes: typing.Optional[RoutesClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._services: typing.Optional[ServicesClient] = None
        self._certificates: typing.Optional[CertificatesClient] = None
        self._pki: typing.Optional[PkiClient] = None
        self._lines: typing.Optional[LinesClient] = None
        self._live: typing.Optional[LiveClient] = None
        self._globalconfig: typing.Optional[GlobalconfigClient] = None
        self._import_export: typing.Optional[ImportExportClient] = None
        self._snowmonkey: typing.Optional[SnowmonkeyClient] = None
        self._jwt_verifiers: typing.Optional[JwtVerifiersClient] = None
        self._auth_modules: typing.Optional[AuthModulesClient] = None
        self._cluster: typing.Optional[ClusterClient] = None
        self._tunnels: typing.Optional[TunnelsClient] = None
        self._scripts: typing.Optional[ScriptsClient] = None
        self._error_templates: typing.Optional[ErrorTemplatesClient] = None
        self._organizations: typing.Optional[OrganizationsClient] = None
        self._teams: typing.Optional[TeamsClient] = None
        self._data_exporters: typing.Optional[DataExportersClient] = None
        self._route_compositions: typing.Optional[RouteCompositionsClient] = None
        self._backends: typing.Optional[BackendsClient] = None
        self._frontends: typing.Optional[FrontendsClient] = None
        self._plugins: typing.Optional[PluginsClient] = None
        self._forms: typing.Optional[FormsClient] = None
        self._analytics: typing.Optional[AnalyticsClient] = None
        self._experimental: typing.Optional[ExperimentalClient] = None
        self._entities: typing.Optional[EntitiesClient] = None
        self._admin_sessions: typing.Optional[AdminSessionsClient] = None
        self._apps_sessions: typing.Optional[AppsSessionsClient] = None
        self._events: typing.Optional[EventsClient] = None

    @property
    def privateapps(self):
        if self._privateapps is None:
            from .privateapps.client import PrivateappsClient

            self._privateapps = PrivateappsClient(client_wrapper=self._client_wrapper)
        return self._privateapps

    @property
    def infos(self):
        if self._infos is None:
            from .infos.client import InfosClient

            self._infos = InfosClient(client_wrapper=self._client_wrapper)
        return self._infos

    @property
    def version(self):
        if self._version is None:
            from .version.client import VersionClient

            self._version = VersionClient(client_wrapper=self._client_wrapper)
        return self._version

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import TemplatesClient

            self._templates = TemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates

    @property
    def tcp(self):
        if self._tcp is None:
            from .tcp.client import TcpClient

            self._tcp = TcpClient(client_wrapper=self._client_wrapper)
        return self._tcp

    @property
    def admins(self):
        if self._admins is None:
            from .admins.client import AdminsClient

            self._admins = AdminsClient(client_wrapper=self._client_wrapper)
        return self._admins

    @property
    def apikeys(self):
        if self._apikeys is None:
            from .apikeys.client import ApikeysClient

            self._apikeys = ApikeysClient(client_wrapper=self._client_wrapper)
        return self._apikeys

    @property
    def routes(self):
        if self._routes is None:
            from .routes.client import RoutesClient

            self._routes = RoutesClient(client_wrapper=self._client_wrapper)
        return self._routes

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def services(self):
        if self._services is None:
            from .services.client import ServicesClient

            self._services = ServicesClient(client_wrapper=self._client_wrapper)
        return self._services

    @property
    def certificates(self):
        if self._certificates is None:
            from .certificates.client import CertificatesClient

            self._certificates = CertificatesClient(client_wrapper=self._client_wrapper)
        return self._certificates

    @property
    def pki(self):
        if self._pki is None:
            from .pki.client import PkiClient

            self._pki = PkiClient(client_wrapper=self._client_wrapper)
        return self._pki

    @property
    def lines(self):
        if self._lines is None:
            from .lines.client import LinesClient

            self._lines = LinesClient(client_wrapper=self._client_wrapper)
        return self._lines

    @property
    def live(self):
        if self._live is None:
            from .live.client import LiveClient

            self._live = LiveClient(client_wrapper=self._client_wrapper)
        return self._live

    @property
    def globalconfig(self):
        if self._globalconfig is None:
            from .globalconfig.client import GlobalconfigClient

            self._globalconfig = GlobalconfigClient(client_wrapper=self._client_wrapper)
        return self._globalconfig

    @property
    def import_export(self):
        if self._import_export is None:
            from .import_export.client import ImportExportClient

            self._import_export = ImportExportClient(client_wrapper=self._client_wrapper)
        return self._import_export

    @property
    def snowmonkey(self):
        if self._snowmonkey is None:
            from .snowmonkey.client import SnowmonkeyClient

            self._snowmonkey = SnowmonkeyClient(client_wrapper=self._client_wrapper)
        return self._snowmonkey

    @property
    def jwt_verifiers(self):
        if self._jwt_verifiers is None:
            from .jwt_verifiers.client import JwtVerifiersClient

            self._jwt_verifiers = JwtVerifiersClient(client_wrapper=self._client_wrapper)
        return self._jwt_verifiers

    @property
    def auth_modules(self):
        if self._auth_modules is None:
            from .auth_modules.client import AuthModulesClient

            self._auth_modules = AuthModulesClient(client_wrapper=self._client_wrapper)
        return self._auth_modules

    @property
    def cluster(self):
        if self._cluster is None:
            from .cluster.client import ClusterClient

            self._cluster = ClusterClient(client_wrapper=self._client_wrapper)
        return self._cluster

    @property
    def tunnels(self):
        if self._tunnels is None:
            from .tunnels.client import TunnelsClient

            self._tunnels = TunnelsClient(client_wrapper=self._client_wrapper)
        return self._tunnels

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import ScriptsClient

            self._scripts = ScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts

    @property
    def error_templates(self):
        if self._error_templates is None:
            from .error_templates.client import ErrorTemplatesClient

            self._error_templates = ErrorTemplatesClient(client_wrapper=self._client_wrapper)
        return self._error_templates

    @property
    def organizations(self):
        if self._organizations is None:
            from .organizations.client import OrganizationsClient

            self._organizations = OrganizationsClient(client_wrapper=self._client_wrapper)
        return self._organizations

    @property
    def teams(self):
        if self._teams is None:
            from .teams.client import TeamsClient

            self._teams = TeamsClient(client_wrapper=self._client_wrapper)
        return self._teams

    @property
    def data_exporters(self):
        if self._data_exporters is None:
            from .data_exporters.client import DataExportersClient

            self._data_exporters = DataExportersClient(client_wrapper=self._client_wrapper)
        return self._data_exporters

    @property
    def route_compositions(self):
        if self._route_compositions is None:
            from .route_compositions.client import RouteCompositionsClient

            self._route_compositions = RouteCompositionsClient(client_wrapper=self._client_wrapper)
        return self._route_compositions

    @property
    def backends(self):
        if self._backends is None:
            from .backends.client import BackendsClient

            self._backends = BackendsClient(client_wrapper=self._client_wrapper)
        return self._backends

    @property
    def frontends(self):
        if self._frontends is None:
            from .frontends.client import FrontendsClient

            self._frontends = FrontendsClient(client_wrapper=self._client_wrapper)
        return self._frontends

    @property
    def plugins(self):
        if self._plugins is None:
            from .plugins.client import PluginsClient

            self._plugins = PluginsClient(client_wrapper=self._client_wrapper)
        return self._plugins

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import FormsClient

            self._forms = FormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def analytics(self):
        if self._analytics is None:
            from .analytics.client import AnalyticsClient

            self._analytics = AnalyticsClient(client_wrapper=self._client_wrapper)
        return self._analytics

    @property
    def experimental(self):
        if self._experimental is None:
            from .experimental.client import ExperimentalClient

            self._experimental = ExperimentalClient(client_wrapper=self._client_wrapper)
        return self._experimental

    @property
    def entities(self):
        if self._entities is None:
            from .entities.client import EntitiesClient

            self._entities = EntitiesClient(client_wrapper=self._client_wrapper)
        return self._entities

    @property
    def admin_sessions(self):
        if self._admin_sessions is None:
            from .admin_sessions.client import AdminSessionsClient

            self._admin_sessions = AdminSessionsClient(client_wrapper=self._client_wrapper)
        return self._admin_sessions

    @property
    def apps_sessions(self):
        if self._apps_sessions is None:
            from .apps_sessions.client import AppsSessionsClient

            self._apps_sessions = AppsSessionsClient(client_wrapper=self._client_wrapper)
        return self._apps_sessions

    @property
    def events(self):
        if self._events is None:
            from .events.client import EventsClient

            self._events = EventsClient(client_wrapper=self._client_wrapper)
        return self._events


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
        self._privateapps: typing.Optional[AsyncPrivateappsClient] = None
        self._infos: typing.Optional[AsyncInfosClient] = None
        self._version: typing.Optional[AsyncVersionClient] = None
        self._templates: typing.Optional[AsyncTemplatesClient] = None
        self._tcp: typing.Optional[AsyncTcpClient] = None
        self._admins: typing.Optional[AsyncAdminsClient] = None
        self._apikeys: typing.Optional[AsyncApikeysClient] = None
        self._routes: typing.Optional[AsyncRoutesClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._services: typing.Optional[AsyncServicesClient] = None
        self._certificates: typing.Optional[AsyncCertificatesClient] = None
        self._pki: typing.Optional[AsyncPkiClient] = None
        self._lines: typing.Optional[AsyncLinesClient] = None
        self._live: typing.Optional[AsyncLiveClient] = None
        self._globalconfig: typing.Optional[AsyncGlobalconfigClient] = None
        self._import_export: typing.Optional[AsyncImportExportClient] = None
        self._snowmonkey: typing.Optional[AsyncSnowmonkeyClient] = None
        self._jwt_verifiers: typing.Optional[AsyncJwtVerifiersClient] = None
        self._auth_modules: typing.Optional[AsyncAuthModulesClient] = None
        self._cluster: typing.Optional[AsyncClusterClient] = None
        self._tunnels: typing.Optional[AsyncTunnelsClient] = None
        self._scripts: typing.Optional[AsyncScriptsClient] = None
        self._error_templates: typing.Optional[AsyncErrorTemplatesClient] = None
        self._organizations: typing.Optional[AsyncOrganizationsClient] = None
        self._teams: typing.Optional[AsyncTeamsClient] = None
        self._data_exporters: typing.Optional[AsyncDataExportersClient] = None
        self._route_compositions: typing.Optional[AsyncRouteCompositionsClient] = None
        self._backends: typing.Optional[AsyncBackendsClient] = None
        self._frontends: typing.Optional[AsyncFrontendsClient] = None
        self._plugins: typing.Optional[AsyncPluginsClient] = None
        self._forms: typing.Optional[AsyncFormsClient] = None
        self._analytics: typing.Optional[AsyncAnalyticsClient] = None
        self._experimental: typing.Optional[AsyncExperimentalClient] = None
        self._entities: typing.Optional[AsyncEntitiesClient] = None
        self._admin_sessions: typing.Optional[AsyncAdminSessionsClient] = None
        self._apps_sessions: typing.Optional[AsyncAppsSessionsClient] = None
        self._events: typing.Optional[AsyncEventsClient] = None

    @property
    def privateapps(self):
        if self._privateapps is None:
            from .privateapps.client import AsyncPrivateappsClient

            self._privateapps = AsyncPrivateappsClient(client_wrapper=self._client_wrapper)
        return self._privateapps

    @property
    def infos(self):
        if self._infos is None:
            from .infos.client import AsyncInfosClient

            self._infos = AsyncInfosClient(client_wrapper=self._client_wrapper)
        return self._infos

    @property
    def version(self):
        if self._version is None:
            from .version.client import AsyncVersionClient

            self._version = AsyncVersionClient(client_wrapper=self._client_wrapper)
        return self._version

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import AsyncTemplatesClient

            self._templates = AsyncTemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates

    @property
    def tcp(self):
        if self._tcp is None:
            from .tcp.client import AsyncTcpClient

            self._tcp = AsyncTcpClient(client_wrapper=self._client_wrapper)
        return self._tcp

    @property
    def admins(self):
        if self._admins is None:
            from .admins.client import AsyncAdminsClient

            self._admins = AsyncAdminsClient(client_wrapper=self._client_wrapper)
        return self._admins

    @property
    def apikeys(self):
        if self._apikeys is None:
            from .apikeys.client import AsyncApikeysClient

            self._apikeys = AsyncApikeysClient(client_wrapper=self._client_wrapper)
        return self._apikeys

    @property
    def routes(self):
        if self._routes is None:
            from .routes.client import AsyncRoutesClient

            self._routes = AsyncRoutesClient(client_wrapper=self._client_wrapper)
        return self._routes

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def services(self):
        if self._services is None:
            from .services.client import AsyncServicesClient

            self._services = AsyncServicesClient(client_wrapper=self._client_wrapper)
        return self._services

    @property
    def certificates(self):
        if self._certificates is None:
            from .certificates.client import AsyncCertificatesClient

            self._certificates = AsyncCertificatesClient(client_wrapper=self._client_wrapper)
        return self._certificates

    @property
    def pki(self):
        if self._pki is None:
            from .pki.client import AsyncPkiClient

            self._pki = AsyncPkiClient(client_wrapper=self._client_wrapper)
        return self._pki

    @property
    def lines(self):
        if self._lines is None:
            from .lines.client import AsyncLinesClient

            self._lines = AsyncLinesClient(client_wrapper=self._client_wrapper)
        return self._lines

    @property
    def live(self):
        if self._live is None:
            from .live.client import AsyncLiveClient

            self._live = AsyncLiveClient(client_wrapper=self._client_wrapper)
        return self._live

    @property
    def globalconfig(self):
        if self._globalconfig is None:
            from .globalconfig.client import AsyncGlobalconfigClient

            self._globalconfig = AsyncGlobalconfigClient(client_wrapper=self._client_wrapper)
        return self._globalconfig

    @property
    def import_export(self):
        if self._import_export is None:
            from .import_export.client import AsyncImportExportClient

            self._import_export = AsyncImportExportClient(client_wrapper=self._client_wrapper)
        return self._import_export

    @property
    def snowmonkey(self):
        if self._snowmonkey is None:
            from .snowmonkey.client import AsyncSnowmonkeyClient

            self._snowmonkey = AsyncSnowmonkeyClient(client_wrapper=self._client_wrapper)
        return self._snowmonkey

    @property
    def jwt_verifiers(self):
        if self._jwt_verifiers is None:
            from .jwt_verifiers.client import AsyncJwtVerifiersClient

            self._jwt_verifiers = AsyncJwtVerifiersClient(client_wrapper=self._client_wrapper)
        return self._jwt_verifiers

    @property
    def auth_modules(self):
        if self._auth_modules is None:
            from .auth_modules.client import AsyncAuthModulesClient

            self._auth_modules = AsyncAuthModulesClient(client_wrapper=self._client_wrapper)
        return self._auth_modules

    @property
    def cluster(self):
        if self._cluster is None:
            from .cluster.client import AsyncClusterClient

            self._cluster = AsyncClusterClient(client_wrapper=self._client_wrapper)
        return self._cluster

    @property
    def tunnels(self):
        if self._tunnels is None:
            from .tunnels.client import AsyncTunnelsClient

            self._tunnels = AsyncTunnelsClient(client_wrapper=self._client_wrapper)
        return self._tunnels

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import AsyncScriptsClient

            self._scripts = AsyncScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts

    @property
    def error_templates(self):
        if self._error_templates is None:
            from .error_templates.client import AsyncErrorTemplatesClient

            self._error_templates = AsyncErrorTemplatesClient(client_wrapper=self._client_wrapper)
        return self._error_templates

    @property
    def organizations(self):
        if self._organizations is None:
            from .organizations.client import AsyncOrganizationsClient

            self._organizations = AsyncOrganizationsClient(client_wrapper=self._client_wrapper)
        return self._organizations

    @property
    def teams(self):
        if self._teams is None:
            from .teams.client import AsyncTeamsClient

            self._teams = AsyncTeamsClient(client_wrapper=self._client_wrapper)
        return self._teams

    @property
    def data_exporters(self):
        if self._data_exporters is None:
            from .data_exporters.client import AsyncDataExportersClient

            self._data_exporters = AsyncDataExportersClient(client_wrapper=self._client_wrapper)
        return self._data_exporters

    @property
    def route_compositions(self):
        if self._route_compositions is None:
            from .route_compositions.client import AsyncRouteCompositionsClient

            self._route_compositions = AsyncRouteCompositionsClient(client_wrapper=self._client_wrapper)
        return self._route_compositions

    @property
    def backends(self):
        if self._backends is None:
            from .backends.client import AsyncBackendsClient

            self._backends = AsyncBackendsClient(client_wrapper=self._client_wrapper)
        return self._backends

    @property
    def frontends(self):
        if self._frontends is None:
            from .frontends.client import AsyncFrontendsClient

            self._frontends = AsyncFrontendsClient(client_wrapper=self._client_wrapper)
        return self._frontends

    @property
    def plugins(self):
        if self._plugins is None:
            from .plugins.client import AsyncPluginsClient

            self._plugins = AsyncPluginsClient(client_wrapper=self._client_wrapper)
        return self._plugins

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import AsyncFormsClient

            self._forms = AsyncFormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def analytics(self):
        if self._analytics is None:
            from .analytics.client import AsyncAnalyticsClient

            self._analytics = AsyncAnalyticsClient(client_wrapper=self._client_wrapper)
        return self._analytics

    @property
    def experimental(self):
        if self._experimental is None:
            from .experimental.client import AsyncExperimentalClient

            self._experimental = AsyncExperimentalClient(client_wrapper=self._client_wrapper)
        return self._experimental

    @property
    def entities(self):
        if self._entities is None:
            from .entities.client import AsyncEntitiesClient

            self._entities = AsyncEntitiesClient(client_wrapper=self._client_wrapper)
        return self._entities

    @property
    def admin_sessions(self):
        if self._admin_sessions is None:
            from .admin_sessions.client import AsyncAdminSessionsClient

            self._admin_sessions = AsyncAdminSessionsClient(client_wrapper=self._client_wrapper)
        return self._admin_sessions

    @property
    def apps_sessions(self):
        if self._apps_sessions is None:
            from .apps_sessions.client import AsyncAppsSessionsClient

            self._apps_sessions = AsyncAppsSessionsClient(client_wrapper=self._client_wrapper)
        return self._apps_sessions

    @property
    def events(self):
        if self._events is None:
            from .events.client import AsyncEventsClient

            self._events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        return self._events


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
