

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .actions.client import ActionsClient, AsyncActionsClient
    from .ethernet.client import AsyncEthernetClient, EthernetClient
    from .general.client import AsyncGeneralClient, GeneralClient
    from .maintenance.client import AsyncMaintenanceClient, MaintenanceClient
    from .measurements.client import AsyncMeasurementsClient, MeasurementsClient
    from .sd_card.client import AsyncSdCardClient, SdCardClient
    from .settings.client import AsyncSettingsClient, SettingsClient
    from .streaming.client import AsyncStreamingClient, StreamingClient
    from .wi_fi.client import AsyncWiFiClient, WiFiClient


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
        self._general: typing.Optional[GeneralClient] = None
        self._measurements: typing.Optional[MeasurementsClient] = None
        self._streaming: typing.Optional[StreamingClient] = None
        self._settings: typing.Optional[SettingsClient] = None
        self._maintenance: typing.Optional[MaintenanceClient] = None
        self._wi_fi: typing.Optional[WiFiClient] = None
        self._ethernet: typing.Optional[EthernetClient] = None
        self._actions: typing.Optional[ActionsClient] = None
        self._sd_card: typing.Optional[SdCardClient] = None

    @property
    def general(self):
        if self._general is None:
            from .general.client import GeneralClient

            self._general = GeneralClient(client_wrapper=self._client_wrapper)
        return self._general

    @property
    def measurements(self):
        if self._measurements is None:
            from .measurements.client import MeasurementsClient

            self._measurements = MeasurementsClient(client_wrapper=self._client_wrapper)
        return self._measurements

    @property
    def streaming(self):
        if self._streaming is None:
            from .streaming.client import StreamingClient

            self._streaming = StreamingClient(client_wrapper=self._client_wrapper)
        return self._streaming

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import SettingsClient

            self._settings = SettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import MaintenanceClient

            self._maintenance = MaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance

    @property
    def wi_fi(self):
        if self._wi_fi is None:
            from .wi_fi.client import WiFiClient

            self._wi_fi = WiFiClient(client_wrapper=self._client_wrapper)
        return self._wi_fi

    @property
    def ethernet(self):
        if self._ethernet is None:
            from .ethernet.client import EthernetClient

            self._ethernet = EthernetClient(client_wrapper=self._client_wrapper)
        return self._ethernet

    @property
    def actions(self):
        if self._actions is None:
            from .actions.client import ActionsClient

            self._actions = ActionsClient(client_wrapper=self._client_wrapper)
        return self._actions

    @property
    def sd_card(self):
        if self._sd_card is None:
            from .sd_card.client import SdCardClient

            self._sd_card = SdCardClient(client_wrapper=self._client_wrapper)
        return self._sd_card


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
        self._general: typing.Optional[AsyncGeneralClient] = None
        self._measurements: typing.Optional[AsyncMeasurementsClient] = None
        self._streaming: typing.Optional[AsyncStreamingClient] = None
        self._settings: typing.Optional[AsyncSettingsClient] = None
        self._maintenance: typing.Optional[AsyncMaintenanceClient] = None
        self._wi_fi: typing.Optional[AsyncWiFiClient] = None
        self._ethernet: typing.Optional[AsyncEthernetClient] = None
        self._actions: typing.Optional[AsyncActionsClient] = None
        self._sd_card: typing.Optional[AsyncSdCardClient] = None

    @property
    def general(self):
        if self._general is None:
            from .general.client import AsyncGeneralClient

            self._general = AsyncGeneralClient(client_wrapper=self._client_wrapper)
        return self._general

    @property
    def measurements(self):
        if self._measurements is None:
            from .measurements.client import AsyncMeasurementsClient

            self._measurements = AsyncMeasurementsClient(client_wrapper=self._client_wrapper)
        return self._measurements

    @property
    def streaming(self):
        if self._streaming is None:
            from .streaming.client import AsyncStreamingClient

            self._streaming = AsyncStreamingClient(client_wrapper=self._client_wrapper)
        return self._streaming

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import AsyncSettingsClient

            self._settings = AsyncSettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def maintenance(self):
        if self._maintenance is None:
            from .maintenance.client import AsyncMaintenanceClient

            self._maintenance = AsyncMaintenanceClient(client_wrapper=self._client_wrapper)
        return self._maintenance

    @property
    def wi_fi(self):
        if self._wi_fi is None:
            from .wi_fi.client import AsyncWiFiClient

            self._wi_fi = AsyncWiFiClient(client_wrapper=self._client_wrapper)
        return self._wi_fi

    @property
    def ethernet(self):
        if self._ethernet is None:
            from .ethernet.client import AsyncEthernetClient

            self._ethernet = AsyncEthernetClient(client_wrapper=self._client_wrapper)
        return self._ethernet

    @property
    def actions(self):
        if self._actions is None:
            from .actions.client import AsyncActionsClient

            self._actions = AsyncActionsClient(client_wrapper=self._client_wrapper)
        return self._actions

    @property
    def sd_card(self):
        if self._sd_card is None:
            from .sd_card.client import AsyncSdCardClient

            self._sd_card = AsyncSdCardClient(client_wrapper=self._client_wrapper)
        return self._sd_card


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
