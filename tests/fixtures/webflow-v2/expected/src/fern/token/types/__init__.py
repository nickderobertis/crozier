



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .authorized_by_token_response import AuthorizedByTokenResponse
    from .introspect_token_response import IntrospectTokenResponse
    from .introspect_token_response_application import IntrospectTokenResponseApplication
    from .introspect_token_response_authorization import IntrospectTokenResponseAuthorization
    from .introspect_token_response_authorization_authorized_to import IntrospectTokenResponseAuthorizationAuthorizedTo
_dynamic_imports: typing.Dict[str, str] = {
    "AuthorizedByTokenResponse": ".authorized_by_token_response",
    "IntrospectTokenResponse": ".introspect_token_response",
    "IntrospectTokenResponseApplication": ".introspect_token_response_application",
    "IntrospectTokenResponseAuthorization": ".introspect_token_response_authorization",
    "IntrospectTokenResponseAuthorizationAuthorizedTo": ".introspect_token_response_authorization_authorized_to",
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
    "AuthorizedByTokenResponse",
    "IntrospectTokenResponse",
    "IntrospectTokenResponseApplication",
    "IntrospectTokenResponseAuthorization",
    "IntrospectTokenResponseAuthorizationAuthorizedTo",
]
