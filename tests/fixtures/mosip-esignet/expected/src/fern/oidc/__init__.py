



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetAuthorizeRequestAcrValues,
        GetAuthorizeRequestDisplay,
        GetAuthorizeRequestPrompt,
        GetAuthorizeRequestResponseType,
        GetAuthorizeRequestScope,
        GetCertsResponse,
        GetCertsResponseKeysItem,
        GetCertsResponseKeysItemKty,
        GetCertsResponseKeysItemUse,
        GetIntrospectRequestTokenTypeHint,
        GetIntrospectResponse,
        GetWellKnownOpenidConfigurationResponse,
        GetWellKnownOpenidConfigurationResponseIdTokenSigningAlgValuesSupportedItem,
        GetWellKnownOpenidConfigurationResponseResponseModesSupportedItem,
        GetWellKnownOpenidConfigurationResponseTokenEndpointAuthSigningAlgValuesSupportedItem,
        PostOauthParRequestClientAssertionType,
        PostOauthParRequestCodeChallengeMethod,
        PostOauthParRequestResponseType,
        PostOauthParRequestScope,
        PostOauthParResponse,
        PostTokenRequestClientAssertionType,
        PostTokenRequestGrantType,
        PostTokenResponse,
        PostTokenResponseTokenType,
        PostTokenV2RequestClientAssertionType,
        PostTokenV2RequestGrantType,
        PostTokenV2Response,
        PostTokenV2ResponseTokenType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetAuthorizeRequestAcrValues": ".types",
    "GetAuthorizeRequestDisplay": ".types",
    "GetAuthorizeRequestPrompt": ".types",
    "GetAuthorizeRequestResponseType": ".types",
    "GetAuthorizeRequestScope": ".types",
    "GetCertsResponse": ".types",
    "GetCertsResponseKeysItem": ".types",
    "GetCertsResponseKeysItemKty": ".types",
    "GetCertsResponseKeysItemUse": ".types",
    "GetIntrospectRequestTokenTypeHint": ".types",
    "GetIntrospectResponse": ".types",
    "GetWellKnownOpenidConfigurationResponse": ".types",
    "GetWellKnownOpenidConfigurationResponseIdTokenSigningAlgValuesSupportedItem": ".types",
    "GetWellKnownOpenidConfigurationResponseResponseModesSupportedItem": ".types",
    "GetWellKnownOpenidConfigurationResponseTokenEndpointAuthSigningAlgValuesSupportedItem": ".types",
    "PostOauthParRequestClientAssertionType": ".types",
    "PostOauthParRequestCodeChallengeMethod": ".types",
    "PostOauthParRequestResponseType": ".types",
    "PostOauthParRequestScope": ".types",
    "PostOauthParResponse": ".types",
    "PostTokenRequestClientAssertionType": ".types",
    "PostTokenRequestGrantType": ".types",
    "PostTokenResponse": ".types",
    "PostTokenResponseTokenType": ".types",
    "PostTokenV2RequestClientAssertionType": ".types",
    "PostTokenV2RequestGrantType": ".types",
    "PostTokenV2Response": ".types",
    "PostTokenV2ResponseTokenType": ".types",
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
    "GetAuthorizeRequestAcrValues",
    "GetAuthorizeRequestDisplay",
    "GetAuthorizeRequestPrompt",
    "GetAuthorizeRequestResponseType",
    "GetAuthorizeRequestScope",
    "GetCertsResponse",
    "GetCertsResponseKeysItem",
    "GetCertsResponseKeysItemKty",
    "GetCertsResponseKeysItemUse",
    "GetIntrospectRequestTokenTypeHint",
    "GetIntrospectResponse",
    "GetWellKnownOpenidConfigurationResponse",
    "GetWellKnownOpenidConfigurationResponseIdTokenSigningAlgValuesSupportedItem",
    "GetWellKnownOpenidConfigurationResponseResponseModesSupportedItem",
    "GetWellKnownOpenidConfigurationResponseTokenEndpointAuthSigningAlgValuesSupportedItem",
    "PostOauthParRequestClientAssertionType",
    "PostOauthParRequestCodeChallengeMethod",
    "PostOauthParRequestResponseType",
    "PostOauthParRequestScope",
    "PostOauthParResponse",
    "PostTokenRequestClientAssertionType",
    "PostTokenRequestGrantType",
    "PostTokenResponse",
    "PostTokenResponseTokenType",
    "PostTokenV2RequestClientAssertionType",
    "PostTokenV2RequestGrantType",
    "PostTokenV2Response",
    "PostTokenV2ResponseTokenType",
]
