



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .approval_requests_response import ApprovalRequestsResponse
    from .approval_requests_response_list_item import ApprovalRequestsResponseListItem
    from .create_a_new_workflow_async_response import CreateANewWorkflowAsyncResponse
    from .deprecated_create_a_comment_on_a_workflow_response import DeprecatedCreateACommentOnAWorkflowResponse
    from .list_all_workflow_approvals_response import ListAllWorkflowApprovalsResponse
    from .list_all_workflow_approvals_response_approval_groups_item import (
        ListAllWorkflowApprovalsResponseApprovalGroupsItem,
    )
    from .list_all_workflow_approvals_response_approval_groups_item_reviewers_item import (
        ListAllWorkflowApprovalsResponseApprovalGroupsItemReviewersItem,
    )
    from .list_all_workflow_approvals_response_roles_item import ListAllWorkflowApprovalsResponseRolesItem
    from .list_all_workflow_approvals_response_roles_item_assignees_item import (
        ListAllWorkflowApprovalsResponseRolesItemAssigneesItem,
    )
    from .list_all_workflow_participants_response import ListAllWorkflowParticipantsResponse
    from .list_all_workflow_participants_response_list_item import ListAllWorkflowParticipantsResponseListItem
    from .list_all_workflow_schemas_response import ListAllWorkflowSchemasResponse
    from .list_all_workflow_schemas_response_list_item import ListAllWorkflowSchemasResponseListItem
    from .list_all_workflow_schemas_response_list_item_schema import ListAllWorkflowSchemasResponseListItemSchema
    from .list_all_workflow_schemas_response_list_item_schema_amount import (
        ListAllWorkflowSchemasResponseListItemSchemaAmount,
    )
    from .list_all_workflow_schemas_response_list_item_schema_counterparty_name import (
        ListAllWorkflowSchemasResponseListItemSchemaCounterpartyName,
    )
    from .list_all_workflow_schemas_response_list_item_schema_draft import (
        ListAllWorkflowSchemasResponseListItemSchemaDraft,
    )
    from .list_all_workflow_schemas_response_list_item_schema_draft_element_type import (
        ListAllWorkflowSchemasResponseListItemSchemaDraftElementType,
    )
    from .list_all_workflow_schemas_response_list_item_schema_fee import ListAllWorkflowSchemasResponseListItemSchemaFee
    from .list_all_workflow_schemas_response_list_item_schema_line_items import (
        ListAllWorkflowSchemasResponseListItemSchemaLineItems,
    )
    from .list_all_workflow_schemas_response_list_item_schema_line_items_element_type import (
        ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementType,
    )
    from .list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema import (
        ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchema,
    )
    from .list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema_another_child_attribute import (
        ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaAnotherChildAttribute,
    )
    from .list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema_child_attribute import (
        ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaChildAttribute,
    )
    from .list_all_workflow_signers_response import ListAllWorkflowSignersResponse
    from .list_all_workflow_signers_response_signers_item import ListAllWorkflowSignersResponseSignersItem
    from .list_all_workflow_signers_response_signers_item_delegates_item import (
        ListAllWorkflowSignersResponseSignersItemDelegatesItem,
    )
    from .list_all_workflows_request_status import ListAllWorkflowsRequestStatus
    from .list_all_workflows_response import ListAllWorkflowsResponse
    from .retrieve_a_workflow_document_response import RetrieveAWorkflowDocumentResponse
    from .retrieve_a_workflow_schema_response import RetrieveAWorkflowSchemaResponse
    from .retrieve_a_workflow_schema_response_schema import RetrieveAWorkflowSchemaResponseSchema
    from .retrieve_a_workflow_schema_response_schema_amount import RetrieveAWorkflowSchemaResponseSchemaAmount
    from .retrieve_a_workflow_schema_response_schema_counterparty_name import (
        RetrieveAWorkflowSchemaResponseSchemaCounterpartyName,
    )
    from .retrieve_a_workflow_schema_response_schema_draft import RetrieveAWorkflowSchemaResponseSchemaDraft
    from .retrieve_a_workflow_schema_response_schema_draft_element_type import (
        RetrieveAWorkflowSchemaResponseSchemaDraftElementType,
    )
    from .retrieve_a_workflow_schema_response_schema_fee import RetrieveAWorkflowSchemaResponseSchemaFee
    from .retrieve_a_workflow_schema_response_schema_line_items import RetrieveAWorkflowSchemaResponseSchemaLineItems
    from .retrieve_a_workflow_schema_response_schema_line_items_element_type import (
        RetrieveAWorkflowSchemaResponseSchemaLineItemsElementType,
    )
    from .retrieve_a_workflow_schema_response_schema_line_items_element_type_schema import (
        RetrieveAWorkflowSchemaResponseSchemaLineItemsElementTypeSchema,
    )
    from .retrieve_a_workflow_schema_response_schema_line_items_element_type_schema_another_child_attribute import (
        RetrieveAWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute,
    )
    from .retrieve_a_workflow_schema_response_schema_line_items_element_type_schema_child_attribute import (
        RetrieveAWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaChildAttribute,
    )
    from .retrieve_asynchronous_workflow_status_response import RetrieveAsynchronousWorkflowStatusResponse
    from .retrieve_attachment_from_email_thread_response import RetrieveAttachmentFromEmailThreadResponse
    from .retrieve_email_threads_from_workflow_response import RetrieveEmailThreadsFromWorkflowResponse
    from .revert_to_review_request_user import RevertToReviewRequestUser
    from .turn_history_response import TurnHistoryResponse
    from .turn_history_response_list_item import TurnHistoryResponseListItem
    from .update_workflow_approval_request_status import UpdateWorkflowApprovalRequestStatus
    from .update_workflow_approval_request_user import UpdateWorkflowApprovalRequestUser
    from .update_workflow_metadata_request_updates_item import UpdateWorkflowMetadataRequestUpdatesItem
    from .update_workflow_metadata_request_updates_item_action import UpdateWorkflowMetadataRequestUpdatesItemAction
    from .update_workflow_metadata_response import UpdateWorkflowMetadataResponse
    from .update_workflow_metadata_response_approvals import UpdateWorkflowMetadataResponseApprovals
    from .update_workflow_metadata_response_attributes import UpdateWorkflowMetadataResponseAttributes
    from .update_workflow_metadata_response_attributes_draft_item import (
        UpdateWorkflowMetadataResponseAttributesDraftItem,
    )
    from .update_workflow_metadata_response_attributes_fee import UpdateWorkflowMetadataResponseAttributesFee
    from .update_workflow_metadata_response_creator import UpdateWorkflowMetadataResponseCreator
    from .update_workflow_metadata_response_roles_item import UpdateWorkflowMetadataResponseRolesItem
    from .update_workflow_metadata_response_roles_item_assignees_item import (
        UpdateWorkflowMetadataResponseRolesItemAssigneesItem,
    )
    from .update_workflow_metadata_response_schema import UpdateWorkflowMetadataResponseSchema
    from .update_workflow_metadata_response_schema_amount import UpdateWorkflowMetadataResponseSchemaAmount
    from .update_workflow_metadata_response_schema_counterparty_name import (
        UpdateWorkflowMetadataResponseSchemaCounterpartyName,
    )
    from .update_workflow_metadata_response_schema_draft import UpdateWorkflowMetadataResponseSchemaDraft
    from .update_workflow_metadata_response_schema_draft_element_type import (
        UpdateWorkflowMetadataResponseSchemaDraftElementType,
    )
    from .update_workflow_metadata_response_schema_fee import UpdateWorkflowMetadataResponseSchemaFee
    from .update_workflow_metadata_response_schema_line_items import UpdateWorkflowMetadataResponseSchemaLineItems
    from .update_workflow_metadata_response_schema_line_items_element_type import (
        UpdateWorkflowMetadataResponseSchemaLineItemsElementType,
    )
    from .update_workflow_metadata_response_schema_line_items_element_type_schema import (
        UpdateWorkflowMetadataResponseSchemaLineItemsElementTypeSchema,
    )
    from .update_workflow_metadata_response_schema_line_items_element_type_schema_another_child_attribute import (
        UpdateWorkflowMetadataResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute,
    )
    from .update_workflow_metadata_response_schema_line_items_element_type_schema_child_attribute import (
        UpdateWorkflowMetadataResponseSchemaLineItemsElementTypeSchemaChildAttribute,
    )
    from .update_workflow_metadata_response_signatures import UpdateWorkflowMetadataResponseSignatures
