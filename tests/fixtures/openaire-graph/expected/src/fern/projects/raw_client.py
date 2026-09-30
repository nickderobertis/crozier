

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.error_response import ErrorResponse
from ..types.project_search_response import ProjectSearchResponse
from ..types.search_response import SearchResponse
from .types.search2request_logical_operator import Search2RequestLogicalOperator
from .types.search8request_format import Search8RequestFormat
from pydantic import ValidationError


class RawProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search2(
        self,
        *,
        logical_operator: typing.Optional[Search2RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        keywords: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        acronym: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        call_identifier: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        funding_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        funding_stream_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_start_date: typing.Optional[str] = None,
        to_start_date: typing.Optional[str] = None,
        from_end_date: typing.Optional[str] = None,
        to_end_date: typing.Optional[str] = None,
        rel_organization_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_organization_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_organization_country_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchResponse]:
        """
        Explore projects exploiting various filter parameters

        Parameters
        ----------
        logical_operator : typing.Optional[Search2RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        title : typing.Optional[str]
            Search in the project's title. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        keywords : typing.Optional[str]
            The project's keywords. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the project. Logical operator: *OR*

        code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The grant agreement (GA) code of the project. Logical operator: *OR*

        acronym : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Project's acronym. Logical operator: *OR*

        call_identifier : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the research call. Logical operator: *OR*

        funding_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The short name of the funder. Logical operator: *OR*

        funding_stream_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the funding stream. Logical operator: *OR*

        from_start_date : typing.Optional[str]
            Gets the projects with start date greater than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        to_start_date : typing.Optional[str]
            Gets the projects with start date less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        from_end_date : typing.Optional[str]
            Gets the projects with end date greater than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        to_end_date : typing.Optional[str]
            Gets the projects with end date less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        rel_organization_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The name or short name of the related organization. Logical operator: *OR*

        rel_organization_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The organization identifier of the related organization. Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve projects connected to the community (with OpenAIRE id). Logical operator: *OR*

        rel_organization_country_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The country code of the related organizations. Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve projects collected from the data source (with OpenAIRE id). Logical operator: *OR*

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
        HttpResponse[SearchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/projects",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "title": title,
                "keywords": keywords,
                "id": id,
                "code": code,
                "acronym": acronym,
                "callIdentifier": call_identifier,
                "fundingShortName": funding_short_name,
                "fundingStreamId": funding_stream_id,
                "fromStartDate": from_start_date,
                "toStartDate": to_start_date,
                "fromEndDate": from_end_date,
                "toEndDate": to_end_date,
                "relOrganizationName": rel_organization_name,
                "relOrganizationId": rel_organization_id,
                "relCommunityId": rel_community_id,
                "relOrganizationCountryCode": rel_organization_country_code,
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
                    SearchResponse,
                    parse_obj_as(
                        type_=SearchResponse,
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

    def get_by_id2(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectSearchResponse]:
        """
        Get a project object by specifying its id.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectSearchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectSearchResponse,
                    parse_obj_as(
                        type_=ProjectSearchResponse,
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

    def search8(
        self,
        *,
        format: typing.Optional[Search8RequestFormat] = None,
        keywords: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        acronym: typing.Optional[str] = None,
        grant_id: typing.Optional[str] = None,
        call_id: typing.Optional[str] = None,
        funder: typing.Optional[str] = None,
        funding_stream: typing.Optional[str] = None,
        openaire_publication_id: typing.Optional[str] = None,
        participant_countries: typing.Optional[str] = None,
        participant_acronyms: typing.Optional[str] = None,
        has_ec_funding: typing.Optional[str] = None,
        has_wt_funding: typing.Optional[str] = None,
        start_year: typing.Optional[str] = None,
        end_year: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        cursor_mark: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Search and filter projects using the legacy XML API format.

        Parameters
        ----------
        format : typing.Optional[Search8RequestFormat]
            Response format

        keywords : typing.Optional[str]
            Keyword-based search

        name : typing.Optional[str]
            Search in project title/name

        acronym : typing.Optional[str]
            Filter by project acronym(s)

        grant_id : typing.Optional[str]
            Filter by grant ID / project code(s)

        call_id : typing.Optional[str]
            Filter by call identifier(s)

        funder : typing.Optional[str]
            Filter by funder shortname(s)

        funding_stream : typing.Optional[str]
            Filter by funding stream name(s)

        openaire_publication_id : typing.Optional[str]
            Filter by OpenAIRE publication ID(s)

        participant_countries : typing.Optional[str]
            Filter by participant country codes

        participant_acronyms : typing.Optional[str]
            Filter by participant organization acronyms

        has_ec_funding : typing.Optional[str]
            Filter projects with EC (European Commission) funding

        has_wt_funding : typing.Optional[str]
            Filter projects with Wellcome Trust funding

        start_year : typing.Optional[str]
            Filter by project start year

        end_year : typing.Optional[str]
            Filter by project end year

        sort_by : typing.Optional[str]
            sortBy=field,[ascending|descending] <br>
            'field' is one of: projectstartdate, projectstartyear, projectenddate, projectendyear, projectduration

        page : typing.Optional[str]
            Page number

        size : typing.Optional[str]
            Number of results per page (max 100)

        cursor_mark : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "search/projects",
            method="GET",
            params={
                "format": format,
                "keywords": keywords,
                "name": name,
                "acronym": acronym,
                "grantID": grant_id,
                "callID": call_id,
                "funder": funder,
                "fundingStream": funding_stream,
                "openairePublicationID": openaire_publication_id,
                "participantCountries": participant_countries,
                "participantAcronyms": participant_acronyms,
                "hasECFunding": has_ec_funding,
                "hasWTFunding": has_wt_funding,
                "startYear": start_year,
                "endYear": end_year,
                "sortBy": sort_by,
                "page": page,
                "size": size,
                "cursorMark": cursor_mark,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search2(
        self,
        *,
        logical_operator: typing.Optional[Search2RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        keywords: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        acronym: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        call_identifier: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        funding_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        funding_stream_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_start_date: typing.Optional[str] = None,
        to_start_date: typing.Optional[str] = None,
        from_end_date: typing.Optional[str] = None,
        to_end_date: typing.Optional[str] = None,
        rel_organization_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_organization_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_organization_country_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchResponse]:
        """
        Explore projects exploiting various filter parameters

        Parameters
        ----------
        logical_operator : typing.Optional[Search2RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        title : typing.Optional[str]
            Search in the project's title. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        keywords : typing.Optional[str]
            The project's keywords. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the project. Logical operator: *OR*

        code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The grant agreement (GA) code of the project. Logical operator: *OR*

        acronym : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Project's acronym. Logical operator: *OR*

        call_identifier : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the research call. Logical operator: *OR*

        funding_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The short name of the funder. Logical operator: *OR*

        funding_stream_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the funding stream. Logical operator: *OR*

        from_start_date : typing.Optional[str]
            Gets the projects with start date greater than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        to_start_date : typing.Optional[str]
            Gets the projects with start date less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        from_end_date : typing.Optional[str]
            Gets the projects with end date greater than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        to_end_date : typing.Optional[str]
            Gets the projects with end date less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        rel_organization_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The name or short name of the related organization. Logical operator: *OR*

        rel_organization_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The organization identifier of the related organization. Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve projects connected to the community (with OpenAIRE id). Logical operator: *OR*

        rel_organization_country_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The country code of the related organizations. Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve projects collected from the data source (with OpenAIRE id). Logical operator: *OR*

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
        AsyncHttpResponse[SearchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/projects",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "title": title,
                "keywords": keywords,
                "id": id,
                "code": code,
                "acronym": acronym,
                "callIdentifier": call_identifier,
                "fundingShortName": funding_short_name,
                "fundingStreamId": funding_stream_id,
                "fromStartDate": from_start_date,
                "toStartDate": to_start_date,
                "fromEndDate": from_end_date,
                "toEndDate": to_end_date,
                "relOrganizationName": rel_organization_name,
                "relOrganizationId": rel_organization_id,
                "relCommunityId": rel_community_id,
                "relOrganizationCountryCode": rel_organization_country_code,
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
                    SearchResponse,
                    parse_obj_as(
                        type_=SearchResponse,
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

    async def get_by_id2(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectSearchResponse]:
        """
        Get a project object by specifying its id.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectSearchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectSearchResponse,
                    parse_obj_as(
                        type_=ProjectSearchResponse,
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

    async def search8(
        self,
        *,
        format: typing.Optional[Search8RequestFormat] = None,
        keywords: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        acronym: typing.Optional[str] = None,
        grant_id: typing.Optional[str] = None,
        call_id: typing.Optional[str] = None,
        funder: typing.Optional[str] = None,
        funding_stream: typing.Optional[str] = None,
        openaire_publication_id: typing.Optional[str] = None,
        participant_countries: typing.Optional[str] = None,
        participant_acronyms: typing.Optional[str] = None,
        has_ec_funding: typing.Optional[str] = None,
        has_wt_funding: typing.Optional[str] = None,
        start_year: typing.Optional[str] = None,
        end_year: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        cursor_mark: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Search and filter projects using the legacy XML API format.

        Parameters
        ----------
        format : typing.Optional[Search8RequestFormat]
            Response format

        keywords : typing.Optional[str]
            Keyword-based search

        name : typing.Optional[str]
            Search in project title/name

        acronym : typing.Optional[str]
            Filter by project acronym(s)

        grant_id : typing.Optional[str]
            Filter by grant ID / project code(s)

        call_id : typing.Optional[str]
            Filter by call identifier(s)

        funder : typing.Optional[str]
            Filter by funder shortname(s)

        funding_stream : typing.Optional[str]
            Filter by funding stream name(s)

        openaire_publication_id : typing.Optional[str]
            Filter by OpenAIRE publication ID(s)

        participant_countries : typing.Optional[str]
            Filter by participant country codes

        participant_acronyms : typing.Optional[str]
            Filter by participant organization acronyms

        has_ec_funding : typing.Optional[str]
            Filter projects with EC (European Commission) funding

        has_wt_funding : typing.Optional[str]
            Filter projects with Wellcome Trust funding

        start_year : typing.Optional[str]
            Filter by project start year

        end_year : typing.Optional[str]
            Filter by project end year

        sort_by : typing.Optional[str]
            sortBy=field,[ascending|descending] <br>
            'field' is one of: projectstartdate, projectstartyear, projectenddate, projectendyear, projectduration

        page : typing.Optional[str]
            Page number

        size : typing.Optional[str]
            Number of results per page (max 100)

        cursor_mark : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search/projects",
            method="GET",
            params={
                "format": format,
                "keywords": keywords,
                "name": name,
                "acronym": acronym,
                "grantID": grant_id,
                "callID": call_id,
                "funder": funder,
                "fundingStream": funding_stream,
                "openairePublicationID": openaire_publication_id,
                "participantCountries": participant_countries,
                "participantAcronyms": participant_acronyms,
                "hasECFunding": has_ec_funding,
                "hasWTFunding": has_wt_funding,
                "startYear": start_year,
                "endYear": end_year,
                "sortBy": sort_by,
                "page": page,
                "size": size,
                "cursorMark": cursor_mark,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
