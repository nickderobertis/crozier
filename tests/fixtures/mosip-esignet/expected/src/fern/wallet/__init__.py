



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostAuthorizationLinkTransactionRequestRequest,
        PostAuthorizationLinkTransactionResponse,
        PostAuthorizationLinkTransactionResponseErrorsItem,
        PostAuthorizationLinkTransactionResponseErrorsItemErrorCode,
        PostAuthorizationLinkTransactionResponseResponse,
        PostAuthorizationLinkTransactionV2RequestRequest,
        PostAuthorizationLinkTransactionV2Response,
        PostAuthorizationLinkTransactionV2ResponseErrorsItem,
        PostAuthorizationLinkTransactionV2ResponseErrorsItemErrorCode,
        PostAuthorizationLinkTransactionV2ResponseResponse,
        PostLinkedAuthenticateRequestRequest,
        PostLinkedAuthenticateResponse,
        PostLinkedAuthenticateResponseErrorsItem,
        PostLinkedAuthenticateResponseErrorsItemErrorCode,
        PostLinkedAuthenticateResponseResponse,
        PostLinkedAuthenticateV2RequestRequest,
        PostLinkedAuthenticateV2Response,
        PostLinkedAuthenticateV2ResponseErrorsItem,
        PostLinkedAuthenticateV2ResponseErrorsItemErrorCode,
        PostLinkedAuthenticateV2ResponseResponse,
        PostLinkedAuthenticateV2ResponseResponseConsentAction,
        PostLinkedConsentRequestRequest,
        PostLinkedConsentResponse,
        PostLinkedConsentResponseErrorsItem,
        PostLinkedConsentResponseErrorsItemErrorCode,
        PostLinkedConsentResponseResponse,
        PostLinkedConsentV2RequestRequest,
        PostLinkedConsentV2Response,
        PostLinkedConsentV2ResponseErrorsItem,
        PostLinkedConsentV2ResponseErrorsItemErrorCode,
        PostLinkedConsentV2ResponseResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostAuthorizationLinkTransactionRequestRequest": ".types",
    "PostAuthorizationLinkTransactionResponse": ".types",
    "PostAuthorizationLinkTransactionResponseErrorsItem": ".types",
    "PostAuthorizationLinkTransactionResponseErrorsItemErrorCode": ".types",
    "PostAuthorizationLinkTransactionResponseResponse": ".types",
    "PostAuthorizationLinkTransactionV2RequestRequest": ".types",
    "PostAuthorizationLinkTransactionV2Response": ".types",
    "PostAuthorizationLinkTransactionV2ResponseErrorsItem": ".types",
    "PostAuthorizationLinkTransactionV2ResponseErrorsItemErrorCode": ".types",
    "PostAuthorizationLinkTransactionV2ResponseResponse": ".types",
    "PostLinkedAuthenticateRequestRequest": ".types",
    "PostLinkedAuthenticateResponse": ".types",
    "PostLinkedAuthenticateResponseErrorsItem": ".types",
    "PostLinkedAuthenticateResponseErrorsItemErrorCode": ".types",
    "PostLinkedAuthenticateResponseResponse": ".types",
    "PostLinkedAuthenticateV2RequestRequest": ".types",
    "PostLinkedAuthenticateV2Response": ".types",
    "PostLinkedAuthenticateV2ResponseErrorsItem": ".types",
    "PostLinkedAuthenticateV2ResponseErrorsItemErrorCode": ".types",
    "PostLinkedAuthenticateV2ResponseResponse": ".types",
    "PostLinkedAuthenticateV2ResponseResponseConsentAction": ".types",
    "PostLinkedConsentRequestRequest": ".types",
    "PostLinkedConsentResponse": ".types",
    "PostLinkedConsentResponseErrorsItem": ".types",
    "PostLinkedConsentResponseErrorsItemErrorCode": ".types",
    "PostLinkedConsentResponseResponse": ".types",
    "PostLinkedConsentV2RequestRequest": ".types",
    "PostLinkedConsentV2Response": ".types",
    "PostLinkedConsentV2ResponseErrorsItem": ".types",
    "PostLinkedConsentV2ResponseErrorsItemErrorCode": ".types",
    "PostLinkedConsentV2ResponseResponse": ".types",
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
    "PostAuthorizationLinkTransactionRequestRequest",
    "PostAuthorizationLinkTransactionResponse",
    "PostAuthorizationLinkTransactionResponseErrorsItem",
    "PostAuthorizationLinkTransactionResponseErrorsItemErrorCode",
    "PostAuthorizationLinkTransactionResponseResponse",
    "PostAuthorizationLinkTransactionV2RequestRequest",
    "PostAuthorizationLinkTransactionV2Response",
    "PostAuthorizationLinkTransactionV2ResponseErrorsItem",
    "PostAuthorizationLinkTransactionV2ResponseErrorsItemErrorCode",
    "PostAuthorizationLinkTransactionV2ResponseResponse",
    "PostLinkedAuthenticateRequestRequest",
    "PostLinkedAuthenticateResponse",
    "PostLinkedAuthenticateResponseErrorsItem",
    "PostLinkedAuthenticateResponseErrorsItemErrorCode",
    "PostLinkedAuthenticateResponseResponse",
    "PostLinkedAuthenticateV2RequestRequest",
    "PostLinkedAuthenticateV2Response",
    "PostLinkedAuthenticateV2ResponseErrorsItem",
    "PostLinkedAuthenticateV2ResponseErrorsItemErrorCode",
    "PostLinkedAuthenticateV2ResponseResponse",
    "PostLinkedAuthenticateV2ResponseResponseConsentAction",
    "PostLinkedConsentRequestRequest",
    "PostLinkedConsentResponse",
    "PostLinkedConsentResponseErrorsItem",
    "PostLinkedConsentResponseErrorsItemErrorCode",
    "PostLinkedConsentResponseResponse",
    "PostLinkedConsentV2RequestRequest",
    "PostLinkedConsentV2Response",
    "PostLinkedConsentV2ResponseErrorsItem",
    "PostLinkedConsentV2ResponseErrorsItemErrorCode",
    "PostLinkedConsentV2ResponseResponse",
]
