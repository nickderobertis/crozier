



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action import Action
    from .action_operation import ActionOperation
    from .action_request import ActionRequest, ActionRequest_AmazonSpapiImportReport, ActionRequest_ShopifySyncProducts
    from .action_status import ActionStatus
    from .ads_adapter_status import AdsAdapterStatus
    from .ads_adapter_status_reason_codes_item import AdsAdapterStatusReasonCodesItem
    from .ads_adapter_status_region import AdsAdapterStatusRegion
    from .ads_adapter_status_status import AdsAdapterStatusStatus
    from .ads_capability_gate import AdsCapabilityGate
    from .ads_capability_gate_checks_item import AdsCapabilityGateChecksItem
    from .ads_capability_gate_checks_item_name import AdsCapabilityGateChecksItemName
    from .ads_capability_gate_checks_item_status import AdsCapabilityGateChecksItemStatus
    from .ads_capability_gate_observed_capabilities_item import AdsCapabilityGateObservedCapabilitiesItem
    from .ads_capability_gate_region import AdsCapabilityGateRegion
    from .ads_capability_gate_required_capabilities_item import AdsCapabilityGateRequiredCapabilitiesItem
    from .ads_capability_gate_status import AdsCapabilityGateStatus
    from .agent_artifact import AgentArtifact
    from .agent_artifact_content import AgentArtifactContent
    from .agent_artifact_kind import AgentArtifactKind
    from .agent_evaluation import AgentEvaluation
    from .agent_event import AgentEvent
    from .agent_graph import AgentGraph
    from .agent_graph_bundle import AgentGraphBundle
    from .agent_graph_definition import AgentGraphDefinition
    from .agent_graph_version import AgentGraphVersion
    from .agent_graph_version_status import AgentGraphVersionStatus
    from .agent_run import AgentRun
    from .agent_run_bundle import AgentRunBundle
    from .agent_run_origin import AgentRunOrigin
    from .agent_run_request import AgentRunRequest
    from .agent_run_request_workflow import AgentRunRequestWorkflow
    from .agent_run_review_status import AgentRunReviewStatus
    from .agent_run_status import AgentRunStatus
    from .agent_run_workflow import AgentRunWorkflow
    from .agent_task import AgentTask
    from .agent_task_role import AgentTaskRole
    from .agent_task_status import AgentTaskStatus
    from .amazon_ads_campaign_update_proposal_create_request import AmazonAdsCampaignUpdateProposalCreateRequest
    from .amazon_ads_campaign_update_proposal_payload import AmazonAdsCampaignUpdateProposalPayload
    from .amazon_ads_connector_config import AmazonAdsConnectorConfig
    from .amazon_ads_connector_config_region import AmazonAdsConnectorConfigRegion
    from .amazon_ads_connector_registration import AmazonAdsConnectorRegistration
    from .amazon_ads_provider_details import AmazonAdsProviderDetails
    from .amazon_ads_provider_details_region import AmazonAdsProviderDetailsRegion
    from .amazon_marketplace_catalog_entry import AmazonMarketplaceCatalogEntry
    from .amazon_marketplace_catalog_entry_region import AmazonMarketplaceCatalogEntryRegion
    from .amazon_report_import_action_request import AmazonReportImportActionRequest
    from .amazon_report_import_action_request_payload import AmazonReportImportActionRequestPayload
    from .amazon_spapi_connector_config import AmazonSpapiConnectorConfig
    from .amazon_spapi_connector_config_region import AmazonSpapiConnectorConfigRegion
    from .amazon_spapi_connector_registration import AmazonSpapiConnectorRegistration
    from .amazon_spapi_import_report_proposal_create_request import AmazonSpapiImportReportProposalCreateRequest
    from .amazon_spapi_import_report_proposal_payload import AmazonSpapiImportReportProposalPayload
    from .amazon_spapi_provider_details import AmazonSpapiProviderDetails
    from .amazon_spapi_provider_details_region import AmazonSpapiProviderDetailsRegion
    from .api_key_issued import ApiKeyIssued
    from .api_key_metadata import ApiKeyMetadata
    from .assurance_check import AssuranceCheck
    from .assurance_check_status import AssuranceCheckStatus
    from .assurance_run import AssuranceRun
    from .assurance_run_kind import AssuranceRunKind
    from .assurance_run_request_kind import AssuranceRunRequestKind
    from .assurance_run_status import AssuranceRunStatus
    from .assurance_summary import AssuranceSummary
    from .audit_event import AuditEvent
    from .briefing_agent import BriefingAgent
    from .briefing_agent_status import BriefingAgentStatus
    from .briefing_metric import BriefingMetric
    from .briefing_metric_format import BriefingMetricFormat
    from .briefing_metric_series_item import BriefingMetricSeriesItem
    from .briefing_metric_time_grain import BriefingMetricTimeGrain
    from .briefing_metric_trend_mode import BriefingMetricTrendMode
    from .briefing_metric_unit import BriefingMetricUnit
    from .connector_provider import ConnectorProvider
    from .connector_provider_catalog_entry import ConnectorProviderCatalogEntry
    from .connector_provider_details import ConnectorProviderDetails
    from .connector_record import ConnectorRecord
    from .connector_registration import (
        ConnectorRegistration,
        ConnectorRegistration_AmazonAds,
        ConnectorRegistration_AmazonSpapi,
        ConnectorRegistration_Shopify,
    )
    from .connector_update_request_config import ConnectorUpdateRequestConfig
    from .daily_ops_brief import DailyOpsBrief
    from .daily_ops_brief_envelope import DailyOpsBriefEnvelope
    from .daily_ops_brief_graph import DailyOpsBriefGraph
    from .daily_ops_brief_inputs import DailyOpsBriefInputs
    from .daily_ops_brief_kind import DailyOpsBriefKind
    from .daily_ops_brief_review_status import DailyOpsBriefReviewStatus
    from .daily_ops_brief_schedule import DailyOpsBriefSchedule
    from .daily_ops_brief_status import DailyOpsBriefStatus
    from .daily_ops_evidence_selector import DailyOpsEvidenceSelector
    from .daily_ops_run import DailyOpsRun
    from .daily_ops_run_status import DailyOpsRunStatus
    from .daily_ops_schedule import DailyOpsSchedule
    from .daily_ops_schedule_create import DailyOpsScheduleCreate
    from .daily_ops_schedule_snapshot import DailyOpsScheduleSnapshot
    from .daily_ops_source_gap import DailyOpsSourceGap
    from .daily_ops_source_gap_verdict import DailyOpsSourceGapVerdict
    from .demo_session import DemoSession
    from .demo_session_tenant_mode import DemoSessionTenantMode
    from .empty_request import EmptyRequest
    from .error_envelope import ErrorEnvelope
    from .error_envelope_error import ErrorEnvelopeError
    from .evidence_import import EvidenceImport
    from .evidence_report_type import EvidenceReportType
    from .evidence_source import EvidenceSource
    from .evidence_source_data import EvidenceSourceData
    from .get_v1ads_capability_gates_response import GetV1AdsCapabilityGatesResponse
    from .get_v1agent_graphs_response import GetV1AgentGraphsResponse
    from .get_v1agent_runs_response import GetV1AgentRunsResponse
    from .get_v1agent_runs_run_id_evaluations_response import GetV1AgentRunsRunIdEvaluationsResponse
    from .get_v1agent_runs_run_id_events_response import GetV1AgentRunsRunIdEventsResponse
    from .get_v1api_keys_response import GetV1ApiKeysResponse
    from .get_v1approvals_response import GetV1ApprovalsResponse
    from .get_v1assurance_runs_response import GetV1AssuranceRunsResponse
    from .get_v1audit_response import GetV1AuditResponse
    from .get_v1connectors_response import GetV1ConnectorsResponse
    from .get_v1daily_ops_runs_response import GetV1DailyOpsRunsResponse
    from .get_v1daily_ops_schedules_response import GetV1DailyOpsSchedulesResponse
    from .get_v1evidence_imports_response import GetV1EvidenceImportsResponse
    from .get_v1jobs_response import GetV1JobsResponse
    from .get_v1metric_materializations_request_status import GetV1MetricMaterializationsRequestStatus
    from .get_v1metric_materializations_response import GetV1MetricMaterializationsResponse
    from .get_v1metric_observations_request_currency import GetV1MetricObservationsRequestCurrency
    from .get_v1metric_observations_response import GetV1MetricObservationsResponse
    from .get_v1metrics_response import GetV1MetricsResponse
    from .get_v1proposal_executions_response import GetV1ProposalExecutionsResponse
    from .get_v1proposals_response import GetV1ProposalsResponse
    from .get_v1records_response import GetV1RecordsResponse
    from .get_v1report_recipes_response import GetV1ReportRecipesResponse
    from .get_v1report_syncs_response import GetV1ReportSyncsResponse
    from .get_v1schedules_response import GetV1SchedulesResponse
    from .get_v1users_response import GetV1UsersResponse
    from .graph_edge import GraphEdge
    from .graph_node import GraphNode
    from .graph_node_expansion import GraphNodeExpansion
    from .graph_node_instruction_key import GraphNodeInstructionKey
    from .graph_node_key import GraphNodeKey
    from .graph_node_role import GraphNodeRole
    from .health import Health
    from .health_service import HealthService
    from .health_status import HealthStatus
    from .human_review_proposal_create_request import HumanReviewProposalCreateRequest
    from .human_review_proposal_payload import HumanReviewProposalPayload
    from .job import Job
    from .job_kind import JobKind
    from .job_status import JobStatus
    from .marketplace_account import MarketplaceAccount
    from .marketplace_account_credential_refs_value import MarketplaceAccountCredentialRefsValue
    from .marketplace_account_health_error_code import MarketplaceAccountHealthErrorCode
    from .marketplace_account_health_status import MarketplaceAccountHealthStatus
    from .marketplace_id import MarketplaceId
    from .marketplace_provider_smoke_request import MarketplaceProviderSmokeRequest
    from .marketplace_provider_smoke_request_provider import MarketplaceProviderSmokeRequestProvider
    from .metric_materialization import MetricMaterialization
    from .metric_materialization_quality_summary import MetricMaterializationQualitySummary
    from .metric_materialization_status import MetricMaterializationStatus
    from .metric_observation import MetricObservation
    from .metric_observation_currency import MetricObservationCurrency
    from .metric_observation_provenance import MetricObservationProvenance
    from .metric_observation_quality import MetricObservationQuality
    from .metric_observation_quality_status import MetricObservationQualityStatus
    from .metric_observation_time_grain import MetricObservationTimeGrain
    from .metric_observation_unit import MetricObservationUnit
    from .mission_control import MissionControl
    from .mission_event import MissionEvent
    from .mission_event_cursor import MissionEventCursor
    from .mission_event_event_type import MissionEventEventType
    from .mission_event_metadata import MissionEventMetadata
    from .mission_event_resource_type import MissionEventResourceType
    from .mission_reconnect import MissionReconnect
    from .mission_reconnect_reason import MissionReconnectReason
    from .mission_reset import MissionReset
    from .mission_reset_reason import MissionResetReason
    from .mission_reset_snapshot_url import MissionResetSnapshotUrl
    from .open_ai_provider_smoke_request import OpenAiProviderSmokeRequest
    from .open_ai_provider_smoke_request_provider import OpenAiProviderSmokeRequestProvider
    from .operating_briefing import OperatingBriefing
    from .operating_briefing_evidence import OperatingBriefingEvidence
    from .operating_briefing_platform import OperatingBriefingPlatform
    from .pilot_ads_component import PilotAdsComponent
    from .pilot_ads_component_reason_code import PilotAdsComponentReasonCode
    from .pilot_ads_component_status import PilotAdsComponentStatus
    from .pilot_amazon_spapi_component import PilotAmazonSpapiComponent
    from .pilot_amazon_spapi_component_status import PilotAmazonSpapiComponentStatus
    from .pilot_blocker import PilotBlocker
    from .pilot_count_component import PilotCountComponent
    from .pilot_count_component_status import PilotCountComponentStatus
    from .pilot_open_ai_component import PilotOpenAiComponent
    from .pilot_open_ai_component_status import PilotOpenAiComponentStatus
    from .pilot_runtime_status import PilotRuntimeStatus
    from .pilot_runtime_status_status import PilotRuntimeStatusStatus
    from .pilot_runtime_status_stop_reason import PilotRuntimeStatusStopReason
    from .pilot_schema_component import PilotSchemaComponent
    from .pilot_schema_component_status import PilotSchemaComponentStatus
    from .pilot_status import PilotStatus
    from .pilot_status_status import PilotStatusStatus
    from .pilot_tenant_components import PilotTenantComponents
    from .pilot_tenant_readiness import PilotTenantReadiness
    from .pilot_tenant_readiness_status import PilotTenantReadinessStatus
    from .pilot_tenant_readiness_tenant_mode import PilotTenantReadinessTenantMode
    from .pilot_worker_status import PilotWorkerStatus
    from .pilot_worker_status_name import PilotWorkerStatusName
    from .pilot_worker_status_status import PilotWorkerStatusStatus
    from .platform_id import PlatformId
    from .post_v1api_keys_key_id_revoke_response import PostV1ApiKeysKeyIdRevokeResponse
    from .post_v1api_keys_rotate_response import PostV1ApiKeysRotateResponse
    from .post_v1metric_materializations_backfill_response import PostV1MetricMaterializationsBackfillResponse
    from .principal import Principal
    from .principal_tenant_mode import PrincipalTenantMode
    from .proposal import Proposal
    from .proposal_capability_block import ProposalCapabilityBlock
    from .proposal_capability_block_code import ProposalCapabilityBlockCode
    from .proposal_capability_status import ProposalCapabilityStatus
    from .proposal_create_request import (
        ProposalCreateRequest,
        ProposalCreateRequest_AmazonAdsCampaignUpdate,
        ProposalCreateRequest_AmazonSpapiImportReport,
        ProposalCreateRequest_HumanReview,
        ProposalCreateRequest_ShopifySyncProducts,
    )
    from .proposal_decision import ProposalDecision
    from .proposal_decision_type import ProposalDecisionType
    from .proposal_execution import ProposalExecution
    from .proposal_execution_request import ProposalExecutionRequest
    from .proposal_execution_status import ProposalExecutionStatus
    from .proposal_operation import ProposalOperation
    from .proposal_payload import ProposalPayload
    from .proposal_risk import ProposalRisk
    from .proposal_status import ProposalStatus
    from .proposal_version import ProposalVersion
    from .provider_smoke_provider import ProviderSmokeProvider
    from .provider_smoke_request import ProviderSmokeRequest
    from .provider_smoke_test import ProviderSmokeTest
    from .provider_smoke_test_list import ProviderSmokeTestList
    from .provider_smoke_test_status import ProviderSmokeTestStatus
    from .readiness import Readiness
    from .readiness_status import ReadinessStatus
    from .report_recipe import ReportRecipe
    from .report_recipe_amazon_report_type import ReportRecipeAmazonReportType
    from .report_recipe_catalog_entry import ReportRecipeCatalogEntry
    from .report_recipe_evidence_report_type import ReportRecipeEvidenceReportType
    from .report_recipe_key import ReportRecipeKey
    from .report_sync import ReportSync
    from .report_sync_processing_status import ReportSyncProcessingStatus
    from .report_sync_status import ReportSyncStatus
    from .reviewer_issue import ReviewerIssue
    from .reviewer_issue_severity import ReviewerIssueSeverity
    from .reviewer_verdict import ReviewerVerdict
    from .reviewer_verdict_verdict import ReviewerVerdictVerdict
    from .role import Role
    from .runtime_catalog import RuntimeCatalog
    from .runtime_catalog_action_operations_item import RuntimeCatalogActionOperationsItem
    from .runtime_catalog_platforms_item import RuntimeCatalogPlatformsItem
    from .runtime_catalog_workflows_item import RuntimeCatalogWorkflowsItem
    from .schedule import Schedule
    from .schedule_create import ScheduleCreate
    from .schedule_create_evidence_selectors_item import ScheduleCreateEvidenceSelectorsItem
    from .schedule_evidence_selectors_item import ScheduleEvidenceSelectorsItem
    from .shopify_connector_config import ShopifyConnectorConfig
    from .shopify_connector_registration import ShopifyConnectorRegistration
    from .shopify_provider_details import ShopifyProviderDetails
    from .shopify_sync_action_request import ShopifySyncActionRequest
    from .shopify_sync_action_request_payload import ShopifySyncActionRequestPayload
    from .shopify_sync_products_proposal_create_request import ShopifySyncProductsProposalCreateRequest
    from .shopify_sync_products_proposal_payload import ShopifySyncProductsProposalPayload
    from .tool_policy import ToolPolicy
    from .user import User
    from .user_envelope import UserEnvelope
