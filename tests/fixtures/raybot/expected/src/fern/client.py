

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .alarms.client import AlarmsClient, AsyncAlarmsClient
    from .commands.client import AsyncCommandsClient, CommandsClient
    from .config.client import AsyncConfigClient, ConfigClient
    from .error_codes.client import AsyncErrorCodesClient, ErrorCodesClient
    from .health.client import AsyncHealthClient, HealthClient
    from .peripherals.client import AsyncPeripheralsClient, PeripheralsClient
    from .robot_state.client import AsyncRobotStateClient, RobotStateClient
    from .state.client import AsyncStateClient, StateClient
    from .system.client import AsyncSystemClient, SystemClient
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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._version: typing.Optional[VersionClient] = None
        self._health: typing.Optional[HealthClient] = None
        self._error_codes: typing.Optional[ErrorCodesClient] = None
        self._config: typing.Optional[ConfigClient] = None
        self._system: typing.Optional[SystemClient] = None
        self._robot_state: typing.Optional[RobotStateClient] = None
        self._state: typing.Optional[StateClient] = None
        self._peripherals: typing.Optional[PeripheralsClient] = None
        self._commands: typing.Optional[CommandsClient] = None
        self._alarms: typing.Optional[AlarmsClient] = None

    @property
    def version(self):
        if self._version is None:
            from .version.client import VersionClient

            self._version = VersionClient(client_wrapper=self._client_wrapper)
        return self._version

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def error_codes(self):
        if self._error_codes is None:
            from .error_codes.client import ErrorCodesClient

            self._error_codes = ErrorCodesClient(client_wrapper=self._client_wrapper)
        return self._error_codes

    @property
    def config(self):
        if self._config is None:
            from .config.client import ConfigClient

            self._config = ConfigClient(client_wrapper=self._client_wrapper)
        return self._config

    @property
    def system(self):
        if self._system is None:
            from .system.client import SystemClient

            self._system = SystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def robot_state(self):
        if self._robot_state is None:
            from .robot_state.client import RobotStateClient

            self._robot_state = RobotStateClient(client_wrapper=self._client_wrapper)
        return self._robot_state

    @property
    def state(self):
        if self._state is None:
            from .state.client import StateClient

            self._state = StateClient(client_wrapper=self._client_wrapper)
        return self._state

    @property
    def peripherals(self):
        if self._peripherals is None:
            from .peripherals.client import PeripheralsClient

            self._peripherals = PeripheralsClient(client_wrapper=self._client_wrapper)
        return self._peripherals

    @property
    def commands(self):
        if self._commands is None:
            from .commands.client import CommandsClient

            self._commands = CommandsClient(client_wrapper=self._client_wrapper)
        return self._commands

    @property
    def alarms(self):
        if self._alarms is None:
            from .alarms.client import AlarmsClient

            self._alarms = AlarmsClient(client_wrapper=self._client_wrapper)
        return self._alarms


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

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._version: typing.Optional[AsyncVersionClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None
        self._error_codes: typing.Optional[AsyncErrorCodesClient] = None
        self._config: typing.Optional[AsyncConfigClient] = None
        self._system: typing.Optional[AsyncSystemClient] = None
        self._robot_state: typing.Optional[AsyncRobotStateClient] = None
        self._state: typing.Optional[AsyncStateClient] = None
        self._peripherals: typing.Optional[AsyncPeripheralsClient] = None
        self._commands: typing.Optional[AsyncCommandsClient] = None
        self._alarms: typing.Optional[AsyncAlarmsClient] = None

    @property
    def version(self):
        if self._version is None:
            from .version.client import AsyncVersionClient

            self._version = AsyncVersionClient(client_wrapper=self._client_wrapper)
        return self._version

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def error_codes(self):
        if self._error_codes is None:
            from .error_codes.client import AsyncErrorCodesClient

            self._error_codes = AsyncErrorCodesClient(client_wrapper=self._client_wrapper)
        return self._error_codes

    @property
    def config(self):
        if self._config is None:
            from .config.client import AsyncConfigClient

            self._config = AsyncConfigClient(client_wrapper=self._client_wrapper)
        return self._config

    @property
    def system(self):
        if self._system is None:
            from .system.client import AsyncSystemClient

            self._system = AsyncSystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def robot_state(self):
        if self._robot_state is None:
            from .robot_state.client import AsyncRobotStateClient

            self._robot_state = AsyncRobotStateClient(client_wrapper=self._client_wrapper)
        return self._robot_state

    @property
    def state(self):
        if self._state is None:
            from .state.client import AsyncStateClient

            self._state = AsyncStateClient(client_wrapper=self._client_wrapper)
        return self._state

    @property
    def peripherals(self):
        if self._peripherals is None:
            from .peripherals.client import AsyncPeripheralsClient

            self._peripherals = AsyncPeripheralsClient(client_wrapper=self._client_wrapper)
        return self._peripherals

    @property
    def commands(self):
        if self._commands is None:
            from .commands.client import AsyncCommandsClient

            self._commands = AsyncCommandsClient(client_wrapper=self._client_wrapper)
        return self._commands

    @property
    def alarms(self):
        if self._alarms is None:
            from .alarms.client import AsyncAlarmsClient

            self._alarms = AsyncAlarmsClient(client_wrapper=self._client_wrapper)
        return self._alarms


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
