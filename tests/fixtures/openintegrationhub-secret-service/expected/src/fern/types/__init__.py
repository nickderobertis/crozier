



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_key_secret import ApiKeySecret
    from .auth_client import (
        AuthClient,
        AuthClient_Oa1ThreeLegged,
        AuthClient_Oa1TwoLegged,
        AuthClient_Oa2AuthorizationCode,
        AuthClient_SessionAuth,
    )
    from .auth_client_entry import AuthClientEntry
    from .error_response import ErrorResponse
    from .meta import Meta
    from .mixed_secret import MixedSecret
    from .mutable_auth_client import (
        MutableAuthClient,
        MutableAuthClient_Oa1ThreeLegged,
        MutableAuthClient_Oa1TwoLegged,
        MutableAuthClient_Oa2AuthorizationCode,
        MutableAuthClient_SessionAuth,
    )
    from .mutable_oa1three_legged_client import MutableOa1ThreeLeggedClient
    from .mutable_oa1three_legged_client_endpoints import MutableOa1ThreeLeggedClientEndpoints
    from .mutable_oa1three_legged_client_type import MutableOa1ThreeLeggedClientType
    from .mutable_oa1two_legged_client import MutableOa1TwoLeggedClient
    from .mutable_oa1two_legged_client_type import MutableOa1TwoLeggedClientType
    from .mutable_oa2authorization_code_client import MutableOa2AuthorizationCodeClient
    from .mutable_oa2authorization_code_client_endpoints import MutableOa2AuthorizationCodeClientEndpoints
    from .mutable_oa2authorization_code_client_type import MutableOa2AuthorizationCodeClientType
    from .mutable_secret import MutableSecret
    from .mutable_secret_type import MutableSecretType
    from .mutable_secret_value import (
        MutableSecretValue,
        MutableSecretValue_ApiKey,
        MutableSecretValue_Mixed,
        MutableSecretValue_Oa1ThreeLegged,
        MutableSecretValue_Oa1TwoLegged,
        MutableSecretValue_Oa2AuthorizationCode,
        MutableSecretValue_SessionAuth,
        MutableSecretValue_Simple,
    )
    from .mutable_session_auth_client import MutableSessionAuthClient
    from .mutable_session_auth_client_endpoints import MutableSessionAuthClientEndpoints
    from .mutable_session_auth_client_type import MutableSessionAuthClientType
    from .oa1three_legged_client import Oa1ThreeLeggedClient
    from .oa1three_legged_secret import Oa1ThreeLeggedSecret
    from .oa1two_legged_client import Oa1TwoLeggedClient
    from .oa1two_legged_secret import Oa1TwoLeggedSecret
    from .oa2authorization_code_client import Oa2AuthorizationCodeClient
    from .oa2authorization_code_secret import Oa2AuthorizationCodeSecret
    from .owner import Owner
    from .request_config import RequestConfig
    from .request_config_auth_type import RequestConfigAuthType
    from .request_field import RequestField
    from .secret import Secret
    from .secret_entry import SecretEntry
    from .session_auth_client import SessionAuthClient
    from .session_auth_secret import SessionAuthSecret
    from .session_field import SessionField
    from .simple_secret import SimpleSecret
