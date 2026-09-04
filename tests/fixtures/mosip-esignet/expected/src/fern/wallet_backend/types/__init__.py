



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_binding_otp_request_request import PostBindingOtpRequestRequest
    from .post_binding_otp_response import PostBindingOtpResponse
    from .post_binding_otp_response_errors_item import PostBindingOtpResponseErrorsItem
    from .post_binding_otp_response_errors_item_error_code import PostBindingOtpResponseErrorsItemErrorCode
    from .post_binding_otp_response_response import PostBindingOtpResponseResponse
    from .post_binding_otp_v2request_request import PostBindingOtpV2RequestRequest
    from .post_binding_otp_v2response import PostBindingOtpV2Response
    from .post_binding_otp_v2response_errors_item import PostBindingOtpV2ResponseErrorsItem
    from .post_binding_otp_v2response_errors_item_error_code import PostBindingOtpV2ResponseErrorsItemErrorCode
    from .post_binding_otp_v2response_response import PostBindingOtpV2ResponseResponse
    from .post_wallet_binding_request_request import PostWalletBindingRequestRequest
    from .post_wallet_binding_response import PostWalletBindingResponse
    from .post_wallet_binding_response_errors_item import PostWalletBindingResponseErrorsItem
    from .post_wallet_binding_response_errors_item_error_code import PostWalletBindingResponseErrorsItemErrorCode
    from .post_wallet_binding_response_response import PostWalletBindingResponseResponse
_dynamic_imports: typing.Dict[str, str] = {
    "PostBindingOtpRequestRequest": ".post_binding_otp_request_request",
    "PostBindingOtpResponse": ".post_binding_otp_response",
    "PostBindingOtpResponseErrorsItem": ".post_binding_otp_response_errors_item",
    "PostBindingOtpResponseErrorsItemErrorCode": ".post_binding_otp_response_errors_item_error_code",
    "PostBindingOtpResponseResponse": ".post_binding_otp_response_response",
    "PostBindingOtpV2RequestRequest": ".post_binding_otp_v2request_request",
    "PostBindingOtpV2Response": ".post_binding_otp_v2response",
    "PostBindingOtpV2ResponseErrorsItem": ".post_binding_otp_v2response_errors_item",
    "PostBindingOtpV2ResponseErrorsItemErrorCode": ".post_binding_otp_v2response_errors_item_error_code",
    "PostBindingOtpV2ResponseResponse": ".post_binding_otp_v2response_response",
    "PostWalletBindingRequestRequest": ".post_wallet_binding_request_request",
    "PostWalletBindingResponse": ".post_wallet_binding_response",
    "PostWalletBindingResponseErrorsItem": ".post_wallet_binding_response_errors_item",
    "PostWalletBindingResponseErrorsItemErrorCode": ".post_wallet_binding_response_errors_item_error_code",
    "PostWalletBindingResponseResponse": ".post_wallet_binding_response_response",
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
    "PostBindingOtpRequestRequest",
    "PostBindingOtpResponse",
    "PostBindingOtpResponseErrorsItem",
    "PostBindingOtpResponseErrorsItemErrorCode",
    "PostBindingOtpResponseResponse",
    "PostBindingOtpV2RequestRequest",
    "PostBindingOtpV2Response",
    "PostBindingOtpV2ResponseErrorsItem",
    "PostBindingOtpV2ResponseErrorsItemErrorCode",
    "PostBindingOtpV2ResponseResponse",
    "PostWalletBindingRequestRequest",
    "PostWalletBindingResponse",
    "PostWalletBindingResponseErrorsItem",
    "PostWalletBindingResponseErrorsItemErrorCode",
    "PostWalletBindingResponseResponse",
]
