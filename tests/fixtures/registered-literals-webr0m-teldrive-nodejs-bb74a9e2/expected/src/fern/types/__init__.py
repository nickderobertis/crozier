



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .admin_user_summary import AdminUserSummary
    from .api_key_created import ApiKeyCreated
    from .api_key_summary import ApiKeySummary
    from .bot_create_response import BotCreateResponse
    from .bot_manager_response import BotManagerResponse
    from .bot_manager_response_pending_item import BotManagerResponsePendingItem
    from .bot_summary import BotSummary
    from .casting_device import CastingDevice
    from .casting_device_protocol import CastingDeviceProtocol
    from .casting_devices import CastingDevices
    from .casting_relay import CastingRelay
    from .channel_health import ChannelHealth
    from .channel_summary import ChannelSummary
    from .checksum import Checksum
    from .cookie_session import CookieSession
    from .cursor import Cursor
    from .discovered_channel import DiscoveredChannel
    from .drive_statistics import DriveStatistics
    from .e_tag import ETag
    from .error_detail import ErrorDetail
    from .error_envelope import ErrorEnvelope
    from .event_stream_ticket import EventStreamTicket
    from .file_access_grant_summary import FileAccessGrantSummary
    from .file_bulk_result import FileBulkResult
    from .file_bulk_trash_request import FileBulkTrashRequest
    from .file_category import FileCategory
    from .file_category_statistics import FileCategoryStatistics
    from .file_entry import FileEntry
    from .file_hash import FileHash
    from .file_kind import FileKind
    from .file_list_scope import FileListScope
    from .file_search_type import FileSearchType
    from .file_sort import FileSort
    from .file_status import FileStatus
    from .file_update_request import FileUpdateRequest
    from .file_view_state import FileViewState
    from .folder_create_request import FolderCreateRequest
    from .hash_algorithm import HashAlgorithm
    from .health_status import HealthStatus
    from .health_status_status import HealthStatusStatus
    from .job import Job
    from .job_attempt_error import JobAttemptError
    from .job_page import JobPage
    from .job_page_meta import JobPageMeta
    from .job_purge_result import JobPurgeResult
    from .job_queue import JobQueue
    from .job_queue_list import JobQueueList
    from .job_state import JobState
    from .job_statistics import JobStatistics
    from .managed_bot_response import ManagedBotResponse
    from .media_format import MediaFormat
    from .media_track import MediaTrack
    from .media_track_kind import MediaTrackKind
    from .media_tracks import MediaTracks
    from .name_conflict_policy import NameConflictPolicy
    from .periodic_job import PeriodicJob
    from .periodic_job_catalog import PeriodicJobCatalog
    from .periodic_job_list import PeriodicJobList
    from .periodic_job_template import PeriodicJobTemplate
    from .playback_diagnostics import PlaybackDiagnostics
    from .playback_diagnostics_file import PlaybackDiagnosticsFile
    from .playback_diagnostics_metadata import PlaybackDiagnosticsMetadata
    from .playback_diagnostics_nodes_item import PlaybackDiagnosticsNodesItem
    from .playback_diagnostics_nodes_item_role import PlaybackDiagnosticsNodesItemRole
    from .playback_diagnostics_nodes_item_sources_item import PlaybackDiagnosticsNodesItemSourcesItem
    from .playback_diagnostics_nodes_item_sources_item_kind import PlaybackDiagnosticsNodesItemSourcesItemKind
    from .playback_diagnostics_nodes_item_streams_item import PlaybackDiagnosticsNodesItemStreamsItem
    from .playback_diagnostics_nodes_item_streams_item_conversion_value import (
        PlaybackDiagnosticsNodesItemStreamsItemConversionValue,
    )
    from .playback_diagnostics_nodes_item_streams_item_reader import PlaybackDiagnosticsNodesItemStreamsItemReader
    from .playback_session import PlaybackSession
    from .public_share import PublicShare
    from .session_summary import SessionSummary
    from .share_created import ShareCreated
    from .share_permission import SharePermission
    from .share_summary import ShareSummary
    from .shared_with_me_entry import SharedWithMeEntry
    from .sort_order import SortOrder
    from .storage_activity import StorageActivity
    from .storage_channel_statistic import StorageChannelStatistic
    from .storage_cleanup_statistics import StorageCleanupStatistics
    from .storage_dashboard import StorageDashboard
    from .storage_growth_point import StorageGrowthPoint
    from .storage_summary import StorageSummary
    from .telegram_code_verify_request import TelegramCodeVerifyRequest
    from .telegram_login_start_response import TelegramLoginStartResponse
    from .telegram_password_verify_request import TelegramPasswordVerifyRequest
    from .telegram_qr_login_poll_request import TelegramQrLoginPollRequest
    from .telegram_qr_login_response import TelegramQrLoginResponse
    from .telegram_qr_login_state import TelegramQrLoginState
    from .token_pair import TokenPair
    from .token_pair_token_type import TokenPairTokenType
    from .upload_create_request import UploadCreateRequest
    from .upload_daily_statistics import UploadDailyStatistics
    from .upload_import_source import UploadImportSource
    from .upload_import_source_type import UploadImportSourceType
    from .upload_part import UploadPart
    from .upload_part_state import UploadPartState
    from .upload_session import UploadSession
    from .upload_state import UploadState
    from .uri import Uri
    from .user_profile import UserProfile
    from .user_role import UserRole
    from .user_search_result import UserSearchResult
    from .uuid_ import Uuid
    from .viewer_kind import ViewerKind
