



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .v1authorize_user_request_code_challenge_method import V1AuthorizeUserRequestCodeChallengeMethod
    from .v1authorize_user_request_response_type import V1AuthorizeUserRequestResponseType
    from .v1oauth_authorize_project_claim_request_code_challenge_method import (
        V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod,
    )
    from .v1oauth_authorize_project_claim_request_response_type import V1OauthAuthorizeProjectClaimRequestResponseType
_dynamic_imports: typing.Dict[str, str] = {
    "V1AuthorizeUserRequestCodeChallengeMethod": ".v1authorize_user_request_code_challenge_method",
    "V1AuthorizeUserRequestResponseType": ".v1authorize_user_request_response_type",
    "V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod": ".v1oauth_authorize_project_claim_request_code_challenge_method",
    "V1OauthAuthorizeProjectClaimRequestResponseType": ".v1oauth_authorize_project_claim_request_response_type",
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
    "V1AuthorizeUserRequestCodeChallengeMethod",
    "V1AuthorizeUserRequestResponseType",
    "V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod",
    "V1OauthAuthorizeProjectClaimRequestResponseType",
]
