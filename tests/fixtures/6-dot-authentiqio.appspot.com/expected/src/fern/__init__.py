



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import AuthentiqId, Claims, Error, PushToken
    from .errors import (
        ConflictError,
        GoneError,
        MethodNotAllowedError,
        NotFoundError,
        TooManyRequestsError,
        UnauthorizedError,
    )
    from . import key, login, scope
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .key import (
        KeyBindResponse,
        KeyRegisterResponse,
        KeyRetrieveResponse,
        KeyRevokeNosecretResponse,
        KeyRevokeResponse,
        KeyUpdateResponse,
    )
    from .login import PushLoginRequestResponse
    from .scope import SignConfirmResponse, SignDeleteResponse, SignRequestResponse, SignRetrieveResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "AuthentiqId": ".types",
    "Claims": ".types",
    "ConflictError": ".errors",
    "Error": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GoneError": ".errors",
    "KeyBindResponse": ".key",
    "KeyRegisterResponse": ".key",
    "KeyRetrieveResponse": ".key",
    "KeyRevokeNosecretResponse": ".key",
    "KeyRevokeResponse": ".key",
    "KeyUpdateResponse": ".key",
    "MethodNotAllowedError": ".errors",
    "NotFoundError": ".errors",
    "PushLoginRequestResponse": ".login",
    "PushToken": ".types",
    "SignConfirmResponse": ".scope",
    "SignDeleteResponse": ".scope",
    "SignRequestResponse": ".scope",
    "SignRetrieveResponse": ".scope",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "key": ".key",
    "login": ".login",
    "scope": ".scope",
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
    "AsyncFernApi",
    "AuthentiqId",
    "Claims",
    "ConflictError",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "GoneError",
    "KeyBindResponse",
    "KeyRegisterResponse",
    "KeyRetrieveResponse",
    "KeyRevokeNosecretResponse",
    "KeyRevokeResponse",
    "KeyUpdateResponse",
    "MethodNotAllowedError",
    "NotFoundError",
    "PushLoginRequestResponse",
    "PushToken",
    "SignConfirmResponse",
    "SignDeleteResponse",
    "SignRequestResponse",
    "SignRetrieveResponse",
    "TooManyRequestsError",
    "UnauthorizedError",
    "__version__",
    "key",
    "login",
    "scope",
]
