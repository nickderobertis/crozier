

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.v1o_auth_authorized_application import V1OAuthAuthorizedApplication
from ..types.v1o_auth_introspect_response import V1OAuthIntrospectResponse
from ..types.v1o_auth_token_response import V1OAuthTokenResponse
from .types.get_current_token_info_response import GetCurrentTokenInfoResponse
from .types.v1o_auth_introspect_request_token_type_hint import V1OAuthIntrospectRequestTokenTypeHint
from .types.v1o_auth_revoke_request_token_type_hint import V1OAuthRevokeRequestTokenTypeHint
from .types.v1o_auth_token_request_grant_type import V1OAuthTokenRequestGrantType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_access_token(
        self,
        *,
        grant_type: V1OAuthTokenRequestGrantType,
        client_id: str,
        client_secret: str,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1OAuthTokenResponse]:
        """
        Exchange an authorization code for an access token using OAuth 2.0 authorization code flow.

        Parameters
        ----------
        grant_type : V1OAuthTokenRequestGrantType
            OAuth 2.0 grant type

        client_id : str
            OAuth 2.0 client identifier

        client_secret : str
            OAuth 2.0 client secret

        code : typing.Optional[str]
            Authorization code (required for authorization_code grant)

        redirect_uri : typing.Optional[str]
            Redirect URI (required for authorization_code grant)

        refresh_token : typing.Optional[str]
            Refresh token (required for refresh_token grant)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1OAuthTokenResponse]
            access token created
        """
        _response = self._client_wrapper.httpx_client.request(
            "1.1/oauth/token",
            method="POST",
            json={
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "redirect_uri": redirect_uri,
                "refresh_token": refresh_token,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1OAuthTokenResponse,
                    parse_obj_as(
                        type_=V1OAuthTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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

    def revoke_access_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[V1OAuthRevokeRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Revoke an access token or refresh token.

        Parameters
        ----------
        token : str
            OAuth 2.0 access or refresh token to revoke

        token_type_hint : typing.Optional[V1OAuthRevokeRequestTokenTypeHint]
            Hint about the type of token being revoked

        client_id : typing.Optional[str]
            OAuth 2.0 client identifier

        client_secret : typing.Optional[str]
            OAuth 2.0 client secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            token revoked
        """
        _response = self._client_wrapper.httpx_client.request(
            "1.1/oauth/revoke",
            method="POST",
            json={
                "token": token,
                "token_type_hint": token_type_hint,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def introspect_access_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[V1OAuthIntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1OAuthIntrospectResponse]:
        """
        Check if an access token is active and get its metadata.

        Parameters
        ----------
        token : str
            OAuth 2.0 access token to introspect

        token_type_hint : typing.Optional[V1OAuthIntrospectRequestTokenTypeHint]
            Hint about the type of token being introspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1OAuthIntrospectResponse]
            token introspection result
        """
        _response = self._client_wrapper.httpx_client.request(
            "1.1/oauth/introspect",
            method="POST",
            json={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1OAuthIntrospectResponse,
                    parse_obj_as(
                        type_=V1OAuthIntrospectResponse,
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

    def get_current_token_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetCurrentTokenInfoResponse]:
        """
        Get information about the current access token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCurrentTokenInfoResponse]
            token info
        """
        _response = self._client_wrapper.httpx_client.request(
            "1.1/oauth/token/info",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCurrentTokenInfoResponse,
                    parse_obj_as(
                        type_=GetCurrentTokenInfoResponse,
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

    def list_authorized_applications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[V1OAuthAuthorizedApplication]]:
        """
        List applications that the current user has authorized.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1OAuthAuthorizedApplication]]
            authorized applications
        """
        _response = self._client_wrapper.httpx_client.request(
            "1.1/oauth/authorized_applications",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1OAuthAuthorizedApplication],
                    parse_obj_as(
                        type_=typing.List[V1OAuthAuthorizedApplication],
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

    def revoke_application_authorization(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Revoke authorization for a specific application.

        Parameters
        ----------
        id : int
            Application ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/oauth/authorized_applications/{encode_path_param(id)}",
            method="DELETE",
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
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawOAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_access_token(
        self,
        *,
        grant_type: V1OAuthTokenRequestGrantType,
        client_id: str,
        client_secret: str,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1OAuthTokenResponse]:
        """
        Exchange an authorization code for an access token using OAuth 2.0 authorization code flow.

        Parameters
        ----------
        grant_type : V1OAuthTokenRequestGrantType
            OAuth 2.0 grant type

        client_id : str
            OAuth 2.0 client identifier

        client_secret : str
            OAuth 2.0 client secret

        code : typing.Optional[str]
            Authorization code (required for authorization_code grant)

        redirect_uri : typing.Optional[str]
            Redirect URI (required for authorization_code grant)

        refresh_token : typing.Optional[str]
            Refresh token (required for refresh_token grant)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1OAuthTokenResponse]
            access token created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "1.1/oauth/token",
            method="POST",
            json={
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "redirect_uri": redirect_uri,
                "refresh_token": refresh_token,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1OAuthTokenResponse,
                    parse_obj_as(
                        type_=V1OAuthTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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

    async def revoke_access_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[V1OAuthRevokeRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Revoke an access token or refresh token.

        Parameters
        ----------
        token : str
            OAuth 2.0 access or refresh token to revoke

        token_type_hint : typing.Optional[V1OAuthRevokeRequestTokenTypeHint]
            Hint about the type of token being revoked

        client_id : typing.Optional[str]
            OAuth 2.0 client identifier

        client_secret : typing.Optional[str]
            OAuth 2.0 client secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            token revoked
        """
        _response = await self._client_wrapper.httpx_client.request(
            "1.1/oauth/revoke",
            method="POST",
            json={
                "token": token,
                "token_type_hint": token_type_hint,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def introspect_access_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[V1OAuthIntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1OAuthIntrospectResponse]:
        """
        Check if an access token is active and get its metadata.

        Parameters
        ----------
        token : str
            OAuth 2.0 access token to introspect

        token_type_hint : typing.Optional[V1OAuthIntrospectRequestTokenTypeHint]
            Hint about the type of token being introspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1OAuthIntrospectResponse]
            token introspection result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "1.1/oauth/introspect",
            method="POST",
            json={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1OAuthIntrospectResponse,
                    parse_obj_as(
                        type_=V1OAuthIntrospectResponse,
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

    async def get_current_token_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCurrentTokenInfoResponse]:
        """
        Get information about the current access token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCurrentTokenInfoResponse]
            token info
        """
        _response = await self._client_wrapper.httpx_client.request(
            "1.1/oauth/token/info",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCurrentTokenInfoResponse,
                    parse_obj_as(
                        type_=GetCurrentTokenInfoResponse,
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

    async def list_authorized_applications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[V1OAuthAuthorizedApplication]]:
        """
        List applications that the current user has authorized.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1OAuthAuthorizedApplication]]
            authorized applications
        """
        _response = await self._client_wrapper.httpx_client.request(
            "1.1/oauth/authorized_applications",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1OAuthAuthorizedApplication],
                    parse_obj_as(
                        type_=typing.List[V1OAuthAuthorizedApplication],
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

    async def revoke_application_authorization(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Revoke authorization for a specific application.

        Parameters
        ----------
        id : int
            Application ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/oauth/authorized_applications/{encode_path_param(id)}",
            method="DELETE",
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
            if _response.status_code == 404:
                raise NotFoundError(
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
