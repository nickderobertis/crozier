

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIdentityRegistrationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def display_the_registration_form(
        self, *, request: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            HTML page
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounts/users/register",
            method="GET",
            params={
                "request": request,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def register_a_user(
        self,
        *,
        user_email: str,
        user_password: str,
        request: typing.Optional[str] = None,
        user_metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        user_email : str

        user_password : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        user_metadata : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            HTML page
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounts/users/register",
            method="POST",
            params={
                "request": request,
            },
            data={
                "user[email]": user_email,
                "user[password]": user_password,
                "user[metadata]": user_metadata,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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


class AsyncRawIdentityRegistrationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def display_the_registration_form(
        self, *, request: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            HTML page
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounts/users/register",
            method="GET",
            params={
                "request": request,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def register_a_user(
        self,
        *,
        user_email: str,
        user_password: str,
        request: typing.Optional[str] = None,
        user_metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        user_email : str

        user_password : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        user_metadata : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            HTML page
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounts/users/register",
            method="POST",
            params={
                "request": request,
            },
            data={
                "user[email]": user_email,
                "user[password]": user_password,
                "user[metadata]": user_metadata,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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
