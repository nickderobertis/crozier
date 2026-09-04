



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .authorize_request_code_challenge_method import AuthorizeRequestCodeChallengeMethod
    from .authorize_request_response_type import AuthorizeRequestResponseType
    from .introspect_request_token_type_hint import IntrospectRequestTokenTypeHint
    from .pushed_authorization_request_request_code_challenge_method import (
        PushedAuthorizationRequestRequestCodeChallengeMethod,
    )
    from .pushed_authorization_request_request_purpose import PushedAuthorizationRequestRequestPurpose
    from .pushed_authorization_request_request_response_type import PushedAuthorizationRequestRequestResponseType
    from .pushed_authorization_request_response import PushedAuthorizationRequestResponse
    from .token_request_client_assertion_type import TokenRequestClientAssertionType
    from .token_request_grant_type import TokenRequestGrantType
_dynamic_imports: typing.Dict[str, str] = {
    "AuthorizeRequestCodeChallengeMethod": ".authorize_request_code_challenge_method",
    "AuthorizeRequestResponseType": ".authorize_request_response_type",
    "IntrospectRequestTokenTypeHint": ".introspect_request_token_type_hint",
    "PushedAuthorizationRequestRequestCodeChallengeMethod": ".pushed_authorization_request_request_code_challenge_method",
    "PushedAuthorizationRequestRequestPurpose": ".pushed_authorization_request_request_purpose",
    "PushedAuthorizationRequestRequestResponseType": ".pushed_authorization_request_request_response_type",
    "PushedAuthorizationRequestResponse": ".pushed_authorization_request_response",
    "TokenRequestClientAssertionType": ".token_request_client_assertion_type",
    "TokenRequestGrantType": ".token_request_grant_type",
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
    "AuthorizeRequestCodeChallengeMethod",
    "AuthorizeRequestResponseType",
    "IntrospectRequestTokenTypeHint",
    "PushedAuthorizationRequestRequestCodeChallengeMethod",
    "PushedAuthorizationRequestRequestPurpose",
    "PushedAuthorizationRequestRequestResponseType",
    "PushedAuthorizationRequestResponse",
    "TokenRequestClientAssertionType",
    "TokenRequestGrantType",
]
