



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .apply_display_group_control_request_command_type import ApplyDisplayGroupControlRequestCommandType
    from .asset import Asset
    from .asset_status import AssetStatus
    from .asset_type import AssetType
    from .asset_variant import AssetVariant
    from .brand_bug_input import BrandBugInput
    from .brand_bug_input_background_style import BrandBugInputBackgroundStyle
    from .brand_bug_input_corner import BrandBugInputCorner
    from .brand_bug_input_target_scope import BrandBugInputTargetScope
    from .campaign import Campaign
    from .campaign_block import CampaignBlock
    from .campaign_block_content_type import CampaignBlockContentType
    from .campaign_block_type import CampaignBlockType
    from .campaign_destination import CampaignDestination
    from .campaign_destination_type import CampaignDestinationType
    from .campaign_preflight import CampaignPreflight
    from .campaign_preflight_issues_item import CampaignPreflightIssuesItem
    from .campaign_preflight_issues_item_severity import CampaignPreflightIssuesItemSeverity
    from .campaign_release import CampaignRelease
    from .campaign_release_status import CampaignReleaseStatus
    from .campaign_snapshot import CampaignSnapshot
    from .catalog_plugin import CatalogPlugin
    from .catalog_plugin_category import CatalogPluginCategory
    from .compare_publications_request_type import ComparePublicationsRequestType
    from .compare_publications_response import ComparePublicationsResponse
    from .compare_publications_response_data import ComparePublicationsResponseData
    from .content_submission import ContentSubmission
    from .content_submission_content_type import ContentSubmissionContentType
    from .content_submission_list import ContentSubmissionList
    from .content_submission_list_policy import ContentSubmissionListPolicy
    from .content_submission_status import ContentSubmissionStatus
    from .countdown_bar_input import CountdownBarInput
    from .countdown_bar_input_display_mode import CountdownBarInputDisplayMode
    from .countdown_bar_input_progress_fill import CountdownBarInputProgressFill
    from .countdown_bar_input_schedule_type import CountdownBarInputScheduleType
    from .countdown_bar_input_target_scope import CountdownBarInputTargetScope
    from .create_campaign_response import CreateCampaignResponse
    from .create_playlist_request_source_type import CreatePlaylistRequestSourceType
    from .data_source import DataSource
    from .data_source_input import DataSourceInput
    from .data_source_provider import DataSourceProvider
    from .dependency_edge import DependencyEdge
    from .dependency_edge_from_type import DependencyEdgeFromType
    from .dependency_edge_to_type import DependencyEdgeToType
    from .dependency_graph import DependencyGraph
    from .dependency_node import DependencyNode
    from .dependency_node_type import DependencyNodeType
    from .display_control_action import DisplayControlAction
    from .display_control_action_type import DisplayControlActionType
    from .export_noise_meter_history_request_granularity import ExportNoiseMeterHistoryRequestGranularity
    from .export_noise_meter_history_request_range import ExportNoiseMeterHistoryRequestRange
    from .get_api_v1player_updates_release_id_response import GetApiV1PlayerUpdatesReleaseIdResponse
    from .get_campaign_response import GetCampaignResponse
    from .get_content_submission_response import GetContentSubmissionResponse
    from .get_dependency_graph_response import GetDependencyGraphResponse
    from .inspect_data_source_request_provider import InspectDataSourceRequestProvider
    from .install_plugin_response import InstallPluginResponse
    from .list_assets_request_sort import ListAssetsRequestSort
    from .list_campaign_releases_response import ListCampaignReleasesResponse
    from .list_campaign_releases_response_data import ListCampaignReleasesResponseData
    from .list_campaigns_response import ListCampaignsResponse
    from .list_campaigns_response_data import ListCampaignsResponseData
    from .list_content_submissions_request_state import ListContentSubmissionsRequestState
    from .list_content_submissions_response import ListContentSubmissionsResponse
    from .list_form_records_request_sort import ListFormRecordsRequestSort
    from .list_plugins_response import ListPluginsResponse
    from .list_publication_history_request_type import ListPublicationHistoryRequestType
    from .list_publication_history_response import ListPublicationHistoryResponse
    from .list_publication_history_response_data import ListPublicationHistoryResponseData
    from .manifest_response import ManifestResponse
    from .manifest_schedule import ManifestSchedule
    from .manifest_schedule_type import ManifestScheduleType
    from .noise_meter_history_daily_request_range import NoiseMeterHistoryDailyRequestRange
    from .noise_meter_history_screens_request_range import NoiseMeterHistoryScreensRequestRange
    from .noise_meter_history_series_request_range import NoiseMeterHistorySeriesRequestRange
    from .noise_meter_history_summary_request_range import NoiseMeterHistorySummaryRequestRange
    from .noise_meter_input import NoiseMeterInput
    from .noise_meter_input_display_mode import NoiseMeterInputDisplayMode
    from .noise_meter_input_target_scope import NoiseMeterInputTargetScope
    from .password_confirmation import PasswordConfirmation
    from .player_family import PlayerFamily
    from .player_heartbeat_noise_meter import PlayerHeartbeatNoiseMeter
    from .player_heartbeat_noise_meter_pending_history_item import PlayerHeartbeatNoiseMeterPendingHistoryItem
    from .player_heartbeat_noise_meter_status import PlayerHeartbeatNoiseMeterStatus
    from .player_manifest import PlayerManifest
    from .player_manifest_canvas import PlayerManifestCanvas
    from .player_manifest_mode import PlayerManifestMode
    from .player_manifest_viewport import PlayerManifestViewport
    from .player_update_metadata import PlayerUpdateMetadata
    from .player_update_metadata_architecture import PlayerUpdateMetadataArchitecture
    from .player_update_metadata_platform import PlayerUpdateMetadataPlatform
    from .playlist_bulk_item_input import PlaylistBulkItemInput
    from .playlist_bulk_item_input_transition import PlaylistBulkItemInputTransition
    from .playlist_item_input import PlaylistItemInput
    from .playlist_item_input_delivery_policy import PlaylistItemInputDeliveryPolicy
    from .playlist_item_input_fit_mode import PlaylistItemInputFitMode
    from .playlist_item_input_transition import PlaylistItemInputTransition
    from .playlist_tag_rule_input_match import PlaylistTagRuleInputMatch
    from .plugin_attention import PluginAttention
    from .plugin_catalog import PluginCatalog
    from .plugin_catalog_unsupported_installations_item import PluginCatalogUnsupportedInstallationsItem
    from .plugin_in_use_error import PluginInUseError
    from .plugin_in_use_error_error import PluginInUseErrorError
    from .plugin_in_use_error_error_code import PluginInUseErrorErrorCode
    from .plugin_in_use_error_error_details import PluginInUseErrorErrorDetails
    from .plugin_in_use_error_error_details_resources_item import PluginInUseErrorErrorDetailsResourcesItem
    from .plugin_requirement import PluginRequirement
    from .plugin_requirement_kind import PluginRequirementKind
    from .post_api_v1player_releases_upload_response import PostApiV1PlayerReleasesUploadResponse
    from .post_api_v1player_releases_upload_response_data import PostApiV1PlayerReleasesUploadResponseData
    from .post_api_v1player_releases_upload_response_data_channel import (
        PostApiV1PlayerReleasesUploadResponseDataChannel,
    )
    from .post_api_v1player_releases_upload_response_data_platform import (
        PostApiV1PlayerReleasesUploadResponseDataPlatform,
    )
    from .post_api_v1player_releases_upload_response_data_source import PostApiV1PlayerReleasesUploadResponseDataSource
    from .post_api_v1player_update_deployments_deployment_id_status_request_state import (
        PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState,
    )
    from .preflight_campaign_response import PreflightCampaignResponse
    from .presentation_network import PresentationNetwork
    from .presentation_network_assignment import PresentationNetworkAssignment
    from .presentation_network_assignment_response import PresentationNetworkAssignmentResponse
    from .presentation_network_assignments_response import PresentationNetworkAssignmentsResponse
    from .presentation_network_assignments_response_data import PresentationNetworkAssignmentsResponseData
    from .presentation_network_auth import PresentationNetworkAuth
    from .presentation_network_detail_response import PresentationNetworkDetailResponse
    from .presentation_network_detail_response_data import PresentationNetworkDetailResponseData
    from .presentation_network_error import PresentationNetworkError
    from .presentation_network_error_error import PresentationNetworkErrorError
    from .presentation_network_list_response import PresentationNetworkListResponse
    from .presentation_network_list_response_data import PresentationNetworkListResponseData
    from .presentation_network_list_response_data_supported_security_item import (
        PresentationNetworkListResponseDataSupportedSecurityItem,
    )
    from .presentation_network_provisioning_material import PresentationNetworkProvisioningMaterial
    from .presentation_network_provisioning_response import PresentationNetworkProvisioningResponse
    from .presentation_network_readiness import PresentationNetworkReadiness
    from .presentation_network_readiness_helper_state import PresentationNetworkReadinessHelperState
    from .presentation_network_readiness_reported_state import PresentationNetworkReadinessReportedState
    from .presentation_network_readiness_response import PresentationNetworkReadinessResponse
    from .presentation_network_readiness_status import PresentationNetworkReadinessStatus
    from .presentation_network_response import PresentationNetworkResponse
    from .presentation_network_secret import PresentationNetworkSecret
    from .presentation_network_security import PresentationNetworkSecurity
    from .presentation_network_test_response import PresentationNetworkTestResponse
    from .presentation_network_test_result import PresentationNetworkTestResult
    from .presentation_override import PresentationOverride
    from .presentation_override_content_type import PresentationOverrideContentType
    from .presentation_override_input_after_action import PresentationOverrideInputAfterAction
    from .presentation_override_input_content_type import PresentationOverrideInputContentType
    from .presentation_override_input_target_type import PresentationOverrideInputTargetType
    from .presentation_reference import PresentationReference
    from .presentation_reference_layout_id import PresentationReferenceLayoutId
    from .presentation_reference_playlist_id import PresentationReferencePlaylistId
    from .preview_data_source_request_provider import PreviewDataSourceRequestProvider
    from .preview_display_group_control_request_command_type import PreviewDisplayGroupControlRequestCommandType
    from .publication_history_item import PublicationHistoryItem
    from .publication_history_item_method import PublicationHistoryItemMethod
    from .reset_demo_request_scenario import ResetDemoRequestScenario
    from .restore_campaign_release_response import RestoreCampaignReleaseResponse
    from .restore_publication_as_draft_request_type import RestorePublicationAsDraftRequestType
    from .rollback_publication_request_type import RollbackPublicationRequestType
    from .semantic_change import SemanticChange
    from .span_geometry_input_canvas import SpanGeometryInputCanvas
    from .span_geometry_input_display_mode import SpanGeometryInputDisplayMode
    from .span_panel import SpanPanel
    from .span_preparation import SpanPreparation
    from .span_preparation_status import SpanPreparationStatus
    from .span_status import SpanStatus
    from .span_status_display_mode import SpanStatusDisplayMode
    from .submit_content_draft_request_type import SubmitContentDraftRequestType
    from .update_campaign_draft_response import UpdateCampaignDraftResponse
    from .upload_session import UploadSession
    from .upload_status import UploadStatus
    from .variant_kind import VariantKind
    from .web_authn_assertion_authenticator_attachment import WebAuthnAssertionAuthenticatorAttachment
    from .web_authn_assertion_response import WebAuthnAssertionResponse
    from .web_authn_assertion_type import WebAuthnAssertionType
    from .web_authn_credential_authenticator_attachment import WebAuthnCredentialAuthenticatorAttachment
    from .web_authn_credential_response import WebAuthnCredentialResponse
    from .web_authn_credential_type import WebAuthnCredentialType
    from .widget import Widget
    from .widget_input import WidgetInput
    from .widget_input_preset_id import WidgetInputPresetId
    from .widget_preset_id import WidgetPresetId
    from .widget_provider import WidgetProvider
