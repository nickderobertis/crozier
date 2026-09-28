

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .asyncapi.client import AsyncapiClient, AsyncAsyncapiClient
    from .audit.client import AsyncAuditClient, AuditClient
    from .chaos.client import AsyncChaosClient, ChaosClient
    from .cluster.client import AsyncClusterClient, ClusterClient
    from .contract.client import AsyncContractClient, ContractClient
    from .control.client import AsyncControlClient, ControlClient
    from .crud.client import AsyncCrudClient, CrudClient
    from .drift.client import AsyncDriftClient, DriftClient
    from .expectation.client import AsyncExpectationClient, ExpectationClient
    from .files.client import AsyncFilesClient, FilesClient
    from .grpc.client import AsyncGrpcClient, GrpcClient
    from .import_.client import AsyncImportClient, ImportClient
    from .llm.client import AsyncLlmClient, LlmClient
    from .loadgen.client import AsyncLoadgenClient, LoadgenClient
    from .mcp.client import AsyncMcpClient, McpClient
    from .metrics.client import AsyncMetricsClient, MetricsClient
    from .oidc.client import AsyncOidcClient, OidcClient
    from .pact.client import AsyncPactClient, PactClient
    from .saml.client import AsyncSamlClient, SamlClient
    from .scenario.client import AsyncScenarioClient, ScenarioClient
    from .scim.client import AsyncScimClient, ScimClient
    from .slo.client import AsyncSloClient, SloClient
    from .troubleshooting.client import AsyncTroubleshootingClient, TroubleshootingClient
    from .verify.client import AsyncVerifyClient, VerifyClient
    from .wasm.client import AsyncWasmClient, WasmClient


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
        self._expectation: typing.Optional[ExpectationClient] = None
        self._control: typing.Optional[ControlClient] = None
        self._verify: typing.Optional[VerifyClient] = None
        self._import_: typing.Optional[ImportClient] = None
        self._crud: typing.Optional[CrudClient] = None
        self._files: typing.Optional[FilesClient] = None
        self._chaos: typing.Optional[ChaosClient] = None
        self._drift: typing.Optional[DriftClient] = None
        self._audit: typing.Optional[AuditClient] = None
        self._scenario: typing.Optional[ScenarioClient] = None
        self._oidc: typing.Optional[OidcClient] = None
        self._saml: typing.Optional[SamlClient] = None
        self._scim: typing.Optional[ScimClient] = None
        self._asyncapi: typing.Optional[AsyncapiClient] = None
        self._wasm: typing.Optional[WasmClient] = None
        self._grpc: typing.Optional[GrpcClient] = None
        self._troubleshooting: typing.Optional[TroubleshootingClient] = None
        self._pact: typing.Optional[PactClient] = None
        self._loadgen: typing.Optional[LoadgenClient] = None
        self._slo: typing.Optional[SloClient] = None
        self._contract: typing.Optional[ContractClient] = None
        self._metrics: typing.Optional[MetricsClient] = None
        self._cluster: typing.Optional[ClusterClient] = None
        self._llm: typing.Optional[LlmClient] = None
        self._mcp: typing.Optional[McpClient] = None

    @property
    def expectation(self):
        if self._expectation is None:
            from .expectation.client import ExpectationClient

            self._expectation = ExpectationClient(client_wrapper=self._client_wrapper)
        return self._expectation

    @property
    def control(self):
        if self._control is None:
            from .control.client import ControlClient

            self._control = ControlClient(client_wrapper=self._client_wrapper)
        return self._control

    @property
    def verify(self):
        if self._verify is None:
            from .verify.client import VerifyClient

            self._verify = VerifyClient(client_wrapper=self._client_wrapper)
        return self._verify

    @property
    def import_(self):
        if self._import_ is None:
            from .import_.client import ImportClient

            self._import_ = ImportClient(client_wrapper=self._client_wrapper)
        return self._import_

    @property
    def crud(self):
        if self._crud is None:
            from .crud.client import CrudClient

            self._crud = CrudClient(client_wrapper=self._client_wrapper)
        return self._crud

    @property
    def files(self):
        if self._files is None:
            from .files.client import FilesClient

            self._files = FilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def chaos(self):
        if self._chaos is None:
            from .chaos.client import ChaosClient

            self._chaos = ChaosClient(client_wrapper=self._client_wrapper)
        return self._chaos

    @property
    def drift(self):
        if self._drift is None:
            from .drift.client import DriftClient

            self._drift = DriftClient(client_wrapper=self._client_wrapper)
        return self._drift

    @property
    def audit(self):
        if self._audit is None:
            from .audit.client import AuditClient

            self._audit = AuditClient(client_wrapper=self._client_wrapper)
        return self._audit

    @property
    def scenario(self):
        if self._scenario is None:
            from .scenario.client import ScenarioClient

            self._scenario = ScenarioClient(client_wrapper=self._client_wrapper)
        return self._scenario

    @property
    def oidc(self):
        if self._oidc is None:
            from .oidc.client import OidcClient

            self._oidc = OidcClient(client_wrapper=self._client_wrapper)
        return self._oidc

    @property
    def saml(self):
        if self._saml is None:
            from .saml.client import SamlClient

            self._saml = SamlClient(client_wrapper=self._client_wrapper)
        return self._saml

    @property
    def scim(self):
        if self._scim is None:
            from .scim.client import ScimClient

            self._scim = ScimClient(client_wrapper=self._client_wrapper)
        return self._scim

    @property
    def asyncapi(self):
        if self._asyncapi is None:
            from .asyncapi.client import AsyncapiClient

            self._asyncapi = AsyncapiClient(client_wrapper=self._client_wrapper)
        return self._asyncapi

    @property
    def wasm(self):
        if self._wasm is None:
            from .wasm.client import WasmClient

            self._wasm = WasmClient(client_wrapper=self._client_wrapper)
        return self._wasm

    @property
    def grpc(self):
        if self._grpc is None:
            from .grpc.client import GrpcClient

            self._grpc = GrpcClient(client_wrapper=self._client_wrapper)
        return self._grpc

    @property
    def troubleshooting(self):
        if self._troubleshooting is None:
            from .troubleshooting.client import TroubleshootingClient

            self._troubleshooting = TroubleshootingClient(client_wrapper=self._client_wrapper)
        return self._troubleshooting

    @property
    def pact(self):
        if self._pact is None:
            from .pact.client import PactClient

            self._pact = PactClient(client_wrapper=self._client_wrapper)
        return self._pact

    @property
    def loadgen(self):
        if self._loadgen is None:
            from .loadgen.client import LoadgenClient

            self._loadgen = LoadgenClient(client_wrapper=self._client_wrapper)
        return self._loadgen

    @property
    def slo(self):
        if self._slo is None:
            from .slo.client import SloClient

            self._slo = SloClient(client_wrapper=self._client_wrapper)
        return self._slo

    @property
    def contract(self):
        if self._contract is None:
            from .contract.client import ContractClient

            self._contract = ContractClient(client_wrapper=self._client_wrapper)
        return self._contract

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import MetricsClient

            self._metrics = MetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def cluster(self):
        if self._cluster is None:
            from .cluster.client import ClusterClient

            self._cluster = ClusterClient(client_wrapper=self._client_wrapper)
        return self._cluster

    @property
    def llm(self):
        if self._llm is None:
            from .llm.client import LlmClient

            self._llm = LlmClient(client_wrapper=self._client_wrapper)
        return self._llm

    @property
    def mcp(self):
        if self._mcp is None:
            from .mcp.client import McpClient

            self._mcp = McpClient(client_wrapper=self._client_wrapper)
        return self._mcp


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
        self._expectation: typing.Optional[AsyncExpectationClient] = None
        self._control: typing.Optional[AsyncControlClient] = None
        self._verify: typing.Optional[AsyncVerifyClient] = None
        self._import_: typing.Optional[AsyncImportClient] = None
        self._crud: typing.Optional[AsyncCrudClient] = None
        self._files: typing.Optional[AsyncFilesClient] = None
        self._chaos: typing.Optional[AsyncChaosClient] = None
        self._drift: typing.Optional[AsyncDriftClient] = None
        self._audit: typing.Optional[AsyncAuditClient] = None
        self._scenario: typing.Optional[AsyncScenarioClient] = None
        self._oidc: typing.Optional[AsyncOidcClient] = None
        self._saml: typing.Optional[AsyncSamlClient] = None
        self._scim: typing.Optional[AsyncScimClient] = None
        self._asyncapi: typing.Optional[AsyncAsyncapiClient] = None
        self._wasm: typing.Optional[AsyncWasmClient] = None
        self._grpc: typing.Optional[AsyncGrpcClient] = None
        self._troubleshooting: typing.Optional[AsyncTroubleshootingClient] = None
        self._pact: typing.Optional[AsyncPactClient] = None
        self._loadgen: typing.Optional[AsyncLoadgenClient] = None
        self._slo: typing.Optional[AsyncSloClient] = None
        self._contract: typing.Optional[AsyncContractClient] = None
        self._metrics: typing.Optional[AsyncMetricsClient] = None
        self._cluster: typing.Optional[AsyncClusterClient] = None
        self._llm: typing.Optional[AsyncLlmClient] = None
        self._mcp: typing.Optional[AsyncMcpClient] = None

    @property
    def expectation(self):
        if self._expectation is None:
            from .expectation.client import AsyncExpectationClient

            self._expectation = AsyncExpectationClient(client_wrapper=self._client_wrapper)
        return self._expectation

    @property
    def control(self):
        if self._control is None:
            from .control.client import AsyncControlClient

            self._control = AsyncControlClient(client_wrapper=self._client_wrapper)
        return self._control

    @property
    def verify(self):
        if self._verify is None:
            from .verify.client import AsyncVerifyClient

            self._verify = AsyncVerifyClient(client_wrapper=self._client_wrapper)
        return self._verify

    @property
    def import_(self):
        if self._import_ is None:
            from .import_.client import AsyncImportClient

            self._import_ = AsyncImportClient(client_wrapper=self._client_wrapper)
        return self._import_

    @property
    def crud(self):
        if self._crud is None:
            from .crud.client import AsyncCrudClient

            self._crud = AsyncCrudClient(client_wrapper=self._client_wrapper)
        return self._crud

    @property
    def files(self):
        if self._files is None:
            from .files.client import AsyncFilesClient

            self._files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def chaos(self):
        if self._chaos is None:
            from .chaos.client import AsyncChaosClient

            self._chaos = AsyncChaosClient(client_wrapper=self._client_wrapper)
        return self._chaos

    @property
    def drift(self):
        if self._drift is None:
            from .drift.client import AsyncDriftClient

            self._drift = AsyncDriftClient(client_wrapper=self._client_wrapper)
        return self._drift

    @property
    def audit(self):
        if self._audit is None:
            from .audit.client import AsyncAuditClient

            self._audit = AsyncAuditClient(client_wrapper=self._client_wrapper)
        return self._audit

    @property
    def scenario(self):
        if self._scenario is None:
            from .scenario.client import AsyncScenarioClient

            self._scenario = AsyncScenarioClient(client_wrapper=self._client_wrapper)
        return self._scenario

    @property
    def oidc(self):
        if self._oidc is None:
            from .oidc.client import AsyncOidcClient

            self._oidc = AsyncOidcClient(client_wrapper=self._client_wrapper)
        return self._oidc

    @property
    def saml(self):
        if self._saml is None:
            from .saml.client import AsyncSamlClient

            self._saml = AsyncSamlClient(client_wrapper=self._client_wrapper)
        return self._saml

    @property
    def scim(self):
        if self._scim is None:
            from .scim.client import AsyncScimClient

            self._scim = AsyncScimClient(client_wrapper=self._client_wrapper)
        return self._scim

    @property
    def asyncapi(self):
        if self._asyncapi is None:
            from .asyncapi.client import AsyncAsyncapiClient

            self._asyncapi = AsyncAsyncapiClient(client_wrapper=self._client_wrapper)
        return self._asyncapi

    @property
    def wasm(self):
        if self._wasm is None:
            from .wasm.client import AsyncWasmClient

            self._wasm = AsyncWasmClient(client_wrapper=self._client_wrapper)
        return self._wasm

    @property
    def grpc(self):
        if self._grpc is None:
            from .grpc.client import AsyncGrpcClient

            self._grpc = AsyncGrpcClient(client_wrapper=self._client_wrapper)
        return self._grpc

    @property
    def troubleshooting(self):
        if self._troubleshooting is None:
            from .troubleshooting.client import AsyncTroubleshootingClient

            self._troubleshooting = AsyncTroubleshootingClient(client_wrapper=self._client_wrapper)
        return self._troubleshooting

    @property
    def pact(self):
        if self._pact is None:
            from .pact.client import AsyncPactClient

            self._pact = AsyncPactClient(client_wrapper=self._client_wrapper)
        return self._pact

    @property
    def loadgen(self):
        if self._loadgen is None:
            from .loadgen.client import AsyncLoadgenClient

            self._loadgen = AsyncLoadgenClient(client_wrapper=self._client_wrapper)
        return self._loadgen

    @property
    def slo(self):
        if self._slo is None:
            from .slo.client import AsyncSloClient

            self._slo = AsyncSloClient(client_wrapper=self._client_wrapper)
        return self._slo

    @property
    def contract(self):
        if self._contract is None:
            from .contract.client import AsyncContractClient

            self._contract = AsyncContractClient(client_wrapper=self._client_wrapper)
        return self._contract

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import AsyncMetricsClient

            self._metrics = AsyncMetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def cluster(self):
        if self._cluster is None:
            from .cluster.client import AsyncClusterClient

            self._cluster = AsyncClusterClient(client_wrapper=self._client_wrapper)
        return self._cluster

    @property
    def llm(self):
        if self._llm is None:
            from .llm.client import AsyncLlmClient

            self._llm = AsyncLlmClient(client_wrapper=self._client_wrapper)
        return self._llm

    @property
    def mcp(self):
        if self._mcp is None:
            from .mcp.client import AsyncMcpClient

            self._mcp = AsyncMcpClient(client_wrapper=self._client_wrapper)
        return self._mcp


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
