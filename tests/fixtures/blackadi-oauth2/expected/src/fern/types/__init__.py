



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .forbidden_error_body import ForbiddenErrorBody
    from .get_authorization_request_code_challenge_method import GetAuthorizationRequestCodeChallengeMethod
    from .get_authorization_request_prompt import GetAuthorizationRequestPrompt
    from .get_authorization_request_response_type import GetAuthorizationRequestResponseType
    from .get_fapi_config_response import GetFapiConfigResponse
    from .get_fapi_config_response_mode import GetFapiConfigResponseMode
    from .get_fapi_config_response_specs import GetFapiConfigResponseSpecs
    from .get_fapi_status_response import GetFapiStatusResponse
    from .get_health_all_response import GetHealthAllResponse
    from .get_health_all_response_checks import GetHealthAllResponseChecks
    from .get_health_all_response_checks_authlete import GetHealthAllResponseChecksAuthlete
    from .get_health_all_response_checks_redis import GetHealthAllResponseChecksRedis
    from .get_health_authlete_request_extended import GetHealthAuthleteRequestExtended
    from .get_health_response import GetHealthResponse
    from .get_logout_request_backchannel import GetLogoutRequestBackchannel
    from .get_token_list_response import GetTokenListResponse
    from .post_ciba_complete_request_result import PostCibaCompleteRequestResult
    from .post_device_authorization_response import PostDeviceAuthorizationResponse
    from .post_device_complete_request_result import PostDeviceCompleteRequestResult
    from .post_introspection_standard_response import PostIntrospectionStandardResponse
    from .post_logout_request_backchannel import PostLogoutRequestBackchannel
    from .post_par_response import PostParResponse
    from .post_session_consent_request_decision import PostSessionConsentRequestDecision
    from .post_token_request_grant_type import PostTokenRequestGrantType
    from .post_token_response import PostTokenResponse
    from .post_token_response_token_type import PostTokenResponseTokenType
    from .post_vci_deferred_issue_request_order import PostVciDeferredIssueRequestOrder
_dynamic_imports: typing.Dict[str, str] = {
    "ForbiddenErrorBody": ".forbidden_error_body",
    "GetAuthorizationRequestCodeChallengeMethod": ".get_authorization_request_code_challenge_method",
    "GetAuthorizationRequestPrompt": ".get_authorization_request_prompt",
    "GetAuthorizationRequestResponseType": ".get_authorization_request_response_type",
    "GetFapiConfigResponse": ".get_fapi_config_response",
    "GetFapiConfigResponseMode": ".get_fapi_config_response_mode",
    "GetFapiConfigResponseSpecs": ".get_fapi_config_response_specs",
    "GetFapiStatusResponse": ".get_fapi_status_response",
    "GetHealthAllResponse": ".get_health_all_response",
    "GetHealthAllResponseChecks": ".get_health_all_response_checks",
    "GetHealthAllResponseChecksAuthlete": ".get_health_all_response_checks_authlete",
    "GetHealthAllResponseChecksRedis": ".get_health_all_response_checks_redis",
    "GetHealthAuthleteRequestExtended": ".get_health_authlete_request_extended",
    "GetHealthResponse": ".get_health_response",
    "GetLogoutRequestBackchannel": ".get_logout_request_backchannel",
    "GetTokenListResponse": ".get_token_list_response",
    "PostCibaCompleteRequestResult": ".post_ciba_complete_request_result",
    "PostDeviceAuthorizationResponse": ".post_device_authorization_response",
    "PostDeviceCompleteRequestResult": ".post_device_complete_request_result",
    "PostIntrospectionStandardResponse": ".post_introspection_standard_response",
    "PostLogoutRequestBackchannel": ".post_logout_request_backchannel",
    "PostParResponse": ".post_par_response",
    "PostSessionConsentRequestDecision": ".post_session_consent_request_decision",
    "PostTokenRequestGrantType": ".post_token_request_grant_type",
    "PostTokenResponse": ".post_token_response",
    "PostTokenResponseTokenType": ".post_token_response_token_type",
    "PostVciDeferredIssueRequestOrder": ".post_vci_deferred_issue_request_order",
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
    "ForbiddenErrorBody",
    "GetAuthorizationRequestCodeChallengeMethod",
    "GetAuthorizationRequestPrompt",
    "GetAuthorizationRequestResponseType",
    "GetFapiConfigResponse",
    "GetFapiConfigResponseMode",
    "GetFapiConfigResponseSpecs",
    "GetFapiStatusResponse",
    "GetHealthAllResponse",
    "GetHealthAllResponseChecks",
    "GetHealthAllResponseChecksAuthlete",
    "GetHealthAllResponseChecksRedis",
    "GetHealthAuthleteRequestExtended",
    "GetHealthResponse",
    "GetLogoutRequestBackchannel",
    "GetTokenListResponse",
    "PostCibaCompleteRequestResult",
    "PostDeviceAuthorizationResponse",
    "PostDeviceCompleteRequestResult",
    "PostIntrospectionStandardResponse",
    "PostLogoutRequestBackchannel",
    "PostParResponse",
    "PostSessionConsentRequestDecision",
    "PostTokenRequestGrantType",
    "PostTokenResponse",
    "PostTokenResponseTokenType",
    "PostVciDeferredIssueRequestOrder",
]
