



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .create_drive_group_response import CreateDriveGroupResponse
    from .create_drive_response import CreateDriveResponse
    from .create_file_request import CreateFileRequest
    from .create_file_response import CreateFileResponse
    from .create_folder_response import CreateFolderResponse
    from .create_shared_link_response import CreateSharedLinkResponse
    from .create_upload_session_response import CreateUploadSessionResponse
    from .created_at import CreatedAt
    from .created_by import CreatedBy
    from .delete_drive_group_response import DeleteDriveGroupResponse
    from .delete_drive_response import DeleteDriveResponse
    from .delete_file_response import DeleteFileResponse
    from .delete_folder_response import DeleteFolderResponse
    from .delete_shared_link_response import DeleteSharedLinkResponse
    from .delete_upload_session_response import DeleteUploadSessionResponse
    from .description import Description
    from .downstream_id import DownstreamId
    from .drive import Drive
    from .drive_group import DriveGroup
    from .drive_groups_filter import DriveGroupsFilter
    from .drives_filter import DrivesFilter
    from .expires_at import ExpiresAt
    from .file_size import FileSize
    from .file_storage_event_type import FileStorageEventType
    from .file_type import FileType
    from .files_filter import FilesFilter
    from .files_sort import FilesSort
    from .files_sort_by import FilesSortBy
    from .folder import Folder
    from .get_drive_group_response import GetDriveGroupResponse
    from .get_drive_groups_response import GetDriveGroupsResponse
    from .get_drive_response import GetDriveResponse
    from .get_drives_response import GetDrivesResponse
    from .get_file_response import GetFileResponse
    from .get_files_response import GetFilesResponse
    from .get_folder_response import GetFolderResponse
    from .get_folders_response import GetFoldersResponse
    from .get_shared_link_response import GetSharedLinkResponse
    from .get_shared_links_response import GetSharedLinksResponse
    from .get_upload_session_response import GetUploadSessionResponse
    from .id import Id
    from .linked_folder import LinkedFolder
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .owner import Owner
    from .parent_folder_id import ParentFolderId
    from .pass_through_query import PassThroughQuery
    from .payment_required_response import PaymentRequiredResponse
    from .shared_link import SharedLink
    from .shared_link_scope import SharedLinkScope
    from .shared_link_target import SharedLinkTarget
    from .sort_direction import SortDirection
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_file import UnifiedFile
    from .unified_id import UnifiedId
    from .unprocessable_response import UnprocessableResponse
    from .update_drive_group_response import UpdateDriveGroupResponse
    from .update_drive_response import UpdateDriveResponse
    from .update_file_response import UpdateFileResponse
    from .update_folder_response import UpdateFolderResponse
    from .update_shared_link_response import UpdateSharedLinkResponse
    from .update_upload_session_response import UpdateUploadSessionResponse
    from .updated_at import UpdatedAt
    from .updated_by import UpdatedBy
    from .upload_session import UploadSession
    from .webhook_event import WebhookEvent
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "CreateDriveGroupResponse": ".create_drive_group_response",
    "CreateDriveResponse": ".create_drive_response",
    "CreateFileRequest": ".create_file_request",
    "CreateFileResponse": ".create_file_response",
    "CreateFolderResponse": ".create_folder_response",
    "CreateSharedLinkResponse": ".create_shared_link_response",
    "CreateUploadSessionResponse": ".create_upload_session_response",
    "CreatedAt": ".created_at",
    "CreatedBy": ".created_by",
    "DeleteDriveGroupResponse": ".delete_drive_group_response",
    "DeleteDriveResponse": ".delete_drive_response",
    "DeleteFileResponse": ".delete_file_response",
    "DeleteFolderResponse": ".delete_folder_response",
    "DeleteSharedLinkResponse": ".delete_shared_link_response",
    "DeleteUploadSessionResponse": ".delete_upload_session_response",
    "Description": ".description",
    "DownstreamId": ".downstream_id",
    "Drive": ".drive",
    "DriveGroup": ".drive_group",
    "DriveGroupsFilter": ".drive_groups_filter",
    "DrivesFilter": ".drives_filter",
    "ExpiresAt": ".expires_at",
    "FileSize": ".file_size",
    "FileStorageEventType": ".file_storage_event_type",
    "FileType": ".file_type",
    "FilesFilter": ".files_filter",
    "FilesSort": ".files_sort",
    "FilesSortBy": ".files_sort_by",
    "Folder": ".folder",
    "GetDriveGroupResponse": ".get_drive_group_response",
    "GetDriveGroupsResponse": ".get_drive_groups_response",
    "GetDriveResponse": ".get_drive_response",
    "GetDrivesResponse": ".get_drives_response",
    "GetFileResponse": ".get_file_response",
    "GetFilesResponse": ".get_files_response",
    "GetFolderResponse": ".get_folder_response",
    "GetFoldersResponse": ".get_folders_response",
    "GetSharedLinkResponse": ".get_shared_link_response",
    "GetSharedLinksResponse": ".get_shared_links_response",
    "GetUploadSessionResponse": ".get_upload_session_response",
    "Id": ".id",
    "LinkedFolder": ".linked_folder",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "Owner": ".owner",
    "ParentFolderId": ".parent_folder_id",
    "PassThroughQuery": ".pass_through_query",
    "PaymentRequiredResponse": ".payment_required_response",
    "SharedLink": ".shared_link",
    "SharedLinkScope": ".shared_link_scope",
    "SharedLinkTarget": ".shared_link_target",
    "SortDirection": ".sort_direction",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedFile": ".unified_file",
    "UnifiedId": ".unified_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateDriveGroupResponse": ".update_drive_group_response",
    "UpdateDriveResponse": ".update_drive_response",
    "UpdateFileResponse": ".update_file_response",
    "UpdateFolderResponse": ".update_folder_response",
    "UpdateSharedLinkResponse": ".update_shared_link_response",
    "UpdateUploadSessionResponse": ".update_upload_session_response",
    "UpdatedAt": ".updated_at",
    "UpdatedBy": ".updated_by",
    "UploadSession": ".upload_session",
    "WebhookEvent": ".webhook_event",
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
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "CreateDriveGroupResponse",
    "CreateDriveResponse",
    "CreateFileRequest",
    "CreateFileResponse",
    "CreateFolderResponse",
    "CreateSharedLinkResponse",
    "CreateUploadSessionResponse",
    "CreatedAt",
    "CreatedBy",
    "DeleteDriveGroupResponse",
    "DeleteDriveResponse",
    "DeleteFileResponse",
    "DeleteFolderResponse",
    "DeleteSharedLinkResponse",
    "DeleteUploadSessionResponse",
    "Description",
    "DownstreamId",
    "Drive",
    "DriveGroup",
    "DriveGroupsFilter",
    "DrivesFilter",
    "ExpiresAt",
    "FileSize",
    "FileStorageEventType",
    "FileType",
    "FilesFilter",
    "FilesSort",
    "FilesSortBy",
    "Folder",
    "GetDriveGroupResponse",
    "GetDriveGroupsResponse",
    "GetDriveResponse",
    "GetDrivesResponse",
    "GetFileResponse",
    "GetFilesResponse",
    "GetFolderResponse",
    "GetFoldersResponse",
    "GetSharedLinkResponse",
    "GetSharedLinksResponse",
    "GetUploadSessionResponse",
    "Id",
    "LinkedFolder",
    "Links",
    "Meta",
    "MetaCursors",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "Owner",
    "ParentFolderId",
    "PassThroughQuery",
    "PaymentRequiredResponse",
    "SharedLink",
    "SharedLinkScope",
    "SharedLinkTarget",
    "SortDirection",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedFile",
    "UnifiedId",
    "UnprocessableResponse",
    "UpdateDriveGroupResponse",
    "UpdateDriveResponse",
    "UpdateFileResponse",
    "UpdateFolderResponse",
    "UpdateSharedLinkResponse",
    "UpdateUploadSessionResponse",
    "UpdatedAt",
    "UpdatedBy",
    "UploadSession",
    "WebhookEvent",
]
