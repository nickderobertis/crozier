

import datetime as dt
import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.action import Action
from .types.action_request import ActionRequest
from .types.ads_adapter_status import AdsAdapterStatus
from .types.ads_capability_gate import AdsCapabilityGate
from .types.agent_evaluation import AgentEvaluation
from .types.agent_graph_bundle import AgentGraphBundle
from .types.agent_graph_definition import AgentGraphDefinition
from .types.agent_graph_version import AgentGraphVersion
from .types.agent_run import AgentRun
from .types.agent_run_bundle import AgentRunBundle
from .types.agent_run_request import AgentRunRequest
from .types.api_key_issued import ApiKeyIssued
from .types.assurance_run import AssuranceRun
from .types.assurance_run_request_kind import AssuranceRunRequestKind
from .types.connector_registration import ConnectorRegistration
from .types.connector_update_request_config import ConnectorUpdateRequestConfig
from .types.daily_ops_brief_envelope import DailyOpsBriefEnvelope
from .types.daily_ops_evidence_selector import DailyOpsEvidenceSelector
from .types.daily_ops_run import DailyOpsRun
from .types.daily_ops_schedule import DailyOpsSchedule
from .types.demo_session import DemoSession
from .types.empty_request import EmptyRequest
from .types.evidence_import import EvidenceImport
from .types.evidence_report_type import EvidenceReportType
from .types.get_v1ads_capability_gates_response import GetV1AdsCapabilityGatesResponse
from .types.get_v1agent_graphs_response import GetV1AgentGraphsResponse
from .types.get_v1agent_runs_response import GetV1AgentRunsResponse
from .types.get_v1agent_runs_run_id_evaluations_response import GetV1AgentRunsRunIdEvaluationsResponse
from .types.get_v1agent_runs_run_id_events_response import GetV1AgentRunsRunIdEventsResponse
from .types.get_v1api_keys_response import GetV1ApiKeysResponse
from .types.get_v1approvals_response import GetV1ApprovalsResponse
from .types.get_v1assurance_runs_response import GetV1AssuranceRunsResponse
from .types.get_v1audit_response import GetV1AuditResponse
from .types.get_v1connectors_response import GetV1ConnectorsResponse
from .types.get_v1daily_ops_runs_response import GetV1DailyOpsRunsResponse
from .types.get_v1daily_ops_schedules_response import GetV1DailyOpsSchedulesResponse
from .types.get_v1evidence_imports_response import GetV1EvidenceImportsResponse
from .types.get_v1jobs_response import GetV1JobsResponse
from .types.get_v1metric_materializations_request_status import GetV1MetricMaterializationsRequestStatus
from .types.get_v1metric_materializations_response import GetV1MetricMaterializationsResponse
from .types.get_v1metric_observations_request_currency import GetV1MetricObservationsRequestCurrency
from .types.get_v1metric_observations_response import GetV1MetricObservationsResponse
from .types.get_v1metrics_response import GetV1MetricsResponse
from .types.get_v1proposal_executions_response import GetV1ProposalExecutionsResponse
from .types.get_v1proposals_response import GetV1ProposalsResponse
from .types.get_v1records_response import GetV1RecordsResponse
from .types.get_v1report_recipes_response import GetV1ReportRecipesResponse
from .types.get_v1report_syncs_response import GetV1ReportSyncsResponse
from .types.get_v1schedules_response import GetV1SchedulesResponse
from .types.get_v1users_response import GetV1UsersResponse
from .types.health import Health
from .types.job import Job
from .types.marketplace_account import MarketplaceAccount
from .types.marketplace_id import MarketplaceId
from .types.metric_materialization import MetricMaterialization
from .types.metric_observation import MetricObservation
from .types.mission_control import MissionControl
from .types.operating_briefing import OperatingBriefing
from .types.pilot_status import PilotStatus
from .types.post_v1api_keys_key_id_revoke_response import PostV1ApiKeysKeyIdRevokeResponse
from .types.post_v1api_keys_rotate_response import PostV1ApiKeysRotateResponse
from .types.post_v1metric_materializations_backfill_response import PostV1MetricMaterializationsBackfillResponse
from .types.principal import Principal
from .types.proposal import Proposal
from .types.proposal_create_request import ProposalCreateRequest
from .types.proposal_decision_type import ProposalDecisionType
from .types.proposal_execution import ProposalExecution
from .types.proposal_operation import ProposalOperation
from .types.proposal_payload import ProposalPayload
from .types.proposal_risk import ProposalRisk
from .types.proposal_status import ProposalStatus
from .types.provider_smoke_request import ProviderSmokeRequest
from .types.provider_smoke_test import ProviderSmokeTest
from .types.provider_smoke_test_list import ProviderSmokeTestList
from .types.readiness import Readiness
from .types.report_recipe import ReportRecipe
from .types.report_recipe_key import ReportRecipeKey
from .types.report_sync import ReportSync
from .types.role import Role
from .types.runtime_catalog import RuntimeCatalog
from .types.schedule import Schedule
from .types.schedule_create import ScheduleCreate
from .types.user_envelope import UserEnvelope


