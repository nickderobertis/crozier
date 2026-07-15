



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_type import AddressType
    from .assignee import Assignee
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .collection import Collection
    from .collection_tag import CollectionTag
    from .collection_ticket_comment import CollectionTicketComment
    from .collection_user import CollectionUser
    from .collections_sort import CollectionsSort
    from .collections_sort_by import CollectionsSortBy
    from .comments_sort import CommentsSort
    from .comments_sort_by import CommentsSortBy
    from .company_id import CompanyId
    from .company_name import CompanyName
    from .create_comment_response import CreateCommentResponse
    from .create_ticket_response import CreateTicketResponse
    from .created_at import CreatedAt
    from .created_by import CreatedBy
    from .currency import Currency
    from .custom_field import CustomField
    from .custom_field_value import CustomFieldValue
    from .delete_comment_response import DeleteCommentResponse
    from .delete_ticket_response import DeleteTicketResponse
    from .department import Department
    from .description import Description
    from .division import Division
    from .email import Email
    from .email_type import EmailType
    from .first_name import FirstName
    from .gender import Gender
    from .get_collection_response import GetCollectionResponse
    from .get_collection_tags_response import GetCollectionTagsResponse
    from .get_collection_user_response import GetCollectionUserResponse
    from .get_collection_users_response import GetCollectionUsersResponse
    from .get_collections_response import GetCollectionsResponse
    from .get_comment_response import GetCommentResponse
    from .get_comments_response import GetCommentsResponse
    from .get_ticket_response import GetTicketResponse
    from .get_tickets_response import GetTicketsResponse
    from .id import Id
    from .issue_tracking_event_type import IssueTrackingEventType
    from .issue_tracking_webhook_event import IssueTrackingWebhookEvent
    from .issues_filter import IssuesFilter
    from .language import Language
    from .last_name import LastName
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .middle_name import MiddleName
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .pass_through_query import PassThroughQuery
    from .payment_required_response import PaymentRequiredResponse
    from .payment_unit import PaymentUnit
    from .phone_number import PhoneNumber
    from .phone_number_type import PhoneNumberType
    from .photo_url import PhotoUrl
    from .row_version import RowVersion
    from .sort_direction import SortDirection
    from .ticket import Ticket
    from .ticket_priority import TicketPriority
    from .tickets_sort import TicketsSort
    from .tickets_sort_by import TicketsSortBy
    from .title import Title
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_id import UnifiedId
    from .unprocessable_response import UnprocessableResponse
    from .update_comment_response import UpdateCommentResponse
    from .update_ticket_response import UpdateTicketResponse
    from .updated_at import UpdatedAt
    from .updated_by import UpdatedBy
    from .website import Website
    from .website_type import WebsiteType
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressType": ".address_type",
    "Assignee": ".assignee",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "Collection": ".collection",
    "CollectionTag": ".collection_tag",
    "CollectionTicketComment": ".collection_ticket_comment",
    "CollectionUser": ".collection_user",
    "CollectionsSort": ".collections_sort",
    "CollectionsSortBy": ".collections_sort_by",
    "CommentsSort": ".comments_sort",
    "CommentsSortBy": ".comments_sort_by",
    "CompanyId": ".company_id",
    "CompanyName": ".company_name",
    "CreateCommentResponse": ".create_comment_response",
    "CreateTicketResponse": ".create_ticket_response",
    "CreatedAt": ".created_at",
    "CreatedBy": ".created_by",
    "Currency": ".currency",
    "CustomField": ".custom_field",
    "CustomFieldValue": ".custom_field_value",
    "DeleteCommentResponse": ".delete_comment_response",
    "DeleteTicketResponse": ".delete_ticket_response",
    "Department": ".department",
    "Description": ".description",
    "Division": ".division",
    "Email": ".email",
    "EmailType": ".email_type",
    "FirstName": ".first_name",
    "Gender": ".gender",
    "GetCollectionResponse": ".get_collection_response",
    "GetCollectionTagsResponse": ".get_collection_tags_response",
    "GetCollectionUserResponse": ".get_collection_user_response",
    "GetCollectionUsersResponse": ".get_collection_users_response",
    "GetCollectionsResponse": ".get_collections_response",
    "GetCommentResponse": ".get_comment_response",
    "GetCommentsResponse": ".get_comments_response",
    "GetTicketResponse": ".get_ticket_response",
    "GetTicketsResponse": ".get_tickets_response",
    "Id": ".id",
    "IssueTrackingEventType": ".issue_tracking_event_type",
    "IssueTrackingWebhookEvent": ".issue_tracking_webhook_event",
    "IssuesFilter": ".issues_filter",
    "Language": ".language",
    "LastName": ".last_name",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "MiddleName": ".middle_name",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "PassThroughQuery": ".pass_through_query",
    "PaymentRequiredResponse": ".payment_required_response",
    "PaymentUnit": ".payment_unit",
    "PhoneNumber": ".phone_number",
    "PhoneNumberType": ".phone_number_type",
    "PhotoUrl": ".photo_url",
    "RowVersion": ".row_version",
    "SortDirection": ".sort_direction",
    "Ticket": ".ticket",
    "TicketPriority": ".ticket_priority",
    "TicketsSort": ".tickets_sort",
    "TicketsSortBy": ".tickets_sort_by",
    "Title": ".title",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedId": ".unified_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateCommentResponse": ".update_comment_response",
    "UpdateTicketResponse": ".update_ticket_response",
    "UpdatedAt": ".updated_at",
    "UpdatedBy": ".updated_by",
    "Website": ".website",
    "WebsiteType": ".website_type",
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
    "Address",
    "AddressType",
    "Assignee",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "Collection",
    "CollectionTag",
    "CollectionTicketComment",
    "CollectionUser",
    "CollectionsSort",
    "CollectionsSortBy",
    "CommentsSort",
    "CommentsSortBy",
    "CompanyId",
    "CompanyName",
    "CreateCommentResponse",
    "CreateTicketResponse",
    "CreatedAt",
    "CreatedBy",
    "Currency",
    "CustomField",
    "CustomFieldValue",
    "DeleteCommentResponse",
    "DeleteTicketResponse",
    "Department",
    "Description",
    "Division",
    "Email",
    "EmailType",
    "FirstName",
    "Gender",
    "GetCollectionResponse",
    "GetCollectionTagsResponse",
    "GetCollectionUserResponse",
    "GetCollectionUsersResponse",
    "GetCollectionsResponse",
    "GetCommentResponse",
    "GetCommentsResponse",
    "GetTicketResponse",
    "GetTicketsResponse",
    "Id",
    "IssueTrackingEventType",
    "IssueTrackingWebhookEvent",
    "IssuesFilter",
    "Language",
    "LastName",
    "Links",
    "Meta",
    "MetaCursors",
    "MiddleName",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PassThroughQuery",
    "PaymentRequiredResponse",
    "PaymentUnit",
    "PhoneNumber",
    "PhoneNumberType",
    "PhotoUrl",
    "RowVersion",
    "SortDirection",
    "Ticket",
    "TicketPriority",
    "TicketsSort",
    "TicketsSortBy",
    "Title",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableResponse",
    "UpdateCommentResponse",
    "UpdateTicketResponse",
    "UpdatedAt",
    "UpdatedBy",
    "Website",
    "WebsiteType",
]
