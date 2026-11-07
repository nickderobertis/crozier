

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .alerting.client import AlertingClient, AsyncAlertingClient
    from .catalog_resource.client import AsyncCatalogResourceClient, CatalogResourceClient
    from .connections.client import AsyncConnectionsClient, ConnectionsClient
    from .destinations.client import AsyncDestinationsClient, DestinationsClient
    from .monitoring.client import AsyncMonitoringClient, MonitoringClient
    from .pipelines.client import AsyncPipelinesClient, PipelinesClient
    from .sources.client import AsyncSourcesClient, SourcesClient
    from .transforms.client import AsyncTransformsClient, TransformsClient
    from .vaults.client import AsyncVaultsClient, VaultsClient


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
        self._alerting: typing.Optional[AlertingClient] = None
        self._catalog_resource: typing.Optional[CatalogResourceClient] = None
        self._connections: typing.Optional[ConnectionsClient] = None
        self._destinations: typing.Optional[DestinationsClient] = None
        self._monitoring: typing.Optional[MonitoringClient] = None
        self._pipelines: typing.Optional[PipelinesClient] = None
        self._sources: typing.Optional[SourcesClient] = None
        self._transforms: typing.Optional[TransformsClient] = None
        self._vaults: typing.Optional[VaultsClient] = None

    @property
    def alerting(self):
        if self._alerting is None:
            from .alerting.client import AlertingClient

            self._alerting = AlertingClient(client_wrapper=self._client_wrapper)
        return self._alerting

    @property
    def catalog_resource(self):
        if self._catalog_resource is None:
            from .catalog_resource.client import CatalogResourceClient

            self._catalog_resource = CatalogResourceClient(client_wrapper=self._client_wrapper)
        return self._catalog_resource

    @property
    def connections(self):
        if self._connections is None:
            from .connections.client import ConnectionsClient

            self._connections = ConnectionsClient(client_wrapper=self._client_wrapper)
        return self._connections

    @property
    def destinations(self):
        if self._destinations is None:
            from .destinations.client import DestinationsClient

            self._destinations = DestinationsClient(client_wrapper=self._client_wrapper)
        return self._destinations

    @property
    def monitoring(self):
        if self._monitoring is None:
            from .monitoring.client import MonitoringClient

            self._monitoring = MonitoringClient(client_wrapper=self._client_wrapper)
        return self._monitoring

    @property
    def pipelines(self):
        if self._pipelines is None:
            from .pipelines.client import PipelinesClient

            self._pipelines = PipelinesClient(client_wrapper=self._client_wrapper)
        return self._pipelines

    @property
    def sources(self):
        if self._sources is None:
            from .sources.client import SourcesClient

            self._sources = SourcesClient(client_wrapper=self._client_wrapper)
        return self._sources

    @property
    def transforms(self):
        if self._transforms is None:
            from .transforms.client import TransformsClient

            self._transforms = TransformsClient(client_wrapper=self._client_wrapper)
        return self._transforms

    @property
    def vaults(self):
        if self._vaults is None:
            from .vaults.client import VaultsClient

            self._vaults = VaultsClient(client_wrapper=self._client_wrapper)
        return self._vaults


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
        self._alerting: typing.Optional[AsyncAlertingClient] = None
        self._catalog_resource: typing.Optional[AsyncCatalogResourceClient] = None
        self._connections: typing.Optional[AsyncConnectionsClient] = None
        self._destinations: typing.Optional[AsyncDestinationsClient] = None
        self._monitoring: typing.Optional[AsyncMonitoringClient] = None
        self._pipelines: typing.Optional[AsyncPipelinesClient] = None
        self._sources: typing.Optional[AsyncSourcesClient] = None
        self._transforms: typing.Optional[AsyncTransformsClient] = None
        self._vaults: typing.Optional[AsyncVaultsClient] = None

    @property
    def alerting(self):
        if self._alerting is None:
            from .alerting.client import AsyncAlertingClient

            self._alerting = AsyncAlertingClient(client_wrapper=self._client_wrapper)
        return self._alerting

    @property
    def catalog_resource(self):
        if self._catalog_resource is None:
            from .catalog_resource.client import AsyncCatalogResourceClient

            self._catalog_resource = AsyncCatalogResourceClient(client_wrapper=self._client_wrapper)
        return self._catalog_resource

    @property
    def connections(self):
        if self._connections is None:
            from .connections.client import AsyncConnectionsClient

            self._connections = AsyncConnectionsClient(client_wrapper=self._client_wrapper)
        return self._connections

    @property
    def destinations(self):
        if self._destinations is None:
            from .destinations.client import AsyncDestinationsClient

            self._destinations = AsyncDestinationsClient(client_wrapper=self._client_wrapper)
        return self._destinations

    @property
    def monitoring(self):
        if self._monitoring is None:
            from .monitoring.client import AsyncMonitoringClient

            self._monitoring = AsyncMonitoringClient(client_wrapper=self._client_wrapper)
        return self._monitoring

    @property
    def pipelines(self):
        if self._pipelines is None:
            from .pipelines.client import AsyncPipelinesClient

            self._pipelines = AsyncPipelinesClient(client_wrapper=self._client_wrapper)
        return self._pipelines

    @property
    def sources(self):
        if self._sources is None:
            from .sources.client import AsyncSourcesClient

            self._sources = AsyncSourcesClient(client_wrapper=self._client_wrapper)
        return self._sources

    @property
    def transforms(self):
        if self._transforms is None:
            from .transforms.client import AsyncTransformsClient

            self._transforms = AsyncTransformsClient(client_wrapper=self._client_wrapper)
        return self._transforms

    @property
    def vaults(self):
        if self._vaults is None:
            from .vaults.client import AsyncVaultsClient

            self._vaults = AsyncVaultsClient(client_wrapper=self._client_wrapper)
        return self._vaults


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
