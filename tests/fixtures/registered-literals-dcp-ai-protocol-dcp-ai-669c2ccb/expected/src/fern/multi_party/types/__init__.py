



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .multi_party_authorize_request_authorization import MultiPartyAuthorizeRequestAuthorization
    from .multi_party_authorize_request_authorization_authorizations_item import (
        MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem,
    )
    from .multi_party_authorize_request_authorization_operation import MultiPartyAuthorizeRequestAuthorizationOperation
    from .multi_party_authorize_request_authorization_type import MultiPartyAuthorizeRequestAuthorizationType
    from .multi_party_authorize_response import MultiPartyAuthorizeResponse
_dynamic_imports: typing.Dict[str, str] = {
    "MultiPartyAuthorizeRequestAuthorization": ".multi_party_authorize_request_authorization",
    "MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem": ".multi_party_authorize_request_authorization_authorizations_item",
    "MultiPartyAuthorizeRequestAuthorizationOperation": ".multi_party_authorize_request_authorization_operation",
    "MultiPartyAuthorizeRequestAuthorizationType": ".multi_party_authorize_request_authorization_type",
    "MultiPartyAuthorizeResponse": ".multi_party_authorize_response",
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
    "MultiPartyAuthorizeRequestAuthorization",
    "MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem",
    "MultiPartyAuthorizeRequestAuthorizationOperation",
    "MultiPartyAuthorizeRequestAuthorizationType",
    "MultiPartyAuthorizeResponse",
]
