

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from ..types.introspection_response import IntrospectionResponse
from ..types.token_response import TokenResponse
from ..types.user_info import UserInfo
from .types.authorize_request_code_challenge_method import AuthorizeRequestCodeChallengeMethod
from .types.authorize_request_response_type import AuthorizeRequestResponseType
from .types.introspect_request_token_type_hint import IntrospectRequestTokenTypeHint
from .types.pushed_authorization_request_request_code_challenge_method import (
    PushedAuthorizationRequestRequestCodeChallengeMethod,
)
from .types.pushed_authorization_request_request_purpose import PushedAuthorizationRequestRequestPurpose
from .types.pushed_authorization_request_request_response_type import PushedAuthorizationRequestRequestResponseType
from .types.pushed_authorization_request_response import PushedAuthorizationRequestResponse
from .types.token_request_client_assertion_type import TokenRequestClientAssertionType
from .types.token_request_grant_type import TokenRequestGrantType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOAuth21OidcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def authorize(
        self,
        *,
        response_type: AuthorizeRequestResponseType,
        client_id: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: AuthorizeRequestCodeChallengeMethod,
        nonce: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        FAPI 2.0 compliant OAuth 2.1 authorization endpoint. Supports PAR (Pushed Authorization Requests)
        and requires PKCE for all authorization flows.

        Parameters
        ----------
        response_type : AuthorizeRequestResponseType
            Must be 'code' for authorization code flow

        client_id : str
            OAuth client identifier

        redirect_uri : str
            Client redirect URI

        scope : str
            Requested OAuth scopes

        state : str
            Client state parameter for CSRF protection

        code_challenge : str
            PKCE code challenge (S256)

        code_challenge_method : AuthorizeRequestCodeChallengeMethod
            PKCE code challenge method

        nonce : typing.Optional[str]
            OpenID Connect nonce

        request_uri : typing.Optional[str]
            PAR request URI (urn:ietf:params:oauth:request_uri:*)

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
                "response_type": response_type,
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "scope": scope,
                "state": state,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "nonce": nonce,
                "request_uri": request_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def token(
        self,
        *,
        grant_type: TokenRequestGrantType,
        client_id: str,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[TokenRequestClientAssertionType] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TokenResponse]:
        """
        FAPI 2.0 compliant token endpoint supporting authorization_code and refresh_token grants.
        Requires mTLS or private_key_jwt client authentication.

        Parameters
        ----------
        grant_type : TokenRequestGrantType

        client_id : str

        code : typing.Optional[str]
            Required for authorization_code grant

        redirect_uri : typing.Optional[str]
            Required for authorization_code grant

        code_verifier : typing.Optional[str]
            PKCE code verifier

        refresh_token : typing.Optional[str]
            Required for refresh_token grant

        client_assertion_type : typing.Optional[TokenRequestClientAssertionType]
            For private_key_jwt authentication

        client_assertion : typing.Optional[str]
            JWT assertion for private_key_jwt authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokenResponse]
            Access token response
        """
        _response = self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            data={
                "grant_type": grant_type,
                "client_id": client_id,
                "code": code,
                "redirect_uri": redirect_uri,
                "code_verifier": code_verifier,
                "refresh_token": refresh_token,
                "client_assertion_type": client_assertion_type,
                "client_assertion": client_assertion,
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
                    TokenResponse,
                    parse_obj_as(
                        type_=TokenResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def userinfo(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[UserInfo]:
        """
        Returns user information for the authenticated user. Supports DPoP token binding.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserInfo]
            User information
        """
        _response = self._client_wrapper.httpx_client.request(
            "userinfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserInfo,
                    parse_obj_as(
                        type_=UserInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def introspect(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[IntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IntrospectionResponse]:
        """
        RFC 7662 compliant token introspection endpoint for resource servers.

        Parameters
        ----------
        token : str
            Token to introspect

        token_type_hint : typing.Optional[IntrospectRequestTokenTypeHint]
            Hint about token type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IntrospectionResponse]
            Token introspection response
        """
        _response = self._client_wrapper.httpx_client.request(
            "introspect",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
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
                    IntrospectionResponse,
                    parse_obj_as(
                        type_=IntrospectionResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def pushed_authorization_request(
        self,
        *,
        client_id: str,
        response_type: PushedAuthorizationRequestRequestResponseType,
        scope: str,
        redirect_uri: str,
        code_challenge: str,
        code_challenge_method: PushedAuthorizationRequestRequestCodeChallengeMethod,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        purpose: typing.Optional[PushedAuthorizationRequestRequestPurpose] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PushedAuthorizationRequestResponse]:
        """
        FAPI 2.0 compliant PAR endpoint for securely submitting authorization request parameters.

        Parameters
        ----------
        client_id : str

        response_type : PushedAuthorizationRequestRequestResponseType

        scope : str

        redirect_uri : str

        code_challenge : str

        code_challenge_method : PushedAuthorizationRequestRequestCodeChallengeMethod

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        purpose : typing.Optional[PushedAuthorizationRequestRequestPurpose]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PushedAuthorizationRequestResponse]
            PAR response with request_uri
        """
        _response = self._client_wrapper.httpx_client.request(
            "par",
            method="POST",
            data={
                "client_id": client_id,
                "response_type": response_type,
                "scope": scope,
                "redirect_uri": redirect_uri,
                "state": state,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "nonce": nonce,
                "purpose": purpose,
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
                    PushedAuthorizationRequestResponse,
                    parse_obj_as(
                        type_=PushedAuthorizationRequestResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawOAuth21OidcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def authorize(
        self,
        *,
        response_type: AuthorizeRequestResponseType,
        client_id: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: AuthorizeRequestCodeChallengeMethod,
        nonce: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        FAPI 2.0 compliant OAuth 2.1 authorization endpoint. Supports PAR (Pushed Authorization Requests)
        and requires PKCE for all authorization flows.

        Parameters
        ----------
        response_type : AuthorizeRequestResponseType
            Must be 'code' for authorization code flow

        client_id : str
            OAuth client identifier

        redirect_uri : str
            Client redirect URI

        scope : str
            Requested OAuth scopes

        state : str
            Client state parameter for CSRF protection

        code_challenge : str
            PKCE code challenge (S256)

        code_challenge_method : AuthorizeRequestCodeChallengeMethod
            PKCE code challenge method

        nonce : typing.Optional[str]
            OpenID Connect nonce

        request_uri : typing.Optional[str]
            PAR request URI (urn:ietf:params:oauth:request_uri:*)

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
                "response_type": response_type,
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "scope": scope,
                "state": state,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "nonce": nonce,
                "request_uri": request_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def token(
        self,
        *,
        grant_type: TokenRequestGrantType,
        client_id: str,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[TokenRequestClientAssertionType] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TokenResponse]:
        """
        FAPI 2.0 compliant token endpoint supporting authorization_code and refresh_token grants.
        Requires mTLS or private_key_jwt client authentication.

        Parameters
        ----------
        grant_type : TokenRequestGrantType

        client_id : str

        code : typing.Optional[str]
            Required for authorization_code grant

        redirect_uri : typing.Optional[str]
            Required for authorization_code grant

        code_verifier : typing.Optional[str]
            PKCE code verifier

        refresh_token : typing.Optional[str]
            Required for refresh_token grant

        client_assertion_type : typing.Optional[TokenRequestClientAssertionType]
            For private_key_jwt authentication

        client_assertion : typing.Optional[str]
            JWT assertion for private_key_jwt authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokenResponse]
            Access token response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            data={
                "grant_type": grant_type,
                "client_id": client_id,
                "code": code,
                "redirect_uri": redirect_uri,
                "code_verifier": code_verifier,
                "refresh_token": refresh_token,
                "client_assertion_type": client_assertion_type,
                "client_assertion": client_assertion,
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
                    TokenResponse,
                    parse_obj_as(
                        type_=TokenResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def userinfo(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[UserInfo]:
        """
        Returns user information for the authenticated user. Supports DPoP token binding.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserInfo]
            User information
        """
        _response = await self._client_wrapper.httpx_client.request(
            "userinfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserInfo,
                    parse_obj_as(
                        type_=UserInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def introspect(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[IntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IntrospectionResponse]:
        """
        RFC 7662 compliant token introspection endpoint for resource servers.

        Parameters
        ----------
        token : str
            Token to introspect

        token_type_hint : typing.Optional[IntrospectRequestTokenTypeHint]
            Hint about token type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IntrospectionResponse]
            Token introspection response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "introspect",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
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
                    IntrospectionResponse,
                    parse_obj_as(
                        type_=IntrospectionResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def pushed_authorization_request(
        self,
        *,
        client_id: str,
        response_type: PushedAuthorizationRequestRequestResponseType,
        scope: str,
        redirect_uri: str,
        code_challenge: str,
        code_challenge_method: PushedAuthorizationRequestRequestCodeChallengeMethod,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        purpose: typing.Optional[PushedAuthorizationRequestRequestPurpose] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PushedAuthorizationRequestResponse]:
        """
        FAPI 2.0 compliant PAR endpoint for securely submitting authorization request parameters.

        Parameters
        ----------
        client_id : str

        response_type : PushedAuthorizationRequestRequestResponseType

        scope : str

        redirect_uri : str

        code_challenge : str

        code_challenge_method : PushedAuthorizationRequestRequestCodeChallengeMethod

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        purpose : typing.Optional[PushedAuthorizationRequestRequestPurpose]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PushedAuthorizationRequestResponse]
            PAR response with request_uri
        """
        _response = await self._client_wrapper.httpx_client.request(
            "par",
            method="POST",
            data={
                "client_id": client_id,
                "response_type": response_type,
                "scope": scope,
                "redirect_uri": redirect_uri,
                "state": state,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "nonce": nonce,
                "purpose": purpose,
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
                    PushedAuthorizationRequestResponse,
                    parse_obj_as(
                        type_=PushedAuthorizationRequestResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
