



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .a_folder import AFolder, AFolder_Delete, AFolder_Move, AFolder_Rename
    from .a_folder_delete import AFolderDelete
    from .a_folder_move import AFolderMove
    from .a_folder_rename import AFolderRename
    from .a_note import (
        ANote,
        ANote_Delete,
        ANote_Move,
        ANote_Publish,
        ANote_Rename,
        ANote_Restore,
        ANote_Unpublish,
        ANote_Update,
    )
    from .a_note_delete import ANoteDelete
    from .a_note_move import ANoteMove
    from .a_note_publish import ANotePublish
    from .a_note_rename import ANoteRename
    from .a_note_restore import ANoteRestore
    from .a_note_unpublish import ANoteUnpublish
    from .a_note_update import ANoteUpdate
    from .a_notebook import (
        ANotebook,
        ANotebook_BatchImport,
        ANotebook_BatchImportTree,
        ANotebook_CreateFolder,
        ANotebook_CreateNote,
        ANotebook_Delete,
        ANotebook_Folder,
        ANotebook_Invite,
        ANotebook_Note,
        ANotebook_Rename,
        ANotebook_Visibility,
    )
    from .action import (
        Action,
        Action_AcceptInvite,
        Action_ClearApiKey,
        Action_CreateNotebook,
        Action_DeclineInvite,
        Action_Join,
        Action_Leave,
        Action_Notebook,
        Action_RegenerateApiKey,
    )
    from .action_accept_invite import ActionAcceptInvite
    from .action_clear_api_key import ActionClearApiKey
    from .action_create_notebook import ActionCreateNotebook
    from .action_decline_invite import ActionDeclineInvite
    from .action_error import ActionError
    from .action_join import ActionJoin
    from .action_leave import ActionLeave
    from .action_notebook_envelope import ActionNotebookEnvelope
    from .action_regenerate_api_key import ActionRegenerateApiKey
    from .flag import Flag
    from .folder import Folder
    from .import_node import ImportNode
    from .import_node_body import ImportNodeBody
    from .import_node_children import ImportNodeChildren
    from .invite_record import InviteRecord
    from .member_record import MemberRecord
    from .member_record_role import MemberRecordRole
    from .nb_batch_import import NbBatchImport
    from .nb_batch_import_notes_item import NbBatchImportNotesItem
    from .nb_batch_import_tree import NbBatchImportTree
    from .nb_create_folder import NbCreateFolder
    from .nb_create_note import NbCreateNote
    from .nb_delete import NbDelete
    from .nb_folder_envelope import NbFolderEnvelope
    from .nb_invite import NbInvite
    from .nb_note_envelope import NbNoteEnvelope
    from .nb_rename import NbRename
    from .nb_visibility import NbVisibility
    from .nb_visibility_visibility import NbVisibilityVisibility
    from .note import Note
    from .note_revision import NoteRevision
    from .notebook import Notebook
    from .notebook_summary import NotebookSummary
    from .notebook_summary_visibility import NotebookSummaryVisibility
    from .poke_status import PokeStatus
    from .r_notes import RNotes, RNotes_Snapshot, RNotes_Update
    from .r_snapshot import RSnapshot
    from .r_snapshot_visibility import RSnapshotVisibility
    from .r_update import RUpdate
    from .request_id import RequestId
    from .response import Response
    from .response_api_key import ResponseApiKey
    from .response_body import (
        ResponseBody,
        ResponseBody_ApiKey,
        ResponseBody_Error,
        ResponseBody_NoChange,
        ResponseBody_Notebook,
        ResponseBody_Ok,
        ResponseBody_Pending,
    )
    from .response_error import ResponseError
    from .response_no_change import ResponseNoChange
    from .response_notebook import ResponseNotebook
    from .response_ok import ResponseOk
    from .response_pending import ResponsePending
    from .ship_ref import ShipRef
    from .u_folder import UFolder, UFolder_FolderCreated, UFolder_FolderDeleted, UFolder_FolderUpdated
    from .u_folder_folder_created import UFolderFolderCreated
    from .u_folder_folder_deleted import UFolderFolderDeleted
    from .u_folder_folder_updated import UFolderFolderUpdated
    from .u_folder_update import UFolderUpdate
    from .u_invite_received import UInviteReceived
    from .u_invite_removed import UInviteRemoved
    from .u_member_joined import UMemberJoined
    from .u_member_joined_role import UMemberJoinedRole
    from .u_member_left import UMemberLeft
    from .u_nb_created import UNbCreated
    from .u_nb_created_visibility import UNbCreatedVisibility
    from .u_nb_deleted import UNbDeleted
    from .u_nb_updated import UNbUpdated
    from .u_nb_visibility_changed import UNbVisibilityChanged
    from .u_nb_visibility_changed_visibility import UNbVisibilityChangedVisibility
    from .u_note import (
        UNote,
        UNote_NoteCreated,
        UNote_NoteDeleted,
        UNote_NoteHistoryArchived,
        UNote_NotePublished,
        UNote_NoteUnpublished,
        UNote_NoteUpdated,
    )
    from .u_note_note_created import UNoteNoteCreated
    from .u_note_note_deleted import UNoteNoteDeleted
    from .u_note_note_history_archived import UNoteNoteHistoryArchived
    from .u_note_note_published import UNoteNotePublished
    from .u_note_note_unpublished import UNoteNoteUnpublished
    from .u_note_note_updated import UNoteNoteUpdated
    from .u_note_update import UNoteUpdate
    from .u_notebook import (
        UNotebook,
        UNotebook_FolderUpdate,
        UNotebook_InviteReceived,
        UNotebook_InviteRemoved,
        UNotebook_MemberJoined,
        UNotebook_MemberLeft,
        UNotebook_NoteUpdate,
        UNotebook_NotebookCreated,
        UNotebook_NotebookDeleted,
        UNotebook_NotebookUpdated,
        UNotebook_NotebookVisibilityChanged,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AFolder": ".a_folder",
    "AFolderDelete": ".a_folder_delete",
    "AFolderMove": ".a_folder_move",
    "AFolderRename": ".a_folder_rename",
    "AFolder_Delete": ".a_folder",
    "AFolder_Move": ".a_folder",
    "AFolder_Rename": ".a_folder",
    "ANote": ".a_note",
    "ANoteDelete": ".a_note_delete",
    "ANoteMove": ".a_note_move",
    "ANotePublish": ".a_note_publish",
    "ANoteRename": ".a_note_rename",
    "ANoteRestore": ".a_note_restore",
    "ANoteUnpublish": ".a_note_unpublish",
    "ANoteUpdate": ".a_note_update",
    "ANote_Delete": ".a_note",
    "ANote_Move": ".a_note",
    "ANote_Publish": ".a_note",
    "ANote_Rename": ".a_note",
    "ANote_Restore": ".a_note",
    "ANote_Unpublish": ".a_note",
    "ANote_Update": ".a_note",
    "ANotebook": ".a_notebook",
    "ANotebook_BatchImport": ".a_notebook",
    "ANotebook_BatchImportTree": ".a_notebook",
    "ANotebook_CreateFolder": ".a_notebook",
    "ANotebook_CreateNote": ".a_notebook",
    "ANotebook_Delete": ".a_notebook",
    "ANotebook_Folder": ".a_notebook",
    "ANotebook_Invite": ".a_notebook",
    "ANotebook_Note": ".a_notebook",
    "ANotebook_Rename": ".a_notebook",
    "ANotebook_Visibility": ".a_notebook",
    "Action": ".action",
    "ActionAcceptInvite": ".action_accept_invite",
    "ActionClearApiKey": ".action_clear_api_key",
    "ActionCreateNotebook": ".action_create_notebook",
    "ActionDeclineInvite": ".action_decline_invite",
    "ActionError": ".action_error",
    "ActionJoin": ".action_join",
    "ActionLeave": ".action_leave",
    "ActionNotebookEnvelope": ".action_notebook_envelope",
    "ActionRegenerateApiKey": ".action_regenerate_api_key",
    "Action_AcceptInvite": ".action",
    "Action_ClearApiKey": ".action",
    "Action_CreateNotebook": ".action",
    "Action_DeclineInvite": ".action",
    "Action_Join": ".action",
    "Action_Leave": ".action",
    "Action_Notebook": ".action",
    "Action_RegenerateApiKey": ".action",
    "Flag": ".flag",
    "Folder": ".folder",
    "ImportNode": ".import_node",
    "ImportNodeBody": ".import_node_body",
    "ImportNodeChildren": ".import_node_children",
    "InviteRecord": ".invite_record",
    "MemberRecord": ".member_record",
    "MemberRecordRole": ".member_record_role",
    "NbBatchImport": ".nb_batch_import",
    "NbBatchImportNotesItem": ".nb_batch_import_notes_item",
    "NbBatchImportTree": ".nb_batch_import_tree",
    "NbCreateFolder": ".nb_create_folder",
    "NbCreateNote": ".nb_create_note",
    "NbDelete": ".nb_delete",
    "NbFolderEnvelope": ".nb_folder_envelope",
    "NbInvite": ".nb_invite",
    "NbNoteEnvelope": ".nb_note_envelope",
    "NbRename": ".nb_rename",
    "NbVisibility": ".nb_visibility",
    "NbVisibilityVisibility": ".nb_visibility_visibility",
    "Note": ".note",
    "NoteRevision": ".note_revision",
    "Notebook": ".notebook",
    "NotebookSummary": ".notebook_summary",
    "NotebookSummaryVisibility": ".notebook_summary_visibility",
    "PokeStatus": ".poke_status",
    "RNotes": ".r_notes",
    "RNotes_Snapshot": ".r_notes",
    "RNotes_Update": ".r_notes",
    "RSnapshot": ".r_snapshot",
    "RSnapshotVisibility": ".r_snapshot_visibility",
    "RUpdate": ".r_update",
    "RequestId": ".request_id",
    "Response": ".response",
    "ResponseApiKey": ".response_api_key",
    "ResponseBody": ".response_body",
    "ResponseBody_ApiKey": ".response_body",
    "ResponseBody_Error": ".response_body",
    "ResponseBody_NoChange": ".response_body",
    "ResponseBody_Notebook": ".response_body",
    "ResponseBody_Ok": ".response_body",
    "ResponseBody_Pending": ".response_body",
    "ResponseError": ".response_error",
    "ResponseNoChange": ".response_no_change",
    "ResponseNotebook": ".response_notebook",
    "ResponseOk": ".response_ok",
    "ResponsePending": ".response_pending",
    "ShipRef": ".ship_ref",
    "UFolder": ".u_folder",
    "UFolderFolderCreated": ".u_folder_folder_created",
    "UFolderFolderDeleted": ".u_folder_folder_deleted",
    "UFolderFolderUpdated": ".u_folder_folder_updated",
    "UFolderUpdate": ".u_folder_update",
    "UFolder_FolderCreated": ".u_folder",
    "UFolder_FolderDeleted": ".u_folder",
    "UFolder_FolderUpdated": ".u_folder",
    "UInviteReceived": ".u_invite_received",
    "UInviteRemoved": ".u_invite_removed",
    "UMemberJoined": ".u_member_joined",
    "UMemberJoinedRole": ".u_member_joined_role",
    "UMemberLeft": ".u_member_left",
    "UNbCreated": ".u_nb_created",
    "UNbCreatedVisibility": ".u_nb_created_visibility",
    "UNbDeleted": ".u_nb_deleted",
    "UNbUpdated": ".u_nb_updated",
    "UNbVisibilityChanged": ".u_nb_visibility_changed",
    "UNbVisibilityChangedVisibility": ".u_nb_visibility_changed_visibility",
    "UNote": ".u_note",
    "UNoteNoteCreated": ".u_note_note_created",
    "UNoteNoteDeleted": ".u_note_note_deleted",
    "UNoteNoteHistoryArchived": ".u_note_note_history_archived",
    "UNoteNotePublished": ".u_note_note_published",
    "UNoteNoteUnpublished": ".u_note_note_unpublished",
    "UNoteNoteUpdated": ".u_note_note_updated",
    "UNoteUpdate": ".u_note_update",
    "UNote_NoteCreated": ".u_note",
    "UNote_NoteDeleted": ".u_note",
    "UNote_NoteHistoryArchived": ".u_note",
    "UNote_NotePublished": ".u_note",
    "UNote_NoteUnpublished": ".u_note",
    "UNote_NoteUpdated": ".u_note",
    "UNotebook": ".u_notebook",
    "UNotebook_FolderUpdate": ".u_notebook",
    "UNotebook_InviteReceived": ".u_notebook",
    "UNotebook_InviteRemoved": ".u_notebook",
    "UNotebook_MemberJoined": ".u_notebook",
    "UNotebook_MemberLeft": ".u_notebook",
    "UNotebook_NoteUpdate": ".u_notebook",
    "UNotebook_NotebookCreated": ".u_notebook",
    "UNotebook_NotebookDeleted": ".u_notebook",
    "UNotebook_NotebookUpdated": ".u_notebook",
    "UNotebook_NotebookVisibilityChanged": ".u_notebook",
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
    "AFolder",
    "AFolderDelete",
    "AFolderMove",
    "AFolderRename",
    "AFolder_Delete",
    "AFolder_Move",
    "AFolder_Rename",
    "ANote",
    "ANoteDelete",
    "ANoteMove",
    "ANotePublish",
    "ANoteRename",
    "ANoteRestore",
    "ANoteUnpublish",
    "ANoteUpdate",
    "ANote_Delete",
    "ANote_Move",
    "ANote_Publish",
    "ANote_Rename",
    "ANote_Restore",
    "ANote_Unpublish",
    "ANote_Update",
    "ANotebook",
    "ANotebook_BatchImport",
    "ANotebook_BatchImportTree",
    "ANotebook_CreateFolder",
    "ANotebook_CreateNote",
    "ANotebook_Delete",
    "ANotebook_Folder",
    "ANotebook_Invite",
    "ANotebook_Note",
    "ANotebook_Rename",
    "ANotebook_Visibility",
    "Action",
    "ActionAcceptInvite",
    "ActionClearApiKey",
    "ActionCreateNotebook",
    "ActionDeclineInvite",
    "ActionError",
    "ActionJoin",
    "ActionLeave",
    "ActionNotebookEnvelope",
    "ActionRegenerateApiKey",
    "Action_AcceptInvite",
    "Action_ClearApiKey",
    "Action_CreateNotebook",
    "Action_DeclineInvite",
    "Action_Join",
    "Action_Leave",
    "Action_Notebook",
    "Action_RegenerateApiKey",
    "Flag",
    "Folder",
    "ImportNode",
    "ImportNodeBody",
    "ImportNodeChildren",
    "InviteRecord",
    "MemberRecord",
    "MemberRecordRole",
    "NbBatchImport",
    "NbBatchImportNotesItem",
    "NbBatchImportTree",
    "NbCreateFolder",
    "NbCreateNote",
    "NbDelete",
    "NbFolderEnvelope",
    "NbInvite",
    "NbNoteEnvelope",
    "NbRename",
    "NbVisibility",
    "NbVisibilityVisibility",
    "Note",
    "NoteRevision",
    "Notebook",
    "NotebookSummary",
    "NotebookSummaryVisibility",
    "PokeStatus",
    "RNotes",
    "RNotes_Snapshot",
    "RNotes_Update",
    "RSnapshot",
    "RSnapshotVisibility",
    "RUpdate",
    "RequestId",
    "Response",
    "ResponseApiKey",
    "ResponseBody",
    "ResponseBody_ApiKey",
    "ResponseBody_Error",
    "ResponseBody_NoChange",
    "ResponseBody_Notebook",
    "ResponseBody_Ok",
    "ResponseBody_Pending",
    "ResponseError",
    "ResponseNoChange",
    "ResponseNotebook",
    "ResponseOk",
    "ResponsePending",
    "ShipRef",
    "UFolder",
    "UFolderFolderCreated",
    "UFolderFolderDeleted",
    "UFolderFolderUpdated",
    "UFolderUpdate",
    "UFolder_FolderCreated",
    "UFolder_FolderDeleted",
    "UFolder_FolderUpdated",
    "UInviteReceived",
    "UInviteRemoved",
    "UMemberJoined",
    "UMemberJoinedRole",
    "UMemberLeft",
    "UNbCreated",
    "UNbCreatedVisibility",
    "UNbDeleted",
    "UNbUpdated",
    "UNbVisibilityChanged",
    "UNbVisibilityChangedVisibility",
    "UNote",
    "UNoteNoteCreated",
    "UNoteNoteDeleted",
    "UNoteNoteHistoryArchived",
    "UNoteNotePublished",
    "UNoteNoteUnpublished",
    "UNoteNoteUpdated",
    "UNoteUpdate",
    "UNote_NoteCreated",
    "UNote_NoteDeleted",
    "UNote_NoteHistoryArchived",
    "UNote_NotePublished",
    "UNote_NoteUnpublished",
    "UNote_NoteUpdated",
    "UNotebook",
    "UNotebook_FolderUpdate",
    "UNotebook_InviteReceived",
    "UNotebook_InviteRemoved",
    "UNotebook_MemberJoined",
    "UNotebook_MemberLeft",
    "UNotebook_NoteUpdate",
    "UNotebook_NotebookCreated",
    "UNotebook_NotebookDeleted",
    "UNotebook_NotebookUpdated",
    "UNotebook_NotebookVisibilityChanged",
]
