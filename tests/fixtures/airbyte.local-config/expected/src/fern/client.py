

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .attempt.client import AsyncAttemptClient, AttemptClient
    from .connection.client import AsyncConnectionClient, ConnectionClient
    from .destination.client import AsyncDestinationClient, DestinationClient
    from .destination_definition.client import AsyncDestinationDefinitionClient, DestinationDefinitionClient
    from .destination_definition_specification.client import (
        AsyncDestinationDefinitionSpecificationClient,
        DestinationDefinitionSpecificationClient,
    )
    from .destination_oauth.client import AsyncDestinationOauthClient, DestinationOauthClient
    from .health.client import AsyncHealthClient, HealthClient
    from .jobs.client import AsyncJobsClient, JobsClient
    from .logs.client import AsyncLogsClient, LogsClient
    from .notifications.client import AsyncNotificationsClient, NotificationsClient
    from .openapi.client import AsyncOpenapiClient, OpenapiClient
    from .operation.client import AsyncOperationClient, OperationClient
    from .scheduler.client import AsyncSchedulerClient, SchedulerClient
    from .source.client import AsyncSourceClient, SourceClient
    from .source_definition.client import AsyncSourceDefinitionClient, SourceDefinitionClient
    from .source_definition_specification.client import (
        AsyncSourceDefinitionSpecificationClient,
        SourceDefinitionSpecificationClient,
    )
    from .source_oauth.client import AsyncSourceOauthClient, SourceOauthClient
    from .state.client import AsyncStateClient, StateClient
    from .web_backend.client import AsyncWebBackendClient, WebBackendClient
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
        self._attempt: typing.Optional[AttemptClient] = None
        self._connection: typing.Optional[ConnectionClient] = None
        self._destination_definition_specification: typing.Optional[DestinationDefinitionSpecificationClient] = None
        self._destination_definition: typing.Optional[DestinationDefinitionClient] = None
        self._destination_oauth: typing.Optional[DestinationOauthClient] = None
        self._destination: typing.Optional[DestinationClient] = None
        self._health: typing.Optional[HealthClient] = None
        self._jobs: typing.Optional[JobsClient] = None
        self._logs: typing.Optional[LogsClient] = None
        self._notifications: typing.Optional[NotificationsClient] = None
        self._openapi: typing.Optional[OpenapiClient] = None
        self._operation: typing.Optional[OperationClient] = None
        self._scheduler: typing.Optional[SchedulerClient] = None
        self._source_definition_specification: typing.Optional[SourceDefinitionSpecificationClient] = None
        self._source_definition: typing.Optional[SourceDefinitionClient] = None
        self._source_oauth: typing.Optional[SourceOauthClient] = None
        self._source: typing.Optional[SourceClient] = None
        self._state: typing.Optional[StateClient] = None
        self._web_backend: typing.Optional[WebBackendClient] = None
        self._workspace: typing.Optional[WorkspaceClient] = None

    @property
    def attempt(self):
        if self._attempt is None:
            from .attempt.client import AttemptClient

            self._attempt = AttemptClient(client_wrapper=self._client_wrapper)
        return self._attempt

    @property
    def connection(self):
        if self._connection is None:
            from .connection.client import ConnectionClient

            self._connection = ConnectionClient(client_wrapper=self._client_wrapper)
        return self._connection

    @property
    def destination_definition_specification(self):
        if self._destination_definition_specification is None:
            from .destination_definition_specification.client import (
                DestinationDefinitionSpecificationClient,
            )

            self._destination_definition_specification = DestinationDefinitionSpecificationClient(
                client_wrapper=self._client_wrapper
            )
        return self._destination_definition_specification

    @property
    def destination_definition(self):
        if self._destination_definition is None:
            from .destination_definition.client import DestinationDefinitionClient

            self._destination_definition = DestinationDefinitionClient(client_wrapper=self._client_wrapper)
        return self._destination_definition

    @property
    def destination_oauth(self):
        if self._destination_oauth is None:
            from .destination_oauth.client import DestinationOauthClient

            self._destination_oauth = DestinationOauthClient(client_wrapper=self._client_wrapper)
        return self._destination_oauth

    @property
    def destination(self):
        if self._destination is None:
            from .destination.client import DestinationClient

            self._destination = DestinationClient(client_wrapper=self._client_wrapper)
        return self._destination

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import JobsClient

            self._jobs = JobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import LogsClient

            self._logs = LogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import NotificationsClient

            self._notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def openapi(self):
        if self._openapi is None:
            from .openapi.client import OpenapiClient

            self._openapi = OpenapiClient(client_wrapper=self._client_wrapper)
        return self._openapi

    @property
    def operation(self):
        if self._operation is None:
            from .operation.client import OperationClient

            self._operation = OperationClient(client_wrapper=self._client_wrapper)
        return self._operation

    @property
    def scheduler(self):
        if self._scheduler is None:
            from .scheduler.client import SchedulerClient

            self._scheduler = SchedulerClient(client_wrapper=self._client_wrapper)
        return self._scheduler

    @property
    def source_definition_specification(self):
        if self._source_definition_specification is None:
            from .source_definition_specification.client import SourceDefinitionSpecificationClient

            self._source_definition_specification = SourceDefinitionSpecificationClient(
                client_wrapper=self._client_wrapper
            )
        return self._source_definition_specification

    @property
    def source_definition(self):
        if self._source_definition is None:
            from .source_definition.client import SourceDefinitionClient

            self._source_definition = SourceDefinitionClient(client_wrapper=self._client_wrapper)
        return self._source_definition

    @property
    def source_oauth(self):
        if self._source_oauth is None:
            from .source_oauth.client import SourceOauthClient

            self._source_oauth = SourceOauthClient(client_wrapper=self._client_wrapper)
        return self._source_oauth

    @property
    def source(self):
        if self._source is None:
            from .source.client import SourceClient

            self._source = SourceClient(client_wrapper=self._client_wrapper)
        return self._source

    @property
    def state(self):
        if self._state is None:
            from .state.client import StateClient

            self._state = StateClient(client_wrapper=self._client_wrapper)
        return self._state

    @property
    def web_backend(self):
        if self._web_backend is None:
            from .web_backend.client import WebBackendClient

            self._web_backend = WebBackendClient(client_wrapper=self._client_wrapper)
        return self._web_backend

    @property
    def workspace(self):
        if self._workspace is None:
            from .workspace.client import WorkspaceClient

            self._workspace = WorkspaceClient(client_wrapper=self._client_wrapper)
        return self._workspace


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
        self._attempt: typing.Optional[AsyncAttemptClient] = None
        self._connection: typing.Optional[AsyncConnectionClient] = None
        self._destination_definition_specification: typing.Optional[AsyncDestinationDefinitionSpecificationClient] = (
            None
        )
        self._destination_definition: typing.Optional[AsyncDestinationDefinitionClient] = None
        self._destination_oauth: typing.Optional[AsyncDestinationOauthClient] = None
        self._destination: typing.Optional[AsyncDestinationClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None
        self._jobs: typing.Optional[AsyncJobsClient] = None
        self._logs: typing.Optional[AsyncLogsClient] = None
        self._notifications: typing.Optional[AsyncNotificationsClient] = None
        self._openapi: typing.Optional[AsyncOpenapiClient] = None
        self._operation: typing.Optional[AsyncOperationClient] = None
        self._scheduler: typing.Optional[AsyncSchedulerClient] = None
        self._source_definition_specification: typing.Optional[AsyncSourceDefinitionSpecificationClient] = None
        self._source_definition: typing.Optional[AsyncSourceDefinitionClient] = None
        self._source_oauth: typing.Optional[AsyncSourceOauthClient] = None
        self._source: typing.Optional[AsyncSourceClient] = None
        self._state: typing.Optional[AsyncStateClient] = None
        self._web_backend: typing.Optional[AsyncWebBackendClient] = None
        self._workspace: typing.Optional[AsyncWorkspaceClient] = None

    @property
    def attempt(self):
        if self._attempt is None:
            from .attempt.client import AsyncAttemptClient

            self._attempt = AsyncAttemptClient(client_wrapper=self._client_wrapper)
        return self._attempt

    @property
    def connection(self):
        if self._connection is None:
            from .connection.client import AsyncConnectionClient

            self._connection = AsyncConnectionClient(client_wrapper=self._client_wrapper)
        return self._connection

    @property
    def destination_definition_specification(self):
        if self._destination_definition_specification is None:
            from .destination_definition_specification.client import (
                AsyncDestinationDefinitionSpecificationClient,
            )

            self._destination_definition_specification = AsyncDestinationDefinitionSpecificationClient(
                client_wrapper=self._client_wrapper
            )
        return self._destination_definition_specification

    @property
    def destination_definition(self):
        if self._destination_definition is None:
            from .destination_definition.client import AsyncDestinationDefinitionClient

            self._destination_definition = AsyncDestinationDefinitionClient(client_wrapper=self._client_wrapper)
        return self._destination_definition

    @property
    def destination_oauth(self):
        if self._destination_oauth is None:
            from .destination_oauth.client import AsyncDestinationOauthClient

            self._destination_oauth = AsyncDestinationOauthClient(client_wrapper=self._client_wrapper)
        return self._destination_oauth

    @property
    def destination(self):
        if self._destination is None:
            from .destination.client import AsyncDestinationClient

            self._destination = AsyncDestinationClient(client_wrapper=self._client_wrapper)
        return self._destination

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import AsyncJobsClient

            self._jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import AsyncLogsClient

            self._logs = AsyncLogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import AsyncNotificationsClient

            self._notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def openapi(self):
        if self._openapi is None:
            from .openapi.client import AsyncOpenapiClient

            self._openapi = AsyncOpenapiClient(client_wrapper=self._client_wrapper)
        return self._openapi

    @property
    def operation(self):
        if self._operation is None:
            from .operation.client import AsyncOperationClient

            self._operation = AsyncOperationClient(client_wrapper=self._client_wrapper)
        return self._operation

    @property
    def scheduler(self):
        if self._scheduler is None:
            from .scheduler.client import AsyncSchedulerClient

            self._scheduler = AsyncSchedulerClient(client_wrapper=self._client_wrapper)
        return self._scheduler

    @property
    def source_definition_specification(self):
        if self._source_definition_specification is None:
            from .source_definition_specification.client import AsyncSourceDefinitionSpecificationClient

            self._source_definition_specification = AsyncSourceDefinitionSpecificationClient(
                client_wrapper=self._client_wrapper
            )
        return self._source_definition_specification

    @property
    def source_definition(self):
        if self._source_definition is None:
            from .source_definition.client import AsyncSourceDefinitionClient

            self._source_definition = AsyncSourceDefinitionClient(client_wrapper=self._client_wrapper)
        return self._source_definition

    @property
    def source_oauth(self):
        if self._source_oauth is None:
            from .source_oauth.client import AsyncSourceOauthClient

            self._source_oauth = AsyncSourceOauthClient(client_wrapper=self._client_wrapper)
        return self._source_oauth

    @property
    def source(self):
        if self._source is None:
            from .source.client import AsyncSourceClient

            self._source = AsyncSourceClient(client_wrapper=self._client_wrapper)
        return self._source

    @property
    def state(self):
        if self._state is None:
            from .state.client import AsyncStateClient

            self._state = AsyncStateClient(client_wrapper=self._client_wrapper)
        return self._state

    @property
    def web_backend(self):
        if self._web_backend is None:
            from .web_backend.client import AsyncWebBackendClient

            self._web_backend = AsyncWebBackendClient(client_wrapper=self._client_wrapper)
        return self._web_backend

    @property
    def workspace(self):
        if self._workspace is None:
            from .workspace.client import AsyncWorkspaceClient

            self._workspace = AsyncWorkspaceClient(client_wrapper=self._client_wrapper)
        return self._workspace


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
