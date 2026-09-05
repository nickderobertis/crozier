

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .bandwidth_allocations.client import AsyncBandwidthAllocationsClient, BandwidthAllocationsClient
    from .ike_crypto_profiles.client import AsyncIkeCryptoProfilesClient, IkeCryptoProfilesClient
    from .ike_gateway.client import AsyncIkeGatewayClient, IkeGatewayClient
    from .ip_sec_crypto_profiles.client import AsyncIpSecCryptoProfilesClient, IpSecCryptoProfilesClient
    from .location_information.client import AsyncLocationInformationClient, LocationInformationClient
    from .remote_networks.client import AsyncRemoteNetworksClient, RemoteNetworksClient


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
        self._bandwidth_allocations: typing.Optional[BandwidthAllocationsClient] = None
        self._ike_crypto_profiles: typing.Optional[IkeCryptoProfilesClient] = None
        self._ike_gateway: typing.Optional[IkeGatewayClient] = None
        self._ip_sec_crypto_profiles: typing.Optional[IpSecCryptoProfilesClient] = None
        self._location_information: typing.Optional[LocationInformationClient] = None
        self._remote_networks: typing.Optional[RemoteNetworksClient] = None

    @property
    def bandwidth_allocations(self):
        if self._bandwidth_allocations is None:
            from .bandwidth_allocations.client import BandwidthAllocationsClient

            self._bandwidth_allocations = BandwidthAllocationsClient(client_wrapper=self._client_wrapper)
        return self._bandwidth_allocations

    @property
    def ike_crypto_profiles(self):
        if self._ike_crypto_profiles is None:
            from .ike_crypto_profiles.client import IkeCryptoProfilesClient

            self._ike_crypto_profiles = IkeCryptoProfilesClient(client_wrapper=self._client_wrapper)
        return self._ike_crypto_profiles

    @property
    def ike_gateway(self):
        if self._ike_gateway is None:
            from .ike_gateway.client import IkeGatewayClient

            self._ike_gateway = IkeGatewayClient(client_wrapper=self._client_wrapper)
        return self._ike_gateway

    @property
    def ip_sec_crypto_profiles(self):
        if self._ip_sec_crypto_profiles is None:
            from .ip_sec_crypto_profiles.client import IpSecCryptoProfilesClient

            self._ip_sec_crypto_profiles = IpSecCryptoProfilesClient(client_wrapper=self._client_wrapper)
        return self._ip_sec_crypto_profiles

    @property
    def location_information(self):
        if self._location_information is None:
            from .location_information.client import LocationInformationClient

            self._location_information = LocationInformationClient(client_wrapper=self._client_wrapper)
        return self._location_information

    @property
    def remote_networks(self):
        if self._remote_networks is None:
            from .remote_networks.client import RemoteNetworksClient

            self._remote_networks = RemoteNetworksClient(client_wrapper=self._client_wrapper)
        return self._remote_networks


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
        self._bandwidth_allocations: typing.Optional[AsyncBandwidthAllocationsClient] = None
        self._ike_crypto_profiles: typing.Optional[AsyncIkeCryptoProfilesClient] = None
        self._ike_gateway: typing.Optional[AsyncIkeGatewayClient] = None
        self._ip_sec_crypto_profiles: typing.Optional[AsyncIpSecCryptoProfilesClient] = None
        self._location_information: typing.Optional[AsyncLocationInformationClient] = None
        self._remote_networks: typing.Optional[AsyncRemoteNetworksClient] = None

    @property
    def bandwidth_allocations(self):
        if self._bandwidth_allocations is None:
            from .bandwidth_allocations.client import AsyncBandwidthAllocationsClient

            self._bandwidth_allocations = AsyncBandwidthAllocationsClient(client_wrapper=self._client_wrapper)
        return self._bandwidth_allocations

    @property
    def ike_crypto_profiles(self):
        if self._ike_crypto_profiles is None:
            from .ike_crypto_profiles.client import AsyncIkeCryptoProfilesClient

            self._ike_crypto_profiles = AsyncIkeCryptoProfilesClient(client_wrapper=self._client_wrapper)
        return self._ike_crypto_profiles

    @property
    def ike_gateway(self):
        if self._ike_gateway is None:
            from .ike_gateway.client import AsyncIkeGatewayClient

            self._ike_gateway = AsyncIkeGatewayClient(client_wrapper=self._client_wrapper)
        return self._ike_gateway

    @property
    def ip_sec_crypto_profiles(self):
        if self._ip_sec_crypto_profiles is None:
            from .ip_sec_crypto_profiles.client import AsyncIpSecCryptoProfilesClient

            self._ip_sec_crypto_profiles = AsyncIpSecCryptoProfilesClient(client_wrapper=self._client_wrapper)
        return self._ip_sec_crypto_profiles

    @property
    def location_information(self):
        if self._location_information is None:
            from .location_information.client import AsyncLocationInformationClient

            self._location_information = AsyncLocationInformationClient(client_wrapper=self._client_wrapper)
        return self._location_information

    @property
    def remote_networks(self):
        if self._remote_networks is None:
            from .remote_networks.client import AsyncRemoteNetworksClient

            self._remote_networks = AsyncRemoteNetworksClient(client_wrapper=self._client_wrapper)
        return self._remote_networks


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
