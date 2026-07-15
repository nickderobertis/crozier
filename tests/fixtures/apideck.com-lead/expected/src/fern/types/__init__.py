



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_type import AddressType
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .bank_account import BankAccount
    from .bank_account_account_type import BankAccountAccountType
    from .create_lead_response import CreateLeadResponse
    from .currency import Currency
    from .custom_field import CustomField
    from .custom_field_value import CustomFieldValue
    from .delete_lead_response import DeleteLeadResponse
    from .email import Email
    from .email_type import EmailType
    from .get_lead_response import GetLeadResponse
    from .get_leads_response import GetLeadsResponse
    from .lead import Lead
    from .lead_event_type import LeadEventType
    from .lead_webhook_event import LeadWebhookEvent
    from .leads_filter import LeadsFilter
    from .leads_sort import LeadsSort
    from .leads_sort_by import LeadsSortBy
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .payment_required_response import PaymentRequiredResponse
    from .phone_number import PhoneNumber
    from .phone_number_type import PhoneNumberType
    from .row_version import RowVersion
    from .social_link import SocialLink
    from .sort_direction import SortDirection
    from .tags import Tags
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_id import UnifiedId
    from .unprocessable_response import UnprocessableResponse
    from .update_lead_response import UpdateLeadResponse
    from .website import Website
    from .website_type import WebsiteType
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressType": ".address_type",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "BankAccount": ".bank_account",
    "BankAccountAccountType": ".bank_account_account_type",
    "CreateLeadResponse": ".create_lead_response",
    "Currency": ".currency",
    "CustomField": ".custom_field",
    "CustomFieldValue": ".custom_field_value",
    "DeleteLeadResponse": ".delete_lead_response",
    "Email": ".email",
    "EmailType": ".email_type",
    "GetLeadResponse": ".get_lead_response",
    "GetLeadsResponse": ".get_leads_response",
    "Lead": ".lead",
    "LeadEventType": ".lead_event_type",
    "LeadWebhookEvent": ".lead_webhook_event",
    "LeadsFilter": ".leads_filter",
    "LeadsSort": ".leads_sort",
    "LeadsSortBy": ".leads_sort_by",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "PaymentRequiredResponse": ".payment_required_response",
    "PhoneNumber": ".phone_number",
    "PhoneNumberType": ".phone_number_type",
    "RowVersion": ".row_version",
    "SocialLink": ".social_link",
    "SortDirection": ".sort_direction",
    "Tags": ".tags",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedId": ".unified_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateLeadResponse": ".update_lead_response",
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
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "BankAccount",
    "BankAccountAccountType",
    "CreateLeadResponse",
    "Currency",
    "CustomField",
    "CustomFieldValue",
    "DeleteLeadResponse",
    "Email",
    "EmailType",
    "GetLeadResponse",
    "GetLeadsResponse",
    "Lead",
    "LeadEventType",
    "LeadWebhookEvent",
    "LeadsFilter",
    "LeadsSort",
    "LeadsSortBy",
    "Links",
    "Meta",
    "MetaCursors",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PaymentRequiredResponse",
    "PhoneNumber",
    "PhoneNumberType",
    "RowVersion",
    "SocialLink",
    "SortDirection",
    "Tags",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableResponse",
    "UpdateLeadResponse",
    "Website",
    "WebsiteType",
]
