

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.recursive_types_category_response import RecursiveTypesCategoryResponse
from .types.recursive_types_linked_list_response import RecursiveTypesLinkedListResponse
from .types.recursive_types_tree_response import RecursiveTypesTreeResponse
from pydantic import ValidationError


class RawRecursiveTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def recursive_types_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RecursiveTypesTreeResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RecursiveTypesTreeResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "recursiveTypes.tree",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecursiveTypesTreeResponse,
                    parse_obj_as(
                        type_=RecursiveTypesTreeResponse,
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

    def recursive_types_linked_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RecursiveTypesLinkedListResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RecursiveTypesLinkedListResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "recursiveTypes.linkedList",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecursiveTypesLinkedListResponse,
                    parse_obj_as(
                        type_=RecursiveTypesLinkedListResponse,
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

    def recursive_types_category(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RecursiveTypesCategoryResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RecursiveTypesCategoryResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "recursiveTypes.category",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecursiveTypesCategoryResponse,
                    parse_obj_as(
                        type_=RecursiveTypesCategoryResponse,
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


class AsyncRawRecursiveTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def recursive_types_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RecursiveTypesTreeResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RecursiveTypesTreeResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "recursiveTypes.tree",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecursiveTypesTreeResponse,
                    parse_obj_as(
                        type_=RecursiveTypesTreeResponse,
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

    async def recursive_types_linked_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RecursiveTypesLinkedListResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RecursiveTypesLinkedListResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "recursiveTypes.linkedList",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecursiveTypesLinkedListResponse,
                    parse_obj_as(
                        type_=RecursiveTypesLinkedListResponse,
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

    async def recursive_types_category(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RecursiveTypesCategoryResponse]:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RecursiveTypesCategoryResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "recursiveTypes.category",
            method="GET",
            params={
                "input": input,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecursiveTypesCategoryResponse,
                    parse_obj_as(
                        type_=RecursiveTypesCategoryResponse,
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
