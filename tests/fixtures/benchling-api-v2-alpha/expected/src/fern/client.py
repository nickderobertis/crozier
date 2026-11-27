

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .access_policies.client import AccessPoliciesClient, AsyncAccessPoliciesClient
    from .app_definitions.client import AppDefinitionsClient, AsyncAppDefinitionsClient
    from .apps.client import AppsClient, AsyncAppsClient
    from .assemblies.client import AssembliesClient, AsyncAssembliesClient
    from .authentication.client import AsyncAuthenticationClient, AuthenticationClient
    from .collaborations.client import AsyncCollaborationsClient, CollaborationsClient
    from .dna_oligos.client import AsyncDnaOligosClient, DnaOligosClient
    from .entries.client import AsyncEntriesClient, EntriesClient
    from .folders.client import AsyncFoldersClient, FoldersClient
    from .forms.client import AsyncFormsClient, FormsClient
    from .lab_automation.client import AsyncLabAutomationClient, LabAutomationClient
    from .legacy_workflows.client import AsyncLegacyWorkflowsClient, LegacyWorkflowsClient
    from .projects.client import AsyncProjectsClient, ProjectsClient
    from .schemas.client import AsyncSchemasClient, SchemasClient
    from .studies.client import AsyncStudiesClient, StudiesClient
    from .units.client import AsyncUnitsClient, UnitsClient
    from .worklists.client import AsyncWorklistsClient, WorklistsClient


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
        self._app_definitions: typing.Optional[AppDefinitionsClient] = None
        self._apps: typing.Optional[AppsClient] = None
        self._assemblies: typing.Optional[AssembliesClient] = None
        self._lab_automation: typing.Optional[LabAutomationClient] = None
        self._collaborations: typing.Optional[CollaborationsClient] = None
        self._dna_oligos: typing.Optional[DnaOligosClient] = None
        self._schemas: typing.Optional[SchemasClient] = None
        self._entries: typing.Optional[EntriesClient] = None
        self._folders: typing.Optional[FoldersClient] = None
        self._forms: typing.Optional[FormsClient] = None
        self._access_policies: typing.Optional[AccessPoliciesClient] = None
        self._projects: typing.Optional[ProjectsClient] = None
        self._legacy_workflows: typing.Optional[LegacyWorkflowsClient] = None
        self._studies: typing.Optional[StudiesClient] = None
        self._authentication: typing.Optional[AuthenticationClient] = None
        self._units: typing.Optional[UnitsClient] = None
        self._worklists: typing.Optional[WorklistsClient] = None

    @property
    def app_definitions(self):
        if self._app_definitions is None:
            from .app_definitions.client import AppDefinitionsClient

            self._app_definitions = AppDefinitionsClient(client_wrapper=self._client_wrapper)
        return self._app_definitions

    @property
    def apps(self):
        if self._apps is None:
            from .apps.client import AppsClient

            self._apps = AppsClient(client_wrapper=self._client_wrapper)
        return self._apps

    @property
    def assemblies(self):
        if self._assemblies is None:
            from .assemblies.client import AssembliesClient

            self._assemblies = AssembliesClient(client_wrapper=self._client_wrapper)
        return self._assemblies

    @property
    def lab_automation(self):
        if self._lab_automation is None:
            from .lab_automation.client import LabAutomationClient

            self._lab_automation = LabAutomationClient(client_wrapper=self._client_wrapper)
        return self._lab_automation

    @property
    def collaborations(self):
        if self._collaborations is None:
            from .collaborations.client import CollaborationsClient

            self._collaborations = CollaborationsClient(client_wrapper=self._client_wrapper)
        return self._collaborations

    @property
    def dna_oligos(self):
        if self._dna_oligos is None:
            from .dna_oligos.client import DnaOligosClient

            self._dna_oligos = DnaOligosClient(client_wrapper=self._client_wrapper)
        return self._dna_oligos

    @property
    def schemas(self):
        if self._schemas is None:
            from .schemas.client import SchemasClient

            self._schemas = SchemasClient(client_wrapper=self._client_wrapper)
        return self._schemas

    @property
    def entries(self):
        if self._entries is None:
            from .entries.client import EntriesClient

            self._entries = EntriesClient(client_wrapper=self._client_wrapper)
        return self._entries

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import FoldersClient

            self._folders = FoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import FormsClient

            self._forms = FormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def access_policies(self):
        if self._access_policies is None:
            from .access_policies.client import AccessPoliciesClient

            self._access_policies = AccessPoliciesClient(client_wrapper=self._client_wrapper)
        return self._access_policies

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import ProjectsClient

            self._projects = ProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def legacy_workflows(self):
        if self._legacy_workflows is None:
            from .legacy_workflows.client import LegacyWorkflowsClient

            self._legacy_workflows = LegacyWorkflowsClient(client_wrapper=self._client_wrapper)
        return self._legacy_workflows

    @property
    def studies(self):
        if self._studies is None:
            from .studies.client import StudiesClient

            self._studies = StudiesClient(client_wrapper=self._client_wrapper)
        return self._studies

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AuthenticationClient

            self._authentication = AuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def units(self):
        if self._units is None:
            from .units.client import UnitsClient

            self._units = UnitsClient(client_wrapper=self._client_wrapper)
        return self._units

    @property
    def worklists(self):
        if self._worklists is None:
            from .worklists.client import WorklistsClient

            self._worklists = WorklistsClient(client_wrapper=self._client_wrapper)
        return self._worklists


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
        self._app_definitions: typing.Optional[AsyncAppDefinitionsClient] = None
        self._apps: typing.Optional[AsyncAppsClient] = None
        self._assemblies: typing.Optional[AsyncAssembliesClient] = None
        self._lab_automation: typing.Optional[AsyncLabAutomationClient] = None
        self._collaborations: typing.Optional[AsyncCollaborationsClient] = None
        self._dna_oligos: typing.Optional[AsyncDnaOligosClient] = None
        self._schemas: typing.Optional[AsyncSchemasClient] = None
        self._entries: typing.Optional[AsyncEntriesClient] = None
        self._folders: typing.Optional[AsyncFoldersClient] = None
        self._forms: typing.Optional[AsyncFormsClient] = None
        self._access_policies: typing.Optional[AsyncAccessPoliciesClient] = None
        self._projects: typing.Optional[AsyncProjectsClient] = None
        self._legacy_workflows: typing.Optional[AsyncLegacyWorkflowsClient] = None
        self._studies: typing.Optional[AsyncStudiesClient] = None
        self._authentication: typing.Optional[AsyncAuthenticationClient] = None
        self._units: typing.Optional[AsyncUnitsClient] = None
        self._worklists: typing.Optional[AsyncWorklistsClient] = None

    @property
    def app_definitions(self):
        if self._app_definitions is None:
            from .app_definitions.client import AsyncAppDefinitionsClient

            self._app_definitions = AsyncAppDefinitionsClient(client_wrapper=self._client_wrapper)
        return self._app_definitions

    @property
    def apps(self):
        if self._apps is None:
            from .apps.client import AsyncAppsClient

            self._apps = AsyncAppsClient(client_wrapper=self._client_wrapper)
        return self._apps

    @property
    def assemblies(self):
        if self._assemblies is None:
            from .assemblies.client import AsyncAssembliesClient

            self._assemblies = AsyncAssembliesClient(client_wrapper=self._client_wrapper)
        return self._assemblies

    @property
    def lab_automation(self):
        if self._lab_automation is None:
            from .lab_automation.client import AsyncLabAutomationClient

            self._lab_automation = AsyncLabAutomationClient(client_wrapper=self._client_wrapper)
        return self._lab_automation

    @property
    def collaborations(self):
        if self._collaborations is None:
            from .collaborations.client import AsyncCollaborationsClient

            self._collaborations = AsyncCollaborationsClient(client_wrapper=self._client_wrapper)
        return self._collaborations

    @property
    def dna_oligos(self):
        if self._dna_oligos is None:
            from .dna_oligos.client import AsyncDnaOligosClient

            self._dna_oligos = AsyncDnaOligosClient(client_wrapper=self._client_wrapper)
        return self._dna_oligos

    @property
    def schemas(self):
        if self._schemas is None:
            from .schemas.client import AsyncSchemasClient

            self._schemas = AsyncSchemasClient(client_wrapper=self._client_wrapper)
        return self._schemas

    @property
    def entries(self):
        if self._entries is None:
            from .entries.client import AsyncEntriesClient

            self._entries = AsyncEntriesClient(client_wrapper=self._client_wrapper)
        return self._entries

    @property
    def folders(self):
        if self._folders is None:
            from .folders.client import AsyncFoldersClient

            self._folders = AsyncFoldersClient(client_wrapper=self._client_wrapper)
        return self._folders

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import AsyncFormsClient

            self._forms = AsyncFormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def access_policies(self):
        if self._access_policies is None:
            from .access_policies.client import AsyncAccessPoliciesClient

            self._access_policies = AsyncAccessPoliciesClient(client_wrapper=self._client_wrapper)
        return self._access_policies

    @property
    def projects(self):
        if self._projects is None:
            from .projects.client import AsyncProjectsClient

            self._projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        return self._projects

    @property
    def legacy_workflows(self):
        if self._legacy_workflows is None:
            from .legacy_workflows.client import AsyncLegacyWorkflowsClient

            self._legacy_workflows = AsyncLegacyWorkflowsClient(client_wrapper=self._client_wrapper)
        return self._legacy_workflows

    @property
    def studies(self):
        if self._studies is None:
            from .studies.client import AsyncStudiesClient

            self._studies = AsyncStudiesClient(client_wrapper=self._client_wrapper)
        return self._studies

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AsyncAuthenticationClient

            self._authentication = AsyncAuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def units(self):
        if self._units is None:
            from .units.client import AsyncUnitsClient

            self._units = AsyncUnitsClient(client_wrapper=self._client_wrapper)
        return self._units

    @property
    def worklists(self):
        if self._worklists is None:
            from .worklists.client import AsyncWorklistsClient

            self._worklists = AsyncWorklistsClient(client_wrapper=self._client_wrapper)
        return self._worklists


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
