



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .activity_author_model import (
        ActivityAuthorModel,
        ActivityAuthorModel_ExternalUser,
        ActivityAuthorModel_Integration,
        ActivityAuthorModel_InternalUser,
        ActivityAuthorModel_System,
    )
    from .activity_author_model_integration import ActivityAuthorModelIntegration
    from .activity_author_model_system import ActivityAuthorModelSystem
    from .activity_metadata_model import ActivityMetadataModel, ActivityMetadataModel_Comment
    from .activity_reaction_model import ActivityReactionModel
    from .attachment_not_found import AttachmentNotFound
    from .attribute_number_model import AttributeNumberModel
    from .attribute_string_model import AttributeStringModel
    from .attributes_model import AttributesModel
    from .attributes_model_draft_item import AttributesModelDraftItem
    from .attributes_model_paper_source import AttributesModelPaperSource
    from .bad_request_error_record_attachment_already_exists import BadRequestErrorRecordAttachmentAlreadyExists
    from .bad_request_error_record_attachment_extension import BadRequestErrorRecordAttachmentExtension
    from .bad_request_error_record_attachment_id_not_found import BadRequestErrorRecordAttachmentIdNotFound
    from .bad_request_error_record_attachment_missing_form_data_part import (
        BadRequestErrorRecordAttachmentMissingFormDataPart,
    )
    from .bad_request_error_record_attachment_unknown_attachment_key import (
        BadRequestErrorRecordAttachmentUnknownAttachmentKey,
    )
    from .bad_request_error_record_attachment_unknown_content_type import (
        BadRequestErrorRecordAttachmentUnknownContentType,
    )
    from .bad_request_error_record_id_not_found import BadRequestErrorRecordIdNotFound
    from .bad_request_error_record_not_found import BadRequestErrorRecordNotFound
    from .bad_request_error_workflow_launch import BadRequestErrorWorkflowLaunch
    from .bad_request_error_workflow_launch_code import BadRequestErrorWorkflowLaunchCode
    from .base_activity_feed_item_model import BaseActivityFeedItemModel
    from .base_activity_feed_item_model_type import BaseActivityFeedItemModelType
    from .comment_metadata_model import CommentMetadataModel
    from .comment_metadata_model_replied_to import CommentMetadataModelRepliedTo
    from .creator_email_model import CreatorEmailModel
    from .creator_id_model import CreatorIdModel
    from .creator_model import CreatorModel
    from .email_not_found import EmailNotFound
    from .email_response_model import (
        EmailResponseModel,
        EmailResponseModel_InboundEmail,
        EmailResponseModel_OutboundEmail,
    )
    from .external_user_model import ExternalUserModel
    from .inbound_attachment_model import InboundAttachmentModel
    from .inbound_email_response import InboundEmailResponse
    from .internal_user_model import InternalUserModel
    from .launched_workflow_model import LaunchedWorkflowModel
    from .launched_workflow_model_approvals import LaunchedWorkflowModelApprovals
    from .launched_workflow_model_approvals_state import LaunchedWorkflowModelApprovalsState
    from .launched_workflow_model_creator import LaunchedWorkflowModelCreator
    from .launched_workflow_model_signatures import LaunchedWorkflowModelSignatures
    from .launched_workflow_model_signatures_state import LaunchedWorkflowModelSignaturesState
    from .launched_workflow_model_status import LaunchedWorkflowModelStatus
    from .launched_workflow_model_step import LaunchedWorkflowModelStep
    from .outbound_attachment_model import OutboundAttachmentModel
    from .outbound_email_response import OutboundEmailResponse
    from .outbound_email_response_email_opened_timestamps_item import OutboundEmailResponseEmailOpenedTimestampsItem
    from .record_model import RecordModel
    from .record_model_attachments import RecordModelAttachments
    from .record_model_attachments_signed_copy import RecordModelAttachmentsSignedCopy
    from .record_model_links_item import RecordModelLinksItem
    from .record_model_properties import RecordModelProperties
    from .record_model_properties_agreement_date import RecordModelPropertiesAgreementDate
    from .record_model_properties_counterparty_email import RecordModelPropertiesCounterpartyEmail
    from .record_model_properties_counterparty_name import RecordModelPropertiesCounterpartyName
    from .record_model_properties_hourly_rate import RecordModelPropertiesHourlyRate
    from .record_model_properties_hourly_rate_value import RecordModelPropertiesHourlyRateValue
    from .record_model_source import RecordModelSource
    from .record_property_link_model import RecordPropertyLinkModel
    from .records_create_attachment400response import RecordsCreateAttachment400Response
    from .records_create_attachment_response import RecordsCreateAttachmentResponse
    from .records_create_record_response import RecordsCreateRecordResponse
    from .records_delete_record400response import RecordsDeleteRecord400Response
    from .records_delete_record_response import RecordsDeleteRecordResponse
    from .records_get_attachment400response import RecordsGetAttachment400Response
    from .records_get_attachment_response import RecordsGetAttachmentResponse
    from .records_get_predictions400response import RecordsGetPredictions400Response
    from .records_get_predictions403response import RecordsGetPredictions403Response
    from .records_get_predictions404response import RecordsGetPredictions404Response
    from .records_get_predictions_response import RecordsGetPredictionsResponse
    from .records_get_predictions_response_one_item import RecordsGetPredictionsResponseOneItem
    from .records_get_predictions_response_one_item_status import RecordsGetPredictionsResponseOneItemStatus
    from .records_get_record_data_response import RecordsGetRecordDataResponse
    from .records_get_schema400response import RecordsGetSchema400Response
    from .records_get_schema_response import RecordsGetSchemaResponse
    from .records_get_schema_response_attachments import RecordsGetSchemaResponseAttachments
    from .records_get_schema_response_attachments_signed_copy import RecordsGetSchemaResponseAttachmentsSignedCopy
    from .records_get_schema_response_links import RecordsGetSchemaResponseLinks
    from .records_get_schema_response_properties import RecordsGetSchemaResponseProperties
    from .records_get_schema_response_properties_additional_notes import (
        RecordsGetSchemaResponsePropertiesAdditionalNotes,
    )
    from .records_get_schema_response_properties_agreement_date import RecordsGetSchemaResponsePropertiesAgreementDate
    from .records_get_schema_response_properties_workflow_id import RecordsGetSchemaResponsePropertiesWorkflowId
    from .records_get_schema_response_record_types import RecordsGetSchemaResponseRecordTypes
    from .records_get_schema_response_record_types_contract import RecordsGetSchemaResponseRecordTypesContract
    from .records_get_xlsx_export_file400response import RecordsGetXlsxExportFile400Response
    from .records_get_xlsx_export_file_response import RecordsGetXlsxExportFileResponse
    from .records_list_all400response import RecordsListAll400Response
    from .records_list_all_response import RecordsListAllResponse
    from .records_remove_attachment_response import RecordsRemoveAttachmentResponse
    from .records_replace_metadata_response import RecordsReplaceMetadataResponse
    from .records_update_metadata404response import RecordsUpdateMetadata404Response
    from .records_update_metadata_response import RecordsUpdateMetadataResponse
    from .records_upload_smart_import_record400response import RecordsUploadSmartImportRecord400Response
    from .records_upload_smart_import_record403response import RecordsUploadSmartImportRecord403Response
    from .records_upload_smart_import_record404response import RecordsUploadSmartImportRecord404Response
    from .records_upload_smart_import_record_response import RecordsUploadSmartImportRecordResponse
    from .records_upload_smart_import_record_with_predictions400response import (
        RecordsUploadSmartImportRecordWithPredictions400Response,
    )
    from .records_upload_smart_import_record_with_predictions403response import (
        RecordsUploadSmartImportRecordWithPredictions403Response,
    )
    from .records_upload_smart_import_record_with_predictions404response import (
        RecordsUploadSmartImportRecordWithPredictions404Response,
    )
    from .records_upload_smart_import_record_with_predictions_response import (
        RecordsUploadSmartImportRecordWithPredictionsResponse,
    )
    from .user_model import UserModel
    from .webhook_event_type_value import WebhookEventTypeValue
    from .webhook_invalid_event_type_bad_request_response import WebhookInvalidEventTypeBadRequestResponse
    from .webhook_target_url_exists_bad_request_response import WebhookTargetUrlExistsBadRequestResponse
    from .webhooks_create_new400response import WebhooksCreateNew400Response
    from .webhooks_create_new_response import WebhooksCreateNewResponse
    from .webhooks_delete_specific400response import WebhooksDeleteSpecific400Response
    from .webhooks_delete_specific_response import WebhooksDeleteSpecificResponse
    from .webhooks_get_data400response import WebhooksGetData400Response
    from .webhooks_get_data_response import WebhooksGetDataResponse
    from .webhooks_get_verification_key_response import WebhooksGetVerificationKeyResponse
    from .webhooks_list_all400response import WebhooksListAll400Response
    from .webhooks_list_all_response import WebhooksListAllResponse
    from .webhooks_list_all_response_list_item import WebhooksListAllResponseListItem
    from .webhooks_update_webhook_data400response import WebhooksUpdateWebhookData400Response
    from .webhooks_update_webhook_data_response import WebhooksUpdateWebhookDataResponse
    from .workflow_async_in_progress_response import WorkflowAsyncInProgressResponse
    from .workflow_async_launch_failed_response import WorkflowAsyncLaunchFailedResponse
    from .workflow_async_launch_success_response import WorkflowAsyncLaunchSuccessResponse
    from .workflow_async_launch_success_response_workflow_urls import WorkflowAsyncLaunchSuccessResponseWorkflowUrls
    from .workflow_last_modified_author_model import (
        WorkflowLastModifiedAuthorModel,
        WorkflowLastModifiedAuthorModel_Counterparty,
        WorkflowLastModifiedAuthorModel_ExternalUser,
        WorkflowLastModifiedAuthorModel_InternalUser,
    )
    from .workflow_last_modified_author_model_counterparty import WorkflowLastModifiedAuthorModelCounterparty
    from .workflow_not_found import WorkflowNotFound
    from .workflow_request_model import WorkflowRequestModel
    from .workflow_response_model import WorkflowResponseModel
    from .workflow_response_model_attributes import WorkflowResponseModelAttributes
    from .workflow_response_model_attributes_draft_item import WorkflowResponseModelAttributesDraftItem
    from .workflow_response_model_attributes_draft_item_last_modified import (
        WorkflowResponseModelAttributesDraftItemLastModified,
    )
    from .workflow_response_model_attributes_fee import WorkflowResponseModelAttributesFee
    from .workflow_response_model_creator import WorkflowResponseModelCreator
    from .workflow_response_model_roles_item import WorkflowResponseModelRolesItem
    from .workflow_response_model_roles_item_assignees_item import WorkflowResponseModelRolesItemAssigneesItem
    from .workflow_response_model_schema import WorkflowResponseModelSchema
    from .workflow_response_model_schema_amount import WorkflowResponseModelSchemaAmount
    from .workflow_response_model_schema_counterparty_name import WorkflowResponseModelSchemaCounterpartyName
    from .workflow_response_model_schema_draft import WorkflowResponseModelSchemaDraft
    from .workflow_response_model_schema_draft_element_type import WorkflowResponseModelSchemaDraftElementType
    from .workflow_response_model_schema_fee import WorkflowResponseModelSchemaFee
    from .workflow_response_model_schema_line_items import WorkflowResponseModelSchemaLineItems
    from .workflow_response_model_schema_line_items_element_type import WorkflowResponseModelSchemaLineItemsElementType
    from .workflow_response_model_schema_line_items_element_type_schema import (
        WorkflowResponseModelSchemaLineItemsElementTypeSchema,
    )
    from .workflow_response_model_schema_line_items_element_type_schema_another_child_attribute import (
        WorkflowResponseModelSchemaLineItemsElementTypeSchemaAnotherChildAttribute,
    )
    from .workflow_response_model_schema_line_items_element_type_schema_child_attribute import (
        WorkflowResponseModelSchemaLineItemsElementTypeSchemaChildAttribute,
    )
    from .workflow_response_model_status import WorkflowResponseModelStatus
    from .workflow_role_assignee_model import WorkflowRoleAssigneeModel
    from .workflow_role_model import WorkflowRoleModel
    from .workflow_state_model import (
        WorkflowStateModel,
        WorkflowStateModel_Completed,
        WorkflowStateModel_InProgress,
        WorkflowStateModel_NotApplicable,
        WorkflowStateModel_NotStarted,
    )
    from .workflow_state_model_completed import WorkflowStateModelCompleted
    from .workflow_state_model_in_progress import WorkflowStateModelInProgress
    from .workflow_state_model_not_applicable import WorkflowStateModelNotApplicable
    from .workflow_state_model_not_started import WorkflowStateModelNotStarted
    from .workflow_template_id_model import WorkflowTemplateIdModel
    from .workflows_create_comment400response import WorkflowsCreateComment400Response
    from .workflows_create_comment_response import WorkflowsCreateCommentResponse
    from .workflows_get_approval_requests403response import WorkflowsGetApprovalRequests403Response
    from .workflows_get_approval_requests404response import WorkflowsGetApprovalRequests404Response
    from .workflows_get_approval_requests_response import WorkflowsGetApprovalRequestsResponse
    from .workflows_get_approval_requests_response_list_item import WorkflowsGetApprovalRequestsResponseListItem
    from .workflows_get_async_job_status404response import WorkflowsGetAsyncJobStatus404Response
    from .workflows_get_async_job_status_response import WorkflowsGetAsyncJobStatusResponse
    from .workflows_get_attachment_from_email_thread404response import WorkflowsGetAttachmentFromEmailThread404Response
    from .workflows_get_attachment_from_email_thread_response import WorkflowsGetAttachmentFromEmailThreadResponse
    from .workflows_get_document_by_key400response import WorkflowsGetDocumentByKey400Response
    from .workflows_get_document_by_key_response import WorkflowsGetDocumentByKeyResponse
    from .workflows_get_email_thread_response import WorkflowsGetEmailThreadResponse
    from .workflows_get_email_threads_response import WorkflowsGetEmailThreadsResponse
    from .workflows_get_turn_history403response import WorkflowsGetTurnHistory403Response
    from .workflows_get_turn_history404response import WorkflowsGetTurnHistory404Response
    from .workflows_get_turn_history_response import WorkflowsGetTurnHistoryResponse
    from .workflows_get_turn_history_response_list_item import WorkflowsGetTurnHistoryResponseListItem
    from .workflows_get_workflow_response import WorkflowsGetWorkflowResponse
    from .workflows_get_workflow_schema400response import WorkflowsGetWorkflowSchema400Response
    from .workflows_get_workflow_schema_response import WorkflowsGetWorkflowSchemaResponse
    from .workflows_get_workflow_schema_response_schema import WorkflowsGetWorkflowSchemaResponseSchema
    from .workflows_get_workflow_schema_response_schema_amount import WorkflowsGetWorkflowSchemaResponseSchemaAmount
    from .workflows_get_workflow_schema_response_schema_counterparty_name import (
        WorkflowsGetWorkflowSchemaResponseSchemaCounterpartyName,
    )
    from .workflows_get_workflow_schema_response_schema_draft import WorkflowsGetWorkflowSchemaResponseSchemaDraft
    from .workflows_get_workflow_schema_response_schema_draft_element_type import (
        WorkflowsGetWorkflowSchemaResponseSchemaDraftElementType,
    )
    from .workflows_get_workflow_schema_response_schema_fee import WorkflowsGetWorkflowSchemaResponseSchemaFee
    from .workflows_get_workflow_schema_response_schema_line_items import (
        WorkflowsGetWorkflowSchemaResponseSchemaLineItems,
    )
    from .workflows_get_workflow_schema_response_schema_line_items_element_type import (
        WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementType,
    )
    from .workflows_get_workflow_schema_response_schema_line_items_element_type_schema import (
        WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchema,
    )
    from .workflows_get_workflow_schema_response_schema_line_items_element_type_schema_another_child_attribute import (
        WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute,
    )
    from .workflows_get_workflow_schema_response_schema_line_items_element_type_schema_child_attribute import (
        WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaChildAttribute,
    )
    from .workflows_launch_asynchronously400response import WorkflowsLaunchAsynchronously400Response
    from .workflows_launch_asynchronously_response import WorkflowsLaunchAsynchronouslyResponse
    from .workflows_list_all_participants403response import WorkflowsListAllParticipants403Response
    from .workflows_list_all_participants404response import WorkflowsListAllParticipants404Response
    from .workflows_list_all_participants_response import WorkflowsListAllParticipantsResponse
    from .workflows_list_all_participants_response_list_item import WorkflowsListAllParticipantsResponseListItem
    from .workflows_list_all_response import WorkflowsListAllResponse
    from .workflows_list_all_workflow_schemas400response import WorkflowsListAllWorkflowSchemas400Response
    from .workflows_list_all_workflow_schemas_response import WorkflowsListAllWorkflowSchemasResponse
    from .workflows_list_all_workflow_schemas_response_list_item import WorkflowsListAllWorkflowSchemasResponseListItem
    from .workflows_list_all_workflow_schemas_response_list_item_schema import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchema,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_amount import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaAmount,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_counterparty_name import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaCounterpartyName,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_draft import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaDraft,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_draft_element_type import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaDraftElementType,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_fee import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaFee,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_line_items import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItems,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_line_items_element_type import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementType,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchema,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema_another_child_attribute import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaAnotherChildAttribute,
    )
    from .workflows_list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema_child_attribute import (
        WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaChildAttribute,
    )
    from .workflows_list_approvals400response import WorkflowsListApprovals400Response
    from .workflows_list_approvals_response import WorkflowsListApprovalsResponse
    from .workflows_list_approvals_response_approval_groups_item import WorkflowsListApprovalsResponseApprovalGroupsItem
    from .workflows_list_approvals_response_approval_groups_item_reviewers_item import (
        WorkflowsListApprovalsResponseApprovalGroupsItemReviewersItem,
    )
    from .workflows_list_approvals_response_roles_item import WorkflowsListApprovalsResponseRolesItem
    from .workflows_list_approvals_response_roles_item_assignees_item import (
        WorkflowsListApprovalsResponseRolesItemAssigneesItem,
    )
    from .workflows_list_signatures400response import WorkflowsListSignatures400Response
    from .workflows_list_signatures403response import WorkflowsListSignatures403Response
    from .workflows_list_signatures_response import WorkflowsListSignaturesResponse
    from .workflows_list_signatures_response_signers_item import WorkflowsListSignaturesResponseSignersItem
    from .workflows_list_signatures_response_signers_item_delegates_item import (
        WorkflowsListSignaturesResponseSignersItemDelegatesItem,
    )
    from .workflows_revert_to_review403response import WorkflowsRevertToReview403Response
    from .workflows_revert_to_review404response import WorkflowsRevertToReview404Response
    from .workflows_revert_to_review_response import WorkflowsRevertToReviewResponse
    from .workflows_revert_to_review_response_code import WorkflowsRevertToReviewResponseCode
    from .workflows_revert_to_review_response_message import WorkflowsRevertToReviewResponseMessage
    from .workflows_update_approval_status400response import WorkflowsUpdateApprovalStatus400Response
    from .workflows_update_approval_status400response_message import WorkflowsUpdateApprovalStatus400ResponseMessage
    from .workflows_update_approval_status_response import WorkflowsUpdateApprovalStatusResponse
    from .workflows_update_metadata400response import WorkflowsUpdateMetadata400Response
    from .workflows_update_metadata403response import WorkflowsUpdateMetadata403Response
    from .workflows_update_metadata404response import WorkflowsUpdateMetadata404Response
    from .workflows_update_metadata_response import WorkflowsUpdateMetadataResponse
    from .workflows_update_metadata_response_approvals import WorkflowsUpdateMetadataResponseApprovals
    from .workflows_update_metadata_response_attributes import WorkflowsUpdateMetadataResponseAttributes
    from .workflows_update_metadata_response_attributes_draft_item import (
        WorkflowsUpdateMetadataResponseAttributesDraftItem,
    )
    from .workflows_update_metadata_response_attributes_fee import WorkflowsUpdateMetadataResponseAttributesFee
    from .workflows_update_metadata_response_creator import WorkflowsUpdateMetadataResponseCreator
    from .workflows_update_metadata_response_roles_item import WorkflowsUpdateMetadataResponseRolesItem
    from .workflows_update_metadata_response_roles_item_assignees_item import (
        WorkflowsUpdateMetadataResponseRolesItemAssigneesItem,
    )
    from .workflows_update_metadata_response_schema import WorkflowsUpdateMetadataResponseSchema
    from .workflows_update_metadata_response_schema_amount import WorkflowsUpdateMetadataResponseSchemaAmount
    from .workflows_update_metadata_response_schema_counterparty_name import (
        WorkflowsUpdateMetadataResponseSchemaCounterpartyName,
    )
    from .workflows_update_metadata_response_schema_draft import WorkflowsUpdateMetadataResponseSchemaDraft
    from .workflows_update_metadata_response_schema_draft_element_type import (
        WorkflowsUpdateMetadataResponseSchemaDraftElementType,
    )
    from .workflows_update_metadata_response_schema_fee import WorkflowsUpdateMetadataResponseSchemaFee
    from .workflows_update_metadata_response_schema_line_items import WorkflowsUpdateMetadataResponseSchemaLineItems
    from .workflows_update_metadata_response_schema_line_items_element_type import (
        WorkflowsUpdateMetadataResponseSchemaLineItemsElementType,
    )
    from .workflows_update_metadata_response_schema_line_items_element_type_schema import (
        WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchema,
    )
    from .workflows_update_metadata_response_schema_line_items_element_type_schema_another_child_attribute import (
        WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute,
    )
    from .workflows_update_metadata_response_schema_line_items_element_type_schema_child_attribute import (
        WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaChildAttribute,
    )
    from .workflows_update_metadata_response_signatures import WorkflowsUpdateMetadataResponseSignatures