_dynamic_imports: typing.Dict[str, str] = {
    "ApiKeySecret": ".api_key_secret",
    "AuthClient": ".auth_client",
    "AuthClientEntry": ".auth_client_entry",
    "AuthClient_Oa1ThreeLegged": ".auth_client",
    "AuthClient_Oa1TwoLegged": ".auth_client",
    "AuthClient_Oa2AuthorizationCode": ".auth_client",
    "AuthClient_SessionAuth": ".auth_client",
    "ErrorResponse": ".error_response",
    "Meta": ".meta",
    "MixedSecret": ".mixed_secret",
    "MutableAuthClient": ".mutable_auth_client",
    "MutableAuthClient_Oa1ThreeLegged": ".mutable_auth_client",
    "MutableAuthClient_Oa1TwoLegged": ".mutable_auth_client",
    "MutableAuthClient_Oa2AuthorizationCode": ".mutable_auth_client",
    "MutableAuthClient_SessionAuth": ".mutable_auth_client",
    "MutableOa1ThreeLeggedClient": ".mutable_oa1three_legged_client",
    "MutableOa1ThreeLeggedClientEndpoints": ".mutable_oa1three_legged_client_endpoints",
    "MutableOa1ThreeLeggedClientType": ".mutable_oa1three_legged_client_type",
    "MutableOa1TwoLeggedClient": ".mutable_oa1two_legged_client",
    "MutableOa1TwoLeggedClientType": ".mutable_oa1two_legged_client_type",
    "MutableOa2AuthorizationCodeClient": ".mutable_oa2authorization_code_client",
    "MutableOa2AuthorizationCodeClientEndpoints": ".mutable_oa2authorization_code_client_endpoints",
    "MutableOa2AuthorizationCodeClientType": ".mutable_oa2authorization_code_client_type",
    "MutableSecret": ".mutable_secret",
    "MutableSecretType": ".mutable_secret_type",
    "MutableSecretValue": ".mutable_secret_value",
    "MutableSecretValue_ApiKey": ".mutable_secret_value",
    "MutableSecretValue_Mixed": ".mutable_secret_value",
    "MutableSecretValue_Oa1ThreeLegged": ".mutable_secret_value",
    "MutableSecretValue_Oa1TwoLegged": ".mutable_secret_value",
    "MutableSecretValue_Oa2AuthorizationCode": ".mutable_secret_value",
    "MutableSecretValue_SessionAuth": ".mutable_secret_value",
    "MutableSecretValue_Simple": ".mutable_secret_value",
    "MutableSessionAuthClient": ".mutable_session_auth_client",
    "MutableSessionAuthClientEndpoints": ".mutable_session_auth_client_endpoints",
    "MutableSessionAuthClientType": ".mutable_session_auth_client_type",
    "Oa1ThreeLeggedClient": ".oa1three_legged_client",
    "Oa1ThreeLeggedSecret": ".oa1three_legged_secret",
    "Oa1TwoLeggedClient": ".oa1two_legged_client",
    "Oa1TwoLeggedSecret": ".oa1two_legged_secret",
    "Oa2AuthorizationCodeClient": ".oa2authorization_code_client",
    "Oa2AuthorizationCodeSecret": ".oa2authorization_code_secret",
    "Owner": ".owner",
    "RequestConfig": ".request_config",
    "RequestConfigAuthType": ".request_config_auth_type",
    "RequestField": ".request_field",
    "Secret": ".secret",
    "SecretEntry": ".secret_entry",
    "SessionAuthClient": ".session_auth_client",
    "SessionAuthSecret": ".session_auth_secret",
    "SessionField": ".session_field",
    "SimpleSecret": ".simple_secret",
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
    "ApiKeySecret",
    "AuthClient",
    "AuthClientEntry",
    "AuthClient_Oa1ThreeLegged",
    "AuthClient_Oa1TwoLegged",
    "AuthClient_Oa2AuthorizationCode",
    "AuthClient_SessionAuth",
    "ErrorResponse",
    "Meta",
    "MixedSecret",
    "MutableAuthClient",
    "MutableAuthClient_Oa1ThreeLegged",
    "MutableAuthClient_Oa1TwoLegged",
    "MutableAuthClient_Oa2AuthorizationCode",
    "MutableAuthClient_SessionAuth",
    "MutableOa1ThreeLeggedClient",
    "MutableOa1ThreeLeggedClientEndpoints",
    "MutableOa1ThreeLeggedClientType",
    "MutableOa1TwoLeggedClient",
    "MutableOa1TwoLeggedClientType",
    "MutableOa2AuthorizationCodeClient",
    "MutableOa2AuthorizationCodeClientEndpoints",
    "MutableOa2AuthorizationCodeClientType",
    "MutableSecret",
    "MutableSecretType",
    "MutableSecretValue",
    "MutableSecretValue_ApiKey",
    "MutableSecretValue_Mixed",
    "MutableSecretValue_Oa1ThreeLegged",
    "MutableSecretValue_Oa1TwoLegged",
    "MutableSecretValue_Oa2AuthorizationCode",
    "MutableSecretValue_SessionAuth",
    "MutableSecretValue_Simple",
    "MutableSessionAuthClient",
    "MutableSessionAuthClientEndpoints",
    "MutableSessionAuthClientType",
    "Oa1ThreeLeggedClient",
    "Oa1ThreeLeggedSecret",
    "Oa1TwoLeggedClient",
    "Oa1TwoLeggedSecret",
    "Oa2AuthorizationCodeClient",
    "Oa2AuthorizationCodeSecret",
    "Owner",
    "RequestConfig",
    "RequestConfigAuthType",
    "RequestField",
    "Secret",
    "SecretEntry",
    "SessionAuthClient",
    "SessionAuthSecret",
    "SessionField",
    "SimpleSecret",
]
