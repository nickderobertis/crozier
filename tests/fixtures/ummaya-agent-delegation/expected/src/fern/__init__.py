



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ConsentRecord,
        ConsentRequest,
        DelegationToken,
        DelegationTokenAalAsserted,
        DelegationTokenTokenType,
        Error,
        IntrospectionRequest,
        IntrospectionRequestTokenTypeHint,
        IntrospectionResponse,
        IntrospectionResponseAalAsserted,
        RevocationRequest,
        RevocationRequestTokenTypeHint,
        TokenRequest,
        TokenRequestGrantType,
    )
    from .errors import BadRequestError, UnauthorizedError
    from . import consent, introspection, revocation, token
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConsentRecord": ".types",
    "ConsentRequest": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DelegationToken": ".types",
    "DelegationTokenAalAsserted": ".types",
    "DelegationTokenTokenType": ".types",
    "Error": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "IntrospectionRequest": ".types",
    "IntrospectionRequestTokenTypeHint": ".types",
    "IntrospectionResponse": ".types",
    "IntrospectionResponseAalAsserted": ".types",
    "RevocationRequest": ".types",
    "RevocationRequestTokenTypeHint": ".types",
    "TokenRequest": ".types",
    "TokenRequestGrantType": ".types",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "consent": ".consent",
    "introspection": ".introspection",
    "revocation": ".revocation",
    "token": ".token",
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
    "BadRequestError",
    "ConsentRecord",
    "ConsentRequest",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DelegationToken",
    "DelegationTokenAalAsserted",
    "DelegationTokenTokenType",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "IntrospectionRequest",
    "IntrospectionRequestTokenTypeHint",
    "IntrospectionResponse",
    "IntrospectionResponseAalAsserted",
    "RevocationRequest",
    "RevocationRequestTokenTypeHint",
    "TokenRequest",
    "TokenRequestGrantType",
    "UnauthorizedError",
    "__version__",
    "consent",
    "introspection",
    "revocation",
    "token",
]
