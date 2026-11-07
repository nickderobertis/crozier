

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .agent_telemetry.client import AgentTelemetryClient, AsyncAgentTelemetryClient
    from .agents.client import AgentsClient, AsyncAgentsClient
    from .billing.client import AsyncBillingClient, BillingClient
    from .configuration.client import AsyncConfigurationClient, ConfigurationClient
    from .environments.client import AsyncEnvironmentsClient, EnvironmentsClient
    from .health.client import AsyncHealthClient, HealthClient
    from .heart_beat.client import AsyncHeartBeatClient, HeartBeatClient
    from .locations.client import AsyncLocationsClient, LocationsClient
    from .netmon.client import AsyncNetmonClient, NetmonClient
    from .network_settings.client import AsyncNetworkSettingsClient, NetworkSettingsClient
    from .plans.client import AsyncPlansClient, PlansClient
    from .pool.client import AsyncPoolClient, PoolClient
    from .pool_group.client import AsyncPoolGroupClient, PoolGroupClient
    from .pools.client import AsyncPoolsClient, PoolsClient
    from .prebuilds.client import AsyncPrebuildsClient, PrebuildsClient
    from .prebuilds_v.client import AsyncPrebuildsVClient, PrebuildsVClient
    from .privacy.client import AsyncPrivacyClient, PrivacyClient
    from .resources.client import AsyncResourcesClient, ResourcesClient
    from .sas.client import AsyncSasClient, SasClient
    from .secrets.client import AsyncSecretsClient, SecretsClient
    from .tenant.client import AsyncTenantClient, TenantClient
    from .tokens.client import AsyncTokensClient, TokensClient
    from .tunnel.client import AsyncTunnelClient, TunnelClient
    from .user_subscriptions.client import AsyncUserSubscriptionsClient, UserSubscriptionsClient
    from .vm.client import AsyncVmClient, VmClient
    from .vnet_pool_definitions.client import AsyncVnetPoolDefinitionsClient, VnetPoolDefinitionsClient
    from .warmup.client import AsyncWarmupClient, WarmupClient


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
        self._agent_telemetry: typing.Optional[AgentTelemetryClient] = None
        self._agents: typing.Optional[AgentsClient] = None
        self._environments: typing.Optional[EnvironmentsClient] = None
        self._billing: typing.Optional[BillingClient] = None
        self._configuration: typing.Optional[ConfigurationClient] = None
        self._pools: typing.Optional[PoolsClient] = None
        self._prebuilds: typing.Optional[PrebuildsClient] = None
        self._privacy: typing.Optional[PrivacyClient] = None
        self._resources: typing.Optional[ResourcesClient] = None
        self._vnet_pool_definitions: typing.Optional[VnetPoolDefinitionsClient] = None
        self._heart_beat: typing.Optional[HeartBeatClient] = None
        self._locations: typing.Optional[LocationsClient] = None
        self._sas: typing.Optional[SasClient] = None
        self._secrets: typing.Optional[SecretsClient] = None
        self._tenant: typing.Optional[TenantClient] = None
        self._tokens: typing.Optional[TokensClient] = None
        self._tunnel: typing.Optional[TunnelClient] = None
        self._user_subscriptions: typing.Optional[UserSubscriptionsClient] = None
        self._network_settings: typing.Optional[NetworkSettingsClient] = None
        self._plans: typing.Optional[PlansClient] = None
        self._pool: typing.Optional[PoolClient] = None
        self._pool_group: typing.Optional[PoolGroupClient] = None
        self._vm: typing.Optional[VmClient] = None
        self._prebuilds_v: typing.Optional[PrebuildsVClient] = None
        self._health: typing.Optional[HealthClient] = None
        self._netmon: typing.Optional[NetmonClient] = None
        self._warmup: typing.Optional[WarmupClient] = None

    @property
    def agent_telemetry(self):
        if self._agent_telemetry is None:
            from .agent_telemetry.client import AgentTelemetryClient

            self._agent_telemetry = AgentTelemetryClient(client_wrapper=self._client_wrapper)
        return self._agent_telemetry

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AgentsClient

            self._agents = AgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import EnvironmentsClient

            self._environments = EnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def billing(self):
        if self._billing is None:
            from .billing.client import BillingClient

            self._billing = BillingClient(client_wrapper=self._client_wrapper)
        return self._billing

    @property
    def configuration(self):
        if self._configuration is None:
            from .configuration.client import ConfigurationClient

            self._configuration = ConfigurationClient(client_wrapper=self._client_wrapper)
        return self._configuration

    @property
    def pools(self):
        if self._pools is None:
            from .pools.client import PoolsClient

            self._pools = PoolsClient(client_wrapper=self._client_wrapper)
        return self._pools

    @property
    def prebuilds(self):
        if self._prebuilds is None:
            from .prebuilds.client import PrebuildsClient

            self._prebuilds = PrebuildsClient(client_wrapper=self._client_wrapper)
        return self._prebuilds

    @property
    def privacy(self):
        if self._privacy is None:
            from .privacy.client import PrivacyClient

            self._privacy = PrivacyClient(client_wrapper=self._client_wrapper)
        return self._privacy

    @property
    def resources(self):
        if self._resources is None:
            from .resources.client import ResourcesClient

            self._resources = ResourcesClient(client_wrapper=self._client_wrapper)
        return self._resources

    @property
    def vnet_pool_definitions(self):
        if self._vnet_pool_definitions is None:
            from .vnet_pool_definitions.client import VnetPoolDefinitionsClient

            self._vnet_pool_definitions = VnetPoolDefinitionsClient(client_wrapper=self._client_wrapper)
        return self._vnet_pool_definitions

    @property
    def heart_beat(self):
        if self._heart_beat is None:
            from .heart_beat.client import HeartBeatClient

            self._heart_beat = HeartBeatClient(client_wrapper=self._client_wrapper)
        return self._heart_beat

    @property
    def locations(self):
        if self._locations is None:
            from .locations.client import LocationsClient

            self._locations = LocationsClient(client_wrapper=self._client_wrapper)
        return self._locations

    @property
    def sas(self):
        if self._sas is None:
            from .sas.client import SasClient

            self._sas = SasClient(client_wrapper=self._client_wrapper)
        return self._sas

    @property
    def secrets(self):
        if self._secrets is None:
            from .secrets.client import SecretsClient

            self._secrets = SecretsClient(client_wrapper=self._client_wrapper)
        return self._secrets

    @property
    def tenant(self):
        if self._tenant is None:
            from .tenant.client import TenantClient

            self._tenant = TenantClient(client_wrapper=self._client_wrapper)
        return self._tenant

    @property
    def tokens(self):
        if self._tokens is None:
            from .tokens.client import TokensClient

            self._tokens = TokensClient(client_wrapper=self._client_wrapper)
        return self._tokens

    @property
    def tunnel(self):
        if self._tunnel is None:
            from .tunnel.client import TunnelClient

            self._tunnel = TunnelClient(client_wrapper=self._client_wrapper)
        return self._tunnel

    @property
    def user_subscriptions(self):
        if self._user_subscriptions is None:
            from .user_subscriptions.client import UserSubscriptionsClient

            self._user_subscriptions = UserSubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._user_subscriptions

    @property
    def network_settings(self):
        if self._network_settings is None:
            from .network_settings.client import NetworkSettingsClient

            self._network_settings = NetworkSettingsClient(client_wrapper=self._client_wrapper)
        return self._network_settings

    @property
    def plans(self):
        if self._plans is None:
            from .plans.client import PlansClient

            self._plans = PlansClient(client_wrapper=self._client_wrapper)
        return self._plans

    @property
    def pool(self):
        if self._pool is None:
            from .pool.client import PoolClient

            self._pool = PoolClient(client_wrapper=self._client_wrapper)
        return self._pool

    @property
    def pool_group(self):
        if self._pool_group is None:
            from .pool_group.client import PoolGroupClient

            self._pool_group = PoolGroupClient(client_wrapper=self._client_wrapper)
        return self._pool_group

    @property
    def vm(self):
        if self._vm is None:
            from .vm.client import VmClient

            self._vm = VmClient(client_wrapper=self._client_wrapper)
        return self._vm

    @property
    def prebuilds_v(self):
        if self._prebuilds_v is None:
            from .prebuilds_v.client import PrebuildsVClient

            self._prebuilds_v = PrebuildsVClient(client_wrapper=self._client_wrapper)
        return self._prebuilds_v

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def netmon(self):
        if self._netmon is None:
            from .netmon.client import NetmonClient

            self._netmon = NetmonClient(client_wrapper=self._client_wrapper)
        return self._netmon

    @property
    def warmup(self):
        if self._warmup is None:
            from .warmup.client import WarmupClient

            self._warmup = WarmupClient(client_wrapper=self._client_wrapper)
        return self._warmup


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
        self._agent_telemetry: typing.Optional[AsyncAgentTelemetryClient] = None
        self._agents: typing.Optional[AsyncAgentsClient] = None
        self._environments: typing.Optional[AsyncEnvironmentsClient] = None
        self._billing: typing.Optional[AsyncBillingClient] = None
        self._configuration: typing.Optional[AsyncConfigurationClient] = None
        self._pools: typing.Optional[AsyncPoolsClient] = None
        self._prebuilds: typing.Optional[AsyncPrebuildsClient] = None
        self._privacy: typing.Optional[AsyncPrivacyClient] = None
        self._resources: typing.Optional[AsyncResourcesClient] = None
        self._vnet_pool_definitions: typing.Optional[AsyncVnetPoolDefinitionsClient] = None
        self._heart_beat: typing.Optional[AsyncHeartBeatClient] = None
        self._locations: typing.Optional[AsyncLocationsClient] = None
        self._sas: typing.Optional[AsyncSasClient] = None
        self._secrets: typing.Optional[AsyncSecretsClient] = None
        self._tenant: typing.Optional[AsyncTenantClient] = None
        self._tokens: typing.Optional[AsyncTokensClient] = None
        self._tunnel: typing.Optional[AsyncTunnelClient] = None
        self._user_subscriptions: typing.Optional[AsyncUserSubscriptionsClient] = None
        self._network_settings: typing.Optional[AsyncNetworkSettingsClient] = None
        self._plans: typing.Optional[AsyncPlansClient] = None
        self._pool: typing.Optional[AsyncPoolClient] = None
        self._pool_group: typing.Optional[AsyncPoolGroupClient] = None
        self._vm: typing.Optional[AsyncVmClient] = None
        self._prebuilds_v: typing.Optional[AsyncPrebuildsVClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None
        self._netmon: typing.Optional[AsyncNetmonClient] = None
        self._warmup: typing.Optional[AsyncWarmupClient] = None

    @property
    def agent_telemetry(self):
        if self._agent_telemetry is None:
            from .agent_telemetry.client import AsyncAgentTelemetryClient

            self._agent_telemetry = AsyncAgentTelemetryClient(client_wrapper=self._client_wrapper)
        return self._agent_telemetry

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AsyncAgentsClient

            self._agents = AsyncAgentsClient(client_wrapper=self._client_wrapper)
        return self._agents

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import AsyncEnvironmentsClient

            self._environments = AsyncEnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def billing(self):
        if self._billing is None:
            from .billing.client import AsyncBillingClient

            self._billing = AsyncBillingClient(client_wrapper=self._client_wrapper)
        return self._billing

    @property
    def configuration(self):
        if self._configuration is None:
            from .configuration.client import AsyncConfigurationClient

            self._configuration = AsyncConfigurationClient(client_wrapper=self._client_wrapper)
        return self._configuration

    @property
    def pools(self):
        if self._pools is None:
            from .pools.client import AsyncPoolsClient

            self._pools = AsyncPoolsClient(client_wrapper=self._client_wrapper)
        return self._pools

    @property
    def prebuilds(self):
        if self._prebuilds is None:
            from .prebuilds.client import AsyncPrebuildsClient

            self._prebuilds = AsyncPrebuildsClient(client_wrapper=self._client_wrapper)
        return self._prebuilds

    @property
    def privacy(self):
        if self._privacy is None:
            from .privacy.client import AsyncPrivacyClient

            self._privacy = AsyncPrivacyClient(client_wrapper=self._client_wrapper)
        return self._privacy

    @property
    def resources(self):
        if self._resources is None:
            from .resources.client import AsyncResourcesClient

            self._resources = AsyncResourcesClient(client_wrapper=self._client_wrapper)
        return self._resources

    @property
    def vnet_pool_definitions(self):
        if self._vnet_pool_definitions is None:
            from .vnet_pool_definitions.client import AsyncVnetPoolDefinitionsClient

            self._vnet_pool_definitions = AsyncVnetPoolDefinitionsClient(client_wrapper=self._client_wrapper)
        return self._vnet_pool_definitions

    @property
    def heart_beat(self):
        if self._heart_beat is None:
            from .heart_beat.client import AsyncHeartBeatClient

            self._heart_beat = AsyncHeartBeatClient(client_wrapper=self._client_wrapper)
        return self._heart_beat

    @property
    def locations(self):
        if self._locations is None:
            from .locations.client import AsyncLocationsClient

            self._locations = AsyncLocationsClient(client_wrapper=self._client_wrapper)
        return self._locations

    @property
    def sas(self):
        if self._sas is None:
            from .sas.client import AsyncSasClient

            self._sas = AsyncSasClient(client_wrapper=self._client_wrapper)
        return self._sas

    @property
    def secrets(self):
        if self._secrets is None:
            from .secrets.client import AsyncSecretsClient

            self._secrets = AsyncSecretsClient(client_wrapper=self._client_wrapper)
        return self._secrets

    @property
    def tenant(self):
        if self._tenant is None:
            from .tenant.client import AsyncTenantClient

            self._tenant = AsyncTenantClient(client_wrapper=self._client_wrapper)
        return self._tenant

    @property
    def tokens(self):
        if self._tokens is None:
            from .tokens.client import AsyncTokensClient

            self._tokens = AsyncTokensClient(client_wrapper=self._client_wrapper)
        return self._tokens

    @property
    def tunnel(self):
        if self._tunnel is None:
            from .tunnel.client import AsyncTunnelClient

            self._tunnel = AsyncTunnelClient(client_wrapper=self._client_wrapper)
        return self._tunnel

    @property
    def user_subscriptions(self):
        if self._user_subscriptions is None:
            from .user_subscriptions.client import AsyncUserSubscriptionsClient

            self._user_subscriptions = AsyncUserSubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._user_subscriptions

    @property
    def network_settings(self):
        if self._network_settings is None:
            from .network_settings.client import AsyncNetworkSettingsClient

            self._network_settings = AsyncNetworkSettingsClient(client_wrapper=self._client_wrapper)
        return self._network_settings

    @property
    def plans(self):
        if self._plans is None:
            from .plans.client import AsyncPlansClient

            self._plans = AsyncPlansClient(client_wrapper=self._client_wrapper)
        return self._plans

    @property
    def pool(self):
        if self._pool is None:
            from .pool.client import AsyncPoolClient

            self._pool = AsyncPoolClient(client_wrapper=self._client_wrapper)
        return self._pool

    @property
    def pool_group(self):
        if self._pool_group is None:
            from .pool_group.client import AsyncPoolGroupClient

            self._pool_group = AsyncPoolGroupClient(client_wrapper=self._client_wrapper)
        return self._pool_group

    @property
    def vm(self):
        if self._vm is None:
            from .vm.client import AsyncVmClient

            self._vm = AsyncVmClient(client_wrapper=self._client_wrapper)
        return self._vm

    @property
    def prebuilds_v(self):
        if self._prebuilds_v is None:
            from .prebuilds_v.client import AsyncPrebuildsVClient

            self._prebuilds_v = AsyncPrebuildsVClient(client_wrapper=self._client_wrapper)
        return self._prebuilds_v

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def netmon(self):
        if self._netmon is None:
            from .netmon.client import AsyncNetmonClient

            self._netmon = AsyncNetmonClient(client_wrapper=self._client_wrapper)
        return self._netmon

    @property
    def warmup(self):
        if self._warmup is None:
            from .warmup.client import AsyncWarmupClient

            self._warmup = AsyncWarmupClient(client_wrapper=self._client_wrapper)
        return self._warmup


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
