

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
from ..types.error import Error
from .types.get_access_token_request_grant_type import GetAccessTokenRequestGrantType
from .types.get_access_token_response import GetAccessTokenResponse
from .types.get_rate_limit_response import GetRateLimitResponse
from .types.register_application_response import RegisterApplicationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register_application(
        self, *, name: str, description: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegisterApplicationResponse]:
        """
        Register a new application to obtain client credentials for API access.

        Parameters
        ----------
        name : str
            Application name

        description : str
            Application description

        email : str
            Contact email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegisterApplicationResponse]
            Application registered successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth_tokens/register",
            method="POST",
            json={
                "name": name,
                "description": description,
                "email": email,
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
                    RegisterApplicationResponse,
                    parse_obj_as(
                        type_=RegisterApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_access_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: GetAccessTokenRequestGrantType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAccessTokenResponse]:
        """
        Exchange client credentials for an API access token.

        Parameters
        ----------
        client_id : str

        client_secret : str

        grant_type : GetAccessTokenRequestGrantType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAccessTokenResponse]
            Access token
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth_tokens/token",
            method="POST",
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": grant_type,
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
                    GetAccessTokenResponse,
                    parse_obj_as(
                        type_=GetAccessTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_rate_limit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetRateLimitResponse]:
        """
        Check the current rate limit status for your API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRateLimitResponse]
            Rate limit status
        """
        _response = self._client_wrapper.httpx_client.request(
            "rate_limit",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRateLimitResponse,
                    parse_obj_as(
                        type_=GetRateLimitResponse,
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


class AsyncRawAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register_application(
        self, *, name: str, description: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegisterApplicationResponse]:
        """
        Register a new application to obtain client credentials for API access.

        Parameters
        ----------
        name : str
            Application name

        description : str
            Application description

        email : str
            Contact email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegisterApplicationResponse]
            Application registered successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth_tokens/register",
            method="POST",
            json={
                "name": name,
                "description": description,
                "email": email,
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
                    RegisterApplicationResponse,
                    parse_obj_as(
                        type_=RegisterApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_access_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: GetAccessTokenRequestGrantType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAccessTokenResponse]:
        """
        Exchange client credentials for an API access token.

        Parameters
        ----------
        client_id : str

        client_secret : str

        grant_type : GetAccessTokenRequestGrantType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAccessTokenResponse]
            Access token
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth_tokens/token",
            method="POST",
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": grant_type,
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
                    GetAccessTokenResponse,
                    parse_obj_as(
                        type_=GetAccessTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_rate_limit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetRateLimitResponse]:
        """
        Check the current rate limit status for your API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRateLimitResponse]
            Rate limit status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "rate_limit",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRateLimitResponse,
                    parse_obj_as(
                        type_=GetRateLimitResponse,
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