_dynamic_imports: typing.Dict[str, str] = {
    "ApprovalRequestsResponse": ".approval_requests_response",
    "ApprovalRequestsResponseListItem": ".approval_requests_response_list_item",
    "CreateANewWorkflowAsyncResponse": ".create_a_new_workflow_async_response",
    "DeprecatedCreateACommentOnAWorkflowResponse": ".deprecated_create_a_comment_on_a_workflow_response",
    "ListAllWorkflowApprovalsResponse": ".list_all_workflow_approvals_response",
    "ListAllWorkflowApprovalsResponseApprovalGroupsItem": ".list_all_workflow_approvals_response_approval_groups_item",
    "ListAllWorkflowApprovalsResponseApprovalGroupsItemReviewersItem": ".list_all_workflow_approvals_response_approval_groups_item_reviewers_item",
    "ListAllWorkflowApprovalsResponseRolesItem": ".list_all_workflow_approvals_response_roles_item",
    "ListAllWorkflowApprovalsResponseRolesItemAssigneesItem": ".list_all_workflow_approvals_response_roles_item_assignees_item",
    "ListAllWorkflowParticipantsResponse": ".list_all_workflow_participants_response",
    "ListAllWorkflowParticipantsResponseListItem": ".list_all_workflow_participants_response_list_item",
    "ListAllWorkflowSchemasResponse": ".list_all_workflow_schemas_response",
    "ListAllWorkflowSchemasResponseListItem": ".list_all_workflow_schemas_response_list_item",
    "ListAllWorkflowSchemasResponseListItemSchema": ".list_all_workflow_schemas_response_list_item_schema",
    "ListAllWorkflowSchemasResponseListItemSchemaAmount": ".list_all_workflow_schemas_response_list_item_schema_amount",
    "ListAllWorkflowSchemasResponseListItemSchemaCounterpartyName": ".list_all_workflow_schemas_response_list_item_schema_counterparty_name",
    "ListAllWorkflowSchemasResponseListItemSchemaDraft": ".list_all_workflow_schemas_response_list_item_schema_draft",
    "ListAllWorkflowSchemasResponseListItemSchemaDraftElementType": ".list_all_workflow_schemas_response_list_item_schema_draft_element_type",
    "ListAllWorkflowSchemasResponseListItemSchemaFee": ".list_all_workflow_schemas_response_list_item_schema_fee",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItems": ".list_all_workflow_schemas_response_list_item_schema_line_items",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementType": ".list_all_workflow_schemas_response_list_item_schema_line_items_element_type",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchema": ".list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaAnotherChildAttribute": ".list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema_another_child_attribute",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaChildAttribute": ".list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema_child_attribute",
    "ListAllWorkflowSignersResponse": ".list_all_workflow_signers_response",
    "ListAllWorkflowSignersResponseSignersItem": ".list_all_workflow_signers_response_signers_item",
    "ListAllWorkflowSignersResponseSignersItemDelegatesItem": ".list_all_workflow_signers_response_signers_item_delegates_item",
    "ListAllWorkflowsRequestStatus": ".list_all_workflows_request_status",
    "ListAllWorkflowsResponse": ".list_all_workflows_response",
    "RetrieveAWorkflowDocumentResponse": ".retrieve_a_workflow_document_response",
    "RetrieveAWorkflowSchemaResponse": ".retrieve_a_workflow_schema_response",
    "RetrieveAWorkflowSchemaResponseSchema": ".retrieve_a_workflow_schema_response_schema",
    "RetrieveAWorkflowSchemaResponseSchemaAmount": ".retrieve_a_workflow_schema_response_schema_amount",
    "RetrieveAWorkflowSchemaResponseSchemaCounterpartyName": ".retrieve_a_workflow_schema_response_schema_counterparty_name",
    "RetrieveAWorkflowSchemaResponseSchemaDraft": ".retrieve_a_workflow_schema_response_schema_draft",
    "RetrieveAWorkflowSchemaResponseSchemaDraftElementType": ".retrieve_a_workflow_schema_response_schema_draft_element_type",
    "RetrieveAWorkflowSchemaResponseSchemaFee": ".retrieve_a_workflow_schema_response_schema_fee",
    "RetrieveAWorkflowSchemaResponseSchemaLineItems": ".retrieve_a_workflow_schema_response_schema_line_items",
    "RetrieveAWorkflowSchemaResponseSchemaLineItemsElementType": ".retrieve_a_workflow_schema_response_schema_line_items_element_type",
    "RetrieveAWorkflowSchemaResponseSchemaLineItemsElementTypeSchema": ".retrieve_a_workflow_schema_response_schema_line_items_element_type_schema",
    "RetrieveAWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute": ".retrieve_a_workflow_schema_response_schema_line_items_element_type_schema_another_child_attribute",
    "RetrieveAWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaChildAttribute": ".retrieve_a_workflow_schema_response_schema_line_items_element_type_schema_child_attribute",
    "RetrieveAsynchronousWorkflowStatusResponse": ".retrieve_asynchronous_workflow_status_response",
    "RetrieveAttachmentFromEmailThreadResponse": ".retrieve_attachment_from_email_thread_response",
    "RetrieveEmailThreadsFromWorkflowResponse": ".retrieve_email_threads_from_workflow_response",
    "RevertToReviewRequestUser": ".revert_to_review_request_user",
    "TurnHistoryResponse": ".turn_history_response",
    "TurnHistoryResponseListItem": ".turn_history_response_list_item",
    "UpdateWorkflowApprovalRequestStatus": ".update_workflow_approval_request_status",
    "UpdateWorkflowApprovalRequestUser": ".update_workflow_approval_request_user",
    "UpdateWorkflowMetadataRequestUpdatesItem": ".update_workflow_metadata_request_updates_item",
    "UpdateWorkflowMetadataRequestUpdatesItemAction": ".update_workflow_metadata_request_updates_item_action",
    "UpdateWorkflowMetadataResponse": ".update_workflow_metadata_response",
    "UpdateWorkflowMetadataResponseApprovals": ".update_workflow_metadata_response_approvals",
    "UpdateWorkflowMetadataResponseAttributes": ".update_workflow_metadata_response_attributes",
    "UpdateWorkflowMetadataResponseAttributesDraftItem": ".update_workflow_metadata_response_attributes_draft_item",
    "UpdateWorkflowMetadataResponseAttributesFee": ".update_workflow_metadata_response_attributes_fee",
    "UpdateWorkflowMetadataResponseCreator": ".update_workflow_metadata_response_creator",
    "UpdateWorkflowMetadataResponseRolesItem": ".update_workflow_metadata_response_roles_item",
    "UpdateWorkflowMetadataResponseRolesItemAssigneesItem": ".update_workflow_metadata_response_roles_item_assignees_item",
    "UpdateWorkflowMetadataResponseSchema": ".update_workflow_metadata_response_schema",
    "UpdateWorkflowMetadataResponseSchemaAmount": ".update_workflow_metadata_response_schema_amount",
    "UpdateWorkflowMetadataResponseSchemaCounterpartyName": ".update_workflow_metadata_response_schema_counterparty_name",
    "UpdateWorkflowMetadataResponseSchemaDraft": ".update_workflow_metadata_response_schema_draft",
    "UpdateWorkflowMetadataResponseSchemaDraftElementType": ".update_workflow_metadata_response_schema_draft_element_type",
    "UpdateWorkflowMetadataResponseSchemaFee": ".update_workflow_metadata_response_schema_fee",
    "UpdateWorkflowMetadataResponseSchemaLineItems": ".update_workflow_metadata_response_schema_line_items",
    "UpdateWorkflowMetadataResponseSchemaLineItemsElementType": ".update_workflow_metadata_response_schema_line_items_element_type",
    "UpdateWorkflowMetadataResponseSchemaLineItemsElementTypeSchema": ".update_workflow_metadata_response_schema_line_items_element_type_schema",
    "UpdateWorkflowMetadataResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute": ".update_workflow_metadata_response_schema_line_items_element_type_schema_another_child_attribute",
    "UpdateWorkflowMetadataResponseSchemaLineItemsElementTypeSchemaChildAttribute": ".update_workflow_metadata_response_schema_line_items_element_type_schema_child_attribute",
    "UpdateWorkflowMetadataResponseSignatures": ".update_workflow_metadata_response_signatures",
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
    "ApprovalRequestsResponse",
    "ApprovalRequestsResponseListItem",
    "CreateANewWorkflowAsyncResponse",
    "DeprecatedCreateACommentOnAWorkflowResponse",
    "ListAllWorkflowApprovalsResponse",
    "ListAllWorkflowApprovalsResponseApprovalGroupsItem",
    "ListAllWorkflowApprovalsResponseApprovalGroupsItemReviewersItem",
    "ListAllWorkflowApprovalsResponseRolesItem",
    "ListAllWorkflowApprovalsResponseRolesItemAssigneesItem",
    "ListAllWorkflowParticipantsResponse",
    "ListAllWorkflowParticipantsResponseListItem",
    "ListAllWorkflowSchemasResponse",
    "ListAllWorkflowSchemasResponseListItem",
    "ListAllWorkflowSchemasResponseListItemSchema",
    "ListAllWorkflowSchemasResponseListItemSchemaAmount",
    "ListAllWorkflowSchemasResponseListItemSchemaCounterpartyName",
    "ListAllWorkflowSchemasResponseListItemSchemaDraft",
    "ListAllWorkflowSchemasResponseListItemSchemaDraftElementType",
    "ListAllWorkflowSchemasResponseListItemSchemaFee",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItems",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementType",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchema",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaAnotherChildAttribute",
    "ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchemaChildAttribute",
    "ListAllWorkflowSignersResponse",
    "ListAllWorkflowSignersResponseSignersItem",
    "ListAllWorkflowSignersResponseSignersItemDelegatesItem",
    "ListAllWorkflowsRequestStatus",
    "ListAllWorkflowsResponse",
    "RetrieveAWorkflowDocumentResponse",
    "RetrieveAWorkflowSchemaResponse",
    "RetrieveAWorkflowSchemaResponseSchema",
    "RetrieveAWorkflowSchemaResponseSchemaAmount",
    "RetrieveAWorkflowSchemaResponseSchemaCounterpartyName",
    "RetrieveAWorkflowSchemaResponseSchemaDraft",
    "RetrieveAWorkflowSchemaResponseSchemaDraftElementType",
    "RetrieveAWorkflowSchemaResponseSchemaFee",
    "RetrieveAWorkflowSchemaResponseSchemaLineItems",
    "RetrieveAWorkflowSchemaResponseSchemaLineItemsElementType",
    "RetrieveAWorkflowSchemaResponseSchemaLineItemsElementTypeSchema",
    "RetrieveAWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute",
    "RetrieveAWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaChildAttribute",
    "RetrieveAsynchronousWorkflowStatusResponse",
    "RetrieveAttachmentFromEmailThreadResponse",
    "RetrieveEmailThreadsFromWorkflowResponse",
    "RevertToReviewRequestUser",
    "TurnHistoryResponse",
    "TurnHistoryResponseListItem",
    "UpdateWorkflowApprovalRequestStatus",
    "UpdateWorkflowApprovalRequestUser",
    "UpdateWorkflowMetadataRequestUpdatesItem",
    "UpdateWorkflowMetadataRequestUpdatesItemAction",
    "UpdateWorkflowMetadataResponse",
    "UpdateWorkflowMetadataResponseApprovals",
    "UpdateWorkflowMetadataResponseAttributes",
    "UpdateWorkflowMetadataResponseAttributesDraftItem",
    "UpdateWorkflowMetadataResponseAttributesFee",
    "UpdateWorkflowMetadataResponseCreator",
    "UpdateWorkflowMetadataResponseRolesItem",
    "UpdateWorkflowMetadataResponseRolesItemAssigneesItem",
    "UpdateWorkflowMetadataResponseSchema",
    "UpdateWorkflowMetadataResponseSchemaAmount",
    "UpdateWorkflowMetadataResponseSchemaCounterpartyName",
    "UpdateWorkflowMetadataResponseSchemaDraft",
    "UpdateWorkflowMetadataResponseSchemaDraftElementType",
    "UpdateWorkflowMetadataResponseSchemaFee",
    "UpdateWorkflowMetadataResponseSchemaLineItems",
    "UpdateWorkflowMetadataResponseSchemaLineItemsElementType",
    "UpdateWorkflowMetadataResponseSchemaLineItemsElementTypeSchema",
    "UpdateWorkflowMetadataResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute",
    "UpdateWorkflowMetadataResponseSchemaLineItemsElementTypeSchemaChildAttribute",
    "UpdateWorkflowMetadataResponseSignatures",
]
