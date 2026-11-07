

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .app_v1.client import AppV1Client, AsyncAppV1Client
    from .auth_v1.client import AsyncAuthV1Client, AuthV1Client
    from .billing_v1.client import AsyncBillingV1Client, BillingV1Client
    from .build_v1.client import AsyncBuildV1Client, BuildV1Client
    from .deployment_v1.client import AsyncDeploymentV1Client, DeploymentV1Client
    from .deployment_v2.client import AsyncDeploymentV2Client, DeploymentV2Client
    from .discovery_v1.client import AsyncDiscoveryV1Client, DiscoveryV1Client
    from .lobby_v1.client import AsyncLobbyV1Client, LobbyV1Client
    from .lobby_v2.client import AsyncLobbyV2Client, LobbyV2Client
    from .lobby_v3.client import AsyncLobbyV3Client, LobbyV3Client
    from .log_v1.client import AsyncLogV1Client, LogV1Client
    from .management_v1.client import AsyncManagementV1Client, ManagementV1Client
    from .metrics_v1.client import AsyncMetricsV1Client, MetricsV1Client
    from .org_tokens_v1.client import AsyncOrgTokensV1Client, OrgTokensV1Client
    from .processes_v1.client import AsyncProcessesV1Client, ProcessesV1Client
    from .processes_v2.client import AsyncProcessesV2Client, ProcessesV2Client
    from .room_v1.client import AsyncRoomV1Client, RoomV1Client
    from .room_v2.client import AsyncRoomV2Client, RoomV2Client


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
        self._app_v1: typing.Optional[AppV1Client] = None
        self._auth_v1: typing.Optional[AuthV1Client] = None
        self._billing_v1: typing.Optional[BillingV1Client] = None
        self._build_v1: typing.Optional[BuildV1Client] = None
        self._deployment_v1: typing.Optional[DeploymentV1Client] = None
        self._deployment_v2: typing.Optional[DeploymentV2Client] = None
        self._discovery_v1: typing.Optional[DiscoveryV1Client] = None
        self._lobby_v1: typing.Optional[LobbyV1Client] = None
        self._lobby_v2: typing.Optional[LobbyV2Client] = None
        self._lobby_v3: typing.Optional[LobbyV3Client] = None
        self._log_v1: typing.Optional[LogV1Client] = None
        self._management_v1: typing.Optional[ManagementV1Client] = None
        self._metrics_v1: typing.Optional[MetricsV1Client] = None
        self._processes_v1: typing.Optional[ProcessesV1Client] = None
        self._processes_v2: typing.Optional[ProcessesV2Client] = None
        self._room_v1: typing.Optional[RoomV1Client] = None
        self._room_v2: typing.Optional[RoomV2Client] = None
        self._org_tokens_v1: typing.Optional[OrgTokensV1Client] = None

    @property
    def app_v1(self):
        if self._app_v1 is None:
            from .app_v1.client import AppV1Client

            self._app_v1 = AppV1Client(client_wrapper=self._client_wrapper)
        return self._app_v1

    @property
    def auth_v1(self):
        if self._auth_v1 is None:
            from .auth_v1.client import AuthV1Client

            self._auth_v1 = AuthV1Client(client_wrapper=self._client_wrapper)
        return self._auth_v1

    @property
    def billing_v1(self):
        if self._billing_v1 is None:
            from .billing_v1.client import BillingV1Client

            self._billing_v1 = BillingV1Client(client_wrapper=self._client_wrapper)
        return self._billing_v1

    @property
    def build_v1(self):
        if self._build_v1 is None:
            from .build_v1.client import BuildV1Client

            self._build_v1 = BuildV1Client(client_wrapper=self._client_wrapper)
        return self._build_v1

    @property
    def deployment_v1(self):
        if self._deployment_v1 is None:
            from .deployment_v1.client import DeploymentV1Client

            self._deployment_v1 = DeploymentV1Client(client_wrapper=self._client_wrapper)
        return self._deployment_v1

    @property
    def deployment_v2(self):
        if self._deployment_v2 is None:
            from .deployment_v2.client import DeploymentV2Client

            self._deployment_v2 = DeploymentV2Client(client_wrapper=self._client_wrapper)
        return self._deployment_v2

    @property
    def discovery_v1(self):
        if self._discovery_v1 is None:
            from .discovery_v1.client import DiscoveryV1Client

            self._discovery_v1 = DiscoveryV1Client(client_wrapper=self._client_wrapper)
        return self._discovery_v1

    @property
    def lobby_v1(self):
        if self._lobby_v1 is None:
            from .lobby_v1.client import LobbyV1Client

            self._lobby_v1 = LobbyV1Client(client_wrapper=self._client_wrapper)
        return self._lobby_v1

    @property
    def lobby_v2(self):
        if self._lobby_v2 is None:
            from .lobby_v2.client import LobbyV2Client

            self._lobby_v2 = LobbyV2Client(client_wrapper=self._client_wrapper)
        return self._lobby_v2

    @property
    def lobby_v3(self):
        if self._lobby_v3 is None:
            from .lobby_v3.client import LobbyV3Client

            self._lobby_v3 = LobbyV3Client(client_wrapper=self._client_wrapper)
        return self._lobby_v3

    @property
    def log_v1(self):
        if self._log_v1 is None:
            from .log_v1.client import LogV1Client

            self._log_v1 = LogV1Client(client_wrapper=self._client_wrapper)
        return self._log_v1

    @property
    def management_v1(self):
        if self._management_v1 is None:
            from .management_v1.client import ManagementV1Client

            self._management_v1 = ManagementV1Client(client_wrapper=self._client_wrapper)
        return self._management_v1

    @property
    def metrics_v1(self):
        if self._metrics_v1 is None:
            from .metrics_v1.client import MetricsV1Client

            self._metrics_v1 = MetricsV1Client(client_wrapper=self._client_wrapper)
        return self._metrics_v1

    @property
    def processes_v1(self):
        if self._processes_v1 is None:
            from .processes_v1.client import ProcessesV1Client

            self._processes_v1 = ProcessesV1Client(client_wrapper=self._client_wrapper)
        return self._processes_v1

    @property
    def processes_v2(self):
        if self._processes_v2 is None:
            from .processes_v2.client import ProcessesV2Client

            self._processes_v2 = ProcessesV2Client(client_wrapper=self._client_wrapper)
        return self._processes_v2

    @property
    def room_v1(self):
        if self._room_v1 is None:
            from .room_v1.client import RoomV1Client

            self._room_v1 = RoomV1Client(client_wrapper=self._client_wrapper)
        return self._room_v1

    @property
    def room_v2(self):
        if self._room_v2 is None:
            from .room_v2.client import RoomV2Client

            self._room_v2 = RoomV2Client(client_wrapper=self._client_wrapper)
        return self._room_v2

    @property
    def org_tokens_v1(self):
        if self._org_tokens_v1 is None:
            from .org_tokens_v1.client import OrgTokensV1Client

            self._org_tokens_v1 = OrgTokensV1Client(client_wrapper=self._client_wrapper)
        return self._org_tokens_v1


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
        self._app_v1: typing.Optional[AsyncAppV1Client] = None
        self._auth_v1: typing.Optional[AsyncAuthV1Client] = None
        self._billing_v1: typing.Optional[AsyncBillingV1Client] = None
        self._build_v1: typing.Optional[AsyncBuildV1Client] = None
        self._deployment_v1: typing.Optional[AsyncDeploymentV1Client] = None
        self._deployment_v2: typing.Optional[AsyncDeploymentV2Client] = None
        self._discovery_v1: typing.Optional[AsyncDiscoveryV1Client] = None
        self._lobby_v1: typing.Optional[AsyncLobbyV1Client] = None
        self._lobby_v2: typing.Optional[AsyncLobbyV2Client] = None
        self._lobby_v3: typing.Optional[AsyncLobbyV3Client] = None
        self._log_v1: typing.Optional[AsyncLogV1Client] = None
        self._management_v1: typing.Optional[AsyncManagementV1Client] = None
        self._metrics_v1: typing.Optional[AsyncMetricsV1Client] = None
        self._processes_v1: typing.Optional[AsyncProcessesV1Client] = None
        self._processes_v2: typing.Optional[AsyncProcessesV2Client] = None
        self._room_v1: typing.Optional[AsyncRoomV1Client] = None
        self._room_v2: typing.Optional[AsyncRoomV2Client] = None
        self._org_tokens_v1: typing.Optional[AsyncOrgTokensV1Client] = None

    @property
    def app_v1(self):
        if self._app_v1 is None:
            from .app_v1.client import AsyncAppV1Client

            self._app_v1 = AsyncAppV1Client(client_wrapper=self._client_wrapper)
        return self._app_v1

    @property
    def auth_v1(self):
        if self._auth_v1 is None:
            from .auth_v1.client import AsyncAuthV1Client

            self._auth_v1 = AsyncAuthV1Client(client_wrapper=self._client_wrapper)
        return self._auth_v1

    @property
    def billing_v1(self):
        if self._billing_v1 is None:
            from .billing_v1.client import AsyncBillingV1Client

            self._billing_v1 = AsyncBillingV1Client(client_wrapper=self._client_wrapper)
        return self._billing_v1

    @property
    def build_v1(self):
        if self._build_v1 is None:
            from .build_v1.client import AsyncBuildV1Client

            self._build_v1 = AsyncBuildV1Client(client_wrapper=self._client_wrapper)
        return self._build_v1

    @property
    def deployment_v1(self):
        if self._deployment_v1 is None:
            from .deployment_v1.client import AsyncDeploymentV1Client

            self._deployment_v1 = AsyncDeploymentV1Client(client_wrapper=self._client_wrapper)
        return self._deployment_v1

    @property
    def deployment_v2(self):
        if self._deployment_v2 is None:
            from .deployment_v2.client import AsyncDeploymentV2Client

            self._deployment_v2 = AsyncDeploymentV2Client(client_wrapper=self._client_wrapper)
        return self._deployment_v2

    @property
    def discovery_v1(self):
        if self._discovery_v1 is None:
            from .discovery_v1.client import AsyncDiscoveryV1Client

            self._discovery_v1 = AsyncDiscoveryV1Client(client_wrapper=self._client_wrapper)
        return self._discovery_v1

    @property
    def lobby_v1(self):
        if self._lobby_v1 is None:
            from .lobby_v1.client import AsyncLobbyV1Client

            self._lobby_v1 = AsyncLobbyV1Client(client_wrapper=self._client_wrapper)
        return self._lobby_v1

    @property
    def lobby_v2(self):
        if self._lobby_v2 is None:
            from .lobby_v2.client import AsyncLobbyV2Client

            self._lobby_v2 = AsyncLobbyV2Client(client_wrapper=self._client_wrapper)
        return self._lobby_v2

    @property
    def lobby_v3(self):
        if self._lobby_v3 is None:
            from .lobby_v3.client import AsyncLobbyV3Client

            self._lobby_v3 = AsyncLobbyV3Client(client_wrapper=self._client_wrapper)
        return self._lobby_v3

    @property
    def log_v1(self):
        if self._log_v1 is None:
            from .log_v1.client import AsyncLogV1Client

            self._log_v1 = AsyncLogV1Client(client_wrapper=self._client_wrapper)
        return self._log_v1

    @property
    def management_v1(self):
        if self._management_v1 is None:
            from .management_v1.client import AsyncManagementV1Client

            self._management_v1 = AsyncManagementV1Client(client_wrapper=self._client_wrapper)
        return self._management_v1

    @property
    def metrics_v1(self):
        if self._metrics_v1 is None:
            from .metrics_v1.client import AsyncMetricsV1Client

            self._metrics_v1 = AsyncMetricsV1Client(client_wrapper=self._client_wrapper)
        return self._metrics_v1

    @property
    def processes_v1(self):
        if self._processes_v1 is None:
            from .processes_v1.client import AsyncProcessesV1Client

            self._processes_v1 = AsyncProcessesV1Client(client_wrapper=self._client_wrapper)
        return self._processes_v1

    @property
    def processes_v2(self):
        if self._processes_v2 is None:
            from .processes_v2.client import AsyncProcessesV2Client

            self._processes_v2 = AsyncProcessesV2Client(client_wrapper=self._client_wrapper)
        return self._processes_v2

    @property
    def room_v1(self):
        if self._room_v1 is None:
            from .room_v1.client import AsyncRoomV1Client

            self._room_v1 = AsyncRoomV1Client(client_wrapper=self._client_wrapper)
        return self._room_v1

    @property
    def room_v2(self):
        if self._room_v2 is None:
            from .room_v2.client import AsyncRoomV2Client

            self._room_v2 = AsyncRoomV2Client(client_wrapper=self._client_wrapper)
        return self._room_v2

    @property
    def org_tokens_v1(self):
        if self._org_tokens_v1 is None:
            from .org_tokens_v1.client import AsyncOrgTokensV1Client

            self._org_tokens_v1 = AsyncOrgTokensV1Client(client_wrapper=self._client_wrapper)
        return self._org_tokens_v1


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
