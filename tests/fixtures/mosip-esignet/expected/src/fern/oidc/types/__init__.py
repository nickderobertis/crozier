



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_authorize_request_acr_values import GetAuthorizeRequestAcrValues
    from .get_authorize_request_display import GetAuthorizeRequestDisplay
    from .get_authorize_request_prompt import GetAuthorizeRequestPrompt
    from .get_authorize_request_response_type import GetAuthorizeRequestResponseType
    from .get_authorize_request_scope import GetAuthorizeRequestScope
    from .get_certs_response import GetCertsResponse
    from .get_certs_response_keys_item import GetCertsResponseKeysItem
    from .get_certs_response_keys_item_kty import GetCertsResponseKeysItemKty
    from .get_certs_response_keys_item_use import GetCertsResponseKeysItemUse
    from .get_introspect_request_token_type_hint import GetIntrospectRequestTokenTypeHint
    from .get_introspect_response import GetIntrospectResponse
    from .get_well_known_openid_configuration_response import GetWellKnownOpenidConfigurationResponse
    from .get_well_known_openid_configuration_response_id_token_signing_alg_values_supported_item import (
        GetWellKnownOpenidConfigurationResponseIdTokenSigningAlgValuesSupportedItem,
    )
    from .get_well_known_openid_configuration_response_response_modes_supported_item import (
        GetWellKnownOpenidConfigurationResponseResponseModesSupportedItem,
    )
    from .get_well_known_openid_configuration_response_token_endpoint_auth_signing_alg_values_supported_item import (
        GetWellKnownOpenidConfigurationResponseTokenEndpointAuthSigningAlgValuesSupportedItem,
    )
    from .post_oauth_par_request_client_assertion_type import PostOauthParRequestClientAssertionType
    from .post_oauth_par_request_code_challenge_method import PostOauthParRequestCodeChallengeMethod
    from .post_oauth_par_request_response_type import PostOauthParRequestResponseType
    from .post_oauth_par_request_scope import PostOauthParRequestScope
    from .post_oauth_par_response import PostOauthParResponse
    from .post_token_request_client_assertion_type import PostTokenRequestClientAssertionType
    from .post_token_request_grant_type import PostTokenRequestGrantType
    from .post_token_response import PostTokenResponse
    from .post_token_response_token_type import PostTokenResponseTokenType
    from .post_token_v2request_client_assertion_type import PostTokenV2RequestClientAssertionType
    from .post_token_v2request_grant_type import PostTokenV2RequestGrantType
    from .post_token_v2response import PostTokenV2Response
    from .post_token_v2response_token_type import PostTokenV2ResponseTokenType
_dynamic_imports: typing.Dict[str, str] = {
    "GetAuthorizeRequestAcrValues": ".get_authorize_request_acr_values",
    "GetAuthorizeRequestDisplay": ".get_authorize_request_display",
    "GetAuthorizeRequestPrompt": ".get_authorize_request_prompt",
    "GetAuthorizeRequestResponseType": ".get_authorize_request_response_type",
    "GetAuthorizeRequestScope": ".get_authorize_request_scope",
    "GetCertsResponse": ".get_certs_response",
    "GetCertsResponseKeysItem": ".get_certs_response_keys_item",
    "GetCertsResponseKeysItemKty": ".get_certs_response_keys_item_kty",
    "GetCertsResponseKeysItemUse": ".get_certs_response_keys_item_use",
    "GetIntrospectRequestTokenTypeHint": ".get_introspect_request_token_type_hint",
    "GetIntrospectResponse": ".get_introspect_response",
    "GetWellKnownOpenidConfigurationResponse": ".get_well_known_openid_configuration_response",
    "GetWellKnownOpenidConfigurationResponseIdTokenSigningAlgValuesSupportedItem": ".get_well_known_openid_configuration_response_id_token_signing_alg_values_supported_item",
    "GetWellKnownOpenidConfigurationResponseResponseModesSupportedItem": ".get_well_known_openid_configuration_response_response_modes_supported_item",
    "GetWellKnownOpenidConfigurationResponseTokenEndpointAuthSigningAlgValuesSupportedItem": ".get_well_known_openid_configuration_response_token_endpoint_auth_signing_alg_values_supported_item",
    "PostOauthParRequestClientAssertionType": ".post_oauth_par_request_client_assertion_type",
    "PostOauthParRequestCodeChallengeMethod": ".post_oauth_par_request_code_challenge_method",
    "PostOauthParRequestResponseType": ".post_oauth_par_request_response_type",
    "PostOauthParRequestScope": ".post_oauth_par_request_scope",
    "PostOauthParResponse": ".post_oauth_par_response",
    "PostTokenRequestClientAssertionType": ".post_token_request_client_assertion_type",
    "PostTokenRequestGrantType": ".post_token_request_grant_type",
    "PostTokenResponse": ".post_token_response",
    "PostTokenResponseTokenType": ".post_token_response_token_type",
    "PostTokenV2RequestClientAssertionType": ".post_token_v2request_client_assertion_type",
    "PostTokenV2RequestGrantType": ".post_token_v2request_grant_type",
    "PostTokenV2Response": ".post_token_v2response",
    "PostTokenV2ResponseTokenType": ".post_token_v2response_token_type",
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
