

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.token_request_token_scope import TokenRequestTokenScope
from .types.create_token_response import CreateTokenResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_token(
        self,
        *,
        username: str,
        password: str,
        token_name: str,
        token_scope: TokenRequestTokenScope,
        token_expire: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTokenResponse]:
        """
        Generate a new token to access REST API

        Parameters
        ----------
        username : str
            Username of the login user.

        password : str
            Password of the user trying to login.

        token_name : str
            Friendly name of the token

        token_scope : TokenRequestTokenScope
            The scope of the token.

        token_expire : dt.date
            Date when the token must expire (default max 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTokenResponse]
            Token generated
        """
        _response = self._client_wrapper.httpx_client.request(
            "tokens",
            method="POST",
            data={
                "username": username,
                "password": password,
                "token_name": token_name,
                "token_scope": token_scope,
                "token_expire": token_expire,
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
                    CreateTokenResponse,
                    parse_obj_as(
                        type_=CreateTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_token(
        self,
        *,
        username: str,
        password: str,
        token_name: str,
        token_scope: TokenRequestTokenScope,
        token_expire: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTokenResponse]:
        """
        Generate a new token to access REST API

        Parameters
        ----------
        username : str
            Username of the login user.

        password : str
            Password of the user trying to login.

        token_name : str
            Friendly name of the token

        token_scope : TokenRequestTokenScope
            The scope of the token.

        token_expire : dt.date
            Date when the token must expire (default max 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTokenResponse]
            Token generated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tokens",
            method="POST",
            data={
                "username": username,
                "password": password,
                "token_name": token_name,
                "token_scope": token_scope,
                "token_expire": token_expire,
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
                    CreateTokenResponse,
                    parse_obj_as(
                        type_=CreateTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
