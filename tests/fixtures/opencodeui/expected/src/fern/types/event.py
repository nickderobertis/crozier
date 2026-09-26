

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_command_executed_properties import EventCommandExecutedProperties
from .event_file_edited_properties import EventFileEditedProperties
from .event_file_watcher_updated_properties import EventFileWatcherUpdatedProperties
from .event_global_disposed_properties import EventGlobalDisposedProperties
from .event_installation_update_available_properties import EventInstallationUpdateAvailableProperties
from .event_installation_updated_properties import EventInstallationUpdatedProperties
from .event_lsp_client_diagnostics_properties import EventLspClientDiagnosticsProperties
from .event_lsp_updated_properties import EventLspUpdatedProperties
from .event_mcp_browser_open_failed_properties import EventMcpBrowserOpenFailedProperties
from .event_mcp_tools_changed_properties import EventMcpToolsChangedProperties
from .event_message_part_removed_properties import EventMessagePartRemovedProperties
from .event_message_part_updated_properties import EventMessagePartUpdatedProperties
from .event_message_removed_properties import EventMessageRemovedProperties
from .event_message_updated_properties import EventMessageUpdatedProperties
from .event_permission_replied_properties import EventPermissionRepliedProperties
from .event_pty_created_properties import EventPtyCreatedProperties
from .event_pty_deleted_properties import EventPtyDeletedProperties
from .event_pty_exited_properties import EventPtyExitedProperties
from .event_pty_updated_properties import EventPtyUpdatedProperties
from .event_question_rejected_properties import EventQuestionRejectedProperties
from .event_question_replied_properties import EventQuestionRepliedProperties
from .event_server_connected_properties import EventServerConnectedProperties
from .event_server_instance_disposed_properties import EventServerInstanceDisposedProperties
from .event_session_compacted_properties import EventSessionCompactedProperties
from .event_session_created_properties import EventSessionCreatedProperties
from .event_session_deleted_properties import EventSessionDeletedProperties
from .event_session_diff_properties import EventSessionDiffProperties
from .event_session_error_properties import EventSessionErrorProperties
from .event_session_idle_properties import EventSessionIdleProperties
from .event_session_status_properties import EventSessionStatusProperties
from .event_session_updated_properties import EventSessionUpdatedProperties
from .event_todo_updated_properties import EventTodoUpdatedProperties
from .event_tui_command_execute_properties import EventTuiCommandExecuteProperties
from .event_tui_prompt_append_properties import EventTuiPromptAppendProperties
from .event_tui_session_select_properties import EventTuiSessionSelectProperties
from .event_tui_toast_show_properties import EventTuiToastShowProperties
from .event_vcs_branch_updated_properties import EventVcsBranchUpdatedProperties
from .event_worktree_failed_properties import EventWorktreeFailedProperties
from .event_worktree_ready_properties import EventWorktreeReadyProperties
from .permission_request import PermissionRequest
from .project import Project
from .question_request import QuestionRequest