_dynamic_imports: typing.Dict[str, str] = {
    "AdminUserSummary": ".admin_user_summary",
    "ApiKeyCreated": ".api_key_created",
    "ApiKeySummary": ".api_key_summary",
    "BotCreateResponse": ".bot_create_response",
    "BotManagerResponse": ".bot_manager_response",
    "BotManagerResponsePendingItem": ".bot_manager_response_pending_item",
    "BotSummary": ".bot_summary",
    "CastingDevice": ".casting_device",
    "CastingDeviceProtocol": ".casting_device_protocol",
    "CastingDevices": ".casting_devices",
    "CastingRelay": ".casting_relay",
    "ChannelHealth": ".channel_health",
    "ChannelSummary": ".channel_summary",
    "Checksum": ".checksum",
    "CookieSession": ".cookie_session",
    "Cursor": ".cursor",
    "DiscoveredChannel": ".discovered_channel",
    "DriveStatistics": ".drive_statistics",
    "ETag": ".e_tag",
    "ErrorDetail": ".error_detail",
    "ErrorEnvelope": ".error_envelope",
    "EventStreamTicket": ".event_stream_ticket",
    "FileAccessGrantSummary": ".file_access_grant_summary",
    "FileBulkResult": ".file_bulk_result",
    "FileBulkTrashRequest": ".file_bulk_trash_request",
    "FileCategory": ".file_category",
    "FileCategoryStatistics": ".file_category_statistics",
    "FileEntry": ".file_entry",
    "FileHash": ".file_hash",
    "FileKind": ".file_kind",
    "FileListScope": ".file_list_scope",
    "FileSearchType": ".file_search_type",
    "FileSort": ".file_sort",
    "FileStatus": ".file_status",
    "FileUpdateRequest": ".file_update_request",
    "FileViewState": ".file_view_state",
    "FolderCreateRequest": ".folder_create_request",
    "HashAlgorithm": ".hash_algorithm",
    "HealthStatus": ".health_status",
    "HealthStatusStatus": ".health_status_status",
    "Job": ".job",
    "JobAttemptError": ".job_attempt_error",
    "JobPage": ".job_page",
    "JobPageMeta": ".job_page_meta",
    "JobPurgeResult": ".job_purge_result",
    "JobQueue": ".job_queue",
    "JobQueueList": ".job_queue_list",
    "JobState": ".job_state",
    "JobStatistics": ".job_statistics",
    "ManagedBotResponse": ".managed_bot_response",
    "MediaFormat": ".media_format",
    "MediaTrack": ".media_track",
    "MediaTrackKind": ".media_track_kind",
    "MediaTracks": ".media_tracks",
    "NameConflictPolicy": ".name_conflict_policy",
    "PeriodicJob": ".periodic_job",
    "PeriodicJobCatalog": ".periodic_job_catalog",
    "PeriodicJobList": ".periodic_job_list",
    "PeriodicJobTemplate": ".periodic_job_template",
    "PlaybackDiagnostics": ".playback_diagnostics",
    "PlaybackDiagnosticsFile": ".playback_diagnostics_file",
    "PlaybackDiagnosticsMetadata": ".playback_diagnostics_metadata",
    "PlaybackDiagnosticsNodesItem": ".playback_diagnostics_nodes_item",
    "PlaybackDiagnosticsNodesItemRole": ".playback_diagnostics_nodes_item_role",
    "PlaybackDiagnosticsNodesItemSourcesItem": ".playback_diagnostics_nodes_item_sources_item",
    "PlaybackDiagnosticsNodesItemSourcesItemKind": ".playback_diagnostics_nodes_item_sources_item_kind",
    "PlaybackDiagnosticsNodesItemStreamsItem": ".playback_diagnostics_nodes_item_streams_item",
    "PlaybackDiagnosticsNodesItemStreamsItemConversionValue": ".playback_diagnostics_nodes_item_streams_item_conversion_value",
    "PlaybackDiagnosticsNodesItemStreamsItemReader": ".playback_diagnostics_nodes_item_streams_item_reader",
    "PlaybackSession": ".playback_session",
    "PublicShare": ".public_share",
    "SessionSummary": ".session_summary",
    "ShareCreated": ".share_created",
    "SharePermission": ".share_permission",
    "ShareSummary": ".share_summary",
    "SharedWithMeEntry": ".shared_with_me_entry",
    "SortOrder": ".sort_order",
    "StorageActivity": ".storage_activity",
    "StorageChannelStatistic": ".storage_channel_statistic",
    "StorageCleanupStatistics": ".storage_cleanup_statistics",
    "StorageDashboard": ".storage_dashboard",
    "StorageGrowthPoint": ".storage_growth_point",
    "StorageSummary": ".storage_summary",
    "TelegramCodeVerifyRequest": ".telegram_code_verify_request",
    "TelegramLoginStartResponse": ".telegram_login_start_response",
    "TelegramPasswordVerifyRequest": ".telegram_password_verify_request",
    "TelegramQrLoginPollRequest": ".telegram_qr_login_poll_request",
    "TelegramQrLoginResponse": ".telegram_qr_login_response",
    "TelegramQrLoginState": ".telegram_qr_login_state",
    "TokenPair": ".token_pair",
    "TokenPairTokenType": ".token_pair_token_type",
    "UploadCreateRequest": ".upload_create_request",
    "UploadDailyStatistics": ".upload_daily_statistics",
    "UploadImportSource": ".upload_import_source",
    "UploadImportSourceType": ".upload_import_source_type",
    "UploadPart": ".upload_part",
    "UploadPartState": ".upload_part_state",
    "UploadSession": ".upload_session",
    "UploadState": ".upload_state",
    "Uri": ".uri",
    "UserProfile": ".user_profile",
    "UserRole": ".user_role",
    "UserSearchResult": ".user_search_result",
    "Uuid": ".uuid_",
    "ViewerKind": ".viewer_kind",
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
    "AdminUserSummary",
    "ApiKeyCreated",
    "ApiKeySummary",
    "BotCreateResponse",
    "BotManagerResponse",
    "BotManagerResponsePendingItem",
    "BotSummary",
    "CastingDevice",
    "CastingDeviceProtocol",
    "CastingDevices",
    "CastingRelay",
    "ChannelHealth",
    "ChannelSummary",
    "Checksum",
    "CookieSession",
    "Cursor",
    "DiscoveredChannel",
    "DriveStatistics",
    "ETag",
    "ErrorDetail",
    "ErrorEnvelope",
    "EventStreamTicket",
    "FileAccessGrantSummary",
    "FileBulkResult",
    "FileBulkTrashRequest",
    "FileCategory",
    "FileCategoryStatistics",
    "FileEntry",
    "FileHash",
    "FileKind",
    "FileListScope",
    "FileSearchType",
    "FileSort",
    "FileStatus",
    "FileUpdateRequest",
    "FileViewState",
    "FolderCreateRequest",
    "HashAlgorithm",
    "HealthStatus",
    "HealthStatusStatus",
    "Job",
    "JobAttemptError",
    "JobPage",
    "JobPageMeta",
    "JobPurgeResult",
    "JobQueue",
    "JobQueueList",
    "JobState",
    "JobStatistics",
    "ManagedBotResponse",
    "MediaFormat",
    "MediaTrack",
    "MediaTrackKind",
    "MediaTracks",
    "NameConflictPolicy",
    "PeriodicJob",
    "PeriodicJobCatalog",
    "PeriodicJobList",
    "PeriodicJobTemplate",
    "PlaybackDiagnostics",
    "PlaybackDiagnosticsFile",
    "PlaybackDiagnosticsMetadata",
    "PlaybackDiagnosticsNodesItem",
    "PlaybackDiagnosticsNodesItemRole",
    "PlaybackDiagnosticsNodesItemSourcesItem",
    "PlaybackDiagnosticsNodesItemSourcesItemKind",
    "PlaybackDiagnosticsNodesItemStreamsItem",
    "PlaybackDiagnosticsNodesItemStreamsItemConversionValue",
    "PlaybackDiagnosticsNodesItemStreamsItemReader",
    "PlaybackSession",
    "PublicShare",
    "SessionSummary",
    "ShareCreated",
    "SharePermission",
    "ShareSummary",
    "SharedWithMeEntry",
    "SortOrder",
    "StorageActivity",
    "StorageChannelStatistic",
    "StorageCleanupStatistics",
    "StorageDashboard",
    "StorageGrowthPoint",
    "StorageSummary",
    "TelegramCodeVerifyRequest",
    "TelegramLoginStartResponse",
    "TelegramPasswordVerifyRequest",
    "TelegramQrLoginPollRequest",
    "TelegramQrLoginResponse",
    "TelegramQrLoginState",
    "TokenPair",
    "TokenPairTokenType",
    "UploadCreateRequest",
    "UploadDailyStatistics",
    "UploadImportSource",
    "UploadImportSourceType",
    "UploadPart",
    "UploadPartState",
    "UploadSession",
    "UploadState",
    "Uri",
    "UserProfile",
    "UserRole",
    "UserSearchResult",
    "Uuid",
    "ViewerKind",
]
