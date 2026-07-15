



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_type import AddressType
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .bank_account import BankAccount
    from .bank_account_account_type import BankAccountAccountType
    from .company import Company
    from .company_name import CompanyName
    from .company_row_type import CompanyRowType
    from .contact import Contact
    from .contact_gender import ContactGender
    from .contact_type import ContactType
    from .create_customer_support_customer_response import CreateCustomerSupportCustomerResponse
    from .currency import Currency
    from .custom_field import CustomField
    from .custom_field_value import CustomFieldValue
    from .customer_support_customer import CustomerSupportCustomer
    from .customer_support_customer_status import CustomerSupportCustomerStatus
    from .delete_customer_support_customer_response import DeleteCustomerSupportCustomerResponse
    from .email import Email
    from .email_type import EmailType
    from .first_name import FirstName
    from .get_customer_support_customer_response import GetCustomerSupportCustomerResponse
    from .get_customer_support_customers_response import GetCustomerSupportCustomersResponse
    from .last_name import LastName
    from .lead import Lead
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .opportunity import Opportunity
    from .payment_required_response import PaymentRequiredResponse
    from .phone_number import PhoneNumber
    from .phone_number_type import PhoneNumberType
    from .row_version import RowVersion
    from .social_link import SocialLink
    from .tags import Tags
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_id import UnifiedId
    from .unprocessable_response import UnprocessableResponse
    from .update_customer_support_customer_response import UpdateCustomerSupportCustomerResponse
    from .website import Website
    from .website_type import WebsiteType
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressType": ".address_type",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "BankAccount": ".bank_account",
    "BankAccountAccountType": ".bank_account_account_type",
    "Company": ".company",
    "CompanyName": ".company_name",
    "CompanyRowType": ".company_row_type",
    "Contact": ".contact",
    "ContactGender": ".contact_gender",
    "ContactType": ".contact_type",
    "CreateCustomerSupportCustomerResponse": ".create_customer_support_customer_response",
    "Currency": ".currency",
    "CustomField": ".custom_field",
    "CustomFieldValue": ".custom_field_value",
    "CustomerSupportCustomer": ".customer_support_customer",
    "CustomerSupportCustomerStatus": ".customer_support_customer_status",
    "DeleteCustomerSupportCustomerResponse": ".delete_customer_support_customer_response",
    "Email": ".email",
    "EmailType": ".email_type",
    "FirstName": ".first_name",
    "GetCustomerSupportCustomerResponse": ".get_customer_support_customer_response",
    "GetCustomerSupportCustomersResponse": ".get_customer_support_customers_response",
    "LastName": ".last_name",
    "Lead": ".lead",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "Opportunity": ".opportunity",
    "PaymentRequiredResponse": ".payment_required_response",
    "PhoneNumber": ".phone_number",
    "PhoneNumberType": ".phone_number_type",
    "RowVersion": ".row_version",
    "SocialLink": ".social_link",
    "Tags": ".tags",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedId": ".unified_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateCustomerSupportCustomerResponse": ".update_customer_support_customer_response",
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
    "Company",
    "CompanyName",
    "CompanyRowType",
    "Contact",
    "ContactGender",
    "ContactType",
    "CreateCustomerSupportCustomerResponse",
    "Currency",
    "CustomField",
    "CustomFieldValue",
    "CustomerSupportCustomer",
    "CustomerSupportCustomerStatus",
    "DeleteCustomerSupportCustomerResponse",
    "Email",
    "EmailType",
    "FirstName",
    "GetCustomerSupportCustomerResponse",
    "GetCustomerSupportCustomersResponse",
    "LastName",
    "Lead",
    "Links",
    "Meta",
    "MetaCursors",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "Opportunity",
    "PaymentRequiredResponse",
    "PhoneNumber",
    "PhoneNumberType",
    "RowVersion",
    "SocialLink",
    "Tags",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableResponse",
    "UpdateCustomerSupportCustomerResponse",
    "Website",
    "WebsiteType",
]
