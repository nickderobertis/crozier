

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.access_token import AccessToken
from ..types.bad_request import BadRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAdvancedAuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_auth_api_key(
        self, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AccessToken]:
        """
        Returns a bearer token that can be used to authenticate other endpoint.

        You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

        Parameters
        ----------
        api_key : str
            Your account API key. You can use your sandbox API key, or you can use your production API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccessToken]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/api-key",
            method="POST",
            json={
                "apiKey": api_key,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest,
                        parse_obj_as(
                            type_=BadRequest,
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

    def post_auth_refresh(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AccessToken]:
        """
        Accepts the old bearer token and returns a new bearer token that can be used to authenticate other endpoint.

        You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

        Parameters
        ----------
        refresh_token : str
            The refresh token is either the first refresh token you received when you authenticated with the auth/api-key endpoint, or it's the refresh token from the last time you used the auth/refresh endpoint. Place this in the body of your request to obtain a new access token (which is valid for an hour) and a new refresh token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccessToken]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/refresh",
            method="POST",
            json={
                "refreshToken": refresh_token,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest,
                        parse_obj_as(
                            type_=BadRequest,
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


class AsyncRawAdvancedAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_auth_api_key(
        self, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AccessToken]:
        """
        Returns a bearer token that can be used to authenticate other endpoint.

        You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

        Parameters
        ----------
        api_key : str
            Your account API key. You can use your sandbox API key, or you can use your production API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccessToken]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/api-key",
            method="POST",
            json={
                "apiKey": api_key,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest,
                        parse_obj_as(
                            type_=BadRequest,
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

    async def post_auth_refresh(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AccessToken]:
        """
        Accepts the old bearer token and returns a new bearer token that can be used to authenticate other endpoint.

        You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

        Parameters
        ----------
        refresh_token : str
            The refresh token is either the first refresh token you received when you authenticated with the auth/api-key endpoint, or it's the refresh token from the last time you used the auth/refresh endpoint. Place this in the body of your request to obtain a new access token (which is valid for an hour) and a new refresh token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccessToken]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/refresh",
            method="POST",
            json={
                "refreshToken": refresh_token,
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
                    AccessToken,
                    parse_obj_as(
                        type_=AccessToken,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequest,
                        parse_obj_as(
                            type_=BadRequest,
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
