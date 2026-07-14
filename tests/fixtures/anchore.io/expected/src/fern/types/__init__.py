



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_credential import AccessCredential
    from .access_credential_type import AccessCredentialType
    from .account import Account
    from .account_list import AccountList
    from .account_state import AccountState
    from .account_status import AccountStatus
    from .account_status_state import AccountStatusState
    from .account_type import AccountType
    from .add_analysis_archive_result import AddAnalysisArchiveResult
    from .analysis_archive_add_result import AnalysisArchiveAddResult
    from .analysis_archive_add_result_status import AnalysisArchiveAddResultStatus
    from .analysis_archive_rules import AnalysisArchiveRules
    from .analysis_archive_rules_summary import AnalysisArchiveRulesSummary
    from .analysis_archive_source import AnalysisArchiveSource
    from .analysis_archive_summary import AnalysisArchiveSummary
    from .analysis_archive_transition_history import AnalysisArchiveTransitionHistory
    from .analysis_archive_transition_history_transition import AnalysisArchiveTransitionHistoryTransition
    from .analysis_archive_transition_rule import AnalysisArchiveTransitionRule
    from .analysis_archive_transition_rule_exclude import AnalysisArchiveTransitionRuleExclude
    from .analysis_archive_transition_rule_transition import AnalysisArchiveTransitionRuleTransition
    from .analysis_update_eval import AnalysisUpdateEval
    from .analysis_update_notification import AnalysisUpdateNotification
    from .analysis_update_notification_data import AnalysisUpdateNotificationData
    from .analysis_update_notification_payload import AnalysisUpdateNotificationPayload
    from .anchore_error_code import AnchoreErrorCode
    from .anchore_image import AnchoreImage
    from .anchore_image_analysis_status import AnchoreImageAnalysisStatus
    from .anchore_image_image_status import AnchoreImageImageStatus
    from .anchore_image_list import AnchoreImageList
    from .anchore_image_tag_summary import AnchoreImageTagSummary
    from .anchore_image_tag_summary_list import AnchoreImageTagSummaryList
    from .annotations import Annotations
    from .api_error_response import ApiErrorResponse
    from .archive_summary import ArchiveSummary
    from .archived_analyses import ArchivedAnalyses
    from .archived_analysis import ArchivedAnalysis
    from .archived_analysis_status import ArchivedAnalysisStatus
    from .base_notification_data import BaseNotificationData
    from .content_files_response import ContentFilesResponse
    from .content_files_response_content_item import ContentFilesResponseContentItem
    from .content_java_package_response import ContentJavaPackageResponse
    from .content_java_package_response_content_item import ContentJavaPackageResponseContentItem
    from .content_malware_response import ContentMalwareResponse
    from .content_package_response import ContentPackageResponse
    from .content_package_response_content_item import ContentPackageResponseContentItem
    from .content_response import ContentResponse
    from .credential_list import CredentialList
    from .cvssv2scores import Cvssv2Scores
    from .cvssv3scores import Cvssv3Scores
    from .delete_image_response import DeleteImageResponse
    from .delete_image_response_list import DeleteImageResponseList
    from .delete_image_response_status import DeleteImageResponseStatus
    from .event_category import EventCategory
    from .event_description import EventDescription
    from .event_response import EventResponse
    from .event_response_event import EventResponseEvent
    from .event_response_event_resource import EventResponseEventResource
    from .event_response_event_source import EventResponseEventSource
    from .event_subcategory import EventSubcategory
    from .event_types_list import EventTypesList
    from .events_list import EventsList
    from .feed_group_metadata import FeedGroupMetadata
    from .feed_metadata import FeedMetadata
    from .feed_sync_result import FeedSyncResult
    from .feed_sync_result_status import FeedSyncResultStatus
    from .feed_sync_results import FeedSyncResults
    from .file_content_search_list import FileContentSearchList
    from .file_content_search_result import FileContentSearchResult
    from .gate_spec import GateSpec
    from .gate_spec_state import GateSpecState
    from .generic_notification_payload import GenericNotificationPayload
    from .group_sync_result import GroupSyncResult
    from .group_sync_result_status import GroupSyncResultStatus
    from .image_analysis_references import ImageAnalysisReferences
    from .image_analysis_report import ImageAnalysisReport
    from .image_content import ImageContent
    from .image_content_delete_response import ImageContentDeleteResponse
    from .image_detail import ImageDetail
    from .image_filter import ImageFilter
    from .image_import_content_response import ImageImportContentResponse
    from .image_import_manifest import ImageImportManifest
    from .image_import_operation import ImageImportOperation
    from .image_import_operation_status import ImageImportOperationStatus
    from .image_imports import ImageImports
    from .image_ref import ImageRef
    from .image_ref_type import ImageRefType
    from .image_reference import ImageReference
    from .image_selection_rule import ImageSelectionRule
    from .image_selector import ImageSelector
    from .image_source import ImageSource
    from .image_with_packages import ImageWithPackages
    from .import_content_digest_list import ImportContentDigestList
    from .import_content_digests import ImportContentDigests
    from .import_descriptor import ImportDescriptor
    from .import_distribution import ImportDistribution
    from .import_package import ImportPackage
    from .import_package_location import ImportPackageLocation
    from .import_package_relationship import ImportPackageRelationship
    from .import_schema import ImportSchema
    from .import_source import ImportSource
    from .local_analysis_source import LocalAnalysisSource
    from .malware_scan import MalwareScan
    from .malware_scan_findings_item import MalwareScanFindingsItem
    from .mapping_rule import MappingRule
    from .metadata_response import MetadataResponse
    from .native_sbom import NativeSbom
    from .notification_base import NotificationBase
    from .nvd_data_list import NvdDataList
    from .nvd_data_object import NvdDataObject
    from .package_reference import PackageReference
    from .paginated_image_list import PaginatedImageList
    from .paginated_vulnerability_list import PaginatedVulnerabilityList
    from .paginated_vulnerable_image_list import PaginatedVulnerableImageList
    from .pagination_properties import PaginationProperties
    from .policy import Policy
    from .policy_bundle import PolicyBundle
    from .policy_bundle_list import PolicyBundleList
    from .policy_bundle_record import PolicyBundleRecord
    from .policy_eval_notification import PolicyEvalNotification
    from .policy_eval_notification_data import PolicyEvalNotificationData
    from .policy_eval_notification_payload import PolicyEvalNotificationPayload
    from .policy_evaluation import PolicyEvaluation
    from .policy_evaluation_list import PolicyEvaluationList
    from .policy_rule import PolicyRule
    from .policy_rule_action import PolicyRuleAction
    from .policy_rule_params_item import PolicyRuleParamsItem
    from .regex_content_match import RegexContentMatch
    from .registry_configuration import RegistryConfiguration
    from .registry_configuration_list import RegistryConfigurationList
    from .registry_configuration_request import RegistryConfigurationRequest
    from .registry_digest_source import RegistryDigestSource
    from .registry_tag_source import RegistryTagSource
    from .repository_tag_list import RepositoryTagList
    from .retrieved_file import RetrievedFile
    from .retrieved_file_list import RetrievedFileList
    from .secret_search_list import SecretSearchList
    from .secret_search_result import SecretSearchResult
    from .service import Service
    from .service_list import ServiceList
    from .service_version import ServiceVersion
    from .service_version_api import ServiceVersionApi
    from .service_version_db import ServiceVersionDb
    from .service_version_service import ServiceVersionService
    from .standalone_vulnerability import StandaloneVulnerability
    from .standalone_vulnerability_severity import StandaloneVulnerabilitySeverity
    from .status_response import StatusResponse
    from .subscription import Subscription
    from .subscription_list import SubscriptionList
    from .system_status_response import SystemStatusResponse
    from .tag_entry import TagEntry
    from .tag_update_notification import TagUpdateNotification
    from .tag_update_notification_data import TagUpdateNotificationData
    from .tag_update_notification_payload import TagUpdateNotificationPayload
    from .token_response import TokenResponse
    from .trigger_param_spec import TriggerParamSpec
    from .trigger_param_spec_state import TriggerParamSpecState
    from .trigger_spec import TriggerSpec
    from .trigger_spec_state import TriggerSpecState
    from .user import User
    from .user_list import UserList
    from .user_type import UserType
    from .vendor_data_list import VendorDataList
    from .vendor_data_object import VendorDataObject
    from .vuln_diff_result import VulnDiffResult
    from .vuln_update_notification import VulnUpdateNotification
    from .vuln_update_notification_data import VulnUpdateNotificationData
    from .vuln_update_notification_payload import VulnUpdateNotificationPayload
    from .vulnerability import Vulnerability
    from .vulnerability_list import VulnerabilityList
    from .vulnerability_reference import VulnerabilityReference
    from .vulnerability_response import VulnerabilityResponse
    from .vulnerable_image import VulnerableImage
    from .vulnerable_package_reference import VulnerablePackageReference
    from .whitelist import Whitelist
    from .whitelist_item import WhitelistItem
