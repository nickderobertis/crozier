



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .client_registration_request_grant_types_item import ClientRegistrationRequestGrantTypesItem
    from .client_registration_request_id_token_signed_response_alg import (
        ClientRegistrationRequestIdTokenSignedResponseAlg,
    )
    from .client_registration_request_industry_type import ClientRegistrationRequestIndustryType
    from .client_registration_request_response_types_item import ClientRegistrationRequestResponseTypesItem
    from .client_registration_request_token_endpoint_auth_method import ClientRegistrationRequestTokenEndpointAuthMethod
    from .client_registration_request_token_endpoint_auth_signing_alg import (
        ClientRegistrationRequestTokenEndpointAuthSigningAlg,
    )
    from .client_update_request_industry_type import ClientUpdateRequestIndustryType
_dynamic_imports: typing.Dict[str, str] = {
    "ClientRegistrationRequestGrantTypesItem": ".client_registration_request_grant_types_item",
    "ClientRegistrationRequestIdTokenSignedResponseAlg": ".client_registration_request_id_token_signed_response_alg",
    "ClientRegistrationRequestIndustryType": ".client_registration_request_industry_type",
    "ClientRegistrationRequestResponseTypesItem": ".client_registration_request_response_types_item",
    "ClientRegistrationRequestTokenEndpointAuthMethod": ".client_registration_request_token_endpoint_auth_method",
    "ClientRegistrationRequestTokenEndpointAuthSigningAlg": ".client_registration_request_token_endpoint_auth_signing_alg",
    "ClientUpdateRequestIndustryType": ".client_update_request_industry_type",
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
    "ClientRegistrationRequestGrantTypesItem",
    "ClientRegistrationRequestIdTokenSignedResponseAlg",
    "ClientRegistrationRequestIndustryType",
    "ClientRegistrationRequestResponseTypesItem",
    "ClientRegistrationRequestTokenEndpointAuthMethod",
    "ClientRegistrationRequestTokenEndpointAuthSigningAlg",
    "ClientUpdateRequestIndustryType",
]
