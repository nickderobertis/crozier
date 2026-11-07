



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
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_code import BadRequestErrorBodyCode
    from .bad_request_error_body_message import BadRequestErrorBodyMessage
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
    from .comment_activity_model import CommentActivityModel
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
    from .forbidden_error_body import ForbiddenErrorBody
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
    from .not_found_error_body import NotFoundErrorBody
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
    from .user_model import UserModel
    from .webhook_event_type_value import WebhookEventTypeValue
    from .webhook_invalid_event_type_bad_request_response import WebhookInvalidEventTypeBadRequestResponse
    from .webhook_target_url_exists_bad_request_response import WebhookTargetUrlExistsBadRequestResponse
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
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyCode": ".bad_request_error_body_code",
    "BadRequestErrorBodyMessage": ".bad_request_error_body_message",
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
    "CommentActivityModel": ".comment_activity_model",
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
    "ForbiddenErrorBody": ".forbidden_error_body",
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
    "NotFoundErrorBody": ".not_found_error_body",
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
    "UserModel": ".user_model",
    "WebhookEventTypeValue": ".webhook_event_type_value",
    "WebhookInvalidEventTypeBadRequestResponse": ".webhook_invalid_event_type_bad_request_response",
    "WebhookTargetUrlExistsBadRequestResponse": ".webhook_target_url_exists_bad_request_response",
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
    "BadRequestErrorBody",
    "BadRequestErrorBodyCode",
    "BadRequestErrorBodyMessage",
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
    "CommentActivityModel",
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
    "ForbiddenErrorBody",
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
    "NotFoundErrorBody",
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
    "UserModel",
    "WebhookEventTypeValue",
    "WebhookInvalidEventTypeBadRequestResponse",
    "WebhookTargetUrlExistsBadRequestResponse",
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
]