OMIT = typing.cast(typing.Any, ...)


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
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def check_process_liveness(self, *, request_options: typing.Optional[RequestOptions] = None) -> Health:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Health
            Healthy

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.check_process_liveness()
        """
        _response = self._raw_client.check_process_liveness(request_options=request_options)
        return _response.data

    def check_database_and_schema_readiness(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Readiness:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Readiness
            Database schema ready

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.check_database_and_schema_readiness()
        """
        _response = self._raw_client.check_database_and_schema_readiness(request_options=request_options)
        return _response.data

    def bootstrap_the_loopback_only_explicit_demo_ui_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DemoSession:
        """
        Available only when the separate `demo` CLI starts a database containing exactly one Demo tenant. Normal Runtime API processes return 404.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DemoSession
            Temporary Demo key kept in page memory and revoked when the Demo server stops

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.bootstrap_the_loopback_only_explicit_demo_ui_session()
        """
        _response = self._raw_client.bootstrap_the_loopback_only_explicit_demo_ui_session(
            request_options=request_options
        )
        return _response.data

    def read_the_authenticated_principal(self, *, request_options: typing.Optional[RequestOptions] = None) -> Principal:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Principal
            Authenticated principal

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_the_authenticated_principal()
        """
        _response = self._raw_client.read_the_authenticated_principal(request_options=request_options)
        return _response.data

    def list_users_owned_by_the_authenticated_tenant(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1UsersResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1UsersResponse
            Tenant users without API-key material

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_users_owned_by_the_authenticated_tenant()
        """
        _response = self._raw_client.list_users_owned_by_the_authenticated_tenant(request_options=request_options)
        return _response.data

    def create_a_tenant_user(
        self, *, email: str, role: Role, request_options: typing.Optional[RequestOptions] = None
    ) -> UserEnvelope:
        """
        Admins may assign roles up to admin; only an owner may assign owner.

        Parameters
        ----------
        email : str

        role : Role

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserEnvelope
            User created

        Examples
        --------
        from fern import FernApi, Role

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_a_tenant_user(
            email="email",
            role=Role.VIEWER,
        )
        """
        _response = self._raw_client.create_a_tenant_user(email=email, role=role, request_options=request_options)
        return _response.data

    def change_a_tenant_users_role(
        self, user_id: str, *, role: Role, request_options: typing.Optional[RequestOptions] = None
    ) -> UserEnvelope:
        """
        Self-role changes and last-owner demotion are rejected.

        Parameters
        ----------
        user_id : str

        role : Role

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserEnvelope
            Role updated

        Examples
        --------
        from fern import FernApi, Role

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.change_a_tenant_users_role(
            user_id="userId",
            role=Role.VIEWER,
        )
        """
        _response = self._raw_client.change_a_tenant_users_role(user_id, role=role, request_options=request_options)
        return _response.data

    def list_tenant_api_key_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ApiKeysResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ApiKeysResponse
            Key metadata without secrets or hashes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_api_key_metadata()
        """
        _response = self._raw_client.list_tenant_api_key_metadata(request_options=request_options)
        return _response.data

    def issue_a_one_time_api_key_for_a_tenant_user(
        self, *, user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyIssued:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyIssued
            One-time API key; the clear value is never returned again

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.issue_a_one_time_api_key_for_a_tenant_user(
            user_id="user_id",
        )
        """
        _response = self._raw_client.issue_a_one_time_api_key_for_a_tenant_user(
            user_id=user_id, request_options=request_options
        )
        return _response.data

    def rotate_the_current_callers_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1ApiKeysRotateResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1ApiKeysRotateResponse
            Replacement one-time API key

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rotate_the_current_callers_api_key()
        """
        _response = self._raw_client.rotate_the_current_callers_api_key(request_options=request_options)
        return _response.data

    def revoke_a_tenant_api_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1ApiKeysKeyIdRevokeResponse:
        """
        Parameters
        ----------
        key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1ApiKeysKeyIdRevokeResponse
            Key revoked

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.revoke_a_tenant_api_key(
            key_id="keyId",
        )
        """
        _response = self._raw_client.revoke_a_tenant_api_key(key_id, request_options=request_options)
        return _response.data

    def list_tenant_owned_marketplace_connector_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ConnectorsResponse:
        """
        Viewer, operator, admin, and owner roles may read the safe connector representation for their authenticated tenant. Credential values and environment-variable names are never returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ConnectorsResponse
            Connector accounts with redacted credential references

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_marketplace_connector_accounts()
        """
        _response = self._raw_client.list_tenant_owned_marketplace_connector_accounts(request_options=request_options)
        return _response.data

    def create_a_tenant_marketplace_connector_account(
        self, *, request: ConnectorRegistration, request_options: typing.Optional[RequestOptions] = None
    ) -> MarketplaceAccount:
        """
        Requires admin or owner role. The request stores only non-secret connector details and environment-variable references; the response redacts those references to a present marker.

        Parameters
        ----------
        request : ConnectorRegistration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarketplaceAccount
            Connector account created with initial unchecked health

        Examples
        --------
        from fern import ConnectorRegistration_Shopify, FernApi, ShopifyConnectorConfig

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_a_tenant_marketplace_connector_account(
            request=ConnectorRegistration_Shopify(
                external_account_id="external_account_id",
                config=ShopifyConnectorConfig(
                    shop_domain="shop_domain",
                    api_version="api_version",
                    credential_ref="credential_ref",
                ),
            ),
        )
        """
        _response = self._raw_client.create_a_tenant_marketplace_connector_account(
            request=request, request_options=request_options
        )
        return _response.data

    def read_one_tenant_marketplace_connector_account(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarketplaceAccount:
        """
        Viewer, operator, admin, and owner roles may read the safe connector representation. An account outside the authenticated tenant is indistinguishable from a missing account and returns 404.

        Parameters
        ----------
        account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarketplaceAccount
            Connector account with redacted credential references

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_tenant_marketplace_connector_account(
            account_id="accountId",
        )
        """
        _response = self._raw_client.read_one_tenant_marketplace_connector_account(
            account_id, request_options=request_options
        )
        return _response.data

    def update_a_tenant_marketplace_connector_account(
        self,
        account_id: str,
        *,
        config: ConnectorUpdateRequestConfig,
        external_account_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MarketplaceAccount:
        """
        Requires admin or owner role. The existing provider is retained; config is required and must contain the complete provider configuration. external_account_id is optional and omitted values retain the existing identifier. Updating config resets health to unchecked and clears the persisted health error.

        Parameters
        ----------
        account_id : str

        config : ConnectorUpdateRequestConfig

        external_account_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarketplaceAccount
            Updated connector account with health reset to unchecked

        Examples
        --------
        from fern import FernApi, ShopifyConnectorConfig

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_a_tenant_marketplace_connector_account(
            account_id="accountId",
            config=ShopifyConnectorConfig(
                shop_domain="shop_domain",
                api_version="api_version",
                credential_ref="credential_ref",
            ),
        )
        """
        _response = self._raw_client.update_a_tenant_marketplace_connector_account(
            account_id, config=config, external_account_id=external_account_id, request_options=request_options
        )
        return _response.data

    def run_and_persist_a_connector_health_check(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarketplaceAccount:
        """
        Requires operator, admin, or owner role. The check is synchronous and provider-specific: Amazon SP-API verifies Sellers marketplaceParticipations, Amazon Ads verifies the configured profile through the regional v2 profiles endpoint without reading campaigns, and Shopify reads shop.json. A failed remote check is persisted on the account and returned as a 200 response with health_status, health_error_code, and health_error_message; it is not converted into a transient success.

        Parameters
        ----------
        account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarketplaceAccount
            Connector account after the persisted health result; health_status may be healthy, unhealthy, or misconfigured

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.run_and_persist_a_connector_health_check(
            account_id="accountId",
        )
        """
        _response = self._raw_client.run_and_persist_a_connector_health_check(
            account_id, request_options=request_options
        )
        return _response.data

    def list_tenant_owned_provider_connectivity_tests(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderSmokeTestList:
        """
        Viewer, operator, admin, and owner roles may read bounded, safe metadata for their authenticated tenant. Listing never calls a provider and never returns credentials, request bodies, response bodies, model output, idempotency keys, fingerprints, or lease state.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderSmokeTestList
            Persisted provider connectivity test history, newest first

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_provider_connectivity_tests()
        """
        _response = self._raw_client.list_tenant_owned_provider_connectivity_tests(
            limit=limit, request_options=request_options
        )
        return _response.data

    def run_an_audited_live_provider_connectivity_test(
        self,
        *,
        idempotency_key: str,
        request: ProviderSmokeRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderSmokeTest:
        """
        Requires operator, admin, or owner role and Idempotency-Key. OpenAI performs one minimal Responses API request against the fixed official endpoint with store disabled and does not persist model output or raw response data. Amazon SP-API and Shopify reuse their existing read-only account health adapters and update connector health. Results and safe failure codes are tenant-persisted and hash-chain audited. A per-target cooldown may return 429 before any provider call.

        Parameters
        ----------
        idempotency_key : str
            Safe tenant-local provider-test replay key; the same key cannot be reused for a different provider target.

        request : ProviderSmokeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderSmokeTest
            Newly completed test, terminal idempotent replay, or active running replay

        Examples
        --------
        from fern import (
            FernApi,
            OpenAiProviderSmokeRequest,
            OpenAiProviderSmokeRequestProvider,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.run_an_audited_live_provider_connectivity_test(
            idempotency_key="Idempotency-Key",
            request=OpenAiProviderSmokeRequest(
                provider=OpenAiProviderSmokeRequestProvider.OPENAI,
            ),
        )
        """
        _response = self._raw_client.run_an_audited_live_provider_connectivity_test(
            idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    def read_one_tenant_owned_provider_connectivity_test(
        self, smoke_test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderSmokeTest:
        """
        A test outside the authenticated tenant is indistinguishable from a missing test and returns 404. The response contains safe metadata only and never calls a provider.

        Parameters
        ----------
        smoke_test_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderSmokeTest
            Persisted safe provider connectivity test metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_tenant_owned_provider_connectivity_test(
            smoke_test_id="smokeTestId",
        )
        """
        _response = self._raw_client.read_one_tenant_owned_provider_connectivity_test(
            smoke_test_id, request_options=request_options
        )
        return _response.data

    def list_tenant_owned_amazon_report_recipes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ReportRecipesResponse:
        """
        Viewer, operator, admin, and owner roles may read persisted report recipes for their authenticated tenant. Listing recipes never calls Amazon.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportRecipesResponse
            Persisted report recipes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_amazon_report_recipes()
        """
        _response = self._raw_client.list_tenant_owned_amazon_report_recipes(request_options=request_options)
        return _response.data

    def persist_an_amazon_report_recipe(
        self,
        *,
        connector_account_id: str,
        name: str,
        recipe_key: ReportRecipeKey,
        marketplace_ids: typing.Sequence[str],
        interval_minutes: int,
        lookback_days: int,
        enabled: bool,
        next_run_at: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportRecipe:
        """
        Requires operator or owner role. This L2 operation validates and persists configuration only; it does not call Amazon, enqueue work, or create a report. connector_account_id must reference an Amazon SP-API account in the authenticated tenant, and marketplace_ids must be a subset of that account's configured marketplaces.

        Parameters
        ----------
        connector_account_id : str

        name : str

        recipe_key : ReportRecipeKey

        marketplace_ids : typing.Sequence[str]

        interval_minutes : int

        lookback_days : int

        enabled : bool

        next_run_at : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportRecipe
            Persisted report recipe

        Examples
        --------
        import datetime

        from fern import FernApi, ReportRecipeKey

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.persist_an_amazon_report_recipe(
            connector_account_id="connector_account_id",
            name="name",
            recipe_key=ReportRecipeKey.SALES_TRAFFIC_DAILY,
            marketplace_ids=["marketplace_ids"],
            interval_minutes=1,
            lookback_days=1,
            enabled=True,
            next_run_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.persist_an_amazon_report_recipe(
            connector_account_id=connector_account_id,
            name=name,
            recipe_key=recipe_key,
            marketplace_ids=marketplace_ids,
            interval_minutes=interval_minutes,
            lookback_days=lookback_days,
            enabled=enabled,
            next_run_at=next_run_at,
            request_options=request_options,
        )
        return _response.data

    def read_one_tenant_owned_amazon_report_recipe(
        self, recipe_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportRecipe:
        """
        Viewer, operator, admin, and owner roles may read a persisted recipe. A recipe outside the authenticated tenant returns 404.

        Parameters
        ----------
        recipe_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportRecipe
            Persisted report recipe

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_tenant_owned_amazon_report_recipe(
            recipe_id="recipeId",
        )
        """
        _response = self._raw_client.read_one_tenant_owned_amazon_report_recipe(
            recipe_id, request_options=request_options
        )
        return _response.data

    def update_a_tenant_owned_amazon_report_recipe(
        self,
        recipe_id: str,
        *,
        name: str,
        recipe_key: ReportRecipeKey,
        marketplace_ids: typing.Sequence[str],
        interval_minutes: int,
        lookback_days: int,
        enabled: bool,
        next_run_at: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportRecipe:
        """
        Requires operator or owner role. All recipe fields except connector_account_id are required on update; the connector account cannot be changed. The update persists configuration only and never calls Amazon. marketplace_ids must remain a subset of the linked account's configured marketplaces.

        Parameters
        ----------
        recipe_id : str

        name : str

        recipe_key : ReportRecipeKey

        marketplace_ids : typing.Sequence[str]

        interval_minutes : int

        lookback_days : int

        enabled : bool

        next_run_at : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportRecipe
            Updated persisted report recipe

        Examples
        --------
        import datetime

        from fern import FernApi, ReportRecipeKey

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.update_a_tenant_owned_amazon_report_recipe(
            recipe_id="recipeId",
            name="name",
            recipe_key=ReportRecipeKey.SALES_TRAFFIC_DAILY,
            marketplace_ids=["marketplace_ids"],
            interval_minutes=1,
            lookback_days=1,
            enabled=True,
            next_run_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.update_a_tenant_owned_amazon_report_recipe(
            recipe_id,
            name=name,
            recipe_key=recipe_key,
            marketplace_ids=marketplace_ids,
            interval_minutes=interval_minutes,
            lookback_days=lookback_days,
            enabled=enabled,
            next_run_at=next_run_at,
            request_options=request_options,
        )
        return _response.data

    def enqueue_an_idempotent_amazon_report_synchronization(
        self, recipe_id: str, *, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportSync:
        """
        Requires operator or higher and an Idempotency-Key. The linked Amazon account and recipe must be enabled and healthy. A durable L3 worker performs the official createReport call, then getReport polling through IN_QUEUE, IN_PROGRESS, DONE, CANCELLED, or FATAL, document retrieval, bounded normalization, and Evidence import asynchronously. HTTP 429 responses preserve Retry-After and use bounded retry/backoff; L3 never writes to Amazon and does not automatically schedule enabled recipes.

        Parameters
        ----------
        recipe_id : str

        idempotency_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportSync
            Durable queued or replayed report sync

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.enqueue_an_idempotent_amazon_report_synchronization(
            recipe_id="recipeId",
            idempotency_key="Idempotency-Key",
        )
        """
        _response = self._raw_client.enqueue_an_idempotent_amazon_report_synchronization(
            recipe_id, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def list_tenant_owned_amazon_report_syncs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ReportSyncsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportSyncsResponse
            Durable report synchronization states

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_amazon_report_syncs()
        """
        _response = self._raw_client.list_tenant_owned_amazon_report_syncs(limit=limit, request_options=request_options)
        return _response.data

    def read_one_tenant_owned_amazon_report_sync(
        self, sync_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportSync:
        """
        Parameters
        ----------
        sync_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportSync
            Durable report synchronization state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_tenant_owned_amazon_report_sync(
            sync_id="syncId",
        )
        """
        _response = self._raw_client.read_one_tenant_owned_amazon_report_sync(sync_id, request_options=request_options)
        return _response.data

    def list_tenant_owned_amazon_ads_capability_gates(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AdsCapabilityGatesResponse:
        """
        Viewer, operator, admin, and owner roles may inspect persisted Ads admission checks. The route never probes Amazon.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AdsCapabilityGatesResponse
            Persisted Ads capability gates

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_amazon_ads_capability_gates()
        """
        _response = self._raw_client.list_tenant_owned_amazon_ads_capability_gates(
            limit=limit, request_options=request_options
        )
        return _response.data

    def run_a_read_only_amazon_ads_capability_gate(
        self,
        *,
        idempotency_key: str,
        connector_account_id: str,
        attestation_reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdsCapabilityGate:
        """
        Requires admin or owner role and Idempotency-Key. The request performs only live probes and records an optional external attestation reference; it never creates or mutates an Ads resource.

        Parameters
        ----------
        idempotency_key : str

        connector_account_id : str

        attestation_reference : typing.Optional[str]
            Opaque external approval reference; secrets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdsCapabilityGate
            Persisted terminal gate result, or a replayed checking result held by another request lease

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.run_a_read_only_amazon_ads_capability_gate(
            idempotency_key="Idempotency-Key",
            connector_account_id="connector_account_id",
        )
        """
        _response = self._raw_client.run_a_read_only_amazon_ads_capability_gate(
            idempotency_key=idempotency_key,
            connector_account_id=connector_account_id,
            attestation_reference=attestation_reference,
            request_options=request_options,
        )
        return _response.data

    def read_one_tenant_owned_amazon_ads_capability_gate(
        self, gate_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AdsCapabilityGate:
        """
        Parameters
        ----------
        gate_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdsCapabilityGate
            Persisted Ads capability gate

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_tenant_owned_amazon_ads_capability_gate(
            gate_id="gateId",
        )
        """
        _response = self._raw_client.read_one_tenant_owned_amazon_ads_capability_gate(
            gate_id, request_options=request_options
        )
        return _response.data

    def read_the_conditional_amazon_ads_adapter_status(
        self,
        *,
        connector_account_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdsAdapterStatus:
        """
        Viewer-readable negative gate. This build does not register Ads write adapters, routes, or actions. `eligible_not_installed` is the only non-blocked fixture outcome permitted until a future release satisfies the L5 gate and approval safeguards.

        Parameters
        ----------
        connector_account_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdsAdapterStatus
            Tenant-scoped adapter status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_the_conditional_amazon_ads_adapter_status()
        """
        _response = self._raw_client.read_the_conditional_amazon_ads_adapter_status(
            connector_account_id=connector_account_id, request_options=request_options
        )
        return _response.data

    def request_an_idempotent_action(
        self, *, idempotency_key: str, request: ActionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        idempotency_key : str

        request : ActionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            Existing idempotent action or newly requested action

        Examples
        --------
        from fern import (
            ActionRequest_ShopifySyncProducts,
            FernApi,
            ShopifySyncActionRequestPayload,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.request_an_idempotent_action(
            idempotency_key="Idempotency-Key",
            request=ActionRequest_ShopifySyncProducts(
                payload=ShopifySyncActionRequestPayload(
                    external_account_id="external_account_id",
                ),
            ),
        )
        """
        _response = self._raw_client.request_an_idempotent_action(
            idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    def approve_a_requested_action_as_a_second_actor(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            Approved action

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.approve_a_requested_action_as_a_second_actor(
            action_id="actionId",
        )
        """
        _response = self._raw_client.approve_a_requested_action_as_a_second_actor(
            action_id, request_options=request_options
        )
        return _response.data

    def execute_an_approved_action(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            Executed action

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.execute_an_approved_action(
            action_id="actionId",
        )
        """
        _response = self._raw_client.execute_an_approved_action(action_id, request_options=request_options)
        return _response.data

    def re_queue_a_failed_or_expired_execution_without_bypassing_approval(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            Action returned to approved state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.re_queue_a_failed_or_expired_execution_without_bypassing_approval(
            action_id="actionId",
        )
        """
        _response = self._raw_client.re_queue_a_failed_or_expired_execution_without_bypassing_approval(
            action_id, request_options=request_options
        )
        return _response.data

    def list_tenant_owned_durable_proposals(
        self,
        *,
        status: typing.Optional[ProposalStatus] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ProposalsResponse:
        """
        Parameters
        ----------
        status : typing.Optional[ProposalStatus]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ProposalsResponse
            Full tenant proposal representations, including local decisions, linked executions, immutable versions, and capability preflight state.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_durable_proposals()
        """
        _response = self._raw_client.list_tenant_owned_durable_proposals(
            status=status, limit=limit, request_options=request_options
        )
        return _response.data

    def derive_an_idempotent_proposal_from_an_approved_daily_ops_priority(
        self,
        *,
        idempotency_key: str,
        request: ProposalCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Proposal:
        """
        Requires operator or higher and an Idempotency-Key. Source run, graph, evidence, metric, and payload lineage are derived server-side; caller-supplied provenance is rejected. Replaying the original create request after a revision returns the same resource's current representation, while a changed request with the same key conflicts.

        Parameters
        ----------
        idempotency_key : str

        request : ProposalCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Existing idempotent proposal or newly created draft

        Examples
        --------
        import datetime

        from fern import (
            FernApi,
            HumanReviewProposalPayload,
            ProposalCreateRequest_HumanReview,
            ProposalRisk,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.derive_an_idempotent_proposal_from_an_approved_daily_ops_priority(
            idempotency_key="Idempotency-Key",
            request=ProposalCreateRequest_HumanReview(
                daily_ops_run_id="daily_ops_run_id",
                priority_rank=1,
                rollback_plan="rollback_plan",
                payload=HumanReviewProposalPayload(
                    instructions="instructions",
                ),
                risk=ProposalRisk.LOW,
                expires_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            ),
        )
        """
        _response = self._raw_client.derive_an_idempotent_proposal_from_an_approved_daily_ops_priority(
            idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    def read_a_tenant_owned_proposal_and_its_local_decisions(
        self, proposal_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Proposal:
        """
        Parameters
        ----------
        proposal_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Proposal detail

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_a_tenant_owned_proposal_and_its_local_decisions(
            proposal_id="proposalId",
        )
        """
        _response = self._raw_client.read_a_tenant_owned_proposal_and_its_local_decisions(
            proposal_id, request_options=request_options
        )
        return _response.data

    def revise_a_draft_or_revision_required_proposal_optimistically(
        self,
        proposal_id: str,
        *,
        expected_version: int,
        title: typing.Optional[str] = OMIT,
        rationale: typing.Optional[str] = OMIT,
        expected_impact: typing.Optional[str] = OMIT,
        rollback_plan: typing.Optional[str] = OMIT,
        operation: typing.Optional[ProposalOperation] = OMIT,
        payload: typing.Optional[ProposalPayload] = OMIT,
        risk: typing.Optional[ProposalRisk] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Proposal:
        """
        Parameters
        ----------
        proposal_id : str

        expected_version : int

        title : typing.Optional[str]

        rationale : typing.Optional[str]

        expected_impact : typing.Optional[str]

        rollback_plan : typing.Optional[str]

        operation : typing.Optional[ProposalOperation]

        payload : typing.Optional[ProposalPayload]

        risk : typing.Optional[ProposalRisk]

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Revised proposal with a new version and payload hash

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.revise_a_draft_or_revision_required_proposal_optimistically(
            proposal_id="proposalId",
            expected_version=1,
        )
        """
        _response = self._raw_client.revise_a_draft_or_revision_required_proposal_optimistically(
            proposal_id,
            expected_version=expected_version,
            title=title,
            rationale=rationale,
            expected_impact=expected_impact,
            rollback_plan=rollback_plan,
            operation=operation,
            payload=payload,
            risk=risk,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    def submit_a_proposal_to_local_human_review(
        self, proposal_id: str, *, expected_version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> Proposal:
        """
        Parameters
        ----------
        proposal_id : str

        expected_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Submitted proposal

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.submit_a_proposal_to_local_human_review(
            proposal_id="proposalId",
            expected_version=1,
        )
        """
        _response = self._raw_client.submit_a_proposal_to_local_human_review(
            proposal_id, expected_version=expected_version, request_options=request_options
        )
        return _response.data

    def record_a_local_human_review_decision_optimistically(
        self,
        proposal_id: str,
        *,
        expected_version: int,
        decision: ProposalDecisionType,
        comment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Proposal:
        """
        Local human.review is an auditable local decision only. A requester cannot approve their own proposal and this endpoint does not attest marketplace or Ads approval.

        Parameters
        ----------
        proposal_id : str

        expected_version : int

        decision : ProposalDecisionType

        comment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Proposal after decision

        Examples
        --------
        from fern import FernApi, ProposalDecisionType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.record_a_local_human_review_decision_optimistically(
            proposal_id="proposalId",
            expected_version=1,
            decision=ProposalDecisionType.APPROVE,
            comment="comment",
        )
        """
        _response = self._raw_client.record_a_local_human_review_decision_optimistically(
            proposal_id,
            expected_version=expected_version,
            decision=decision,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    def idempotently_execute_an_approved_safe_read_proposal(
        self,
        proposal_id: str,
        *,
        idempotency_key: str,
        expected_version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProposalExecution:
        """
        Requires operator or higher and an Idempotency-Key. Only existing safe read Action operations are permitted; no general marketplace or Amazon Ads write is registered. A different Idempotency-Key for the same approved proposal version conflicts rather than creating a second execution.

        Parameters
        ----------
        proposal_id : str

        idempotency_key : str

        expected_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProposalExecution
            Existing idempotent execution or a new durable execution

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.idempotently_execute_an_approved_safe_read_proposal(
            proposal_id="proposalId",
            idempotency_key="Idempotency-Key",
            expected_version=1,
        )
        """
        _response = self._raw_client.idempotently_execute_an_approved_safe_read_proposal(
            proposal_id,
            idempotency_key=idempotency_key,
            expected_version=expected_version,
            request_options=request_options,
        )
        return _response.data

    def retry_a_failed_proposal_execution_idempotently_on_its_existing_durable_execution_row(
        self,
        proposal_id: str,
        *,
        idempotency_key: str,
        expected_version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProposalExecution:
        """
        Requires a new Idempotency-Key and the current version. Retry records a retry receipt and reuses the existing execution row; it does not create another execution resource. A connector failure is durably recorded before a 502 response.

        Parameters
        ----------
        proposal_id : str

        idempotency_key : str

        expected_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProposalExecution
            Existing idempotent retry or the same durable execution after its retry transition

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.retry_a_failed_proposal_execution_idempotently_on_its_existing_durable_execution_row(
            proposal_id="proposalId",
            idempotency_key="Idempotency-Key",
            expected_version=1,
        )
        """
        _response = (
            self._raw_client.retry_a_failed_proposal_execution_idempotently_on_its_existing_durable_execution_row(
                proposal_id,
                idempotency_key=idempotency_key,
                expected_version=expected_version,
                request_options=request_options,
            )
        )
        return _response.data

    def list_tenant_owned_proposal_executions(
        self,
        *,
        proposal_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ProposalExecutionsResponse:
        """
        Parameters
        ----------
        proposal_id : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ProposalExecutionsResponse
            Proposal execution history

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_proposal_executions()
        """
        _response = self._raw_client.list_tenant_owned_proposal_executions(
            proposal_id=proposal_id, limit=limit, request_options=request_options
        )
        return _response.data

    def read_one_tenant_owned_proposal_execution(
        self, execution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProposalExecution:
        """
        Parameters
        ----------
        execution_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProposalExecution
            Proposal execution detail

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_tenant_owned_proposal_execution(
            execution_id="executionId",
        )
        """
        _response = self._raw_client.read_one_tenant_owned_proposal_execution(
            execution_id, request_options=request_options
        )
        return _response.data

    def list_tenant_owned_csv_evidence_imports(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1EvidenceImportsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1EvidenceImportsResponse
            Import metadata without stored rows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_csv_evidence_imports()
        """
        _response = self._raw_client.list_tenant_owned_csv_evidence_imports(
            limit=limit, request_options=request_options
        )
        return _response.data

    def parse_and_persist_real_marketplace_csv_evidence(
        self,
        *,
        idempotency_key: str,
        evidence_platform: MarketplaceId,
        evidence_type: EvidenceReportType,
        evidence_filename: str,
        evidence_observed_at: dt.datetime,
        evidence_sheet: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvidenceImport:
        """
        Amazon typed reports receive semantic column validation; platform_generic accepts any ontology marketplace.

        Parameters
        ----------
        idempotency_key : str

        evidence_platform : MarketplaceId

        evidence_type : EvidenceReportType

        evidence_filename : str

        evidence_observed_at : dt.datetime

        evidence_sheet : typing.Optional[str]
            Optional worksheet name for XLSX; defaults to the active sheet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvidenceImport
            Persisted evidence-import metadata; parsed rows remain server-side

        Examples
        --------
        import datetime

        from fern import EvidenceReportType, FernApi, MarketplaceId

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.parse_and_persist_real_marketplace_csv_evidence(
            idempotency_key="Idempotency-Key",
            evidence_platform=MarketplaceId.ALIEXPRESS,
            evidence_type=EvidenceReportType.AMAZON_BUSINESS_REPORT,
            evidence_filename="X-Evidence-Filename",
            evidence_observed_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.parse_and_persist_real_marketplace_csv_evidence(
            idempotency_key=idempotency_key,
            evidence_platform=evidence_platform,
            evidence_type=evidence_type,
            evidence_filename=evidence_filename,
            evidence_observed_at=evidence_observed_at,
            evidence_sheet=evidence_sheet,
            request_options=request_options,
        )
        return _response.data

    def read_tenant_owned_evidence_import_metadata(
        self, import_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvidenceImport:
        """
        Parameters
        ----------
        import_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvidenceImport
            Evidence-import metadata without stored rows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_tenant_owned_evidence_import_metadata(
            import_id="importId",
        )
        """
        _response = self._raw_client.read_tenant_owned_evidence_import_metadata(
            import_id, request_options=request_options
        )
        return _response.data

    def materialize_durable_metric_observations_from_one_tenant_owned_evidence_import(
        self, import_id: str, *, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MetricMaterialization:
        """
        Requires operator or higher and an Idempotency-Key. The Evidence import is resolved inside the authenticated tenant. Recognized finite decimal values are persisted with period, grain, provenance, and quality metadata. Monetary rows without an explicit ISO 4217 currency are quarantined and never emitted as observations. A failed materialization remains independently inspectable and never rolls back an already successful L3 Evidence import or report sync.

        Parameters
        ----------
        import_id : str

        idempotency_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricMaterialization
            Newly persisted or idempotently replayed materialization

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.materialize_durable_metric_observations_from_one_tenant_owned_evidence_import(
            import_id="importId",
            idempotency_key="Idempotency-Key",
        )
        """
        _response = self._raw_client.materialize_durable_metric_observations_from_one_tenant_owned_evidence_import(
            import_id, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def list_persisted_metric_observations_owned_by_the_authenticated_tenant(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        evidence_import_id: typing.Optional[str] = None,
        platform: typing.Optional[MarketplaceId] = None,
        metric_key: typing.Optional[str] = None,
        currency: typing.Optional[GetV1MetricObservationsRequestCurrency] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1MetricObservationsResponse:
        """
        Viewer access. Results remain currency-isolated; the API does not aggregate or convert monetary observations across currencies.

        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        evidence_import_id : typing.Optional[str]

        platform : typing.Optional[MarketplaceId]

        metric_key : typing.Optional[str]

        currency : typing.Optional[GetV1MetricObservationsRequestCurrency]
            Uppercase ISO 4217 currency code. Omit only when querying non-monetary observations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1MetricObservationsResponse
            Stable cursor page of tenant-owned observations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_persisted_metric_observations_owned_by_the_authenticated_tenant()
        """
        _response = self._raw_client.list_persisted_metric_observations_owned_by_the_authenticated_tenant(
            limit=limit,
            cursor=cursor,
            evidence_import_id=evidence_import_id,
            platform=platform,
            metric_key=metric_key,
            currency=currency,
            request_options=request_options,
        )
        return _response.data

    def read_one_persisted_metric_observation_owned_by_the_authenticated_tenant(
        self, observation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetricObservation:
        """
        Parameters
        ----------
        observation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricObservation
            Tenant-owned metric observation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_persisted_metric_observation_owned_by_the_authenticated_tenant(
            observation_id="observationId",
        )
        """
        _response = self._raw_client.read_one_persisted_metric_observation_owned_by_the_authenticated_tenant(
            observation_id, request_options=request_options
        )
        return _response.data

    def list_persisted_metric_materialization_attempts_owned_by_the_authenticated_tenant(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        evidence_import_id: typing.Optional[str] = None,
        status: typing.Optional[GetV1MetricMaterializationsRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1MetricMaterializationsResponse:
        """
        Viewer access. Successful, partial, quarantined, and failed attempts remain durable and visible after refresh.

        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        evidence_import_id : typing.Optional[str]

        status : typing.Optional[GetV1MetricMaterializationsRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1MetricMaterializationsResponse
            Stable cursor page of materialization attempts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_persisted_metric_materialization_attempts_owned_by_the_authenticated_tenant()
        """
        _response = self._raw_client.list_persisted_metric_materialization_attempts_owned_by_the_authenticated_tenant(
            limit=limit,
            cursor=cursor,
            evidence_import_id=evidence_import_id,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def materialize_a_bounded_page_of_existing_tenant_evidence_imports(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1MetricMaterializationsBackfillResponse:
        """
        Requires admin or owner. Backfill is always explicit, bounded to at most 100 imports per call, and cursor-resumable; it never fabricates Evidence or silently scans every tenant import.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]
            Opaque tenant-scoped cursor returned by the previous backfill page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1MetricMaterializationsBackfillResponse
            Persisted materialization results for the processed page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.materialize_a_bounded_page_of_existing_tenant_evidence_imports(
            limit=1,
        )
        """
        _response = self._raw_client.materialize_a_bounded_page_of_existing_tenant_evidence_imports(
            limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    def list_tenant_owned_multi_agent_workflow_runs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AgentRunsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AgentRunsResponse
            Agent-run summaries; evidence bodies are omitted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_multi_agent_workflow_runs()
        """
        _response = self._raw_client.list_tenant_owned_multi_agent_workflow_runs(
            limit=limit, request_options=request_options
        )
        return _response.data

    def create_an_idempotent_weekly_ops_council_run(
        self, *, idempotency_key: str, request: AgentRunRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRun:
        """
        Persists user-supplied real evidence but does not call a model until execute.

        Parameters
        ----------
        idempotency_key : str

        request : AgentRunRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            Existing idempotent run or newly requested run

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_an_idempotent_weekly_ops_council_run(
            idempotency_key="idempotencyKey",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_an_idempotent_weekly_ops_council_run(
            idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    def list_tenant_owned_daily_ops_schedules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1DailyOpsSchedulesResponse:
        """
        Viewer-or-higher. Schedules are calendar-day operations, not the legacy interval `/v1/schedules` resource.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1DailyOpsSchedulesResponse
            Tenant schedules

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_daily_ops_schedules()
        """
        _response = self._raw_client.list_tenant_owned_daily_ops_schedules(request_options=request_options)
        return _response.data

    def create_a_daily_ops_schedule(
        self,
        *,
        name: str,
        platform: MarketplaceId,
        objective: str,
        timezone_name: str,
        local_time: str,
        graph_version_id: str,
        evidence_selectors: typing.Sequence[DailyOpsEvidenceSelector],
        max_source_age_hours: typing.Optional[int] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyOpsSchedule:
        """
        Operator-or-higher. The IANA timezone and local clock time define the business date and DST behavior.

        Parameters
        ----------
        name : str

        platform : MarketplaceId

        objective : str

        timezone_name : str
            IANA timezone name, for example `America/Los_Angeles`.

        local_time : str
            24-hour wall-clock time in timezone_name.

        graph_version_id : str

        evidence_selectors : typing.Sequence[DailyOpsEvidenceSelector]

        max_source_age_hours : typing.Optional[int]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsSchedule
            Persisted Daily Ops schedule

        Examples
        --------
        from fern import (
            DailyOpsEvidenceSelector,
            EvidenceReportType,
            FernApi,
            MarketplaceId,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_a_daily_ops_schedule(
            name="name",
            platform=MarketplaceId.ALIEXPRESS,
            objective="objective",
            timezone_name="timezone_name",
            local_time="local_time",
            graph_version_id="graph_version_id",
            evidence_selectors=[
                DailyOpsEvidenceSelector(
                    report_type=EvidenceReportType.AMAZON_BUSINESS_REPORT,
                )
            ],
        )
        """
        _response = self._raw_client.create_a_daily_ops_schedule(
            name=name,
            platform=platform,
            objective=objective,
            timezone_name=timezone_name,
            local_time=local_time,
            graph_version_id=graph_version_id,
            evidence_selectors=evidence_selectors,
            max_source_age_hours=max_source_age_hours,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def read_a_tenant_owned_daily_ops_schedule(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyOpsSchedule:
        """
        Parameters
        ----------
        schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsSchedule
            Daily Ops schedule

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_a_tenant_owned_daily_ops_schedule(
            schedule_id="scheduleId",
        )
        """
        _response = self._raw_client.read_a_tenant_owned_daily_ops_schedule(
            schedule_id, request_options=request_options
        )
        return _response.data

    def replace_a_daily_ops_schedule_configuration(
        self,
        schedule_id: str,
        *,
        max_source_age_hours: int,
        enabled: bool,
        name: str,
        platform: MarketplaceId,
        objective: str,
        timezone_name: str,
        local_time: str,
        graph_version_id: str,
        evidence_selectors: typing.Sequence[DailyOpsEvidenceSelector],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyOpsSchedule:
        """
        Operator-or-higher. Full replacement prevents accidental partial timezone, graph, or evidence-selector configuration.

        Parameters
        ----------
        schedule_id : str

        max_source_age_hours : int

        enabled : bool

        name : str

        platform : MarketplaceId

        objective : str

        timezone_name : str
            IANA timezone name, for example `America/Los_Angeles`.

        local_time : str
            24-hour wall-clock time in timezone_name.

        graph_version_id : str

        evidence_selectors : typing.Sequence[DailyOpsEvidenceSelector]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsSchedule
            Updated persisted schedule

        Examples
        --------
        from fern import (
            DailyOpsEvidenceSelector,
            EvidenceReportType,
            FernApi,
            MarketplaceId,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.replace_a_daily_ops_schedule_configuration(
            schedule_id="scheduleId",
            name="name",
            platform=MarketplaceId.ALIEXPRESS,
            objective="objective",
            timezone_name="timezone_name",
            local_time="local_time",
            graph_version_id="graph_version_id",
            evidence_selectors=[
                DailyOpsEvidenceSelector(
                    report_type=EvidenceReportType.AMAZON_BUSINESS_REPORT,
                )
            ],
            max_source_age_hours=1,
            enabled=True,
        )
        """
        _response = self._raw_client.replace_a_daily_ops_schedule_configuration(
            schedule_id,
            max_source_age_hours=max_source_age_hours,
            enabled=enabled,
            name=name,
            platform=platform,
            objective=objective,
            timezone_name=timezone_name,
            local_time=local_time,
            graph_version_id=graph_version_id,
            evidence_selectors=evidence_selectors,
            request_options=request_options,
        )
        return _response.data

    def create_or_return_the_local_date_daily_ops_occurrence(
        self,
        schedule_id: str,
        *,
        idempotency_key: str,
        local_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyOpsRun:
        """
        Operator-or-higher. Repeating a trigger for the same tenant, schedule, and local date returns the durable occurrence; no second Daily Ops run is created.

        Parameters
        ----------
        schedule_id : str

        idempotency_key : str

        local_date : typing.Optional[dt.date]
            Optional schedule-local business date; omitted means the current date in the schedule timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsRun
            Durable local-date occurrence

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_or_return_the_local_date_daily_ops_occurrence(
            schedule_id="scheduleId",
            idempotency_key="Idempotency-Key",
        )
        """
        _response = self._raw_client.create_or_return_the_local_date_daily_ops_occurrence(
            schedule_id, idempotency_key=idempotency_key, local_date=local_date, request_options=request_options
        )
        return _response.data

    def list_tenant_owned_daily_ops_occurrences(
        self,
        *,
        schedule_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1DailyOpsRunsResponse:
        """
        Viewer-or-higher. Filter by the owning Daily Ops schedule, not by a cross-tenant run ID.

        Parameters
        ----------
        schedule_id : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1DailyOpsRunsResponse
            Tenant Daily Ops runs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_daily_ops_occurrences()
        """
        _response = self._raw_client.list_tenant_owned_daily_ops_occurrences(
            schedule_id=schedule_id, limit=limit, request_options=request_options
        )
        return _response.data

    def read_a_tenant_owned_daily_ops_occurrence(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyOpsRun:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsRun
            Daily Ops occurrence and durable state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_a_tenant_owned_daily_ops_occurrence(
            run_id="runId",
        )
        """
        _response = self._raw_client.read_a_tenant_owned_daily_ops_occurrence(run_id, request_options=request_options)
        return _response.data

    def read_the_persisted_eligible_daily_ops_brief(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyOpsBriefEnvelope:
        """
        Viewer-or-higher. Completed operational briefs require a final approved Reviewer verdict; empty and Reviewer-blocked occurrences may persist explicit non-actionable briefs. Returns 409 when no brief exists.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsBriefEnvelope
            Daily Ops occurrence with its persisted brief

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_the_persisted_eligible_daily_ops_brief(
            run_id="runId",
        )
        """
        _response = self._raw_client.read_the_persisted_eligible_daily_ops_brief(
            run_id, request_options=request_options
        )
        return _response.data

    def execute_one_queued_daily_ops_occurrence(
        self, run_id: str, *, request: EmptyRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyOpsRun:
        """
        Operator-or-higher. Executes the published graph with persisted inputs, produces a brief only after Reviewer approval, and exposes no external-write tool.

        Parameters
        ----------
        run_id : str

        request : EmptyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsRun
            Updated durable Daily Ops run

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.execute_one_queued_daily_ops_occurrence(
            run_id="runId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.execute_one_queued_daily_ops_occurrence(
            run_id, request=request, request_options=request_options
        )
        return _response.data

    def retry_one_failed_or_blocked_daily_ops_occurrence(
        self,
        run_id: str,
        *,
        idempotency_key: str,
        request: EmptyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyOpsRun:
        """
        Operator-or-higher. Retry changes durable state and is protected by Idempotency-Key; it never creates a second local-date occurrence.

        Parameters
        ----------
        run_id : str

        idempotency_key : str

        request : EmptyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsRun
            Retried durable Daily Ops run

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.retry_one_failed_or_blocked_daily_ops_occurrence(
            run_id="runId",
            idempotency_key="Idempotency-Key",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.retry_one_failed_or_blocked_daily_ops_occurrence(
            run_id, idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    def list_tenant_owned_agent_graph_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AgentGraphsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AgentGraphsResponse
            Versioned graph definitions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_agent_graph_definitions()
        """
        _response = self._raw_client.list_tenant_owned_agent_graph_definitions(request_options=request_options)
        return _response.data

    def create_an_immutable_versioned_agent_graph_definition(
        self, *, name: str, definition: AgentGraphDefinition, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphBundle:
        """
        Parameters
        ----------
        name : str

        definition : AgentGraphDefinition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphBundle
            Graph created with initial draft version

        Examples
        --------
        from fern import (
            AgentGraphDefinition,
            FernApi,
            GraphEdge,
            GraphNode,
            GraphNodeExpansion,
            GraphNodeInstructionKey,
            GraphNodeKey,
            GraphNodeRole,
            ToolPolicy,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_an_immutable_versioned_agent_graph_definition(
            name="name",
            definition=AgentGraphDefinition(
                schema_version=1,
                nodes=[
                    GraphNode(
                        key=GraphNodeKey.EVIDENCE_ANALYST,
                        role=GraphNodeRole.EVIDENCE_ANALYST,
                        expansion=GraphNodeExpansion.SINGLETON,
                        optional=True,
                        skill_ids=["skill_ids"],
                        instruction_key=GraphNodeInstructionKey.WEEKLY_OPS_EVIDENCE_ANALYST_V1,
                        tool_policy=ToolPolicy(
                            allowed_tools=["allowed_tools"],
                            max_tool_calls=1,
                        ),
                    )
                ],
                edges=[
                    GraphEdge(
                        from_="from",
                        to="to",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.create_an_immutable_versioned_agent_graph_definition(
            name=name, definition=definition, request_options=request_options
        )
        return _response.data

    def read_a_tenant_owned_agent_graph_and_versions(
        self, graph_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphBundle:
        """
        Parameters
        ----------
        graph_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphBundle
            Graph with version history

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_a_tenant_owned_agent_graph_and_versions(
            graph_id="graphId",
        )
        """
        _response = self._raw_client.read_a_tenant_owned_agent_graph_and_versions(
            graph_id, request_options=request_options
        )
        return _response.data

    def create_a_new_draft_graph_version(
        self,
        graph_id: str,
        *,
        definition: AgentGraphDefinition,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentGraphVersion:
        """
        Parameters
        ----------
        graph_id : str

        definition : AgentGraphDefinition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphVersion
            Immutable draft version

        Examples
        --------
        from fern import (
            AgentGraphDefinition,
            FernApi,
            GraphEdge,
            GraphNode,
            GraphNodeExpansion,
            GraphNodeInstructionKey,
            GraphNodeKey,
            GraphNodeRole,
            ToolPolicy,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_a_new_draft_graph_version(
            graph_id="graphId",
            definition=AgentGraphDefinition(
                schema_version=1,
                nodes=[
                    GraphNode(
                        key=GraphNodeKey.EVIDENCE_ANALYST,
                        role=GraphNodeRole.EVIDENCE_ANALYST,
                        expansion=GraphNodeExpansion.SINGLETON,
                        optional=True,
                        skill_ids=["skill_ids"],
                        instruction_key=GraphNodeInstructionKey.WEEKLY_OPS_EVIDENCE_ANALYST_V1,
                        tool_policy=ToolPolicy(
                            allowed_tools=["allowed_tools"],
                            max_tool_calls=1,
                        ),
                    )
                ],
                edges=[
                    GraphEdge(
                        from_="from",
                        to="to",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.create_a_new_draft_graph_version(
            graph_id, definition=definition, request_options=request_options
        )
        return _response.data

    def read_one_tenant_owned_agent_graph_version(
        self, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphVersion:
        """
        Parameters
        ----------
        version_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphVersion
            Draft, published, or retired graph version

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_tenant_owned_agent_graph_version(
            version_id="versionId",
        )
        """
        _response = self._raw_client.read_one_tenant_owned_agent_graph_version(
            version_id, request_options=request_options
        )
        return _response.data

    def publish_a_graph_version_after_validation_and_review(
        self, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphVersion:
        """
        Parameters
        ----------
        version_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphVersion
            Published immutable version

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.publish_a_graph_version_after_validation_and_review(
            version_id="versionId",
        )
        """
        _response = self._raw_client.publish_a_graph_version_after_validation_and_review(
            version_id, request_options=request_options
        )
        return _response.data

    def publish_a_graph_version_using_the_nested_compatibility_route(
        self, graph_id: str, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphVersion:
        """
        Parameters
        ----------
        graph_id : str

        version_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphVersion
            Published immutable version

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.publish_a_graph_version_using_the_nested_compatibility_route(
            graph_id="graphId",
            version_id="versionId",
        )
        """
        _response = self._raw_client.publish_a_graph_version_using_the_nested_compatibility_route(
            graph_id, version_id, request_options=request_options
        )
        return _response.data

    def read_a_tenant_owned_run_with_tasks_artifacts_and_events(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRunBundle:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRunBundle
            Complete durable workflow state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_a_tenant_owned_run_with_tasks_artifacts_and_events(
            run_id="runId",
        )
        """
        _response = self._raw_client.read_a_tenant_owned_run_with_tasks_artifacts_and_events(
            run_id, request_options=request_options
        )
        return _response.data

    def read_an_incremental_event_page_for_a_run(
        self,
        run_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1AgentRunsRunIdEventsResponse:
        """
        Parameters
        ----------
        run_id : str

        after : typing.Optional[str]
            SQLite event sequence cursor returned as next_cursor

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AgentRunsRunIdEventsResponse
            Tenant-scoped event page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_an_incremental_event_page_for_a_run(
            run_id="runId",
        )
        """
        _response = self._raw_client.read_an_incremental_event_page_for_a_run(
            run_id, after=after, limit=limit, request_options=request_options
        )
        return _response.data

    def execute_the_bound_domain_agent_graph_and_independent_reviewer(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRunBundle:
        """
        Requires operator or higher plus OPENAI_API_KEY and EAI_OPENAI_MODEL in the server environment. Application code runs the Evidence Analyst and dynamic marketplace specialists in parallel, then the optional cross-platform controller, Manager, and Reviewer sequentially. No model tools are exposed.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRunBundle
            Completed run, or the existing result for an already completed run

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.execute_the_bound_domain_agent_graph_and_independent_reviewer(
            run_id="runId",
        )
        """
        _response = self._raw_client.execute_the_bound_domain_agent_graph_and_independent_reviewer(
            run_id, request_options=request_options
        )
        return _response.data

    def evaluate_a_completed_weekly_ops_run_with_deterministic_graders(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentEvaluation:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentEvaluation
            Persisted workflow evaluation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.evaluate_a_completed_weekly_ops_run_with_deterministic_graders(
            run_id="runId",
        )
        """
        _response = self._raw_client.evaluate_a_completed_weekly_ops_run_with_deterministic_graders(
            run_id, request_options=request_options
        )
        return _response.data

    def list_persisted_evaluations_for_a_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AgentRunsRunIdEvaluationsResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AgentRunsRunIdEvaluationsResponse
            Workflow evaluations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_persisted_evaluations_for_a_run(
            run_id="runId",
        )
        """
        _response = self._raw_client.list_persisted_evaluations_for_a_run(run_id, request_options=request_options)
        return _response.data

    def list_tenant_owned_durable_jobs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1JobsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1JobsResponse
            Durable jobs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_durable_jobs()
        """
        _response = self._raw_client.list_tenant_owned_durable_jobs(limit=limit, request_options=request_options)
        return _response.data

    def enqueue_an_agent_run_for_background_execution(
        self,
        *,
        idempotency_key: str,
        run_id: str,
        max_attempts: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
        """
        Parameters
        ----------
        idempotency_key : str

        run_id : str

        max_attempts : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            Existing or new durable job

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.enqueue_an_agent_run_for_background_execution(
            idempotency_key="Idempotency-Key",
            run_id="run_id",
        )
        """
        _response = self._raw_client.enqueue_an_agent_run_for_background_execution(
            idempotency_key=idempotency_key, run_id=run_id, max_attempts=max_attempts, request_options=request_options
        )
        return _response.data

    def read_one_tenant_owned_durable_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Job:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            Durable job

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_tenant_owned_durable_job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.read_one_tenant_owned_durable_job(job_id, request_options=request_options)
        return _response.data

    def list_tenant_owned_interval_schedules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1SchedulesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1SchedulesResponse
            Schedules

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_owned_interval_schedules()
        """
        _response = self._raw_client.list_tenant_owned_interval_schedules(request_options=request_options)
        return _response.data

    def schedule_repeated_weekly_ops_runs(
        self, *, request: ScheduleCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> Schedule:
        """
        Parameters
        ----------
        request : ScheduleCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schedule
            Schedule created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schedule_repeated_weekly_ops_runs(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.schedule_repeated_weekly_ops_runs(request=request, request_options=request_options)
        return _response.data

    def enable_or_disable_a_schedule(
        self, schedule_id: str, *, enabled: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> Schedule:
        """
        Parameters
        ----------
        schedule_id : str

        enabled : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schedule
            Updated schedule

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.enable_or_disable_a_schedule(
            schedule_id="scheduleId",
            enabled=True,
        )
        """
        _response = self._raw_client.enable_or_disable_a_schedule(
            schedule_id, enabled=enabled, request_options=request_options
        )
        return _response.data

    def list_requested_actions_awaiting_a_second_actor(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ApprovalsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ApprovalsResponse
            Approval inbox

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_requested_actions_awaiting_a_second_actor()
        """
        _response = self._raw_client.list_requested_actions_awaiting_a_second_actor(request_options=request_options)
        return _response.data

    def read_a_tenants_operational_control_plane_snapshot(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MissionControl:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MissionControl
            Real persisted counts, attention queues, recent runs, and schedules

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_a_tenants_operational_control_plane_snapshot()
        """
        _response = self._raw_client.read_a_tenants_operational_control_plane_snapshot(request_options=request_options)
        return _response.data

    def stream_tenant_scoped_mission_control_changes(
        self,
        *,
        after: typing.Optional[int] = None,
        last_event_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Viewer-or-higher bearer authentication is required. This is a fetch-streaming endpoint, not an EventSource endpoint: clients send `Authorization: Bearer` and MUST NOT put an API key in a query string, URL, browser storage, logs, or referrers. Resume position is a non-sensitive tenant-local integer cursor: `Last-Event-ID` takes precedence over `after`; neither is a credential or tenant identifier. The server emits SSE frames (`id`, `event`, `data`) with `mission.update`, `mission.reset`, and `mission.reconnect` events, plus comment-only heartbeats. `mission.update` is an incremental safe metadata update; `mission.reset` requires the client to discard its cached stream state and refetch `/v1/mission-control`; and `mission.reconnect` asks the client to reconnect after its advertised delay. A retention gap also produces `mission.reset`. The server may end a stream at its bounded backlog or lifetime; reconnect with the last received event id.

        Parameters
        ----------
        after : typing.Optional[int]
            Non-sensitive tenant-local fallback cursor used only if `Last-Event-ID` is absent.

        last_event_id : typing.Optional[int]
            Non-sensitive tenant-local monotonic stream cursor. Takes precedence over `after` when both are supplied.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            A bounded `text/event-stream` response. Events contain safe metadata only; event data never contains API keys, Authorization values, credentials, evidence rows, action payloads, or cross-tenant identifiers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        response = client.stream_tenant_scoped_mission_control_changes()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_tenant_scoped_mission_control_changes(
            after=after, last_event_id=last_event_id, request_options=request_options
        ) as r:
            yield from r.data

    def read_tenant_scoped_pilot_readiness_and_local_worker_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PilotStatus:
        """
        Viewer-or-higher bearer authentication is required. This endpoint reports the current authenticated tenant only. Credential fields report presence and safe aggregate counts only—never secrets, API keys, token values, reference names, or provider responses. `attention`, `blocked`, degraded, stale, stopping, or stopped is an explicit operational state, not a successful external Amazon or OpenAI smoke. Worker status is evaluated at read time from the latest heartbeat.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PilotStatus
            Closed tenant readiness and single-process worker status snapshot

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_tenant_scoped_pilot_readiness_and_local_worker_health()
        """
        _response = self._raw_client.read_tenant_scoped_pilot_readiness_and_local_worker_health(
            request_options=request_options
        )
        return _response.data

    def list_tenant_scoped_durable_assurance_runs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AssuranceRunsResponse:
        """
        Viewer-or-higher may read only the authenticated tenant's immutable Assurance runs.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AssuranceRunsResponse
            Tenant-scoped assurance run history

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.list_tenant_scoped_durable_assurance_runs()
        """
        _response = self._raw_client.list_tenant_scoped_durable_assurance_runs(
            limit=limit, request_options=request_options
        )
        return _response.data

    def run_a_tenant_assurance_evaluation_or_security_check(
        self,
        *,
        idempotency_key: str,
        kind: AssuranceRunRequestKind,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssuranceRun:
        """
        Admin-only and idempotent. Only `eval` and `security` can be created over HTTP. `restore` Assurance runs are written only by a verified CLI restore into its newly created target database; no API can forge a restore result. An eval with no eligible real workflow data completes `blocked` with an explicit check instead of inventing a passing evaluation.

        Parameters
        ----------
        idempotency_key : str

        kind : AssuranceRunRequestKind

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssuranceRun
            Persisted immutable assurance run; replay returns the same run for the same key and kind

        Examples
        --------
        from fern import AssuranceRunRequestKind, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.run_a_tenant_assurance_evaluation_or_security_check(
            idempotency_key="Idempotency-Key",
            kind=AssuranceRunRequestKind.EVAL,
        )
        """
        _response = self._raw_client.run_a_tenant_assurance_evaluation_or_security_check(
            idempotency_key=idempotency_key, kind=kind, request_options=request_options
        )
        return _response.data

    def read_one_tenant_scoped_assurance_run(
        self, assurance_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssuranceRun:
        """
        Parameters
        ----------
        assurance_run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssuranceRun
            Immutable tenant-scoped assurance result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_one_tenant_scoped_assurance_run(
            assurance_run_id="assuranceRunId",
        )
        """
        _response = self._raw_client.read_one_tenant_scoped_assurance_run(
            assurance_run_id, request_options=request_options
        )
        return _response.data

    def read_an_evidence_backed_operating_brief_for_one_marketplace(
        self,
        *,
        platform: typing.Optional[MarketplaceId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OperatingBriefing:
        """
        Metrics are calculated only from recognized fields in tenant-owned Evidence; priorities and agent state come from persisted Weekly Ops runs.

        Parameters
        ----------
        platform : typing.Optional[MarketplaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperatingBriefing
            Tenant-safe marketplace briefing without synthetic metrics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_an_evidence_backed_operating_brief_for_one_marketplace()
        """
        _response = self._raw_client.read_an_evidence_backed_operating_brief_for_one_marketplace(
            platform=platform, request_options=request_options
        )
        return _response.data

    def read_the_live_platform_report_workflow_and_action_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RuntimeCatalog:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RuntimeCatalog
            Runtime catalog generated from ontology and service registries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_the_live_platform_report_workflow_and_action_catalog()
        """
        _response = self._raw_client.read_the_live_platform_report_workflow_and_action_catalog(
            request_options=request_options
        )
        return _response.data

    def read_tenant_audit_events(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AuditResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AuditResponse
            Audit events

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_tenant_audit_events()
        """
        _response = self._raw_client.read_tenant_audit_events(limit=limit, request_options=request_options)
        return _response.data

    def read_tenant_owned_connector_records(
        self, *, provider: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1RecordsResponse:
        """
        Parameters
        ----------
        provider : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1RecordsResponse
            Connector records

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_tenant_owned_connector_records()
        """
        _response = self._raw_client.read_tenant_owned_connector_records(
            provider=provider, request_options=request_options
        )
        return _response.data

    def read_disposable_process_counters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1MetricsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1MetricsResponse
            Process counters; not business metrics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.read_disposable_process_counters()
        """
        _response = self._raw_client.read_disposable_process_counters(request_options=request_options)
        return _response.data


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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def check_process_liveness(self, *, request_options: typing.Optional[RequestOptions] = None) -> Health:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Health
            Healthy

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.check_process_liveness()


        asyncio.run(main())
        """
        _response = await self._raw_client.check_process_liveness(request_options=request_options)
        return _response.data

    async def check_database_and_schema_readiness(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Readiness:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Readiness
            Database schema ready

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.check_database_and_schema_readiness()


        asyncio.run(main())
        """
        _response = await self._raw_client.check_database_and_schema_readiness(request_options=request_options)
        return _response.data

    async def bootstrap_the_loopback_only_explicit_demo_ui_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DemoSession:
        """
        Available only when the separate `demo` CLI starts a database containing exactly one Demo tenant. Normal Runtime API processes return 404.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DemoSession
            Temporary Demo key kept in page memory and revoked when the Demo server stops

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bootstrap_the_loopback_only_explicit_demo_ui_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.bootstrap_the_loopback_only_explicit_demo_ui_session(
            request_options=request_options
        )
        return _response.data

    async def read_the_authenticated_principal(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Principal:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Principal
            Authenticated principal

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_the_authenticated_principal()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_the_authenticated_principal(request_options=request_options)
        return _response.data

    async def list_users_owned_by_the_authenticated_tenant(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1UsersResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1UsersResponse
            Tenant users without API-key material

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_users_owned_by_the_authenticated_tenant()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users_owned_by_the_authenticated_tenant(request_options=request_options)
        return _response.data

    async def create_a_tenant_user(
        self, *, email: str, role: Role, request_options: typing.Optional[RequestOptions] = None
    ) -> UserEnvelope:
        """
        Admins may assign roles up to admin; only an owner may assign owner.

        Parameters
        ----------
        email : str

        role : Role

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserEnvelope
            User created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Role

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_a_tenant_user(
                email="email",
                role=Role.VIEWER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_tenant_user(email=email, role=role, request_options=request_options)
        return _response.data

    async def change_a_tenant_users_role(
        self, user_id: str, *, role: Role, request_options: typing.Optional[RequestOptions] = None
    ) -> UserEnvelope:
        """
        Self-role changes and last-owner demotion are rejected.

        Parameters
        ----------
        user_id : str

        role : Role

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserEnvelope
            Role updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Role

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.change_a_tenant_users_role(
                user_id="userId",
                role=Role.VIEWER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_a_tenant_users_role(
            user_id, role=role, request_options=request_options
        )
        return _response.data

    async def list_tenant_api_key_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ApiKeysResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ApiKeysResponse
            Key metadata without secrets or hashes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_api_key_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_api_key_metadata(request_options=request_options)
        return _response.data

    async def issue_a_one_time_api_key_for_a_tenant_user(
        self, *, user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyIssued:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyIssued
            One-time API key; the clear value is never returned again

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.issue_a_one_time_api_key_for_a_tenant_user(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_a_one_time_api_key_for_a_tenant_user(
            user_id=user_id, request_options=request_options
        )
        return _response.data

    async def rotate_the_current_callers_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1ApiKeysRotateResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1ApiKeysRotateResponse
            Replacement one-time API key

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rotate_the_current_callers_api_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.rotate_the_current_callers_api_key(request_options=request_options)
        return _response.data

    async def revoke_a_tenant_api_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1ApiKeysKeyIdRevokeResponse:
        """
        Parameters
        ----------
        key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1ApiKeysKeyIdRevokeResponse
            Key revoked

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.revoke_a_tenant_api_key(
                key_id="keyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_a_tenant_api_key(key_id, request_options=request_options)
        return _response.data

    async def list_tenant_owned_marketplace_connector_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ConnectorsResponse:
        """
        Viewer, operator, admin, and owner roles may read the safe connector representation for their authenticated tenant. Credential values and environment-variable names are never returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ConnectorsResponse
            Connector accounts with redacted credential references

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_marketplace_connector_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_marketplace_connector_accounts(
            request_options=request_options
        )
        return _response.data

    async def create_a_tenant_marketplace_connector_account(
        self, *, request: ConnectorRegistration, request_options: typing.Optional[RequestOptions] = None
    ) -> MarketplaceAccount:
        """
        Requires admin or owner role. The request stores only non-secret connector details and environment-variable references; the response redacts those references to a present marker.

        Parameters
        ----------
        request : ConnectorRegistration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarketplaceAccount
            Connector account created with initial unchecked health

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ConnectorRegistration_Shopify,
            ShopifyConnectorConfig,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_a_tenant_marketplace_connector_account(
                request=ConnectorRegistration_Shopify(
                    external_account_id="external_account_id",
                    config=ShopifyConnectorConfig(
                        shop_domain="shop_domain",
                        api_version="api_version",
                        credential_ref="credential_ref",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_tenant_marketplace_connector_account(
            request=request, request_options=request_options
        )
        return _response.data

    async def read_one_tenant_marketplace_connector_account(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarketplaceAccount:
        """
        Viewer, operator, admin, and owner roles may read the safe connector representation. An account outside the authenticated tenant is indistinguishable from a missing account and returns 404.

        Parameters
        ----------
        account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarketplaceAccount
            Connector account with redacted credential references

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_tenant_marketplace_connector_account(
                account_id="accountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_tenant_marketplace_connector_account(
            account_id, request_options=request_options
        )
        return _response.data

    async def update_a_tenant_marketplace_connector_account(
        self,
        account_id: str,
        *,
        config: ConnectorUpdateRequestConfig,
        external_account_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MarketplaceAccount:
        """
        Requires admin or owner role. The existing provider is retained; config is required and must contain the complete provider configuration. external_account_id is optional and omitted values retain the existing identifier. Updating config resets health to unchecked and clears the persisted health error.

        Parameters
        ----------
        account_id : str

        config : ConnectorUpdateRequestConfig

        external_account_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarketplaceAccount
            Updated connector account with health reset to unchecked

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ShopifyConnectorConfig

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_a_tenant_marketplace_connector_account(
                account_id="accountId",
                config=ShopifyConnectorConfig(
                    shop_domain="shop_domain",
                    api_version="api_version",
                    credential_ref="credential_ref",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_tenant_marketplace_connector_account(
            account_id, config=config, external_account_id=external_account_id, request_options=request_options
        )
        return _response.data

    async def run_and_persist_a_connector_health_check(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MarketplaceAccount:
        """
        Requires operator, admin, or owner role. The check is synchronous and provider-specific: Amazon SP-API verifies Sellers marketplaceParticipations, Amazon Ads verifies the configured profile through the regional v2 profiles endpoint without reading campaigns, and Shopify reads shop.json. A failed remote check is persisted on the account and returned as a 200 response with health_status, health_error_code, and health_error_message; it is not converted into a transient success.

        Parameters
        ----------
        account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarketplaceAccount
            Connector account after the persisted health result; health_status may be healthy, unhealthy, or misconfigured

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.run_and_persist_a_connector_health_check(
                account_id="accountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_and_persist_a_connector_health_check(
            account_id, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_provider_connectivity_tests(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderSmokeTestList:
        """
        Viewer, operator, admin, and owner roles may read bounded, safe metadata for their authenticated tenant. Listing never calls a provider and never returns credentials, request bodies, response bodies, model output, idempotency keys, fingerprints, or lease state.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderSmokeTestList
            Persisted provider connectivity test history, newest first

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_provider_connectivity_tests()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_provider_connectivity_tests(
            limit=limit, request_options=request_options
        )
        return _response.data

    async def run_an_audited_live_provider_connectivity_test(
        self,
        *,
        idempotency_key: str,
        request: ProviderSmokeRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderSmokeTest:
        """
        Requires operator, admin, or owner role and Idempotency-Key. OpenAI performs one minimal Responses API request against the fixed official endpoint with store disabled and does not persist model output or raw response data. Amazon SP-API and Shopify reuse their existing read-only account health adapters and update connector health. Results and safe failure codes are tenant-persisted and hash-chain audited. A per-target cooldown may return 429 before any provider call.

        Parameters
        ----------
        idempotency_key : str
            Safe tenant-local provider-test replay key; the same key cannot be reused for a different provider target.

        request : ProviderSmokeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderSmokeTest
            Newly completed test, terminal idempotent replay, or active running replay

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            OpenAiProviderSmokeRequest,
            OpenAiProviderSmokeRequestProvider,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.run_an_audited_live_provider_connectivity_test(
                idempotency_key="Idempotency-Key",
                request=OpenAiProviderSmokeRequest(
                    provider=OpenAiProviderSmokeRequestProvider.OPENAI,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_an_audited_live_provider_connectivity_test(
            idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    async def read_one_tenant_owned_provider_connectivity_test(
        self, smoke_test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderSmokeTest:
        """
        A test outside the authenticated tenant is indistinguishable from a missing test and returns 404. The response contains safe metadata only and never calls a provider.

        Parameters
        ----------
        smoke_test_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderSmokeTest
            Persisted safe provider connectivity test metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_tenant_owned_provider_connectivity_test(
                smoke_test_id="smokeTestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_tenant_owned_provider_connectivity_test(
            smoke_test_id, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_amazon_report_recipes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ReportRecipesResponse:
        """
        Viewer, operator, admin, and owner roles may read persisted report recipes for their authenticated tenant. Listing recipes never calls Amazon.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportRecipesResponse
            Persisted report recipes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_amazon_report_recipes()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_amazon_report_recipes(request_options=request_options)
        return _response.data

    async def persist_an_amazon_report_recipe(
        self,
        *,
        connector_account_id: str,
        name: str,
        recipe_key: ReportRecipeKey,
        marketplace_ids: typing.Sequence[str],
        interval_minutes: int,
        lookback_days: int,
        enabled: bool,
        next_run_at: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportRecipe:
        """
        Requires operator or owner role. This L2 operation validates and persists configuration only; it does not call Amazon, enqueue work, or create a report. connector_account_id must reference an Amazon SP-API account in the authenticated tenant, and marketplace_ids must be a subset of that account's configured marketplaces.

        Parameters
        ----------
        connector_account_id : str

        name : str

        recipe_key : ReportRecipeKey

        marketplace_ids : typing.Sequence[str]

        interval_minutes : int

        lookback_days : int

        enabled : bool

        next_run_at : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportRecipe
            Persisted report recipe

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, ReportRecipeKey

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.persist_an_amazon_report_recipe(
                connector_account_id="connector_account_id",
                name="name",
                recipe_key=ReportRecipeKey.SALES_TRAFFIC_DAILY,
                marketplace_ids=["marketplace_ids"],
                interval_minutes=1,
                lookback_days=1,
                enabled=True,
                next_run_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.persist_an_amazon_report_recipe(
            connector_account_id=connector_account_id,
            name=name,
            recipe_key=recipe_key,
            marketplace_ids=marketplace_ids,
            interval_minutes=interval_minutes,
            lookback_days=lookback_days,
            enabled=enabled,
            next_run_at=next_run_at,
            request_options=request_options,
        )
        return _response.data

    async def read_one_tenant_owned_amazon_report_recipe(
        self, recipe_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportRecipe:
        """
        Viewer, operator, admin, and owner roles may read a persisted recipe. A recipe outside the authenticated tenant returns 404.

        Parameters
        ----------
        recipe_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportRecipe
            Persisted report recipe

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_tenant_owned_amazon_report_recipe(
                recipe_id="recipeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_tenant_owned_amazon_report_recipe(
            recipe_id, request_options=request_options
        )
        return _response.data

    async def update_a_tenant_owned_amazon_report_recipe(
        self,
        recipe_id: str,
        *,
        name: str,
        recipe_key: ReportRecipeKey,
        marketplace_ids: typing.Sequence[str],
        interval_minutes: int,
        lookback_days: int,
        enabled: bool,
        next_run_at: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportRecipe:
        """
        Requires operator or owner role. All recipe fields except connector_account_id are required on update; the connector account cannot be changed. The update persists configuration only and never calls Amazon. marketplace_ids must remain a subset of the linked account's configured marketplaces.

        Parameters
        ----------
        recipe_id : str

        name : str

        recipe_key : ReportRecipeKey

        marketplace_ids : typing.Sequence[str]

        interval_minutes : int

        lookback_days : int

        enabled : bool

        next_run_at : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportRecipe
            Updated persisted report recipe

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, ReportRecipeKey

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_a_tenant_owned_amazon_report_recipe(
                recipe_id="recipeId",
                name="name",
                recipe_key=ReportRecipeKey.SALES_TRAFFIC_DAILY,
                marketplace_ids=["marketplace_ids"],
                interval_minutes=1,
                lookback_days=1,
                enabled=True,
                next_run_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_tenant_owned_amazon_report_recipe(
            recipe_id,
            name=name,
            recipe_key=recipe_key,
            marketplace_ids=marketplace_ids,
            interval_minutes=interval_minutes,
            lookback_days=lookback_days,
            enabled=enabled,
            next_run_at=next_run_at,
            request_options=request_options,
        )
        return _response.data

    async def enqueue_an_idempotent_amazon_report_synchronization(
        self, recipe_id: str, *, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportSync:
        """
        Requires operator or higher and an Idempotency-Key. The linked Amazon account and recipe must be enabled and healthy. A durable L3 worker performs the official createReport call, then getReport polling through IN_QUEUE, IN_PROGRESS, DONE, CANCELLED, or FATAL, document retrieval, bounded normalization, and Evidence import asynchronously. HTTP 429 responses preserve Retry-After and use bounded retry/backoff; L3 never writes to Amazon and does not automatically schedule enabled recipes.

        Parameters
        ----------
        recipe_id : str

        idempotency_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportSync
            Durable queued or replayed report sync

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.enqueue_an_idempotent_amazon_report_synchronization(
                recipe_id="recipeId",
                idempotency_key="Idempotency-Key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enqueue_an_idempotent_amazon_report_synchronization(
            recipe_id, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_amazon_report_syncs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ReportSyncsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportSyncsResponse
            Durable report synchronization states

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_amazon_report_syncs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_amazon_report_syncs(
            limit=limit, request_options=request_options
        )
        return _response.data

    async def read_one_tenant_owned_amazon_report_sync(
        self, sync_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportSync:
        """
        Parameters
        ----------
        sync_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportSync
            Durable report synchronization state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_tenant_owned_amazon_report_sync(
                sync_id="syncId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_tenant_owned_amazon_report_sync(
            sync_id, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_amazon_ads_capability_gates(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AdsCapabilityGatesResponse:
        """
        Viewer, operator, admin, and owner roles may inspect persisted Ads admission checks. The route never probes Amazon.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AdsCapabilityGatesResponse
            Persisted Ads capability gates

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_amazon_ads_capability_gates()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_amazon_ads_capability_gates(
            limit=limit, request_options=request_options
        )
        return _response.data

    async def run_a_read_only_amazon_ads_capability_gate(
        self,
        *,
        idempotency_key: str,
        connector_account_id: str,
        attestation_reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdsCapabilityGate:
        """
        Requires admin or owner role and Idempotency-Key. The request performs only live probes and records an optional external attestation reference; it never creates or mutates an Ads resource.

        Parameters
        ----------
        idempotency_key : str

        connector_account_id : str

        attestation_reference : typing.Optional[str]
            Opaque external approval reference; secrets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdsCapabilityGate
            Persisted terminal gate result, or a replayed checking result held by another request lease

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.run_a_read_only_amazon_ads_capability_gate(
                idempotency_key="Idempotency-Key",
                connector_account_id="connector_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_a_read_only_amazon_ads_capability_gate(
            idempotency_key=idempotency_key,
            connector_account_id=connector_account_id,
            attestation_reference=attestation_reference,
            request_options=request_options,
        )
        return _response.data

    async def read_one_tenant_owned_amazon_ads_capability_gate(
        self, gate_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AdsCapabilityGate:
        """
        Parameters
        ----------
        gate_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdsCapabilityGate
            Persisted Ads capability gate

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_tenant_owned_amazon_ads_capability_gate(
                gate_id="gateId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_tenant_owned_amazon_ads_capability_gate(
            gate_id, request_options=request_options
        )
        return _response.data

    async def read_the_conditional_amazon_ads_adapter_status(
        self,
        *,
        connector_account_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdsAdapterStatus:
        """
        Viewer-readable negative gate. This build does not register Ads write adapters, routes, or actions. `eligible_not_installed` is the only non-blocked fixture outcome permitted until a future release satisfies the L5 gate and approval safeguards.

        Parameters
        ----------
        connector_account_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdsAdapterStatus
            Tenant-scoped adapter status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_the_conditional_amazon_ads_adapter_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_the_conditional_amazon_ads_adapter_status(
            connector_account_id=connector_account_id, request_options=request_options
        )
        return _response.data

    async def request_an_idempotent_action(
        self, *, idempotency_key: str, request: ActionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        idempotency_key : str

        request : ActionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            Existing idempotent action or newly requested action

        Examples
        --------
        import asyncio

        from fern import (
            ActionRequest_ShopifySyncProducts,
            AsyncFernApi,
            ShopifySyncActionRequestPayload,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.request_an_idempotent_action(
                idempotency_key="Idempotency-Key",
                request=ActionRequest_ShopifySyncProducts(
                    payload=ShopifySyncActionRequestPayload(
                        external_account_id="external_account_id",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_an_idempotent_action(
            idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    async def approve_a_requested_action_as_a_second_actor(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            Approved action

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.approve_a_requested_action_as_a_second_actor(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approve_a_requested_action_as_a_second_actor(
            action_id, request_options=request_options
        )
        return _response.data

    async def execute_an_approved_action(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            Executed action

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.execute_an_approved_action(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_an_approved_action(action_id, request_options=request_options)
        return _response.data

    async def re_queue_a_failed_or_expired_execution_without_bypassing_approval(
        self, action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Action:
        """
        Parameters
        ----------
        action_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Action
            Action returned to approved state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.re_queue_a_failed_or_expired_execution_without_bypassing_approval(
                action_id="actionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.re_queue_a_failed_or_expired_execution_without_bypassing_approval(
            action_id, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_durable_proposals(
        self,
        *,
        status: typing.Optional[ProposalStatus] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ProposalsResponse:
        """
        Parameters
        ----------
        status : typing.Optional[ProposalStatus]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ProposalsResponse
            Full tenant proposal representations, including local decisions, linked executions, immutable versions, and capability preflight state.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_durable_proposals()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_durable_proposals(
            status=status, limit=limit, request_options=request_options
        )
        return _response.data

    async def derive_an_idempotent_proposal_from_an_approved_daily_ops_priority(
        self,
        *,
        idempotency_key: str,
        request: ProposalCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Proposal:
        """
        Requires operator or higher and an Idempotency-Key. Source run, graph, evidence, metric, and payload lineage are derived server-side; caller-supplied provenance is rejected. Replaying the original create request after a revision returns the same resource's current representation, while a changed request with the same key conflicts.

        Parameters
        ----------
        idempotency_key : str

        request : ProposalCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Existing idempotent proposal or newly created draft

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            HumanReviewProposalPayload,
            ProposalCreateRequest_HumanReview,
            ProposalRisk,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.derive_an_idempotent_proposal_from_an_approved_daily_ops_priority(
                idempotency_key="Idempotency-Key",
                request=ProposalCreateRequest_HumanReview(
                    daily_ops_run_id="daily_ops_run_id",
                    priority_rank=1,
                    rollback_plan="rollback_plan",
                    payload=HumanReviewProposalPayload(
                        instructions="instructions",
                    ),
                    risk=ProposalRisk.LOW,
                    expires_at=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.derive_an_idempotent_proposal_from_an_approved_daily_ops_priority(
            idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    async def read_a_tenant_owned_proposal_and_its_local_decisions(
        self, proposal_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Proposal:
        """
        Parameters
        ----------
        proposal_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Proposal detail

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_a_tenant_owned_proposal_and_its_local_decisions(
                proposal_id="proposalId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_a_tenant_owned_proposal_and_its_local_decisions(
            proposal_id, request_options=request_options
        )
        return _response.data

    async def revise_a_draft_or_revision_required_proposal_optimistically(
        self,
        proposal_id: str,
        *,
        expected_version: int,
        title: typing.Optional[str] = OMIT,
        rationale: typing.Optional[str] = OMIT,
        expected_impact: typing.Optional[str] = OMIT,
        rollback_plan: typing.Optional[str] = OMIT,
        operation: typing.Optional[ProposalOperation] = OMIT,
        payload: typing.Optional[ProposalPayload] = OMIT,
        risk: typing.Optional[ProposalRisk] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Proposal:
        """
        Parameters
        ----------
        proposal_id : str

        expected_version : int

        title : typing.Optional[str]

        rationale : typing.Optional[str]

        expected_impact : typing.Optional[str]

        rollback_plan : typing.Optional[str]

        operation : typing.Optional[ProposalOperation]

        payload : typing.Optional[ProposalPayload]

        risk : typing.Optional[ProposalRisk]

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Revised proposal with a new version and payload hash

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.revise_a_draft_or_revision_required_proposal_optimistically(
                proposal_id="proposalId",
                expected_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revise_a_draft_or_revision_required_proposal_optimistically(
            proposal_id,
            expected_version=expected_version,
            title=title,
            rationale=rationale,
            expected_impact=expected_impact,
            rollback_plan=rollback_plan,
            operation=operation,
            payload=payload,
            risk=risk,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    async def submit_a_proposal_to_local_human_review(
        self, proposal_id: str, *, expected_version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> Proposal:
        """
        Parameters
        ----------
        proposal_id : str

        expected_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Submitted proposal

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.submit_a_proposal_to_local_human_review(
                proposal_id="proposalId",
                expected_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_proposal_to_local_human_review(
            proposal_id, expected_version=expected_version, request_options=request_options
        )
        return _response.data

    async def record_a_local_human_review_decision_optimistically(
        self,
        proposal_id: str,
        *,
        expected_version: int,
        decision: ProposalDecisionType,
        comment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Proposal:
        """
        Local human.review is an auditable local decision only. A requester cannot approve their own proposal and this endpoint does not attest marketplace or Ads approval.

        Parameters
        ----------
        proposal_id : str

        expected_version : int

        decision : ProposalDecisionType

        comment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Proposal
            Proposal after decision

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProposalDecisionType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.record_a_local_human_review_decision_optimistically(
                proposal_id="proposalId",
                expected_version=1,
                decision=ProposalDecisionType.APPROVE,
                comment="comment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_a_local_human_review_decision_optimistically(
            proposal_id,
            expected_version=expected_version,
            decision=decision,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    async def idempotently_execute_an_approved_safe_read_proposal(
        self,
        proposal_id: str,
        *,
        idempotency_key: str,
        expected_version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProposalExecution:
        """
        Requires operator or higher and an Idempotency-Key. Only existing safe read Action operations are permitted; no general marketplace or Amazon Ads write is registered. A different Idempotency-Key for the same approved proposal version conflicts rather than creating a second execution.

        Parameters
        ----------
        proposal_id : str

        idempotency_key : str

        expected_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProposalExecution
            Existing idempotent execution or a new durable execution

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.idempotently_execute_an_approved_safe_read_proposal(
                proposal_id="proposalId",
                idempotency_key="Idempotency-Key",
                expected_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.idempotently_execute_an_approved_safe_read_proposal(
            proposal_id,
            idempotency_key=idempotency_key,
            expected_version=expected_version,
            request_options=request_options,
        )
        return _response.data

    async def retry_a_failed_proposal_execution_idempotently_on_its_existing_durable_execution_row(
        self,
        proposal_id: str,
        *,
        idempotency_key: str,
        expected_version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProposalExecution:
        """
        Requires a new Idempotency-Key and the current version. Retry records a retry receipt and reuses the existing execution row; it does not create another execution resource. A connector failure is durably recorded before a 502 response.

        Parameters
        ----------
        proposal_id : str

        idempotency_key : str

        expected_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProposalExecution
            Existing idempotent retry or the same durable execution after its retry transition

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.retry_a_failed_proposal_execution_idempotently_on_its_existing_durable_execution_row(
                proposal_id="proposalId",
                idempotency_key="Idempotency-Key",
                expected_version=1,
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.retry_a_failed_proposal_execution_idempotently_on_its_existing_durable_execution_row(
                proposal_id,
                idempotency_key=idempotency_key,
                expected_version=expected_version,
                request_options=request_options,
            )
        )
        return _response.data

    async def list_tenant_owned_proposal_executions(
        self,
        *,
        proposal_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ProposalExecutionsResponse:
        """
        Parameters
        ----------
        proposal_id : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ProposalExecutionsResponse
            Proposal execution history

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_proposal_executions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_proposal_executions(
            proposal_id=proposal_id, limit=limit, request_options=request_options
        )
        return _response.data

    async def read_one_tenant_owned_proposal_execution(
        self, execution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProposalExecution:
        """
        Parameters
        ----------
        execution_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProposalExecution
            Proposal execution detail

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_tenant_owned_proposal_execution(
                execution_id="executionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_tenant_owned_proposal_execution(
            execution_id, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_csv_evidence_imports(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1EvidenceImportsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1EvidenceImportsResponse
            Import metadata without stored rows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_csv_evidence_imports()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_csv_evidence_imports(
            limit=limit, request_options=request_options
        )
        return _response.data

    async def parse_and_persist_real_marketplace_csv_evidence(
        self,
        *,
        idempotency_key: str,
        evidence_platform: MarketplaceId,
        evidence_type: EvidenceReportType,
        evidence_filename: str,
        evidence_observed_at: dt.datetime,
        evidence_sheet: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvidenceImport:
        """
        Amazon typed reports receive semantic column validation; platform_generic accepts any ontology marketplace.

        Parameters
        ----------
        idempotency_key : str

        evidence_platform : MarketplaceId

        evidence_type : EvidenceReportType

        evidence_filename : str

        evidence_observed_at : dt.datetime

        evidence_sheet : typing.Optional[str]
            Optional worksheet name for XLSX; defaults to the active sheet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvidenceImport
            Persisted evidence-import metadata; parsed rows remain server-side

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, EvidenceReportType, MarketplaceId

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.parse_and_persist_real_marketplace_csv_evidence(
                idempotency_key="Idempotency-Key",
                evidence_platform=MarketplaceId.ALIEXPRESS,
                evidence_type=EvidenceReportType.AMAZON_BUSINESS_REPORT,
                evidence_filename="X-Evidence-Filename",
                evidence_observed_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.parse_and_persist_real_marketplace_csv_evidence(
            idempotency_key=idempotency_key,
            evidence_platform=evidence_platform,
            evidence_type=evidence_type,
            evidence_filename=evidence_filename,
            evidence_observed_at=evidence_observed_at,
            evidence_sheet=evidence_sheet,
            request_options=request_options,
        )
        return _response.data

    async def read_tenant_owned_evidence_import_metadata(
        self, import_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EvidenceImport:
        """
        Parameters
        ----------
        import_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvidenceImport
            Evidence-import metadata without stored rows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_tenant_owned_evidence_import_metadata(
                import_id="importId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_tenant_owned_evidence_import_metadata(
            import_id, request_options=request_options
        )
        return _response.data

    async def materialize_durable_metric_observations_from_one_tenant_owned_evidence_import(
        self, import_id: str, *, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> MetricMaterialization:
        """
        Requires operator or higher and an Idempotency-Key. The Evidence import is resolved inside the authenticated tenant. Recognized finite decimal values are persisted with period, grain, provenance, and quality metadata. Monetary rows without an explicit ISO 4217 currency are quarantined and never emitted as observations. A failed materialization remains independently inspectable and never rolls back an already successful L3 Evidence import or report sync.

        Parameters
        ----------
        import_id : str

        idempotency_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricMaterialization
            Newly persisted or idempotently replayed materialization

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.materialize_durable_metric_observations_from_one_tenant_owned_evidence_import(
                import_id="importId",
                idempotency_key="Idempotency-Key",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.materialize_durable_metric_observations_from_one_tenant_owned_evidence_import(
                import_id, idempotency_key=idempotency_key, request_options=request_options
            )
        )
        return _response.data

    async def list_persisted_metric_observations_owned_by_the_authenticated_tenant(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        evidence_import_id: typing.Optional[str] = None,
        platform: typing.Optional[MarketplaceId] = None,
        metric_key: typing.Optional[str] = None,
        currency: typing.Optional[GetV1MetricObservationsRequestCurrency] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1MetricObservationsResponse:
        """
        Viewer access. Results remain currency-isolated; the API does not aggregate or convert monetary observations across currencies.

        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        evidence_import_id : typing.Optional[str]

        platform : typing.Optional[MarketplaceId]

        metric_key : typing.Optional[str]

        currency : typing.Optional[GetV1MetricObservationsRequestCurrency]
            Uppercase ISO 4217 currency code. Omit only when querying non-monetary observations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1MetricObservationsResponse
            Stable cursor page of tenant-owned observations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_persisted_metric_observations_owned_by_the_authenticated_tenant()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_persisted_metric_observations_owned_by_the_authenticated_tenant(
            limit=limit,
            cursor=cursor,
            evidence_import_id=evidence_import_id,
            platform=platform,
            metric_key=metric_key,
            currency=currency,
            request_options=request_options,
        )
        return _response.data

    async def read_one_persisted_metric_observation_owned_by_the_authenticated_tenant(
        self, observation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetricObservation:
        """
        Parameters
        ----------
        observation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricObservation
            Tenant-owned metric observation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_persisted_metric_observation_owned_by_the_authenticated_tenant(
                observation_id="observationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_persisted_metric_observation_owned_by_the_authenticated_tenant(
            observation_id, request_options=request_options
        )
        return _response.data

    async def list_persisted_metric_materialization_attempts_owned_by_the_authenticated_tenant(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        evidence_import_id: typing.Optional[str] = None,
        status: typing.Optional[GetV1MetricMaterializationsRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1MetricMaterializationsResponse:
        """
        Viewer access. Successful, partial, quarantined, and failed attempts remain durable and visible after refresh.

        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        evidence_import_id : typing.Optional[str]

        status : typing.Optional[GetV1MetricMaterializationsRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1MetricMaterializationsResponse
            Stable cursor page of materialization attempts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_persisted_metric_materialization_attempts_owned_by_the_authenticated_tenant()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.list_persisted_metric_materialization_attempts_owned_by_the_authenticated_tenant(
                limit=limit,
                cursor=cursor,
                evidence_import_id=evidence_import_id,
                status=status,
                request_options=request_options,
            )
        )
        return _response.data

    async def materialize_a_bounded_page_of_existing_tenant_evidence_imports(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1MetricMaterializationsBackfillResponse:
        """
        Requires admin or owner. Backfill is always explicit, bounded to at most 100 imports per call, and cursor-resumable; it never fabricates Evidence or silently scans every tenant import.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]
            Opaque tenant-scoped cursor returned by the previous backfill page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1MetricMaterializationsBackfillResponse
            Persisted materialization results for the processed page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.materialize_a_bounded_page_of_existing_tenant_evidence_imports(
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.materialize_a_bounded_page_of_existing_tenant_evidence_imports(
            limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_multi_agent_workflow_runs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AgentRunsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AgentRunsResponse
            Agent-run summaries; evidence bodies are omitted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_multi_agent_workflow_runs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_multi_agent_workflow_runs(
            limit=limit, request_options=request_options
        )
        return _response.data

    async def create_an_idempotent_weekly_ops_council_run(
        self, *, idempotency_key: str, request: AgentRunRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRun:
        """
        Persists user-supplied real evidence but does not call a model until execute.

        Parameters
        ----------
        idempotency_key : str

        request : AgentRunRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRun
            Existing idempotent run or newly requested run

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_an_idempotent_weekly_ops_council_run(
                idempotency_key="idempotencyKey",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_an_idempotent_weekly_ops_council_run(
            idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_daily_ops_schedules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1DailyOpsSchedulesResponse:
        """
        Viewer-or-higher. Schedules are calendar-day operations, not the legacy interval `/v1/schedules` resource.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1DailyOpsSchedulesResponse
            Tenant schedules

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_daily_ops_schedules()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_daily_ops_schedules(request_options=request_options)
        return _response.data

    async def create_a_daily_ops_schedule(
        self,
        *,
        name: str,
        platform: MarketplaceId,
        objective: str,
        timezone_name: str,
        local_time: str,
        graph_version_id: str,
        evidence_selectors: typing.Sequence[DailyOpsEvidenceSelector],
        max_source_age_hours: typing.Optional[int] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyOpsSchedule:
        """
        Operator-or-higher. The IANA timezone and local clock time define the business date and DST behavior.

        Parameters
        ----------
        name : str

        platform : MarketplaceId

        objective : str

        timezone_name : str
            IANA timezone name, for example `America/Los_Angeles`.

        local_time : str
            24-hour wall-clock time in timezone_name.

        graph_version_id : str

        evidence_selectors : typing.Sequence[DailyOpsEvidenceSelector]

        max_source_age_hours : typing.Optional[int]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsSchedule
            Persisted Daily Ops schedule

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DailyOpsEvidenceSelector,
            EvidenceReportType,
            MarketplaceId,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_a_daily_ops_schedule(
                name="name",
                platform=MarketplaceId.ALIEXPRESS,
                objective="objective",
                timezone_name="timezone_name",
                local_time="local_time",
                graph_version_id="graph_version_id",
                evidence_selectors=[
                    DailyOpsEvidenceSelector(
                        report_type=EvidenceReportType.AMAZON_BUSINESS_REPORT,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_daily_ops_schedule(
            name=name,
            platform=platform,
            objective=objective,
            timezone_name=timezone_name,
            local_time=local_time,
            graph_version_id=graph_version_id,
            evidence_selectors=evidence_selectors,
            max_source_age_hours=max_source_age_hours,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def read_a_tenant_owned_daily_ops_schedule(
        self, schedule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyOpsSchedule:
        """
        Parameters
        ----------
        schedule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsSchedule
            Daily Ops schedule

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_a_tenant_owned_daily_ops_schedule(
                schedule_id="scheduleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_a_tenant_owned_daily_ops_schedule(
            schedule_id, request_options=request_options
        )
        return _response.data

    async def replace_a_daily_ops_schedule_configuration(
        self,
        schedule_id: str,
        *,
        max_source_age_hours: int,
        enabled: bool,
        name: str,
        platform: MarketplaceId,
        objective: str,
        timezone_name: str,
        local_time: str,
        graph_version_id: str,
        evidence_selectors: typing.Sequence[DailyOpsEvidenceSelector],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyOpsSchedule:
        """
        Operator-or-higher. Full replacement prevents accidental partial timezone, graph, or evidence-selector configuration.

        Parameters
        ----------
        schedule_id : str

        max_source_age_hours : int

        enabled : bool

        name : str

        platform : MarketplaceId

        objective : str

        timezone_name : str
            IANA timezone name, for example `America/Los_Angeles`.

        local_time : str
            24-hour wall-clock time in timezone_name.

        graph_version_id : str

        evidence_selectors : typing.Sequence[DailyOpsEvidenceSelector]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsSchedule
            Updated persisted schedule

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DailyOpsEvidenceSelector,
            EvidenceReportType,
            MarketplaceId,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.replace_a_daily_ops_schedule_configuration(
                schedule_id="scheduleId",
                name="name",
                platform=MarketplaceId.ALIEXPRESS,
                objective="objective",
                timezone_name="timezone_name",
                local_time="local_time",
                graph_version_id="graph_version_id",
                evidence_selectors=[
                    DailyOpsEvidenceSelector(
                        report_type=EvidenceReportType.AMAZON_BUSINESS_REPORT,
                    )
                ],
                max_source_age_hours=1,
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_a_daily_ops_schedule_configuration(
            schedule_id,
            max_source_age_hours=max_source_age_hours,
            enabled=enabled,
            name=name,
            platform=platform,
            objective=objective,
            timezone_name=timezone_name,
            local_time=local_time,
            graph_version_id=graph_version_id,
            evidence_selectors=evidence_selectors,
            request_options=request_options,
        )
        return _response.data

    async def create_or_return_the_local_date_daily_ops_occurrence(
        self,
        schedule_id: str,
        *,
        idempotency_key: str,
        local_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyOpsRun:
        """
        Operator-or-higher. Repeating a trigger for the same tenant, schedule, and local date returns the durable occurrence; no second Daily Ops run is created.

        Parameters
        ----------
        schedule_id : str

        idempotency_key : str

        local_date : typing.Optional[dt.date]
            Optional schedule-local business date; omitted means the current date in the schedule timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsRun
            Durable local-date occurrence

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_or_return_the_local_date_daily_ops_occurrence(
                schedule_id="scheduleId",
                idempotency_key="Idempotency-Key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_return_the_local_date_daily_ops_occurrence(
            schedule_id, idempotency_key=idempotency_key, local_date=local_date, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_daily_ops_occurrences(
        self,
        *,
        schedule_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1DailyOpsRunsResponse:
        """
        Viewer-or-higher. Filter by the owning Daily Ops schedule, not by a cross-tenant run ID.

        Parameters
        ----------
        schedule_id : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1DailyOpsRunsResponse
            Tenant Daily Ops runs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_daily_ops_occurrences()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_daily_ops_occurrences(
            schedule_id=schedule_id, limit=limit, request_options=request_options
        )
        return _response.data

    async def read_a_tenant_owned_daily_ops_occurrence(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyOpsRun:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsRun
            Daily Ops occurrence and durable state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_a_tenant_owned_daily_ops_occurrence(
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_a_tenant_owned_daily_ops_occurrence(
            run_id, request_options=request_options
        )
        return _response.data

    async def read_the_persisted_eligible_daily_ops_brief(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyOpsBriefEnvelope:
        """
        Viewer-or-higher. Completed operational briefs require a final approved Reviewer verdict; empty and Reviewer-blocked occurrences may persist explicit non-actionable briefs. Returns 409 when no brief exists.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsBriefEnvelope
            Daily Ops occurrence with its persisted brief

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_the_persisted_eligible_daily_ops_brief(
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_the_persisted_eligible_daily_ops_brief(
            run_id, request_options=request_options
        )
        return _response.data

    async def execute_one_queued_daily_ops_occurrence(
        self, run_id: str, *, request: EmptyRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyOpsRun:
        """
        Operator-or-higher. Executes the published graph with persisted inputs, produces a brief only after Reviewer approval, and exposes no external-write tool.

        Parameters
        ----------
        run_id : str

        request : EmptyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsRun
            Updated durable Daily Ops run

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.execute_one_queued_daily_ops_occurrence(
                run_id="runId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_one_queued_daily_ops_occurrence(
            run_id, request=request, request_options=request_options
        )
        return _response.data

    async def retry_one_failed_or_blocked_daily_ops_occurrence(
        self,
        run_id: str,
        *,
        idempotency_key: str,
        request: EmptyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyOpsRun:
        """
        Operator-or-higher. Retry changes durable state and is protected by Idempotency-Key; it never creates a second local-date occurrence.

        Parameters
        ----------
        run_id : str

        idempotency_key : str

        request : EmptyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyOpsRun
            Retried durable Daily Ops run

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.retry_one_failed_or_blocked_daily_ops_occurrence(
                run_id="runId",
                idempotency_key="Idempotency-Key",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retry_one_failed_or_blocked_daily_ops_occurrence(
            run_id, idempotency_key=idempotency_key, request=request, request_options=request_options
        )
        return _response.data

    async def list_tenant_owned_agent_graph_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AgentGraphsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AgentGraphsResponse
            Versioned graph definitions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_agent_graph_definitions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_agent_graph_definitions(request_options=request_options)
        return _response.data

    async def create_an_immutable_versioned_agent_graph_definition(
        self, *, name: str, definition: AgentGraphDefinition, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphBundle:
        """
        Parameters
        ----------
        name : str

        definition : AgentGraphDefinition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphBundle
            Graph created with initial draft version

        Examples
        --------
        import asyncio

        from fern import (
            AgentGraphDefinition,
            AsyncFernApi,
            GraphEdge,
            GraphNode,
            GraphNodeExpansion,
            GraphNodeInstructionKey,
            GraphNodeKey,
            GraphNodeRole,
            ToolPolicy,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_an_immutable_versioned_agent_graph_definition(
                name="name",
                definition=AgentGraphDefinition(
                    schema_version=1,
                    nodes=[
                        GraphNode(
                            key=GraphNodeKey.EVIDENCE_ANALYST,
                            role=GraphNodeRole.EVIDENCE_ANALYST,
                            expansion=GraphNodeExpansion.SINGLETON,
                            optional=True,
                            skill_ids=["skill_ids"],
                            instruction_key=GraphNodeInstructionKey.WEEKLY_OPS_EVIDENCE_ANALYST_V1,
                            tool_policy=ToolPolicy(
                                allowed_tools=["allowed_tools"],
                                max_tool_calls=1,
                            ),
                        )
                    ],
                    edges=[
                        GraphEdge(
                            from_="from",
                            to="to",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_an_immutable_versioned_agent_graph_definition(
            name=name, definition=definition, request_options=request_options
        )
        return _response.data

    async def read_a_tenant_owned_agent_graph_and_versions(
        self, graph_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphBundle:
        """
        Parameters
        ----------
        graph_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphBundle
            Graph with version history

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_a_tenant_owned_agent_graph_and_versions(
                graph_id="graphId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_a_tenant_owned_agent_graph_and_versions(
            graph_id, request_options=request_options
        )
        return _response.data

    async def create_a_new_draft_graph_version(
        self,
        graph_id: str,
        *,
        definition: AgentGraphDefinition,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentGraphVersion:
        """
        Parameters
        ----------
        graph_id : str

        definition : AgentGraphDefinition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphVersion
            Immutable draft version

        Examples
        --------
        import asyncio

        from fern import (
            AgentGraphDefinition,
            AsyncFernApi,
            GraphEdge,
            GraphNode,
            GraphNodeExpansion,
            GraphNodeInstructionKey,
            GraphNodeKey,
            GraphNodeRole,
            ToolPolicy,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_a_new_draft_graph_version(
                graph_id="graphId",
                definition=AgentGraphDefinition(
                    schema_version=1,
                    nodes=[
                        GraphNode(
                            key=GraphNodeKey.EVIDENCE_ANALYST,
                            role=GraphNodeRole.EVIDENCE_ANALYST,
                            expansion=GraphNodeExpansion.SINGLETON,
                            optional=True,
                            skill_ids=["skill_ids"],
                            instruction_key=GraphNodeInstructionKey.WEEKLY_OPS_EVIDENCE_ANALYST_V1,
                            tool_policy=ToolPolicy(
                                allowed_tools=["allowed_tools"],
                                max_tool_calls=1,
                            ),
                        )
                    ],
                    edges=[
                        GraphEdge(
                            from_="from",
                            to="to",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_draft_graph_version(
            graph_id, definition=definition, request_options=request_options
        )
        return _response.data

    async def read_one_tenant_owned_agent_graph_version(
        self, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphVersion:
        """
        Parameters
        ----------
        version_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphVersion
            Draft, published, or retired graph version

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_tenant_owned_agent_graph_version(
                version_id="versionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_tenant_owned_agent_graph_version(
            version_id, request_options=request_options
        )
        return _response.data

    async def publish_a_graph_version_after_validation_and_review(
        self, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphVersion:
        """
        Parameters
        ----------
        version_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphVersion
            Published immutable version

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.publish_a_graph_version_after_validation_and_review(
                version_id="versionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_a_graph_version_after_validation_and_review(
            version_id, request_options=request_options
        )
        return _response.data

    async def publish_a_graph_version_using_the_nested_compatibility_route(
        self, graph_id: str, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentGraphVersion:
        """
        Parameters
        ----------
        graph_id : str

        version_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentGraphVersion
            Published immutable version

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.publish_a_graph_version_using_the_nested_compatibility_route(
                graph_id="graphId",
                version_id="versionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_a_graph_version_using_the_nested_compatibility_route(
            graph_id, version_id, request_options=request_options
        )
        return _response.data

    async def read_a_tenant_owned_run_with_tasks_artifacts_and_events(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRunBundle:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRunBundle
            Complete durable workflow state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_a_tenant_owned_run_with_tasks_artifacts_and_events(
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_a_tenant_owned_run_with_tasks_artifacts_and_events(
            run_id, request_options=request_options
        )
        return _response.data

    async def read_an_incremental_event_page_for_a_run(
        self,
        run_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1AgentRunsRunIdEventsResponse:
        """
        Parameters
        ----------
        run_id : str

        after : typing.Optional[str]
            SQLite event sequence cursor returned as next_cursor

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AgentRunsRunIdEventsResponse
            Tenant-scoped event page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_an_incremental_event_page_for_a_run(
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_an_incremental_event_page_for_a_run(
            run_id, after=after, limit=limit, request_options=request_options
        )
        return _response.data

    async def execute_the_bound_domain_agent_graph_and_independent_reviewer(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentRunBundle:
        """
        Requires operator or higher plus OPENAI_API_KEY and EAI_OPENAI_MODEL in the server environment. Application code runs the Evidence Analyst and dynamic marketplace specialists in parallel, then the optional cross-platform controller, Manager, and Reviewer sequentially. No model tools are exposed.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRunBundle
            Completed run, or the existing result for an already completed run

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.execute_the_bound_domain_agent_graph_and_independent_reviewer(
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_the_bound_domain_agent_graph_and_independent_reviewer(
            run_id, request_options=request_options
        )
        return _response.data

    async def evaluate_a_completed_weekly_ops_run_with_deterministic_graders(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentEvaluation:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentEvaluation
            Persisted workflow evaluation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.evaluate_a_completed_weekly_ops_run_with_deterministic_graders(
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.evaluate_a_completed_weekly_ops_run_with_deterministic_graders(
            run_id, request_options=request_options
        )
        return _response.data

    async def list_persisted_evaluations_for_a_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AgentRunsRunIdEvaluationsResponse:
        """
        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AgentRunsRunIdEvaluationsResponse
            Workflow evaluations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_persisted_evaluations_for_a_run(
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_persisted_evaluations_for_a_run(run_id, request_options=request_options)
        return _response.data

    async def list_tenant_owned_durable_jobs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1JobsResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1JobsResponse
            Durable jobs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_durable_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_durable_jobs(limit=limit, request_options=request_options)
        return _response.data

    async def enqueue_an_agent_run_for_background_execution(
        self,
        *,
        idempotency_key: str,
        run_id: str,
        max_attempts: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
        """
        Parameters
        ----------
        idempotency_key : str

        run_id : str

        max_attempts : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            Existing or new durable job

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.enqueue_an_agent_run_for_background_execution(
                idempotency_key="Idempotency-Key",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enqueue_an_agent_run_for_background_execution(
            idempotency_key=idempotency_key, run_id=run_id, max_attempts=max_attempts, request_options=request_options
        )
        return _response.data

    async def read_one_tenant_owned_durable_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Job:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            Durable job

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_tenant_owned_durable_job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_tenant_owned_durable_job(job_id, request_options=request_options)
        return _response.data

    async def list_tenant_owned_interval_schedules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1SchedulesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1SchedulesResponse
            Schedules

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_owned_interval_schedules()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_owned_interval_schedules(request_options=request_options)
        return _response.data

    async def schedule_repeated_weekly_ops_runs(
        self, *, request: ScheduleCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> Schedule:
        """
        Parameters
        ----------
        request : ScheduleCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schedule
            Schedule created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schedule_repeated_weekly_ops_runs(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schedule_repeated_weekly_ops_runs(
            request=request, request_options=request_options
        )
        return _response.data

    async def enable_or_disable_a_schedule(
        self, schedule_id: str, *, enabled: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> Schedule:
        """
        Parameters
        ----------
        schedule_id : str

        enabled : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schedule
            Updated schedule

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.enable_or_disable_a_schedule(
                schedule_id="scheduleId",
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_or_disable_a_schedule(
            schedule_id, enabled=enabled, request_options=request_options
        )
        return _response.data

    async def list_requested_actions_awaiting_a_second_actor(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1ApprovalsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ApprovalsResponse
            Approval inbox

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_requested_actions_awaiting_a_second_actor()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_requested_actions_awaiting_a_second_actor(
            request_options=request_options
        )
        return _response.data

    async def read_a_tenants_operational_control_plane_snapshot(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MissionControl:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MissionControl
            Real persisted counts, attention queues, recent runs, and schedules

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_a_tenants_operational_control_plane_snapshot()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_a_tenants_operational_control_plane_snapshot(
            request_options=request_options
        )
        return _response.data

    async def stream_tenant_scoped_mission_control_changes(
        self,
        *,
        after: typing.Optional[int] = None,
        last_event_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Viewer-or-higher bearer authentication is required. This is a fetch-streaming endpoint, not an EventSource endpoint: clients send `Authorization: Bearer` and MUST NOT put an API key in a query string, URL, browser storage, logs, or referrers. Resume position is a non-sensitive tenant-local integer cursor: `Last-Event-ID` takes precedence over `after`; neither is a credential or tenant identifier. The server emits SSE frames (`id`, `event`, `data`) with `mission.update`, `mission.reset`, and `mission.reconnect` events, plus comment-only heartbeats. `mission.update` is an incremental safe metadata update; `mission.reset` requires the client to discard its cached stream state and refetch `/v1/mission-control`; and `mission.reconnect` asks the client to reconnect after its advertised delay. A retention gap also produces `mission.reset`. The server may end a stream at its bounded backlog or lifetime; reconnect with the last received event id.

        Parameters
        ----------
        after : typing.Optional[int]
            Non-sensitive tenant-local fallback cursor used only if `Last-Event-ID` is absent.

        last_event_id : typing.Optional[int]
            Non-sensitive tenant-local monotonic stream cursor. Takes precedence over `after` when both are supplied.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            A bounded `text/event-stream` response. Events contain safe metadata only; event data never contains API keys, Authorization values, credentials, evidence rows, action payloads, or cross-tenant identifiers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = client.stream_tenant_scoped_mission_control_changes()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_tenant_scoped_mission_control_changes(
            after=after, last_event_id=last_event_id, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def read_tenant_scoped_pilot_readiness_and_local_worker_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PilotStatus:
        """
        Viewer-or-higher bearer authentication is required. This endpoint reports the current authenticated tenant only. Credential fields report presence and safe aggregate counts only—never secrets, API keys, token values, reference names, or provider responses. `attention`, `blocked`, degraded, stale, stopping, or stopped is an explicit operational state, not a successful external Amazon or OpenAI smoke. Worker status is evaluated at read time from the latest heartbeat.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PilotStatus
            Closed tenant readiness and single-process worker status snapshot

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_tenant_scoped_pilot_readiness_and_local_worker_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_tenant_scoped_pilot_readiness_and_local_worker_health(
            request_options=request_options
        )
        return _response.data

    async def list_tenant_scoped_durable_assurance_runs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AssuranceRunsResponse:
        """
        Viewer-or-higher may read only the authenticated tenant's immutable Assurance runs.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AssuranceRunsResponse
            Tenant-scoped assurance run history

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_tenant_scoped_durable_assurance_runs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tenant_scoped_durable_assurance_runs(
            limit=limit, request_options=request_options
        )
        return _response.data

    async def run_a_tenant_assurance_evaluation_or_security_check(
        self,
        *,
        idempotency_key: str,
        kind: AssuranceRunRequestKind,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssuranceRun:
        """
        Admin-only and idempotent. Only `eval` and `security` can be created over HTTP. `restore` Assurance runs are written only by a verified CLI restore into its newly created target database; no API can forge a restore result. An eval with no eligible real workflow data completes `blocked` with an explicit check instead of inventing a passing evaluation.

        Parameters
        ----------
        idempotency_key : str

        kind : AssuranceRunRequestKind

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssuranceRun
            Persisted immutable assurance run; replay returns the same run for the same key and kind

        Examples
        --------
        import asyncio

        from fern import AssuranceRunRequestKind, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.run_a_tenant_assurance_evaluation_or_security_check(
                idempotency_key="Idempotency-Key",
                kind=AssuranceRunRequestKind.EVAL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_a_tenant_assurance_evaluation_or_security_check(
            idempotency_key=idempotency_key, kind=kind, request_options=request_options
        )
        return _response.data

    async def read_one_tenant_scoped_assurance_run(
        self, assurance_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssuranceRun:
        """
        Parameters
        ----------
        assurance_run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssuranceRun
            Immutable tenant-scoped assurance result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_one_tenant_scoped_assurance_run(
                assurance_run_id="assuranceRunId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_one_tenant_scoped_assurance_run(
            assurance_run_id, request_options=request_options
        )
        return _response.data

    async def read_an_evidence_backed_operating_brief_for_one_marketplace(
        self,
        *,
        platform: typing.Optional[MarketplaceId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OperatingBriefing:
        """
        Metrics are calculated only from recognized fields in tenant-owned Evidence; priorities and agent state come from persisted Weekly Ops runs.

        Parameters
        ----------
        platform : typing.Optional[MarketplaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperatingBriefing
            Tenant-safe marketplace briefing without synthetic metrics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_an_evidence_backed_operating_brief_for_one_marketplace()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_an_evidence_backed_operating_brief_for_one_marketplace(
            platform=platform, request_options=request_options
        )
        return _response.data

    async def read_the_live_platform_report_workflow_and_action_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RuntimeCatalog:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RuntimeCatalog
            Runtime catalog generated from ontology and service registries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_the_live_platform_report_workflow_and_action_catalog()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_the_live_platform_report_workflow_and_action_catalog(
            request_options=request_options
        )
        return _response.data

    async def read_tenant_audit_events(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1AuditResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1AuditResponse
            Audit events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_tenant_audit_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_tenant_audit_events(limit=limit, request_options=request_options)
        return _response.data

    async def read_tenant_owned_connector_records(
        self, *, provider: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1RecordsResponse:
        """
        Parameters
        ----------
        provider : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1RecordsResponse
            Connector records

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_tenant_owned_connector_records()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_tenant_owned_connector_records(
            provider=provider, request_options=request_options
        )
        return _response.data

    async def read_disposable_process_counters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1MetricsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1MetricsResponse
            Process counters; not business metrics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.read_disposable_process_counters()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_disposable_process_counters(request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
