

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .access.client import AccessClient, AsyncAccessClient
    from .agent.client import AgentClient, AsyncAgentClient
    from .coap.client import AsyncCoapClient, CoapClient
    from .daemon.client import AsyncDaemonClient, DaemonClient
    from .dhcp.client import AsyncDhcpClient, DhcpClient
    from .ipmi.client import AsyncIpmiClient, IpmiClient
    from .mqtt.client import AsyncMqttClient, MqttClient
    from .netflow.client import AsyncNetflowClient, NetflowClient
    from .proxy.client import AsyncProxyClient, ProxyClient
    from .sflow.client import AsyncSflowClient, SflowClient
    from .snm_pv3.client import AsyncSnmPv3Client, SnmPv3Client
    from .snmptcp.client import AsyncSnmptcpClient, SnmptcpClient
    from .ssh.client import AsyncSshClient, SshClient
    from .syslog.client import AsyncSyslogClient, SyslogClient
    from .telnet.client import AsyncTelnetClient, TelnetClient
    from .tftp.client import AsyncTftpClient, TftpClient
    from .tod.client import AsyncTodClient, TodClient
    from .valuespace.client import AsyncValuespaceClient, ValuespaceClient
    from .web.client import AsyncWebClient, WebClient


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
        self._access: typing.Optional[AccessClient] = None
        self._agent: typing.Optional[AgentClient] = None
        self._coap: typing.Optional[CoapClient] = None
        self._dhcp: typing.Optional[DhcpClient] = None
        self._ipmi: typing.Optional[IpmiClient] = None
        self._mqtt: typing.Optional[MqttClient] = None
        self._netflow: typing.Optional[NetflowClient] = None
        self._proxy: typing.Optional[ProxyClient] = None
        self._sflow: typing.Optional[SflowClient] = None
        self._snmptcp: typing.Optional[SnmptcpClient] = None
        self._snm_pv3: typing.Optional[SnmPv3Client] = None
        self._ssh: typing.Optional[SshClient] = None
        self._syslog: typing.Optional[SyslogClient] = None
        self._telnet: typing.Optional[TelnetClient] = None
        self._tftp: typing.Optional[TftpClient] = None
        self._tod: typing.Optional[TodClient] = None
        self._web: typing.Optional[WebClient] = None
        self._valuespace: typing.Optional[ValuespaceClient] = None
        self._daemon: typing.Optional[DaemonClient] = None

    @property
    def access(self):
        if self._access is None:
            from .access.client import AccessClient

            self._access = AccessClient(client_wrapper=self._client_wrapper)
        return self._access

    @property
    def agent(self):
        if self._agent is None:
            from .agent.client import AgentClient

            self._agent = AgentClient(client_wrapper=self._client_wrapper)
        return self._agent

    @property
    def coap(self):
        if self._coap is None:
            from .coap.client import CoapClient

            self._coap = CoapClient(client_wrapper=self._client_wrapper)
        return self._coap

    @property
    def dhcp(self):
        if self._dhcp is None:
            from .dhcp.client import DhcpClient

            self._dhcp = DhcpClient(client_wrapper=self._client_wrapper)
        return self._dhcp

    @property
    def ipmi(self):
        if self._ipmi is None:
            from .ipmi.client import IpmiClient

            self._ipmi = IpmiClient(client_wrapper=self._client_wrapper)
        return self._ipmi

    @property
    def mqtt(self):
        if self._mqtt is None:
            from .mqtt.client import MqttClient

            self._mqtt = MqttClient(client_wrapper=self._client_wrapper)
        return self._mqtt

    @property
    def netflow(self):
        if self._netflow is None:
            from .netflow.client import NetflowClient

            self._netflow = NetflowClient(client_wrapper=self._client_wrapper)
        return self._netflow

    @property
    def proxy(self):
        if self._proxy is None:
            from .proxy.client import ProxyClient

            self._proxy = ProxyClient(client_wrapper=self._client_wrapper)
        return self._proxy

    @property
    def sflow(self):
        if self._sflow is None:
            from .sflow.client import SflowClient

            self._sflow = SflowClient(client_wrapper=self._client_wrapper)
        return self._sflow

    @property
    def snmptcp(self):
        if self._snmptcp is None:
            from .snmptcp.client import SnmptcpClient

            self._snmptcp = SnmptcpClient(client_wrapper=self._client_wrapper)
        return self._snmptcp

    @property
    def snm_pv3(self):
        if self._snm_pv3 is None:
            from .snm_pv3.client import SnmPv3Client

            self._snm_pv3 = SnmPv3Client(client_wrapper=self._client_wrapper)
        return self._snm_pv3

    @property
    def ssh(self):
        if self._ssh is None:
            from .ssh.client import SshClient

            self._ssh = SshClient(client_wrapper=self._client_wrapper)
        return self._ssh

    @property
    def syslog(self):
        if self._syslog is None:
            from .syslog.client import SyslogClient

            self._syslog = SyslogClient(client_wrapper=self._client_wrapper)
        return self._syslog

    @property
    def telnet(self):
        if self._telnet is None:
            from .telnet.client import TelnetClient

            self._telnet = TelnetClient(client_wrapper=self._client_wrapper)
        return self._telnet

    @property
    def tftp(self):
        if self._tftp is None:
            from .tftp.client import TftpClient

            self._tftp = TftpClient(client_wrapper=self._client_wrapper)
        return self._tftp

    @property
    def tod(self):
        if self._tod is None:
            from .tod.client import TodClient

            self._tod = TodClient(client_wrapper=self._client_wrapper)
        return self._tod

    @property
    def web(self):
        if self._web is None:
            from .web.client import WebClient

            self._web = WebClient(client_wrapper=self._client_wrapper)
        return self._web

    @property
    def valuespace(self):
        if self._valuespace is None:
            from .valuespace.client import ValuespaceClient

            self._valuespace = ValuespaceClient(client_wrapper=self._client_wrapper)
        return self._valuespace

    @property
    def daemon(self):
        if self._daemon is None:
            from .daemon.client import DaemonClient

            self._daemon = DaemonClient(client_wrapper=self._client_wrapper)
        return self._daemon


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
        self._access: typing.Optional[AsyncAccessClient] = None
        self._agent: typing.Optional[AsyncAgentClient] = None
        self._coap: typing.Optional[AsyncCoapClient] = None
        self._dhcp: typing.Optional[AsyncDhcpClient] = None
        self._ipmi: typing.Optional[AsyncIpmiClient] = None
        self._mqtt: typing.Optional[AsyncMqttClient] = None
        self._netflow: typing.Optional[AsyncNetflowClient] = None
        self._proxy: typing.Optional[AsyncProxyClient] = None
        self._sflow: typing.Optional[AsyncSflowClient] = None
        self._snmptcp: typing.Optional[AsyncSnmptcpClient] = None
        self._snm_pv3: typing.Optional[AsyncSnmPv3Client] = None
        self._ssh: typing.Optional[AsyncSshClient] = None
        self._syslog: typing.Optional[AsyncSyslogClient] = None
        self._telnet: typing.Optional[AsyncTelnetClient] = None
        self._tftp: typing.Optional[AsyncTftpClient] = None
        self._tod: typing.Optional[AsyncTodClient] = None
        self._web: typing.Optional[AsyncWebClient] = None
        self._valuespace: typing.Optional[AsyncValuespaceClient] = None
        self._daemon: typing.Optional[AsyncDaemonClient] = None

    @property
    def access(self):
        if self._access is None:
            from .access.client import AsyncAccessClient

            self._access = AsyncAccessClient(client_wrapper=self._client_wrapper)
        return self._access

    @property
    def agent(self):
        if self._agent is None:
            from .agent.client import AsyncAgentClient

            self._agent = AsyncAgentClient(client_wrapper=self._client_wrapper)
        return self._agent

    @property
    def coap(self):
        if self._coap is None:
            from .coap.client import AsyncCoapClient

            self._coap = AsyncCoapClient(client_wrapper=self._client_wrapper)
        return self._coap

    @property
    def dhcp(self):
        if self._dhcp is None:
            from .dhcp.client import AsyncDhcpClient

            self._dhcp = AsyncDhcpClient(client_wrapper=self._client_wrapper)
        return self._dhcp

    @property
    def ipmi(self):
        if self._ipmi is None:
            from .ipmi.client import AsyncIpmiClient

            self._ipmi = AsyncIpmiClient(client_wrapper=self._client_wrapper)
        return self._ipmi

    @property
    def mqtt(self):
        if self._mqtt is None:
            from .mqtt.client import AsyncMqttClient

            self._mqtt = AsyncMqttClient(client_wrapper=self._client_wrapper)
        return self._mqtt

    @property
    def netflow(self):
        if self._netflow is None:
            from .netflow.client import AsyncNetflowClient

            self._netflow = AsyncNetflowClient(client_wrapper=self._client_wrapper)
        return self._netflow

    @property
    def proxy(self):
        if self._proxy is None:
            from .proxy.client import AsyncProxyClient

            self._proxy = AsyncProxyClient(client_wrapper=self._client_wrapper)
        return self._proxy

    @property
    def sflow(self):
        if self._sflow is None:
            from .sflow.client import AsyncSflowClient

            self._sflow = AsyncSflowClient(client_wrapper=self._client_wrapper)
        return self._sflow

    @property
    def snmptcp(self):
        if self._snmptcp is None:
            from .snmptcp.client import AsyncSnmptcpClient

            self._snmptcp = AsyncSnmptcpClient(client_wrapper=self._client_wrapper)
        return self._snmptcp

    @property
    def snm_pv3(self):
        if self._snm_pv3 is None:
            from .snm_pv3.client import AsyncSnmPv3Client

            self._snm_pv3 = AsyncSnmPv3Client(client_wrapper=self._client_wrapper)
        return self._snm_pv3

    @property
    def ssh(self):
        if self._ssh is None:
            from .ssh.client import AsyncSshClient

            self._ssh = AsyncSshClient(client_wrapper=self._client_wrapper)
        return self._ssh

    @property
    def syslog(self):
        if self._syslog is None:
            from .syslog.client import AsyncSyslogClient

            self._syslog = AsyncSyslogClient(client_wrapper=self._client_wrapper)
        return self._syslog

    @property
    def telnet(self):
        if self._telnet is None:
            from .telnet.client import AsyncTelnetClient

            self._telnet = AsyncTelnetClient(client_wrapper=self._client_wrapper)
        return self._telnet

    @property
    def tftp(self):
        if self._tftp is None:
            from .tftp.client import AsyncTftpClient

            self._tftp = AsyncTftpClient(client_wrapper=self._client_wrapper)
        return self._tftp

    @property
    def tod(self):
        if self._tod is None:
            from .tod.client import AsyncTodClient

            self._tod = AsyncTodClient(client_wrapper=self._client_wrapper)
        return self._tod

    @property
    def web(self):
        if self._web is None:
            from .web.client import AsyncWebClient

            self._web = AsyncWebClient(client_wrapper=self._client_wrapper)
        return self._web

    @property
    def valuespace(self):
        if self._valuespace is None:
            from .valuespace.client import AsyncValuespaceClient

            self._valuespace = AsyncValuespaceClient(client_wrapper=self._client_wrapper)
        return self._valuespace

    @property
    def daemon(self):
        if self._daemon is None:
            from .daemon.client import AsyncDaemonClient

            self._daemon = AsyncDaemonClient(client_wrapper=self._client_wrapper)
        return self._daemon


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
