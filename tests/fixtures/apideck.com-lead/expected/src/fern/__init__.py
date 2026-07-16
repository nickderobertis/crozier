



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Address,
        AddressType,
        BadRequestResponse,
        BadRequestResponseDetail,
        BankAccount,
        BankAccountAccountType,
        CreateLeadResponse,
        Currency,
        CustomField,
        CustomFieldValue,
        DeleteLeadResponse,
        Email,
        EmailType,
        GetLeadResponse,
        GetLeadsResponse,
        Lead,
        LeadEventType,
        LeadWebhookEvent,
        LeadsFilter,
        LeadsSort,
        LeadsSortBy,
        Links,
        Meta,
        MetaCursors,
        NotFoundResponse,
        NotFoundResponseDetail,
        NotImplementedResponse,
        NotImplementedResponseDetail,
        PaymentRequiredResponse,
        PhoneNumber,
        PhoneNumberType,
        RowVersion,
        SocialLink,
        SortDirection,
        Tags,
        TooManyRequestsResponse,
        TooManyRequestsResponseDetail,
        UnauthorizedResponse,
        UnexpectedErrorResponse,
        UnexpectedErrorResponseDetail,
        UnifiedId,
        UnprocessableResponse,
        UpdateLeadResponse,
        Website,
        WebsiteType,
    )
    from .errors import (
        BadRequestError,
        NotFoundError,
        PaymentRequiredError,
        UnauthorizedError,
        UnprocessableEntityError,
    )
    from . import leads
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".types",
    "AddressType": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestResponse": ".types",
    "BadRequestResponseDetail": ".types",
    "BankAccount": ".types",
    "BankAccountAccountType": ".types",
    "CreateLeadResponse": ".types",
    "Currency": ".types",
    "CustomField": ".types",
    "CustomFieldValue": ".types",
    "DeleteLeadResponse": ".types",
    "Email": ".types",
    "EmailType": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetLeadResponse": ".types",
    "GetLeadsResponse": ".types",
    "Lead": ".types",
    "LeadEventType": ".types",
    "LeadWebhookEvent": ".types",
    "LeadsFilter": ".types",
    "LeadsSort": ".types",
    "LeadsSortBy": ".types",
    "Links": ".types",
    "Meta": ".types",
    "MetaCursors": ".types",
    "NotFoundError": ".errors",
    "NotFoundResponse": ".types",
    "NotFoundResponseDetail": ".types",
    "NotImplementedResponse": ".types",
    "NotImplementedResponseDetail": ".types",
    "PaymentRequiredError": ".errors",
    "PaymentRequiredResponse": ".types",
    "PhoneNumber": ".types",
    "PhoneNumberType": ".types",
    "RowVersion": ".types",
    "SocialLink": ".types",
    "SortDirection": ".types",
    "Tags": ".types",
    "TooManyRequestsResponse": ".types",
    "TooManyRequestsResponseDetail": ".types",
    "UnauthorizedError": ".errors",
    "UnauthorizedResponse": ".types",
    "UnexpectedErrorResponse": ".types",
    "UnexpectedErrorResponseDetail": ".types",
    "UnifiedId": ".types",
    "UnprocessableEntityError": ".errors",
    "UnprocessableResponse": ".types",
    "UpdateLeadResponse": ".types",
    "Website": ".types",
    "WebsiteType": ".types",
    "__version__": ".version",
    "leads": ".leads",
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
    "AsyncFernApi",
    "BadRequestError",
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
    "FernApi",
    "FernApiEnvironment",
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
    "NotFoundError",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PaymentRequiredError",
    "PaymentRequiredResponse",
    "PhoneNumber",
    "PhoneNumberType",
    "RowVersion",
    "SocialLink",
    "SortDirection",
    "Tags",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedError",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableEntityError",
    "UnprocessableResponse",
    "UpdateLeadResponse",
    "Website",
    "WebsiteType",
    "__version__",
    "leads",
]