_dynamic_imports: typing.Dict[str, str] = {
    "ActivityAuthorModel": ".activity_author_model",
    "ActivityAuthorModelIntegration": ".activity_author_model_integration",
    "ActivityAuthorModelSystem": ".activity_author_model_system",
    "ActivityAuthorModel_ExternalUser": ".activity_author_model",
    "ActivityAuthorModel_Integration": ".activity_author_model",
    "ActivityAuthorModel_InternalUser": ".activity_author_model",
    "ActivityAuthorModel_System": ".activity_author_model",
    "ActivityMetadataModel": ".activity_metadata_model",
    "ActivityMetadataModel_Comment": ".activity_metadata_model",
    "ActivityReactionModel": ".activity_reaction_model",
    "AttachmentNotFound": ".attachment_not_found",
    "AttributeNumberModel": ".attribute_number_model",
    "AttributeStringModel": ".attribute_string_model",
    "AttributesModel": ".attributes_model",
    "AttributesModelDraftItem": ".attributes_model_draft_item",
    "AttributesModelPaperSource": ".attributes_model_paper_source",
    "BadRequestErrorRecordAttachmentAlreadyExists": ".bad_request_error_record_attachment_already_exists",
    "BadRequestErrorRecordAttachmentExtension": ".bad_request_error_record_attachment_extension",
    "BadRequestErrorRecordAttachmentIdNotFound": ".bad_request_error_record_attachment_id_not_found",
    "BadRequestErrorRecordAttachmentMissingFormDataPart": ".bad_request_error_record_attachment_missing_form_data_part",
    "BadRequestErrorRecordAttachmentUnknownAttachmentKey": ".bad_request_error_record_attachment_unknown_attachment_key",
    "BadRequestErrorRecordAttachmentUnknownContentType": ".bad_request_error_record_attachment_unknown_content_type",
    "BadRequestErrorRecordIdNotFound": ".bad_request_error_record_id_not_found",
    "BadRequestErrorRecordNotFound": ".bad_request_error_record_not_found",
    "BadRequestErrorWorkflowLaunch": ".bad_request_error_workflow_launch",
    "BadRequestErrorWorkflowLaunchCode": ".bad_request_error_workflow_launch_code",
    "BaseActivityFeedItemModel": ".base_activity_feed_item_model",
    "BaseActivityFeedItemModelType": ".base_activity_feed_item_model_type",
    "CommentMetadataModel": ".comment_metadata_model",
    "CommentMetadataModelRepliedTo": ".comment_metadata_model_replied_to",
    "CreatorEmailModel": ".creator_email_model",
    "CreatorIdModel": ".creator_id_model",
    "CreatorModel": ".creator_model",
    "EmailNotFound": ".email_not_found",
    "EmailResponseModel": ".email_response_model",
    "EmailResponseModel_InboundEmail": ".email_response_model",
    "EmailResponseModel_OutboundEmail": ".email_response_model",
    "ExternalUserModel": ".external_user_model",
    "InboundAttachmentModel": ".inbound_attachment_model",
    "InboundEmailResponse": ".inbound_email_response",
    "InternalUserModel": ".internal_user_model",
    "LaunchedWorkflowModel": ".launched_workflow_model",
    "LaunchedWorkflowModelApprovals": ".launched_workflow_model_approvals",
    "LaunchedWorkflowModelApprovalsState": ".launched_workflow_model_approvals_state",
    "LaunchedWorkflowModelCreator": ".launched_workflow_model_creator",
    "LaunchedWorkflowModelSignatures": ".launched_workflow_model_signatures",
    "LaunchedWorkflowModelSignaturesState": ".launched_workflow_model_signatures_state",
    "LaunchedWorkflowModelStatus": ".launched_workflow_model_status",
    "LaunchedWorkflowModelStep": ".launched_workflow_model_step",
    "OutboundAttachmentModel": ".outbound_attachment_model",
    "OutboundEmailResponse": ".outbound_email_response",
    "OutboundEmailResponseEmailOpenedTimestampsItem": ".outbound_email_response_email_opened_timestamps_item",
    "RecordModel": ".record_model",
    "RecordModelAttachments": ".record_model_attachments",
    "RecordModelAttachmentsSignedCopy": ".record_model_attachments_signed_copy",
    "RecordModelLinksItem": ".record_model_links_item",
    "RecordModelProperties": ".record_model_properties",
    "RecordModelPropertiesAgreementDate": ".record_model_properties_agreement_date",
    "RecordModelPropertiesCounterpartyEmail": ".record_model_properties_counterparty_email",
    "RecordModelPropertiesCounterpartyName": ".record_model_properties_counterparty_name",
    "RecordModelPropertiesHourlyRate": ".record_model_properties_hourly_rate",
    "RecordModelPropertiesHourlyRateValue": ".record_model_properties_hourly_rate_value",
    "RecordModelSource": ".record_model_source",
    "RecordPropertyLinkModel": ".record_property_link_model",
    "RecordsCreateAttachment400Response": ".records_create_attachment400response",
    "RecordsCreateAttachmentResponse": ".records_create_attachment_response",
    "RecordsCreateRecordResponse": ".records_create_record_response",
    "RecordsDeleteRecord400Response": ".records_delete_record400response",
    "RecordsDeleteRecordResponse": ".records_delete_record_response",
    "RecordsGetAttachment400Response": ".records_get_attachment400response",
    "RecordsGetAttachmentResponse": ".records_get_attachment_response",
    "RecordsGetPredictions400Response": ".records_get_predictions400response",
    "RecordsGetPredictions403Response": ".records_get_predictions403response",
    "RecordsGetPredictions404Response": ".records_get_predictions404response",
    "RecordsGetPredictionsResponse": ".records_get_predictions_response",
    "RecordsGetPredictionsResponseOneItem": ".records_get_predictions_response_one_item",
    "RecordsGetPredictionsResponseOneItemStatus": ".records_get_predictions_response_one_item_status",
    "RecordsGetRecordDataResponse": ".records_get_record_data_response",
    "RecordsGetSchema400Response": ".records_get_schema400response",
    "RecordsGetSchemaResponse": ".records_get_schema_response",
    "RecordsGetSchemaResponseAttachments": ".records_get_schema_response_attachments",
    "RecordsGetSchemaResponseAttachmentsSignedCopy": ".records_get_schema_response_attachments_signed_copy",
    "RecordsGetSchemaResponseLinks": ".records_get_schema_response_links",
    "RecordsGetSchemaResponseProperties": ".records_get_schema_response_properties",
    "RecordsGetSchemaResponsePropertiesAdditionalNotes": ".records_get_schema_response_properties_additional_notes",
    "RecordsGetSchemaResponsePropertiesAgreementDate": ".records_get_schema_response_properties_agreement_date",
    "RecordsGetSchemaResponsePropertiesWorkflowId": ".records_get_schema_response_properties_workflow_id",
    "RecordsGetSchemaResponseRecordTypes": ".records_get_schema_response_record_types",
    "RecordsGetSchemaResponseRecordTypesContract": ".records_get_schema_response_record_types_contract",
    "RecordsGetXlsxExportFile400Response": ".records_get_xlsx_export_file400response",
    "RecordsGetXlsxExportFileResponse": ".records_get_xlsx_export_file_response",
    "RecordsListAll400Response": ".records_list_all400response",
    "RecordsListAllResponse": ".records_list_all_response",
    "RecordsRemoveAttachmentResponse": ".records_remove_attachment_response",
    "RecordsReplaceMetadataResponse": ".records_replace_metadata_response",
    "RecordsUpdateMetadata404Response": ".records_update_metadata404response",
    "RecordsUpdateMetadataResponse": ".records_update_metadata_response",
    "RecordsUploadSmartImportRecord400Response": ".records_upload_smart_import_record400response",
    "RecordsUploadSmartImportRecord403Response": ".records_upload_smart_import_record403response",
    "RecordsUploadSmartImportRecord404Response": ".records_upload_smart_import_record404response",
    "RecordsUploadSmartImportRecordResponse": ".records_upload_smart_import_record_response",
    "RecordsUploadSmartImportRecordWithPredictions400Response": ".records_upload_smart_import_record_with_predictions400response",
    "RecordsUploadSmartImportRecordWithPredictions403Response": ".records_upload_smart_import_record_with_predictions403response",
    "RecordsUploadSmartImportRecordWithPredictions404Response": ".records_upload_smart_import_record_with_predictions404response",
    "RecordsUploadSmartImportRecordWithPredictionsResponse": ".records_upload_smart_import_record_with_predictions_response",
    "UserModel": ".user_model",
    "WebhookEventTypeValue": ".webhook_event_type_value",
    "WebhookInvalidEventTypeBadRequestResponse": ".webhook_invalid_event_type_bad_request_response",
    "WebhookTargetUrlExistsBadRequestResponse": ".webhook_target_url_exists_bad_request_response",
    "WebhooksCreateNew400Response": ".webhooks_create_new400response",
    "WebhooksCreateNewResponse": ".webhooks_create_new_response",
    "WebhooksDeleteSpecific400Response": ".webhooks_delete_specific400response",
    "WebhooksDeleteSpecificResponse": ".webhooks_delete_specific_response",
    "WebhooksGetData400Response": ".webhooks_get_data400response",
    "WebhooksGetDataResponse": ".webhooks_get_data_response",
    "WebhooksGetVerificationKeyResponse": ".webhooks_get_verification_key_response",
    "WebhooksListAll400Response": ".webhooks_list_all400response",
    "WebhooksListAllResponse": ".webhooks_list_all_response",
    "WebhooksListAllResponseListItem": ".webhooks_list_all_response_list_item",
    "WebhooksUpdateWebhookData400Response": ".webhooks_update_webhook_data400response",
    "WebhooksUpdateWebhookDataResponse": ".webhooks_update_webhook_data_response",
    "WorkflowAsyncInProgressResponse": ".workflow_async_in_progress_response",
    "WorkflowAsyncLaunchFailedResponse": ".workflow_async_launch_failed_response",
    "WorkflowAsyncLaunchSuccessResponse": ".workflow_async_launch_success_response",
    "WorkflowAsyncLaunchSuccessResponseWorkflowUrls": ".workflow_async_launch_success_response_workflow_urls",
    "WorkflowLastModifiedAuthorModel": ".workflow_last_modified_author_model",
    "WorkflowLastModifiedAuthorModelCounterparty": ".workflow_last_modified_author_model_counterparty",
    "WorkflowLastModifiedAuthorModel_Counterparty": ".workflow_last_modified_author_model",
    "WorkflowLastModifiedAuthorModel_ExternalUser": ".workflow_last_modified_author_model",
    "WorkflowLastModifiedAuthorModel_InternalUser": ".workflow_last_modified_author_model",
    "WorkflowNotFound": ".workflow_not_found",
    "WorkflowRequestModel": ".workflow_request_model",
    "WorkflowResponseModel": ".workflow_response_model",
    "WorkflowResponseModelAttributes": ".workflow_response_model_attributes",
    "WorkflowResponseModelAttributesDraftItem": ".workflow_response_model_attributes_draft_item",
    "WorkflowResponseModelAttributesDraftItemLastModified": ".workflow_response_model_attributes_draft_item_last_modified",
    "WorkflowResponseModelAttributesFee": ".workflow_response_model_attributes_fee",
    "WorkflowResponseModelCreator": ".workflow_response_model_creator",
    "WorkflowResponseModelRolesItem": ".workflow_response_model_roles_item",
    "WorkflowResponseModelRolesItemAssigneesItem": ".workflow_response_model_roles_item_assignees_item",
    "WorkflowResponseModelSchema": ".workflow_response_model_schema",
    "WorkflowResponseModelSchemaAmount": ".workflow_response_model_schema_amount",
    "WorkflowResponseModelSchemaCounterpartyName": ".workflow_response_model_schema_counterparty_name",
    "WorkflowResponseModelSchemaDraft": ".workflow_response_model_schema_draft",
    "WorkflowResponseModelSchemaDraftElementType": ".workflow_response_model_schema_draft_element_type",
    "WorkflowResponseModelSchemaFee": ".workflow_response_model_schema_fee",
    "WorkflowResponseModelSchemaLineItems": ".workflow_response_model_schema_line_items",
    "WorkflowResponseModelSchemaLineItemsElementType": ".workflow_response_model_schema_line_items_element_type",
    "WorkflowResponseModelSchemaLineItemsElementTypeSchema": ".workflow_response_model_schema_line_items_element_type_schema",
    "WorkflowResponseModelSchemaLineItemsElementTypeSchemaAnotherChildAttribute": ".workflow_response_model_schema_line_items_element_type_schema_another_child_attribute",
    "WorkflowResponseModelSchemaLineItemsElementTypeSchemaChildAttribute": ".workflow_response_model_schema_line_items_element_type_schema_child_attribute",
    "WorkflowResponseModelStatus": ".workflow_response_model_status",
    "WorkflowRoleAssigneeModel": ".workflow_role_assignee_model",
    "WorkflowRoleModel": ".workflow_role_model",
    "WorkflowStateModel": ".workflow_state_model",
    "WorkflowStateModelCompleted": ".workflow_state_model_completed",
    "WorkflowStateModelInProgress": ".workflow_state_model_in_progress",
    "WorkflowStateModelNotApplicable": ".workflow_state_model_not_applicable",
    "WorkflowStateModelNotStarted": ".workflow_state_model_not_started",
    "WorkflowStateModel_Completed": ".workflow_state_model",
    "WorkflowStateModel_InProgress": ".workflow_state_model",
    "WorkflowStateModel_NotApplicable": ".workflow_state_model",
    "WorkflowStateModel_NotStarted": ".workflow_state_model",
    "WorkflowTemplateIdModel": ".workflow_template_id_model",
    "WorkflowsCreateComment400Response": ".workflows_create_comment400response",
    "WorkflowsCreateCommentResponse": ".workflows_create_comment_response",
    "WorkflowsGetApprovalRequests403Response": ".workflows_get_approval_requests403response",
    "WorkflowsGetApprovalRequests404Response": ".workflows_get_approval_requests404response",
    "WorkflowsGetApprovalRequestsResponse": ".workflows_get_approval_requests_response",
    "WorkflowsGetApprovalRequestsResponseListItem": ".workflows_get_approval_requests_response_list_item",
    "WorkflowsGetAsyncJobStatus404Response": ".workflows_get_async_job_status404response",
    "WorkflowsGetAsyncJobStatusResponse": ".workflows_get_async_job_status_response",
    "WorkflowsGetAttachmentFromEmailThread404Response": ".workflows_get_attachment_from_email_thread404response",
    "WorkflowsGetAttachmentFromEmailThreadResponse": ".workflows_get_attachment_from_email_thread_response",
    "WorkflowsGetDocumentByKey400Response": ".workflows_get_document_by_key400response",
    "WorkflowsGetDocumentByKeyResponse": ".workflows_get_document_by_key_response",
    "WorkflowsGetEmailThreadResponse": ".workflows_get_email_thread_response",
    "WorkflowsGetEmailThreadsResponse": ".workflows_get_email_threads_response",
    "WorkflowsGetTurnHistory403Response": ".workflows_get_turn_history403response",
    "WorkflowsGetTurnHistory404Response": ".workflows_get_turn_history404response",
    "WorkflowsGetTurnHistoryResponse": ".workflows_get_turn_history_response",
    "WorkflowsGetTurnHistoryResponseListItem": ".workflows_get_turn_history_response_list_item",
    "WorkflowsGetWorkflowResponse": ".workflows_get_workflow_response",
    "WorkflowsGetWorkflowSchema400Response": ".workflows_get_workflow_schema400response",
    "WorkflowsGetWorkflowSchemaResponse": ".workflows_get_workflow_schema_response",
    "WorkflowsGetWorkflowSchemaResponseSchema": ".workflows_get_workflow_schema_response_schema",
    "WorkflowsGetWorkflowSchemaResponseSchemaAmount": ".workflows_get_workflow_schema_response_schema_amount",
    "WorkflowsGetWorkflowSchemaResponseSchemaCounterpartyName": ".workflows_get_workflow_schema_response_schema_counterparty_name",
    "WorkflowsGetWorkflowSchemaResponseSchemaDraft": ".workflows_get_workflow_schema_response_schema_draft",
    "WorkflowsGetWorkflowSchemaResponseSchemaDraftElementType": ".workflows_get_workflow_schema_response_schema_draft_element_type",
    "WorkflowsGetWorkflowSchemaResponseSchemaFee": ".workflows_get_workflow_schema_response_schema_fee",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItems": ".workflows_get_workflow_schema_response_schema_line_items",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementType": ".workflows_get_workflow_schema_response_schema_line_items_element_type",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchema": ".workflows_get_workflow_schema_response_schema_line_items_element_type_schema",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute": ".workflows_get_workflow_schema_response_schema_line_items_element_type_schema_another_child_attribute",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaChildAttribute": ".workflows_get_workflow_schema_response_schema_line_items_element_type_schema_child_attribute",
    "WorkflowsLaunchAsynchronously400Response": ".workflows_launch_asynchronously400response",
    "WorkflowsLaunchAsynchronouslyResponse": ".workflows_launch_asynchronously_response",
    "WorkflowsListAllParticipants403Response": ".workflows_list_all_participants403response",
    "WorkflowsListAllParticipants404Response": ".workflows_list_all_participants404response",
    "WorkflowsListAllParticipantsResponse": ".workflows_list_all_participants_response",
    "WorkflowsListAllParticipantsResponseListItem": ".workflows_list_all_participants_response_list_item",
    "WorkflowsListAllResponse": ".workflows_list_all_response",
    "WorkflowsListAllWorkflowSchemas400Response": ".workflows_list_all_workflow_schemas400response",
    "WorkflowsListAllWorkflowSchemasResponse": ".workflows_list_all_workflow_schemas_response",
    "WorkflowsListAllWorkflowSchemasResponseListItem": ".workflows_list_all_workflow_schemas_response_list_item",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchema": ".workflows_list_all_workflow_schemas_response_list_item_schema",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaAmount": ".workflows_list_all_workflow_schemas_response_list_item_schema_amount",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaCounterpartyName": ".workflows_list_all_workflow_schemas_response_list_item_schema_counterparty_name",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaDraft": ".workflows_list_all_workflow_schemas_response_list_item_schema_draft",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaDraftElementType": ".workflows_list_all_workflow_schemas_response_list_item_schema_draft_element_type",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaFee": ".workflows_list_all_workflow_schemas_response_list_item_schema_fee",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItems": ".workflows_list_all_workflow_schemas_response_list_item_schema_line_items",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementType": ".workflows_list_all_workflow_schemas_response_list_item_schema_line_items_element_type",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchema": ".workflows_list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaAnotherChildAttribute": ".workflows_list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema_another_child_attribute",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaChildAttribute": ".workflows_list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema_child_attribute",
    "WorkflowsListApprovals400Response": ".workflows_list_approvals400response",
    "WorkflowsListApprovalsResponse": ".workflows_list_approvals_response",
    "WorkflowsListApprovalsResponseApprovalGroupsItem": ".workflows_list_approvals_response_approval_groups_item",
    "WorkflowsListApprovalsResponseApprovalGroupsItemReviewersItem": ".workflows_list_approvals_response_approval_groups_item_reviewers_item",
    "WorkflowsListApprovalsResponseRolesItem": ".workflows_list_approvals_response_roles_item",
    "WorkflowsListApprovalsResponseRolesItemAssigneesItem": ".workflows_list_approvals_response_roles_item_assignees_item",
    "WorkflowsListSignatures400Response": ".workflows_list_signatures400response",
    "WorkflowsListSignatures403Response": ".workflows_list_signatures403response",
    "WorkflowsListSignaturesResponse": ".workflows_list_signatures_response",
    "WorkflowsListSignaturesResponseSignersItem": ".workflows_list_signatures_response_signers_item",
    "WorkflowsListSignaturesResponseSignersItemDelegatesItem": ".workflows_list_signatures_response_signers_item_delegates_item",
    "WorkflowsRevertToReview403Response": ".workflows_revert_to_review403response",
    "WorkflowsRevertToReview404Response": ".workflows_revert_to_review404response",
    "WorkflowsRevertToReviewResponse": ".workflows_revert_to_review_response",
    "WorkflowsRevertToReviewResponseCode": ".workflows_revert_to_review_response_code",
    "WorkflowsRevertToReviewResponseMessage": ".workflows_revert_to_review_response_message",
    "WorkflowsUpdateApprovalStatus400Response": ".workflows_update_approval_status400response",
    "WorkflowsUpdateApprovalStatus400ResponseMessage": ".workflows_update_approval_status400response_message",
    "WorkflowsUpdateApprovalStatusResponse": ".workflows_update_approval_status_response",
    "WorkflowsUpdateMetadata400Response": ".workflows_update_metadata400response",
    "WorkflowsUpdateMetadata403Response": ".workflows_update_metadata403response",
    "WorkflowsUpdateMetadata404Response": ".workflows_update_metadata404response",
    "WorkflowsUpdateMetadataResponse": ".workflows_update_metadata_response",
    "WorkflowsUpdateMetadataResponseApprovals": ".workflows_update_metadata_response_approvals",
    "WorkflowsUpdateMetadataResponseAttributes": ".workflows_update_metadata_response_attributes",
    "WorkflowsUpdateMetadataResponseAttributesDraftItem": ".workflows_update_metadata_response_attributes_draft_item",
    "WorkflowsUpdateMetadataResponseAttributesFee": ".workflows_update_metadata_response_attributes_fee",
    "WorkflowsUpdateMetadataResponseCreator": ".workflows_update_metadata_response_creator",
    "WorkflowsUpdateMetadataResponseRolesItem": ".workflows_update_metadata_response_roles_item",
    "WorkflowsUpdateMetadataResponseRolesItemAssigneesItem": ".workflows_update_metadata_response_roles_item_assignees_item",
    "WorkflowsUpdateMetadataResponseSchema": ".workflows_update_metadata_response_schema",
    "WorkflowsUpdateMetadataResponseSchemaAmount": ".workflows_update_metadata_response_schema_amount",
    "WorkflowsUpdateMetadataResponseSchemaCounterpartyName": ".workflows_update_metadata_response_schema_counterparty_name",
    "WorkflowsUpdateMetadataResponseSchemaDraft": ".workflows_update_metadata_response_schema_draft",
    "WorkflowsUpdateMetadataResponseSchemaDraftElementType": ".workflows_update_metadata_response_schema_draft_element_type",
    "WorkflowsUpdateMetadataResponseSchemaFee": ".workflows_update_metadata_response_schema_fee",
    "WorkflowsUpdateMetadataResponseSchemaLineItems": ".workflows_update_metadata_response_schema_line_items",
    "WorkflowsUpdateMetadataResponseSchemaLineItemsElementType": ".workflows_update_metadata_response_schema_line_items_element_type",
    "WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchema": ".workflows_update_metadata_response_schema_line_items_element_type_schema",
    "WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute": ".workflows_update_metadata_response_schema_line_items_element_type_schema_another_child_attribute",
    "WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaChildAttribute": ".workflows_update_metadata_response_schema_line_items_element_type_schema_child_attribute",
    "WorkflowsUpdateMetadataResponseSignatures": ".workflows_update_metadata_response_signatures",
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
    "ActivityAuthorModel",
    "ActivityAuthorModelIntegration",
    "ActivityAuthorModelSystem",
    "ActivityAuthorModel_ExternalUser",
    "ActivityAuthorModel_Integration",
    "ActivityAuthorModel_InternalUser",
    "ActivityAuthorModel_System",
    "ActivityMetadataModel",
    "ActivityMetadataModel_Comment",
    "ActivityReactionModel",
    "AttachmentNotFound",
    "AttributeNumberModel",
    "AttributeStringModel",
    "AttributesModel",
    "AttributesModelDraftItem",
    "AttributesModelPaperSource",
    "BadRequestErrorRecordAttachmentAlreadyExists",
    "BadRequestErrorRecordAttachmentExtension",
    "BadRequestErrorRecordAttachmentIdNotFound",
    "BadRequestErrorRecordAttachmentMissingFormDataPart",
    "BadRequestErrorRecordAttachmentUnknownAttachmentKey",
    "BadRequestErrorRecordAttachmentUnknownContentType",
    "BadRequestErrorRecordIdNotFound",
    "BadRequestErrorRecordNotFound",
    "BadRequestErrorWorkflowLaunch",
    "BadRequestErrorWorkflowLaunchCode",
    "BaseActivityFeedItemModel",
    "BaseActivityFeedItemModelType",
    "CommentMetadataModel",
    "CommentMetadataModelRepliedTo",
    "CreatorEmailModel",
    "CreatorIdModel",
    "CreatorModel",
    "EmailNotFound",
    "EmailResponseModel",
    "EmailResponseModel_InboundEmail",
    "EmailResponseModel_OutboundEmail",
    "ExternalUserModel",
    "InboundAttachmentModel",
    "InboundEmailResponse",
    "InternalUserModel",
    "LaunchedWorkflowModel",
    "LaunchedWorkflowModelApprovals",
    "LaunchedWorkflowModelApprovalsState",
    "LaunchedWorkflowModelCreator",
    "LaunchedWorkflowModelSignatures",
    "LaunchedWorkflowModelSignaturesState",
    "LaunchedWorkflowModelStatus",
    "LaunchedWorkflowModelStep",
    "OutboundAttachmentModel",
    "OutboundEmailResponse",
    "OutboundEmailResponseEmailOpenedTimestampsItem",
    "RecordModel",
    "RecordModelAttachments",
    "RecordModelAttachmentsSignedCopy",
    "RecordModelLinksItem",
    "RecordModelProperties",
    "RecordModelPropertiesAgreementDate",
    "RecordModelPropertiesCounterpartyEmail",
    "RecordModelPropertiesCounterpartyName",
    "RecordModelPropertiesHourlyRate",
    "RecordModelPropertiesHourlyRateValue",
    "RecordModelSource",
    "RecordPropertyLinkModel",
    "RecordsCreateAttachment400Response",
    "RecordsCreateAttachmentResponse",
    "RecordsCreateRecordResponse",
    "RecordsDeleteRecord400Response",
    "RecordsDeleteRecordResponse",
    "RecordsGetAttachment400Response",
    "RecordsGetAttachmentResponse",
    "RecordsGetPredictions400Response",
    "RecordsGetPredictions403Response",
    "RecordsGetPredictions404Response",
    "RecordsGetPredictionsResponse",
    "RecordsGetPredictionsResponseOneItem",
    "RecordsGetPredictionsResponseOneItemStatus",
    "RecordsGetRecordDataResponse",
    "RecordsGetSchema400Response",
    "RecordsGetSchemaResponse",
    "RecordsGetSchemaResponseAttachments",
    "RecordsGetSchemaResponseAttachmentsSignedCopy",
    "RecordsGetSchemaResponseLinks",
    "RecordsGetSchemaResponseProperties",
    "RecordsGetSchemaResponsePropertiesAdditionalNotes",
    "RecordsGetSchemaResponsePropertiesAgreementDate",
    "RecordsGetSchemaResponsePropertiesWorkflowId",
    "RecordsGetSchemaResponseRecordTypes",
    "RecordsGetSchemaResponseRecordTypesContract",
    "RecordsGetXlsxExportFile400Response",
    "RecordsGetXlsxExportFileResponse",
    "RecordsListAll400Response",
    "RecordsListAllResponse",
    "RecordsRemoveAttachmentResponse",
    "RecordsReplaceMetadataResponse",
    "RecordsUpdateMetadata404Response",
    "RecordsUpdateMetadataResponse",
    "RecordsUploadSmartImportRecord400Response",
    "RecordsUploadSmartImportRecord403Response",
    "RecordsUploadSmartImportRecord404Response",
    "RecordsUploadSmartImportRecordResponse",
    "RecordsUploadSmartImportRecordWithPredictions400Response",
    "RecordsUploadSmartImportRecordWithPredictions403Response",
    "RecordsUploadSmartImportRecordWithPredictions404Response",
    "RecordsUploadSmartImportRecordWithPredictionsResponse",
    "UserModel",
    "WebhookEventTypeValue",
    "WebhookInvalidEventTypeBadRequestResponse",
    "WebhookTargetUrlExistsBadRequestResponse",
    "WebhooksCreateNew400Response",
    "WebhooksCreateNewResponse",
    "WebhooksDeleteSpecific400Response",
    "WebhooksDeleteSpecificResponse",
    "WebhooksGetData400Response",
    "WebhooksGetDataResponse",
    "WebhooksGetVerificationKeyResponse",
    "WebhooksListAll400Response",
    "WebhooksListAllResponse",
    "WebhooksListAllResponseListItem",
    "WebhooksUpdateWebhookData400Response",
    "WebhooksUpdateWebhookDataResponse",
    "WorkflowAsyncInProgressResponse",
    "WorkflowAsyncLaunchFailedResponse",
    "WorkflowAsyncLaunchSuccessResponse",
    "WorkflowAsyncLaunchSuccessResponseWorkflowUrls",
    "WorkflowLastModifiedAuthorModel",
    "WorkflowLastModifiedAuthorModelCounterparty",
    "WorkflowLastModifiedAuthorModel_Counterparty",
    "WorkflowLastModifiedAuthorModel_ExternalUser",
    "WorkflowLastModifiedAuthorModel_InternalUser",
    "WorkflowNotFound",
    "WorkflowRequestModel",
    "WorkflowResponseModel",
    "WorkflowResponseModelAttributes",
    "WorkflowResponseModelAttributesDraftItem",
    "WorkflowResponseModelAttributesDraftItemLastModified",
    "WorkflowResponseModelAttributesFee",
    "WorkflowResponseModelCreator",
    "WorkflowResponseModelRolesItem",
    "WorkflowResponseModelRolesItemAssigneesItem",
    "WorkflowResponseModelSchema",
    "WorkflowResponseModelSchemaAmount",
    "WorkflowResponseModelSchemaCounterpartyName",
    "WorkflowResponseModelSchemaDraft",
    "WorkflowResponseModelSchemaDraftElementType",
    "WorkflowResponseModelSchemaFee",
    "WorkflowResponseModelSchemaLineItems",
    "WorkflowResponseModelSchemaLineItemsElementType",
    "WorkflowResponseModelSchemaLineItemsElementTypeSchema",
    "WorkflowResponseModelSchemaLineItemsElementTypeSchemaAnotherChildAttribute",
    "WorkflowResponseModelSchemaLineItemsElementTypeSchemaChildAttribute",
    "WorkflowResponseModelStatus",
    "WorkflowRoleAssigneeModel",
    "WorkflowRoleModel",
    "WorkflowStateModel",
    "WorkflowStateModelCompleted",
    "WorkflowStateModelInProgress",
    "WorkflowStateModelNotApplicable",
    "WorkflowStateModelNotStarted",
    "WorkflowStateModel_Completed",
    "WorkflowStateModel_InProgress",
    "WorkflowStateModel_NotApplicable",
    "WorkflowStateModel_NotStarted",
    "WorkflowTemplateIdModel",
    "WorkflowsCreateComment400Response",
    "WorkflowsCreateCommentResponse",
    "WorkflowsGetApprovalRequests403Response",
    "WorkflowsGetApprovalRequests404Response",
    "WorkflowsGetApprovalRequestsResponse",
    "WorkflowsGetApprovalRequestsResponseListItem",
    "WorkflowsGetAsyncJobStatus404Response",
    "WorkflowsGetAsyncJobStatusResponse",
    "WorkflowsGetAttachmentFromEmailThread404Response",
    "WorkflowsGetAttachmentFromEmailThreadResponse",
    "WorkflowsGetDocumentByKey400Response",
    "WorkflowsGetDocumentByKeyResponse",
    "WorkflowsGetEmailThreadResponse",
    "WorkflowsGetEmailThreadsResponse",
    "WorkflowsGetTurnHistory403Response",
    "WorkflowsGetTurnHistory404Response",
    "WorkflowsGetTurnHistoryResponse",
    "WorkflowsGetTurnHistoryResponseListItem",
    "WorkflowsGetWorkflowResponse",
    "WorkflowsGetWorkflowSchema400Response",
    "WorkflowsGetWorkflowSchemaResponse",
    "WorkflowsGetWorkflowSchemaResponseSchema",
    "WorkflowsGetWorkflowSchemaResponseSchemaAmount",
    "WorkflowsGetWorkflowSchemaResponseSchemaCounterpartyName",
    "WorkflowsGetWorkflowSchemaResponseSchemaDraft",
    "WorkflowsGetWorkflowSchemaResponseSchemaDraftElementType",
    "WorkflowsGetWorkflowSchemaResponseSchemaFee",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItems",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementType",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchema",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute",
    "WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaChildAttribute",
    "WorkflowsLaunchAsynchronously400Response",
    "WorkflowsLaunchAsynchronouslyResponse",
    "WorkflowsListAllParticipants403Response",
    "WorkflowsListAllParticipants404Response",
    "WorkflowsListAllParticipantsResponse",
    "WorkflowsListAllParticipantsResponseListItem",
    "WorkflowsListAllResponse",
    "WorkflowsListAllWorkflowSchemas400Response",
    "WorkflowsListAllWorkflowSchemasResponse",
    "WorkflowsListAllWorkflowSchemasResponseListItem",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchema",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaAmount",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaCounterpartyName",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaDraft",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaDraftElementType",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaFee",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItems",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementType",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchema",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaAnotherChildAttribute",
    "WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaChildAttribute",
    "WorkflowsListApprovals400Response",
    "WorkflowsListApprovalsResponse",
    "WorkflowsListApprovalsResponseApprovalGroupsItem",
    "WorkflowsListApprovalsResponseApprovalGroupsItemReviewersItem",
    "WorkflowsListApprovalsResponseRolesItem",
    "WorkflowsListApprovalsResponseRolesItemAssigneesItem",
    "WorkflowsListSignatures400Response",
    "WorkflowsListSignatures403Response",
    "WorkflowsListSignaturesResponse",
    "WorkflowsListSignaturesResponseSignersItem",
    "WorkflowsListSignaturesResponseSignersItemDelegatesItem",
    "WorkflowsRevertToReview403Response",
    "WorkflowsRevertToReview404Response",
    "WorkflowsRevertToReviewResponse",
    "WorkflowsRevertToReviewResponseCode",
    "WorkflowsRevertToReviewResponseMessage",
    "WorkflowsUpdateApprovalStatus400Response",
    "WorkflowsUpdateApprovalStatus400ResponseMessage",
    "WorkflowsUpdateApprovalStatusResponse",
    "WorkflowsUpdateMetadata400Response",
    "WorkflowsUpdateMetadata403Response",
    "WorkflowsUpdateMetadata404Response",
    "WorkflowsUpdateMetadataResponse",
    "WorkflowsUpdateMetadataResponseApprovals",
    "WorkflowsUpdateMetadataResponseAttributes",
    "WorkflowsUpdateMetadataResponseAttributesDraftItem",
    "WorkflowsUpdateMetadataResponseAttributesFee",
    "WorkflowsUpdateMetadataResponseCreator",
    "WorkflowsUpdateMetadataResponseRolesItem",
    "WorkflowsUpdateMetadataResponseRolesItemAssigneesItem",
    "WorkflowsUpdateMetadataResponseSchema",
    "WorkflowsUpdateMetadataResponseSchemaAmount",
    "WorkflowsUpdateMetadataResponseSchemaCounterpartyName",
    "WorkflowsUpdateMetadataResponseSchemaDraft",
    "WorkflowsUpdateMetadataResponseSchemaDraftElementType",
    "WorkflowsUpdateMetadataResponseSchemaFee",
    "WorkflowsUpdateMetadataResponseSchemaLineItems",
    "WorkflowsUpdateMetadataResponseSchemaLineItemsElementType",
    "WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchema",
    "WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute",
    "WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaChildAttribute",
    "WorkflowsUpdateMetadataResponseSignatures",
]
