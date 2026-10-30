



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .absolute_path import AbsolutePath
    from .access_grants import AccessGrants
    from .access_revision_no import AccessRevisionNo
    from .access_right import AccessRight
    from .access_rights import AccessRights
    from .actor_id import ActorId
    from .attribute_key import AttributeKey
    from .attribute_value import AttributeValue
    from .attributes import Attributes
    from .attributes_revision_no import AttributesRevisionNo
    from .binding_version import BindingVersion
    from .capability_document import CapabilityDocument
    from .change_seq import ChangeSeq
    from .checkpoint import Checkpoint
    from .checkpoint_owner import CheckpointOwner, CheckpointOwner_Fork, CheckpointOwner_User
    from .checkpoint_owner_fork import CheckpointOwnerFork
    from .checkpoint_owner_user import CheckpointOwnerUser
    from .checksum import Checksum
    from .checksum_algorithm import ChecksumAlgorithm
    from .commit import Commit
    from .commit_id import CommitId
    from .commit_precondition import (
        CommitPrecondition,
        CommitPrecondition_AccessRevision,
        CommitPrecondition_AttributesRevision,
        CommitPrecondition_FileRevision,
        CommitPrecondition_InodeBinding,
        CommitPrecondition_NameAbsence,
        CommitPrecondition_NamespaceHead,
        CommitPrecondition_PathAbsence,
        CommitPrecondition_PathBinding,
    )
    from .commit_precondition_access_revision import CommitPreconditionAccessRevision
    from .commit_precondition_attributes_revision import CommitPreconditionAttributesRevision
    from .commit_precondition_file_revision import CommitPreconditionFileRevision
    from .commit_precondition_inode_binding import CommitPreconditionInodeBinding
    from .commit_precondition_name_absence import CommitPreconditionNameAbsence
    from .commit_precondition_namespace_head import CommitPreconditionNamespaceHead
    from .commit_precondition_path_absence import CommitPreconditionPathAbsence
    from .commit_precondition_path_binding import CommitPreconditionPathBinding
    from .complete_upload_body import (
        CompleteUploadBody,
        CompleteUploadBody_DirectMultipart,
        CompleteUploadBody_DirectPut,
        CompleteUploadBody_ServiceProxied,
    )
    from .complete_upload_body_direct_multipart import CompleteUploadBodyDirectMultipart
    from .complete_upload_body_direct_put import CompleteUploadBodyDirectPut
    from .complete_upload_body_service_proxied import CompleteUploadBodyServiceProxied
    from .completed_upload_part import CompletedUploadPart
    from .content_id import ContentId
    from .content_ref import ContentRef
    from .content_ref_kind import ContentRefKind
    from .content_token import ContentToken
    from .create_download_by_inode_response import CreateDownloadByInodeResponse
    from .create_download_response import CreateDownloadResponse
    from .create_upload_body import (
        CreateUploadBody,
        CreateUploadBody_DirectMultipart,
        CreateUploadBody_DirectPut,
        CreateUploadBody_ServiceProxied,
    )
    from .create_upload_body_direct_multipart import CreateUploadBodyDirectMultipart
    from .create_upload_body_direct_put import CreateUploadBodyDirectPut
    from .create_upload_body_service_proxied import CreateUploadBodyServiceProxied
    from .delete_directory_behavior import DeleteDirectoryBehavior
    from .delete_namespace_response import DeleteNamespaceResponse
    from .delete_snapshot_response import DeleteSnapshotResponse
    from .deleted_checkpoints_by_owner import DeletedCheckpointsByOwner
    from .deleted_object_counts import DeletedObjectCounts
    from .destination_behavior import DestinationBehavior
    from .directory_binding import DirectoryBinding
    from .display_name import DisplayName
    from .download_range import DownloadRange
    from .error_details import ErrorDetails
    from .error_response import ErrorResponse
    from .extension_gc_reports import ExtensionGcReports
    from .file_revision import FileRevision
    from .filesystem_change import (
        FilesystemChange,
        FilesystemChange_AccessChanged,
        FilesystemChange_AttributesChanged,
        FilesystemChange_ContentChanged,
        FilesystemChange_Deleted,
        FilesystemChange_DirectoryCreated,
        FilesystemChange_FileCreated,
        FilesystemChange_Moved,
        FilesystemChange_Undeleted,
    )
    from .filesystem_change_access_changed import FilesystemChangeAccessChanged
    from .filesystem_change_attributes_changed import FilesystemChangeAttributesChanged
    from .filesystem_change_content_changed import FilesystemChangeContentChanged
    from .filesystem_change_deleted import FilesystemChangeDeleted
    from .filesystem_change_directory_created import FilesystemChangeDirectoryCreated
    from .filesystem_change_file_created import FilesystemChangeFileCreated
    from .filesystem_change_moved import FilesystemChangeMoved
    from .filesystem_change_undeleted import FilesystemChangeUndeleted
    from .filesystem_operation import (
        FilesystemOperation,
        FilesystemOperation_AppendFile,
        FilesystemOperation_AppendFileByInode,
        FilesystemOperation_CopyByInode,
        FilesystemOperation_CopyPath,
        FilesystemOperation_CreateDirectory,
        FilesystemOperation_CreateDirectoryByInode,
        FilesystemOperation_CreateFileByInode,
        FilesystemOperation_DeleteByInode,
        FilesystemOperation_DeletePath,
        FilesystemOperation_MoveByInode,
        FilesystemOperation_MovePath,
        FilesystemOperation_PutFile,
        FilesystemOperation_PutFileRevisionByInode,
        FilesystemOperation_RestoreRevision,
        FilesystemOperation_RestoreRevisionByInode,
        FilesystemOperation_Undelete,
        FilesystemOperation_UpdateAccess,
        FilesystemOperation_UpdateAccessByInode,
        FilesystemOperation_UpdateAttributes,
        FilesystemOperation_UpdateAttributesByInode,
    )
    from .filesystem_operation_append_file import FilesystemOperationAppendFile
    from .filesystem_operation_append_file_by_inode import FilesystemOperationAppendFileByInode
    from .filesystem_operation_copy_by_inode import FilesystemOperationCopyByInode
    from .filesystem_operation_copy_path import FilesystemOperationCopyPath
    from .filesystem_operation_create_directory import FilesystemOperationCreateDirectory
    from .filesystem_operation_create_directory_by_inode import FilesystemOperationCreateDirectoryByInode
    from .filesystem_operation_create_file_by_inode import FilesystemOperationCreateFileByInode
    from .filesystem_operation_delete_by_inode import FilesystemOperationDeleteByInode
    from .filesystem_operation_delete_path import FilesystemOperationDeletePath
    from .filesystem_operation_move_by_inode import FilesystemOperationMoveByInode
    from .filesystem_operation_move_path import FilesystemOperationMovePath
    from .filesystem_operation_put_file import FilesystemOperationPutFile
    from .filesystem_operation_put_file_revision_by_inode import FilesystemOperationPutFileRevisionByInode
    from .filesystem_operation_restore_revision import FilesystemOperationRestoreRevision
    from .filesystem_operation_restore_revision_by_inode import FilesystemOperationRestoreRevisionByInode
    from .filesystem_operation_undelete import FilesystemOperationUndelete
    from .filesystem_operation_update_access import FilesystemOperationUpdateAccess
    from .filesystem_operation_update_access_by_inode import FilesystemOperationUpdateAccessByInode
    from .filesystem_operation_update_attributes import FilesystemOperationUpdateAttributes
    from .filesystem_operation_update_attributes_by_inode import FilesystemOperationUpdateAttributesByInode
    from .grep_gc_report import GrepGcReport
    from .grep_index import GrepIndex, GrepIndex_Active, GrepIndex_Backfilling, GrepIndex_Disabled
    from .grep_index_status_active import GrepIndexStatusActive
    from .grep_index_status_backfilling import GrepIndexStatusBackfilling
    from .grep_index_status_disabled import GrepIndexStatusDisabled
    from .grep_match import GrepMatch
    from .grep_response import GrepResponse
    from .inode_id import InodeId
    from .inode_kind import InodeKind
    from .list_changes_response import ListChangesResponse
    from .list_checkpoints_response import ListCheckpointsResponse
    from .list_file_revisions_response import ListFileRevisionsResponse
    from .list_inode_children_response import ListInodeChildrenResponse
    from .list_path_entries_response import ListPathEntriesResponse
    from .list_snapshots_response import ListSnapshotsResponse
    from .list_trash_response import ListTrashResponse
    from .manifest_no import ManifestNo
    from .metadata_maintenance_outcome import MetadataMaintenanceOutcome
    from .name_key import NameKey
    from .namespace_access import NamespaceAccess, NamespaceAccess_Acl, NamespaceAccess_Unrestricted
    from .namespace_access_acl import NamespaceAccessAcl
    from .namespace_access_mode import NamespaceAccessMode, NamespaceAccessMode_Acl, NamespaceAccessMode_Unrestricted
    from .namespace_access_mode_acl import NamespaceAccessModeAcl
    from .namespace_access_mode_unrestricted import NamespaceAccessModeUnrestricted
    from .namespace_access_unrestricted import NamespaceAccessUnrestricted
    from .namespace_diagnostics import NamespaceDiagnostics
    from .namespace_fork_basis import NamespaceForkBasis
    from .namespace_id import NamespaceId
    from .namespace_metadata import NamespaceMetadata
    from .object_transfer_access import ObjectTransferAccess, ObjectTransferAccess_PresignedUrl
    from .object_transfer_access_presigned_url import ObjectTransferAccessPresignedUrl
    from .path_entry import PathEntry, PathEntry_Dir, PathEntry_File
    from .path_entry_directory import PathEntryDirectory
    from .path_entry_file import PathEntryFile
    from .pin_id import PinId
    from .principal_id import PrincipalId
    from .principal_scope import PrincipalScope
    from .probe_run_id import ProbeRunId
    from .read_consistency import ReadConsistency
    from .retained_candidates import RetainedCandidates
    from .revision_no import RevisionNo
    from .run_maintenance_request import (
        RunMaintenanceRequest,
        RunMaintenanceRequest_Gc,
        RunMaintenanceRequest_Metadata,
        RunMaintenanceRequest_RecoverAdministrator,
        RunMaintenanceRequest_Retention,
        RunMaintenanceRequest_RetentionWindow,
    )
    from .run_maintenance_request_gc import RunMaintenanceRequestGc
    from .run_maintenance_request_metadata import RunMaintenanceRequestMetadata
    from .run_maintenance_request_recover_administrator import RunMaintenanceRequestRecoverAdministrator
    from .run_maintenance_request_retention import RunMaintenanceRequestRetention
    from .run_maintenance_request_retention_window import RunMaintenanceRequestRetentionWindow
    from .run_maintenance_response import (
        RunMaintenanceResponse,
        RunMaintenanceResponse_Gc,
        RunMaintenanceResponse_Metadata,
        RunMaintenanceResponse_RecoverAdministrator,
        RunMaintenanceResponse_Retention,
        RunMaintenanceResponse_RetentionWindow,
    )
    from .run_maintenance_response_gc import RunMaintenanceResponseGc
    from .run_maintenance_response_metadata import RunMaintenanceResponseMetadata
    from .run_maintenance_response_recover_administrator import RunMaintenanceResponseRecoverAdministrator
    from .run_maintenance_response_retention import RunMaintenanceResponseRetention
    from .run_maintenance_response_retention_window import RunMaintenanceResponseRetentionWindow
    from .run_no import RunNo
    from .service_unavailable_error_body import ServiceUnavailableErrorBody
    from .sign_upload_parts_response import SignUploadPartsResponse
    from .signed_upload_part import SignedUploadPart
    from .snapshot import Snapshot
    from .store_probe_check import (
        StoreProbeCheck,
        StoreProbeCheck_Failed,
        StoreProbeCheck_Passed,
        StoreProbeCheck_Unsupported,
    )
    from .store_probe_check_failed import StoreProbeCheckFailed
    from .store_probe_check_passed import StoreProbeCheckPassed
    from .store_probe_check_unsupported import StoreProbeCheckUnsupported
    from .store_probe_request import StoreProbeRequest
    from .store_probe_response import StoreProbeResponse
    from .trash_entry import TrashEntry
    from .upload_content_claim import UploadContentClaim
    from .upload_id import UploadId
    from .upload_mode import UploadMode
    from .upload_part_checksum_claim import UploadPartChecksumClaim
    from .upload_session import UploadSession, UploadSession_Aborted, UploadSession_Completed, UploadSession_Open
    from .upload_session_status_aborted import UploadSessionStatusAborted
    from .upload_session_status_completed import UploadSessionStatusCompleted
    from .upload_session_status_open import UploadSessionStatusOpen
    from .writer_epoch import WriterEpoch
    from .writer_id import WriterId
