

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .ai.client import AiClient, AsyncAiClient
    from .aigateway.client import AigatewayClient, AsyncAigatewayClient
    from .application.client import ApplicationClient, AsyncApplicationClient
    from .auditlog.client import AsyncAuditlogClient, AuditlogClient
    from .billing.client import AsyncBillingClient, BillingClient
    from .feed.client import AsyncFeedClient, FeedClient
    from .global_.client import AsyncGlobalClient, GlobalClient
    from .monitor.client import AsyncMonitorClient, MonitorClient
    from .page.client import AsyncPageClient, PageClient
    from .survey.client import AsyncSurveyClient, SurveyClient
    from .telemetry.client import AsyncTelemetryClient, TelemetryClient
    from .user.client import AsyncUserClient, UserClient
    from .website.client import AsyncWebsiteClient, WebsiteClient
    from .worker.client import AsyncWorkerClient, WorkerClient
    from .workspace.client import AsyncWorkspaceClient, WorkspaceClient


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
        self._ai: typing.Optional[AiClient] = None
        self._aigateway: typing.Optional[AigatewayClient] = None
        self._application: typing.Optional[ApplicationClient] = None
        self._global_: typing.Optional[GlobalClient] = None
        self._user: typing.Optional[UserClient] = None
        self._workspace: typing.Optional[WorkspaceClient] = None
        self._website: typing.Optional[WebsiteClient] = None
        self._monitor: typing.Optional[MonitorClient] = None
        self._page: typing.Optional[PageClient] = None
        self._telemetry: typing.Optional[TelemetryClient] = None
        self._survey: typing.Optional[SurveyClient] = None
        self._auditlog: typing.Optional[AuditlogClient] = None
        self._billing: typing.Optional[BillingClient] = None
        self._feed: typing.Optional[FeedClient] = None
        self._worker: typing.Optional[WorkerClient] = None

    @property
    def ai(self):
        if self._ai is None:
            from .ai.client import AiClient

            self._ai = AiClient(client_wrapper=self._client_wrapper)
        return self._ai

    @property
    def aigateway(self):
        if self._aigateway is None:
            from .aigateway.client import AigatewayClient

            self._aigateway = AigatewayClient(client_wrapper=self._client_wrapper)
        return self._aigateway

    @property
    def application(self):
        if self._application is None:
            from .application.client import ApplicationClient

            self._application = ApplicationClient(client_wrapper=self._client_wrapper)
        return self._application

    @property
    def global_(self):
        if self._global_ is None:
            from .global_.client import GlobalClient

            self._global_ = GlobalClient(client_wrapper=self._client_wrapper)
        return self._global_

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def workspace(self):
        if self._workspace is None:
            from .workspace.client import WorkspaceClient

            self._workspace = WorkspaceClient(client_wrapper=self._client_wrapper)
        return self._workspace

    @property
    def website(self):
        if self._website is None:
            from .website.client import WebsiteClient

            self._website = WebsiteClient(client_wrapper=self._client_wrapper)
        return self._website

    @property
    def monitor(self):
        if self._monitor is None:
            from .monitor.client import MonitorClient

            self._monitor = MonitorClient(client_wrapper=self._client_wrapper)
        return self._monitor

    @property
    def page(self):
        if self._page is None:
            from .page.client import PageClient

            self._page = PageClient(client_wrapper=self._client_wrapper)
        return self._page

    @property
    def telemetry(self):
        if self._telemetry is None:
            from .telemetry.client import TelemetryClient

            self._telemetry = TelemetryClient(client_wrapper=self._client_wrapper)
        return self._telemetry

    @property
    def survey(self):
        if self._survey is None:
            from .survey.client import SurveyClient

            self._survey = SurveyClient(client_wrapper=self._client_wrapper)
        return self._survey

    @property
    def auditlog(self):
        if self._auditlog is None:
            from .auditlog.client import AuditlogClient

            self._auditlog = AuditlogClient(client_wrapper=self._client_wrapper)
        return self._auditlog

    @property
    def billing(self):
        if self._billing is None:
            from .billing.client import BillingClient

            self._billing = BillingClient(client_wrapper=self._client_wrapper)
        return self._billing

    @property
    def feed(self):
        if self._feed is None:
            from .feed.client import FeedClient

            self._feed = FeedClient(client_wrapper=self._client_wrapper)
        return self._feed

    @property
    def worker(self):
        if self._worker is None:
            from .worker.client import WorkerClient

            self._worker = WorkerClient(client_wrapper=self._client_wrapper)
        return self._worker


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
        self._ai: typing.Optional[AsyncAiClient] = None
        self._aigateway: typing.Optional[AsyncAigatewayClient] = None
        self._application: typing.Optional[AsyncApplicationClient] = None
        self._global_: typing.Optional[AsyncGlobalClient] = None
        self._user: typing.Optional[AsyncUserClient] = None
        self._workspace: typing.Optional[AsyncWorkspaceClient] = None
        self._website: typing.Optional[AsyncWebsiteClient] = None
        self._monitor: typing.Optional[AsyncMonitorClient] = None
        self._page: typing.Optional[AsyncPageClient] = None
        self._telemetry: typing.Optional[AsyncTelemetryClient] = None
        self._survey: typing.Optional[AsyncSurveyClient] = None
        self._auditlog: typing.Optional[AsyncAuditlogClient] = None
        self._billing: typing.Optional[AsyncBillingClient] = None
        self._feed: typing.Optional[AsyncFeedClient] = None
        self._worker: typing.Optional[AsyncWorkerClient] = None

    @property
    def ai(self):
        if self._ai is None:
            from .ai.client import AsyncAiClient

            self._ai = AsyncAiClient(client_wrapper=self._client_wrapper)
        return self._ai

    @property
    def aigateway(self):
        if self._aigateway is None:
            from .aigateway.client import AsyncAigatewayClient

            self._aigateway = AsyncAigatewayClient(client_wrapper=self._client_wrapper)
        return self._aigateway

    @property
    def application(self):
        if self._application is None:
            from .application.client import AsyncApplicationClient

            self._application = AsyncApplicationClient(client_wrapper=self._client_wrapper)
        return self._application

    @property
    def global_(self):
        if self._global_ is None:
            from .global_.client import AsyncGlobalClient

            self._global_ = AsyncGlobalClient(client_wrapper=self._client_wrapper)
        return self._global_

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def workspace(self):
        if self._workspace is None:
            from .workspace.client import AsyncWorkspaceClient

            self._workspace = AsyncWorkspaceClient(client_wrapper=self._client_wrapper)
        return self._workspace

    @property
    def website(self):
        if self._website is None:
            from .website.client import AsyncWebsiteClient

            self._website = AsyncWebsiteClient(client_wrapper=self._client_wrapper)
        return self._website

    @property
    def monitor(self):
        if self._monitor is None:
            from .monitor.client import AsyncMonitorClient

            self._monitor = AsyncMonitorClient(client_wrapper=self._client_wrapper)
        return self._monitor

    @property
    def page(self):
        if self._page is None:
            from .page.client import AsyncPageClient

            self._page = AsyncPageClient(client_wrapper=self._client_wrapper)
        return self._page

    @property
    def telemetry(self):
        if self._telemetry is None:
            from .telemetry.client import AsyncTelemetryClient

            self._telemetry = AsyncTelemetryClient(client_wrapper=self._client_wrapper)
        return self._telemetry

    @property
    def survey(self):
        if self._survey is None:
            from .survey.client import AsyncSurveyClient

            self._survey = AsyncSurveyClient(client_wrapper=self._client_wrapper)
        return self._survey

    @property
    def auditlog(self):
        if self._auditlog is None:
            from .auditlog.client import AsyncAuditlogClient

            self._auditlog = AsyncAuditlogClient(client_wrapper=self._client_wrapper)
        return self._auditlog

    @property
    def billing(self):
        if self._billing is None:
            from .billing.client import AsyncBillingClient

            self._billing = AsyncBillingClient(client_wrapper=self._client_wrapper)
        return self._billing

    @property
    def feed(self):
        if self._feed is None:
            from .feed.client import AsyncFeedClient

            self._feed = AsyncFeedClient(client_wrapper=self._client_wrapper)
        return self._feed

    @property
    def worker(self):
        if self._worker is None:
            from .worker.client import AsyncWorkerClient

            self._worker = AsyncWorkerClient(client_wrapper=self._client_wrapper)
        return self._worker


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
