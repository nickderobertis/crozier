



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .credential_requests_peek_response import CredentialRequestsPeekResponse
    from .credential_requests_peek_response_error import CredentialRequestsPeekResponseError
    from .credential_requests_peek_response_error_error import CredentialRequestsPeekResponseErrorError
    from .credential_requests_peek_response_error_error_code import CredentialRequestsPeekResponseErrorErrorCode
    from .credential_requests_peek_response_expires_at import CredentialRequestsPeekResponseExpiresAt
    from .credential_requests_submit_response import CredentialRequestsSubmitResponse
    from .credential_requests_submit_response_error import CredentialRequestsSubmitResponseError
    from .credential_requests_submit_response_error_error import CredentialRequestsSubmitResponseErrorError
    from .credential_requests_submit_response_error_error_code import CredentialRequestsSubmitResponseErrorErrorCode
    from .credential_requests_submit_response_ok import CredentialRequestsSubmitResponseOk
_dynamic_imports: typing.Dict[str, str] = {
    "CredentialRequestsPeekResponse": ".credential_requests_peek_response",
    "CredentialRequestsPeekResponseError": ".credential_requests_peek_response_error",
    "CredentialRequestsPeekResponseErrorError": ".credential_requests_peek_response_error_error",
    "CredentialRequestsPeekResponseErrorErrorCode": ".credential_requests_peek_response_error_error_code",
    "CredentialRequestsPeekResponseExpiresAt": ".credential_requests_peek_response_expires_at",
    "CredentialRequestsSubmitResponse": ".credential_requests_submit_response",
    "CredentialRequestsSubmitResponseError": ".credential_requests_submit_response_error",
    "CredentialRequestsSubmitResponseErrorError": ".credential_requests_submit_response_error_error",
    "CredentialRequestsSubmitResponseErrorErrorCode": ".credential_requests_submit_response_error_error_code",
    "CredentialRequestsSubmitResponseOk": ".credential_requests_submit_response_ok",
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
    "CredentialRequestsPeekResponse",
    "CredentialRequestsPeekResponseError",
    "CredentialRequestsPeekResponseErrorError",
    "CredentialRequestsPeekResponseErrorErrorCode",
    "CredentialRequestsPeekResponseExpiresAt",
    "CredentialRequestsSubmitResponse",
    "CredentialRequestsSubmitResponseError",
    "CredentialRequestsSubmitResponseErrorError",
    "CredentialRequestsSubmitResponseErrorErrorCode",
    "CredentialRequestsSubmitResponseOk",
]
