

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .circuits.client import AsyncCircuitsClient, CircuitsClient
    from .dcim.client import AsyncDcimClient, DcimClient
    from .extras.client import AsyncExtrasClient, ExtrasClient
    from .ipam.client import AsyncIpamClient, IpamClient
    from .status.client import AsyncStatusClient, StatusClient
    from .tenancy.client import AsyncTenancyClient, TenancyClient
    from .users.client import AsyncUsersClient, UsersClient
    from .virtualization.client import AsyncVirtualizationClient, VirtualizationClient
    from .wireless.client import AsyncWirelessClient, WirelessClient


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



    api_key : str
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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            api_key=api_key,
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
        self._circuits: typing.Optional[CircuitsClient] = None
        self._dcim: typing.Optional[DcimClient] = None
        self._extras: typing.Optional[ExtrasClient] = None
        self._ipam: typing.Optional[IpamClient] = None
        self._status: typing.Optional[StatusClient] = None
        self._tenancy: typing.Optional[TenancyClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._virtualization: typing.Optional[VirtualizationClient] = None
        self._wireless: typing.Optional[WirelessClient] = None

    @property
    def circuits(self):
        if self._circuits is None:
            from .circuits.client import CircuitsClient

            self._circuits = CircuitsClient(client_wrapper=self._client_wrapper)
        return self._circuits

    @property
    def dcim(self):
        if self._dcim is None:
            from .dcim.client import DcimClient

            self._dcim = DcimClient(client_wrapper=self._client_wrapper)
        return self._dcim

    @property
    def extras(self):
        if self._extras is None:
            from .extras.client import ExtrasClient

            self._extras = ExtrasClient(client_wrapper=self._client_wrapper)
        return self._extras

    @property
    def ipam(self):
        if self._ipam is None:
            from .ipam.client import IpamClient

            self._ipam = IpamClient(client_wrapper=self._client_wrapper)
        return self._ipam

    @property
    def status(self):
        if self._status is None:
            from .status.client import StatusClient

            self._status = StatusClient(client_wrapper=self._client_wrapper)
        return self._status

    @property
    def tenancy(self):
        if self._tenancy is None:
            from .tenancy.client import TenancyClient

            self._tenancy = TenancyClient(client_wrapper=self._client_wrapper)
        return self._tenancy

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def virtualization(self):
        if self._virtualization is None:
            from .virtualization.client import VirtualizationClient

            self._virtualization = VirtualizationClient(client_wrapper=self._client_wrapper)
        return self._virtualization

    @property
    def wireless(self):
        if self._wireless is None:
            from .wireless.client import WirelessClient

            self._wireless = WirelessClient(client_wrapper=self._client_wrapper)
        return self._wireless


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



    api_key : str
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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            api_key=api_key,
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
        self._circuits: typing.Optional[AsyncCircuitsClient] = None
        self._dcim: typing.Optional[AsyncDcimClient] = None
        self._extras: typing.Optional[AsyncExtrasClient] = None
        self._ipam: typing.Optional[AsyncIpamClient] = None
        self._status: typing.Optional[AsyncStatusClient] = None
        self._tenancy: typing.Optional[AsyncTenancyClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._virtualization: typing.Optional[AsyncVirtualizationClient] = None
        self._wireless: typing.Optional[AsyncWirelessClient] = None

    @property
    def circuits(self):
        if self._circuits is None:
            from .circuits.client import AsyncCircuitsClient

            self._circuits = AsyncCircuitsClient(client_wrapper=self._client_wrapper)
        return self._circuits

    @property
    def dcim(self):
        if self._dcim is None:
            from .dcim.client import AsyncDcimClient

            self._dcim = AsyncDcimClient(client_wrapper=self._client_wrapper)
        return self._dcim

    @property
    def extras(self):
        if self._extras is None:
            from .extras.client import AsyncExtrasClient

            self._extras = AsyncExtrasClient(client_wrapper=self._client_wrapper)
        return self._extras

    @property
    def ipam(self):
        if self._ipam is None:
            from .ipam.client import AsyncIpamClient

            self._ipam = AsyncIpamClient(client_wrapper=self._client_wrapper)
        return self._ipam

    @property
    def status(self):
        if self._status is None:
            from .status.client import AsyncStatusClient

            self._status = AsyncStatusClient(client_wrapper=self._client_wrapper)
        return self._status

    @property
    def tenancy(self):
        if self._tenancy is None:
            from .tenancy.client import AsyncTenancyClient

            self._tenancy = AsyncTenancyClient(client_wrapper=self._client_wrapper)
        return self._tenancy

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def virtualization(self):
        if self._virtualization is None:
            from .virtualization.client import AsyncVirtualizationClient

            self._virtualization = AsyncVirtualizationClient(client_wrapper=self._client_wrapper)
        return self._virtualization

    @property
    def wireless(self):
        if self._wireless is None:
            from .wireless.client import AsyncWirelessClient

            self._wireless = AsyncWirelessClient(client_wrapper=self._client_wrapper)
        return self._wireless


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
