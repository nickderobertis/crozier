



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_gateway_error import BadGatewayError
    from .bandwidth_limit_exceeded_error import BandwidthLimitExceededError
    from .client_closed_request_error import ClientClosedRequestError
    from .gateway_timeout_error import GatewayTimeoutError
    from .http_version_not_supported_error import HttpVersionNotSupportedError
    from .insufficient_storage_error import InsufficientStorageError
    from .internal_server_error import InternalServerError
    from .invalid_token_error import InvalidTokenError
    from .loop_detected_error import LoopDetectedError
    from .network_authentication_required_error import NetworkAuthenticationRequiredError
    from .not_extended_error import NotExtendedError
    from .not_implemented_error import NotImplementedError
    from .service_unavailable_error import ServiceUnavailableError
    from .variant_also_negotiates_error import VariantAlsoNegotiatesError
_dynamic_imports: typing.Dict[str, str] = {
    "BadGatewayError": ".bad_gateway_error",
    "BandwidthLimitExceededError": ".bandwidth_limit_exceeded_error",
    "ClientClosedRequestError": ".client_closed_request_error",
    "GatewayTimeoutError": ".gateway_timeout_error",
    "HttpVersionNotSupportedError": ".http_version_not_supported_error",
    "InsufficientStorageError": ".insufficient_storage_error",
    "InternalServerError": ".internal_server_error",
    "InvalidTokenError": ".invalid_token_error",
    "LoopDetectedError": ".loop_detected_error",
    "NetworkAuthenticationRequiredError": ".network_authentication_required_error",
    "NotExtendedError": ".not_extended_error",
    "NotImplementedError": ".not_implemented_error",
    "ServiceUnavailableError": ".service_unavailable_error",
    "VariantAlsoNegotiatesError": ".variant_also_negotiates_error",
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
    "BadGatewayError",
    "BandwidthLimitExceededError",
    "ClientClosedRequestError",
    "GatewayTimeoutError",
    "HttpVersionNotSupportedError",
    "InsufficientStorageError",
    "InternalServerError",
    "InvalidTokenError",
    "LoopDetectedError",
    "NetworkAuthenticationRequiredError",
    "NotExtendedError",
    "NotImplementedError",
    "ServiceUnavailableError",
    "VariantAlsoNegotiatesError",
]
