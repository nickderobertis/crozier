



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .consent_record import ConsentRecord
    from .consent_request import ConsentRequest
    from .delegation_token import DelegationToken
    from .delegation_token_aal_asserted import DelegationTokenAalAsserted
    from .delegation_token_token_type import DelegationTokenTokenType
    from .error import Error
    from .introspection_request import IntrospectionRequest
    from .introspection_request_token_type_hint import IntrospectionRequestTokenTypeHint
    from .introspection_response import IntrospectionResponse
    from .introspection_response_aal_asserted import IntrospectionResponseAalAsserted
    from .revocation_request import RevocationRequest
    from .revocation_request_token_type_hint import RevocationRequestTokenTypeHint
    from .token_request import TokenRequest
    from .token_request_grant_type import TokenRequestGrantType
_dynamic_imports: typing.Dict[str, str] = {
    "ConsentRecord": ".consent_record",
    "ConsentRequest": ".consent_request",
    "DelegationToken": ".delegation_token",
    "DelegationTokenAalAsserted": ".delegation_token_aal_asserted",
    "DelegationTokenTokenType": ".delegation_token_token_type",
    "Error": ".error",
    "IntrospectionRequest": ".introspection_request",
    "IntrospectionRequestTokenTypeHint": ".introspection_request_token_type_hint",
    "IntrospectionResponse": ".introspection_response",
    "IntrospectionResponseAalAsserted": ".introspection_response_aal_asserted",
    "RevocationRequest": ".revocation_request",
    "RevocationRequestTokenTypeHint": ".revocation_request_token_type_hint",
    "TokenRequest": ".token_request",
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
    "ConsentRecord",
    "ConsentRequest",
    "DelegationToken",
    "DelegationTokenAalAsserted",
    "DelegationTokenTokenType",
    "Error",
    "IntrospectionRequest",
    "IntrospectionRequestTokenTypeHint",
    "IntrospectionResponse",
    "IntrospectionResponseAalAsserted",
    "RevocationRequest",
    "RevocationRequestTokenTypeHint",
    "TokenRequest",
    "TokenRequestGrantType",
]
