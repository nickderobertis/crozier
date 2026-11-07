



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .authorization_server_metadata import AuthorizationServerMetadata
    from .credential_issuer_metadata import CredentialIssuerMetadata
    from .credential_response import CredentialResponse
    from .introspection_response import IntrospectionResponse
    from .json_web_key_set import JsonWebKeySet
    from .o_auth_error import OAuthError
    from .pushed_authorization_response import PushedAuthorizationResponse
    from .token_request import TokenRequest
    from .token_request_grant_type import TokenRequestGrantType
    from .token_response import TokenResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AuthorizationServerMetadata": ".authorization_server_metadata",
    "CredentialIssuerMetadata": ".credential_issuer_metadata",
    "CredentialResponse": ".credential_response",
    "IntrospectionResponse": ".introspection_response",
    "JsonWebKeySet": ".json_web_key_set",
    "OAuthError": ".o_auth_error",
    "PushedAuthorizationResponse": ".pushed_authorization_response",
    "TokenRequest": ".token_request",
    "TokenRequestGrantType": ".token_request_grant_type",
    "TokenResponse": ".token_response",
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
    "AuthorizationServerMetadata",
    "CredentialIssuerMetadata",
    "CredentialResponse",
    "IntrospectionResponse",
    "JsonWebKeySet",
    "OAuthError",
    "PushedAuthorizationResponse",
    "TokenRequest",
    "TokenRequestGrantType",
    "TokenResponse",
]
