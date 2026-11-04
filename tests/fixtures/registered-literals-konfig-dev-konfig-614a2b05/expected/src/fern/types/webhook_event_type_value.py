

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookEventTypeValue(enum.StrEnum):
    ALL = "*"
    WORKFLOW_LAUNCHED = "workflow_launched"
    WORKFLOW_UPDATED = "workflow_updated"
    WORKFLOW_CANCELLED = "workflow_cancelled"
    WORKFLOW_COMPLETED = "workflow_completed"
    WORKFLOW_APPROVAL_STATUS_CHANGED = "workflow_approval_status_changed"
    WORKFLOW_ATTRIBUTE_UPDATED = "workflow_attribute_updated"
    WORKFLOW_COMMENT_ADDED = "workflow_comment_added"
    WORKFLOW_COMMENT_REMOVED = "workflow_comment_removed"
    WORKFLOW_COMMENT_UPDATED = "workflow_comment_updated"
    WORKFLOW_COMMENT_REACTION_ADDED = "workflow_comment_reaction_added"
    WORKFLOW_COMMENT_REACTION_REMOVED = "workflow_comment_reaction_removed"
    WORKFLOW_COUNTERPARTY_INVITE_SENT = "workflow_counterparty_invite_sent"
    WORKFLOW_COUNTERPARTY_INVITE_REVOKED = "workflow_counterparty_invite_revoked"
    WORKFLOW_DOCUMENTS_ADDED = "workflow_documents_added"
    WORKFLOW_DOCUMENTS_REMOVED = "workflow_documents_removed"
    WORKFLOW_DOCUMENTS_UPDATED = "workflow_documents_updated"
    WORKFLOW_DOCUMENTS_RENAMED = "workflow_documents_renamed"
    WORKFLOW_DOCUMENT_EDITED = "workflow_document_edited"
    WORKFLOW_CHANGED_TURN = "workflow_changed_turn"
    WORKFLOW_PAUSED = "workflow_paused"
    WORKFLOW_RESUMED = "workflow_resumed"
    WORKFLOW_SIGNATURE_PACKET_SENT = "workflow_signature_packet_sent"
    WORKFLOW_SIGNATURE_PACKET_UPLOADED = "workflow_signature_packet_uploaded"
    WORKFLOW_SIGNATURE_PACKET_CANCELLED = "workflow_signature_packet_cancelled"
    WORKFLOW_SIGNER_ADDED = "workflow_signer_added"
    WORKFLOW_SIGNER_REMOVED = "workflow_signer_removed"
    WORKFLOW_SIGNER_REASSIGNED = "workflow_signer_reassigned"
    WORKFLOW_STEP_UPDATED = "workflow_step_updated"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        workflow_launched: typing.Callable[[], T_Result],
        workflow_updated: typing.Callable[[], T_Result],
        workflow_cancelled: typing.Callable[[], T_Result],
        workflow_completed: typing.Callable[[], T_Result],
        workflow_approval_status_changed: typing.Callable[[], T_Result],
        workflow_attribute_updated: typing.Callable[[], T_Result],
        workflow_comment_added: typing.Callable[[], T_Result],
        workflow_comment_removed: typing.Callable[[], T_Result],
        workflow_comment_updated: typing.Callable[[], T_Result],
        workflow_comment_reaction_added: typing.Callable[[], T_Result],
        workflow_comment_reaction_removed: typing.Callable[[], T_Result],
        workflow_counterparty_invite_sent: typing.Callable[[], T_Result],
        workflow_counterparty_invite_revoked: typing.Callable[[], T_Result],
        workflow_documents_added: typing.Callable[[], T_Result],
        workflow_documents_removed: typing.Callable[[], T_Result],
        workflow_documents_updated: typing.Callable[[], T_Result],
        workflow_documents_renamed: typing.Callable[[], T_Result],
        workflow_document_edited: typing.Callable[[], T_Result],
        workflow_changed_turn: typing.Callable[[], T_Result],
        workflow_paused: typing.Callable[[], T_Result],
        workflow_resumed: typing.Callable[[], T_Result],
        workflow_signature_packet_sent: typing.Callable[[], T_Result],
        workflow_signature_packet_uploaded: typing.Callable[[], T_Result],
        workflow_signature_packet_cancelled: typing.Callable[[], T_Result],
        workflow_signer_added: typing.Callable[[], T_Result],
        workflow_signer_removed: typing.Callable[[], T_Result],
        workflow_signer_reassigned: typing.Callable[[], T_Result],
        workflow_step_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookEventTypeValue.ALL:
            return all_()
        if self is WebhookEventTypeValue.WORKFLOW_LAUNCHED:
            return workflow_launched()
        if self is WebhookEventTypeValue.WORKFLOW_UPDATED:
            return workflow_updated()
        if self is WebhookEventTypeValue.WORKFLOW_CANCELLED:
            return workflow_cancelled()
        if self is WebhookEventTypeValue.WORKFLOW_COMPLETED:
            return workflow_completed()
        if self is WebhookEventTypeValue.WORKFLOW_APPROVAL_STATUS_CHANGED:
            return workflow_approval_status_changed()
        if self is WebhookEventTypeValue.WORKFLOW_ATTRIBUTE_UPDATED:
            return workflow_attribute_updated()
        if self is WebhookEventTypeValue.WORKFLOW_COMMENT_ADDED:
            return workflow_comment_added()
        if self is WebhookEventTypeValue.WORKFLOW_COMMENT_REMOVED:
            return workflow_comment_removed()
        if self is WebhookEventTypeValue.WORKFLOW_COMMENT_UPDATED:
            return workflow_comment_updated()
        if self is WebhookEventTypeValue.WORKFLOW_COMMENT_REACTION_ADDED:
            return workflow_comment_reaction_added()
        if self is WebhookEventTypeValue.WORKFLOW_COMMENT_REACTION_REMOVED:
            return workflow_comment_reaction_removed()
        if self is WebhookEventTypeValue.WORKFLOW_COUNTERPARTY_INVITE_SENT:
            return workflow_counterparty_invite_sent()
        if self is WebhookEventTypeValue.WORKFLOW_COUNTERPARTY_INVITE_REVOKED:
            return workflow_counterparty_invite_revoked()
        if self is WebhookEventTypeValue.WORKFLOW_DOCUMENTS_ADDED:
            return workflow_documents_added()
        if self is WebhookEventTypeValue.WORKFLOW_DOCUMENTS_REMOVED:
            return workflow_documents_removed()
        if self is WebhookEventTypeValue.WORKFLOW_DOCUMENTS_UPDATED:
            return workflow_documents_updated()
        if self is WebhookEventTypeValue.WORKFLOW_DOCUMENTS_RENAMED:
            return workflow_documents_renamed()
        if self is WebhookEventTypeValue.WORKFLOW_DOCUMENT_EDITED:
            return workflow_document_edited()
        if self is WebhookEventTypeValue.WORKFLOW_CHANGED_TURN:
            return workflow_changed_turn()
        if self is WebhookEventTypeValue.WORKFLOW_PAUSED:
            return workflow_paused()
        if self is WebhookEventTypeValue.WORKFLOW_RESUMED:
            return workflow_resumed()
        if self is WebhookEventTypeValue.WORKFLOW_SIGNATURE_PACKET_SENT:
            return workflow_signature_packet_sent()
        if self is WebhookEventTypeValue.WORKFLOW_SIGNATURE_PACKET_UPLOADED:
            return workflow_signature_packet_uploaded()
        if self is WebhookEventTypeValue.WORKFLOW_SIGNATURE_PACKET_CANCELLED:
            return workflow_signature_packet_cancelled()
        if self is WebhookEventTypeValue.WORKFLOW_SIGNER_ADDED:
            return workflow_signer_added()
        if self is WebhookEventTypeValue.WORKFLOW_SIGNER_REMOVED:
            return workflow_signer_removed()
        if self is WebhookEventTypeValue.WORKFLOW_SIGNER_REASSIGNED:
            return workflow_signer_reassigned()
        if self is WebhookEventTypeValue.WORKFLOW_STEP_UPDATED:
            return workflow_step_updated()
