

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
from ..types.data_source_search_response import DataSourceSearchResponse
from ..types.datasource import Datasource
from ..types.error_response import ErrorResponse
from .types.search5request_logical_operator import Search5RequestLogicalOperator
from pydantic import ValidationError


class RawDataSourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search5(
        self,
        *,
        logical_operator: typing.Optional[Search5RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        official_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        english_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        legal_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        subjects: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        data_source_type_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        content_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_organization_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DataSourceSearchResponse]:
        """
        Explore data sources exploiting various filter parameters

        Parameters
        ----------
        logical_operator : typing.Optional[Search5RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        official_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The official name of the data source. Logical operator: *OR*

        english_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The English name of the data source. Logical operator: *OR*

        legal_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The legal name of the organization in short form. Logical operator: *OR*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the data source. Logical operator: *OR*

        pid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The persistent identifier of the data source. Logical operator: *OR*

        subjects : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of subjects associated to the datasource. Logical operator: *OR*

        data_source_type_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The data source type; see all possible values <a href='https://api.openaire.eu/vocabularies/dnet:datasource_typologies' target='_blank'>here</a>. Logical operator: *OR*

        content_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Types of content in the data source, as defined by OpenDOAR. Logical operator: *OR*

        rel_organization_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve data sources connected to the organization (with OpenAIRE id). Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve data sources connected to the community (with OpenAIRE id). Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve data sources collected from the data source (with OpenAIRE id). Logical operator: *OR*

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
            The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, organizations can be only sorted by the 'relevance'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DataSourceSearchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/dataSources",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "officialName": official_name,
                "englishName": english_name,
                "legalShortName": legal_short_name,
                "id": id,
                "pid": pid,
                "subjects": subjects,
                "dataSourceTypeName": data_source_type_name,
                "contentTypes": content_types,
                "relOrganizationId": rel_organization_id,
                "relCommunityId": rel_community_id,
                "relCollectedFromDatasourceId": rel_collected_from_datasource_id,
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
                    DataSourceSearchResponse,
                    parse_obj_as(
                        type_=DataSourceSearchResponse,
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

    def get_by_id5(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Datasource]:
        """
        Get a data source object by specifying its id.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the data source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Datasource]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dataSources/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Datasource,
                    parse_obj_as(
                        type_=Datasource,
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


class AsyncRawDataSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search5(
        self,
        *,
        logical_operator: typing.Optional[Search5RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        official_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        english_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        legal_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        subjects: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        data_source_type_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        content_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_organization_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DataSourceSearchResponse]:
        """
        Explore data sources exploiting various filter parameters

        Parameters
        ----------
        logical_operator : typing.Optional[Search5RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        official_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The official name of the data source. Logical operator: *OR*

        english_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The English name of the data source. Logical operator: *OR*

        legal_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The legal name of the organization in short form. Logical operator: *OR*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the data source. Logical operator: *OR*

        pid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The persistent identifier of the data source. Logical operator: *OR*

        subjects : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of subjects associated to the datasource. Logical operator: *OR*

        data_source_type_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The data source type; see all possible values <a href='https://api.openaire.eu/vocabularies/dnet:datasource_typologies' target='_blank'>here</a>. Logical operator: *OR*

        content_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Types of content in the data source, as defined by OpenDOAR. Logical operator: *OR*

        rel_organization_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve data sources connected to the organization (with OpenAIRE id). Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve data sources connected to the community (with OpenAIRE id). Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve data sources collected from the data source (with OpenAIRE id). Logical operator: *OR*

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
            The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, organizations can be only sorted by the 'relevance'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DataSourceSearchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/dataSources",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "officialName": official_name,
                "englishName": english_name,
                "legalShortName": legal_short_name,
                "id": id,
                "pid": pid,
                "subjects": subjects,
                "dataSourceTypeName": data_source_type_name,
                "contentTypes": content_types,
                "relOrganizationId": rel_organization_id,
                "relCommunityId": rel_community_id,
                "relCollectedFromDatasourceId": rel_collected_from_datasource_id,
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
                    DataSourceSearchResponse,
                    parse_obj_as(
                        type_=DataSourceSearchResponse,
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

    async def get_by_id5(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Datasource]:
        """
        Get a data source object by specifying its id.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the data source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Datasource]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dataSources/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Datasource,
                    parse_obj_as(
                        type_=Datasource,
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