_dynamic_imports: typing.Dict[str, str] = {
    "Action": ".action",
    "ActionOperation": ".action_operation",
    "ActionRequest": ".action_request",
    "ActionRequest_AmazonSpapiImportReport": ".action_request",
    "ActionRequest_ShopifySyncProducts": ".action_request",
    "ActionStatus": ".action_status",
    "AdsAdapterStatus": ".ads_adapter_status",
    "AdsAdapterStatusReasonCodesItem": ".ads_adapter_status_reason_codes_item",
    "AdsAdapterStatusRegion": ".ads_adapter_status_region",
    "AdsAdapterStatusStatus": ".ads_adapter_status_status",
    "AdsCapabilityGate": ".ads_capability_gate",
    "AdsCapabilityGateChecksItem": ".ads_capability_gate_checks_item",
    "AdsCapabilityGateChecksItemName": ".ads_capability_gate_checks_item_name",
    "AdsCapabilityGateChecksItemStatus": ".ads_capability_gate_checks_item_status",
    "AdsCapabilityGateObservedCapabilitiesItem": ".ads_capability_gate_observed_capabilities_item",
    "AdsCapabilityGateRegion": ".ads_capability_gate_region",
    "AdsCapabilityGateRequiredCapabilitiesItem": ".ads_capability_gate_required_capabilities_item",
    "AdsCapabilityGateStatus": ".ads_capability_gate_status",
    "AgentArtifact": ".agent_artifact",
    "AgentArtifactContent": ".agent_artifact_content",
    "AgentArtifactKind": ".agent_artifact_kind",
    "AgentEvaluation": ".agent_evaluation",
    "AgentEvent": ".agent_event",
    "AgentGraph": ".agent_graph",
    "AgentGraphBundle": ".agent_graph_bundle",
    "AgentGraphDefinition": ".agent_graph_definition",
    "AgentGraphVersion": ".agent_graph_version",
    "AgentGraphVersionStatus": ".agent_graph_version_status",
    "AgentRun": ".agent_run",
    "AgentRunBundle": ".agent_run_bundle",
    "AgentRunOrigin": ".agent_run_origin",
    "AgentRunRequest": ".agent_run_request",
    "AgentRunRequestWorkflow": ".agent_run_request_workflow",
    "AgentRunReviewStatus": ".agent_run_review_status",
    "AgentRunStatus": ".agent_run_status",
    "AgentRunWorkflow": ".agent_run_workflow",
    "AgentTask": ".agent_task",
    "AgentTaskRole": ".agent_task_role",
    "AgentTaskStatus": ".agent_task_status",
    "AmazonAdsCampaignUpdateProposalCreateRequest": ".amazon_ads_campaign_update_proposal_create_request",
    "AmazonAdsCampaignUpdateProposalPayload": ".amazon_ads_campaign_update_proposal_payload",
    "AmazonAdsConnectorConfig": ".amazon_ads_connector_config",
    "AmazonAdsConnectorConfigRegion": ".amazon_ads_connector_config_region",
    "AmazonAdsConnectorRegistration": ".amazon_ads_connector_registration",
    "AmazonAdsProviderDetails": ".amazon_ads_provider_details",
    "AmazonAdsProviderDetailsRegion": ".amazon_ads_provider_details_region",
    "AmazonMarketplaceCatalogEntry": ".amazon_marketplace_catalog_entry",
    "AmazonMarketplaceCatalogEntryRegion": ".amazon_marketplace_catalog_entry_region",
    "AmazonReportImportActionRequest": ".amazon_report_import_action_request",
    "AmazonReportImportActionRequestPayload": ".amazon_report_import_action_request_payload",
    "AmazonSpapiConnectorConfig": ".amazon_spapi_connector_config",
    "AmazonSpapiConnectorConfigRegion": ".amazon_spapi_connector_config_region",
    "AmazonSpapiConnectorRegistration": ".amazon_spapi_connector_registration",
    "AmazonSpapiImportReportProposalCreateRequest": ".amazon_spapi_import_report_proposal_create_request",
    "AmazonSpapiImportReportProposalPayload": ".amazon_spapi_import_report_proposal_payload",
    "AmazonSpapiProviderDetails": ".amazon_spapi_provider_details",
    "AmazonSpapiProviderDetailsRegion": ".amazon_spapi_provider_details_region",
    "ApiKeyIssued": ".api_key_issued",
    "ApiKeyMetadata": ".api_key_metadata",
    "AssuranceCheck": ".assurance_check",
    "AssuranceCheckStatus": ".assurance_check_status",
    "AssuranceRun": ".assurance_run",
    "AssuranceRunKind": ".assurance_run_kind",
    "AssuranceRunRequestKind": ".assurance_run_request_kind",
    "AssuranceRunStatus": ".assurance_run_status",
    "AssuranceSummary": ".assurance_summary",
    "AuditEvent": ".audit_event",
    "BriefingAgent": ".briefing_agent",
    "BriefingAgentStatus": ".briefing_agent_status",
    "BriefingMetric": ".briefing_metric",
    "BriefingMetricFormat": ".briefing_metric_format",
    "BriefingMetricSeriesItem": ".briefing_metric_series_item",
    "BriefingMetricTimeGrain": ".briefing_metric_time_grain",
    "BriefingMetricTrendMode": ".briefing_metric_trend_mode",
    "BriefingMetricUnit": ".briefing_metric_unit",
    "ConnectorProvider": ".connector_provider",
    "ConnectorProviderCatalogEntry": ".connector_provider_catalog_entry",
    "ConnectorProviderDetails": ".connector_provider_details",
    "ConnectorRecord": ".connector_record",
    "ConnectorRegistration": ".connector_registration",
    "ConnectorRegistration_AmazonAds": ".connector_registration",
    "ConnectorRegistration_AmazonSpapi": ".connector_registration",
    "ConnectorRegistration_Shopify": ".connector_registration",
    "ConnectorUpdateRequestConfig": ".connector_update_request_config",
    "DailyOpsBrief": ".daily_ops_brief",
    "DailyOpsBriefEnvelope": ".daily_ops_brief_envelope",
    "DailyOpsBriefGraph": ".daily_ops_brief_graph",
    "DailyOpsBriefInputs": ".daily_ops_brief_inputs",
    "DailyOpsBriefKind": ".daily_ops_brief_kind",
    "DailyOpsBriefReviewStatus": ".daily_ops_brief_review_status",
    "DailyOpsBriefSchedule": ".daily_ops_brief_schedule",
    "DailyOpsBriefStatus": ".daily_ops_brief_status",
    "DailyOpsEvidenceSelector": ".daily_ops_evidence_selector",
    "DailyOpsRun": ".daily_ops_run",
    "DailyOpsRunStatus": ".daily_ops_run_status",
    "DailyOpsSchedule": ".daily_ops_schedule",
    "DailyOpsScheduleCreate": ".daily_ops_schedule_create",
    "DailyOpsScheduleSnapshot": ".daily_ops_schedule_snapshot",
    "DailyOpsSourceGap": ".daily_ops_source_gap",
    "DailyOpsSourceGapVerdict": ".daily_ops_source_gap_verdict",
    "DemoSession": ".demo_session",
    "DemoSessionTenantMode": ".demo_session_tenant_mode",
    "EmptyRequest": ".empty_request",
    "ErrorEnvelope": ".error_envelope",
    "ErrorEnvelopeError": ".error_envelope_error",
    "EvidenceImport": ".evidence_import",
    "EvidenceReportType": ".evidence_report_type",
    "EvidenceSource": ".evidence_source",
    "EvidenceSourceData": ".evidence_source_data",
    "GetV1AdsCapabilityGatesResponse": ".get_v1ads_capability_gates_response",
    "GetV1AgentGraphsResponse": ".get_v1agent_graphs_response",
    "GetV1AgentRunsResponse": ".get_v1agent_runs_response",
    "GetV1AgentRunsRunIdEvaluationsResponse": ".get_v1agent_runs_run_id_evaluations_response",
    "GetV1AgentRunsRunIdEventsResponse": ".get_v1agent_runs_run_id_events_response",
    "GetV1ApiKeysResponse": ".get_v1api_keys_response",
    "GetV1ApprovalsResponse": ".get_v1approvals_response",
    "GetV1AssuranceRunsResponse": ".get_v1assurance_runs_response",
    "GetV1AuditResponse": ".get_v1audit_response",
    "GetV1ConnectorsResponse": ".get_v1connectors_response",
    "GetV1DailyOpsRunsResponse": ".get_v1daily_ops_runs_response",
    "GetV1DailyOpsSchedulesResponse": ".get_v1daily_ops_schedules_response",
    "GetV1EvidenceImportsResponse": ".get_v1evidence_imports_response",
    "GetV1JobsResponse": ".get_v1jobs_response",
    "GetV1MetricMaterializationsRequestStatus": ".get_v1metric_materializations_request_status",
    "GetV1MetricMaterializationsResponse": ".get_v1metric_materializations_response",
    "GetV1MetricObservationsRequestCurrency": ".get_v1metric_observations_request_currency",
    "GetV1MetricObservationsResponse": ".get_v1metric_observations_response",
    "GetV1MetricsResponse": ".get_v1metrics_response",
    "GetV1ProposalExecutionsResponse": ".get_v1proposal_executions_response",
    "GetV1ProposalsResponse": ".get_v1proposals_response",
    "GetV1RecordsResponse": ".get_v1records_response",
    "GetV1ReportRecipesResponse": ".get_v1report_recipes_response",
    "GetV1ReportSyncsResponse": ".get_v1report_syncs_response",
    "GetV1SchedulesResponse": ".get_v1schedules_response",
    "GetV1UsersResponse": ".get_v1users_response",
    "GraphEdge": ".graph_edge",
    "GraphNode": ".graph_node",
    "GraphNodeExpansion": ".graph_node_expansion",
    "GraphNodeInstructionKey": ".graph_node_instruction_key",
    "GraphNodeKey": ".graph_node_key",
    "GraphNodeRole": ".graph_node_role",
    "Health": ".health",
    "HealthService": ".health_service",
    "HealthStatus": ".health_status",
    "HumanReviewProposalCreateRequest": ".human_review_proposal_create_request",
    "HumanReviewProposalPayload": ".human_review_proposal_payload",
    "Job": ".job",
    "JobKind": ".job_kind",
    "JobStatus": ".job_status",
    "MarketplaceAccount": ".marketplace_account",
    "MarketplaceAccountCredentialRefsValue": ".marketplace_account_credential_refs_value",
    "MarketplaceAccountHealthErrorCode": ".marketplace_account_health_error_code",
    "MarketplaceAccountHealthStatus": ".marketplace_account_health_status",
    "MarketplaceId": ".marketplace_id",
    "MarketplaceProviderSmokeRequest": ".marketplace_provider_smoke_request",
    "MarketplaceProviderSmokeRequestProvider": ".marketplace_provider_smoke_request_provider",
    "MetricMaterialization": ".metric_materialization",
    "MetricMaterializationQualitySummary": ".metric_materialization_quality_summary",
    "MetricMaterializationStatus": ".metric_materialization_status",
    "MetricObservation": ".metric_observation",
    "MetricObservationCurrency": ".metric_observation_currency",
    "MetricObservationProvenance": ".metric_observation_provenance",
    "MetricObservationQuality": ".metric_observation_quality",
    "MetricObservationQualityStatus": ".metric_observation_quality_status",
    "MetricObservationTimeGrain": ".metric_observation_time_grain",
    "MetricObservationUnit": ".metric_observation_unit",
    "MissionControl": ".mission_control",
    "MissionEvent": ".mission_event",
    "MissionEventCursor": ".mission_event_cursor",
    "MissionEventEventType": ".mission_event_event_type",
    "MissionEventMetadata": ".mission_event_metadata",
    "MissionEventResourceType": ".mission_event_resource_type",
    "MissionReconnect": ".mission_reconnect",
    "MissionReconnectReason": ".mission_reconnect_reason",
    "MissionReset": ".mission_reset",
    "MissionResetReason": ".mission_reset_reason",
    "MissionResetSnapshotUrl": ".mission_reset_snapshot_url",
    "OpenAiProviderSmokeRequest": ".open_ai_provider_smoke_request",
    "OpenAiProviderSmokeRequestProvider": ".open_ai_provider_smoke_request_provider",
    "OperatingBriefing": ".operating_briefing",
    "OperatingBriefingEvidence": ".operating_briefing_evidence",
    "OperatingBriefingPlatform": ".operating_briefing_platform",
    "PilotAdsComponent": ".pilot_ads_component",
    "PilotAdsComponentReasonCode": ".pilot_ads_component_reason_code",
    "PilotAdsComponentStatus": ".pilot_ads_component_status",
    "PilotAmazonSpapiComponent": ".pilot_amazon_spapi_component",
    "PilotAmazonSpapiComponentStatus": ".pilot_amazon_spapi_component_status",
    "PilotBlocker": ".pilot_blocker",
    "PilotCountComponent": ".pilot_count_component",
    "PilotCountComponentStatus": ".pilot_count_component_status",
    "PilotOpenAiComponent": ".pilot_open_ai_component",
    "PilotOpenAiComponentStatus": ".pilot_open_ai_component_status",
    "PilotRuntimeStatus": ".pilot_runtime_status",
    "PilotRuntimeStatusStatus": ".pilot_runtime_status_status",
    "PilotRuntimeStatusStopReason": ".pilot_runtime_status_stop_reason",
    "PilotSchemaComponent": ".pilot_schema_component",
    "PilotSchemaComponentStatus": ".pilot_schema_component_status",
    "PilotStatus": ".pilot_status",
    "PilotStatusStatus": ".pilot_status_status",
    "PilotTenantComponents": ".pilot_tenant_components",
    "PilotTenantReadiness": ".pilot_tenant_readiness",
    "PilotTenantReadinessStatus": ".pilot_tenant_readiness_status",
    "PilotTenantReadinessTenantMode": ".pilot_tenant_readiness_tenant_mode",
    "PilotWorkerStatus": ".pilot_worker_status",
    "PilotWorkerStatusName": ".pilot_worker_status_name",
    "PilotWorkerStatusStatus": ".pilot_worker_status_status",
    "PlatformId": ".platform_id",
    "PostV1ApiKeysKeyIdRevokeResponse": ".post_v1api_keys_key_id_revoke_response",
    "PostV1ApiKeysRotateResponse": ".post_v1api_keys_rotate_response",
    "PostV1MetricMaterializationsBackfillResponse": ".post_v1metric_materializations_backfill_response",
    "Principal": ".principal",
    "PrincipalTenantMode": ".principal_tenant_mode",
    "Proposal": ".proposal",
    "ProposalCapabilityBlock": ".proposal_capability_block",
    "ProposalCapabilityBlockCode": ".proposal_capability_block_code",
    "ProposalCapabilityStatus": ".proposal_capability_status",
    "ProposalCreateRequest": ".proposal_create_request",
    "ProposalCreateRequest_AmazonAdsCampaignUpdate": ".proposal_create_request",
    "ProposalCreateRequest_AmazonSpapiImportReport": ".proposal_create_request",
    "ProposalCreateRequest_HumanReview": ".proposal_create_request",
    "ProposalCreateRequest_ShopifySyncProducts": ".proposal_create_request",
    "ProposalDecision": ".proposal_decision",
    "ProposalDecisionType": ".proposal_decision_type",
    "ProposalExecution": ".proposal_execution",
    "ProposalExecutionRequest": ".proposal_execution_request",
    "ProposalExecutionStatus": ".proposal_execution_status",
    "ProposalOperation": ".proposal_operation",
    "ProposalPayload": ".proposal_payload",
    "ProposalRisk": ".proposal_risk",
    "ProposalStatus": ".proposal_status",
    "ProposalVersion": ".proposal_version",
    "ProviderSmokeProvider": ".provider_smoke_provider",
    "ProviderSmokeRequest": ".provider_smoke_request",
    "ProviderSmokeTest": ".provider_smoke_test",
    "ProviderSmokeTestList": ".provider_smoke_test_list",
    "ProviderSmokeTestStatus": ".provider_smoke_test_status",
    "Readiness": ".readiness",
    "ReadinessStatus": ".readiness_status",
    "ReportRecipe": ".report_recipe",
    "ReportRecipeAmazonReportType": ".report_recipe_amazon_report_type",
    "ReportRecipeCatalogEntry": ".report_recipe_catalog_entry",
    "ReportRecipeEvidenceReportType": ".report_recipe_evidence_report_type",
    "ReportRecipeKey": ".report_recipe_key",
    "ReportSync": ".report_sync",
    "ReportSyncProcessingStatus": ".report_sync_processing_status",
    "ReportSyncStatus": ".report_sync_status",
    "ReviewerIssue": ".reviewer_issue",
    "ReviewerIssueSeverity": ".reviewer_issue_severity",
    "ReviewerVerdict": ".reviewer_verdict",
    "ReviewerVerdictVerdict": ".reviewer_verdict_verdict",
    "Role": ".role",
    "RuntimeCatalog": ".runtime_catalog",
    "RuntimeCatalogActionOperationsItem": ".runtime_catalog_action_operations_item",
    "RuntimeCatalogPlatformsItem": ".runtime_catalog_platforms_item",
    "RuntimeCatalogWorkflowsItem": ".runtime_catalog_workflows_item",
    "Schedule": ".schedule",
    "ScheduleCreate": ".schedule_create",
    "ScheduleCreateEvidenceSelectorsItem": ".schedule_create_evidence_selectors_item",
    "ScheduleEvidenceSelectorsItem": ".schedule_evidence_selectors_item",
    "ShopifyConnectorConfig": ".shopify_connector_config",
    "ShopifyConnectorRegistration": ".shopify_connector_registration",
    "ShopifyProviderDetails": ".shopify_provider_details",
    "ShopifySyncActionRequest": ".shopify_sync_action_request",
    "ShopifySyncActionRequestPayload": ".shopify_sync_action_request_payload",
    "ShopifySyncProductsProposalCreateRequest": ".shopify_sync_products_proposal_create_request",
    "ShopifySyncProductsProposalPayload": ".shopify_sync_products_proposal_payload",
    "ToolPolicy": ".tool_policy",
    "User": ".user",
    "UserEnvelope": ".user_envelope",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Action",
    "ActionOperation",
    "ActionRequest",
    "ActionRequest_AmazonSpapiImportReport",
    "ActionRequest_ShopifySyncProducts",
    "ActionStatus",
    "AdsAdapterStatus",
    "AdsAdapterStatusReasonCodesItem",
    "AdsAdapterStatusRegion",
    "AdsAdapterStatusStatus",
    "AdsCapabilityGate",
    "AdsCapabilityGateChecksItem",
    "AdsCapabilityGateChecksItemName",
    "AdsCapabilityGateChecksItemStatus",
    "AdsCapabilityGateObservedCapabilitiesItem",
    "AdsCapabilityGateRegion",
    "AdsCapabilityGateRequiredCapabilitiesItem",
    "AdsCapabilityGateStatus",
    "AgentArtifact",
    "AgentArtifactContent",
    "AgentArtifactKind",
    "AgentEvaluation",
    "AgentEvent",
    "AgentGraph",
    "AgentGraphBundle",
    "AgentGraphDefinition",
    "AgentGraphVersion",
    "AgentGraphVersionStatus",
    "AgentRun",
    "AgentRunBundle",
    "AgentRunOrigin",
    "AgentRunRequest",
    "AgentRunRequestWorkflow",
    "AgentRunReviewStatus",
    "AgentRunStatus",
    "AgentRunWorkflow",
    "AgentTask",
    "AgentTaskRole",
    "AgentTaskStatus",
    "AmazonAdsCampaignUpdateProposalCreateRequest",
    "AmazonAdsCampaignUpdateProposalPayload",
    "AmazonAdsConnectorConfig",
    "AmazonAdsConnectorConfigRegion",
    "AmazonAdsConnectorRegistration",
    "AmazonAdsProviderDetails",
    "AmazonAdsProviderDetailsRegion",
    "AmazonMarketplaceCatalogEntry",
    "AmazonMarketplaceCatalogEntryRegion",
    "AmazonReportImportActionRequest",
    "AmazonReportImportActionRequestPayload",
    "AmazonSpapiConnectorConfig",
    "AmazonSpapiConnectorConfigRegion",
    "AmazonSpapiConnectorRegistration",
    "AmazonSpapiImportReportProposalCreateRequest",
    "AmazonSpapiImportReportProposalPayload",
    "AmazonSpapiProviderDetails",
    "AmazonSpapiProviderDetailsRegion",
    "ApiKeyIssued",
    "ApiKeyMetadata",
    "AssuranceCheck",
    "AssuranceCheckStatus",
    "AssuranceRun",
    "AssuranceRunKind",
    "AssuranceRunRequestKind",
    "AssuranceRunStatus",
    "AssuranceSummary",
    "AuditEvent",
    "BriefingAgent",
    "BriefingAgentStatus",
    "BriefingMetric",
    "BriefingMetricFormat",
    "BriefingMetricSeriesItem",
    "BriefingMetricTimeGrain",
    "BriefingMetricTrendMode",
    "BriefingMetricUnit",
    "ConnectorProvider",
    "ConnectorProviderCatalogEntry",
    "ConnectorProviderDetails",
    "ConnectorRecord",
    "ConnectorRegistration",
    "ConnectorRegistration_AmazonAds",
    "ConnectorRegistration_AmazonSpapi",
    "ConnectorRegistration_Shopify",
    "ConnectorUpdateRequestConfig",
    "DailyOpsBrief",
    "DailyOpsBriefEnvelope",
    "DailyOpsBriefGraph",
    "DailyOpsBriefInputs",
    "DailyOpsBriefKind",
    "DailyOpsBriefReviewStatus",
    "DailyOpsBriefSchedule",
    "DailyOpsBriefStatus",
    "DailyOpsEvidenceSelector",
    "DailyOpsRun",
    "DailyOpsRunStatus",
    "DailyOpsSchedule",
    "DailyOpsScheduleCreate",
    "DailyOpsScheduleSnapshot",
    "DailyOpsSourceGap",
    "DailyOpsSourceGapVerdict",
    "DemoSession",
    "DemoSessionTenantMode",
    "EmptyRequest",
    "ErrorEnvelope",
    "ErrorEnvelopeError",
    "EvidenceImport",
    "EvidenceReportType",
    "EvidenceSource",
    "EvidenceSourceData",
    "GetV1AdsCapabilityGatesResponse",
    "GetV1AgentGraphsResponse",
    "GetV1AgentRunsResponse",
    "GetV1AgentRunsRunIdEvaluationsResponse",
    "GetV1AgentRunsRunIdEventsResponse",
    "GetV1ApiKeysResponse",
    "GetV1ApprovalsResponse",
    "GetV1AssuranceRunsResponse",
    "GetV1AuditResponse",
    "GetV1ConnectorsResponse",
    "GetV1DailyOpsRunsResponse",
    "GetV1DailyOpsSchedulesResponse",
    "GetV1EvidenceImportsResponse",
    "GetV1JobsResponse",
    "GetV1MetricMaterializationsRequestStatus",
    "GetV1MetricMaterializationsResponse",
    "GetV1MetricObservationsRequestCurrency",
    "GetV1MetricObservationsResponse",
    "GetV1MetricsResponse",
    "GetV1ProposalExecutionsResponse",
    "GetV1ProposalsResponse",
    "GetV1RecordsResponse",
    "GetV1ReportRecipesResponse",
    "GetV1ReportSyncsResponse",
    "GetV1SchedulesResponse",
    "GetV1UsersResponse",
    "GraphEdge",
    "GraphNode",
    "GraphNodeExpansion",
    "GraphNodeInstructionKey",
    "GraphNodeKey",
    "GraphNodeRole",
    "Health",
    "HealthService",
    "HealthStatus",
    "HumanReviewProposalCreateRequest",
    "HumanReviewProposalPayload",
    "Job",
    "JobKind",
    "JobStatus",
    "MarketplaceAccount",
    "MarketplaceAccountCredentialRefsValue",
    "MarketplaceAccountHealthErrorCode",
    "MarketplaceAccountHealthStatus",
    "MarketplaceId",
    "MarketplaceProviderSmokeRequest",
    "MarketplaceProviderSmokeRequestProvider",
    "MetricMaterialization",
    "MetricMaterializationQualitySummary",
    "MetricMaterializationStatus",
    "MetricObservation",
    "MetricObservationCurrency",
    "MetricObservationProvenance",
    "MetricObservationQuality",
    "MetricObservationQualityStatus",
    "MetricObservationTimeGrain",
    "MetricObservationUnit",
    "MissionControl",
    "MissionEvent",
    "MissionEventCursor",
    "MissionEventEventType",
    "MissionEventMetadata",
    "MissionEventResourceType",
    "MissionReconnect",
    "MissionReconnectReason",
    "MissionReset",
    "MissionResetReason",
    "MissionResetSnapshotUrl",
    "OpenAiProviderSmokeRequest",
    "OpenAiProviderSmokeRequestProvider",
    "OperatingBriefing",
    "OperatingBriefingEvidence",
    "OperatingBriefingPlatform",
    "PilotAdsComponent",
    "PilotAdsComponentReasonCode",
    "PilotAdsComponentStatus",
    "PilotAmazonSpapiComponent",
    "PilotAmazonSpapiComponentStatus",
    "PilotBlocker",
    "PilotCountComponent",
    "PilotCountComponentStatus",
    "PilotOpenAiComponent",
    "PilotOpenAiComponentStatus",
    "PilotRuntimeStatus",
    "PilotRuntimeStatusStatus",
    "PilotRuntimeStatusStopReason",
    "PilotSchemaComponent",
    "PilotSchemaComponentStatus",
    "PilotStatus",
    "PilotStatusStatus",
    "PilotTenantComponents",
    "PilotTenantReadiness",
    "PilotTenantReadinessStatus",
    "PilotTenantReadinessTenantMode",
    "PilotWorkerStatus",
    "PilotWorkerStatusName",
    "PilotWorkerStatusStatus",
    "PlatformId",
    "PostV1ApiKeysKeyIdRevokeResponse",
    "PostV1ApiKeysRotateResponse",
    "PostV1MetricMaterializationsBackfillResponse",
    "Principal",
    "PrincipalTenantMode",
    "Proposal",
    "ProposalCapabilityBlock",
    "ProposalCapabilityBlockCode",
    "ProposalCapabilityStatus",
    "ProposalCreateRequest",
    "ProposalCreateRequest_AmazonAdsCampaignUpdate",
    "ProposalCreateRequest_AmazonSpapiImportReport",
    "ProposalCreateRequest_HumanReview",
    "ProposalCreateRequest_ShopifySyncProducts",
    "ProposalDecision",
    "ProposalDecisionType",
    "ProposalExecution",
    "ProposalExecutionRequest",
    "ProposalExecutionStatus",
    "ProposalOperation",
    "ProposalPayload",
    "ProposalRisk",
    "ProposalStatus",
    "ProposalVersion",
    "ProviderSmokeProvider",
    "ProviderSmokeRequest",
    "ProviderSmokeTest",
    "ProviderSmokeTestList",
    "ProviderSmokeTestStatus",
    "Readiness",
    "ReadinessStatus",
    "ReportRecipe",
    "ReportRecipeAmazonReportType",
    "ReportRecipeCatalogEntry",
    "ReportRecipeEvidenceReportType",
    "ReportRecipeKey",
    "ReportSync",
    "ReportSyncProcessingStatus",
    "ReportSyncStatus",
    "ReviewerIssue",
    "ReviewerIssueSeverity",
    "ReviewerVerdict",
    "ReviewerVerdictVerdict",
    "Role",
    "RuntimeCatalog",
    "RuntimeCatalogActionOperationsItem",
    "RuntimeCatalogPlatformsItem",
    "RuntimeCatalogWorkflowsItem",
    "Schedule",
    "ScheduleCreate",
    "ScheduleCreateEvidenceSelectorsItem",
    "ScheduleEvidenceSelectorsItem",
    "ShopifyConnectorConfig",
    "ShopifyConnectorRegistration",
    "ShopifyProviderDetails",
    "ShopifySyncActionRequest",
    "ShopifySyncActionRequestPayload",
    "ShopifySyncProductsProposalCreateRequest",
    "ShopifySyncProductsProposalPayload",
    "ToolPolicy",
    "User",
    "UserEnvelope",
]
