

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.api_person import ApiPerson
from ..types.error_response import ErrorResponse
from ..types.graph_result import GraphResult
from .types.search3request_logical_operator import Search3RequestLogicalOperator
from pydantic import ValidationError


class RawPersonsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search3(
        self,
        *,
        logical_operator: typing.Optional[Search3RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        original_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        given_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPerson]:
        """
        Search for persons using filters and pagination options

        Parameters
        ----------
        logical_operator : typing.Optional[Search3RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the project. Logical operator: *OR*

        original_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the record at the original sources. Logical operator: *OR*

        given_name : typing.Optional[str]
            The given name of the person. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        last_name : typing.Optional[str]
            The last name of the person. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        page : typing.Optional[int]
            Page number of the results,
            used for basic start/rows pagination.
            Max dataset to retrieve - 10000 records.
            To get more than that, use cursor-based pagination.

        page_size : typing.Optional[int]
            Number of results per page

        cursor : typing.Optional[str]
            Cursor-based pagination. Initial value: `cursor=*`.
            Cursor should be used when it is required to retrieve a big dataset (more than 10000 records).
            To get the next page of results, use nextCursor returned in the response.

        sort_by : typing.Optional[str]
            The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'startDate', 'endDate'. Multiple sorting parameters should be comma-separated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPerson]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/persons",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "id": id,
                "originalId": original_id,
                "givenName": given_name,
                "lastName": last_name,
                "page": page,
                "pageSize": page_size,
                "cursor": cursor,
                "sortBy": sort_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPerson,
                    parse_obj_as(
                        type_=ApiPerson,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_by_id3(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GraphResult]:
        """
        Retrieve a person by id

        Parameters
        ----------
        id : str
            The OpenAIRE id of the person

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GraphResult]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/persons/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GraphResult,
                    parse_obj_as(
                        type_=GraphResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawPersonsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search3(
        self,
        *,
        logical_operator: typing.Optional[Search3RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        original_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        given_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPerson]:
        """
        Search for persons using filters and pagination options

        Parameters
        ----------
        logical_operator : typing.Optional[Search3RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the project. Logical operator: *OR*

        original_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the record at the original sources. Logical operator: *OR*

        given_name : typing.Optional[str]
            The given name of the person. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        last_name : typing.Optional[str]
            The last name of the person. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        page : typing.Optional[int]
            Page number of the results,
            used for basic start/rows pagination.
            Max dataset to retrieve - 10000 records.
            To get more than that, use cursor-based pagination.

        page_size : typing.Optional[int]
            Number of results per page

        cursor : typing.Optional[str]
            Cursor-based pagination. Initial value: `cursor=*`.
            Cursor should be used when it is required to retrieve a big dataset (more than 10000 records).
            To get the next page of results, use nextCursor returned in the response.

        sort_by : typing.Optional[str]
            The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'startDate', 'endDate'. Multiple sorting parameters should be comma-separated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPerson]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/persons",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "id": id,
                "originalId": original_id,
                "givenName": given_name,
                "lastName": last_name,
                "page": page,
                "pageSize": page_size,
                "cursor": cursor,
                "sortBy": sort_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPerson,
                    parse_obj_as(
                        type_=ApiPerson,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_by_id3(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GraphResult]:
        """
        Retrieve a person by id

        Parameters
        ----------
        id : str
            The OpenAIRE id of the person

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GraphResult]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/persons/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GraphResult,
                    parse_obj_as(
                        type_=GraphResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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
