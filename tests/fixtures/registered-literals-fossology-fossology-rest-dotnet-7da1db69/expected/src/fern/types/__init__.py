



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_edit_delete_license_decision import AddEditDeleteLicenseDecision
    from .admin_license_acknowledgement import AdminLicenseAcknowledgement
    from .agent_of_upload import AgentOfUpload
    from .agent_of_upload_successful_agents_item import AgentOfUploadSuccessfulAgentsItem
    from .agents_revision import AgentsRevision
    from .all_server_jobs import AllServerJobs
    from .all_server_jobs_data_item import AllServerJobsDataItem
    from .all_server_jobs_scheduler import AllServerJobsScheduler
    from .analysis import Analysis
    from .ap_iinfo import ApIinfo
    from .api_info import ApiInfo
    from .api_info_fossology import ApiInfoFossology
    from .api_info_license import ApiInfoLicense
    from .clearing_progress_info import ClearingProgressInfo
    from .conf_response import ConfResponse
    from .conf_response_component_type import ConfResponseComponentType
    from .conf_response_type import ConfResponseType
    from .conf_response_unified_columns import ConfResponseUnifiedColumns
    from .conf_response_unified_columns_report_conf_section_id import ConfResponseUnifiedColumnsReportConfSectionId
    from .customise import Customise
    from .customise_type import CustomiseType
    from .decision_importer import DecisionImporter
    from .disk_usage import DiskUsage
    from .disk_usage_data_item import DiskUsageDataItem
    from .disk_usage_notes import DiskUsageNotes
    from .edited_license import EditedLicense
    from .file import File
    from .file_message import FileMessage
    from .fileinfo import Fileinfo
    from .findings import Findings
    from .folder import Folder
    from .get_active_query import GetActiveQuery
    from .get_active_query_query import GetActiveQueryQuery
    from .get_bulk_history import GetBulkHistory
    from .get_clearing_history import GetClearingHistory
    from .get_clearing_history_scope import GetClearingHistoryScope
    from .get_clearing_history_type import GetClearingHistoryType
    from .get_database_content import GetDatabaseContent
    from .get_database_metric import GetDatabaseMetric
    from .get_file_copyrights import GetFileCopyrights
    from .get_folder_content import GetFolderContent
    from .get_job_statistics import GetJobStatistics
    from .get_php_info import GetPhpInfo
    from .get_php_info_loaded_extensions_item import GetPhpInfoLoadedExtensionsItem
    from .get_prev_next_item import GetPrevNextItem
    from .get_reuse_report_summary import GetReuseReportSummary
    from .get_scheduler_option import GetSchedulerOption
    from .get_suggested_license import GetSuggestedLicense
    from .group import Group
    from .hash import Hash
    from .health_info import HealthInfo
    from .health_info_db import HealthInfoDb
    from .health_info_db_status import HealthInfoDbStatus
    from .health_info_scheduler import HealthInfoScheduler
    from .health_info_scheduler_status import HealthInfoSchedulerStatus
    from .health_info_status import HealthInfoStatus
    from .highlight_info import HighlightInfo
    from .highlight_info_type import HighlightInfoType
    from .info import Info
    from .info_type import InfoType
    from .job import Job
    from .job_queue import JobQueue
    from .job_queue_download import JobQueueDownload
    from .job_status import JobStatus
    from .license import License
    from .license_candidate import LicenseCandidate
    from .license_decider import LicenseDecider
    from .license_decision import LicenseDecision
    from .license_decision_sources_item import LicenseDecisionSourcesItem
    from .license_histogram import LicenseHistogram
    from .mutate_admin_acknowledgement import MutateAdminAcknowledgement
    from .mutate_std_comment import MutateStdComment
    from .obligation import Obligation
    from .obligation_classification import ObligationClassification
    from .obligation_extended import ObligationExtended
    from .obligations_list import ObligationsList
    from .obligations_list_item import ObligationsListItem
    from .one_shot_info import OneShotInfo
    from .reuser import Reuser
    from .scan_options import ScanOptions
    from .scancode import Scancode
    from .scanned_edited_license import ScannedEditedLicense
    from .scanned_edited_license_details import ScannedEditedLicenseDetails
    from .scanned_license import ScannedLicense
    from .search_results import SearchResults
    from .server_upload import ServerUpload
    from .set_copyright_info import SetCopyrightInfo
    from .show_job import ShowJob
    from .spdx_rdf_import import SpdxRdfImport
    from .spdx_rdf_import_add_new_licenses_as import SpdxRdfImportAddNewLicensesAs
    from .standard_comment import StandardComment
    from .token import Token
    from .token_request import TokenRequest
    from .token_request_token_scope import TokenRequestTokenScope
    from .token_scope import TokenScope
    from .tree_view_model import TreeViewModel
    from .tree_view_model_clearing_progress import TreeViewModelClearingProgress
    from .tree_view_model_clearing_status import TreeViewModelClearingStatus
    from .tree_view_model_edited_license_list_item import TreeViewModelEditedLicenseListItem
    from .tree_view_model_file_details import TreeViewModelFileDetails
    from .tree_view_model_license_list_item import TreeViewModelLicenseListItem
    from .tree_view_model_license_list_item_agents_item import TreeViewModelLicenseListItemAgentsItem
    from .upload import Upload
    from .upload_copyrights import UploadCopyrights
    from .upload_copyrights_item import UploadCopyrightsItem
    from .upload_licenses import UploadLicenses
    from .upload_licenses_item import UploadLicensesItem
    from .upload_perm_groups import UploadPermGroups
    from .upload_perm_groups_perm_groups_item import UploadPermGroupsPermGroupsItem
    from .upload_summary import UploadSummary
    from .upload_summary_clearing_status import UploadSummaryClearingStatus
    from .url_upload import UrlUpload
    from .user import User
    from .user_access_level import UserAccessLevel
    from .user_group_member import UserGroupMember
    from .vcs_upload import VcsUpload
    from .vcs_upload_vcs_type import VcsUploadVcsType
