

import typing

WebhookEventTypeValue = typing.Union[
    typing.Literal[
        "*",
        "workflow_launched",
        "workflow_updated",
        "workflow_cancelled",
        "workflow_completed",
        "workflow_approval_status_changed",
        "workflow_attribute_updated",
        "workflow_comment_added",
        "workflow_comment_removed",
        "workflow_comment_updated",
        "workflow_comment_reaction_added",
        "workflow_comment_reaction_removed",
        "workflow_counterparty_invite_sent",
        "workflow_counterparty_invite_revoked",
        "workflow_documents_added",
        "workflow_documents_removed",
        "workflow_documents_updated",
        "workflow_documents_renamed",
        "workflow_document_edited",
        "workflow_changed_turn",
        "workflow_paused",
        "workflow_resumed",
        "workflow_signature_packet_sent",
        "workflow_signature_packet_uploaded",
        "workflow_signature_packet_cancelled",
        "workflow_signer_added",
        "workflow_signer_removed",
        "workflow_signer_reassigned",
        "workflow_step_updated",
    ],
    typing.Any,
]
