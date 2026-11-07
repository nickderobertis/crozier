

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .cql_execution_statistics.client import AsyncCqlExecutionStatisticsClient, CqlExecutionStatisticsClient
    from .edge_message.client import AsyncEdgeMessageClient, EdgeMessageClient
    from .entity_audit.client import AsyncEntityAuditClient, EntityAuditClient
    from .entity_management.client import AsyncEntityManagementClient, EntityManagementClient
    from .entity_model.client import AsyncEntityModelClient, EntityModelClient
    from .entity_model_workflow.client import AsyncEntityModelWorkflowClient, EntityModelWorkflowClient
    from .o_auth_keys.client import AsyncOAuthKeysClient, OAuthKeysClient
    from .o_auth_oidc_providers.client import AsyncOAuthOidcProvidersClient, OAuthOidcProvidersClient
    from .search.client import AsyncSearchClient, SearchClient
    from .sql_schema.client import AsyncSqlSchemaClient, SqlSchemaClient
    from .stream_data.client import AsyncStreamDataClient, StreamDataClient
    from .user_account.client import AsyncUserAccountClient, UserAccountClient
    from .user_machine.client import AsyncUserMachineClient, UserMachineClient


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



    token : typing.Union[str, typing.Callable[[], str]]
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
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._user_account: typing.Optional[UserAccountClient] = None
        self._entity_audit: typing.Optional[EntityAuditClient] = None
        self._user_machine: typing.Optional[UserMachineClient] = None
        self._entity_management: typing.Optional[EntityManagementClient] = None
        self._edge_message: typing.Optional[EdgeMessageClient] = None
        self._entity_model: typing.Optional[EntityModelClient] = None
        self._entity_model_workflow: typing.Optional[EntityModelWorkflowClient] = None
        self._o_auth_keys: typing.Optional[OAuthKeysClient] = None
        self._o_auth_oidc_providers: typing.Optional[OAuthOidcProvidersClient] = None
        self._stream_data: typing.Optional[StreamDataClient] = None
        self._cql_execution_statistics: typing.Optional[CqlExecutionStatisticsClient] = None
        self._search: typing.Optional[SearchClient] = None
        self._sql_schema: typing.Optional[SqlSchemaClient] = None

    @property
    def user_account(self):
        if self._user_account is None:
            from .user_account.client import UserAccountClient

            self._user_account = UserAccountClient(client_wrapper=self._client_wrapper)
        return self._user_account

    @property
    def entity_audit(self):
        if self._entity_audit is None:
            from .entity_audit.client import EntityAuditClient

            self._entity_audit = EntityAuditClient(client_wrapper=self._client_wrapper)
        return self._entity_audit

    @property
    def user_machine(self):
        if self._user_machine is None:
            from .user_machine.client import UserMachineClient

            self._user_machine = UserMachineClient(client_wrapper=self._client_wrapper)
        return self._user_machine

    @property
    def entity_management(self):
        if self._entity_management is None:
            from .entity_management.client import EntityManagementClient

            self._entity_management = EntityManagementClient(client_wrapper=self._client_wrapper)
        return self._entity_management

    @property
    def edge_message(self):
        if self._edge_message is None:
            from .edge_message.client import EdgeMessageClient

            self._edge_message = EdgeMessageClient(client_wrapper=self._client_wrapper)
        return self._edge_message

    @property
    def entity_model(self):
        if self._entity_model is None:
            from .entity_model.client import EntityModelClient

            self._entity_model = EntityModelClient(client_wrapper=self._client_wrapper)
        return self._entity_model

    @property
    def entity_model_workflow(self):
        if self._entity_model_workflow is None:
            from .entity_model_workflow.client import EntityModelWorkflowClient

            self._entity_model_workflow = EntityModelWorkflowClient(client_wrapper=self._client_wrapper)
        return self._entity_model_workflow

    @property
    def o_auth_keys(self):
        if self._o_auth_keys is None:
            from .o_auth_keys.client import OAuthKeysClient

            self._o_auth_keys = OAuthKeysClient(client_wrapper=self._client_wrapper)
        return self._o_auth_keys

    @property
    def o_auth_oidc_providers(self):
        if self._o_auth_oidc_providers is None:
            from .o_auth_oidc_providers.client import OAuthOidcProvidersClient

            self._o_auth_oidc_providers = OAuthOidcProvidersClient(client_wrapper=self._client_wrapper)
        return self._o_auth_oidc_providers

    @property
    def stream_data(self):
        if self._stream_data is None:
            from .stream_data.client import StreamDataClient

            self._stream_data = StreamDataClient(client_wrapper=self._client_wrapper)
        return self._stream_data

    @property
    def cql_execution_statistics(self):
        if self._cql_execution_statistics is None:
            from .cql_execution_statistics.client import CqlExecutionStatisticsClient

            self._cql_execution_statistics = CqlExecutionStatisticsClient(client_wrapper=self._client_wrapper)
        return self._cql_execution_statistics

    @property
    def search(self):
        if self._search is None:
            from .search.client import SearchClient

            self._search = SearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def sql_schema(self):
        if self._sql_schema is None:
            from .sql_schema.client import SqlSchemaClient

            self._sql_schema = SqlSchemaClient(client_wrapper=self._client_wrapper)
        return self._sql_schema


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



    token : typing.Union[str, typing.Callable[[], str]]
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
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._user_account: typing.Optional[AsyncUserAccountClient] = None
        self._entity_audit: typing.Optional[AsyncEntityAuditClient] = None
        self._user_machine: typing.Optional[AsyncUserMachineClient] = None
        self._entity_management: typing.Optional[AsyncEntityManagementClient] = None
        self._edge_message: typing.Optional[AsyncEdgeMessageClient] = None
        self._entity_model: typing.Optional[AsyncEntityModelClient] = None
        self._entity_model_workflow: typing.Optional[AsyncEntityModelWorkflowClient] = None
        self._o_auth_keys: typing.Optional[AsyncOAuthKeysClient] = None
        self._o_auth_oidc_providers: typing.Optional[AsyncOAuthOidcProvidersClient] = None
        self._stream_data: typing.Optional[AsyncStreamDataClient] = None
        self._cql_execution_statistics: typing.Optional[AsyncCqlExecutionStatisticsClient] = None
        self._search: typing.Optional[AsyncSearchClient] = None
        self._sql_schema: typing.Optional[AsyncSqlSchemaClient] = None

    @property
    def user_account(self):
        if self._user_account is None:
            from .user_account.client import AsyncUserAccountClient

            self._user_account = AsyncUserAccountClient(client_wrapper=self._client_wrapper)
        return self._user_account

    @property
    def entity_audit(self):
        if self._entity_audit is None:
            from .entity_audit.client import AsyncEntityAuditClient

            self._entity_audit = AsyncEntityAuditClient(client_wrapper=self._client_wrapper)
        return self._entity_audit

    @property
    def user_machine(self):
        if self._user_machine is None:
            from .user_machine.client import AsyncUserMachineClient

            self._user_machine = AsyncUserMachineClient(client_wrapper=self._client_wrapper)
        return self._user_machine

    @property
    def entity_management(self):
        if self._entity_management is None:
            from .entity_management.client import AsyncEntityManagementClient

            self._entity_management = AsyncEntityManagementClient(client_wrapper=self._client_wrapper)
        return self._entity_management

    @property
    def edge_message(self):
        if self._edge_message is None:
            from .edge_message.client import AsyncEdgeMessageClient

            self._edge_message = AsyncEdgeMessageClient(client_wrapper=self._client_wrapper)
        return self._edge_message

    @property
    def entity_model(self):
        if self._entity_model is None:
            from .entity_model.client import AsyncEntityModelClient

            self._entity_model = AsyncEntityModelClient(client_wrapper=self._client_wrapper)
        return self._entity_model

    @property
    def entity_model_workflow(self):
        if self._entity_model_workflow is None:
            from .entity_model_workflow.client import AsyncEntityModelWorkflowClient

            self._entity_model_workflow = AsyncEntityModelWorkflowClient(client_wrapper=self._client_wrapper)
        return self._entity_model_workflow

    @property
    def o_auth_keys(self):
        if self._o_auth_keys is None:
            from .o_auth_keys.client import AsyncOAuthKeysClient

            self._o_auth_keys = AsyncOAuthKeysClient(client_wrapper=self._client_wrapper)
        return self._o_auth_keys

    @property
    def o_auth_oidc_providers(self):
        if self._o_auth_oidc_providers is None:
            from .o_auth_oidc_providers.client import AsyncOAuthOidcProvidersClient

            self._o_auth_oidc_providers = AsyncOAuthOidcProvidersClient(client_wrapper=self._client_wrapper)
        return self._o_auth_oidc_providers

    @property
    def stream_data(self):
        if self._stream_data is None:
            from .stream_data.client import AsyncStreamDataClient

            self._stream_data = AsyncStreamDataClient(client_wrapper=self._client_wrapper)
        return self._stream_data

    @property
    def cql_execution_statistics(self):
        if self._cql_execution_statistics is None:
            from .cql_execution_statistics.client import AsyncCqlExecutionStatisticsClient

            self._cql_execution_statistics = AsyncCqlExecutionStatisticsClient(client_wrapper=self._client_wrapper)
        return self._cql_execution_statistics

    @property
    def search(self):
        if self._search is None:
            from .search.client import AsyncSearchClient

            self._search = AsyncSearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def sql_schema(self):
        if self._sql_schema is None:
            from .sql_schema.client import AsyncSqlSchemaClient

            self._sql_schema = AsyncSqlSchemaClient(client_wrapper=self._client_wrapper)
        return self._sql_schema


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
