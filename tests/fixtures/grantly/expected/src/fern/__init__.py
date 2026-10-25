



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import ApiEnvelope, ApiEnvelopeStatus, RegisteredClient
    from .errors import BadRequestError, ForbiddenError, NotFoundError, UnauthorizedError
    from . import app, protocol
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .app import GetAuthExternalProviderRequestProvider
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .protocol import (
        GetAuthRequestCodeChallengeMethod,
        GetAuthRequestPrompt,
        GetJwksResponse,
        GetMeResponse,
        PostIntrospectRequestTokenTypeHint,
        PostIntrospectResponse,
        PostRevokeRequestTokenTypeHint,
        PostTokenRequest,
        PostTokenRequestAuthorizationCode,
        PostTokenRequestRefreshToken,
        PostTokenRequest_AuthorizationCode,
        PostTokenRequest_RefreshToken,
        PostTokenResponse,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ApiEnvelope": ".types",
    "ApiEnvelopeStatus": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "GetAuthExternalProviderRequestProvider": ".app",
    "GetAuthRequestCodeChallengeMethod": ".protocol",
    "GetAuthRequestPrompt": ".protocol",
    "GetJwksResponse": ".protocol",
    "GetMeResponse": ".protocol",
    "NotFoundError": ".errors",
    "PostIntrospectRequestTokenTypeHint": ".protocol",
    "PostIntrospectResponse": ".protocol",
    "PostRevokeRequestTokenTypeHint": ".protocol",
    "PostTokenRequest": ".protocol",
    "PostTokenRequestAuthorizationCode": ".protocol",
    "PostTokenRequestRefreshToken": ".protocol",
    "PostTokenRequest_AuthorizationCode": ".protocol",
    "PostTokenRequest_RefreshToken": ".protocol",
    "PostTokenResponse": ".protocol",
    "RegisteredClient": ".types",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "app": ".app",
    "protocol": ".protocol",
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
    "ApiEnvelope",
    "ApiEnvelopeStatus",
    "AsyncFernApi",
    "BadRequestError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "GetAuthExternalProviderRequestProvider",
    "GetAuthRequestCodeChallengeMethod",
    "GetAuthRequestPrompt",
    "GetJwksResponse",
    "GetMeResponse",
    "NotFoundError",
    "PostIntrospectRequestTokenTypeHint",
    "PostIntrospectResponse",
    "PostRevokeRequestTokenTypeHint",
    "PostTokenRequest",
    "PostTokenRequestAuthorizationCode",
    "PostTokenRequestRefreshToken",
    "PostTokenRequest_AuthorizationCode",
    "PostTokenRequest_RefreshToken",
    "PostTokenResponse",
    "RegisteredClient",
    "UnauthorizedError",
    "__version__",
    "app",
    "protocol",
]
