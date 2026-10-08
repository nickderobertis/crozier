

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .connectors_connect_v1.client import AsyncConnectorsConnectV1Client, ConnectorsConnectV1Client
    from .lifecycle_connect_v1.client import AsyncLifecycleConnectV1Client, LifecycleConnectV1Client
    from .managed_connector_plugins_connect_v1.client import (
        AsyncManagedConnectorPluginsConnectV1Client,
        ManagedConnectorPluginsConnectV1Client,
    )
    from .offsets_connect_v1.client import AsyncOffsetsConnectV1Client, OffsetsConnectV1Client
    from .status_connect_v1.client import AsyncStatusConnectV1Client, StatusConnectV1Client


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
        self._connectors_connect_v1: typing.Optional[ConnectorsConnectV1Client] = None
        self._lifecycle_connect_v1: typing.Optional[LifecycleConnectV1Client] = None
        self._status_connect_v1: typing.Optional[StatusConnectV1Client] = None
        self._managed_connector_plugins_connect_v1: typing.Optional[ManagedConnectorPluginsConnectV1Client] = None
        self._offsets_connect_v1: typing.Optional[OffsetsConnectV1Client] = None

    @property
    def connectors_connect_v1(self):
        if self._connectors_connect_v1 is None:
            from .connectors_connect_v1.client import ConnectorsConnectV1Client

            self._connectors_connect_v1 = ConnectorsConnectV1Client(client_wrapper=self._client_wrapper)
        return self._connectors_connect_v1

    @property
    def lifecycle_connect_v1(self):
        if self._lifecycle_connect_v1 is None:
            from .lifecycle_connect_v1.client import LifecycleConnectV1Client

            self._lifecycle_connect_v1 = LifecycleConnectV1Client(client_wrapper=self._client_wrapper)
        return self._lifecycle_connect_v1

    @property
    def status_connect_v1(self):
        if self._status_connect_v1 is None:
            from .status_connect_v1.client import StatusConnectV1Client

            self._status_connect_v1 = StatusConnectV1Client(client_wrapper=self._client_wrapper)
        return self._status_connect_v1

    @property
    def managed_connector_plugins_connect_v1(self):
        if self._managed_connector_plugins_connect_v1 is None:
            from .managed_connector_plugins_connect_v1.client import (
                ManagedConnectorPluginsConnectV1Client,
            )

            self._managed_connector_plugins_connect_v1 = ManagedConnectorPluginsConnectV1Client(
                client_wrapper=self._client_wrapper
            )
        return self._managed_connector_plugins_connect_v1

    @property
    def offsets_connect_v1(self):
        if self._offsets_connect_v1 is None:
            from .offsets_connect_v1.client import OffsetsConnectV1Client

            self._offsets_connect_v1 = OffsetsConnectV1Client(client_wrapper=self._client_wrapper)
        return self._offsets_connect_v1


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
        self._connectors_connect_v1: typing.Optional[AsyncConnectorsConnectV1Client] = None
        self._lifecycle_connect_v1: typing.Optional[AsyncLifecycleConnectV1Client] = None
        self._status_connect_v1: typing.Optional[AsyncStatusConnectV1Client] = None
        self._managed_connector_plugins_connect_v1: typing.Optional[AsyncManagedConnectorPluginsConnectV1Client] = None
        self._offsets_connect_v1: typing.Optional[AsyncOffsetsConnectV1Client] = None

    @property
    def connectors_connect_v1(self):
        if self._connectors_connect_v1 is None:
            from .connectors_connect_v1.client import AsyncConnectorsConnectV1Client

            self._connectors_connect_v1 = AsyncConnectorsConnectV1Client(client_wrapper=self._client_wrapper)
        return self._connectors_connect_v1

    @property
    def lifecycle_connect_v1(self):
        if self._lifecycle_connect_v1 is None:
            from .lifecycle_connect_v1.client import AsyncLifecycleConnectV1Client

            self._lifecycle_connect_v1 = AsyncLifecycleConnectV1Client(client_wrapper=self._client_wrapper)
        return self._lifecycle_connect_v1

    @property
    def status_connect_v1(self):
        if self._status_connect_v1 is None:
            from .status_connect_v1.client import AsyncStatusConnectV1Client

            self._status_connect_v1 = AsyncStatusConnectV1Client(client_wrapper=self._client_wrapper)
        return self._status_connect_v1

    @property
    def managed_connector_plugins_connect_v1(self):
        if self._managed_connector_plugins_connect_v1 is None:
            from .managed_connector_plugins_connect_v1.client import (
                AsyncManagedConnectorPluginsConnectV1Client,
            )

            self._managed_connector_plugins_connect_v1 = AsyncManagedConnectorPluginsConnectV1Client(
                client_wrapper=self._client_wrapper
            )
        return self._managed_connector_plugins_connect_v1

    @property
    def offsets_connect_v1(self):
        if self._offsets_connect_v1 is None:
            from .offsets_connect_v1.client import AsyncOffsetsConnectV1Client

            self._offsets_connect_v1 = AsyncOffsetsConnectV1Client(client_wrapper=self._client_wrapper)
        return self._offsets_connect_v1


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
