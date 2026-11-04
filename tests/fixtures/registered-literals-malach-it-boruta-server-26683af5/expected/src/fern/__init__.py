



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AuthorizationServerMetadata,
        CredentialIssuerMetadata,
        CredentialResponse,
        IntrospectionResponse,
        JsonWebKeySet,
        OAuthError,
        PushedAuthorizationResponse,
        TokenRequest,
        TokenRequestGrantType,
        TokenResponse,
    )
    from .errors import BadRequestError, NotFoundError, UnauthorizedError, UnprocessableEntityError
    from . import (
        assets,
        did_and_verifiable_credentials,
        discovery,
        federated_identity,
        identity_confirmation,
        identity_consent,
        identity_mfa,
        identity_password_recovery,
        identity_registration,
        identity_sessions,
        identity_settings,
        identity_wallet,
        infrastructure,
        o_auth20,
        open_id_connect,
        open_id_for_verifiable_credentials,
        open_id_for_verifiable_presentations,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .o_auth20 import (
        GetOauthAuthorizeRequestCodeChallengeMethod,
        PostOauthIntrospectRequestTokenTypeHint,
        PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod,
        PostOauthRevokeRequestTokenTypeHint,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "AuthorizationServerMetadata": ".types",
    "BadRequestError": ".errors",
    "CredentialIssuerMetadata": ".types",
    "CredentialResponse": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetOauthAuthorizeRequestCodeChallengeMethod": ".o_auth20",
    "IntrospectionResponse": ".types",
    "JsonWebKeySet": ".types",
    "NotFoundError": ".errors",
    "OAuthError": ".types",
    "PostOauthIntrospectRequestTokenTypeHint": ".o_auth20",
    "PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod": ".o_auth20",
    "PostOauthRevokeRequestTokenTypeHint": ".o_auth20",
    "PushedAuthorizationResponse": ".types",
    "TokenRequest": ".types",
    "TokenRequestGrantType": ".types",
    "TokenResponse": ".types",
    "UnauthorizedError": ".errors",
    "UnprocessableEntityError": ".errors",
    "__version__": ".version",
    "assets": ".assets",
    "did_and_verifiable_credentials": ".did_and_verifiable_credentials",
    "discovery": ".discovery",
    "federated_identity": ".federated_identity",
    "identity_confirmation": ".identity_confirmation",
    "identity_consent": ".identity_consent",
    "identity_mfa": ".identity_mfa",
    "identity_password_recovery": ".identity_password_recovery",
    "identity_registration": ".identity_registration",
    "identity_sessions": ".identity_sessions",
    "identity_settings": ".identity_settings",
    "identity_wallet": ".identity_wallet",
    "infrastructure": ".infrastructure",
    "o_auth20": ".o_auth20",
    "open_id_connect": ".open_id_connect",
    "open_id_for_verifiable_credentials": ".open_id_for_verifiable_credentials",
    "open_id_for_verifiable_presentations": ".open_id_for_verifiable_presentations",
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
    "AuthorizationServerMetadata",
    "BadRequestError",
    "CredentialIssuerMetadata",
    "CredentialResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GetOauthAuthorizeRequestCodeChallengeMethod",
    "IntrospectionResponse",
    "JsonWebKeySet",
    "NotFoundError",
    "OAuthError",
    "PostOauthIntrospectRequestTokenTypeHint",
    "PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod",
    "PostOauthRevokeRequestTokenTypeHint",
    "PushedAuthorizationResponse",
    "TokenRequest",
    "TokenRequestGrantType",
    "TokenResponse",
    "UnauthorizedError",
    "UnprocessableEntityError",
    "__version__",
    "assets",
    "did_and_verifiable_credentials",
    "discovery",
    "federated_identity",
    "identity_confirmation",
    "identity_consent",
    "identity_mfa",
    "identity_password_recovery",
    "identity_registration",
    "identity_sessions",
    "identity_settings",
    "identity_wallet",
    "infrastructure",
    "o_auth20",
    "open_id_connect",
    "open_id_for_verifiable_credentials",
    "open_id_for_verifiable_presentations",
]
