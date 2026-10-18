

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .advisors.client import AdvisorsClient, AsyncAdvisorsClient
    from .analytics.client import AnalyticsClient, AsyncAnalyticsClient
    from .auth.client import AsyncAuthClient, AuthClient
    from .billing.client import AsyncBillingClient, BillingClient
    from .database.client import AsyncDatabaseClient, DatabaseClient
    from .domains.client import AsyncDomainsClient, DomainsClient
    from .edge_functions.client import AsyncEdgeFunctionsClient, EdgeFunctionsClient
    from .environments.client import AsyncEnvironmentsClient, EnvironmentsClient
    from .o_auth.client import AsyncOAuthClient, OAuthClient
    from .organizations.client import AsyncOrganizationsClient, OrganizationsClient
    from .profile.client import AsyncProfileClient, ProfileClient
    from .projects.client import AsyncProjectsClient, ProjectsClient
    from .realtime.client import AsyncRealtimeClient, RealtimeClient
    from .rest.client import AsyncRestClient, RestClient
    from .secrets.client import AsyncSecretsClient, SecretsClient
    from .storage.client import AsyncStorageClient, StorageClient


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
        self._environments: typing.Optional[EnvironmentsClient] = None
        self._projects: typing.Optional[ProjectsClient] = None
        self._organizations: typing.Optional[OrganizationsClient] = None
        self._o_auth: typing.Optional[OAuthClient] = None
        self._database: typing.Optional[DatabaseClient] = None
        self._profile: typing.Optional[ProfileClient] = None
        self._secrets: typing.Optional[SecretsClient] = None
        self._domains: typing.Optional[DomainsClient] = None
        self._rest: typing.Optional[RestClient] = None
        self._auth: typing.Optional[AuthClient] = None
        self._billing: typing.Optional[BillingClient] = None
        self._advisors: typing.Optional[AdvisorsClient] = None
        self._analytics: typing.Optional[AnalyticsClient] = None
        self._edge_functions: typing.Optional[EdgeFunctionsClient] = None
        self._storage: typing.Optional[StorageClient] = None
        self._realtime: typing.Optional[RealtimeClient] = None

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import EnvironmentsClient

            self._environments = EnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import ProjectsClient

            self._projects = ProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def organizations(self):
        if self._organizations is None:
            from .organizations.client import OrganizationsClient

            self._organizations = OrganizationsClient(client_wrapper=self._client_wrapper)
        return self._organizations

    @property
    def o_auth(self):
        if self._o_auth is None:
            from .o_auth.client import OAuthClient

            self._o_auth = OAuthClient(client_wrapper=self._client_wrapper)
        return self._o_auth

    @property
    def database(self):
        if self._database is None:
            from .database.client import DatabaseClient

            self._database = DatabaseClient(client_wrapper=self._client_wrapper)
        return self._database

    @property
    def profile(self):
        if self._profile is None:
            from .profile.client import ProfileClient

            self._profile = ProfileClient(client_wrapper=self._client_wrapper)
        return self._profile

    @property
    def secrets(self):
        if self._secrets is None:
            from .secrets.client import SecretsClient

            self._secrets = SecretsClient(client_wrapper=self._client_wrapper)
        return self._secrets

    @property
    def domains(self):
        if self._domains is None:
            from .domains.client import DomainsClient

            self._domains = DomainsClient(client_wrapper=self._client_wrapper)
        return self._domains

    @property
    def rest(self):
        if self._rest is None:
            from .rest.client import RestClient

            self._rest = RestClient(client_wrapper=self._client_wrapper)
        return self._rest

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AuthClient

            self._auth = AuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def billing(self):
        if self._billing is None:
            from .billing.client import BillingClient

            self._billing = BillingClient(client_wrapper=self._client_wrapper)
        return self._billing

    @property
    def advisors(self):
        if self._advisors is None:
            from .advisors.client import AdvisorsClient

            self._advisors = AdvisorsClient(client_wrapper=self._client_wrapper)
        return self._advisors

    @property
    def analytics(self):
        if self._analytics is None:
            from .analytics.client import AnalyticsClient

            self._analytics = AnalyticsClient(client_wrapper=self._client_wrapper)
        return self._analytics

    @property
    def edge_functions(self):
        if self._edge_functions is None:
            from .edge_functions.client import EdgeFunctionsClient

            self._edge_functions = EdgeFunctionsClient(client_wrapper=self._client_wrapper)
        return self._edge_functions

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import StorageClient

            self._storage = StorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def realtime(self):
        if self._realtime is None:
            from .realtime.client import RealtimeClient

            self._realtime = RealtimeClient(client_wrapper=self._client_wrapper)
        return self._realtime


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
        self._environments: typing.Optional[AsyncEnvironmentsClient] = None
        self._projects: typing.Optional[AsyncProjectsClient] = None
        self._organizations: typing.Optional[AsyncOrganizationsClient] = None
        self._o_auth: typing.Optional[AsyncOAuthClient] = None
        self._database: typing.Optional[AsyncDatabaseClient] = None
        self._profile: typing.Optional[AsyncProfileClient] = None
        self._secrets: typing.Optional[AsyncSecretsClient] = None
        self._domains: typing.Optional[AsyncDomainsClient] = None
        self._rest: typing.Optional[AsyncRestClient] = None
        self._auth: typing.Optional[AsyncAuthClient] = None
        self._billing: typing.Optional[AsyncBillingClient] = None
        self._advisors: typing.Optional[AsyncAdvisorsClient] = None
        self._analytics: typing.Optional[AsyncAnalyticsClient] = None
        self._edge_functions: typing.Optional[AsyncEdgeFunctionsClient] = None
        self._storage: typing.Optional[AsyncStorageClient] = None
        self._realtime: typing.Optional[AsyncRealtimeClient] = None

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import AsyncEnvironmentsClient

            self._environments = AsyncEnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            self._projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def organizations(self):
        if self._organizations is None:
            from .organizations.client import AsyncOrganizationsClient

            self._organizations = AsyncOrganizationsClient(client_wrapper=self._client_wrapper)
        return self._organizations

    @property
    def o_auth(self):
        if self._o_auth is None:
            from .o_auth.client import AsyncOAuthClient

            self._o_auth = AsyncOAuthClient(client_wrapper=self._client_wrapper)
        return self._o_auth

    @property
    def database(self):
        if self._database is None:
            from .database.client import AsyncDatabaseClient

            self._database = AsyncDatabaseClient(client_wrapper=self._client_wrapper)
        return self._database

    @property
    def profile(self):
        if self._profile is None:
            from .profile.client import AsyncProfileClient

            self._profile = AsyncProfileClient(client_wrapper=self._client_wrapper)
        return self._profile

    @property
    def secrets(self):
        if self._secrets is None:
            from .secrets.client import AsyncSecretsClient

            self._secrets = AsyncSecretsClient(client_wrapper=self._client_wrapper)
        return self._secrets

    @property
    def domains(self):
        if self._domains is None:
            from .domains.client import AsyncDomainsClient

            self._domains = AsyncDomainsClient(client_wrapper=self._client_wrapper)
        return self._domains

    @property
    def rest(self):
        if self._rest is None:
            from .rest.client import AsyncRestClient

            self._rest = AsyncRestClient(client_wrapper=self._client_wrapper)
        return self._rest

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AsyncAuthClient

            self._auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def billing(self):
        if self._billing is None:
            from .billing.client import AsyncBillingClient

            self._billing = AsyncBillingClient(client_wrapper=self._client_wrapper)
        return self._billing

    @property
    def advisors(self):
        if self._advisors is None:
            from .advisors.client import AsyncAdvisorsClient

            self._advisors = AsyncAdvisorsClient(client_wrapper=self._client_wrapper)
        return self._advisors

    @property
    def analytics(self):
        if self._analytics is None:
            from .analytics.client import AsyncAnalyticsClient

            self._analytics = AsyncAnalyticsClient(client_wrapper=self._client_wrapper)
        return self._analytics

    @property
    def edge_functions(self):
        if self._edge_functions is None:
            from .edge_functions.client import AsyncEdgeFunctionsClient

            self._edge_functions = AsyncEdgeFunctionsClient(client_wrapper=self._client_wrapper)
        return self._edge_functions

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import AsyncStorageClient

            self._storage = AsyncStorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def realtime(self):
        if self._realtime is None:
            from .realtime.client import AsyncRealtimeClient

            self._realtime = AsyncRealtimeClient(client_wrapper=self._client_wrapper)
        return self._realtime


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
