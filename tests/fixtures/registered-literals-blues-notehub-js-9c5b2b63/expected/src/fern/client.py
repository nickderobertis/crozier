

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .alert.client import AlertClient, AsyncAlertClient
    from .authorization.client import AsyncAuthorizationClient, AuthorizationClient
    from .billing_account.client import AsyncBillingAccountClient, BillingAccountClient
    from .description.client import AsyncDescriptionClient, DescriptionClient
    from .device.client import AsyncDeviceClient, DeviceClient
    from .event.client import AsyncEventClient, EventClient
    from .external_devices.client import AsyncExternalDevicesClient, ExternalDevicesClient
    from .jobs.client import AsyncJobsClient, JobsClient
    from .monitor.client import AsyncMonitorClient, MonitorClient
    from .organization.client import AsyncOrganizationClient, OrganizationClient
    from .project.client import AsyncProjectClient, ProjectClient
    from .route.client import AsyncRouteClient, RouteClient
    from .usage.client import AsyncUsageClient, UsageClient
    from .webhook.client import AsyncWebhookClient, WebhookClient


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
        self._authorization: typing.Optional[AuthorizationClient] = None
        self._billing_account: typing.Optional[BillingAccountClient] = None
        self._description: typing.Optional[DescriptionClient] = None
        self._organization: typing.Optional[OrganizationClient] = None
        self._device: typing.Optional[DeviceClient] = None
        self._webhook: typing.Optional[WebhookClient] = None
        self._external_devices: typing.Optional[ExternalDevicesClient] = None
        self._project: typing.Optional[ProjectClient] = None
        self._alert: typing.Optional[AlertClient] = None
        self._event: typing.Optional[EventClient] = None
        self._jobs: typing.Optional[JobsClient] = None
        self._monitor: typing.Optional[MonitorClient] = None
        self._route: typing.Optional[RouteClient] = None
        self._usage: typing.Optional[UsageClient] = None

    @property
    def authorization(self):
        if self._authorization is None:
            from .authorization.client import AuthorizationClient

            self._authorization = AuthorizationClient(client_wrapper=self._client_wrapper)
        return self._authorization

    @property
    def billing_account(self):
        if self._billing_account is None:
            from .billing_account.client import BillingAccountClient

            self._billing_account = BillingAccountClient(client_wrapper=self._client_wrapper)
        return self._billing_account

    @property
    def description(self):
        if self._description is None:
            from .description.client import DescriptionClient

            self._description = DescriptionClient(client_wrapper=self._client_wrapper)
        return self._description

    @property
    def organization(self):
        if self._organization is None:
            from .organization.client import OrganizationClient

            self._organization = OrganizationClient(client_wrapper=self._client_wrapper)
        return self._organization

    @property
    def device(self):
        if self._device is None:
            from .device.client import DeviceClient

            self._device = DeviceClient(client_wrapper=self._client_wrapper)
        return self._device

    @property
    def webhook(self):
        if self._webhook is None:
            from .webhook.client import WebhookClient

            self._webhook = WebhookClient(client_wrapper=self._client_wrapper)
        return self._webhook

    @property
    def external_devices(self):
        if self._external_devices is None:
            from .external_devices.client import ExternalDevicesClient

            self._external_devices = ExternalDevicesClient(client_wrapper=self._client_wrapper)
        return self._external_devices

    @property
    def project(self):
        if self._project is None:
            from .project.client import ProjectClient

            self._project = ProjectClient(client_wrapper=self._client_wrapper)
        return self._project

    @property
    def alert(self):
        if self._alert is None:
            from .alert.client import AlertClient

            self._alert = AlertClient(client_wrapper=self._client_wrapper)
        return self._alert

    @property
    def event(self):
        if self._event is None:
            from .event.client import EventClient

            self._event = EventClient(client_wrapper=self._client_wrapper)
        return self._event

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import JobsClient

            self._jobs = JobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def monitor(self):
        if self._monitor is None:
            from .monitor.client import MonitorClient

            self._monitor = MonitorClient(client_wrapper=self._client_wrapper)
        return self._monitor

    @property
    def route(self):
        if self._route is None:
            from .route.client import RouteClient

            self._route = RouteClient(client_wrapper=self._client_wrapper)
        return self._route

    @property
    def usage(self):
        if self._usage is None:
            from .usage.client import UsageClient

            self._usage = UsageClient(client_wrapper=self._client_wrapper)
        return self._usage


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
        self._authorization: typing.Optional[AsyncAuthorizationClient] = None
        self._billing_account: typing.Optional[AsyncBillingAccountClient] = None
        self._description: typing.Optional[AsyncDescriptionClient] = None
        self._organization: typing.Optional[AsyncOrganizationClient] = None
        self._device: typing.Optional[AsyncDeviceClient] = None
        self._webhook: typing.Optional[AsyncWebhookClient] = None
        self._external_devices: typing.Optional[AsyncExternalDevicesClient] = None
        self._project: typing.Optional[AsyncProjectClient] = None
        self._alert: typing.Optional[AsyncAlertClient] = None
        self._event: typing.Optional[AsyncEventClient] = None
        self._jobs: typing.Optional[AsyncJobsClient] = None
        self._monitor: typing.Optional[AsyncMonitorClient] = None
        self._route: typing.Optional[AsyncRouteClient] = None
        self._usage: typing.Optional[AsyncUsageClient] = None

    @property
    def authorization(self):
        if self._authorization is None:
            from .authorization.client import AsyncAuthorizationClient

            self._authorization = AsyncAuthorizationClient(client_wrapper=self._client_wrapper)
        return self._authorization

    @property
    def billing_account(self):
        if self._billing_account is None:
            from .billing_account.client import AsyncBillingAccountClient

            self._billing_account = AsyncBillingAccountClient(client_wrapper=self._client_wrapper)
        return self._billing_account

    @property
    def description(self):
        if self._description is None:
            from .description.client import AsyncDescriptionClient

            self._description = AsyncDescriptionClient(client_wrapper=self._client_wrapper)
        return self._description

    @property
    def organization(self):
        if self._organization is None:
            from .organization.client import AsyncOrganizationClient

            self._organization = AsyncOrganizationClient(client_wrapper=self._client_wrapper)
        return self._organization

    @property
    def device(self):
        if self._device is None:
            from .device.client import AsyncDeviceClient

            self._device = AsyncDeviceClient(client_wrapper=self._client_wrapper)
        return self._device

    @property
    def webhook(self):
        if self._webhook is None:
            from .webhook.client import AsyncWebhookClient

            self._webhook = AsyncWebhookClient(client_wrapper=self._client_wrapper)
        return self._webhook

    @property
    def external_devices(self):
        if self._external_devices is None:
            from .external_devices.client import AsyncExternalDevicesClient

            self._external_devices = AsyncExternalDevicesClient(client_wrapper=self._client_wrapper)
        return self._external_devices

    @property
    def project(self):
        if self._project is None:
            from .project.client import AsyncProjectClient

            self._project = AsyncProjectClient(client_wrapper=self._client_wrapper)
        return self._project

    @property
    def alert(self):
        if self._alert is None:
            from .alert.client import AsyncAlertClient

            self._alert = AsyncAlertClient(client_wrapper=self._client_wrapper)
        return self._alert

    @property
    def event(self):
        if self._event is None:
            from .event.client import AsyncEventClient

            self._event = AsyncEventClient(client_wrapper=self._client_wrapper)
        return self._event

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import AsyncJobsClient

            self._jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def monitor(self):
        if self._monitor is None:
            from .monitor.client import AsyncMonitorClient

            self._monitor = AsyncMonitorClient(client_wrapper=self._client_wrapper)
        return self._monitor

    @property
    def route(self):
        if self._route is None:
            from .route.client import AsyncRouteClient

            self._route = AsyncRouteClient(client_wrapper=self._client_wrapper)
        return self._route

    @property
    def usage(self):
        if self._usage is None:
            from .usage.client import AsyncUsageClient

            self._usage = AsyncUsageClient(client_wrapper=self._client_wrapper)
        return self._usage


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
