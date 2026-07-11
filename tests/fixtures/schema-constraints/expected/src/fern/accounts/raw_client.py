

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.account import Account


OMIT = typing.cast(typing.Any, ...)


class RawAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def createaccount(
        self,
        *,
        username: str,
        password: str,
        age: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Account]:
        """
        Parameters
        ----------
        username : str

        password : str

        age : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Account]

        """
        _response = self._client_wrapper.httpx_client.request(
            "account",
            method="POST",
            json={
                "username": username,
                "password": password,
                "age": age,
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
                    Account,
                    parse_obj_as(
                        type_=Account,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def createaccount(
        self,
        *,
        username: str,
        password: str,
        age: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Account]:
        """
        Parameters
        ----------
        username : str

        password : str

        age : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Account]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "account",
            method="POST",
            json={
                "username": username,
                "password": password,
                "age": age,
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
                    Account,
                    parse_obj_as(
                        type_=Account,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
