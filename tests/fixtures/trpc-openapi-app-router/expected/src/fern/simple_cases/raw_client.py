

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.simple_cases_nullable_response import SimpleCasesNullableResponse
from .types.simple_cases_nullish_response import SimpleCasesNullishResponse
from .types.simple_cases_optional_response import SimpleCasesOptionalResponse
from pydantic import ValidationError


class RawSimpleCasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def simple_cases_nullish(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SimpleCasesNullishResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SimpleCasesNullishResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "simpleCases.nullish",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimpleCasesNullishResponse,
                    parse_obj_as(
                        type_=SimpleCasesNullishResponse,
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

    def simple_cases_optional(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SimpleCasesOptionalResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SimpleCasesOptionalResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "simpleCases.optional",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimpleCasesOptionalResponse,
                    parse_obj_as(
                        type_=SimpleCasesOptionalResponse,
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

    def simple_cases_nullable(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SimpleCasesNullableResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SimpleCasesNullableResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "simpleCases.nullable",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimpleCasesNullableResponse,
                    parse_obj_as(
                        type_=SimpleCasesNullableResponse,
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


class AsyncRawSimpleCasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def simple_cases_nullish(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SimpleCasesNullishResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SimpleCasesNullishResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "simpleCases.nullish",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimpleCasesNullishResponse,
                    parse_obj_as(
                        type_=SimpleCasesNullishResponse,
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

    async def simple_cases_optional(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SimpleCasesOptionalResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SimpleCasesOptionalResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "simpleCases.optional",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimpleCasesOptionalResponse,
                    parse_obj_as(
                        type_=SimpleCasesOptionalResponse,
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

    async def simple_cases_nullable(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SimpleCasesNullableResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SimpleCasesNullableResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "simpleCases.nullable",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimpleCasesNullableResponse,
                    parse_obj_as(
                        type_=SimpleCasesNullableResponse,
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