_dynamic_imports: typing.Dict[str, str] = {
    "AccessCredential": ".access_credential",
    "AccessCredentialType": ".access_credential_type",
    "Account": ".account",
    "AccountList": ".account_list",
    "AccountState": ".account_state",
    "AccountStatus": ".account_status",
    "AccountStatusState": ".account_status_state",
    "AccountType": ".account_type",
    "AddAnalysisArchiveResult": ".add_analysis_archive_result",
    "AnalysisArchiveAddResult": ".analysis_archive_add_result",
    "AnalysisArchiveAddResultStatus": ".analysis_archive_add_result_status",
    "AnalysisArchiveRules": ".analysis_archive_rules",
    "AnalysisArchiveRulesSummary": ".analysis_archive_rules_summary",
    "AnalysisArchiveSource": ".analysis_archive_source",
    "AnalysisArchiveSummary": ".analysis_archive_summary",
    "AnalysisArchiveTransitionHistory": ".analysis_archive_transition_history",
    "AnalysisArchiveTransitionHistoryTransition": ".analysis_archive_transition_history_transition",
    "AnalysisArchiveTransitionRule": ".analysis_archive_transition_rule",
    "AnalysisArchiveTransitionRuleExclude": ".analysis_archive_transition_rule_exclude",
    "AnalysisArchiveTransitionRuleTransition": ".analysis_archive_transition_rule_transition",
    "AnalysisUpdateEval": ".analysis_update_eval",
    "AnalysisUpdateNotification": ".analysis_update_notification",
    "AnalysisUpdateNotificationData": ".analysis_update_notification_data",
    "AnalysisUpdateNotificationPayload": ".analysis_update_notification_payload",
    "AnchoreErrorCode": ".anchore_error_code",
    "AnchoreImage": ".anchore_image",
    "AnchoreImageAnalysisStatus": ".anchore_image_analysis_status",
    "AnchoreImageImageStatus": ".anchore_image_image_status",
    "AnchoreImageList": ".anchore_image_list",
    "AnchoreImageTagSummary": ".anchore_image_tag_summary",
    "AnchoreImageTagSummaryList": ".anchore_image_tag_summary_list",
    "Annotations": ".annotations",
    "ApiErrorResponse": ".api_error_response",
    "ArchiveSummary": ".archive_summary",
    "ArchivedAnalyses": ".archived_analyses",
    "ArchivedAnalysis": ".archived_analysis",
    "ArchivedAnalysisStatus": ".archived_analysis_status",
    "BaseNotificationData": ".base_notification_data",
    "ContentFilesResponse": ".content_files_response",
    "ContentFilesResponseContentItem": ".content_files_response_content_item",
    "ContentJavaPackageResponse": ".content_java_package_response",
    "ContentJavaPackageResponseContentItem": ".content_java_package_response_content_item",
    "ContentMalwareResponse": ".content_malware_response",
    "ContentPackageResponse": ".content_package_response",
    "ContentPackageResponseContentItem": ".content_package_response_content_item",
    "ContentResponse": ".content_response",
    "CredentialList": ".credential_list",
    "Cvssv2Scores": ".cvssv2scores",
    "Cvssv3Scores": ".cvssv3scores",
    "DeleteImageResponse": ".delete_image_response",
    "DeleteImageResponseList": ".delete_image_response_list",
    "DeleteImageResponseStatus": ".delete_image_response_status",
    "EventCategory": ".event_category",
    "EventDescription": ".event_description",
    "EventResponse": ".event_response",
    "EventResponseEvent": ".event_response_event",
    "EventResponseEventResource": ".event_response_event_resource",
    "EventResponseEventSource": ".event_response_event_source",
    "EventSubcategory": ".event_subcategory",
    "EventTypesList": ".event_types_list",
    "EventsList": ".events_list",
    "FeedGroupMetadata": ".feed_group_metadata",
    "FeedMetadata": ".feed_metadata",
    "FeedSyncResult": ".feed_sync_result",
    "FeedSyncResultStatus": ".feed_sync_result_status",
    "FeedSyncResults": ".feed_sync_results",
    "FileContentSearchList": ".file_content_search_list",
    "FileContentSearchResult": ".file_content_search_result",
    "GateSpec": ".gate_spec",
    "GateSpecState": ".gate_spec_state",
    "GenericNotificationPayload": ".generic_notification_payload",
    "GroupSyncResult": ".group_sync_result",
    "GroupSyncResultStatus": ".group_sync_result_status",
    "ImageAnalysisReferences": ".image_analysis_references",
    "ImageAnalysisReport": ".image_analysis_report",
    "ImageContent": ".image_content",
    "ImageContentDeleteResponse": ".image_content_delete_response",
    "ImageDetail": ".image_detail",
    "ImageFilter": ".image_filter",
    "ImageImportContentResponse": ".image_import_content_response",
    "ImageImportManifest": ".image_import_manifest",
    "ImageImportOperation": ".image_import_operation",
    "ImageImportOperationStatus": ".image_import_operation_status",
    "ImageImports": ".image_imports",
    "ImageRef": ".image_ref",
    "ImageRefType": ".image_ref_type",
    "ImageReference": ".image_reference",
    "ImageSelectionRule": ".image_selection_rule",
    "ImageSelector": ".image_selector",
    "ImageSource": ".image_source",
    "ImageWithPackages": ".image_with_packages",
    "ImportContentDigestList": ".import_content_digest_list",
    "ImportContentDigests": ".import_content_digests",
    "ImportDescriptor": ".import_descriptor",
    "ImportDistribution": ".import_distribution",
    "ImportPackage": ".import_package",
    "ImportPackageLocation": ".import_package_location",
    "ImportPackageRelationship": ".import_package_relationship",
    "ImportSchema": ".import_schema",
    "ImportSource": ".import_source",
    "LocalAnalysisSource": ".local_analysis_source",
    "MalwareScan": ".malware_scan",
    "MalwareScanFindingsItem": ".malware_scan_findings_item",
    "MappingRule": ".mapping_rule",
    "MetadataResponse": ".metadata_response",
    "NativeSbom": ".native_sbom",
    "NotificationBase": ".notification_base",
    "NvdDataList": ".nvd_data_list",
    "NvdDataObject": ".nvd_data_object",
    "PackageReference": ".package_reference",
    "PaginatedImageList": ".paginated_image_list",
    "PaginatedVulnerabilityList": ".paginated_vulnerability_list",
    "PaginatedVulnerableImageList": ".paginated_vulnerable_image_list",
    "PaginationProperties": ".pagination_properties",
    "Policy": ".policy",
    "PolicyBundle": ".policy_bundle",
    "PolicyBundleList": ".policy_bundle_list",
    "PolicyBundleRecord": ".policy_bundle_record",
    "PolicyEvalNotification": ".policy_eval_notification",
    "PolicyEvalNotificationData": ".policy_eval_notification_data",
    "PolicyEvalNotificationPayload": ".policy_eval_notification_payload",
    "PolicyEvaluation": ".policy_evaluation",
    "PolicyEvaluationList": ".policy_evaluation_list",
    "PolicyRule": ".policy_rule",
    "PolicyRuleAction": ".policy_rule_action",
    "PolicyRuleParamsItem": ".policy_rule_params_item",
    "RegexContentMatch": ".regex_content_match",
    "RegistryConfiguration": ".registry_configuration",
    "RegistryConfigurationList": ".registry_configuration_list",
    "RegistryConfigurationRequest": ".registry_configuration_request",
    "RegistryDigestSource": ".registry_digest_source",
    "RegistryTagSource": ".registry_tag_source",
    "RepositoryTagList": ".repository_tag_list",
    "RetrievedFile": ".retrieved_file",
    "RetrievedFileList": ".retrieved_file_list",
    "SecretSearchList": ".secret_search_list",
    "SecretSearchResult": ".secret_search_result",
    "Service": ".service",
    "ServiceList": ".service_list",
    "ServiceVersion": ".service_version",
    "ServiceVersionApi": ".service_version_api",
    "ServiceVersionDb": ".service_version_db",
    "ServiceVersionService": ".service_version_service",
    "StandaloneVulnerability": ".standalone_vulnerability",
    "StandaloneVulnerabilitySeverity": ".standalone_vulnerability_severity",
    "StatusResponse": ".status_response",
    "Subscription": ".subscription",
    "SubscriptionList": ".subscription_list",
    "SystemStatusResponse": ".system_status_response",
    "TagEntry": ".tag_entry",
    "TagUpdateNotification": ".tag_update_notification",
    "TagUpdateNotificationData": ".tag_update_notification_data",
    "TagUpdateNotificationPayload": ".tag_update_notification_payload",
    "TokenResponse": ".token_response",
    "TriggerParamSpec": ".trigger_param_spec",
    "TriggerParamSpecState": ".trigger_param_spec_state",
    "TriggerSpec": ".trigger_spec",
    "TriggerSpecState": ".trigger_spec_state",
    "User": ".user",
    "UserList": ".user_list",
    "UserType": ".user_type",
    "VendorDataList": ".vendor_data_list",
    "VendorDataObject": ".vendor_data_object",
    "VulnDiffResult": ".vuln_diff_result",
    "VulnUpdateNotification": ".vuln_update_notification",
    "VulnUpdateNotificationData": ".vuln_update_notification_data",
    "VulnUpdateNotificationPayload": ".vuln_update_notification_payload",
    "Vulnerability": ".vulnerability",
    "VulnerabilityList": ".vulnerability_list",
    "VulnerabilityReference": ".vulnerability_reference",
    "VulnerabilityResponse": ".vulnerability_response",
    "VulnerableImage": ".vulnerable_image",
    "VulnerablePackageReference": ".vulnerable_package_reference",
    "Whitelist": ".whitelist",
    "WhitelistItem": ".whitelist_item",
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
    "AccessCredential",
    "AccessCredentialType",
    "Account",
    "AccountList",
    "AccountState",
    "AccountStatus",
    "AccountStatusState",
    "AccountType",
    "AddAnalysisArchiveResult",
    "AnalysisArchiveAddResult",
    "AnalysisArchiveAddResultStatus",
    "AnalysisArchiveRules",
    "AnalysisArchiveRulesSummary",
    "AnalysisArchiveSource",
    "AnalysisArchiveSummary",
    "AnalysisArchiveTransitionHistory",
    "AnalysisArchiveTransitionHistoryTransition",
    "AnalysisArchiveTransitionRule",
    "AnalysisArchiveTransitionRuleExclude",
    "AnalysisArchiveTransitionRuleTransition",
    "AnalysisUpdateEval",
    "AnalysisUpdateNotification",
    "AnalysisUpdateNotificationData",
    "AnalysisUpdateNotificationPayload",
    "AnchoreErrorCode",
    "AnchoreImage",
    "AnchoreImageAnalysisStatus",
    "AnchoreImageImageStatus",
    "AnchoreImageList",
    "AnchoreImageTagSummary",
    "AnchoreImageTagSummaryList",
    "Annotations",
    "ApiErrorResponse",
    "ArchiveSummary",
    "ArchivedAnalyses",
    "ArchivedAnalysis",
    "ArchivedAnalysisStatus",
    "BaseNotificationData",
    "ContentFilesResponse",
    "ContentFilesResponseContentItem",
    "ContentJavaPackageResponse",
    "ContentJavaPackageResponseContentItem",
    "ContentMalwareResponse",
    "ContentPackageResponse",
    "ContentPackageResponseContentItem",
    "ContentResponse",
    "CredentialList",
    "Cvssv2Scores",
    "Cvssv3Scores",
    "DeleteImageResponse",
    "DeleteImageResponseList",
    "DeleteImageResponseStatus",
    "EventCategory",
    "EventDescription",
    "EventResponse",
    "EventResponseEvent",
    "EventResponseEventResource",
    "EventResponseEventSource",
    "EventSubcategory",
    "EventTypesList",
    "EventsList",
    "FeedGroupMetadata",
    "FeedMetadata",
    "FeedSyncResult",
    "FeedSyncResultStatus",
    "FeedSyncResults",
    "FileContentSearchList",
    "FileContentSearchResult",
    "GateSpec",
    "GateSpecState",
    "GenericNotificationPayload",
    "GroupSyncResult",
    "GroupSyncResultStatus",
    "ImageAnalysisReferences",
    "ImageAnalysisReport",
    "ImageContent",
    "ImageContentDeleteResponse",
    "ImageDetail",
    "ImageFilter",
    "ImageImportContentResponse",
    "ImageImportManifest",
    "ImageImportOperation",
    "ImageImportOperationStatus",
    "ImageImports",
    "ImageRef",
    "ImageRefType",
    "ImageReference",
    "ImageSelectionRule",
    "ImageSelector",
    "ImageSource",
    "ImageWithPackages",
    "ImportContentDigestList",
    "ImportContentDigests",
    "ImportDescriptor",
    "ImportDistribution",
    "ImportPackage",
    "ImportPackageLocation",
    "ImportPackageRelationship",
    "ImportSchema",
    "ImportSource",
    "LocalAnalysisSource",
    "MalwareScan",
    "MalwareScanFindingsItem",
    "MappingRule",
    "MetadataResponse",
    "NativeSbom",
    "NotificationBase",
    "NvdDataList",
    "NvdDataObject",
    "PackageReference",
    "PaginatedImageList",
    "PaginatedVulnerabilityList",
    "PaginatedVulnerableImageList",
    "PaginationProperties",
    "Policy",
    "PolicyBundle",
    "PolicyBundleList",
    "PolicyBundleRecord",
    "PolicyEvalNotification",
    "PolicyEvalNotificationData",
    "PolicyEvalNotificationPayload",
    "PolicyEvaluation",
    "PolicyEvaluationList",
    "PolicyRule",
    "PolicyRuleAction",
    "PolicyRuleParamsItem",
    "RegexContentMatch",
    "RegistryConfiguration",
    "RegistryConfigurationList",
    "RegistryConfigurationRequest",
    "RegistryDigestSource",
    "RegistryTagSource",
    "RepositoryTagList",
    "RetrievedFile",
    "RetrievedFileList",
    "SecretSearchList",
    "SecretSearchResult",
    "Service",
    "ServiceList",
    "ServiceVersion",
    "ServiceVersionApi",
    "ServiceVersionDb",
    "ServiceVersionService",
    "StandaloneVulnerability",
    "StandaloneVulnerabilitySeverity",
    "StatusResponse",
    "Subscription",
    "SubscriptionList",
    "SystemStatusResponse",
    "TagEntry",
    "TagUpdateNotification",
    "TagUpdateNotificationData",
    "TagUpdateNotificationPayload",
    "TokenResponse",
    "TriggerParamSpec",
    "TriggerParamSpecState",
    "TriggerSpec",
    "TriggerSpecState",
    "User",
    "UserList",
    "UserType",
    "VendorDataList",
    "VendorDataObject",
    "VulnDiffResult",
    "VulnUpdateNotification",
    "VulnUpdateNotificationData",
    "VulnUpdateNotificationPayload",
    "Vulnerability",
    "VulnerabilityList",
    "VulnerabilityReference",
    "VulnerabilityResponse",
    "VulnerableImage",
    "VulnerablePackageReference",
    "Whitelist",
    "WhitelistItem",
]