_dynamic_imports: typing.Dict[str, str] = {
    "ApplyDisplayGroupControlRequestCommandType": ".apply_display_group_control_request_command_type",
    "Asset": ".asset",
    "AssetStatus": ".asset_status",
    "AssetType": ".asset_type",
    "AssetVariant": ".asset_variant",
    "BrandBugInput": ".brand_bug_input",
    "BrandBugInputBackgroundStyle": ".brand_bug_input_background_style",
    "BrandBugInputCorner": ".brand_bug_input_corner",
    "BrandBugInputTargetScope": ".brand_bug_input_target_scope",
    "Campaign": ".campaign",
    "CampaignBlock": ".campaign_block",
    "CampaignBlockContentType": ".campaign_block_content_type",
    "CampaignBlockType": ".campaign_block_type",
    "CampaignDestination": ".campaign_destination",
    "CampaignDestinationType": ".campaign_destination_type",
    "CampaignPreflight": ".campaign_preflight",
    "CampaignPreflightIssuesItem": ".campaign_preflight_issues_item",
    "CampaignPreflightIssuesItemSeverity": ".campaign_preflight_issues_item_severity",
    "CampaignRelease": ".campaign_release",
    "CampaignReleaseStatus": ".campaign_release_status",
    "CampaignSnapshot": ".campaign_snapshot",
    "CatalogPlugin": ".catalog_plugin",
    "CatalogPluginCategory": ".catalog_plugin_category",
    "ComparePublicationsRequestType": ".compare_publications_request_type",
    "ComparePublicationsResponse": ".compare_publications_response",
    "ComparePublicationsResponseData": ".compare_publications_response_data",
    "ContentSubmission": ".content_submission",
    "ContentSubmissionContentType": ".content_submission_content_type",
    "ContentSubmissionList": ".content_submission_list",
    "ContentSubmissionListPolicy": ".content_submission_list_policy",
    "ContentSubmissionStatus": ".content_submission_status",
    "CountdownBarInput": ".countdown_bar_input",
    "CountdownBarInputDisplayMode": ".countdown_bar_input_display_mode",
    "CountdownBarInputProgressFill": ".countdown_bar_input_progress_fill",
    "CountdownBarInputScheduleType": ".countdown_bar_input_schedule_type",
    "CountdownBarInputTargetScope": ".countdown_bar_input_target_scope",
    "CreateCampaignResponse": ".create_campaign_response",
    "CreatePlaylistRequestSourceType": ".create_playlist_request_source_type",
    "DataSource": ".data_source",
    "DataSourceInput": ".data_source_input",
    "DataSourceProvider": ".data_source_provider",
    "DependencyEdge": ".dependency_edge",
    "DependencyEdgeFromType": ".dependency_edge_from_type",
    "DependencyEdgeToType": ".dependency_edge_to_type",
    "DependencyGraph": ".dependency_graph",
    "DependencyNode": ".dependency_node",
    "DependencyNodeType": ".dependency_node_type",
    "DisplayControlAction": ".display_control_action",
    "DisplayControlActionType": ".display_control_action_type",
    "ExportNoiseMeterHistoryRequestGranularity": ".export_noise_meter_history_request_granularity",
    "ExportNoiseMeterHistoryRequestRange": ".export_noise_meter_history_request_range",
    "GetApiV1PlayerUpdatesReleaseIdResponse": ".get_api_v1player_updates_release_id_response",
    "GetCampaignResponse": ".get_campaign_response",
    "GetContentSubmissionResponse": ".get_content_submission_response",
    "GetDependencyGraphResponse": ".get_dependency_graph_response",
    "InspectDataSourceRequestProvider": ".inspect_data_source_request_provider",
    "InstallPluginResponse": ".install_plugin_response",
    "ListAssetsRequestSort": ".list_assets_request_sort",
    "ListCampaignReleasesResponse": ".list_campaign_releases_response",
    "ListCampaignReleasesResponseData": ".list_campaign_releases_response_data",
    "ListCampaignsResponse": ".list_campaigns_response",
    "ListCampaignsResponseData": ".list_campaigns_response_data",
    "ListContentSubmissionsRequestState": ".list_content_submissions_request_state",
    "ListContentSubmissionsResponse": ".list_content_submissions_response",
    "ListFormRecordsRequestSort": ".list_form_records_request_sort",
    "ListPluginsResponse": ".list_plugins_response",
    "ListPublicationHistoryRequestType": ".list_publication_history_request_type",
    "ListPublicationHistoryResponse": ".list_publication_history_response",
    "ListPublicationHistoryResponseData": ".list_publication_history_response_data",
    "ManifestResponse": ".manifest_response",
    "ManifestSchedule": ".manifest_schedule",
    "ManifestScheduleType": ".manifest_schedule_type",
    "NoiseMeterHistoryDailyRequestRange": ".noise_meter_history_daily_request_range",
    "NoiseMeterHistoryScreensRequestRange": ".noise_meter_history_screens_request_range",
    "NoiseMeterHistorySeriesRequestRange": ".noise_meter_history_series_request_range",
    "NoiseMeterHistorySummaryRequestRange": ".noise_meter_history_summary_request_range",
    "NoiseMeterInput": ".noise_meter_input",
    "NoiseMeterInputDisplayMode": ".noise_meter_input_display_mode",
    "NoiseMeterInputTargetScope": ".noise_meter_input_target_scope",
    "PasswordConfirmation": ".password_confirmation",
    "PlayerFamily": ".player_family",
    "PlayerHeartbeatNoiseMeter": ".player_heartbeat_noise_meter",
    "PlayerHeartbeatNoiseMeterPendingHistoryItem": ".player_heartbeat_noise_meter_pending_history_item",
    "PlayerHeartbeatNoiseMeterStatus": ".player_heartbeat_noise_meter_status",
    "PlayerManifest": ".player_manifest",
    "PlayerManifestCanvas": ".player_manifest_canvas",
    "PlayerManifestMode": ".player_manifest_mode",
    "PlayerManifestViewport": ".player_manifest_viewport",
    "PlayerUpdateMetadata": ".player_update_metadata",
    "PlayerUpdateMetadataArchitecture": ".player_update_metadata_architecture",
    "PlayerUpdateMetadataPlatform": ".player_update_metadata_platform",
    "PlaylistBulkItemInput": ".playlist_bulk_item_input",
    "PlaylistBulkItemInputTransition": ".playlist_bulk_item_input_transition",
    "PlaylistItemInput": ".playlist_item_input",
    "PlaylistItemInputDeliveryPolicy": ".playlist_item_input_delivery_policy",
    "PlaylistItemInputFitMode": ".playlist_item_input_fit_mode",
    "PlaylistItemInputTransition": ".playlist_item_input_transition",
    "PlaylistTagRuleInputMatch": ".playlist_tag_rule_input_match",
    "PluginAttention": ".plugin_attention",
    "PluginCatalog": ".plugin_catalog",
    "PluginCatalogUnsupportedInstallationsItem": ".plugin_catalog_unsupported_installations_item",
    "PluginInUseError": ".plugin_in_use_error",
    "PluginInUseErrorError": ".plugin_in_use_error_error",
    "PluginInUseErrorErrorCode": ".plugin_in_use_error_error_code",
    "PluginInUseErrorErrorDetails": ".plugin_in_use_error_error_details",
    "PluginInUseErrorErrorDetailsResourcesItem": ".plugin_in_use_error_error_details_resources_item",
    "PluginRequirement": ".plugin_requirement",
    "PluginRequirementKind": ".plugin_requirement_kind",
    "PostApiV1PlayerReleasesUploadResponse": ".post_api_v1player_releases_upload_response",
    "PostApiV1PlayerReleasesUploadResponseData": ".post_api_v1player_releases_upload_response_data",
    "PostApiV1PlayerReleasesUploadResponseDataChannel": ".post_api_v1player_releases_upload_response_data_channel",
    "PostApiV1PlayerReleasesUploadResponseDataPlatform": ".post_api_v1player_releases_upload_response_data_platform",
    "PostApiV1PlayerReleasesUploadResponseDataSource": ".post_api_v1player_releases_upload_response_data_source",
    "PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState": ".post_api_v1player_update_deployments_deployment_id_status_request_state",
    "PreflightCampaignResponse": ".preflight_campaign_response",
    "PresentationNetwork": ".presentation_network",
    "PresentationNetworkAssignment": ".presentation_network_assignment",
    "PresentationNetworkAssignmentResponse": ".presentation_network_assignment_response",
    "PresentationNetworkAssignmentsResponse": ".presentation_network_assignments_response",
    "PresentationNetworkAssignmentsResponseData": ".presentation_network_assignments_response_data",
    "PresentationNetworkAuth": ".presentation_network_auth",
    "PresentationNetworkDetailResponse": ".presentation_network_detail_response",
    "PresentationNetworkDetailResponseData": ".presentation_network_detail_response_data",
    "PresentationNetworkError": ".presentation_network_error",
    "PresentationNetworkErrorError": ".presentation_network_error_error",
    "PresentationNetworkListResponse": ".presentation_network_list_response",
    "PresentationNetworkListResponseData": ".presentation_network_list_response_data",
    "PresentationNetworkListResponseDataSupportedSecurityItem": ".presentation_network_list_response_data_supported_security_item",
    "PresentationNetworkProvisioningMaterial": ".presentation_network_provisioning_material",
    "PresentationNetworkProvisioningResponse": ".presentation_network_provisioning_response",
    "PresentationNetworkReadiness": ".presentation_network_readiness",
    "PresentationNetworkReadinessHelperState": ".presentation_network_readiness_helper_state",
    "PresentationNetworkReadinessReportedState": ".presentation_network_readiness_reported_state",
    "PresentationNetworkReadinessResponse": ".presentation_network_readiness_response",
    "PresentationNetworkReadinessStatus": ".presentation_network_readiness_status",
    "PresentationNetworkResponse": ".presentation_network_response",
    "PresentationNetworkSecret": ".presentation_network_secret",
    "PresentationNetworkSecurity": ".presentation_network_security",
    "PresentationNetworkTestResponse": ".presentation_network_test_response",
    "PresentationNetworkTestResult": ".presentation_network_test_result",
    "PresentationOverride": ".presentation_override",
    "PresentationOverrideContentType": ".presentation_override_content_type",
    "PresentationOverrideInputAfterAction": ".presentation_override_input_after_action",
    "PresentationOverrideInputContentType": ".presentation_override_input_content_type",
    "PresentationOverrideInputTargetType": ".presentation_override_input_target_type",
    "PresentationReference": ".presentation_reference",
    "PresentationReferenceLayoutId": ".presentation_reference_layout_id",
    "PresentationReferencePlaylistId": ".presentation_reference_playlist_id",
    "PreviewDataSourceRequestProvider": ".preview_data_source_request_provider",
    "PreviewDisplayGroupControlRequestCommandType": ".preview_display_group_control_request_command_type",
    "PublicationHistoryItem": ".publication_history_item",
    "PublicationHistoryItemMethod": ".publication_history_item_method",
    "ResetDemoRequestScenario": ".reset_demo_request_scenario",
    "RestoreCampaignReleaseResponse": ".restore_campaign_release_response",
    "RestorePublicationAsDraftRequestType": ".restore_publication_as_draft_request_type",
    "RollbackPublicationRequestType": ".rollback_publication_request_type",
    "SemanticChange": ".semantic_change",
    "SpanGeometryInputCanvas": ".span_geometry_input_canvas",
    "SpanGeometryInputDisplayMode": ".span_geometry_input_display_mode",
    "SpanPanel": ".span_panel",
    "SpanPreparation": ".span_preparation",
    "SpanPreparationStatus": ".span_preparation_status",
    "SpanStatus": ".span_status",
    "SpanStatusDisplayMode": ".span_status_display_mode",
    "SubmitContentDraftRequestType": ".submit_content_draft_request_type",
    "UpdateCampaignDraftResponse": ".update_campaign_draft_response",
    "UploadSession": ".upload_session",
    "UploadStatus": ".upload_status",
    "VariantKind": ".variant_kind",
    "WebAuthnAssertionAuthenticatorAttachment": ".web_authn_assertion_authenticator_attachment",
    "WebAuthnAssertionResponse": ".web_authn_assertion_response",
    "WebAuthnAssertionType": ".web_authn_assertion_type",
    "WebAuthnCredentialAuthenticatorAttachment": ".web_authn_credential_authenticator_attachment",
    "WebAuthnCredentialResponse": ".web_authn_credential_response",
    "WebAuthnCredentialType": ".web_authn_credential_type",
    "Widget": ".widget",
    "WidgetInput": ".widget_input",
    "WidgetInputPresetId": ".widget_input_preset_id",
    "WidgetPresetId": ".widget_preset_id",
    "WidgetProvider": ".widget_provider",
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
    "ApplyDisplayGroupControlRequestCommandType",
    "Asset",
    "AssetStatus",
    "AssetType",
    "AssetVariant",
    "BrandBugInput",
    "BrandBugInputBackgroundStyle",
    "BrandBugInputCorner",
    "BrandBugInputTargetScope",
    "Campaign",
    "CampaignBlock",
    "CampaignBlockContentType",
    "CampaignBlockType",
    "CampaignDestination",
    "CampaignDestinationType",
    "CampaignPreflight",
    "CampaignPreflightIssuesItem",
    "CampaignPreflightIssuesItemSeverity",
    "CampaignRelease",
    "CampaignReleaseStatus",
    "CampaignSnapshot",
    "CatalogPlugin",
    "CatalogPluginCategory",
    "ComparePublicationsRequestType",
    "ComparePublicationsResponse",
    "ComparePublicationsResponseData",
    "ContentSubmission",
    "ContentSubmissionContentType",
    "ContentSubmissionList",
    "ContentSubmissionListPolicy",
    "ContentSubmissionStatus",
    "CountdownBarInput",
    "CountdownBarInputDisplayMode",
    "CountdownBarInputProgressFill",
    "CountdownBarInputScheduleType",
    "CountdownBarInputTargetScope",
    "CreateCampaignResponse",
    "CreatePlaylistRequestSourceType",
    "DataSource",
    "DataSourceInput",
    "DataSourceProvider",
    "DependencyEdge",
    "DependencyEdgeFromType",
    "DependencyEdgeToType",
    "DependencyGraph",
    "DependencyNode",
    "DependencyNodeType",
    "DisplayControlAction",
    "DisplayControlActionType",
    "ExportNoiseMeterHistoryRequestGranularity",
    "ExportNoiseMeterHistoryRequestRange",
    "GetApiV1PlayerUpdatesReleaseIdResponse",
    "GetCampaignResponse",
    "GetContentSubmissionResponse",
    "GetDependencyGraphResponse",
    "InspectDataSourceRequestProvider",
    "InstallPluginResponse",
    "ListAssetsRequestSort",
    "ListCampaignReleasesResponse",
    "ListCampaignReleasesResponseData",
    "ListCampaignsResponse",
    "ListCampaignsResponseData",
    "ListContentSubmissionsRequestState",
    "ListContentSubmissionsResponse",
    "ListFormRecordsRequestSort",
    "ListPluginsResponse",
    "ListPublicationHistoryRequestType",
    "ListPublicationHistoryResponse",
    "ListPublicationHistoryResponseData",
    "ManifestResponse",
    "ManifestSchedule",
    "ManifestScheduleType",
    "NoiseMeterHistoryDailyRequestRange",
    "NoiseMeterHistoryScreensRequestRange",
    "NoiseMeterHistorySeriesRequestRange",
    "NoiseMeterHistorySummaryRequestRange",
    "NoiseMeterInput",
    "NoiseMeterInputDisplayMode",
    "NoiseMeterInputTargetScope",
    "PasswordConfirmation",
    "PlayerFamily",
    "PlayerHeartbeatNoiseMeter",
    "PlayerHeartbeatNoiseMeterPendingHistoryItem",
    "PlayerHeartbeatNoiseMeterStatus",
    "PlayerManifest",
    "PlayerManifestCanvas",
    "PlayerManifestMode",
    "PlayerManifestViewport",
    "PlayerUpdateMetadata",
    "PlayerUpdateMetadataArchitecture",
    "PlayerUpdateMetadataPlatform",
    "PlaylistBulkItemInput",
    "PlaylistBulkItemInputTransition",
    "PlaylistItemInput",
    "PlaylistItemInputDeliveryPolicy",
    "PlaylistItemInputFitMode",
    "PlaylistItemInputTransition",
    "PlaylistTagRuleInputMatch",
    "PluginAttention",
    "PluginCatalog",
    "PluginCatalogUnsupportedInstallationsItem",
    "PluginInUseError",
    "PluginInUseErrorError",
    "PluginInUseErrorErrorCode",
    "PluginInUseErrorErrorDetails",
    "PluginInUseErrorErrorDetailsResourcesItem",
    "PluginRequirement",
    "PluginRequirementKind",
    "PostApiV1PlayerReleasesUploadResponse",
    "PostApiV1PlayerReleasesUploadResponseData",
    "PostApiV1PlayerReleasesUploadResponseDataChannel",
    "PostApiV1PlayerReleasesUploadResponseDataPlatform",
    "PostApiV1PlayerReleasesUploadResponseDataSource",
    "PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState",
    "PreflightCampaignResponse",
    "PresentationNetwork",
    "PresentationNetworkAssignment",
    "PresentationNetworkAssignmentResponse",
    "PresentationNetworkAssignmentsResponse",
    "PresentationNetworkAssignmentsResponseData",
    "PresentationNetworkAuth",
    "PresentationNetworkDetailResponse",
    "PresentationNetworkDetailResponseData",
    "PresentationNetworkError",
    "PresentationNetworkErrorError",
    "PresentationNetworkListResponse",
    "PresentationNetworkListResponseData",
    "PresentationNetworkListResponseDataSupportedSecurityItem",
    "PresentationNetworkProvisioningMaterial",
    "PresentationNetworkProvisioningResponse",
    "PresentationNetworkReadiness",
    "PresentationNetworkReadinessHelperState",
    "PresentationNetworkReadinessReportedState",
    "PresentationNetworkReadinessResponse",
    "PresentationNetworkReadinessStatus",
    "PresentationNetworkResponse",
    "PresentationNetworkSecret",
    "PresentationNetworkSecurity",
    "PresentationNetworkTestResponse",
    "PresentationNetworkTestResult",
    "PresentationOverride",
    "PresentationOverrideContentType",
    "PresentationOverrideInputAfterAction",
    "PresentationOverrideInputContentType",
    "PresentationOverrideInputTargetType",
    "PresentationReference",
    "PresentationReferenceLayoutId",
    "PresentationReferencePlaylistId",
    "PreviewDataSourceRequestProvider",
    "PreviewDisplayGroupControlRequestCommandType",
    "PublicationHistoryItem",
    "PublicationHistoryItemMethod",
    "ResetDemoRequestScenario",
    "RestoreCampaignReleaseResponse",
    "RestorePublicationAsDraftRequestType",
    "RollbackPublicationRequestType",
    "SemanticChange",
    "SpanGeometryInputCanvas",
    "SpanGeometryInputDisplayMode",
    "SpanPanel",
    "SpanPreparation",
    "SpanPreparationStatus",
    "SpanStatus",
    "SpanStatusDisplayMode",
    "SubmitContentDraftRequestType",
    "UpdateCampaignDraftResponse",
    "UploadSession",
    "UploadStatus",
    "VariantKind",
    "WebAuthnAssertionAuthenticatorAttachment",
    "WebAuthnAssertionResponse",
    "WebAuthnAssertionType",
    "WebAuthnCredentialAuthenticatorAttachment",
    "WebAuthnCredentialResponse",
    "WebAuthnCredentialType",
    "Widget",
    "WidgetInput",
    "WidgetInputPresetId",
    "WidgetPresetId",
    "WidgetProvider",
]
