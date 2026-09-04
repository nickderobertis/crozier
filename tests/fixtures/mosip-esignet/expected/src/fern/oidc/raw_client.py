

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.claim import Claim
from ..types.method_not_allowed_error_body import MethodNotAllowedErrorBody
from .types.get_authorize_request_acr_values import GetAuthorizeRequestAcrValues
from .types.get_authorize_request_display import GetAuthorizeRequestDisplay
from .types.get_authorize_request_prompt import GetAuthorizeRequestPrompt
from .types.get_authorize_request_response_type import GetAuthorizeRequestResponseType
from .types.get_authorize_request_scope import GetAuthorizeRequestScope
from .types.get_certs_response import GetCertsResponse
from .types.get_introspect_request_token_type_hint import GetIntrospectRequestTokenTypeHint
from .types.get_introspect_response import GetIntrospectResponse
from .types.get_well_known_openid_configuration_response import GetWellKnownOpenidConfigurationResponse
from .types.post_oauth_par_request_client_assertion_type import PostOauthParRequestClientAssertionType
from .types.post_oauth_par_request_code_challenge_method import PostOauthParRequestCodeChallengeMethod
from .types.post_oauth_par_request_response_type import PostOauthParRequestResponseType
from .types.post_oauth_par_request_scope import PostOauthParRequestScope
from .types.post_oauth_par_response import PostOauthParResponse
from .types.post_token_request_client_assertion_type import PostTokenRequestClientAssertionType
from .types.post_token_request_grant_type import PostTokenRequestGrantType
from .types.post_token_response import PostTokenResponse
from .types.post_token_v2request_client_assertion_type import PostTokenV2RequestClientAssertionType
from .types.post_token_v2request_grant_type import PostTokenV2RequestGrantType
from .types.post_token_v2response import PostTokenV2Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOidcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_authorize(
        self,
        *,
        scope: GetAuthorizeRequestScope,
        response_type: GetAuthorizeRequestResponseType,
        client_id: str,
        redirect_uri: str,
        state: typing.Optional[str] = None,
        nonce: typing.Optional[str] = None,
        display: typing.Optional[GetAuthorizeRequestDisplay] = None,
        prompt: typing.Optional[GetAuthorizeRequestPrompt] = None,
        max_age: typing.Optional[float] = None,
        ui_locales: typing.Optional[str] = None,
        acr_values: typing.Optional[GetAuthorizeRequestAcrValues] = None,
        claims_locales: typing.Optional[str] = None,
        claims: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[str] = None,
        id_token_hint: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        This is the authorize endpoint of Open ID Connect (OIDC). The relying party applications will do a browser redirect to this endpoint with all required details passed as query parameters.

        This endpoint will respond with a basic HTML page to load a JS application in the browser. UI JS application will then echo all the query parameters received in this endpoint to the "/authorization/oauth-details" endpoint as the request body.

        All the validations on the query parameter values will be performed in the "/authorization/oauth-details" endpoint.

        **Authentication & Authroization**: None

        Parameters
        ----------
        scope : GetAuthorizeRequestScope
            Specifies what access privileges are being requested for Access Tokens. The scopes associated with Access Tokens determine what resources will be available when they are used to access OAuth 2.0 protected endpoints. OpenID Connect requests MUST contain the OpenID scope value.

        response_type : GetAuthorizeRequestResponseType
            The value set here determines the authorization processing flow. To use the Authorization Code Flow, the value should be configured to "code".

        client_id : str
            Valid OAuth 2.0 Client Identifier in the Authorization Server.

        redirect_uri : str
            Redirection URI to which the response would be sent. This URI must match one of the redirection URI values during the client ID creation.

        state : typing.Optional[str]
            Opaque value used to maintain state between the request and the callback. Typically, Cross-Site Request Forgery (CSRF, XSRF) mitigation is done by cryptographically binding the value of this parameter with a browser cookie.

        nonce : typing.Optional[str]
            String value used to associate a Client session with an ID Token, and to mitigate replay attacks. The value is passed through unmodified from the Authentication Request to the ID Token.

        display : typing.Optional[GetAuthorizeRequestDisplay]
            ASCII string value that specifies how the Authorization Server displays the authentication and consent user interface pages to the end user.

        prompt : typing.Optional[GetAuthorizeRequestPrompt]
            Space delimited case-sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for re-authentication and consent.

        max_age : typing.Optional[float]
            Maximum Authentication Age. This specifies the allowable elapsed time in seconds since the last time the end user was actively authenticated by the OP. If the elapsed time is greater than this value, then the OP MUST attempt to actively re-authenticate the end user. The max_age request parameter corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] max_auth_age request parameter. When max_age is used, the ID Token returned MUST include an auth_time claim value.

        ui_locales : typing.Optional[str]
            End user's preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.

        acr_values : typing.Optional[GetAuthorizeRequestAcrValues]
            Requested Authentication Context Class Reference values. Space-separated string that specifies the acr values that the Authorization Server is being requested to use for processing this Authentication Request, with the values appearing in order of preference. The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value, as specified in Section 2. The acr Claim is requested as a Voluntary Claim by this parameter.

        claims_locales : typing.Optional[str]
            End-User's preferred languages and scripts for Claims being returned, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.

        claims : typing.Optional[str]
            This parameter is used to request specific claims to be returned. The value is a JSON object listing the requested claims. The claims parameter value is represented in an OAuth 2.0 request as UTF-8 encoded JSON.

        code_challenge : typing.Optional[str]
            A challenge derived from the code_verifier, This is required if its a VC scoped request.

        code_challenge_method : typing.Optional[str]
            A method that was used to derive code challenge, This will be required if code_challenge is provided.

        id_token_hint : typing.Optional[str]
            ID Token previously issued by the Authorization Server being passed as a hint about the End-User's current or past authenticated session with the Client.

        request_uri : typing.Optional[str]
            The request URI corresponding to the pushed authorization request posted. This URI is a single-use reference to the respective request data in the subsequent authorization request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "authorize",
            method="GET",
            params={
                "scope": scope,
                "response_type": response_type,
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "state": state,
                "nonce": nonce,
                "display": display,
                "prompt": prompt,
                "max_age": max_age,
                "ui_locales": ui_locales,
                "acr_values": acr_values,
                "claims_locales": claims_locales,
                "claims": claims,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "id_token_hint": id_token_hint,
                "request_uri": request_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_token(
        self,
        *,
        grant_type: PostTokenRequestGrantType,
        code: str,
        client_assertion_type: PostTokenRequestClientAssertionType,
        client_assertion: str,
        redirect_uri: str,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostTokenResponse]:
        """
        Once the client / relying party application receives the authorization code through redirect, this OIDC complaint endpoint will be called from the relying party backend application to get the ID and access token.

        1. The only supported client authentication methods : <b>private_key_jwt</b>
        2. clientAssertion is a signed JWT with Clients private key, corresponding public key should be shared with IdP during the OIDC client registration process.
        3. clientAssertion JWT payload must be as below:

        The JWT MUST contain the following REQUIRED Claim Values and MAY contain the additional OPTIONAL Claim Values:

        **iss**<span style="color:#FF0000">*</span> (Issuer): This MUST contain the client_id of the OAuth Client.

        **sub**<span style="color:#FF0000">*</span> (Subject): This MUST contain the client_id of the OAuth Client.

        **aud**<span style="color:#FF0000">*</span> (Audience): Value that identifies the authorization server as an intended audience. The authorization server MUST verify that it is an intended audience for the token. The audience SHOULD be the URL of the authorization server's token endpoint.

        **exp**<span style="color:#FF0000">*</span> (Expiration): Time on or after which the ID token MUST NOT be accepted for processing.

        **iat**<span style="color:#FF0000">*</span>: Time at which the JWT was issued.</p>

        **jti**<span style="color:#FF0000">*</span> (JWT ID): This MUST be unique random string for each client assertion generated.

        **Note**: The Client Assertion JWT can contain other Claims. Any Claims used that are not understood WILL be ignored.</p>

        Parameters
        ----------
        grant_type : PostTokenRequestGrantType
            Authorization code grant type.

        code : str
            Authorization code, sent as query param in the client's redirect URI.

        client_assertion_type : PostTokenRequestClientAssertionType
            Type of the client assertion part of this request.

        client_assertion : str
            Private key signed JWT, This JWT payload structure is defined above as part of request description.

        redirect_uri : str
            Valid client redirect_uri. Must be same as the one sent in the authorize call.

        client_id : typing.Optional[str]
            Client Id of the OIDC client.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostTokenResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "code": code,
                "client_id": client_id,
                "client_assertion_type": client_assertion_type,
                "client_assertion": client_assertion,
                "redirect_uri": redirect_uri,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostTokenResponse,
                    parse_obj_as(
                        type_=PostTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_token_v2(
        self,
        *,
        grant_type: PostTokenV2RequestGrantType,
        code: str,
        client_assertion_type: PostTokenV2RequestClientAssertionType,
        client_assertion: str,
        redirect_uri: str,
        d_po_p: typing.Optional[str] = None,
        client_id: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostTokenV2Response]:
        """
        Once the client / relying party application receives the authorization code through redirect, this OIDC complaint endpoint will be called from the relying party backend application to get the ID and access token.

        1. The only supported client authentication methods : <b>private_key_jwt</b>
        2. clientAssertion is a signed JWT with Clients private key, corresponding public key should be shared with IdP during the OIDC client registration process.
        3. clientAssertion JWT payload must be as below:

        The JWT MUST contain the following REQUIRED Claim Values and MAY contain the additional OPTIONAL Claim Values:

        **iss**<span style="color:#FF0000">*</span> (Issuer): This MUST contain the client_id of the OAuth Client.

        **sub**<span style="color:#FF0000">*</span> (Subject): This MUST contain the client_id of the OAuth Client.

        **aud**<span style="color:#FF0000">*</span> (Audience): Value that identifies the authorization server as an intended audience. The authorization server MUST verify that it is an intended audience for the token. The audience SHOULD be the URL of the authorization server's token endpoint.

        **exp**<span style="color:#FF0000">*</span> (Expiration): Time on or after which the ID token MUST NOT be accepted for processing.

        **iat**<span style="color:#FF0000">*</span>: Time at which the JWT was issued.</p>

        **jti**<span style="color:#FF0000">*</span> (JWT ID): This MUST be unique for each client assertion generated.

        **Note**: The Client Assertion JWT can contain other Claims. Any Claims used that are not understood WILL be ignored.</p>

        Parameters
        ----------
        grant_type : PostTokenV2RequestGrantType
            Authorization code grant type.

        code : str
            Authorization code, sent as query param in the client's redirect URI.

        client_assertion_type : PostTokenV2RequestClientAssertionType
            Type of the client assertion part of this request.

        client_assertion : str
            Private key signed JWT, This JWT payload structure is defined above as part of request description.

        redirect_uri : str
            Valid client redirect_uri. Must be same as the one sent in the authorize call.

        d_po_p : typing.Optional[str]
            A DPoP proof is a JWT [RFC7519] that is signed (using JSON Web Signature (JWS) [RFC7515]) with a private key chosen by the client.          For more details refer - https://datatracker.ietf.org/doc/html/rfc9449#section-4.2

        client_id : typing.Optional[str]
            Client Id of the OIDC client.

        code_verifier : typing.Optional[str]
            A cryptographically random string that is used to correlate the
                  authorization request to the token request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostTokenV2Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/v2/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "code": code,
                "client_id": client_id,
                "client_assertion_type": client_assertion_type,
                "client_assertion": client_assertion,
                "redirect_uri": redirect_uri,
                "code_verifier": code_verifier,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
                "DPoP": str(d_po_p) if d_po_p is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostTokenV2Response,
                    parse_obj_as(
                        type_=PostTokenV2Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_userinfo(
        self, *, d_po_p: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Once the access token is received via the token endpoint, relying party backend application can call this OIDC compliant endpoint to request for the user claims.

        Consented user claims will be returned as a JWT. This JWT will be a nested JWT which is a signed using JWS and then encrypted using JWE.


        **Example**: Assuming the below are the requested claims by the relying party

        name : { "essential" : true }

        phone: { "essential" : true }

        **Response 1**: When consent is provided for both name and phone number:

        { "name" : "John Doe", "phone" : "033456743" }

        **Response 2**: When consent is provided for only name:

        { "name" : "John Doe" }

        **Response 3**: When Claims are requested with claims_locales : "en fr"

        { "name#en" : "John Doe", "name#fr" : "Jean Doe", "phone" : "033456743" }

        **Supported User Info Claims**
        <ul>
        <li>sub - Partner Specific User Token (PSUT)</li>
        <li>name</li>
        <li>address</li>
        <li>gender</li>
        <li>birthdate</li>
        <li>profile photo</li>
        <li>email</li>
        <li>phone</li>
        <li>locale</li>
        <li>Custom - individual_id (You share this claim as a system-level config and it can be UIN, perceptual VID or temporary VID)</li>
        </ul>

        Parameters
        ----------
        d_po_p : typing.Optional[str]
            A DPoP proof is a JWT [RFC7519] that is signed (using JSON Web Signature (JWS) [RFC7515]) with a private key chosen by the client.          For more details refer - https://datatracker.ietf.org/doc/html/rfc9449#section-4.2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "oidc/userinfo",
            method="GET",
            headers={
                "DPoP": str(d_po_p) if d_po_p is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_certs(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[GetCertsResponse]:
        """
        Endpoint to fetch all the public keys of the eSignet server. Returns public key set in the JWKS format.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCertsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            ".well-known/jwks.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCertsResponse,
                    parse_obj_as(
                        type_=GetCertsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_well_known_openid_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetWellKnownOpenidConfigurationResponse]:
        """
        Open ID Connect dynamic provider discovery is not supported currently, this endpoint is only for facilitating the OIDC provider details in a standard way.

        **Reference**: https://openid.net/specs/openid-connect-discovery-1_0.html

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetWellKnownOpenidConfigurationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            ".well-known/openid-configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWellKnownOpenidConfigurationResponse,
                    parse_obj_as(
                        type_=GetWellKnownOpenidConfigurationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_introspect(
        self,
        *,
        token: str,
        token_type_hint: GetIntrospectRequestTokenTypeHint,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetIntrospectResponse]:
        """
        This endpoint takes an access token or ID token and returns a boolean that indicates whether it is active. If the token is active, additional data about the token is also returned. If the token is invalid, expired, or revoked, it is considered inactive.

        **Reference**: https://www.rfc-editor.org/rfc/rfc7662.html

        Parameters
        ----------
        token : str
            An access token or ID token

        token_type_hint : GetIntrospectRequestTokenTypeHint
            Indicates the type of token being passed. Valid values: access_token, id_token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetIntrospectResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/introspect",
            method="GET",
            params={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetIntrospectResponse,
                    parse_obj_as(
                        type_=GetIntrospectResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_oauth_par(
        self,
        *,
        scope: PostOauthParRequestScope,
        response_type: PostOauthParRequestResponseType,
        client_id: str,
        redirect_uri: str,
        client_assertion_type: PostOauthParRequestClientAssertionType,
        client_assertion: str,
        d_po_p: typing.Optional[str] = None,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        acr_values: typing.Optional[str] = OMIT,
        claims: typing.Optional[Claim] = OMIT,
        max_age: typing.Optional[float] = OMIT,
        claims_locales: typing.Optional[str] = OMIT,
        ui_locales: typing.Optional[str] = OMIT,
        code_challenge: typing.Optional[str] = OMIT,
        code_challenge_method: typing.Optional[PostOauthParRequestCodeChallengeMethod] = OMIT,
        id_token_hint: typing.Optional[str] = OMIT,
        dpop_jkt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostOauthParResponse]:
        """
        **PAR - Pushed Authorization Request**

        1. Message body of an this request with parameters formatted with x-www-form-urlencoded using a character encoding of UTF-8
        2. Add "pushed_authorization_request_endpoint" in the authorization server metadata.
        3. Client must adds its authentication credentials to the request body using the same rules as for token endpoint request.
        4. Authenticate the client in the same way as at the token endpoint.
        5. Reject the request if the request_uri authorization request parameter is provided.
        6. Validate the request parmeters in the body as it would be validated in oauth-details request.
        7. Upon successful verification, the server MUST generate a request URI and provide it in the response with a 201 HTTP status code.

        **request_uri** should be in this format: 'urn:ietf:params:oauth:request_uri:<secure random alpha-numeric string with max length of 25>'

        Successfully verified request parameters should be stored in the "par" cache with request_uri as the key. Objects in the "par" cache are set with TTL.
        TTL should be configurable and the expires_in parameter in the response should return same value.

        **Not supported:**
          1. client authentication parameters in the PAR request header.
          2. The request parameter as defined in JAR [RFC9101].
          3. API rate limit is left to the infra to handle.
          4. Use of non-registered redirect_uri's are not allowed.

        Parameters
        ----------
        scope : PostOauthParRequestScope
            Specifies what access privileges are being requested for Access Tokens. The scopes associated with Access Tokens determine what resources will be available when they are used to access OAuth 2.0 protected endpoints. OpenID Connect requests MUST contain the OpenID scope value.

        response_type : PostOauthParRequestResponseType
            Value that determines the authorization processing flow to be used. When using the Authorization Code Flow, this value is code.

        client_id : str
            OAuth 2.0 Client Identifier valid at the Authorization Server

        redirect_uri : str
            Redirection URI to which the response will be sent. This URI MUST exactly match one of the Redirection URI values for the Client pre-registered

        client_assertion_type : PostOauthParRequestClientAssertionType
            Type of the client assertion part of this request.

        client_assertion : str
            The value of the "client_assertion" parameter contains a single JWT.

        d_po_p : typing.Optional[str]
            A DPoP proof is a JWT [RFC7519] that is signed (using JSON Web Signature (JWS) [RFC7515]) with a private key chosen by the client.          For more details refer - https://datatracker.ietf.org/doc/html/rfc9449#section-4.2

        state : typing.Optional[str]
            client state value echoed.

        nonce : typing.Optional[str]
            Client's nonce value echoed.

        display : typing.Optional[str]
            ASCII string value that specifies how the Authorization Server displays the authentication and consent user interface pages to the End-User.

        prompt : typing.Optional[str]
            Space delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for re-authentication and consent.

        acr_values : typing.Optional[str]
            Space separated ACR values, Unknown ACR are ignored. Only registered ACR values will be considered.
            If none of the provided acr value is among the registered values, all the registered ACR's will be considered.

        claims : typing.Optional[Claim]

        max_age : typing.Optional[float]
            Maximum Authentication Age. Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated by the OP. If the elapsed time is greater than this value, the OP MUST attempt to actively re-authenticate the End-User. (The max_age request parameter corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] max_auth_age request parameter.) When max_age is used, the ID Token returned MUST include an auth_time Claim Value.

        claims_locales : typing.Optional[str]
            End-User's preferred languages and scripts for Claims being returned, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.

        ui_locales : typing.Optional[str]
            End-User's preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.

        code_challenge : typing.Optional[str]
            A challenge derived from the code verifier, to be verified against later.

        code_challenge_method : typing.Optional[PostOauthParRequestCodeChallengeMethod]
            A method that was used to derive code challenge.

        id_token_hint : typing.Optional[str]
            ID Token previously issued by the Authorization Server being passed as a hint about the End-User's current or past authenticated session with the Client.

        dpop_jkt : typing.Optional[str]
            The value of the dpop_jkt authorization request parameter is the JWK Thumbprint [RFC7638] of the proof-of-possession public key using the SHA-256 hash function.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostOauthParResponse]
            CREATED
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/par",
            method="POST",
            data={
                "scope": scope,
                "response_type": response_type,
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "state": state,
                "nonce": nonce,
                "display": display,
                "prompt": prompt,
                "acr_values": acr_values,
                "claims": convert_and_respect_annotation_metadata(object_=claims, annotation=Claim, direction="write"),
                "max_age": max_age,
                "claims_locales": claims_locales,
                "ui_locales": ui_locales,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "id_token_hint": id_token_hint,
                "client_assertion_type": client_assertion_type,
                "client_assertion": client_assertion,
                "dpop_jkt": dpop_jkt,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
                "DPoP": str(d_po_p) if d_po_p is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostOauthParResponse,
                    parse_obj_as(
                        type_=PostOauthParResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        MethodNotAllowedErrorBody,
                        parse_obj_as(
                            type_=MethodNotAllowedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawOidcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_authorize(
        self,
        *,
        scope: GetAuthorizeRequestScope,
        response_type: GetAuthorizeRequestResponseType,
        client_id: str,
        redirect_uri: str,
        state: typing.Optional[str] = None,
        nonce: typing.Optional[str] = None,
        display: typing.Optional[GetAuthorizeRequestDisplay] = None,
        prompt: typing.Optional[GetAuthorizeRequestPrompt] = None,
        max_age: typing.Optional[float] = None,
        ui_locales: typing.Optional[str] = None,
        acr_values: typing.Optional[GetAuthorizeRequestAcrValues] = None,
        claims_locales: typing.Optional[str] = None,
        claims: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[str] = None,
        id_token_hint: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        This is the authorize endpoint of Open ID Connect (OIDC). The relying party applications will do a browser redirect to this endpoint with all required details passed as query parameters.

        This endpoint will respond with a basic HTML page to load a JS application in the browser. UI JS application will then echo all the query parameters received in this endpoint to the "/authorization/oauth-details" endpoint as the request body.

        All the validations on the query parameter values will be performed in the "/authorization/oauth-details" endpoint.

        **Authentication & Authroization**: None

        Parameters
        ----------
        scope : GetAuthorizeRequestScope
            Specifies what access privileges are being requested for Access Tokens. The scopes associated with Access Tokens determine what resources will be available when they are used to access OAuth 2.0 protected endpoints. OpenID Connect requests MUST contain the OpenID scope value.

        response_type : GetAuthorizeRequestResponseType
            The value set here determines the authorization processing flow. To use the Authorization Code Flow, the value should be configured to "code".

        client_id : str
            Valid OAuth 2.0 Client Identifier in the Authorization Server.

        redirect_uri : str
            Redirection URI to which the response would be sent. This URI must match one of the redirection URI values during the client ID creation.

        state : typing.Optional[str]
            Opaque value used to maintain state between the request and the callback. Typically, Cross-Site Request Forgery (CSRF, XSRF) mitigation is done by cryptographically binding the value of this parameter with a browser cookie.

        nonce : typing.Optional[str]
            String value used to associate a Client session with an ID Token, and to mitigate replay attacks. The value is passed through unmodified from the Authentication Request to the ID Token.

        display : typing.Optional[GetAuthorizeRequestDisplay]
            ASCII string value that specifies how the Authorization Server displays the authentication and consent user interface pages to the end user.

        prompt : typing.Optional[GetAuthorizeRequestPrompt]
            Space delimited case-sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for re-authentication and consent.

        max_age : typing.Optional[float]
            Maximum Authentication Age. This specifies the allowable elapsed time in seconds since the last time the end user was actively authenticated by the OP. If the elapsed time is greater than this value, then the OP MUST attempt to actively re-authenticate the end user. The max_age request parameter corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] max_auth_age request parameter. When max_age is used, the ID Token returned MUST include an auth_time claim value.

        ui_locales : typing.Optional[str]
            End user's preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.

        acr_values : typing.Optional[GetAuthorizeRequestAcrValues]
            Requested Authentication Context Class Reference values. Space-separated string that specifies the acr values that the Authorization Server is being requested to use for processing this Authentication Request, with the values appearing in order of preference. The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value, as specified in Section 2. The acr Claim is requested as a Voluntary Claim by this parameter.

        claims_locales : typing.Optional[str]
            End-User's preferred languages and scripts for Claims being returned, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.

        claims : typing.Optional[str]
            This parameter is used to request specific claims to be returned. The value is a JSON object listing the requested claims. The claims parameter value is represented in an OAuth 2.0 request as UTF-8 encoded JSON.

        code_challenge : typing.Optional[str]
            A challenge derived from the code_verifier, This is required if its a VC scoped request.

        code_challenge_method : typing.Optional[str]
            A method that was used to derive code challenge, This will be required if code_challenge is provided.

        id_token_hint : typing.Optional[str]
            ID Token previously issued by the Authorization Server being passed as a hint about the End-User's current or past authenticated session with the Client.

        request_uri : typing.Optional[str]
            The request URI corresponding to the pushed authorization request posted. This URI is a single-use reference to the respective request data in the subsequent authorization request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "authorize",
            method="GET",
            params={
                "scope": scope,
                "response_type": response_type,
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "state": state,
                "nonce": nonce,
                "display": display,
                "prompt": prompt,
                "max_age": max_age,
                "ui_locales": ui_locales,
                "acr_values": acr_values,
                "claims_locales": claims_locales,
                "claims": claims,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "id_token_hint": id_token_hint,
                "request_uri": request_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_token(
        self,
        *,
        grant_type: PostTokenRequestGrantType,
        code: str,
        client_assertion_type: PostTokenRequestClientAssertionType,
        client_assertion: str,
        redirect_uri: str,
        client_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostTokenResponse]:
        """
        Once the client / relying party application receives the authorization code through redirect, this OIDC complaint endpoint will be called from the relying party backend application to get the ID and access token.

        1. The only supported client authentication methods : <b>private_key_jwt</b>
        2. clientAssertion is a signed JWT with Clients private key, corresponding public key should be shared with IdP during the OIDC client registration process.
        3. clientAssertion JWT payload must be as below:

        The JWT MUST contain the following REQUIRED Claim Values and MAY contain the additional OPTIONAL Claim Values:

        **iss**<span style="color:#FF0000">*</span> (Issuer): This MUST contain the client_id of the OAuth Client.

        **sub**<span style="color:#FF0000">*</span> (Subject): This MUST contain the client_id of the OAuth Client.

        **aud**<span style="color:#FF0000">*</span> (Audience): Value that identifies the authorization server as an intended audience. The authorization server MUST verify that it is an intended audience for the token. The audience SHOULD be the URL of the authorization server's token endpoint.

        **exp**<span style="color:#FF0000">*</span> (Expiration): Time on or after which the ID token MUST NOT be accepted for processing.

        **iat**<span style="color:#FF0000">*</span>: Time at which the JWT was issued.</p>

        **jti**<span style="color:#FF0000">*</span> (JWT ID): This MUST be unique random string for each client assertion generated.

        **Note**: The Client Assertion JWT can contain other Claims. Any Claims used that are not understood WILL be ignored.</p>

        Parameters
        ----------
        grant_type : PostTokenRequestGrantType
            Authorization code grant type.

        code : str
            Authorization code, sent as query param in the client's redirect URI.

        client_assertion_type : PostTokenRequestClientAssertionType
            Type of the client assertion part of this request.

        client_assertion : str
            Private key signed JWT, This JWT payload structure is defined above as part of request description.

        redirect_uri : str
            Valid client redirect_uri. Must be same as the one sent in the authorize call.

        client_id : typing.Optional[str]
            Client Id of the OIDC client.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostTokenResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "code": code,
                "client_id": client_id,
                "client_assertion_type": client_assertion_type,
                "client_assertion": client_assertion,
                "redirect_uri": redirect_uri,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostTokenResponse,
                    parse_obj_as(
                        type_=PostTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_token_v2(
        self,
        *,
        grant_type: PostTokenV2RequestGrantType,
        code: str,
        client_assertion_type: PostTokenV2RequestClientAssertionType,
        client_assertion: str,
        redirect_uri: str,
        d_po_p: typing.Optional[str] = None,
        client_id: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostTokenV2Response]:
        """
        Once the client / relying party application receives the authorization code through redirect, this OIDC complaint endpoint will be called from the relying party backend application to get the ID and access token.

        1. The only supported client authentication methods : <b>private_key_jwt</b>
        2. clientAssertion is a signed JWT with Clients private key, corresponding public key should be shared with IdP during the OIDC client registration process.
        3. clientAssertion JWT payload must be as below:

        The JWT MUST contain the following REQUIRED Claim Values and MAY contain the additional OPTIONAL Claim Values:

        **iss**<span style="color:#FF0000">*</span> (Issuer): This MUST contain the client_id of the OAuth Client.

        **sub**<span style="color:#FF0000">*</span> (Subject): This MUST contain the client_id of the OAuth Client.

        **aud**<span style="color:#FF0000">*</span> (Audience): Value that identifies the authorization server as an intended audience. The authorization server MUST verify that it is an intended audience for the token. The audience SHOULD be the URL of the authorization server's token endpoint.

        **exp**<span style="color:#FF0000">*</span> (Expiration): Time on or after which the ID token MUST NOT be accepted for processing.

        **iat**<span style="color:#FF0000">*</span>: Time at which the JWT was issued.</p>

        **jti**<span style="color:#FF0000">*</span> (JWT ID): This MUST be unique for each client assertion generated.

        **Note**: The Client Assertion JWT can contain other Claims. Any Claims used that are not understood WILL be ignored.</p>

        Parameters
        ----------
        grant_type : PostTokenV2RequestGrantType
            Authorization code grant type.

        code : str
            Authorization code, sent as query param in the client's redirect URI.

        client_assertion_type : PostTokenV2RequestClientAssertionType
            Type of the client assertion part of this request.

        client_assertion : str
            Private key signed JWT, This JWT payload structure is defined above as part of request description.

        redirect_uri : str
            Valid client redirect_uri. Must be same as the one sent in the authorize call.

        d_po_p : typing.Optional[str]
            A DPoP proof is a JWT [RFC7519] that is signed (using JSON Web Signature (JWS) [RFC7515]) with a private key chosen by the client.          For more details refer - https://datatracker.ietf.org/doc/html/rfc9449#section-4.2

        client_id : typing.Optional[str]
            Client Id of the OIDC client.

        code_verifier : typing.Optional[str]
            A cryptographically random string that is used to correlate the
                  authorization request to the token request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostTokenV2Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/v2/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "code": code,
                "client_id": client_id,
                "client_assertion_type": client_assertion_type,
                "client_assertion": client_assertion,
                "redirect_uri": redirect_uri,
                "code_verifier": code_verifier,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
                "DPoP": str(d_po_p) if d_po_p is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostTokenV2Response,
                    parse_obj_as(
                        type_=PostTokenV2Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_userinfo(
        self, *, d_po_p: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Once the access token is received via the token endpoint, relying party backend application can call this OIDC compliant endpoint to request for the user claims.

        Consented user claims will be returned as a JWT. This JWT will be a nested JWT which is a signed using JWS and then encrypted using JWE.


        **Example**: Assuming the below are the requested claims by the relying party

        name : { "essential" : true }

        phone: { "essential" : true }

        **Response 1**: When consent is provided for both name and phone number:

        { "name" : "John Doe", "phone" : "033456743" }

        **Response 2**: When consent is provided for only name:

        { "name" : "John Doe" }

        **Response 3**: When Claims are requested with claims_locales : "en fr"

        { "name#en" : "John Doe", "name#fr" : "Jean Doe", "phone" : "033456743" }

        **Supported User Info Claims**
        <ul>
        <li>sub - Partner Specific User Token (PSUT)</li>
        <li>name</li>
        <li>address</li>
        <li>gender</li>
        <li>birthdate</li>
        <li>profile photo</li>
        <li>email</li>
        <li>phone</li>
        <li>locale</li>
        <li>Custom - individual_id (You share this claim as a system-level config and it can be UIN, perceptual VID or temporary VID)</li>
        </ul>

        Parameters
        ----------
        d_po_p : typing.Optional[str]
            A DPoP proof is a JWT [RFC7519] that is signed (using JSON Web Signature (JWS) [RFC7515]) with a private key chosen by the client.          For more details refer - https://datatracker.ietf.org/doc/html/rfc9449#section-4.2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oidc/userinfo",
            method="GET",
            headers={
                "DPoP": str(d_po_p) if d_po_p is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_certs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCertsResponse]:
        """
        Endpoint to fetch all the public keys of the eSignet server. Returns public key set in the JWKS format.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCertsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            ".well-known/jwks.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCertsResponse,
                    parse_obj_as(
                        type_=GetCertsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_well_known_openid_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetWellKnownOpenidConfigurationResponse]:
        """
        Open ID Connect dynamic provider discovery is not supported currently, this endpoint is only for facilitating the OIDC provider details in a standard way.

        **Reference**: https://openid.net/specs/openid-connect-discovery-1_0.html

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetWellKnownOpenidConfigurationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            ".well-known/openid-configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWellKnownOpenidConfigurationResponse,
                    parse_obj_as(
                        type_=GetWellKnownOpenidConfigurationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_introspect(
        self,
        *,
        token: str,
        token_type_hint: GetIntrospectRequestTokenTypeHint,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetIntrospectResponse]:
        """
        This endpoint takes an access token or ID token and returns a boolean that indicates whether it is active. If the token is active, additional data about the token is also returned. If the token is invalid, expired, or revoked, it is considered inactive.

        **Reference**: https://www.rfc-editor.org/rfc/rfc7662.html

        Parameters
        ----------
        token : str
            An access token or ID token

        token_type_hint : GetIntrospectRequestTokenTypeHint
            Indicates the type of token being passed. Valid values: access_token, id_token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetIntrospectResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/introspect",
            method="GET",
            params={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetIntrospectResponse,
                    parse_obj_as(
                        type_=GetIntrospectResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_oauth_par(
        self,
        *,
        scope: PostOauthParRequestScope,
        response_type: PostOauthParRequestResponseType,
        client_id: str,
        redirect_uri: str,
        client_assertion_type: PostOauthParRequestClientAssertionType,
        client_assertion: str,
        d_po_p: typing.Optional[str] = None,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        acr_values: typing.Optional[str] = OMIT,
        claims: typing.Optional[Claim] = OMIT,
        max_age: typing.Optional[float] = OMIT,
        claims_locales: typing.Optional[str] = OMIT,
        ui_locales: typing.Optional[str] = OMIT,
        code_challenge: typing.Optional[str] = OMIT,
        code_challenge_method: typing.Optional[PostOauthParRequestCodeChallengeMethod] = OMIT,
        id_token_hint: typing.Optional[str] = OMIT,
        dpop_jkt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostOauthParResponse]:
        """
        **PAR - Pushed Authorization Request**

        1. Message body of an this request with parameters formatted with x-www-form-urlencoded using a character encoding of UTF-8
        2. Add "pushed_authorization_request_endpoint" in the authorization server metadata.
        3. Client must adds its authentication credentials to the request body using the same rules as for token endpoint request.
        4. Authenticate the client in the same way as at the token endpoint.
        5. Reject the request if the request_uri authorization request parameter is provided.
        6. Validate the request parmeters in the body as it would be validated in oauth-details request.
        7. Upon successful verification, the server MUST generate a request URI and provide it in the response with a 201 HTTP status code.

        **request_uri** should be in this format: 'urn:ietf:params:oauth:request_uri:<secure random alpha-numeric string with max length of 25>'

        Successfully verified request parameters should be stored in the "par" cache with request_uri as the key. Objects in the "par" cache are set with TTL.
        TTL should be configurable and the expires_in parameter in the response should return same value.

        **Not supported:**
          1. client authentication parameters in the PAR request header.
          2. The request parameter as defined in JAR [RFC9101].
          3. API rate limit is left to the infra to handle.
          4. Use of non-registered redirect_uri's are not allowed.

        Parameters
        ----------
        scope : PostOauthParRequestScope
            Specifies what access privileges are being requested for Access Tokens. The scopes associated with Access Tokens determine what resources will be available when they are used to access OAuth 2.0 protected endpoints. OpenID Connect requests MUST contain the OpenID scope value.

        response_type : PostOauthParRequestResponseType
            Value that determines the authorization processing flow to be used. When using the Authorization Code Flow, this value is code.

        client_id : str
            OAuth 2.0 Client Identifier valid at the Authorization Server

        redirect_uri : str
            Redirection URI to which the response will be sent. This URI MUST exactly match one of the Redirection URI values for the Client pre-registered

        client_assertion_type : PostOauthParRequestClientAssertionType
            Type of the client assertion part of this request.

        client_assertion : str
            The value of the "client_assertion" parameter contains a single JWT.

        d_po_p : typing.Optional[str]
            A DPoP proof is a JWT [RFC7519] that is signed (using JSON Web Signature (JWS) [RFC7515]) with a private key chosen by the client.          For more details refer - https://datatracker.ietf.org/doc/html/rfc9449#section-4.2

        state : typing.Optional[str]
            client state value echoed.

        nonce : typing.Optional[str]
            Client's nonce value echoed.

        display : typing.Optional[str]
            ASCII string value that specifies how the Authorization Server displays the authentication and consent user interface pages to the End-User.

        prompt : typing.Optional[str]
            Space delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for re-authentication and consent.

        acr_values : typing.Optional[str]
            Space separated ACR values, Unknown ACR are ignored. Only registered ACR values will be considered.
            If none of the provided acr value is among the registered values, all the registered ACR's will be considered.

        claims : typing.Optional[Claim]

        max_age : typing.Optional[float]
            Maximum Authentication Age. Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated by the OP. If the elapsed time is greater than this value, the OP MUST attempt to actively re-authenticate the End-User. (The max_age request parameter corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] max_auth_age request parameter.) When max_age is used, the ID Token returned MUST include an auth_time Claim Value.

        claims_locales : typing.Optional[str]
            End-User's preferred languages and scripts for Claims being returned, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.

        ui_locales : typing.Optional[str]
            End-User's preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.

        code_challenge : typing.Optional[str]
            A challenge derived from the code verifier, to be verified against later.

        code_challenge_method : typing.Optional[PostOauthParRequestCodeChallengeMethod]
            A method that was used to derive code challenge.

        id_token_hint : typing.Optional[str]
            ID Token previously issued by the Authorization Server being passed as a hint about the End-User's current or past authenticated session with the Client.

        dpop_jkt : typing.Optional[str]
            The value of the dpop_jkt authorization request parameter is the JWK Thumbprint [RFC7638] of the proof-of-possession public key using the SHA-256 hash function.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostOauthParResponse]
            CREATED
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/par",
            method="POST",
            data={
                "scope": scope,
                "response_type": response_type,
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "state": state,
                "nonce": nonce,
                "display": display,
                "prompt": prompt,
                "acr_values": acr_values,
                "claims": convert_and_respect_annotation_metadata(object_=claims, annotation=Claim, direction="write"),
                "max_age": max_age,
                "claims_locales": claims_locales,
                "ui_locales": ui_locales,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "id_token_hint": id_token_hint,
                "client_assertion_type": client_assertion_type,
                "client_assertion": client_assertion,
                "dpop_jkt": dpop_jkt,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
                "DPoP": str(d_po_p) if d_po_p is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostOauthParResponse,
                    parse_obj_as(
                        type_=PostOauthParResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        MethodNotAllowedErrorBody,
                        parse_obj_as(
                            type_=MethodNotAllowedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
