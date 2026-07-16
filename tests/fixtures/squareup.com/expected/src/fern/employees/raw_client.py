

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.list_employees_response import ListEmployeesResponse
from ..types.retrieve_employee_response import RetrieveEmployeeResponse
from pydantic import ValidationError


class RawEmployeesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_employees(
        self,
        *,
        location_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListEmployeesResponse]:
        """


        Parameters
        ----------
        location_id : typing.Optional[str]


        status : typing.Optional[str]
            Specifies the EmployeeStatus to filter the employee by.

        limit : typing.Optional[int]
            The number of employees to be returned on each page.

        cursor : typing.Optional[str]
            The token required to retrieve the specified page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListEmployeesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/employees",
            method="GET",
            params={
                "location_id": location_id,
                "status": status,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEmployeesResponse,
                    parse_obj_as(
                        type_=ListEmployeesResponse,
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

    def retrieve_employee(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveEmployeeResponse]:
        """


        Parameters
        ----------
        id : str
            UUID for the employee that was requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveEmployeeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/employees/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveEmployeeResponse,
                    parse_obj_as(
                        type_=RetrieveEmployeeResponse,
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


class AsyncRawEmployeesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_employees(
        self,
        *,
        location_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListEmployeesResponse]:
        """


        Parameters
        ----------
        location_id : typing.Optional[str]


        status : typing.Optional[str]
            Specifies the EmployeeStatus to filter the employee by.

        limit : typing.Optional[int]
            The number of employees to be returned on each page.

        cursor : typing.Optional[str]
            The token required to retrieve the specified page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListEmployeesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/employees",
            method="GET",
            params={
                "location_id": location_id,
                "status": status,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEmployeesResponse,
                    parse_obj_as(
                        type_=ListEmployeesResponse,
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

    async def retrieve_employee(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveEmployeeResponse]:
        """


        Parameters
        ----------
        id : str
            UUID for the employee that was requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveEmployeeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/employees/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveEmployeeResponse,
                    parse_obj_as(
                        type_=RetrieveEmployeeResponse,
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
