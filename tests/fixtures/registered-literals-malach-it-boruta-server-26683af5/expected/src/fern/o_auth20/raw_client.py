

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.introspection_response import IntrospectionResponse
from ..types.o_auth_error import OAuthError
from ..types.pushed_authorization_response import PushedAuthorizationResponse
from ..types.token_request_grant_type import TokenRequestGrantType
from ..types.token_response import TokenResponse
from .types.get_oauth_authorize_request_code_challenge_method import GetOauthAuthorizeRequestCodeChallengeMethod
from .types.post_oauth_introspect_request_token_type_hint import PostOauthIntrospectRequestTokenTypeHint
from .types.post_oauth_pushed_authorization_request_request_code_challenge_method import (
    PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod,
)
from .types.post_oauth_revoke_request_token_type_hint import PostOauthRevokeRequestTokenTypeHint
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOAuth20Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def start_an_authorization_request(
        self,
        *,
        client_id: str,
        response_type: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        nonce: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[GetOauthAuthorizeRequestCodeChallengeMethod] = None,
        prompt: typing.Optional[str] = None,
        max_age: typing.Optional[int] = None,
        request: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        client_id : str

        response_type : str

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[GetOauthAuthorizeRequestCodeChallengeMethod]

        prompt : typing.Optional[str]

        max_age : typing.Optional[int]

        request : typing.Optional[str]
            JWT-secured authorization request

        request_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            HTML page
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/authorize",
            method="GET",
            params={
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "response_type": response_type,
                "scope": scope,
                "state": state,
                "nonce": nonce,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "prompt": prompt,
                "max_age": max_age,
                "request": request,
                "request_uri": request_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
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

    def issue_or_refresh_tokens(
        self,
        *,
        grant_type: TokenRequestGrantType,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[str] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TokenResponse]:
        """
        Parameters
        ----------
        grant_type : TokenRequestGrantType

        code : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        code_verifier : typing.Optional[str]

        refresh_token : typing.Optional[str]

        username : typing.Optional[str]

        password : typing.Optional[str]

        scope : typing.Optional[str]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        client_assertion_type : typing.Optional[str]

        client_assertion : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokenResponse]
            Token response
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "code": code,
                "redirect_uri": redirect_uri,
                "code_verifier": code_verifier,
                "refresh_token": refresh_token,
                "username": username,
                "password": password,
                "scope": scope,
                "client_id": client_id,
                "client_secret": client_secret,
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
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def introspect_a_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostOauthIntrospectRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IntrospectionResponse]:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostOauthIntrospectRequestTokenTypeHint]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IntrospectionResponse]
            Token introspection result
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/introspect",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
                "client_id": client_id,
                "client_secret": client_secret,
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
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def create_a_pushed_authorization_request(
        self,
        *,
        client_id: str,
        response_type: str,
        client_secret: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        code_challenge: typing.Optional[str] = OMIT,
        code_challenge_method: typing.Optional[PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod] = OMIT,
        request: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PushedAuthorizationResponse]:
        """
        Parameters
        ----------
        client_id : str

        response_type : str

        client_secret : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod]

        request : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PushedAuthorizationResponse]
            Pushed authorization request created
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/pushed_authorization_request",
            method="POST",
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "redirect_uri": redirect_uri,
                "response_type": response_type,
                "scope": scope,
                "state": state,
                "nonce": nonce,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "request": request,
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
                    PushedAuthorizationResponse,
                    parse_obj_as(
                        type_=PushedAuthorizationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def revoke_a_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostOauthRevokeRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostOauthRevokeRequestTokenTypeHint]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/revoke",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
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


class AsyncRawOAuth20Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def start_an_authorization_request(
        self,
        *,
        client_id: str,
        response_type: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        nonce: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[GetOauthAuthorizeRequestCodeChallengeMethod] = None,
        prompt: typing.Optional[str] = None,
        max_age: typing.Optional[int] = None,
        request: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        client_id : str

        response_type : str

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[GetOauthAuthorizeRequestCodeChallengeMethod]

        prompt : typing.Optional[str]

        max_age : typing.Optional[int]

        request : typing.Optional[str]
            JWT-secured authorization request

        request_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            HTML page
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/authorize",
            method="GET",
            params={
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "response_type": response_type,
                "scope": scope,
                "state": state,
                "nonce": nonce,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "prompt": prompt,
                "max_age": max_age,
                "request": request,
                "request_uri": request_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
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

    async def issue_or_refresh_tokens(
        self,
        *,
        grant_type: TokenRequestGrantType,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[str] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TokenResponse]:
        """
        Parameters
        ----------
        grant_type : TokenRequestGrantType

        code : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        code_verifier : typing.Optional[str]

        refresh_token : typing.Optional[str]

        username : typing.Optional[str]

        password : typing.Optional[str]

        scope : typing.Optional[str]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        client_assertion_type : typing.Optional[str]

        client_assertion : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokenResponse]
            Token response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "code": code,
                "redirect_uri": redirect_uri,
                "code_verifier": code_verifier,
                "refresh_token": refresh_token,
                "username": username,
                "password": password,
                "scope": scope,
                "client_id": client_id,
                "client_secret": client_secret,
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
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def introspect_a_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostOauthIntrospectRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IntrospectionResponse]:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostOauthIntrospectRequestTokenTypeHint]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IntrospectionResponse]
            Token introspection result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/introspect",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
                "client_id": client_id,
                "client_secret": client_secret,
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
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def create_a_pushed_authorization_request(
        self,
        *,
        client_id: str,
        response_type: str,
        client_secret: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        code_challenge: typing.Optional[str] = OMIT,
        code_challenge_method: typing.Optional[PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod] = OMIT,
        request: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PushedAuthorizationResponse]:
        """
        Parameters
        ----------
        client_id : str

        response_type : str

        client_secret : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod]

        request : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PushedAuthorizationResponse]
            Pushed authorization request created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/pushed_authorization_request",
            method="POST",
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "redirect_uri": redirect_uri,
                "response_type": response_type,
                "scope": scope,
                "state": state,
                "nonce": nonce,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "request": request,
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
                    PushedAuthorizationResponse,
                    parse_obj_as(
                        type_=PushedAuthorizationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def revoke_a_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostOauthRevokeRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostOauthRevokeRequestTokenTypeHint]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/revoke",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
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
