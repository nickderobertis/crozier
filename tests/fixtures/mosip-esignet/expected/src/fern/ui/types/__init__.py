



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_authorization_generate_link_code_request_request import GetAuthorizationGenerateLinkCodeRequestRequest
    from .get_authorization_generate_link_code_response import GetAuthorizationGenerateLinkCodeResponse
    from .get_authorization_generate_link_code_response_errors_item import (
        GetAuthorizationGenerateLinkCodeResponseErrorsItem,
    )
    from .get_authorization_generate_link_code_response_errors_item_error_code import (
        GetAuthorizationGenerateLinkCodeResponseErrorsItemErrorCode,
    )
    from .get_authorization_generate_link_code_response_response import GetAuthorizationGenerateLinkCodeResponseResponse
    from .get_consent_details_response import GetConsentDetailsResponse
    from .get_consent_details_response_errors_item import GetConsentDetailsResponseErrorsItem
    from .get_consent_details_response_errors_item_error_code import GetConsentDetailsResponseErrorsItemErrorCode
    from .get_consent_details_response_response import GetConsentDetailsResponseResponse
    from .get_consent_details_response_response_consent_action import GetConsentDetailsResponseResponseConsentAction
    from .post_auth_code_request_request import PostAuthCodeRequestRequest
    from .post_auth_code_response import PostAuthCodeResponse
    from .post_auth_code_response_errors_item import PostAuthCodeResponseErrorsItem
    from .post_auth_code_response_errors_item_error_code import PostAuthCodeResponseErrorsItemErrorCode
    from .post_auth_code_response_response import PostAuthCodeResponseResponse
    from .post_authenticate_request_request import PostAuthenticateRequestRequest
    from .post_authenticate_response import PostAuthenticateResponse
    from .post_authenticate_response_errors_item import PostAuthenticateResponseErrorsItem
    from .post_authenticate_response_errors_item_error_code import PostAuthenticateResponseErrorsItemErrorCode
    from .post_authenticate_response_response import PostAuthenticateResponseResponse
    from .post_authenticate_v2request_request import PostAuthenticateV2RequestRequest
    from .post_authenticate_v2response import PostAuthenticateV2Response
    from .post_authenticate_v2response_errors_item import PostAuthenticateV2ResponseErrorsItem
    from .post_authenticate_v2response_errors_item_error_code import PostAuthenticateV2ResponseErrorsItemErrorCode
    from .post_authenticate_v2response_response import PostAuthenticateV2ResponseResponse
    from .post_authenticate_v2response_response_consent_action import PostAuthenticateV2ResponseResponseConsentAction
    from .post_authenticate_v3request_request import PostAuthenticateV3RequestRequest
    from .post_authenticate_v3response import PostAuthenticateV3Response
    from .post_authenticate_v3response_errors_item import PostAuthenticateV3ResponseErrorsItem
    from .post_authenticate_v3response_errors_item_error_code import PostAuthenticateV3ResponseErrorsItemErrorCode
    from .post_authenticate_v3response_response import PostAuthenticateV3ResponseResponse
    from .post_authenticate_v3response_response_consent_action import PostAuthenticateV3ResponseResponseConsentAction
    from .post_authorization_link_auth_request_request import PostAuthorizationLinkAuthRequestRequest
    from .post_authorization_link_auth_response import PostAuthorizationLinkAuthResponse
    from .post_authorization_link_auth_response_errors_item import PostAuthorizationLinkAuthResponseErrorsItem
    from .post_authorization_link_auth_response_errors_item_error_code import (
        PostAuthorizationLinkAuthResponseErrorsItemErrorCode,
    )
    from .post_authorization_link_auth_response_response import PostAuthorizationLinkAuthResponseResponse
    from .post_authorization_link_status_request_request import PostAuthorizationLinkStatusRequestRequest
    from .post_authorization_link_status_response import PostAuthorizationLinkStatusResponse
    from .post_authorization_link_status_response_errors_item import PostAuthorizationLinkStatusResponseErrorsItem
    from .post_authorization_link_status_response_errors_item_error_code import (
        PostAuthorizationLinkStatusResponseErrorsItemErrorCode,
    )
    from .post_authorization_link_status_response_response import PostAuthorizationLinkStatusResponseResponse
    from .post_authorization_link_status_response_response_link_status import (
        PostAuthorizationLinkStatusResponseResponseLinkStatus,
    )
    from .post_authorization_prepare_signup_redirect_request_request import (
        PostAuthorizationPrepareSignupRedirectRequestRequest,
    )
    from .post_authorization_prepare_signup_redirect_response import PostAuthorizationPrepareSignupRedirectResponse
    from .post_authorization_prepare_signup_redirect_response_errors_item import (
        PostAuthorizationPrepareSignupRedirectResponseErrorsItem,
    )
    from .post_authorization_prepare_signup_redirect_response_errors_item_error_code import (
        PostAuthorizationPrepareSignupRedirectResponseErrorsItemErrorCode,
    )
    from .post_authorization_prepare_signup_redirect_response_response import (
        PostAuthorizationPrepareSignupRedirectResponseResponse,
    )
    from .post_complete_signup_redirect_request_request import PostCompleteSignupRedirectRequestRequest
    from .post_complete_signup_redirect_response import PostCompleteSignupRedirectResponse
    from .post_complete_signup_redirect_response_errors_item import PostCompleteSignupRedirectResponseErrorsItem
    from .post_complete_signup_redirect_response_errors_item_error_code import (
        PostCompleteSignupRedirectResponseErrorsItemErrorCode,
    )
    from .post_complete_signup_redirect_response_response import PostCompleteSignupRedirectResponseResponse
    from .post_complete_signup_redirect_response_response_status import PostCompleteSignupRedirectResponseResponseStatus
    from .post_oauth_details_request_request import PostOauthDetailsRequestRequest
    from .post_oauth_details_response import PostOauthDetailsResponse
    from .post_oauth_details_response_errors_item import PostOauthDetailsResponseErrorsItem
    from .post_oauth_details_response_errors_item_error_code import PostOauthDetailsResponseErrorsItemErrorCode
    from .post_oauth_details_response_response import PostOauthDetailsResponseResponse
    from .post_oauth_details_v2request_request import PostOauthDetailsV2RequestRequest
    from .post_oauth_details_v2request_request_code_challenge_method import (
        PostOauthDetailsV2RequestRequestCodeChallengeMethod,
    )
    from .post_oauth_details_v2response import PostOauthDetailsV2Response
    from .post_oauth_details_v2response_errors_item import PostOauthDetailsV2ResponseErrorsItem
    from .post_oauth_details_v2response_errors_item_error_code import PostOauthDetailsV2ResponseErrorsItemErrorCode
    from .post_oauth_details_v2response_response import PostOauthDetailsV2ResponseResponse
    from .post_oauth_details_v3request_request import PostOauthDetailsV3RequestRequest
    from .post_oauth_details_v3request_request_code_challenge_method import (
        PostOauthDetailsV3RequestRequestCodeChallengeMethod,
    )
    from .post_oauth_details_v3response import PostOauthDetailsV3Response
    from .post_oauth_details_v3response_errors_item import PostOauthDetailsV3ResponseErrorsItem
    from .post_oauth_details_v3response_errors_item_error_code import PostOauthDetailsV3ResponseErrorsItemErrorCode
    from .post_oauth_details_v3response_response import PostOauthDetailsV3ResponseResponse
    from .post_par_oauth_details_request_request import PostParOauthDetailsRequestRequest
    from .post_par_oauth_details_response import PostParOauthDetailsResponse
    from .post_par_oauth_details_response_errors_item import PostParOauthDetailsResponseErrorsItem
    from .post_par_oauth_details_response_errors_item_error_code import PostParOauthDetailsResponseErrorsItemErrorCode
    from .post_par_oauth_details_response_response import PostParOauthDetailsResponseResponse
    from .post_send_linked_otp_request_request import PostSendLinkedOtpRequestRequest
    from .post_send_linked_otp_request_request_otp_channels_item import PostSendLinkedOtpRequestRequestOtpChannelsItem
    from .post_send_linked_otp_response import PostSendLinkedOtpResponse
    from .post_send_linked_otp_response_errors_item import PostSendLinkedOtpResponseErrorsItem
    from .post_send_linked_otp_response_errors_item_error_code import PostSendLinkedOtpResponseErrorsItemErrorCode
    from .post_send_linked_otp_response_response import PostSendLinkedOtpResponseResponse
    from .post_send_otp_request_request import PostSendOtpRequestRequest
    from .post_send_otp_request_request_otp_channels_item import PostSendOtpRequestRequestOtpChannelsItem
    from .post_send_otp_response import PostSendOtpResponse
    from .post_send_otp_response_errors_item import PostSendOtpResponseErrorsItem
    from .post_send_otp_response_errors_item_error_code import PostSendOtpResponseErrorsItemErrorCode
    from .post_send_otp_response_response import PostSendOtpResponseResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetAuthorizationGenerateLinkCodeRequestRequest": ".get_authorization_generate_link_code_request_request",
    "GetAuthorizationGenerateLinkCodeResponse": ".get_authorization_generate_link_code_response",
    "GetAuthorizationGenerateLinkCodeResponseErrorsItem": ".get_authorization_generate_link_code_response_errors_item",
    "GetAuthorizationGenerateLinkCodeResponseErrorsItemErrorCode": ".get_authorization_generate_link_code_response_errors_item_error_code",
    "GetAuthorizationGenerateLinkCodeResponseResponse": ".get_authorization_generate_link_code_response_response",
    "GetConsentDetailsResponse": ".get_consent_details_response",
    "GetConsentDetailsResponseErrorsItem": ".get_consent_details_response_errors_item",
    "GetConsentDetailsResponseErrorsItemErrorCode": ".get_consent_details_response_errors_item_error_code",
    "GetConsentDetailsResponseResponse": ".get_consent_details_response_response",
    "GetConsentDetailsResponseResponseConsentAction": ".get_consent_details_response_response_consent_action",
    "PostAuthCodeRequestRequest": ".post_auth_code_request_request",
    "PostAuthCodeResponse": ".post_auth_code_response",
    "PostAuthCodeResponseErrorsItem": ".post_auth_code_response_errors_item",
    "PostAuthCodeResponseErrorsItemErrorCode": ".post_auth_code_response_errors_item_error_code",
    "PostAuthCodeResponseResponse": ".post_auth_code_response_response",
    "PostAuthenticateRequestRequest": ".post_authenticate_request_request",
    "PostAuthenticateResponse": ".post_authenticate_response",
    "PostAuthenticateResponseErrorsItem": ".post_authenticate_response_errors_item",
    "PostAuthenticateResponseErrorsItemErrorCode": ".post_authenticate_response_errors_item_error_code",
    "PostAuthenticateResponseResponse": ".post_authenticate_response_response",
    "PostAuthenticateV2RequestRequest": ".post_authenticate_v2request_request",
    "PostAuthenticateV2Response": ".post_authenticate_v2response",
    "PostAuthenticateV2ResponseErrorsItem": ".post_authenticate_v2response_errors_item",
    "PostAuthenticateV2ResponseErrorsItemErrorCode": ".post_authenticate_v2response_errors_item_error_code",
    "PostAuthenticateV2ResponseResponse": ".post_authenticate_v2response_response",
    "PostAuthenticateV2ResponseResponseConsentAction": ".post_authenticate_v2response_response_consent_action",
    "PostAuthenticateV3RequestRequest": ".post_authenticate_v3request_request",
    "PostAuthenticateV3Response": ".post_authenticate_v3response",
    "PostAuthenticateV3ResponseErrorsItem": ".post_authenticate_v3response_errors_item",
    "PostAuthenticateV3ResponseErrorsItemErrorCode": ".post_authenticate_v3response_errors_item_error_code",
    "PostAuthenticateV3ResponseResponse": ".post_authenticate_v3response_response",
    "PostAuthenticateV3ResponseResponseConsentAction": ".post_authenticate_v3response_response_consent_action",
    "PostAuthorizationLinkAuthRequestRequest": ".post_authorization_link_auth_request_request",
    "PostAuthorizationLinkAuthResponse": ".post_authorization_link_auth_response",
    "PostAuthorizationLinkAuthResponseErrorsItem": ".post_authorization_link_auth_response_errors_item",
    "PostAuthorizationLinkAuthResponseErrorsItemErrorCode": ".post_authorization_link_auth_response_errors_item_error_code",
    "PostAuthorizationLinkAuthResponseResponse": ".post_authorization_link_auth_response_response",
    "PostAuthorizationLinkStatusRequestRequest": ".post_authorization_link_status_request_request",
    "PostAuthorizationLinkStatusResponse": ".post_authorization_link_status_response",
    "PostAuthorizationLinkStatusResponseErrorsItem": ".post_authorization_link_status_response_errors_item",
    "PostAuthorizationLinkStatusResponseErrorsItemErrorCode": ".post_authorization_link_status_response_errors_item_error_code",
    "PostAuthorizationLinkStatusResponseResponse": ".post_authorization_link_status_response_response",
    "PostAuthorizationLinkStatusResponseResponseLinkStatus": ".post_authorization_link_status_response_response_link_status",
    "PostAuthorizationPrepareSignupRedirectRequestRequest": ".post_authorization_prepare_signup_redirect_request_request",
    "PostAuthorizationPrepareSignupRedirectResponse": ".post_authorization_prepare_signup_redirect_response",
    "PostAuthorizationPrepareSignupRedirectResponseErrorsItem": ".post_authorization_prepare_signup_redirect_response_errors_item",
    "PostAuthorizationPrepareSignupRedirectResponseErrorsItemErrorCode": ".post_authorization_prepare_signup_redirect_response_errors_item_error_code",
    "PostAuthorizationPrepareSignupRedirectResponseResponse": ".post_authorization_prepare_signup_redirect_response_response",
    "PostCompleteSignupRedirectRequestRequest": ".post_complete_signup_redirect_request_request",
    "PostCompleteSignupRedirectResponse": ".post_complete_signup_redirect_response",
    "PostCompleteSignupRedirectResponseErrorsItem": ".post_complete_signup_redirect_response_errors_item",
    "PostCompleteSignupRedirectResponseErrorsItemErrorCode": ".post_complete_signup_redirect_response_errors_item_error_code",
    "PostCompleteSignupRedirectResponseResponse": ".post_complete_signup_redirect_response_response",
    "PostCompleteSignupRedirectResponseResponseStatus": ".post_complete_signup_redirect_response_response_status",
    "PostOauthDetailsRequestRequest": ".post_oauth_details_request_request",
    "PostOauthDetailsResponse": ".post_oauth_details_response",
    "PostOauthDetailsResponseErrorsItem": ".post_oauth_details_response_errors_item",
    "PostOauthDetailsResponseErrorsItemErrorCode": ".post_oauth_details_response_errors_item_error_code",
    "PostOauthDetailsResponseResponse": ".post_oauth_details_response_response",
    "PostOauthDetailsV2RequestRequest": ".post_oauth_details_v2request_request",
    "PostOauthDetailsV2RequestRequestCodeChallengeMethod": ".post_oauth_details_v2request_request_code_challenge_method",
    "PostOauthDetailsV2Response": ".post_oauth_details_v2response",
    "PostOauthDetailsV2ResponseErrorsItem": ".post_oauth_details_v2response_errors_item",
    "PostOauthDetailsV2ResponseErrorsItemErrorCode": ".post_oauth_details_v2response_errors_item_error_code",
    "PostOauthDetailsV2ResponseResponse": ".post_oauth_details_v2response_response",
    "PostOauthDetailsV3RequestRequest": ".post_oauth_details_v3request_request",
    "PostOauthDetailsV3RequestRequestCodeChallengeMethod": ".post_oauth_details_v3request_request_code_challenge_method",
    "PostOauthDetailsV3Response": ".post_oauth_details_v3response",
    "PostOauthDetailsV3ResponseErrorsItem": ".post_oauth_details_v3response_errors_item",
    "PostOauthDetailsV3ResponseErrorsItemErrorCode": ".post_oauth_details_v3response_errors_item_error_code",
    "PostOauthDetailsV3ResponseResponse": ".post_oauth_details_v3response_response",
    "PostParOauthDetailsRequestRequest": ".post_par_oauth_details_request_request",
    "PostParOauthDetailsResponse": ".post_par_oauth_details_response",
    "PostParOauthDetailsResponseErrorsItem": ".post_par_oauth_details_response_errors_item",
    "PostParOauthDetailsResponseErrorsItemErrorCode": ".post_par_oauth_details_response_errors_item_error_code",
    "PostParOauthDetailsResponseResponse": ".post_par_oauth_details_response_response",
    "PostSendLinkedOtpRequestRequest": ".post_send_linked_otp_request_request",
    "PostSendLinkedOtpRequestRequestOtpChannelsItem": ".post_send_linked_otp_request_request_otp_channels_item",
    "PostSendLinkedOtpResponse": ".post_send_linked_otp_response",
    "PostSendLinkedOtpResponseErrorsItem": ".post_send_linked_otp_response_errors_item",
    "PostSendLinkedOtpResponseErrorsItemErrorCode": ".post_send_linked_otp_response_errors_item_error_code",
    "PostSendLinkedOtpResponseResponse": ".post_send_linked_otp_response_response",
    "PostSendOtpRequestRequest": ".post_send_otp_request_request",
    "PostSendOtpRequestRequestOtpChannelsItem": ".post_send_otp_request_request_otp_channels_item",
    "PostSendOtpResponse": ".post_send_otp_response",
    "PostSendOtpResponseErrorsItem": ".post_send_otp_response_errors_item",
    "PostSendOtpResponseErrorsItemErrorCode": ".post_send_otp_response_errors_item_error_code",
    "PostSendOtpResponseResponse": ".post_send_otp_response_response",
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
    "GetAuthorizationGenerateLinkCodeRequestRequest",
    "GetAuthorizationGenerateLinkCodeResponse",
    "GetAuthorizationGenerateLinkCodeResponseErrorsItem",
    "GetAuthorizationGenerateLinkCodeResponseErrorsItemErrorCode",
    "GetAuthorizationGenerateLinkCodeResponseResponse",
    "GetConsentDetailsResponse",
    "GetConsentDetailsResponseErrorsItem",
    "GetConsentDetailsResponseErrorsItemErrorCode",
    "GetConsentDetailsResponseResponse",
    "GetConsentDetailsResponseResponseConsentAction",
    "PostAuthCodeRequestRequest",
    "PostAuthCodeResponse",
    "PostAuthCodeResponseErrorsItem",
    "PostAuthCodeResponseErrorsItemErrorCode",
    "PostAuthCodeResponseResponse",
    "PostAuthenticateRequestRequest",
    "PostAuthenticateResponse",
    "PostAuthenticateResponseErrorsItem",
    "PostAuthenticateResponseErrorsItemErrorCode",
    "PostAuthenticateResponseResponse",
    "PostAuthenticateV2RequestRequest",
    "PostAuthenticateV2Response",
    "PostAuthenticateV2ResponseErrorsItem",
    "PostAuthenticateV2ResponseErrorsItemErrorCode",
    "PostAuthenticateV2ResponseResponse",
    "PostAuthenticateV2ResponseResponseConsentAction",
    "PostAuthenticateV3RequestRequest",
    "PostAuthenticateV3Response",
    "PostAuthenticateV3ResponseErrorsItem",
    "PostAuthenticateV3ResponseErrorsItemErrorCode",
    "PostAuthenticateV3ResponseResponse",
    "PostAuthenticateV3ResponseResponseConsentAction",
    "PostAuthorizationLinkAuthRequestRequest",
    "PostAuthorizationLinkAuthResponse",
    "PostAuthorizationLinkAuthResponseErrorsItem",
    "PostAuthorizationLinkAuthResponseErrorsItemErrorCode",
    "PostAuthorizationLinkAuthResponseResponse",
    "PostAuthorizationLinkStatusRequestRequest",
    "PostAuthorizationLinkStatusResponse",
    "PostAuthorizationLinkStatusResponseErrorsItem",
    "PostAuthorizationLinkStatusResponseErrorsItemErrorCode",
    "PostAuthorizationLinkStatusResponseResponse",
    "PostAuthorizationLinkStatusResponseResponseLinkStatus",
    "PostAuthorizationPrepareSignupRedirectRequestRequest",
    "PostAuthorizationPrepareSignupRedirectResponse",
    "PostAuthorizationPrepareSignupRedirectResponseErrorsItem",
    "PostAuthorizationPrepareSignupRedirectResponseErrorsItemErrorCode",
    "PostAuthorizationPrepareSignupRedirectResponseResponse",
    "PostCompleteSignupRedirectRequestRequest",
    "PostCompleteSignupRedirectResponse",
    "PostCompleteSignupRedirectResponseErrorsItem",
    "PostCompleteSignupRedirectResponseErrorsItemErrorCode",
    "PostCompleteSignupRedirectResponseResponse",
    "PostCompleteSignupRedirectResponseResponseStatus",
    "PostOauthDetailsRequestRequest",
    "PostOauthDetailsResponse",
    "PostOauthDetailsResponseErrorsItem",
    "PostOauthDetailsResponseErrorsItemErrorCode",
    "PostOauthDetailsResponseResponse",
    "PostOauthDetailsV2RequestRequest",
    "PostOauthDetailsV2RequestRequestCodeChallengeMethod",
    "PostOauthDetailsV2Response",
    "PostOauthDetailsV2ResponseErrorsItem",
    "PostOauthDetailsV2ResponseErrorsItemErrorCode",
    "PostOauthDetailsV2ResponseResponse",
    "PostOauthDetailsV3RequestRequest",
    "PostOauthDetailsV3RequestRequestCodeChallengeMethod",
    "PostOauthDetailsV3Response",
    "PostOauthDetailsV3ResponseErrorsItem",
    "PostOauthDetailsV3ResponseErrorsItemErrorCode",
    "PostOauthDetailsV3ResponseResponse",
    "PostParOauthDetailsRequestRequest",
    "PostParOauthDetailsResponse",
    "PostParOauthDetailsResponseErrorsItem",
    "PostParOauthDetailsResponseErrorsItemErrorCode",
    "PostParOauthDetailsResponseResponse",
    "PostSendLinkedOtpRequestRequest",
    "PostSendLinkedOtpRequestRequestOtpChannelsItem",
    "PostSendLinkedOtpResponse",
    "PostSendLinkedOtpResponseErrorsItem",
    "PostSendLinkedOtpResponseErrorsItemErrorCode",
    "PostSendLinkedOtpResponseResponse",
    "PostSendOtpRequestRequest",
    "PostSendOtpRequestRequestOtpChannelsItem",
    "PostSendOtpResponse",
    "PostSendOtpResponseErrorsItem",
    "PostSendOtpResponseErrorsItemErrorCode",
    "PostSendOtpResponseResponse",
]