_dynamic_imports: typing.Dict[str, str] = {
    "AddEditDeleteLicenseDecision": ".add_edit_delete_license_decision",
    "AdminLicenseAcknowledgement": ".admin_license_acknowledgement",
    "AgentOfUpload": ".agent_of_upload",
    "AgentOfUploadSuccessfulAgentsItem": ".agent_of_upload_successful_agents_item",
    "AgentsRevision": ".agents_revision",
    "AllServerJobs": ".all_server_jobs",
    "AllServerJobsDataItem": ".all_server_jobs_data_item",
    "AllServerJobsScheduler": ".all_server_jobs_scheduler",
    "Analysis": ".analysis",
    "ApIinfo": ".ap_iinfo",
    "ApiInfo": ".api_info",
    "ApiInfoFossology": ".api_info_fossology",
    "ApiInfoLicense": ".api_info_license",
    "ClearingProgressInfo": ".clearing_progress_info",
    "ConfResponse": ".conf_response",
    "ConfResponseComponentType": ".conf_response_component_type",
    "ConfResponseType": ".conf_response_type",
    "ConfResponseUnifiedColumns": ".conf_response_unified_columns",
    "ConfResponseUnifiedColumnsReportConfSectionId": ".conf_response_unified_columns_report_conf_section_id",
    "Customise": ".customise",
    "CustomiseType": ".customise_type",
    "DecisionImporter": ".decision_importer",
    "DiskUsage": ".disk_usage",
    "DiskUsageDataItem": ".disk_usage_data_item",
    "DiskUsageNotes": ".disk_usage_notes",
    "EditedLicense": ".edited_license",
    "File": ".file",
    "FileMessage": ".file_message",
    "Fileinfo": ".fileinfo",
    "Findings": ".findings",
    "Folder": ".folder",
    "GetActiveQuery": ".get_active_query",
    "GetActiveQueryQuery": ".get_active_query_query",
    "GetBulkHistory": ".get_bulk_history",
    "GetClearingHistory": ".get_clearing_history",
    "GetClearingHistoryScope": ".get_clearing_history_scope",
    "GetClearingHistoryType": ".get_clearing_history_type",
    "GetDatabaseContent": ".get_database_content",
    "GetDatabaseMetric": ".get_database_metric",
    "GetFileCopyrights": ".get_file_copyrights",
    "GetFolderContent": ".get_folder_content",
    "GetJobStatistics": ".get_job_statistics",
    "GetPhpInfo": ".get_php_info",
    "GetPhpInfoLoadedExtensionsItem": ".get_php_info_loaded_extensions_item",
    "GetPrevNextItem": ".get_prev_next_item",
    "GetReuseReportSummary": ".get_reuse_report_summary",
    "GetSchedulerOption": ".get_scheduler_option",
    "GetSuggestedLicense": ".get_suggested_license",
    "Group": ".group",
    "Hash": ".hash",
    "HealthInfo": ".health_info",
    "HealthInfoDb": ".health_info_db",
    "HealthInfoDbStatus": ".health_info_db_status",
    "HealthInfoScheduler": ".health_info_scheduler",
    "HealthInfoSchedulerStatus": ".health_info_scheduler_status",
    "HealthInfoStatus": ".health_info_status",
    "HighlightInfo": ".highlight_info",
    "HighlightInfoType": ".highlight_info_type",
    "Info": ".info",
    "InfoType": ".info_type",
    "Job": ".job",
    "JobQueue": ".job_queue",
    "JobQueueDownload": ".job_queue_download",
    "JobStatus": ".job_status",
    "License": ".license",
    "LicenseCandidate": ".license_candidate",
    "LicenseDecider": ".license_decider",
    "LicenseDecision": ".license_decision",
    "LicenseDecisionSourcesItem": ".license_decision_sources_item",
    "LicenseHistogram": ".license_histogram",
    "MutateAdminAcknowledgement": ".mutate_admin_acknowledgement",
    "MutateStdComment": ".mutate_std_comment",
    "Obligation": ".obligation",
    "ObligationClassification": ".obligation_classification",
    "ObligationExtended": ".obligation_extended",
    "ObligationsList": ".obligations_list",
    "ObligationsListItem": ".obligations_list_item",
    "OneShotInfo": ".one_shot_info",
    "Reuser": ".reuser",
    "ScanOptions": ".scan_options",
    "Scancode": ".scancode",
    "ScannedEditedLicense": ".scanned_edited_license",
    "ScannedEditedLicenseDetails": ".scanned_edited_license_details",
    "ScannedLicense": ".scanned_license",
    "SearchResults": ".search_results",
    "ServerUpload": ".server_upload",
    "SetCopyrightInfo": ".set_copyright_info",
    "ShowJob": ".show_job",
    "SpdxRdfImport": ".spdx_rdf_import",
    "SpdxRdfImportAddNewLicensesAs": ".spdx_rdf_import_add_new_licenses_as",
    "StandardComment": ".standard_comment",
    "Token": ".token",
    "TokenRequest": ".token_request",
    "TokenRequestTokenScope": ".token_request_token_scope",
    "TokenScope": ".token_scope",
    "TreeViewModel": ".tree_view_model",
    "TreeViewModelClearingProgress": ".tree_view_model_clearing_progress",
    "TreeViewModelClearingStatus": ".tree_view_model_clearing_status",
    "TreeViewModelEditedLicenseListItem": ".tree_view_model_edited_license_list_item",
    "TreeViewModelFileDetails": ".tree_view_model_file_details",
    "TreeViewModelLicenseListItem": ".tree_view_model_license_list_item",
    "TreeViewModelLicenseListItemAgentsItem": ".tree_view_model_license_list_item_agents_item",
    "Upload": ".upload",
    "UploadCopyrights": ".upload_copyrights",
    "UploadCopyrightsItem": ".upload_copyrights_item",
    "UploadLicenses": ".upload_licenses",
    "UploadLicensesItem": ".upload_licenses_item",
    "UploadPermGroups": ".upload_perm_groups",
    "UploadPermGroupsPermGroupsItem": ".upload_perm_groups_perm_groups_item",
    "UploadSummary": ".upload_summary",
    "UploadSummaryClearingStatus": ".upload_summary_clearing_status",
    "UrlUpload": ".url_upload",
    "User": ".user",
    "UserAccessLevel": ".user_access_level",
    "UserGroupMember": ".user_group_member",
    "VcsUpload": ".vcs_upload",
    "VcsUploadVcsType": ".vcs_upload_vcs_type",
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
    "AddEditDeleteLicenseDecision",
    "AdminLicenseAcknowledgement",
    "AgentOfUpload",
    "AgentOfUploadSuccessfulAgentsItem",
    "AgentsRevision",
    "AllServerJobs",
    "AllServerJobsDataItem",
    "AllServerJobsScheduler",
    "Analysis",
    "ApIinfo",
    "ApiInfo",
    "ApiInfoFossology",
    "ApiInfoLicense",
    "ClearingProgressInfo",
    "ConfResponse",
    "ConfResponseComponentType",
    "ConfResponseType",
    "ConfResponseUnifiedColumns",
    "ConfResponseUnifiedColumnsReportConfSectionId",
    "Customise",
    "CustomiseType",
    "DecisionImporter",
    "DiskUsage",
    "DiskUsageDataItem",
    "DiskUsageNotes",
    "EditedLicense",
    "File",
    "FileMessage",
    "Fileinfo",
    "Findings",
    "Folder",
    "GetActiveQuery",
    "GetActiveQueryQuery",
    "GetBulkHistory",
    "GetClearingHistory",
    "GetClearingHistoryScope",
    "GetClearingHistoryType",
    "GetDatabaseContent",
    "GetDatabaseMetric",
    "GetFileCopyrights",
    "GetFolderContent",
    "GetJobStatistics",
    "GetPhpInfo",
    "GetPhpInfoLoadedExtensionsItem",
    "GetPrevNextItem",
    "GetReuseReportSummary",
    "GetSchedulerOption",
    "GetSuggestedLicense",
    "Group",
    "Hash",
    "HealthInfo",
    "HealthInfoDb",
    "HealthInfoDbStatus",
    "HealthInfoScheduler",
    "HealthInfoSchedulerStatus",
    "HealthInfoStatus",
    "HighlightInfo",
    "HighlightInfoType",
    "Info",
    "InfoType",
    "Job",
    "JobQueue",
    "JobQueueDownload",
    "JobStatus",
    "License",
    "LicenseCandidate",
    "LicenseDecider",
    "LicenseDecision",
    "LicenseDecisionSourcesItem",
    "LicenseHistogram",
    "MutateAdminAcknowledgement",
    "MutateStdComment",
    "Obligation",
    "ObligationClassification",
    "ObligationExtended",
    "ObligationsList",
    "ObligationsListItem",
    "OneShotInfo",
    "Reuser",
    "ScanOptions",
    "Scancode",
    "ScannedEditedLicense",
    "ScannedEditedLicenseDetails",
    "ScannedLicense",
    "SearchResults",
    "ServerUpload",
    "SetCopyrightInfo",
    "ShowJob",
    "SpdxRdfImport",
    "SpdxRdfImportAddNewLicensesAs",
    "StandardComment",
    "Token",
    "TokenRequest",
    "TokenRequestTokenScope",
    "TokenScope",
    "TreeViewModel",
    "TreeViewModelClearingProgress",
    "TreeViewModelClearingStatus",
    "TreeViewModelEditedLicenseListItem",
    "TreeViewModelFileDetails",
    "TreeViewModelLicenseListItem",
    "TreeViewModelLicenseListItemAgentsItem",
    "Upload",
    "UploadCopyrights",
    "UploadCopyrightsItem",
    "UploadLicenses",
    "UploadLicensesItem",
    "UploadPermGroups",
    "UploadPermGroupsPermGroupsItem",
    "UploadSummary",
    "UploadSummaryClearingStatus",
    "UrlUpload",
    "User",
    "UserAccessLevel",
    "UserGroupMember",
    "VcsUpload",
    "VcsUploadVcsType",
]
