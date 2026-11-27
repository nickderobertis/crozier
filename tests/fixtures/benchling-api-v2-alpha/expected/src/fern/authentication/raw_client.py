

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
from ..types.o_auth_unauthorized_error import OAuthUnauthorizedError
from ..types.token_create_grant_type import TokenCreateGrantType
from ..types.token_response import TokenResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate_token(
        self,
        *,
        grant_type: TokenCreateGrantType,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TokenResponse]:
        """
        Generate a token

        Parameters
        ----------
        grant_type : TokenCreateGrantType

        client_id : typing.Optional[str]
            ID of client to request token for. Leave off if client ID and secret are being supplied through Authorization header.

        client_secret : typing.Optional[str]
            Leave off if client ID and secret are being supplied through Authorization header.

        code : typing.Optional[str]
            Authorization code to request token for. Required if grant_type is authorization_code.

        code_verifier : typing.Optional[str]
            Code verifier to request token for. Only required if code_verifier is provided in the authorization code request.

        redirect_uri : typing.Optional[str]
            Redirect URI to request token for. Required if grant_type is authorization_code.

        state : typing.Optional[str]
            State to request token for. Only required if state is provided in the authorization code request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokenResponse]
            Generated token
        """
        _response = self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "code_verifier": code_verifier,
                "grant_type": grant_type,
                "redirect_uri": redirect_uri,
                "state": state,
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
                        OAuthUnauthorizedError,
                        parse_obj_as(
                            type_=OAuthUnauthorizedError,
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


class AsyncRawAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def generate_token(
        self,
        *,
        grant_type: TokenCreateGrantType,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TokenResponse]:
        """
        Generate a token

        Parameters
        ----------
        grant_type : TokenCreateGrantType

        client_id : typing.Optional[str]
            ID of client to request token for. Leave off if client ID and secret are being supplied through Authorization header.

        client_secret : typing.Optional[str]
            Leave off if client ID and secret are being supplied through Authorization header.

        code : typing.Optional[str]
            Authorization code to request token for. Required if grant_type is authorization_code.

        code_verifier : typing.Optional[str]
            Code verifier to request token for. Only required if code_verifier is provided in the authorization code request.

        redirect_uri : typing.Optional[str]
            Redirect URI to request token for. Required if grant_type is authorization_code.

        state : typing.Optional[str]
            State to request token for. Only required if state is provided in the authorization code request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokenResponse]
            Generated token
        """
        _response = await self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "code_verifier": code_verifier,
                "grant_type": grant_type,
                "redirect_uri": redirect_uri,
                "state": state,
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
                        OAuthUnauthorizedError,
                        parse_obj_as(
                            type_=OAuthUnauthorizedError,
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
