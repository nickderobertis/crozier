

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from .types.get_api_endpoint_request_endpoint import GetApiEndpointRequestEndpoint
from pydantic import ValidationError


class RawCommonClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all_resource_ur_ls(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, str]]:
        """
        Making a request to the API's base URL returns an object containing available endpoints.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, str],
                    parse_obj_as(
                        type_=typing.Dict[str, str],
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

    def get_list_of_all_available_resources_for_an_endpoint(
        self, endpoint: GetApiEndpointRequestEndpoint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiReferenceList]:
        """
        Currently only the [`/spells`](#get-/api/spells) and [`/monsters`](#get-/api/monsters) endpoints support filtering with query parameters. Use of these query parameters is documented under the respective [Spells](#tag--Spells) and [Monsters](#tag--Monsters) sections.

        Parameters
        ----------
        endpoint : GetApiEndpointRequestEndpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiReferenceList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/{encode_path_param(endpoint)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
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


class AsyncRawCommonClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all_resource_ur_ls(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, str]]:
        """
        Making a request to the API's base URL returns an object containing available endpoints.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, str],
                    parse_obj_as(
                        type_=typing.Dict[str, str],
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

    async def get_list_of_all_available_resources_for_an_endpoint(
        self, endpoint: GetApiEndpointRequestEndpoint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiReferenceList]:
        """
        Currently only the [`/spells`](#get-/api/spells) and [`/monsters`](#get-/api/monsters) endpoints support filtering with query parameters. Use of these query parameters is documented under the respective [Spells](#tag--Spells) and [Monsters](#tag--Monsters) sections.

        Parameters
        ----------
        endpoint : GetApiEndpointRequestEndpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiReferenceList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/{encode_path_param(endpoint)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
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