class Event_ServerConnected(UniversalBaseModel):
    type: typing.Literal["server.connected"] = "server.connected"
    properties: EventServerConnectedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_GlobalDisposed(UniversalBaseModel):
    type: typing.Literal["global.disposed"] = "global.disposed"
    properties: EventGlobalDisposedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_TuiPromptAppend(UniversalBaseModel):
    type: typing.Literal["tui.prompt.append"] = "tui.prompt.append"
    properties: EventTuiPromptAppendProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_TuiCommandExecute(UniversalBaseModel):
    type: typing.Literal["tui.command.execute"] = "tui.command.execute"
    properties: EventTuiCommandExecuteProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_TuiToastShow(UniversalBaseModel):
    type: typing.Literal["tui.toast.show"] = "tui.toast.show"
    properties: EventTuiToastShowProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_TuiSessionSelect(UniversalBaseModel):
    type: typing.Literal["tui.session.select"] = "tui.session.select"
    properties: EventTuiSessionSelectProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_InstallationUpdated(UniversalBaseModel):
    type: typing.Literal["installation.updated"] = "installation.updated"
    properties: EventInstallationUpdatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_InstallationUpdateAvailable(UniversalBaseModel):
    type: typing.Literal["installation.update-available"] = "installation.update-available"
    properties: EventInstallationUpdateAvailableProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_ProjectUpdated(UniversalBaseModel):
    type: typing.Literal["project.updated"] = "project.updated"
    properties: Project

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_ServerInstanceDisposed(UniversalBaseModel):
    type: typing.Literal["server.instance.disposed"] = "server.instance.disposed"
    properties: EventServerInstanceDisposedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_FileEdited(UniversalBaseModel):
    type: typing.Literal["file.edited"] = "file.edited"
    properties: EventFileEditedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_WorktreeReady(UniversalBaseModel):
    type: typing.Literal["worktree.ready"] = "worktree.ready"
    properties: EventWorktreeReadyProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_WorktreeFailed(UniversalBaseModel):
    type: typing.Literal["worktree.failed"] = "worktree.failed"
    properties: EventWorktreeFailedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_LspClientDiagnostics(UniversalBaseModel):
    type: typing.Literal["lsp.client.diagnostics"] = "lsp.client.diagnostics"
    properties: EventLspClientDiagnosticsProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_PermissionAsked(UniversalBaseModel):
    type: typing.Literal["permission.asked"] = "permission.asked"
    properties: PermissionRequest

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_PermissionReplied(UniversalBaseModel):
    type: typing.Literal["permission.replied"] = "permission.replied"
    properties: EventPermissionRepliedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_SessionStatus(UniversalBaseModel):
    type: typing.Literal["session.status"] = "session.status"
    properties: EventSessionStatusProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_SessionIdle(UniversalBaseModel):
    type: typing.Literal["session.idle"] = "session.idle"
    properties: EventSessionIdleProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_QuestionAsked(UniversalBaseModel):
    type: typing.Literal["question.asked"] = "question.asked"
    properties: QuestionRequest

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_QuestionReplied(UniversalBaseModel):
    type: typing.Literal["question.replied"] = "question.replied"
    properties: EventQuestionRepliedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_QuestionRejected(UniversalBaseModel):
    type: typing.Literal["question.rejected"] = "question.rejected"
    properties: EventQuestionRejectedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_TodoUpdated(UniversalBaseModel):
    type: typing.Literal["todo.updated"] = "todo.updated"
    properties: EventTodoUpdatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_PtyCreated(UniversalBaseModel):
    type: typing.Literal["pty.created"] = "pty.created"
    properties: EventPtyCreatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_PtyUpdated(UniversalBaseModel):
    type: typing.Literal["pty.updated"] = "pty.updated"
    properties: EventPtyUpdatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_PtyExited(UniversalBaseModel):
    type: typing.Literal["pty.exited"] = "pty.exited"
    properties: EventPtyExitedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_PtyDeleted(UniversalBaseModel):
    type: typing.Literal["pty.deleted"] = "pty.deleted"
    properties: EventPtyDeletedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_FileWatcherUpdated(UniversalBaseModel):
    type: typing.Literal["file.watcher.updated"] = "file.watcher.updated"
    properties: EventFileWatcherUpdatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_McpToolsChanged(UniversalBaseModel):
    type: typing.Literal["mcp.tools.changed"] = "mcp.tools.changed"
    properties: EventMcpToolsChangedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_McpBrowserOpenFailed(UniversalBaseModel):
    type: typing.Literal["mcp.browser.open.failed"] = "mcp.browser.open.failed"
    properties: EventMcpBrowserOpenFailedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_LspUpdated(UniversalBaseModel):
    type: typing.Literal["lsp.updated"] = "lsp.updated"
    properties: EventLspUpdatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_VcsBranchUpdated(UniversalBaseModel):
    type: typing.Literal["vcs.branch.updated"] = "vcs.branch.updated"
    properties: EventVcsBranchUpdatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_CommandExecuted(UniversalBaseModel):
    type: typing.Literal["command.executed"] = "command.executed"
    properties: EventCommandExecutedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_MessageUpdated(UniversalBaseModel):
    type: typing.Literal["message.updated"] = "message.updated"
    properties: EventMessageUpdatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_MessageRemoved(UniversalBaseModel):
    type: typing.Literal["message.removed"] = "message.removed"
    properties: EventMessageRemovedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_MessagePartUpdated(UniversalBaseModel):
    type: typing.Literal["message.part.updated"] = "message.part.updated"
    properties: EventMessagePartUpdatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_MessagePartRemoved(UniversalBaseModel):
    type: typing.Literal["message.part.removed"] = "message.part.removed"
    properties: EventMessagePartRemovedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_SessionCompacted(UniversalBaseModel):
    type: typing.Literal["session.compacted"] = "session.compacted"
    properties: EventSessionCompactedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_SessionCreated(UniversalBaseModel):
    type: typing.Literal["session.created"] = "session.created"
    properties: EventSessionCreatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_SessionUpdated(UniversalBaseModel):
    type: typing.Literal["session.updated"] = "session.updated"
    properties: EventSessionUpdatedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_SessionDeleted(UniversalBaseModel):
    type: typing.Literal["session.deleted"] = "session.deleted"
    properties: EventSessionDeletedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_SessionDiff(UniversalBaseModel):
    type: typing.Literal["session.diff"] = "session.diff"
    properties: EventSessionDiffProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Event_SessionError(UniversalBaseModel):
    type: typing.Literal["session.error"] = "session.error"
    properties: EventSessionErrorProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Event = typing_extensions.Annotated[
    typing.Union[
        Event_ServerConnected,
        Event_GlobalDisposed,
        Event_TuiPromptAppend,
        Event_TuiCommandExecute,
        Event_TuiToastShow,
        Event_TuiSessionSelect,
        Event_InstallationUpdated,
        Event_InstallationUpdateAvailable,
        Event_ProjectUpdated,
        Event_ServerInstanceDisposed,
        Event_FileEdited,
        Event_WorktreeReady,
        Event_WorktreeFailed,
        Event_LspClientDiagnostics,
        Event_PermissionAsked,
        Event_PermissionReplied,
        Event_SessionStatus,
        Event_SessionIdle,
        Event_QuestionAsked,
        Event_QuestionReplied,
        Event_QuestionRejected,
        Event_TodoUpdated,
        Event_PtyCreated,
        Event_PtyUpdated,
        Event_PtyExited,
        Event_PtyDeleted,
        Event_FileWatcherUpdated,
        Event_McpToolsChanged,
        Event_McpBrowserOpenFailed,
        Event_LspUpdated,
        Event_VcsBranchUpdated,
        Event_CommandExecuted,
        Event_MessageUpdated,
        Event_MessageRemoved,
        Event_MessagePartUpdated,
        Event_MessagePartRemoved,
        Event_SessionCompacted,
        Event_SessionCreated,
        Event_SessionUpdated,
        Event_SessionDeleted,
        Event_SessionDiff,
        Event_SessionError,
    ],
    pydantic.Field(discriminator="type"),
]
