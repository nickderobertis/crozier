

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUiClient, RawUiClient
from .types.get_authorization_generate_link_code_request_request import GetAuthorizationGenerateLinkCodeRequestRequest
from .types.get_authorization_generate_link_code_response import GetAuthorizationGenerateLinkCodeResponse
from .types.get_consent_details_response import GetConsentDetailsResponse
from .types.post_auth_code_request_request import PostAuthCodeRequestRequest
from .types.post_auth_code_response import PostAuthCodeResponse
from .types.post_authenticate_request_request import PostAuthenticateRequestRequest
from .types.post_authenticate_response import PostAuthenticateResponse
from .types.post_authenticate_v2request_request import PostAuthenticateV2RequestRequest
from .types.post_authenticate_v2response import PostAuthenticateV2Response
from .types.post_authenticate_v3request_request import PostAuthenticateV3RequestRequest
from .types.post_authenticate_v3response import PostAuthenticateV3Response
from .types.post_authorization_link_auth_request_request import PostAuthorizationLinkAuthRequestRequest
from .types.post_authorization_link_auth_response import PostAuthorizationLinkAuthResponse
from .types.post_authorization_link_status_request_request import PostAuthorizationLinkStatusRequestRequest
from .types.post_authorization_link_status_response import PostAuthorizationLinkStatusResponse
from .types.post_authorization_prepare_signup_redirect_request_request import (
    PostAuthorizationPrepareSignupRedirectRequestRequest,
)
from .types.post_authorization_prepare_signup_redirect_response import PostAuthorizationPrepareSignupRedirectResponse
from .types.post_complete_signup_redirect_request_request import PostCompleteSignupRedirectRequestRequest
from .types.post_complete_signup_redirect_response import PostCompleteSignupRedirectResponse
from .types.post_oauth_details_request_request import PostOauthDetailsRequestRequest
from .types.post_oauth_details_response import PostOauthDetailsResponse
from .types.post_oauth_details_v2request_request import PostOauthDetailsV2RequestRequest
from .types.post_oauth_details_v2response import PostOauthDetailsV2Response
from .types.post_oauth_details_v3request_request import PostOauthDetailsV3RequestRequest
from .types.post_oauth_details_v3response import PostOauthDetailsV3Response
from .types.post_par_oauth_details_request_request import PostParOauthDetailsRequestRequest
from .types.post_par_oauth_details_response import PostParOauthDetailsResponse
from .types.post_send_linked_otp_request_request import PostSendLinkedOtpRequestRequest
from .types.post_send_linked_otp_response import PostSendLinkedOtpResponse
from .types.post_send_otp_request_request import PostSendOtpRequestRequest
from .types.post_send_otp_response import PostSendOtpResponse


OMIT = typing.cast(typing.Any, ...)


class UiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUiClient
        """
        return self._raw_client

    def post_oauth_details(
        self,
        *,
        xsrf_token: str,
        request_time: str,
        request: PostOauthDetailsRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOauthDetailsResponse:
        """
        OAuth details request is raised from the UI JS application on page load.

        OAuth details endpoint validates the provided request parameters and resolves the required authentication factors. Combination of resolved authentication factors and the consent details are sent back as response with a unique transactionId.

        The transcationId in the response is used to identify/maintain the end user pre-auth session. This pre-auth session has timeout (configurable in Idp service).

        All the query params passed to /authorize API MUST be sent to /oauth-details endpoint. All these parameters will be validated in IdP before returning success response.

        1. Validates the clientId.
        2. validates redirectUri is one of the redirectUri during client create/update.
        3. validates display,responseType,prompts values are part of supported values in Idp properties.
        4. scope / acrValues / claims / locales / claim_locales - unknown values are ignored. Only valid values are considered.
        5. scopes like profile, email and phone are allowed only if "openid" is also part of the requested scope.
        6. Claims request parameter is allowed, only if 'openid' is part of the scope request parameter
        7. Claims considered only if part of registered claims.
        8. ACR in claims request parameter is given the first priority over acr_values query parameter. if none of them are part of the registered acrs, registered ACRs are only considered to derive the auth factors.

        Parameters
        ----------
        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostOauthDetailsRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauthDetailsResponse
            OK

        Examples
        --------
        from fern.ui import PostOauthDetailsRequestRequest

        from fern import Claim, ClaimDetail, ClaimUserinfo, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_oauth_details(
            xsrf_token="X-XSRF-TOKEN",
            request_time="2022-09-22T08:01:10.000Z",
            request=PostOauthDetailsRequestRequest(
                scope="openid profile",
                response_type="code",
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                redirect_uri="https://fastlane.com/homepage",
                state="eree2311",
                nonce="973eieljzng",
                display="popup",
                prompt="login",
                acr_values="mosip:idp:acr:generated-code",
                claims=Claim(
                    userinfo=ClaimUserinfo(
                        name=ClaimDetail(
                            essential=True,
                        ),
                        email=ClaimDetail(
                            essential=False,
                        ),
                        phone_number=ClaimDetail(
                            essential=True,
                        ),
                        address=ClaimDetail(
                            essential=True,
                        ),
                    ),
                ),
                claims_locales="en",
            ),
        )
        """
        _response = self._raw_client.post_oauth_details(
            xsrf_token=xsrf_token, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_oauth_details_v2(
        self,
        *,
        xsrf_token: str,
        request_time: str,
        request: PostOauthDetailsV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOauthDetailsV2Response:
        """
        OAuth details request is raised from the UI JS application on page load.

        OAuth details endpoint validates the provided request parameters and resolves the required authentication factors. Combination of resolved authentication factors and the consent details are sent back as response with a unique transactionId.

        The transcationId in the response is used to identify/maintain the end user pre-auth session. This pre-auth session has timeout (configurable in Idp service).

        All the query params passed to /authorize API MUST be sent to /oauth-details endpoint. All these parameters will be validated in IdP before returning success response.

        1. Validates the clientId.
        2. validates redirectUri is one of the redirectUri during client create/update.
        3. validates display,responseType,prompts values are part of supported values in Idp properties.
        4. scope / acrValues / claims / locales / claim_locales - unknown values are ignored. Only valid values are considered.
        5. scopes like profile, email and phone are allowed only if "openid" is also part of the requested scope.
        6. Claims request parameter is allowed, only if 'openid' is part of the scope request parameter
        7. claims considered only if part of registered claims.
        8. ACR in claims request parameter is given the first priority over acr_values query parameter. if none of them are part of the registered acrs, registered ACRs are only considered to derive the auth factors.

        Parameters
        ----------
        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostOauthDetailsV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauthDetailsV2Response
            OK

        Examples
        --------
        from fern.ui import (
            PostOauthDetailsV2RequestRequest,
            PostOauthDetailsV2RequestRequestCodeChallengeMethod,
        )

        from fern import Claim, ClaimDetail, ClaimUserinfo, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_oauth_details_v2(
            xsrf_token="X-XSRF-TOKEN",
            request_time="2022-09-22T08:01:10.000Z",
            request=PostOauthDetailsV2RequestRequest(
                scope="openid profile",
                response_type="code",
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                redirect_uri="https://fastlane.com/homepage",
                state="eree2311",
                nonce="973eieljzng",
                display="popup",
                prompt="login",
                acr_values="mosip:idp:acr:generated-code",
                claims=Claim(
                    userinfo=ClaimUserinfo(
                        name=ClaimDetail(
                            essential=True,
                        ),
                        email=ClaimDetail(
                            essential=False,
                        ),
                        phone_number=ClaimDetail(
                            essential=True,
                        ),
                        address=ClaimDetail(
                            essential=True,
                        ),
                    ),
                ),
                claims_locales="en",
                code_challenge="UK95aVX_y3R44DF3hssd3wATvtZmO_WejE0P33-pwTs",
                code_challenge_method=PostOauthDetailsV2RequestRequestCodeChallengeMethod.S256,
            ),
        )
        """
        _response = self._raw_client.post_oauth_details_v2(
            xsrf_token=xsrf_token, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_oauth_details_v3(
        self,
        *,
        xsrf_token: str,
        request_time: str,
        request: PostOauthDetailsV3RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOauthDetailsV3Response:
        """
        OAuth details request is raised from the UI JS application on page load.

        OAuth details endpoint validates the provided request parameters and resolves the required authentication factors. Combination of resolved authentication factors and the consent details are sent back as response with a unique transactionId.

        The transcationId in the response is used to identify/maintain the end user pre-auth session. This pre-auth session has timeout (configurable in Idp service).

        All the query params passed to /authorize API MUST be sent to /oauth-details endpoint. All these parameters will be validated in IdP before returning success response.

        1. Validates the clientId.
        2. validates redirectUri is one of the redirectUri during client create/update.
        3. validates display,responseType,prompts values are part of supported values in Idp properties.
        4. scope / acrValues / claims / locales / claim_locales - unknown values are ignored. Only valid values are considered.
        5. scopes like profile, email and phone are allowed only if "openid" is also part of the requested scope.
        6. Claims request parameter is allowed, only if 'openid' is part of the scope request parameter
        7. claims considered only if part of registered claims.
        8. ACR in claims request parameter is given the first priority over acr_values query parameter. if none of them are part of the registered acrs, registered ACRs are only considered to derive the auth factors.
        9. Unknown or unsupported claims in the verified_claims parameter are ignored.
        10. idTokenHint is optional, if provided then it MUST be a valid JWT. 'sub' claim in the idTokenHint JWT payload must match the cookie name(set on the domain).If the cookie is not found with same name as of 'sub' claim, then the error is thrown.

        Parameters
        ----------
        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostOauthDetailsV3RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauthDetailsV3Response
            OK

        Examples
        --------
        from fern.ui import (
            PostOauthDetailsV3RequestRequest,
            PostOauthDetailsV3RequestRequestCodeChallengeMethod,
        )

        from fern import Claim, ClaimDetail, ClaimUserinfo, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_oauth_details_v3(
            xsrf_token="X-XSRF-TOKEN",
            request_time="2022-09-22T08:01:10.000Z",
            request=PostOauthDetailsV3RequestRequest(
                scope="openid profile",
                response_type="code",
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                redirect_uri="https://fastlane.com/homepage",
                state="eree2311",
                nonce="973eieljzng",
                display="popup",
                prompt="login",
                acr_values="mosip:idp:acr:generated-code",
                claims=Claim(
                    userinfo=ClaimUserinfo(
                        name=ClaimDetail(
                            essential=True,
                        ),
                        email=ClaimDetail(
                            essential=False,
                        ),
                        phone_number=ClaimDetail(
                            essential=True,
                        ),
                        address=ClaimDetail(
                            essential=True,
                        ),
                    ),
                ),
                claims_locales="en",
                code_challenge="UK95aVX_y3R44DF3hssd3wATvtZmO_WejE0P33-pwTs",
                code_challenge_method=PostOauthDetailsV3RequestRequestCodeChallengeMethod.S256,
            ),
        )
        """
        _response = self._raw_client.post_oauth_details_v3(
            xsrf_token=xsrf_token, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_send_otp(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostSendOtpRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostSendOtpResponse:
        """
        When end user want to authenticate using OTP auth factor, he/she will enter their individual id (UIN/VID) and click on the "Generate OTP" button on the UI application. Then this endpoint will be invoked by the JS UI application.

        Since the OTP generation and delivery to end user is to be handled by the integrated authentication system, the request will be relayed to the same.

        1. Validates the transactionId.
        2. Validates null / empty individualId.
        3. Validates captchaToken, if enabled.
        3. Delegates the call to integrated authentication system.
        4. Relays error from authentication system to UI on failure.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostSendOtpRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostSendOtpResponse
            OK

        Examples
        --------
        import datetime

        from fern.ui import (
            PostSendOtpRequestRequest,
            PostSendOtpRequestRequestOtpChannelsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_send_otp(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:10+00:00",
            ),
            request=PostSendOtpRequestRequest(
                transaction_id="vKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                individual_id="464737289558",
                otp_channels=[
                    PostSendOtpRequestRequestOtpChannelsItem.PHONE,
                    PostSendOtpRequestRequestOtpChannelsItem.EMAIL,
                ],
                captcha_token="ALSKDJFURIEOQPZMKFURHFVBH",
            ),
        )
        """
        _response = self._raw_client.post_send_otp(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def post_send_linked_otp(
        self,
        *,
        request_time: dt.datetime,
        request: PostSendLinkedOtpRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostSendLinkedOtpResponse:
        """
        When end user want to authenticate using OTP auth factor, he/she will enter their individual id (UIN/VID) and click on the "Generate OTP" button on the UI application. Then this endpoint will be invoked by wallet app with linked transactionId.

        Since the OTP generation and delivery to end user is to be handled by the integrated authentication system, the request will be relayed to the same.

        1. Validates the linked transactionId.
        2. Validates null / empty individualId.
        3. Delegates the call to integrated authentication system.
        4. Relays error from authentication system to UI on failure.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostSendLinkedOtpRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostSendLinkedOtpResponse
            OK

        Examples
        --------
        import datetime

        from fern.ui import (
            PostSendLinkedOtpRequestRequest,
            PostSendLinkedOtpRequestRequestOtpChannelsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_send_linked_otp(
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:10+00:00",
            ),
            request=PostSendLinkedOtpRequestRequest(
                transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                individual_id="464737289558",
                otp_channels=[
                    PostSendLinkedOtpRequestRequestOtpChannelsItem.PHONE,
                    PostSendLinkedOtpRequestRequestOtpChannelsItem.EMAIL,
                ],
            ),
        )
        """
        _response = self._raw_client.post_send_linked_otp(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_authenticate(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostAuthenticateRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthenticateResponse:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the UI application, this endpoint will be invoked.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates transactionId/linkTransactionId.
        2. Validates null / empty individualId.
        3. Invokes kyc-auth call to integrated authentication server (IDA).
        4. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: Only transaction Id is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostAuthenticateRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthenticateResponse
            OK

        Examples
        --------
        import datetime

        from fern.ui import PostAuthenticateRequestRequest

        from fern import (
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_authenticate(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:10+00:00",
            ),
            request=PostAuthenticateRequestRequest(
                transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                individual_id="464737289558",
                challenge_list=[
                    AuthChallenge(
                        auth_factor_type=AuthChallengeAuthFactorType.OTP,
                        challenge="111111",
                        format=AuthChallengeFormat.ALPHA_NUMERIC,
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.post_authenticate(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def post_authenticate_v2(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostAuthenticateV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthenticateV2Response:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the UI application, this endpoint will be invoked.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates transactionId/linkTransactionId.
        2. Validates null / empty individualId.
        3. Invokes kyc-auth call to integrated authentication server (IDA).
        4. It validates stored userconsent against the requested claims and scopes
        5. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: transaction Id and consentAction is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostAuthenticateV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthenticateV2Response
            OK

        Examples
        --------
        import datetime

        from fern.ui import PostAuthenticateV2RequestRequest

        from fern import (
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_authenticate_v2(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:10+00:00",
            ),
            request=PostAuthenticateV2RequestRequest(
                transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                individual_id="464737289558",
                challenge_list=[
                    AuthChallenge(
                        auth_factor_type=AuthChallengeAuthFactorType.OTP,
                        challenge="111111",
                        format=AuthChallengeFormat.ALPHA_NUMERIC,
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.post_authenticate_v2(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def post_authenticate_v3(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostAuthenticateV3RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthenticateV3Response:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the UI application, this endpoint will be invoked.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates transactionId/linkTransactionId.
        2. Validated the provided captcha token - if the provided auth-factor is configured to be with captcha.
        3. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. It validates stored userconsent against the requested claims and scopes
        6. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: transaction Id and consentAction is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostAuthenticateV3RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthenticateV3Response
            OK

        Examples
        --------
        import datetime

        from fern.ui import PostAuthenticateV3RequestRequest

        from fern import (
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_authenticate_v3(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:10+00:00",
            ),
            request=PostAuthenticateV3RequestRequest(
                transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                individual_id="464737289558",
                challenge_list=[
                    AuthChallenge(
                        auth_factor_type=AuthChallengeAuthFactorType.OTP,
                        challenge="111111",
                        format=AuthChallengeFormat.ALPHA_NUMERIC,
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.post_authenticate_v3(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def post_auth_code(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostAuthCodeRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthCodeResponse:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the UI application to send the accepted consent and permitted scopes.

        Then UI application will receive the authorization code and few other details required for redirecting to the client / relying party application.

        1. Validates transactionId. If valid, stores the accepted claims and permitted scopes in the cache and returns back the authorization code.
        2. Validate accepted claims and permitted scopes in the request.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostAuthCodeRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthCodeResponse
            OK

        Examples
        --------
        import datetime

        from fern.ui import PostAuthCodeRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_auth_code(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:10+00:00",
            ),
            request=PostAuthCodeRequestRequest(
                transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                permitted_authorize_scopes=["permittedAuthorizeScopes"],
                accepted_claims=["name", "email", "phone_number"],
            ),
        )
        """
        _response = self._raw_client.post_auth_code(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def get_authorization_generate_link_code(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: GetAuthorizationGenerateLinkCodeRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAuthorizationGenerateLinkCodeResponse:
        """
        Generate link code request is raised from JS application.

        1. JS application creates a deeplink with this link-code as parameter.
        2. This deeplink is embedded in a Machine-readable-code and the same is rendered in the UI.
        3. End user scans this machine-readable-code to open wallet app.
        4. On open of wallet-app, wallet-app invokes /link-transaction endpoint.
        5. In the JS application, once machine-readable-code is rendered, at the same time /link-status endpoint is invoked as a polling request.

        **Configuration to decide the expire date time of linkCode**: mosip.idp.link-code-expire-in-secs

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : GetAuthorizationGenerateLinkCodeRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAuthorizationGenerateLinkCodeResponse
            OK

        Examples
        --------
        from fern.ui import GetAuthorizationGenerateLinkCodeRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.get_authorization_generate_link_code(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time="2023-09-22T08:01:10.000Z",
            request=GetAuthorizationGenerateLinkCodeRequestRequest(
                transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
            ),
        )
        """
        _response = self._raw_client.get_authorization_generate_link_code(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def post_authorization_link_status(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: PostAuthorizationLinkStatusRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationLinkStatusResponse:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostAuthorizationLinkStatusRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationLinkStatusResponse
            OK

        Examples
        --------
        from fern.ui import PostAuthorizationLinkStatusRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_authorization_link_status(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time="2023-09-22T08:01:10.000Z",
            request=PostAuthorizationLinkStatusRequestRequest(
                transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                link_code="xl4cnYtLQkGRxUj",
            ),
        )
        """
        _response = self._raw_client.post_authorization_link_status(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def post_authorization_link_auth(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: PostAuthorizationLinkAuthRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationLinkAuthResponse:
        """
        Link authorization code endpoint is invoked from JS application.

        1. This is a Long polling request to IdP-service.
        2. validates the transactionId
        3. validates the linkCode if its LINKED.
        4. checks the cache to see if the auth-code is generated, if yes returns the response.
        5. If the auth-code is not yet generated, polling request waits for the configured time.
        6. On successful response, IdP-UI should redirect to the provided redirectUri and auth-code or errors.


        **Configuration to decide the wait interval**: mosip.idp.link-auth-code-deferred-response-timeout-secs

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostAuthorizationLinkAuthRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationLinkAuthResponse
            OK

        Examples
        --------
        from fern.ui import PostAuthorizationLinkAuthRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_authorization_link_auth(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time="2023-09-22T08:01:13.000Z",
            request=PostAuthorizationLinkAuthRequestRequest(
                transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                linked_code="xl4cnYtLQkGRxUj",
            ),
        )
        """
        _response = self._raw_client.post_authorization_link_auth(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def get_consent_details(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConsentDetailsResponse:
        """
        **Prerequisites:**
        1. Request should have valid authenticated transaction id in the header `oauth-details-key`

        **Validations:**
        1. validate the transaction ID in the header.

        Once the end user is successfully authenticated, GET consent-details endpoint is invoked to get details about the claims and consent action.


        **Background:**
        During kyc-auth, integrated ID system should return the list of claim details for the authenticated end user.
        We have introduced new method in the `Authenticator` plugin. New kycAuth method will be invoked only when verified claims are requested by the relying party.
        Claims details returned during the kcy-auth is cached in the `OIDCTransaction` to give out during fetch claim details call.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConsentDetailsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.get_consent_details(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
        )
        """
        _response = self._raw_client.get_consent_details(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_options=request_options,
        )
        return _response.data

    def post_authorization_prepare_signup_redirect(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: PostAuthorizationPrepareSignupRedirectRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationPrepareSignupRedirectResponse:
        """
        **Prerequisite**:
        1. User should be authenticated to invoke prepare-signup-redirect endpoint.
        2. signup-service should be registered as OAUTH client with esignet. And the signup-service's OAuth client id should be configured in this property `mosip.esignet.signup-id-token-audience` and the expire time of the generated ID token depends on below property `mosip.esignet.signup-id-token-expire-seconds`.


        **Validations:**
        1. Validates the input transactionID.
        2. Validates if the transaction requires profile update.


        When this endpoint is invoked, generates the ID-token for "singup-service". and sets the cookie header is also set with cookie name as UUID same as the subject of the ID token ( eg: "d898375b-c883-4408-a9e3-f629f15c1298") and the cookie value is a encoded json:
          `{"code" :"secret code to match with the server", "path-fragment": "path to resume after profile update"}`

        ID token payload is as below
         `{ "iss": "https://esignet.dev.mosip.net", "iat": 1715047546, "exp": 1746583546, "aud": "signup-service-client-id", "sub": "d898375b-c883-4408-a9e3-f629f15c1298" }`

         **Note**: Cookie created expire time should be equal to the expire time if generated ID token.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str
            <yyyy-MM-dd'T'HH:mm:ss.SSS'Z'>

        request : PostAuthorizationPrepareSignupRedirectRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationPrepareSignupRedirectResponse
            OK

        Examples
        --------
        from fern.ui import PostAuthorizationPrepareSignupRedirectRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_authorization_prepare_signup_redirect(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time="requestTime",
            request=PostAuthorizationPrepareSignupRedirectRequestRequest(
                transaction_id="transactionId",
                path_fragment="pathFragment",
            ),
        )
        """
        _response = self._raw_client.post_authorization_prepare_signup_redirect(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def post_complete_signup_redirect(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: PostCompleteSignupRedirectRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostCompleteSignupRedirectResponse:
        """
        This endpoint resumes the halted OIDC transactions halted and marks the completion of the identify verification process.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str
            <yyyy-MM-dd'T'HH:mm:ss.SSS'Z'>

        request : PostCompleteSignupRedirectRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostCompleteSignupRedirectResponse
            OK

        Examples
        --------
        from fern.ui import PostCompleteSignupRedirectRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_complete_signup_redirect(
            oauth_details_hash="oauth-details-hash",
            oauth_details_key="oauth-details-key",
            xsrf_token="X-XSRF-TOKEN",
            request_time="2023-09-22T08:01:10.000Z",
            request=PostCompleteSignupRedirectRequestRequest(
                transaction_id="vKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
            ),
        )
        """
        _response = self._raw_client.post_complete_signup_redirect(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def post_par_oauth_details(
        self,
        *,
        xsrf_token: str,
        request_time: str,
        request: PostParOauthDetailsRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostParOauthDetailsResponse:
        """
        PAR OAuth details request is raised from the UI JS application on page load, only when request_uri is part of the authorize URL.
        OAuth details endpoint validates the provided request parameters.

        Resolved authentication factors and the consent details are sent back as response with a unique transactionId.

        The transcationId in the response is used to identify/maintain the end user pre-auth session.
        This pre-auth session has timeout (configurable).

        1. Validates the clientId.
        2. Validate the request_uri, if an entry is not found in the "par" cache, reject the request.
        3. Upon successful validation, move the object from "par" cache to "preauth" cache.
        4. Ignore unknown parameters in the request.
        5. In the existing oauth-details(v1,v2 & v3) endpoint, clients with **mandate_par_flow** set to true, but still using authorize without request_uri should be rejected.

        Parameters
        ----------
        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostParOauthDetailsRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostParOauthDetailsResponse
            OK

        Examples
        --------
        from fern.ui import PostParOauthDetailsRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ui.post_par_oauth_details(
            xsrf_token="X-XSRF-TOKEN",
            request_time="2022-09-22T08:01:10.000Z",
            request=PostParOauthDetailsRequestRequest(
                request_uri="urn:ietf:params:oauth:request_uri:XiaVWGcLVPNxTNSAddv",
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
            ),
        )
        """
        _response = self._raw_client.post_par_oauth_details(
            xsrf_token=xsrf_token, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data


class AsyncUiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUiClient
        """
        return self._raw_client

    async def post_oauth_details(
        self,
        *,
        xsrf_token: str,
        request_time: str,
        request: PostOauthDetailsRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOauthDetailsResponse:
        """
        OAuth details request is raised from the UI JS application on page load.

        OAuth details endpoint validates the provided request parameters and resolves the required authentication factors. Combination of resolved authentication factors and the consent details are sent back as response with a unique transactionId.

        The transcationId in the response is used to identify/maintain the end user pre-auth session. This pre-auth session has timeout (configurable in Idp service).

        All the query params passed to /authorize API MUST be sent to /oauth-details endpoint. All these parameters will be validated in IdP before returning success response.

        1. Validates the clientId.
        2. validates redirectUri is one of the redirectUri during client create/update.
        3. validates display,responseType,prompts values are part of supported values in Idp properties.
        4. scope / acrValues / claims / locales / claim_locales - unknown values are ignored. Only valid values are considered.
        5. scopes like profile, email and phone are allowed only if "openid" is also part of the requested scope.
        6. Claims request parameter is allowed, only if 'openid' is part of the scope request parameter
        7. Claims considered only if part of registered claims.
        8. ACR in claims request parameter is given the first priority over acr_values query parameter. if none of them are part of the registered acrs, registered ACRs are only considered to derive the auth factors.

        Parameters
        ----------
        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostOauthDetailsRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauthDetailsResponse
            OK

        Examples
        --------
        import asyncio

        from fern.ui import PostOauthDetailsRequestRequest

        from fern import AsyncFernApi, Claim, ClaimDetail, ClaimUserinfo

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_oauth_details(
                xsrf_token="X-XSRF-TOKEN",
                request_time="2022-09-22T08:01:10.000Z",
                request=PostOauthDetailsRequestRequest(
                    scope="openid profile",
                    response_type="code",
                    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                    redirect_uri="https://fastlane.com/homepage",
                    state="eree2311",
                    nonce="973eieljzng",
                    display="popup",
                    prompt="login",
                    acr_values="mosip:idp:acr:generated-code",
                    claims=Claim(
                        userinfo=ClaimUserinfo(
                            name=ClaimDetail(
                                essential=True,
                            ),
                            email=ClaimDetail(
                                essential=False,
                            ),
                            phone_number=ClaimDetail(
                                essential=True,
                            ),
                            address=ClaimDetail(
                                essential=True,
                            ),
                        ),
                    ),
                    claims_locales="en",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_oauth_details(
            xsrf_token=xsrf_token, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_oauth_details_v2(
        self,
        *,
        xsrf_token: str,
        request_time: str,
        request: PostOauthDetailsV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOauthDetailsV2Response:
        """
        OAuth details request is raised from the UI JS application on page load.

        OAuth details endpoint validates the provided request parameters and resolves the required authentication factors. Combination of resolved authentication factors and the consent details are sent back as response with a unique transactionId.

        The transcationId in the response is used to identify/maintain the end user pre-auth session. This pre-auth session has timeout (configurable in Idp service).

        All the query params passed to /authorize API MUST be sent to /oauth-details endpoint. All these parameters will be validated in IdP before returning success response.

        1. Validates the clientId.
        2. validates redirectUri is one of the redirectUri during client create/update.
        3. validates display,responseType,prompts values are part of supported values in Idp properties.
        4. scope / acrValues / claims / locales / claim_locales - unknown values are ignored. Only valid values are considered.
        5. scopes like profile, email and phone are allowed only if "openid" is also part of the requested scope.
        6. Claims request parameter is allowed, only if 'openid' is part of the scope request parameter
        7. claims considered only if part of registered claims.
        8. ACR in claims request parameter is given the first priority over acr_values query parameter. if none of them are part of the registered acrs, registered ACRs are only considered to derive the auth factors.

        Parameters
        ----------
        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostOauthDetailsV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauthDetailsV2Response
            OK

        Examples
        --------
        import asyncio

        from fern.ui import (
            PostOauthDetailsV2RequestRequest,
            PostOauthDetailsV2RequestRequestCodeChallengeMethod,
        )

        from fern import AsyncFernApi, Claim, ClaimDetail, ClaimUserinfo

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_oauth_details_v2(
                xsrf_token="X-XSRF-TOKEN",
                request_time="2022-09-22T08:01:10.000Z",
                request=PostOauthDetailsV2RequestRequest(
                    scope="openid profile",
                    response_type="code",
                    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                    redirect_uri="https://fastlane.com/homepage",
                    state="eree2311",
                    nonce="973eieljzng",
                    display="popup",
                    prompt="login",
                    acr_values="mosip:idp:acr:generated-code",
                    claims=Claim(
                        userinfo=ClaimUserinfo(
                            name=ClaimDetail(
                                essential=True,
                            ),
                            email=ClaimDetail(
                                essential=False,
                            ),
                            phone_number=ClaimDetail(
                                essential=True,
                            ),
                            address=ClaimDetail(
                                essential=True,
                            ),
                        ),
                    ),
                    claims_locales="en",
                    code_challenge="UK95aVX_y3R44DF3hssd3wATvtZmO_WejE0P33-pwTs",
                    code_challenge_method=PostOauthDetailsV2RequestRequestCodeChallengeMethod.S256,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_oauth_details_v2(
            xsrf_token=xsrf_token, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_oauth_details_v3(
        self,
        *,
        xsrf_token: str,
        request_time: str,
        request: PostOauthDetailsV3RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOauthDetailsV3Response:
        """
        OAuth details request is raised from the UI JS application on page load.

        OAuth details endpoint validates the provided request parameters and resolves the required authentication factors. Combination of resolved authentication factors and the consent details are sent back as response with a unique transactionId.

        The transcationId in the response is used to identify/maintain the end user pre-auth session. This pre-auth session has timeout (configurable in Idp service).

        All the query params passed to /authorize API MUST be sent to /oauth-details endpoint. All these parameters will be validated in IdP before returning success response.

        1. Validates the clientId.
        2. validates redirectUri is one of the redirectUri during client create/update.
        3. validates display,responseType,prompts values are part of supported values in Idp properties.
        4. scope / acrValues / claims / locales / claim_locales - unknown values are ignored. Only valid values are considered.
        5. scopes like profile, email and phone are allowed only if "openid" is also part of the requested scope.
        6. Claims request parameter is allowed, only if 'openid' is part of the scope request parameter
        7. claims considered only if part of registered claims.
        8. ACR in claims request parameter is given the first priority over acr_values query parameter. if none of them are part of the registered acrs, registered ACRs are only considered to derive the auth factors.
        9. Unknown or unsupported claims in the verified_claims parameter are ignored.
        10. idTokenHint is optional, if provided then it MUST be a valid JWT. 'sub' claim in the idTokenHint JWT payload must match the cookie name(set on the domain).If the cookie is not found with same name as of 'sub' claim, then the error is thrown.

        Parameters
        ----------
        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostOauthDetailsV3RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauthDetailsV3Response
            OK

        Examples
        --------
        import asyncio

        from fern.ui import (
            PostOauthDetailsV3RequestRequest,
            PostOauthDetailsV3RequestRequestCodeChallengeMethod,
        )

        from fern import AsyncFernApi, Claim, ClaimDetail, ClaimUserinfo

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_oauth_details_v3(
                xsrf_token="X-XSRF-TOKEN",
                request_time="2022-09-22T08:01:10.000Z",
                request=PostOauthDetailsV3RequestRequest(
                    scope="openid profile",
                    response_type="code",
                    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                    redirect_uri="https://fastlane.com/homepage",
                    state="eree2311",
                    nonce="973eieljzng",
                    display="popup",
                    prompt="login",
                    acr_values="mosip:idp:acr:generated-code",
                    claims=Claim(
                        userinfo=ClaimUserinfo(
                            name=ClaimDetail(
                                essential=True,
                            ),
                            email=ClaimDetail(
                                essential=False,
                            ),
                            phone_number=ClaimDetail(
                                essential=True,
                            ),
                            address=ClaimDetail(
                                essential=True,
                            ),
                        ),
                    ),
                    claims_locales="en",
                    code_challenge="UK95aVX_y3R44DF3hssd3wATvtZmO_WejE0P33-pwTs",
                    code_challenge_method=PostOauthDetailsV3RequestRequestCodeChallengeMethod.S256,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_oauth_details_v3(
            xsrf_token=xsrf_token, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_send_otp(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostSendOtpRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostSendOtpResponse:
        """
        When end user want to authenticate using OTP auth factor, he/she will enter their individual id (UIN/VID) and click on the "Generate OTP" button on the UI application. Then this endpoint will be invoked by the JS UI application.

        Since the OTP generation and delivery to end user is to be handled by the integrated authentication system, the request will be relayed to the same.

        1. Validates the transactionId.
        2. Validates null / empty individualId.
        3. Validates captchaToken, if enabled.
        3. Delegates the call to integrated authentication system.
        4. Relays error from authentication system to UI on failure.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostSendOtpRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostSendOtpResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.ui import (
            PostSendOtpRequestRequest,
            PostSendOtpRequestRequestOtpChannelsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_send_otp(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:10+00:00",
                ),
                request=PostSendOtpRequestRequest(
                    transaction_id="vKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                    individual_id="464737289558",
                    otp_channels=[
                        PostSendOtpRequestRequestOtpChannelsItem.PHONE,
                        PostSendOtpRequestRequestOtpChannelsItem.EMAIL,
                    ],
                    captcha_token="ALSKDJFURIEOQPZMKFURHFVBH",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_send_otp(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def post_send_linked_otp(
        self,
        *,
        request_time: dt.datetime,
        request: PostSendLinkedOtpRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostSendLinkedOtpResponse:
        """
        When end user want to authenticate using OTP auth factor, he/she will enter their individual id (UIN/VID) and click on the "Generate OTP" button on the UI application. Then this endpoint will be invoked by wallet app with linked transactionId.

        Since the OTP generation and delivery to end user is to be handled by the integrated authentication system, the request will be relayed to the same.

        1. Validates the linked transactionId.
        2. Validates null / empty individualId.
        3. Delegates the call to integrated authentication system.
        4. Relays error from authentication system to UI on failure.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostSendLinkedOtpRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostSendLinkedOtpResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.ui import (
            PostSendLinkedOtpRequestRequest,
            PostSendLinkedOtpRequestRequestOtpChannelsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_send_linked_otp(
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:10+00:00",
                ),
                request=PostSendLinkedOtpRequestRequest(
                    transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                    individual_id="464737289558",
                    otp_channels=[
                        PostSendLinkedOtpRequestRequestOtpChannelsItem.PHONE,
                        PostSendLinkedOtpRequestRequestOtpChannelsItem.EMAIL,
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_send_linked_otp(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_authenticate(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostAuthenticateRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthenticateResponse:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the UI application, this endpoint will be invoked.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates transactionId/linkTransactionId.
        2. Validates null / empty individualId.
        3. Invokes kyc-auth call to integrated authentication server (IDA).
        4. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: Only transaction Id is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostAuthenticateRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthenticateResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.ui import PostAuthenticateRequestRequest

        from fern import (
            AsyncFernApi,
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_authenticate(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:10+00:00",
                ),
                request=PostAuthenticateRequestRequest(
                    transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                    individual_id="464737289558",
                    challenge_list=[
                        AuthChallenge(
                            auth_factor_type=AuthChallengeAuthFactorType.OTP,
                            challenge="111111",
                            format=AuthChallengeFormat.ALPHA_NUMERIC,
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_authenticate(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def post_authenticate_v2(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostAuthenticateV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthenticateV2Response:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the UI application, this endpoint will be invoked.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates transactionId/linkTransactionId.
        2. Validates null / empty individualId.
        3. Invokes kyc-auth call to integrated authentication server (IDA).
        4. It validates stored userconsent against the requested claims and scopes
        5. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: transaction Id and consentAction is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostAuthenticateV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthenticateV2Response
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.ui import PostAuthenticateV2RequestRequest

        from fern import (
            AsyncFernApi,
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_authenticate_v2(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:10+00:00",
                ),
                request=PostAuthenticateV2RequestRequest(
                    transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                    individual_id="464737289558",
                    challenge_list=[
                        AuthChallenge(
                            auth_factor_type=AuthChallengeAuthFactorType.OTP,
                            challenge="111111",
                            format=AuthChallengeFormat.ALPHA_NUMERIC,
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_authenticate_v2(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def post_authenticate_v3(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostAuthenticateV3RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthenticateV3Response:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the UI application, this endpoint will be invoked.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates transactionId/linkTransactionId.
        2. Validated the provided captcha token - if the provided auth-factor is configured to be with captcha.
        3. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. It validates stored userconsent against the requested claims and scopes
        6. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: transaction Id and consentAction is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostAuthenticateV3RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthenticateV3Response
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.ui import PostAuthenticateV3RequestRequest

        from fern import (
            AsyncFernApi,
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_authenticate_v3(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:10+00:00",
                ),
                request=PostAuthenticateV3RequestRequest(
                    transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                    individual_id="464737289558",
                    challenge_list=[
                        AuthChallenge(
                            auth_factor_type=AuthChallengeAuthFactorType.OTP,
                            challenge="111111",
                            format=AuthChallengeFormat.ALPHA_NUMERIC,
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_authenticate_v3(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def post_auth_code(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: dt.datetime,
        request: PostAuthCodeRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthCodeResponse:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the UI application to send the accepted consent and permitted scopes.

        Then UI application will receive the authorization code and few other details required for redirecting to the client / relying party application.

        1. Validates transactionId. If valid, stores the accepted claims and permitted scopes in the cache and returns back the authorization code.
        2. Validate accepted claims and permitted scopes in the request.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : dt.datetime

        request : PostAuthCodeRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthCodeResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.ui import PostAuthCodeRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_auth_code(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:10+00:00",
                ),
                request=PostAuthCodeRequestRequest(
                    transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                    permitted_authorize_scopes=["permittedAuthorizeScopes"],
                    accepted_claims=["name", "email", "phone_number"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_auth_code(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def get_authorization_generate_link_code(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: GetAuthorizationGenerateLinkCodeRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAuthorizationGenerateLinkCodeResponse:
        """
        Generate link code request is raised from JS application.

        1. JS application creates a deeplink with this link-code as parameter.
        2. This deeplink is embedded in a Machine-readable-code and the same is rendered in the UI.
        3. End user scans this machine-readable-code to open wallet app.
        4. On open of wallet-app, wallet-app invokes /link-transaction endpoint.
        5. In the JS application, once machine-readable-code is rendered, at the same time /link-status endpoint is invoked as a polling request.

        **Configuration to decide the expire date time of linkCode**: mosip.idp.link-code-expire-in-secs

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : GetAuthorizationGenerateLinkCodeRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAuthorizationGenerateLinkCodeResponse
            OK

        Examples
        --------
        import asyncio

        from fern.ui import GetAuthorizationGenerateLinkCodeRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.get_authorization_generate_link_code(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time="2023-09-22T08:01:10.000Z",
                request=GetAuthorizationGenerateLinkCodeRequestRequest(
                    transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authorization_generate_link_code(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def post_authorization_link_status(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: PostAuthorizationLinkStatusRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationLinkStatusResponse:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostAuthorizationLinkStatusRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationLinkStatusResponse
            OK

        Examples
        --------
        import asyncio

        from fern.ui import PostAuthorizationLinkStatusRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_authorization_link_status(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time="2023-09-22T08:01:10.000Z",
                request=PostAuthorizationLinkStatusRequestRequest(
                    transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                    link_code="xl4cnYtLQkGRxUj",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_authorization_link_status(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def post_authorization_link_auth(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: PostAuthorizationLinkAuthRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationLinkAuthResponse:
        """
        Link authorization code endpoint is invoked from JS application.

        1. This is a Long polling request to IdP-service.
        2. validates the transactionId
        3. validates the linkCode if its LINKED.
        4. checks the cache to see if the auth-code is generated, if yes returns the response.
        5. If the auth-code is not yet generated, polling request waits for the configured time.
        6. On successful response, IdP-UI should redirect to the provided redirectUri and auth-code or errors.


        **Configuration to decide the wait interval**: mosip.idp.link-auth-code-deferred-response-timeout-secs

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostAuthorizationLinkAuthRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationLinkAuthResponse
            OK

        Examples
        --------
        import asyncio

        from fern.ui import PostAuthorizationLinkAuthRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_authorization_link_auth(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time="2023-09-22T08:01:13.000Z",
                request=PostAuthorizationLinkAuthRequestRequest(
                    transaction_id="EKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                    linked_code="xl4cnYtLQkGRxUj",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_authorization_link_auth(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def get_consent_details(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConsentDetailsResponse:
        """
        **Prerequisites:**
        1. Request should have valid authenticated transaction id in the header `oauth-details-key`

        **Validations:**
        1. validate the transaction ID in the header.

        Once the end user is successfully authenticated, GET consent-details endpoint is invoked to get details about the claims and consent action.


        **Background:**
        During kyc-auth, integrated ID system should return the list of claim details for the authenticated end user.
        We have introduced new method in the `Authenticator` plugin. New kycAuth method will be invoked only when verified claims are requested by the relying party.
        Claims details returned during the kcy-auth is cached in the `OIDCTransaction` to give out during fetch claim details call.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConsentDetailsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.get_consent_details(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consent_details(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_options=request_options,
        )
        return _response.data

    async def post_authorization_prepare_signup_redirect(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: PostAuthorizationPrepareSignupRedirectRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationPrepareSignupRedirectResponse:
        """
        **Prerequisite**:
        1. User should be authenticated to invoke prepare-signup-redirect endpoint.
        2. signup-service should be registered as OAUTH client with esignet. And the signup-service's OAuth client id should be configured in this property `mosip.esignet.signup-id-token-audience` and the expire time of the generated ID token depends on below property `mosip.esignet.signup-id-token-expire-seconds`.


        **Validations:**
        1. Validates the input transactionID.
        2. Validates if the transaction requires profile update.


        When this endpoint is invoked, generates the ID-token for "singup-service". and sets the cookie header is also set with cookie name as UUID same as the subject of the ID token ( eg: "d898375b-c883-4408-a9e3-f629f15c1298") and the cookie value is a encoded json:
          `{"code" :"secret code to match with the server", "path-fragment": "path to resume after profile update"}`

        ID token payload is as below
         `{ "iss": "https://esignet.dev.mosip.net", "iat": 1715047546, "exp": 1746583546, "aud": "signup-service-client-id", "sub": "d898375b-c883-4408-a9e3-f629f15c1298" }`

         **Note**: Cookie created expire time should be equal to the expire time if generated ID token.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction ID

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str
            <yyyy-MM-dd'T'HH:mm:ss.SSS'Z'>

        request : PostAuthorizationPrepareSignupRedirectRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationPrepareSignupRedirectResponse
            OK

        Examples
        --------
        import asyncio

        from fern.ui import PostAuthorizationPrepareSignupRedirectRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_authorization_prepare_signup_redirect(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time="requestTime",
                request=PostAuthorizationPrepareSignupRedirectRequestRequest(
                    transaction_id="transactionId",
                    path_fragment="pathFragment",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_authorization_prepare_signup_redirect(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def post_complete_signup_redirect(
        self,
        *,
        oauth_details_hash: str,
        oauth_details_key: str,
        xsrf_token: str,
        request_time: str,
        request: PostCompleteSignupRedirectRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostCompleteSignupRedirectResponse:
        """
        This endpoint resumes the halted OIDC transactions halted and marks the completion of the identify verification process.

        Parameters
        ----------
        oauth_details_hash : str
            Base64 encoded SHA-256 hash of the oauth-details endpoint response.

        oauth_details_key : str
            Transaction Id

        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str
            <yyyy-MM-dd'T'HH:mm:ss.SSS'Z'>

        request : PostCompleteSignupRedirectRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostCompleteSignupRedirectResponse
            OK

        Examples
        --------
        import asyncio

        from fern.ui import PostCompleteSignupRedirectRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_complete_signup_redirect(
                oauth_details_hash="oauth-details-hash",
                oauth_details_key="oauth-details-key",
                xsrf_token="X-XSRF-TOKEN",
                request_time="2023-09-22T08:01:10.000Z",
                request=PostCompleteSignupRedirectRequestRequest(
                    transaction_id="vKb8cVbq9PX_yt46_hX0xlBJNExl9cnYtL8kGRxU5OM",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_complete_signup_redirect(
            oauth_details_hash=oauth_details_hash,
            oauth_details_key=oauth_details_key,
            xsrf_token=xsrf_token,
            request_time=request_time,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def post_par_oauth_details(
        self,
        *,
        xsrf_token: str,
        request_time: str,
        request: PostParOauthDetailsRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostParOauthDetailsResponse:
        """
        PAR OAuth details request is raised from the UI JS application on page load, only when request_uri is part of the authorize URL.
        OAuth details endpoint validates the provided request parameters.

        Resolved authentication factors and the consent details are sent back as response with a unique transactionId.

        The transcationId in the response is used to identify/maintain the end user pre-auth session.
        This pre-auth session has timeout (configurable).

        1. Validates the clientId.
        2. Validate the request_uri, if an entry is not found in the "par" cache, reject the request.
        3. Upon successful validation, move the object from "par" cache to "preauth" cache.
        4. Ignore unknown parameters in the request.
        5. In the existing oauth-details(v1,v2 & v3) endpoint, clients with **mandate_par_flow** set to true, but still using authorize without request_uri should be rejected.

        Parameters
        ----------
        xsrf_token : str
            CSRF token as set in cookie key 'XSRF-TOKEN'

        request_time : str

        request : PostParOauthDetailsRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostParOauthDetailsResponse
            OK

        Examples
        --------
        import asyncio

        from fern.ui import PostParOauthDetailsRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ui.post_par_oauth_details(
                xsrf_token="X-XSRF-TOKEN",
                request_time="2022-09-22T08:01:10.000Z",
                request=PostParOauthDetailsRequestRequest(
                    request_uri="urn:ietf:params:oauth:request_uri:XiaVWGcLVPNxTNSAddv",
                    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_par_oauth_details(
            xsrf_token=xsrf_token, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data
