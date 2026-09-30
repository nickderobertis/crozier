

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
from ..types.api_result import ApiResult
from ..types.error_response import ErrorResponse
from ..types.graph_result import GraphResult
from ..types.research_products_search_response import ResearchProductsSearchResponse
from ..types.research_products_search_response_v2 import ResearchProductsSearchResponseV2
from ..types.search_response_relation import SearchResponseRelation
from .types.search1request_best_open_access_right_label_item import Search1RequestBestOpenAccessRightLabelItem
from .types.search1request_citation_count_class_item import Search1RequestCitationCountClassItem
from .types.search1request_impulse_class_item import Search1RequestImpulseClassItem
from .types.search1request_influence_class_item import Search1RequestInfluenceClassItem
from .types.search1request_logical_operator import Search1RequestLogicalOperator
from .types.search1request_open_access_color_item import Search1RequestOpenAccessColorItem
from .types.search1request_popularity_class_item import Search1RequestPopularityClassItem
from .types.search1request_type_item import Search1RequestTypeItem
from .types.search_request_best_open_access_right_label_item import SearchRequestBestOpenAccessRightLabelItem
from .types.search_request_citation_count_class_item import SearchRequestCitationCountClassItem
from .types.search_request_impulse_class_item import SearchRequestImpulseClassItem
from .types.search_request_influence_class_item import SearchRequestInfluenceClassItem
from .types.search_request_logical_operator import SearchRequestLogicalOperator
from .types.search_request_open_access_color_item import SearchRequestOpenAccessColorItem
from .types.search_request_popularity_class_item import SearchRequestPopularityClassItem
from .types.search_request_type_item import SearchRequestTypeItem
from pydantic import ValidationError


class RawResearchProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search(
        self,
        *,
        logical_operator: typing.Optional[SearchRequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        main_title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        original_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ror_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[SearchRequestTypeItem, typing.Sequence[SearchRequestTypeItem]]] = None,
        from_publication_date: typing.Optional[str] = None,
        to_publication_date: typing.Optional[str] = None,
        subjects: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        country_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author_full_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author_orcid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        best_open_access_right_label: typing.Optional[
            typing.Union[
                SearchRequestBestOpenAccessRightLabelItem, typing.Sequence[SearchRequestBestOpenAccessRightLabelItem]
            ]
        ] = None,
        influence_class: typing.Optional[
            typing.Union[SearchRequestInfluenceClassItem, typing.Sequence[SearchRequestInfluenceClassItem]]
        ] = None,
        popularity_class: typing.Optional[
            typing.Union[SearchRequestPopularityClassItem, typing.Sequence[SearchRequestPopularityClassItem]]
        ] = None,
        impulse_class: typing.Optional[
            typing.Union[SearchRequestImpulseClassItem, typing.Sequence[SearchRequestImpulseClassItem]]
        ] = None,
        citation_count_class: typing.Optional[
            typing.Union[SearchRequestCitationCountClassItem, typing.Sequence[SearchRequestCitationCountClassItem]]
        ] = None,
        instance_type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sdg: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        fos: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        is_peer_reviewed: typing.Optional[bool] = None,
        is_in_diamond_journal: typing.Optional[bool] = None,
        is_publicly_funded: typing.Optional[bool] = None,
        is_green: typing.Optional[bool] = None,
        open_access_color: typing.Optional[
            typing.Union[SearchRequestOpenAccessColorItem, typing.Sequence[SearchRequestOpenAccessColorItem]]
        ] = None,
        rel_organization_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        has_project_rel: typing.Optional[bool] = None,
        rel_project_funding_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_funding_stream_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_hosting_data_source_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResearchProductsSearchResponseV2]:
        """
        Explore research products exploiting various filter parameters

        Parameters
        ----------
        logical_operator : typing.Optional[SearchRequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        main_title : typing.Optional[str]
            Search in the research product's main title. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        description : typing.Optional[str]
            Search in the research product's description. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the research product. Logical operator: *OR*

        pid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The persistent identifier of the research product. Logical operator: *OR*

        original_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the record at the original sources. Logical operator: *OR*

        ror_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Research Organization Registry Identifier (ROR). Logical operator: *OR*

        type : typing.Optional[typing.Union[SearchRequestTypeItem, typing.Sequence[SearchRequestTypeItem]]]
            The type of the research product. Logical operator: *OR*

        from_publication_date : typing.Optional[str]
            Gets the research products whose publication date is greater than or equal to he given date. Provide a date in YYYY or YYYY-MM-DD format

        to_publication_date : typing.Optional[str]
            Gets the research products whose publication date is less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        subjects : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of subjects associated to the research product. Logical operator: *OR*

        country_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The country code for the country associated with the research product. Logical operator: *OR*

        author_full_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The full name of the authors involved in producing this research product. Logical operator: *OR*

        author_orcid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The ORCiD of the authors involved in producing this research product. Logical operator: *OR*

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. Logical operator: *OR*

        best_open_access_right_label : typing.Optional[typing.Union[SearchRequestBestOpenAccessRightLabelItem, typing.Sequence[SearchRequestBestOpenAccessRightLabelItem]]]
            The best open access rights among the research product's instances. Logical operator: *OR*

        influence_class : typing.Optional[typing.Union[SearchRequestInfluenceClassItem, typing.Sequence[SearchRequestInfluenceClassItem]]]
            Citation-based indicator that reflects the overall impact of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of influence respectively. </br> Logical operator: *OR*

        popularity_class : typing.Optional[typing.Union[SearchRequestPopularityClassItem, typing.Sequence[SearchRequestPopularityClassItem]]]
            Citation-based indicator that reflects current impact or attention of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of popularity respectively. </br> Logical operator: *OR*

        impulse_class : typing.Optional[typing.Union[SearchRequestImpulseClassItem, typing.Sequence[SearchRequestImpulseClassItem]]]
            Citation-based indicator that reflects the initial momentum of a research product directly after its publication; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and in terms of average impulse respectively. </br> Logical operator: *OR*

        citation_count_class : typing.Optional[typing.Union[SearchRequestCitationCountClassItem, typing.Sequence[SearchRequestCitationCountClassItem]]]
            Citation-based indicator that reflects the overall impact of a research product by summing all its citations; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of citation count respectively. </br> Logical operator: *OR*

        instance_type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve publications of the given instance type; check <a href='http://api.openaire.eu/vocabularies/dnet:publication_resource' target='_blank'>here</a> for all possible instance type values `[Only for publications]`. </br> Logical operator: *OR*

        sdg : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Retrieves publications classified with the respective Sustainable Development Goal number (for further information check <a href='https://sdgs.un.org/goals' target='_blank'>here</a>); please provide an SDG number between 1 and 17 `[Only for publications]`. </br> Logical operator: *OR*

        fos : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieves publications classified with a given Field of Science (FOS); please provide a valid <a href='https://explore.openaire.eu/assets/common-assets/vocabulary/fos.json' target='_blank'>FOS classification identifier</a>  `[Only for publications]`. </br> Logical operator: *OR*

        is_peer_reviewed : typing.Optional[bool]
            Indicates whether the publications are peerReviewed or not `[Only for publications]`

        is_in_diamond_journal : typing.Optional[bool]
            Indicates whether the publication was published in a diamond journal or not `[Only for publications]`

        is_publicly_funded : typing.Optional[bool]
            Indicates whether the publication was publicly funded or not `[Only for publications]`

        is_green : typing.Optional[bool]
            Indicates whether the publication was published following the green open access model `[Only for publications]`

        open_access_color : typing.Optional[typing.Union[SearchRequestOpenAccessColorItem, typing.Sequence[SearchRequestOpenAccessColorItem]]]
            Specifies the Open Access color of the publication `[Only for publications]`. </br> Logical operator: *OR*

        rel_organization_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the organization (with OpenAIRE id). </br> Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the community (with OpenAIRE id). </br> Logical operator: *OR*

        rel_project_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the project (with OpenAIRE id). </br> Logical operator: *OR*

        rel_project_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the project with code. </br> Logical operator: *OR*

        has_project_rel : typing.Optional[bool]
            Retrieve research products that are connected to a project

        rel_project_funding_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to a project that has a funder with the given short name. </br> Logical operator: *OR*

        rel_project_funding_stream_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to a project that has the given funding identifier. </br> Logical operator: *OR*

        rel_hosting_data_source_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products hosted by the data source (with OpenAIRE id). </br> Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products collected from the data source (with OpenAIRE id). </br> Logical operator: *OR*

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
            The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'publicationDate', 'dateOfCollection', 'influence', 'popularity', 'citationCount', 'impulse'. Multiple sorting parameters should be comma-separated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResearchProductsSearchResponseV2]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/researchProducts",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "mainTitle": main_title,
                "description": description,
                "id": id,
                "pid": pid,
                "originalId": original_id,
                "rorId": ror_id,
                "type": type,
                "fromPublicationDate": from_publication_date,
                "toPublicationDate": to_publication_date,
                "subjects": subjects,
                "countryCode": country_code,
                "authorFullName": author_full_name,
                "authorOrcid": author_orcid,
                "publisher": publisher,
                "bestOpenAccessRightLabel": best_open_access_right_label,
                "influenceClass": influence_class,
                "popularityClass": popularity_class,
                "impulseClass": impulse_class,
                "citationCountClass": citation_count_class,
                "instanceType": instance_type,
                "sdg": sdg,
                "fos": fos,
                "isPeerReviewed": is_peer_reviewed,
                "isInDiamondJournal": is_in_diamond_journal,
                "isPubliclyFunded": is_publicly_funded,
                "isGreen": is_green,
                "openAccessColor": open_access_color,
                "relOrganizationId": rel_organization_id,
                "relCommunityId": rel_community_id,
                "relProjectId": rel_project_id,
                "relProjectCode": rel_project_code,
                "hasProjectRel": has_project_rel,
                "relProjectFundingShortName": rel_project_funding_short_name,
                "relProjectFundingStreamId": rel_project_funding_stream_id,
                "relHostingDataSourceId": rel_hosting_data_source_id,
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
                    ResearchProductsSearchResponseV2,
                    parse_obj_as(
                        type_=ResearchProductsSearchResponseV2,
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

    def get_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ApiResult]:
        """
        Get a research product object by specifying its id.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the research product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResult]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/researchProducts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResult,
                    parse_obj_as(
                        type_=ApiResult,
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

    def search1(
        self,
        *,
        logical_operator: typing.Optional[Search1RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        main_title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        original_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ror_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[Search1RequestTypeItem, typing.Sequence[Search1RequestTypeItem]]] = None,
        from_publication_date: typing.Optional[str] = None,
        to_publication_date: typing.Optional[str] = None,
        subjects: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        country_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author_full_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author_orcid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        best_open_access_right_label: typing.Optional[
            typing.Union[
                Search1RequestBestOpenAccessRightLabelItem, typing.Sequence[Search1RequestBestOpenAccessRightLabelItem]
            ]
        ] = None,
        influence_class: typing.Optional[
            typing.Union[Search1RequestInfluenceClassItem, typing.Sequence[Search1RequestInfluenceClassItem]]
        ] = None,
        popularity_class: typing.Optional[
            typing.Union[Search1RequestPopularityClassItem, typing.Sequence[Search1RequestPopularityClassItem]]
        ] = None,
        impulse_class: typing.Optional[
            typing.Union[Search1RequestImpulseClassItem, typing.Sequence[Search1RequestImpulseClassItem]]
        ] = None,
        citation_count_class: typing.Optional[
            typing.Union[Search1RequestCitationCountClassItem, typing.Sequence[Search1RequestCitationCountClassItem]]
        ] = None,
        instance_type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sdg: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        fos: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        is_peer_reviewed: typing.Optional[bool] = None,
        is_in_diamond_journal: typing.Optional[bool] = None,
        is_publicly_funded: typing.Optional[bool] = None,
        is_green: typing.Optional[bool] = None,
        open_access_color: typing.Optional[
            typing.Union[Search1RequestOpenAccessColorItem, typing.Sequence[Search1RequestOpenAccessColorItem]]
        ] = None,
        rel_organization_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        has_project_rel: typing.Optional[bool] = None,
        rel_project_funding_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_funding_stream_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_hosting_data_source_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResearchProductsSearchResponse]:
        """
        Deprecated: Use <a href="https://api.openaire.eu/graph/swagger-ui/index.html?urls.primaryName=OpenAIRE%20Graph%20API%20V2">version 2.0</a> instead.
        This version is no longer supported and will be removed in the future.

        Parameters
        ----------
        logical_operator : typing.Optional[Search1RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        main_title : typing.Optional[str]
            Search in the research product's main title. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        description : typing.Optional[str]
            Search in the research product's description. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the research product. Logical operator: *OR*

        pid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The persistent identifier of the research product. Logical operator: *OR*

        original_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the record at the original sources. Logical operator: *OR*

        ror_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Research Organization Registry Identifier (ROR). Logical operator: *OR*

        type : typing.Optional[typing.Union[Search1RequestTypeItem, typing.Sequence[Search1RequestTypeItem]]]
            The type of the research product. Logical operator: *OR*

        from_publication_date : typing.Optional[str]
            Gets the research products whose publication date is greater than or equal to he given date. Provide a date in YYYY or YYYY-MM-DD format

        to_publication_date : typing.Optional[str]
            Gets the research products whose publication date is less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        subjects : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of subjects associated to the research product. Logical operator: *OR*

        country_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The country code for the country associated with the research product. Logical operator: *OR*

        author_full_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The full name of the authors involved in producing this research product. Logical operator: *OR*

        author_orcid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The ORCiD of the authors involved in producing this research product. Logical operator: *OR*

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. Logical operator: *OR*

        best_open_access_right_label : typing.Optional[typing.Union[Search1RequestBestOpenAccessRightLabelItem, typing.Sequence[Search1RequestBestOpenAccessRightLabelItem]]]
            The best open access rights among the research product's instances. Logical operator: *OR*

        influence_class : typing.Optional[typing.Union[Search1RequestInfluenceClassItem, typing.Sequence[Search1RequestInfluenceClassItem]]]
            Citation-based indicator that reflects the overall impact of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of influence respectively. </br> Logical operator: *OR*

        popularity_class : typing.Optional[typing.Union[Search1RequestPopularityClassItem, typing.Sequence[Search1RequestPopularityClassItem]]]
            Citation-based indicator that reflects current impact or attention of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of popularity respectively. </br> Logical operator: *OR*

        impulse_class : typing.Optional[typing.Union[Search1RequestImpulseClassItem, typing.Sequence[Search1RequestImpulseClassItem]]]
            Citation-based indicator that reflects the initial momentum of a research product directly after its publication; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and in terms of average impulse respectively. </br> Logical operator: *OR*

        citation_count_class : typing.Optional[typing.Union[Search1RequestCitationCountClassItem, typing.Sequence[Search1RequestCitationCountClassItem]]]
            Citation-based indicator that reflects the overall impact of a research product by summing all its citations; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of citation count respectively. </br> Logical operator: *OR*

        instance_type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve publications of the given instance type; check <a href='http://api.openaire.eu/vocabularies/dnet:publication_resource' target='_blank'>here</a> for all possible instance type values `[Only for publications]`. </br> Logical operator: *OR*

        sdg : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Retrieves publications classified with the respective Sustainable Development Goal number (for further information check <a href='https://sdgs.un.org/goals' target='_blank'>here</a>); please provide an SDG number between 1 and 17 `[Only for publications]`. </br> Logical operator: *OR*

        fos : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieves publications classified with a given Field of Science (FOS); please provide a valid <a href='https://explore.openaire.eu/assets/common-assets/vocabulary/fos.json' target='_blank'>FOS classification identifier</a>  `[Only for publications]`. </br> Logical operator: *OR*

        is_peer_reviewed : typing.Optional[bool]
            Indicates whether the publications are peerReviewed or not `[Only for publications]`

        is_in_diamond_journal : typing.Optional[bool]
            Indicates whether the publication was published in a diamond journal or not `[Only for publications]`

        is_publicly_funded : typing.Optional[bool]
            Indicates whether the publication was publicly funded or not `[Only for publications]`

        is_green : typing.Optional[bool]
            Indicates whether the publication was published following the green open access model `[Only for publications]`

        open_access_color : typing.Optional[typing.Union[Search1RequestOpenAccessColorItem, typing.Sequence[Search1RequestOpenAccessColorItem]]]
            Specifies the Open Access color of the publication `[Only for publications]`. </br> Logical operator: *OR*

        rel_organization_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the organization (with OpenAIRE id). </br> Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the community (with OpenAIRE id). </br> Logical operator: *OR*

        rel_project_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the project (with OpenAIRE id). </br> Logical operator: *OR*

        rel_project_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the project with code. </br> Logical operator: *OR*

        has_project_rel : typing.Optional[bool]
            Retrieve research products that are connected to a project

        rel_project_funding_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to a project that has a funder with the given short name. </br> Logical operator: *OR*

        rel_project_funding_stream_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to a project that has the given funding identifier. </br> Logical operator: *OR*

        rel_hosting_data_source_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products hosted by the data source (with OpenAIRE id). </br> Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products collected from the data source (with OpenAIRE id). </br> Logical operator: *OR*

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
            The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'publicationDate', 'dateOfCollection', 'influence', 'popularity', 'citationCount', 'impulse'. Multiple sorting parameters should be comma-separated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResearchProductsSearchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/researchProducts",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "mainTitle": main_title,
                "description": description,
                "id": id,
                "pid": pid,
                "originalId": original_id,
                "rorId": ror_id,
                "type": type,
                "fromPublicationDate": from_publication_date,
                "toPublicationDate": to_publication_date,
                "subjects": subjects,
                "countryCode": country_code,
                "authorFullName": author_full_name,
                "authorOrcid": author_orcid,
                "publisher": publisher,
                "bestOpenAccessRightLabel": best_open_access_right_label,
                "influenceClass": influence_class,
                "popularityClass": popularity_class,
                "impulseClass": impulse_class,
                "citationCountClass": citation_count_class,
                "instanceType": instance_type,
                "sdg": sdg,
                "fos": fos,
                "isPeerReviewed": is_peer_reviewed,
                "isInDiamondJournal": is_in_diamond_journal,
                "isPubliclyFunded": is_publicly_funded,
                "isGreen": is_green,
                "openAccessColor": open_access_color,
                "relOrganizationId": rel_organization_id,
                "relCommunityId": rel_community_id,
                "relProjectId": rel_project_id,
                "relProjectCode": rel_project_code,
                "hasProjectRel": has_project_rel,
                "relProjectFundingShortName": rel_project_funding_short_name,
                "relProjectFundingStreamId": rel_project_funding_stream_id,
                "relHostingDataSourceId": rel_hosting_data_source_id,
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
                    ResearchProductsSearchResponse,
                    parse_obj_as(
                        type_=ResearchProductsSearchResponse,
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

    def get_by_id1(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GraphResult]:
        """
        Deprecated: Use <a href="https://api.openaire.eu/graph/swagger-ui/index.html?urls.primaryName=OpenAIRE%20Graph%20API%20V2">version 2.0</a> instead.
        This version is no longer supported and will be removed in the future.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the research product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GraphResult]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/researchProducts/{encode_path_param(id)}",
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

    def get_links(
        self,
        *,
        target_pid: typing.Optional[str] = None,
        target_publisher: typing.Optional[str] = None,
        target_type: typing.Optional[str] = None,
        source_pid: typing.Optional[str] = None,
        source_publisher: typing.Optional[str] = None,
        source_type: typing.Optional[str] = None,
        relation: typing.Optional[str] = None,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchResponseRelation]:
        """
        Retrieve scholix links

        Parameters
        ----------
        target_pid : typing.Optional[str]
            Filter relationships by target pid

        target_publisher : typing.Optional[str]
            Filter relationships by target publisher

        target_type : typing.Optional[str]
            Filter relationships by target type (publication, dataset, software, other)

        source_pid : typing.Optional[str]
            Filter relationships by source pid

        source_publisher : typing.Optional[str]
            Filter relationships by source publisher

        source_type : typing.Optional[str]
            Filter relationships by source type (publication, dataset, software, other)

        relation : typing.Optional[str]
            Filter by specific relationships

        from_date : typing.Optional[str]
            Provide From date in YYYY or YYYY-MM-DD format

        to_date : typing.Optional[str]
            Provide To date in YYYY or YYYY-MM-DD format

        page : typing.Optional[int]
            Page number of the results

        page_size : typing.Optional[int]
            Page size - maximum value: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchResponseRelation]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/researchProducts/links",
            method="GET",
            params={
                "targetPid": target_pid,
                "targetPublisher": target_publisher,
                "targetType": target_type,
                "sourcePid": source_pid,
                "sourcePublisher": source_publisher,
                "sourceType": source_type,
                "relation": relation,
                "fromDate": from_date,
                "toDate": to_date,
                "page": page,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResponseRelation,
                    parse_obj_as(
                        type_=SearchResponseRelation,
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

    def get_relations_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Retrieve information about available relation types from scholexplorer

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/researchProducts/links/relations-info",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawResearchProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search(
        self,
        *,
        logical_operator: typing.Optional[SearchRequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        main_title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        original_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ror_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[SearchRequestTypeItem, typing.Sequence[SearchRequestTypeItem]]] = None,
        from_publication_date: typing.Optional[str] = None,
        to_publication_date: typing.Optional[str] = None,
        subjects: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        country_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author_full_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author_orcid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        best_open_access_right_label: typing.Optional[
            typing.Union[
                SearchRequestBestOpenAccessRightLabelItem, typing.Sequence[SearchRequestBestOpenAccessRightLabelItem]
            ]
        ] = None,
        influence_class: typing.Optional[
            typing.Union[SearchRequestInfluenceClassItem, typing.Sequence[SearchRequestInfluenceClassItem]]
        ] = None,
        popularity_class: typing.Optional[
            typing.Union[SearchRequestPopularityClassItem, typing.Sequence[SearchRequestPopularityClassItem]]
        ] = None,
        impulse_class: typing.Optional[
            typing.Union[SearchRequestImpulseClassItem, typing.Sequence[SearchRequestImpulseClassItem]]
        ] = None,
        citation_count_class: typing.Optional[
            typing.Union[SearchRequestCitationCountClassItem, typing.Sequence[SearchRequestCitationCountClassItem]]
        ] = None,
        instance_type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sdg: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        fos: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        is_peer_reviewed: typing.Optional[bool] = None,
        is_in_diamond_journal: typing.Optional[bool] = None,
        is_publicly_funded: typing.Optional[bool] = None,
        is_green: typing.Optional[bool] = None,
        open_access_color: typing.Optional[
            typing.Union[SearchRequestOpenAccessColorItem, typing.Sequence[SearchRequestOpenAccessColorItem]]
        ] = None,
        rel_organization_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        has_project_rel: typing.Optional[bool] = None,
        rel_project_funding_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_funding_stream_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_hosting_data_source_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResearchProductsSearchResponseV2]:
        """
        Explore research products exploiting various filter parameters

        Parameters
        ----------
        logical_operator : typing.Optional[SearchRequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        main_title : typing.Optional[str]
            Search in the research product's main title. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        description : typing.Optional[str]
            Search in the research product's description. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the research product. Logical operator: *OR*

        pid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The persistent identifier of the research product. Logical operator: *OR*

        original_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the record at the original sources. Logical operator: *OR*

        ror_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Research Organization Registry Identifier (ROR). Logical operator: *OR*

        type : typing.Optional[typing.Union[SearchRequestTypeItem, typing.Sequence[SearchRequestTypeItem]]]
            The type of the research product. Logical operator: *OR*

        from_publication_date : typing.Optional[str]
            Gets the research products whose publication date is greater than or equal to he given date. Provide a date in YYYY or YYYY-MM-DD format

        to_publication_date : typing.Optional[str]
            Gets the research products whose publication date is less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        subjects : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of subjects associated to the research product. Logical operator: *OR*

        country_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The country code for the country associated with the research product. Logical operator: *OR*

        author_full_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The full name of the authors involved in producing this research product. Logical operator: *OR*

        author_orcid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The ORCiD of the authors involved in producing this research product. Logical operator: *OR*

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. Logical operator: *OR*

        best_open_access_right_label : typing.Optional[typing.Union[SearchRequestBestOpenAccessRightLabelItem, typing.Sequence[SearchRequestBestOpenAccessRightLabelItem]]]
            The best open access rights among the research product's instances. Logical operator: *OR*

        influence_class : typing.Optional[typing.Union[SearchRequestInfluenceClassItem, typing.Sequence[SearchRequestInfluenceClassItem]]]
            Citation-based indicator that reflects the overall impact of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of influence respectively. </br> Logical operator: *OR*

        popularity_class : typing.Optional[typing.Union[SearchRequestPopularityClassItem, typing.Sequence[SearchRequestPopularityClassItem]]]
            Citation-based indicator that reflects current impact or attention of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of popularity respectively. </br> Logical operator: *OR*

        impulse_class : typing.Optional[typing.Union[SearchRequestImpulseClassItem, typing.Sequence[SearchRequestImpulseClassItem]]]
            Citation-based indicator that reflects the initial momentum of a research product directly after its publication; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and in terms of average impulse respectively. </br> Logical operator: *OR*

        citation_count_class : typing.Optional[typing.Union[SearchRequestCitationCountClassItem, typing.Sequence[SearchRequestCitationCountClassItem]]]
            Citation-based indicator that reflects the overall impact of a research product by summing all its citations; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of citation count respectively. </br> Logical operator: *OR*

        instance_type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve publications of the given instance type; check <a href='http://api.openaire.eu/vocabularies/dnet:publication_resource' target='_blank'>here</a> for all possible instance type values `[Only for publications]`. </br> Logical operator: *OR*

        sdg : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Retrieves publications classified with the respective Sustainable Development Goal number (for further information check <a href='https://sdgs.un.org/goals' target='_blank'>here</a>); please provide an SDG number between 1 and 17 `[Only for publications]`. </br> Logical operator: *OR*

        fos : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieves publications classified with a given Field of Science (FOS); please provide a valid <a href='https://explore.openaire.eu/assets/common-assets/vocabulary/fos.json' target='_blank'>FOS classification identifier</a>  `[Only for publications]`. </br> Logical operator: *OR*

        is_peer_reviewed : typing.Optional[bool]
            Indicates whether the publications are peerReviewed or not `[Only for publications]`

        is_in_diamond_journal : typing.Optional[bool]
            Indicates whether the publication was published in a diamond journal or not `[Only for publications]`

        is_publicly_funded : typing.Optional[bool]
            Indicates whether the publication was publicly funded or not `[Only for publications]`

        is_green : typing.Optional[bool]
            Indicates whether the publication was published following the green open access model `[Only for publications]`

        open_access_color : typing.Optional[typing.Union[SearchRequestOpenAccessColorItem, typing.Sequence[SearchRequestOpenAccessColorItem]]]
            Specifies the Open Access color of the publication `[Only for publications]`. </br> Logical operator: *OR*

        rel_organization_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the organization (with OpenAIRE id). </br> Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the community (with OpenAIRE id). </br> Logical operator: *OR*

        rel_project_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the project (with OpenAIRE id). </br> Logical operator: *OR*

        rel_project_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the project with code. </br> Logical operator: *OR*

        has_project_rel : typing.Optional[bool]
            Retrieve research products that are connected to a project

        rel_project_funding_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to a project that has a funder with the given short name. </br> Logical operator: *OR*

        rel_project_funding_stream_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to a project that has the given funding identifier. </br> Logical operator: *OR*

        rel_hosting_data_source_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products hosted by the data source (with OpenAIRE id). </br> Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products collected from the data source (with OpenAIRE id). </br> Logical operator: *OR*

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
            The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'publicationDate', 'dateOfCollection', 'influence', 'popularity', 'citationCount', 'impulse'. Multiple sorting parameters should be comma-separated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResearchProductsSearchResponseV2]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/researchProducts",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "mainTitle": main_title,
                "description": description,
                "id": id,
                "pid": pid,
                "originalId": original_id,
                "rorId": ror_id,
                "type": type,
                "fromPublicationDate": from_publication_date,
                "toPublicationDate": to_publication_date,
                "subjects": subjects,
                "countryCode": country_code,
                "authorFullName": author_full_name,
                "authorOrcid": author_orcid,
                "publisher": publisher,
                "bestOpenAccessRightLabel": best_open_access_right_label,
                "influenceClass": influence_class,
                "popularityClass": popularity_class,
                "impulseClass": impulse_class,
                "citationCountClass": citation_count_class,
                "instanceType": instance_type,
                "sdg": sdg,
                "fos": fos,
                "isPeerReviewed": is_peer_reviewed,
                "isInDiamondJournal": is_in_diamond_journal,
                "isPubliclyFunded": is_publicly_funded,
                "isGreen": is_green,
                "openAccessColor": open_access_color,
                "relOrganizationId": rel_organization_id,
                "relCommunityId": rel_community_id,
                "relProjectId": rel_project_id,
                "relProjectCode": rel_project_code,
                "hasProjectRel": has_project_rel,
                "relProjectFundingShortName": rel_project_funding_short_name,
                "relProjectFundingStreamId": rel_project_funding_stream_id,
                "relHostingDataSourceId": rel_hosting_data_source_id,
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
                    ResearchProductsSearchResponseV2,
                    parse_obj_as(
                        type_=ResearchProductsSearchResponseV2,
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

    async def get_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiResult]:
        """
        Get a research product object by specifying its id.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the research product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResult]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/researchProducts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResult,
                    parse_obj_as(
                        type_=ApiResult,
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

    async def search1(
        self,
        *,
        logical_operator: typing.Optional[Search1RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        main_title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        original_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ror_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[Search1RequestTypeItem, typing.Sequence[Search1RequestTypeItem]]] = None,
        from_publication_date: typing.Optional[str] = None,
        to_publication_date: typing.Optional[str] = None,
        subjects: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        country_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author_full_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author_orcid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        best_open_access_right_label: typing.Optional[
            typing.Union[
                Search1RequestBestOpenAccessRightLabelItem, typing.Sequence[Search1RequestBestOpenAccessRightLabelItem]
            ]
        ] = None,
        influence_class: typing.Optional[
            typing.Union[Search1RequestInfluenceClassItem, typing.Sequence[Search1RequestInfluenceClassItem]]
        ] = None,
        popularity_class: typing.Optional[
            typing.Union[Search1RequestPopularityClassItem, typing.Sequence[Search1RequestPopularityClassItem]]
        ] = None,
        impulse_class: typing.Optional[
            typing.Union[Search1RequestImpulseClassItem, typing.Sequence[Search1RequestImpulseClassItem]]
        ] = None,
        citation_count_class: typing.Optional[
            typing.Union[Search1RequestCitationCountClassItem, typing.Sequence[Search1RequestCitationCountClassItem]]
        ] = None,
        instance_type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sdg: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        fos: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        is_peer_reviewed: typing.Optional[bool] = None,
        is_in_diamond_journal: typing.Optional[bool] = None,
        is_publicly_funded: typing.Optional[bool] = None,
        is_green: typing.Optional[bool] = None,
        open_access_color: typing.Optional[
            typing.Union[Search1RequestOpenAccessColorItem, typing.Sequence[Search1RequestOpenAccessColorItem]]
        ] = None,
        rel_organization_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        has_project_rel: typing.Optional[bool] = None,
        rel_project_funding_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_project_funding_stream_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_hosting_data_source_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResearchProductsSearchResponse]:
        """
        Deprecated: Use <a href="https://api.openaire.eu/graph/swagger-ui/index.html?urls.primaryName=OpenAIRE%20Graph%20API%20V2">version 2.0</a> instead.
        This version is no longer supported and will be removed in the future.

        Parameters
        ----------
        logical_operator : typing.Optional[Search1RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        main_title : typing.Optional[str]
            Search in the research product's main title. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        description : typing.Optional[str]
            Search in the research product's description. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the research product. Logical operator: *OR*

        pid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The persistent identifier of the research product. Logical operator: *OR*

        original_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The identifier of the record at the original sources. Logical operator: *OR*

        ror_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Research Organization Registry Identifier (ROR). Logical operator: *OR*

        type : typing.Optional[typing.Union[Search1RequestTypeItem, typing.Sequence[Search1RequestTypeItem]]]
            The type of the research product. Logical operator: *OR*

        from_publication_date : typing.Optional[str]
            Gets the research products whose publication date is greater than or equal to he given date. Provide a date in YYYY or YYYY-MM-DD format

        to_publication_date : typing.Optional[str]
            Gets the research products whose publication date is less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format

        subjects : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of subjects associated to the research product. Logical operator: *OR*

        country_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The country code for the country associated with the research product. Logical operator: *OR*

        author_full_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The full name of the authors involved in producing this research product. Logical operator: *OR*

        author_orcid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The ORCiD of the authors involved in producing this research product. Logical operator: *OR*

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. Logical operator: *OR*

        best_open_access_right_label : typing.Optional[typing.Union[Search1RequestBestOpenAccessRightLabelItem, typing.Sequence[Search1RequestBestOpenAccessRightLabelItem]]]
            The best open access rights among the research product's instances. Logical operator: *OR*

        influence_class : typing.Optional[typing.Union[Search1RequestInfluenceClassItem, typing.Sequence[Search1RequestInfluenceClassItem]]]
            Citation-based indicator that reflects the overall impact of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of influence respectively. </br> Logical operator: *OR*

        popularity_class : typing.Optional[typing.Union[Search1RequestPopularityClassItem, typing.Sequence[Search1RequestPopularityClassItem]]]
            Citation-based indicator that reflects current impact or attention of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of popularity respectively. </br> Logical operator: *OR*

        impulse_class : typing.Optional[typing.Union[Search1RequestImpulseClassItem, typing.Sequence[Search1RequestImpulseClassItem]]]
            Citation-based indicator that reflects the initial momentum of a research product directly after its publication; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and in terms of average impulse respectively. </br> Logical operator: *OR*

        citation_count_class : typing.Optional[typing.Union[Search1RequestCitationCountClassItem, typing.Sequence[Search1RequestCitationCountClassItem]]]
            Citation-based indicator that reflects the overall impact of a research product by summing all its citations; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of citation count respectively. </br> Logical operator: *OR*

        instance_type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve publications of the given instance type; check <a href='http://api.openaire.eu/vocabularies/dnet:publication_resource' target='_blank'>here</a> for all possible instance type values `[Only for publications]`. </br> Logical operator: *OR*

        sdg : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Retrieves publications classified with the respective Sustainable Development Goal number (for further information check <a href='https://sdgs.un.org/goals' target='_blank'>here</a>); please provide an SDG number between 1 and 17 `[Only for publications]`. </br> Logical operator: *OR*

        fos : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieves publications classified with a given Field of Science (FOS); please provide a valid <a href='https://explore.openaire.eu/assets/common-assets/vocabulary/fos.json' target='_blank'>FOS classification identifier</a>  `[Only for publications]`. </br> Logical operator: *OR*

        is_peer_reviewed : typing.Optional[bool]
            Indicates whether the publications are peerReviewed or not `[Only for publications]`

        is_in_diamond_journal : typing.Optional[bool]
            Indicates whether the publication was published in a diamond journal or not `[Only for publications]`

        is_publicly_funded : typing.Optional[bool]
            Indicates whether the publication was publicly funded or not `[Only for publications]`

        is_green : typing.Optional[bool]
            Indicates whether the publication was published following the green open access model `[Only for publications]`

        open_access_color : typing.Optional[typing.Union[Search1RequestOpenAccessColorItem, typing.Sequence[Search1RequestOpenAccessColorItem]]]
            Specifies the Open Access color of the publication `[Only for publications]`. </br> Logical operator: *OR*

        rel_organization_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the organization (with OpenAIRE id). </br> Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the community (with OpenAIRE id). </br> Logical operator: *OR*

        rel_project_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the project (with OpenAIRE id). </br> Logical operator: *OR*

        rel_project_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to the project with code. </br> Logical operator: *OR*

        has_project_rel : typing.Optional[bool]
            Retrieve research products that are connected to a project

        rel_project_funding_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to a project that has a funder with the given short name. </br> Logical operator: *OR*

        rel_project_funding_stream_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products connected to a project that has the given funding identifier. </br> Logical operator: *OR*

        rel_hosting_data_source_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products hosted by the data source (with OpenAIRE id). </br> Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve research products collected from the data source (with OpenAIRE id). </br> Logical operator: *OR*

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
            The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'publicationDate', 'dateOfCollection', 'influence', 'popularity', 'citationCount', 'impulse'. Multiple sorting parameters should be comma-separated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResearchProductsSearchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/researchProducts",
            method="GET",
            params={
                "logicalOperator": logical_operator,
                "search": search,
                "mainTitle": main_title,
                "description": description,
                "id": id,
                "pid": pid,
                "originalId": original_id,
                "rorId": ror_id,
                "type": type,
                "fromPublicationDate": from_publication_date,
                "toPublicationDate": to_publication_date,
                "subjects": subjects,
                "countryCode": country_code,
                "authorFullName": author_full_name,
                "authorOrcid": author_orcid,
                "publisher": publisher,
                "bestOpenAccessRightLabel": best_open_access_right_label,
                "influenceClass": influence_class,
                "popularityClass": popularity_class,
                "impulseClass": impulse_class,
                "citationCountClass": citation_count_class,
                "instanceType": instance_type,
                "sdg": sdg,
                "fos": fos,
                "isPeerReviewed": is_peer_reviewed,
                "isInDiamondJournal": is_in_diamond_journal,
                "isPubliclyFunded": is_publicly_funded,
                "isGreen": is_green,
                "openAccessColor": open_access_color,
                "relOrganizationId": rel_organization_id,
                "relCommunityId": rel_community_id,
                "relProjectId": rel_project_id,
                "relProjectCode": rel_project_code,
                "hasProjectRel": has_project_rel,
                "relProjectFundingShortName": rel_project_funding_short_name,
                "relProjectFundingStreamId": rel_project_funding_stream_id,
                "relHostingDataSourceId": rel_hosting_data_source_id,
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
                    ResearchProductsSearchResponse,
                    parse_obj_as(
                        type_=ResearchProductsSearchResponse,
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

    async def get_by_id1(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GraphResult]:
        """
        Deprecated: Use <a href="https://api.openaire.eu/graph/swagger-ui/index.html?urls.primaryName=OpenAIRE%20Graph%20API%20V2">version 2.0</a> instead.
        This version is no longer supported and will be removed in the future.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the research product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GraphResult]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/researchProducts/{encode_path_param(id)}",
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

    async def get_links(
        self,
        *,
        target_pid: typing.Optional[str] = None,
        target_publisher: typing.Optional[str] = None,
        target_type: typing.Optional[str] = None,
        source_pid: typing.Optional[str] = None,
        source_publisher: typing.Optional[str] = None,
        source_type: typing.Optional[str] = None,
        relation: typing.Optional[str] = None,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchResponseRelation]:
        """
        Retrieve scholix links

        Parameters
        ----------
        target_pid : typing.Optional[str]
            Filter relationships by target pid

        target_publisher : typing.Optional[str]
            Filter relationships by target publisher

        target_type : typing.Optional[str]
            Filter relationships by target type (publication, dataset, software, other)

        source_pid : typing.Optional[str]
            Filter relationships by source pid

        source_publisher : typing.Optional[str]
            Filter relationships by source publisher

        source_type : typing.Optional[str]
            Filter relationships by source type (publication, dataset, software, other)

        relation : typing.Optional[str]
            Filter by specific relationships

        from_date : typing.Optional[str]
            Provide From date in YYYY or YYYY-MM-DD format

        to_date : typing.Optional[str]
            Provide To date in YYYY or YYYY-MM-DD format

        page : typing.Optional[int]
            Page number of the results

        page_size : typing.Optional[int]
            Page size - maximum value: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchResponseRelation]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/researchProducts/links",
            method="GET",
            params={
                "targetPid": target_pid,
                "targetPublisher": target_publisher,
                "targetType": target_type,
                "sourcePid": source_pid,
                "sourcePublisher": source_publisher,
                "sourceType": source_type,
                "relation": relation,
                "fromDate": from_date,
                "toDate": to_date,
                "page": page,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResponseRelation,
                    parse_obj_as(
                        type_=SearchResponseRelation,
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

    async def get_relations_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Retrieve information about available relation types from scholexplorer

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/researchProducts/links/relations-info",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