_dynamic_imports: typing.Dict[str, str] = {
    "AbsolutePath": ".absolute_path",
    "AccessGrants": ".access_grants",
    "AccessRevisionNo": ".access_revision_no",
    "AccessRight": ".access_right",
    "AccessRights": ".access_rights",
    "ActorId": ".actor_id",
    "AttributeKey": ".attribute_key",
    "AttributeValue": ".attribute_value",
    "Attributes": ".attributes",
    "AttributesRevisionNo": ".attributes_revision_no",
    "BindingVersion": ".binding_version",
    "CapabilityDocument": ".capability_document",
    "ChangeSeq": ".change_seq",
    "Checkpoint": ".checkpoint",
    "CheckpointOwner": ".checkpoint_owner",
    "CheckpointOwnerFork": ".checkpoint_owner_fork",
    "CheckpointOwnerUser": ".checkpoint_owner_user",
    "CheckpointOwner_Fork": ".checkpoint_owner",
    "CheckpointOwner_User": ".checkpoint_owner",
    "Checksum": ".checksum",
    "ChecksumAlgorithm": ".checksum_algorithm",
    "Commit": ".commit",
    "CommitId": ".commit_id",
    "CommitPrecondition": ".commit_precondition",
    "CommitPreconditionAccessRevision": ".commit_precondition_access_revision",
    "CommitPreconditionAttributesRevision": ".commit_precondition_attributes_revision",
    "CommitPreconditionFileRevision": ".commit_precondition_file_revision",
    "CommitPreconditionInodeBinding": ".commit_precondition_inode_binding",
    "CommitPreconditionNameAbsence": ".commit_precondition_name_absence",
    "CommitPreconditionNamespaceHead": ".commit_precondition_namespace_head",
    "CommitPreconditionPathAbsence": ".commit_precondition_path_absence",
    "CommitPreconditionPathBinding": ".commit_precondition_path_binding",
    "CommitPrecondition_AccessRevision": ".commit_precondition",
    "CommitPrecondition_AttributesRevision": ".commit_precondition",
    "CommitPrecondition_FileRevision": ".commit_precondition",
    "CommitPrecondition_InodeBinding": ".commit_precondition",
    "CommitPrecondition_NameAbsence": ".commit_precondition",
    "CommitPrecondition_NamespaceHead": ".commit_precondition",
    "CommitPrecondition_PathAbsence": ".commit_precondition",
    "CommitPrecondition_PathBinding": ".commit_precondition",
    "CompleteUploadBody": ".complete_upload_body",
    "CompleteUploadBodyDirectMultipart": ".complete_upload_body_direct_multipart",
    "CompleteUploadBodyDirectPut": ".complete_upload_body_direct_put",
    "CompleteUploadBodyServiceProxied": ".complete_upload_body_service_proxied",
    "CompleteUploadBody_DirectMultipart": ".complete_upload_body",
    "CompleteUploadBody_DirectPut": ".complete_upload_body",
    "CompleteUploadBody_ServiceProxied": ".complete_upload_body",
    "CompletedUploadPart": ".completed_upload_part",
    "ContentId": ".content_id",
    "ContentRef": ".content_ref",
    "ContentRefKind": ".content_ref_kind",
    "ContentToken": ".content_token",
    "CreateDownloadByInodeResponse": ".create_download_by_inode_response",
    "CreateDownloadResponse": ".create_download_response",
    "CreateUploadBody": ".create_upload_body",
    "CreateUploadBodyDirectMultipart": ".create_upload_body_direct_multipart",
    "CreateUploadBodyDirectPut": ".create_upload_body_direct_put",
    "CreateUploadBodyServiceProxied": ".create_upload_body_service_proxied",
    "CreateUploadBody_DirectMultipart": ".create_upload_body",
    "CreateUploadBody_DirectPut": ".create_upload_body",
    "CreateUploadBody_ServiceProxied": ".create_upload_body",
    "DeleteDirectoryBehavior": ".delete_directory_behavior",
    "DeleteNamespaceResponse": ".delete_namespace_response",
    "DeleteSnapshotResponse": ".delete_snapshot_response",
    "DeletedCheckpointsByOwner": ".deleted_checkpoints_by_owner",
    "DeletedObjectCounts": ".deleted_object_counts",
    "DestinationBehavior": ".destination_behavior",
    "DirectoryBinding": ".directory_binding",
    "DisplayName": ".display_name",
    "DownloadRange": ".download_range",
    "ErrorDetails": ".error_details",
    "ErrorResponse": ".error_response",
    "ExtensionGcReports": ".extension_gc_reports",
    "FileRevision": ".file_revision",
    "FilesystemChange": ".filesystem_change",
    "FilesystemChangeAccessChanged": ".filesystem_change_access_changed",
    "FilesystemChangeAttributesChanged": ".filesystem_change_attributes_changed",
    "FilesystemChangeContentChanged": ".filesystem_change_content_changed",
    "FilesystemChangeDeleted": ".filesystem_change_deleted",
    "FilesystemChangeDirectoryCreated": ".filesystem_change_directory_created",
    "FilesystemChangeFileCreated": ".filesystem_change_file_created",
    "FilesystemChangeMoved": ".filesystem_change_moved",
    "FilesystemChangeUndeleted": ".filesystem_change_undeleted",
    "FilesystemChange_AccessChanged": ".filesystem_change",
    "FilesystemChange_AttributesChanged": ".filesystem_change",
    "FilesystemChange_ContentChanged": ".filesystem_change",
    "FilesystemChange_Deleted": ".filesystem_change",
    "FilesystemChange_DirectoryCreated": ".filesystem_change",
    "FilesystemChange_FileCreated": ".filesystem_change",
    "FilesystemChange_Moved": ".filesystem_change",
    "FilesystemChange_Undeleted": ".filesystem_change",
    "FilesystemOperation": ".filesystem_operation",
    "FilesystemOperationAppendFile": ".filesystem_operation_append_file",
    "FilesystemOperationAppendFileByInode": ".filesystem_operation_append_file_by_inode",
    "FilesystemOperationCopyByInode": ".filesystem_operation_copy_by_inode",
    "FilesystemOperationCopyPath": ".filesystem_operation_copy_path",
    "FilesystemOperationCreateDirectory": ".filesystem_operation_create_directory",
    "FilesystemOperationCreateDirectoryByInode": ".filesystem_operation_create_directory_by_inode",
    "FilesystemOperationCreateFileByInode": ".filesystem_operation_create_file_by_inode",
    "FilesystemOperationDeleteByInode": ".filesystem_operation_delete_by_inode",
    "FilesystemOperationDeletePath": ".filesystem_operation_delete_path",
    "FilesystemOperationMoveByInode": ".filesystem_operation_move_by_inode",
    "FilesystemOperationMovePath": ".filesystem_operation_move_path",
    "FilesystemOperationPutFile": ".filesystem_operation_put_file",
    "FilesystemOperationPutFileRevisionByInode": ".filesystem_operation_put_file_revision_by_inode",
    "FilesystemOperationRestoreRevision": ".filesystem_operation_restore_revision",
    "FilesystemOperationRestoreRevisionByInode": ".filesystem_operation_restore_revision_by_inode",
    "FilesystemOperationUndelete": ".filesystem_operation_undelete",
    "FilesystemOperationUpdateAccess": ".filesystem_operation_update_access",
    "FilesystemOperationUpdateAccessByInode": ".filesystem_operation_update_access_by_inode",
    "FilesystemOperationUpdateAttributes": ".filesystem_operation_update_attributes",
    "FilesystemOperationUpdateAttributesByInode": ".filesystem_operation_update_attributes_by_inode",
    "FilesystemOperation_AppendFile": ".filesystem_operation",
    "FilesystemOperation_AppendFileByInode": ".filesystem_operation",
    "FilesystemOperation_CopyByInode": ".filesystem_operation",
    "FilesystemOperation_CopyPath": ".filesystem_operation",
    "FilesystemOperation_CreateDirectory": ".filesystem_operation",
    "FilesystemOperation_CreateDirectoryByInode": ".filesystem_operation",
    "FilesystemOperation_CreateFileByInode": ".filesystem_operation",
    "FilesystemOperation_DeleteByInode": ".filesystem_operation",
    "FilesystemOperation_DeletePath": ".filesystem_operation",
    "FilesystemOperation_MoveByInode": ".filesystem_operation",
    "FilesystemOperation_MovePath": ".filesystem_operation",
    "FilesystemOperation_PutFile": ".filesystem_operation",
    "FilesystemOperation_PutFileRevisionByInode": ".filesystem_operation",
    "FilesystemOperation_RestoreRevision": ".filesystem_operation",
    "FilesystemOperation_RestoreRevisionByInode": ".filesystem_operation",
    "FilesystemOperation_Undelete": ".filesystem_operation",
    "FilesystemOperation_UpdateAccess": ".filesystem_operation",
    "FilesystemOperation_UpdateAccessByInode": ".filesystem_operation",
    "FilesystemOperation_UpdateAttributes": ".filesystem_operation",
    "FilesystemOperation_UpdateAttributesByInode": ".filesystem_operation",
    "GrepGcReport": ".grep_gc_report",
    "GrepIndex": ".grep_index",
    "GrepIndexStatusActive": ".grep_index_status_active",
    "GrepIndexStatusBackfilling": ".grep_index_status_backfilling",
    "GrepIndexStatusDisabled": ".grep_index_status_disabled",
    "GrepIndex_Active": ".grep_index",
    "GrepIndex_Backfilling": ".grep_index",
    "GrepIndex_Disabled": ".grep_index",
    "GrepMatch": ".grep_match",
    "GrepResponse": ".grep_response",
    "InodeId": ".inode_id",
    "InodeKind": ".inode_kind",
    "ListChangesResponse": ".list_changes_response",
    "ListCheckpointsResponse": ".list_checkpoints_response",
    "ListFileRevisionsResponse": ".list_file_revisions_response",
    "ListInodeChildrenResponse": ".list_inode_children_response",
    "ListPathEntriesResponse": ".list_path_entries_response",
    "ListSnapshotsResponse": ".list_snapshots_response",
    "ListTrashResponse": ".list_trash_response",
    "ManifestNo": ".manifest_no",
    "MetadataMaintenanceOutcome": ".metadata_maintenance_outcome",
    "NameKey": ".name_key",
    "NamespaceAccess": ".namespace_access",
    "NamespaceAccessAcl": ".namespace_access_acl",
    "NamespaceAccessMode": ".namespace_access_mode",
    "NamespaceAccessModeAcl": ".namespace_access_mode_acl",
    "NamespaceAccessModeUnrestricted": ".namespace_access_mode_unrestricted",
    "NamespaceAccessMode_Acl": ".namespace_access_mode",
    "NamespaceAccessMode_Unrestricted": ".namespace_access_mode",
    "NamespaceAccessUnrestricted": ".namespace_access_unrestricted",
    "NamespaceAccess_Acl": ".namespace_access",
    "NamespaceAccess_Unrestricted": ".namespace_access",
    "NamespaceDiagnostics": ".namespace_diagnostics",
    "NamespaceForkBasis": ".namespace_fork_basis",
    "NamespaceId": ".namespace_id",
    "NamespaceMetadata": ".namespace_metadata",
    "ObjectTransferAccess": ".object_transfer_access",
    "ObjectTransferAccessPresignedUrl": ".object_transfer_access_presigned_url",
    "ObjectTransferAccess_PresignedUrl": ".object_transfer_access",
    "PathEntry": ".path_entry",
    "PathEntryDirectory": ".path_entry_directory",
    "PathEntryFile": ".path_entry_file",
    "PathEntry_Dir": ".path_entry",
    "PathEntry_File": ".path_entry",
    "PinId": ".pin_id",
    "PrincipalId": ".principal_id",
    "PrincipalScope": ".principal_scope",
    "ProbeRunId": ".probe_run_id",
    "ReadConsistency": ".read_consistency",
    "RetainedCandidates": ".retained_candidates",
    "RevisionNo": ".revision_no",
    "RunMaintenanceRequest": ".run_maintenance_request",
    "RunMaintenanceRequestGc": ".run_maintenance_request_gc",
    "RunMaintenanceRequestMetadata": ".run_maintenance_request_metadata",
    "RunMaintenanceRequestRecoverAdministrator": ".run_maintenance_request_recover_administrator",
    "RunMaintenanceRequestRetention": ".run_maintenance_request_retention",
    "RunMaintenanceRequestRetentionWindow": ".run_maintenance_request_retention_window",
    "RunMaintenanceRequest_Gc": ".run_maintenance_request",
    "RunMaintenanceRequest_Metadata": ".run_maintenance_request",
    "RunMaintenanceRequest_RecoverAdministrator": ".run_maintenance_request",
    "RunMaintenanceRequest_Retention": ".run_maintenance_request",
    "RunMaintenanceRequest_RetentionWindow": ".run_maintenance_request",
    "RunMaintenanceResponse": ".run_maintenance_response",
    "RunMaintenanceResponseGc": ".run_maintenance_response_gc",
    "RunMaintenanceResponseMetadata": ".run_maintenance_response_metadata",
    "RunMaintenanceResponseRecoverAdministrator": ".run_maintenance_response_recover_administrator",
    "RunMaintenanceResponseRetention": ".run_maintenance_response_retention",
    "RunMaintenanceResponseRetentionWindow": ".run_maintenance_response_retention_window",
    "RunMaintenanceResponse_Gc": ".run_maintenance_response",
    "RunMaintenanceResponse_Metadata": ".run_maintenance_response",
    "RunMaintenanceResponse_RecoverAdministrator": ".run_maintenance_response",
    "RunMaintenanceResponse_Retention": ".run_maintenance_response",
    "RunMaintenanceResponse_RetentionWindow": ".run_maintenance_response",
    "RunNo": ".run_no",
    "ServiceUnavailableErrorBody": ".service_unavailable_error_body",
    "SignUploadPartsResponse": ".sign_upload_parts_response",
    "SignedUploadPart": ".signed_upload_part",
    "Snapshot": ".snapshot",
    "StoreProbeCheck": ".store_probe_check",
    "StoreProbeCheckFailed": ".store_probe_check_failed",
    "StoreProbeCheckPassed": ".store_probe_check_passed",
    "StoreProbeCheckUnsupported": ".store_probe_check_unsupported",
    "StoreProbeCheck_Failed": ".store_probe_check",
    "StoreProbeCheck_Passed": ".store_probe_check",
    "StoreProbeCheck_Unsupported": ".store_probe_check",
    "StoreProbeRequest": ".store_probe_request",
    "StoreProbeResponse": ".store_probe_response",
    "TrashEntry": ".trash_entry",
    "UploadContentClaim": ".upload_content_claim",
    "UploadId": ".upload_id",
    "UploadMode": ".upload_mode",
    "UploadPartChecksumClaim": ".upload_part_checksum_claim",
    "UploadSession": ".upload_session",
    "UploadSessionStatusAborted": ".upload_session_status_aborted",
    "UploadSessionStatusCompleted": ".upload_session_status_completed",
    "UploadSessionStatusOpen": ".upload_session_status_open",
    "UploadSession_Aborted": ".upload_session",
    "UploadSession_Completed": ".upload_session",
    "UploadSession_Open": ".upload_session",
    "WriterEpoch": ".writer_epoch",
    "WriterId": ".writer_id",
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
    "AbsolutePath",
    "AccessGrants",
    "AccessRevisionNo",
    "AccessRight",
    "AccessRights",
    "ActorId",
    "AttributeKey",
    "AttributeValue",
    "Attributes",
    "AttributesRevisionNo",
    "BindingVersion",
    "CapabilityDocument",
    "ChangeSeq",
    "Checkpoint",
    "CheckpointOwner",
    "CheckpointOwnerFork",
    "CheckpointOwnerUser",
    "CheckpointOwner_Fork",
    "CheckpointOwner_User",
    "Checksum",
    "ChecksumAlgorithm",
    "Commit",
    "CommitId",
    "CommitPrecondition",
    "CommitPreconditionAccessRevision",
    "CommitPreconditionAttributesRevision",
    "CommitPreconditionFileRevision",
    "CommitPreconditionInodeBinding",
    "CommitPreconditionNameAbsence",
    "CommitPreconditionNamespaceHead",
    "CommitPreconditionPathAbsence",
    "CommitPreconditionPathBinding",
    "CommitPrecondition_AccessRevision",
    "CommitPrecondition_AttributesRevision",
    "CommitPrecondition_FileRevision",
    "CommitPrecondition_InodeBinding",
    "CommitPrecondition_NameAbsence",
    "CommitPrecondition_NamespaceHead",
    "CommitPrecondition_PathAbsence",
    "CommitPrecondition_PathBinding",
    "CompleteUploadBody",
    "CompleteUploadBodyDirectMultipart",
    "CompleteUploadBodyDirectPut",
    "CompleteUploadBodyServiceProxied",
    "CompleteUploadBody_DirectMultipart",
    "CompleteUploadBody_DirectPut",
    "CompleteUploadBody_ServiceProxied",
    "CompletedUploadPart",
    "ContentId",
    "ContentRef",
    "ContentRefKind",
    "ContentToken",
    "CreateDownloadByInodeResponse",
    "CreateDownloadResponse",
    "CreateUploadBody",
    "CreateUploadBodyDirectMultipart",
    "CreateUploadBodyDirectPut",
    "CreateUploadBodyServiceProxied",
    "CreateUploadBody_DirectMultipart",
    "CreateUploadBody_DirectPut",
    "CreateUploadBody_ServiceProxied",
    "DeleteDirectoryBehavior",
    "DeleteNamespaceResponse",
    "DeleteSnapshotResponse",
    "DeletedCheckpointsByOwner",
    "DeletedObjectCounts",
    "DestinationBehavior",
    "DirectoryBinding",
    "DisplayName",
    "DownloadRange",
    "ErrorDetails",
    "ErrorResponse",
    "ExtensionGcReports",
    "FileRevision",
    "FilesystemChange",
    "FilesystemChangeAccessChanged",
    "FilesystemChangeAttributesChanged",
    "FilesystemChangeContentChanged",
    "FilesystemChangeDeleted",
    "FilesystemChangeDirectoryCreated",
    "FilesystemChangeFileCreated",
    "FilesystemChangeMoved",
    "FilesystemChangeUndeleted",
    "FilesystemChange_AccessChanged",
    "FilesystemChange_AttributesChanged",
    "FilesystemChange_ContentChanged",
    "FilesystemChange_Deleted",
    "FilesystemChange_DirectoryCreated",
    "FilesystemChange_FileCreated",
    "FilesystemChange_Moved",
    "FilesystemChange_Undeleted",
    "FilesystemOperation",
    "FilesystemOperationAppendFile",
    "FilesystemOperationAppendFileByInode",
    "FilesystemOperationCopyByInode",
    "FilesystemOperationCopyPath",
    "FilesystemOperationCreateDirectory",
    "FilesystemOperationCreateDirectoryByInode",
    "FilesystemOperationCreateFileByInode",
    "FilesystemOperationDeleteByInode",
    "FilesystemOperationDeletePath",
    "FilesystemOperationMoveByInode",
    "FilesystemOperationMovePath",
    "FilesystemOperationPutFile",
    "FilesystemOperationPutFileRevisionByInode",
    "FilesystemOperationRestoreRevision",
    "FilesystemOperationRestoreRevisionByInode",
    "FilesystemOperationUndelete",
    "FilesystemOperationUpdateAccess",
    "FilesystemOperationUpdateAccessByInode",
    "FilesystemOperationUpdateAttributes",
    "FilesystemOperationUpdateAttributesByInode",
    "FilesystemOperation_AppendFile",
    "FilesystemOperation_AppendFileByInode",
    "FilesystemOperation_CopyByInode",
    "FilesystemOperation_CopyPath",
    "FilesystemOperation_CreateDirectory",
    "FilesystemOperation_CreateDirectoryByInode",
    "FilesystemOperation_CreateFileByInode",
    "FilesystemOperation_DeleteByInode",
    "FilesystemOperation_DeletePath",
    "FilesystemOperation_MoveByInode",
    "FilesystemOperation_MovePath",
    "FilesystemOperation_PutFile",
    "FilesystemOperation_PutFileRevisionByInode",
    "FilesystemOperation_RestoreRevision",
    "FilesystemOperation_RestoreRevisionByInode",
    "FilesystemOperation_Undelete",
    "FilesystemOperation_UpdateAccess",
    "FilesystemOperation_UpdateAccessByInode",
    "FilesystemOperation_UpdateAttributes",
    "FilesystemOperation_UpdateAttributesByInode",
    "GrepGcReport",
    "GrepIndex",
    "GrepIndexStatusActive",
    "GrepIndexStatusBackfilling",
    "GrepIndexStatusDisabled",
    "GrepIndex_Active",
    "GrepIndex_Backfilling",
    "GrepIndex_Disabled",
    "GrepMatch",
    "GrepResponse",
    "InodeId",
    "InodeKind",
    "ListChangesResponse",
    "ListCheckpointsResponse",
    "ListFileRevisionsResponse",
    "ListInodeChildrenResponse",
    "ListPathEntriesResponse",
    "ListSnapshotsResponse",
    "ListTrashResponse",
    "ManifestNo",
    "MetadataMaintenanceOutcome",
    "NameKey",
    "NamespaceAccess",
    "NamespaceAccessAcl",
    "NamespaceAccessMode",
    "NamespaceAccessModeAcl",
    "NamespaceAccessModeUnrestricted",
    "NamespaceAccessMode_Acl",
    "NamespaceAccessMode_Unrestricted",
    "NamespaceAccessUnrestricted",
    "NamespaceAccess_Acl",
    "NamespaceAccess_Unrestricted",
    "NamespaceDiagnostics",
    "NamespaceForkBasis",
    "NamespaceId",
    "NamespaceMetadata",
    "ObjectTransferAccess",
    "ObjectTransferAccessPresignedUrl",
    "ObjectTransferAccess_PresignedUrl",
    "PathEntry",
    "PathEntryDirectory",
    "PathEntryFile",
    "PathEntry_Dir",
    "PathEntry_File",
    "PinId",
    "PrincipalId",
    "PrincipalScope",
    "ProbeRunId",
    "ReadConsistency",
    "RetainedCandidates",
    "RevisionNo",
    "RunMaintenanceRequest",
    "RunMaintenanceRequestGc",
    "RunMaintenanceRequestMetadata",
    "RunMaintenanceRequestRecoverAdministrator",
    "RunMaintenanceRequestRetention",
    "RunMaintenanceRequestRetentionWindow",
    "RunMaintenanceRequest_Gc",
    "RunMaintenanceRequest_Metadata",
    "RunMaintenanceRequest_RecoverAdministrator",
    "RunMaintenanceRequest_Retention",
    "RunMaintenanceRequest_RetentionWindow",
    "RunMaintenanceResponse",
    "RunMaintenanceResponseGc",
    "RunMaintenanceResponseMetadata",
    "RunMaintenanceResponseRecoverAdministrator",
    "RunMaintenanceResponseRetention",
    "RunMaintenanceResponseRetentionWindow",
    "RunMaintenanceResponse_Gc",
    "RunMaintenanceResponse_Metadata",
    "RunMaintenanceResponse_RecoverAdministrator",
    "RunMaintenanceResponse_Retention",
    "RunMaintenanceResponse_RetentionWindow",
    "RunNo",
    "ServiceUnavailableErrorBody",
    "SignUploadPartsResponse",
    "SignedUploadPart",
    "Snapshot",
    "StoreProbeCheck",
    "StoreProbeCheckFailed",
    "StoreProbeCheckPassed",
    "StoreProbeCheckUnsupported",
    "StoreProbeCheck_Failed",
    "StoreProbeCheck_Passed",
    "StoreProbeCheck_Unsupported",
    "StoreProbeRequest",
    "StoreProbeResponse",
    "TrashEntry",
    "UploadContentClaim",
    "UploadId",
    "UploadMode",
    "UploadPartChecksumClaim",
    "UploadSession",
    "UploadSessionStatusAborted",
    "UploadSessionStatusCompleted",
    "UploadSessionStatusOpen",
    "UploadSession_Aborted",
    "UploadSession_Completed",
    "UploadSession_Open",
    "WriterEpoch",
    "WriterId",
]
