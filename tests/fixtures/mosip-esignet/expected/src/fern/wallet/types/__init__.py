



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_authorization_link_transaction_request_request import PostAuthorizationLinkTransactionRequestRequest
    from .post_authorization_link_transaction_response import PostAuthorizationLinkTransactionResponse
    from .post_authorization_link_transaction_response_errors_item import (
        PostAuthorizationLinkTransactionResponseErrorsItem,
    )
    from .post_authorization_link_transaction_response_errors_item_error_code import (
        PostAuthorizationLinkTransactionResponseErrorsItemErrorCode,
    )
    from .post_authorization_link_transaction_response_response import PostAuthorizationLinkTransactionResponseResponse
    from .post_authorization_link_transaction_v2request_request import PostAuthorizationLinkTransactionV2RequestRequest
    from .post_authorization_link_transaction_v2response import PostAuthorizationLinkTransactionV2Response
    from .post_authorization_link_transaction_v2response_errors_item import (
        PostAuthorizationLinkTransactionV2ResponseErrorsItem,
    )
    from .post_authorization_link_transaction_v2response_errors_item_error_code import (
        PostAuthorizationLinkTransactionV2ResponseErrorsItemErrorCode,
    )
    from .post_authorization_link_transaction_v2response_response import (
        PostAuthorizationLinkTransactionV2ResponseResponse,
    )
    from .post_linked_authenticate_request_request import PostLinkedAuthenticateRequestRequest
    from .post_linked_authenticate_response import PostLinkedAuthenticateResponse
    from .post_linked_authenticate_response_errors_item import PostLinkedAuthenticateResponseErrorsItem
    from .post_linked_authenticate_response_errors_item_error_code import (
        PostLinkedAuthenticateResponseErrorsItemErrorCode,
    )
    from .post_linked_authenticate_response_response import PostLinkedAuthenticateResponseResponse
    from .post_linked_authenticate_v2request_request import PostLinkedAuthenticateV2RequestRequest
    from .post_linked_authenticate_v2response import PostLinkedAuthenticateV2Response
    from .post_linked_authenticate_v2response_errors_item import PostLinkedAuthenticateV2ResponseErrorsItem
    from .post_linked_authenticate_v2response_errors_item_error_code import (
        PostLinkedAuthenticateV2ResponseErrorsItemErrorCode,
    )
    from .post_linked_authenticate_v2response_response import PostLinkedAuthenticateV2ResponseResponse
    from .post_linked_authenticate_v2response_response_consent_action import (
        PostLinkedAuthenticateV2ResponseResponseConsentAction,
    )
    from .post_linked_consent_request_request import PostLinkedConsentRequestRequest
    from .post_linked_consent_response import PostLinkedConsentResponse
    from .post_linked_consent_response_errors_item import PostLinkedConsentResponseErrorsItem
    from .post_linked_consent_response_errors_item_error_code import PostLinkedConsentResponseErrorsItemErrorCode
    from .post_linked_consent_response_response import PostLinkedConsentResponseResponse
    from .post_linked_consent_v2request_request import PostLinkedConsentV2RequestRequest
    from .post_linked_consent_v2response import PostLinkedConsentV2Response
    from .post_linked_consent_v2response_errors_item import PostLinkedConsentV2ResponseErrorsItem
    from .post_linked_consent_v2response_errors_item_error_code import PostLinkedConsentV2ResponseErrorsItemErrorCode
    from .post_linked_consent_v2response_response import PostLinkedConsentV2ResponseResponse
_dynamic_imports: typing.Dict[str, str] = {
    "PostAuthorizationLinkTransactionRequestRequest": ".post_authorization_link_transaction_request_request",
    "PostAuthorizationLinkTransactionResponse": ".post_authorization_link_transaction_response",
    "PostAuthorizationLinkTransactionResponseErrorsItem": ".post_authorization_link_transaction_response_errors_item",
    "PostAuthorizationLinkTransactionResponseErrorsItemErrorCode": ".post_authorization_link_transaction_response_errors_item_error_code",
    "PostAuthorizationLinkTransactionResponseResponse": ".post_authorization_link_transaction_response_response",
    "PostAuthorizationLinkTransactionV2RequestRequest": ".post_authorization_link_transaction_v2request_request",
    "PostAuthorizationLinkTransactionV2Response": ".post_authorization_link_transaction_v2response",
    "PostAuthorizationLinkTransactionV2ResponseErrorsItem": ".post_authorization_link_transaction_v2response_errors_item",
    "PostAuthorizationLinkTransactionV2ResponseErrorsItemErrorCode": ".post_authorization_link_transaction_v2response_errors_item_error_code",
    "PostAuthorizationLinkTransactionV2ResponseResponse": ".post_authorization_link_transaction_v2response_response",
    "PostLinkedAuthenticateRequestRequest": ".post_linked_authenticate_request_request",
    "PostLinkedAuthenticateResponse": ".post_linked_authenticate_response",
    "PostLinkedAuthenticateResponseErrorsItem": ".post_linked_authenticate_response_errors_item",
    "PostLinkedAuthenticateResponseErrorsItemErrorCode": ".post_linked_authenticate_response_errors_item_error_code",
    "PostLinkedAuthenticateResponseResponse": ".post_linked_authenticate_response_response",
    "PostLinkedAuthenticateV2RequestRequest": ".post_linked_authenticate_v2request_request",
    "PostLinkedAuthenticateV2Response": ".post_linked_authenticate_v2response",
    "PostLinkedAuthenticateV2ResponseErrorsItem": ".post_linked_authenticate_v2response_errors_item",
    "PostLinkedAuthenticateV2ResponseErrorsItemErrorCode": ".post_linked_authenticate_v2response_errors_item_error_code",
    "PostLinkedAuthenticateV2ResponseResponse": ".post_linked_authenticate_v2response_response",
    "PostLinkedAuthenticateV2ResponseResponseConsentAction": ".post_linked_authenticate_v2response_response_consent_action",
    "PostLinkedConsentRequestRequest": ".post_linked_consent_request_request",
    "PostLinkedConsentResponse": ".post_linked_consent_response",
    "PostLinkedConsentResponseErrorsItem": ".post_linked_consent_response_errors_item",
    "PostLinkedConsentResponseErrorsItemErrorCode": ".post_linked_consent_response_errors_item_error_code",
    "PostLinkedConsentResponseResponse": ".post_linked_consent_response_response",
    "PostLinkedConsentV2RequestRequest": ".post_linked_consent_v2request_request",
    "PostLinkedConsentV2Response": ".post_linked_consent_v2response",
    "PostLinkedConsentV2ResponseErrorsItem": ".post_linked_consent_v2response_errors_item",
    "PostLinkedConsentV2ResponseErrorsItemErrorCode": ".post_linked_consent_v2response_errors_item_error_code",
    "PostLinkedConsentV2ResponseResponse": ".post_linked_consent_v2response_response",
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
