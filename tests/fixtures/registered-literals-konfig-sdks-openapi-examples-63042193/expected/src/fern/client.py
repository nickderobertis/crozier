

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .context.client import AsyncContextClient, ContextClient
    from .insights.client import AsyncInsightsClient, InsightsClient
    from .job.client import AsyncJobClient, JobClient
    from .oidc_token_management.client import AsyncOidcTokenManagementClient, OidcTokenManagementClient
    from .pipeline.client import AsyncPipelineClient, PipelineClient
    from .policy_management.client import AsyncPolicyManagementClient, PolicyManagementClient
    from .project.client import AsyncProjectClient, ProjectClient
    from .schedule.client import AsyncScheduleClient, ScheduleClient
    from .user.client import AsyncUserClient, UserClient
    from .webhook.client import AsyncWebhookClient, WebhookClient
    from .workflow.client import AsyncWorkflowClient, WorkflowClient


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
        self._context: typing.Optional[ContextClient] = None
        self._insights: typing.Optional[InsightsClient] = None
        self._user: typing.Optional[UserClient] = None
        self._pipeline: typing.Optional[PipelineClient] = None
        self._project: typing.Optional[ProjectClient] = None
        self._job: typing.Optional[JobClient] = None
        self._schedule: typing.Optional[ScheduleClient] = None
        self._webhook: typing.Optional[WebhookClient] = None
        self._workflow: typing.Optional[WorkflowClient] = None
        self._oidc_token_management: typing.Optional[OidcTokenManagementClient] = None
        self._policy_management: typing.Optional[PolicyManagementClient] = None

    @property
    def context(self):
        if self._context is None:
            from .context.client import ContextClient

            self._context = ContextClient(client_wrapper=self._client_wrapper)
        return self._context

    @property
    def insights(self):
        if self._insights is None:
            from .insights.client import InsightsClient

            self._insights = InsightsClient(client_wrapper=self._client_wrapper)
        return self._insights

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def pipeline(self):
        if self._pipeline is None:
            from .pipeline.client import PipelineClient

            self._pipeline = PipelineClient(client_wrapper=self._client_wrapper)
        return self._pipeline

    @property
    def project(self):
        if self._project is None:
            from .project.client import ProjectClient

            self._project = ProjectClient(client_wrapper=self._client_wrapper)
        return self._project

    @property
    def job(self):
        if self._job is None:
            from .job.client import JobClient

            self._job = JobClient(client_wrapper=self._client_wrapper)
        return self._job

    @property
    def schedule(self):
        if self._schedule is None:
            from .schedule.client import ScheduleClient

            self._schedule = ScheduleClient(client_wrapper=self._client_wrapper)
        return self._schedule

    @property
    def webhook(self):
        if self._webhook is None:
            from .webhook.client import WebhookClient

            self._webhook = WebhookClient(client_wrapper=self._client_wrapper)
        return self._webhook

    @property
    def workflow(self):
        if self._workflow is None:
            from .workflow.client import WorkflowClient

            self._workflow = WorkflowClient(client_wrapper=self._client_wrapper)
        return self._workflow

    @property
    def oidc_token_management(self):
        if self._oidc_token_management is None:
            from .oidc_token_management.client import OidcTokenManagementClient

            self._oidc_token_management = OidcTokenManagementClient(client_wrapper=self._client_wrapper)
        return self._oidc_token_management

    @property
    def policy_management(self):
        if self._policy_management is None:
            from .policy_management.client import PolicyManagementClient

            self._policy_management = PolicyManagementClient(client_wrapper=self._client_wrapper)
        return self._policy_management


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
        self._context: typing.Optional[AsyncContextClient] = None
        self._insights: typing.Optional[AsyncInsightsClient] = None
        self._user: typing.Optional[AsyncUserClient] = None
        self._pipeline: typing.Optional[AsyncPipelineClient] = None
        self._project: typing.Optional[AsyncProjectClient] = None
        self._job: typing.Optional[AsyncJobClient] = None
        self._schedule: typing.Optional[AsyncScheduleClient] = None
        self._webhook: typing.Optional[AsyncWebhookClient] = None
        self._workflow: typing.Optional[AsyncWorkflowClient] = None
        self._oidc_token_management: typing.Optional[AsyncOidcTokenManagementClient] = None
        self._policy_management: typing.Optional[AsyncPolicyManagementClient] = None

    @property
    def context(self):
        if self._context is None:
            from .context.client import AsyncContextClient

            self._context = AsyncContextClient(client_wrapper=self._client_wrapper)
        return self._context

    @property
    def insights(self):
        if self._insights is None:
            from .insights.client import AsyncInsightsClient

            self._insights = AsyncInsightsClient(client_wrapper=self._client_wrapper)
        return self._insights

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def pipeline(self):
        if self._pipeline is None:
            from .pipeline.client import AsyncPipelineClient

            self._pipeline = AsyncPipelineClient(client_wrapper=self._client_wrapper)
        return self._pipeline

    @property
    def project(self):
        if self._project is None:
            from .project.client import AsyncProjectClient

            self._project = AsyncProjectClient(client_wrapper=self._client_wrapper)
        return self._project

    @property
    def job(self):
        if self._job is None:
            from .job.client import AsyncJobClient

            self._job = AsyncJobClient(client_wrapper=self._client_wrapper)
        return self._job

    @property
    def schedule(self):
        if self._schedule is None:
            from .schedule.client import AsyncScheduleClient

            self._schedule = AsyncScheduleClient(client_wrapper=self._client_wrapper)
        return self._schedule

    @property
    def webhook(self):
        if self._webhook is None:
            from .webhook.client import AsyncWebhookClient

            self._webhook = AsyncWebhookClient(client_wrapper=self._client_wrapper)
        return self._webhook

    @property
    def workflow(self):
        if self._workflow is None:
            from .workflow.client import AsyncWorkflowClient

            self._workflow = AsyncWorkflowClient(client_wrapper=self._client_wrapper)
        return self._workflow

    @property
    def oidc_token_management(self):
        if self._oidc_token_management is None:
            from .oidc_token_management.client import AsyncOidcTokenManagementClient

            self._oidc_token_management = AsyncOidcTokenManagementClient(client_wrapper=self._client_wrapper)
        return self._oidc_token_management

    @property
    def policy_management(self):
        if self._policy_management is None:
            from .policy_management.client import AsyncPolicyManagementClient

            self._policy_management = AsyncPolicyManagementClient(client_wrapper=self._client_wrapper)
        return self._policy_management


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
