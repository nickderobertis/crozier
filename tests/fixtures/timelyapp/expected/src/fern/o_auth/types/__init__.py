



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_current_token_info_response import GetCurrentTokenInfoResponse
    from .get_current_token_info_response_application import GetCurrentTokenInfoResponseApplication
    from .v1o_auth_introspect_request_token_type_hint import V1OAuthIntrospectRequestTokenTypeHint
    from .v1o_auth_revoke_request_token_type_hint import V1OAuthRevokeRequestTokenTypeHint
    from .v1o_auth_token_request_grant_type import V1OAuthTokenRequestGrantType
_dynamic_imports: typing.Dict[str, str] = {
    "GetCurrentTokenInfoResponse": ".get_current_token_info_response",
    "GetCurrentTokenInfoResponseApplication": ".get_current_token_info_response_application",
    "V1OAuthIntrospectRequestTokenTypeHint": ".v1o_auth_introspect_request_token_type_hint",
    "V1OAuthRevokeRequestTokenTypeHint": ".v1o_auth_revoke_request_token_type_hint",
    "V1OAuthTokenRequestGrantType": ".v1o_auth_token_request_grant_type",
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
    "GetCurrentTokenInfoResponse",
    "GetCurrentTokenInfoResponseApplication",
    "V1OAuthIntrospectRequestTokenTypeHint",
    "V1OAuthRevokeRequestTokenTypeHint",
    "V1OAuthTokenRequestGrantType",
]
