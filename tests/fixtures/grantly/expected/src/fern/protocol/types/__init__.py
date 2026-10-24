



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_auth_request_code_challenge_method import GetAuthRequestCodeChallengeMethod
    from .get_auth_request_prompt import GetAuthRequestPrompt
    from .get_jwks_response import GetJwksResponse
    from .get_me_response import GetMeResponse
    from .post_introspect_request_token_type_hint import PostIntrospectRequestTokenTypeHint
    from .post_introspect_response import PostIntrospectResponse
    from .post_revoke_request_token_type_hint import PostRevokeRequestTokenTypeHint
    from .post_token_request import PostTokenRequest, PostTokenRequest_AuthorizationCode, PostTokenRequest_RefreshToken
    from .post_token_request_authorization_code import PostTokenRequestAuthorizationCode
    from .post_token_request_refresh_token import PostTokenRequestRefreshToken
    from .post_token_response import PostTokenResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetAuthRequestCodeChallengeMethod": ".get_auth_request_code_challenge_method",
    "GetAuthRequestPrompt": ".get_auth_request_prompt",
    "GetJwksResponse": ".get_jwks_response",
    "GetMeResponse": ".get_me_response",
    "PostIntrospectRequestTokenTypeHint": ".post_introspect_request_token_type_hint",
    "PostIntrospectResponse": ".post_introspect_response",
    "PostRevokeRequestTokenTypeHint": ".post_revoke_request_token_type_hint",
    "PostTokenRequest": ".post_token_request",
    "PostTokenRequestAuthorizationCode": ".post_token_request_authorization_code",
    "PostTokenRequestRefreshToken": ".post_token_request_refresh_token",
    "PostTokenRequest_AuthorizationCode": ".post_token_request",
    "PostTokenRequest_RefreshToken": ".post_token_request",
    "PostTokenResponse": ".post_token_response",
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
    "GetAuthRequestCodeChallengeMethod",
    "GetAuthRequestPrompt",
    "GetJwksResponse",
    "GetMeResponse",
    "PostIntrospectRequestTokenTypeHint",
    "PostIntrospectResponse",
    "PostRevokeRequestTokenTypeHint",
    "PostTokenRequest",
    "PostTokenRequestAuthorizationCode",
    "PostTokenRequestRefreshToken",
    "PostTokenRequest_AuthorizationCode",
    "PostTokenRequest_RefreshToken",
    "PostTokenResponse",
]
