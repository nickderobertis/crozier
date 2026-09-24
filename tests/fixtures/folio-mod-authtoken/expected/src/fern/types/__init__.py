



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .refresh_token import RefreshToken
    from .sign_token_payload import SignTokenPayload
    from .sign_token_payload_payload import SignTokenPayloadPayload
    from .token import Token
    from .token_response import TokenResponse
    from .token_response_legacy import TokenResponseLegacy
_dynamic_imports: typing.Dict[str, str] = {
    "RefreshToken": ".refresh_token",
    "SignTokenPayload": ".sign_token_payload",
    "SignTokenPayloadPayload": ".sign_token_payload_payload",
    "Token": ".token",
    "TokenResponse": ".token_response",
    "TokenResponseLegacy": ".token_response_legacy",
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
    "RefreshToken",
    "SignTokenPayload",
    "SignTokenPayloadPayload",
    "Token",
    "TokenResponse",
    "TokenResponseLegacy",
]
