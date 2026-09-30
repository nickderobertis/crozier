

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_result import ApiResult
from ..types.graph_result import GraphResult
from ..types.research_products_search_response import ResearchProductsSearchResponse
from ..types.research_products_search_response_v2 import ResearchProductsSearchResponseV2
from ..types.search_response_relation import SearchResponseRelation
from .raw_client import AsyncRawResearchProductsClient, RawResearchProductsClient
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


class ResearchProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawResearchProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawResearchProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawResearchProductsClient
        """
        return self._raw_client

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
    ) -> ResearchProductsSearchResponseV2:
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
        ResearchProductsSearchResponseV2
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.research_products.search()
        """
        _response = self._raw_client.search(
            logical_operator=logical_operator,
            search=search,
            main_title=main_title,
            description=description,
            id=id,
            pid=pid,
            original_id=original_id,
            ror_id=ror_id,
            type=type,
            from_publication_date=from_publication_date,
            to_publication_date=to_publication_date,
            subjects=subjects,
            country_code=country_code,
            author_full_name=author_full_name,
            author_orcid=author_orcid,
            publisher=publisher,
            best_open_access_right_label=best_open_access_right_label,
            influence_class=influence_class,
            popularity_class=popularity_class,
            impulse_class=impulse_class,
            citation_count_class=citation_count_class,
            instance_type=instance_type,
            sdg=sdg,
            fos=fos,
            is_peer_reviewed=is_peer_reviewed,
            is_in_diamond_journal=is_in_diamond_journal,
            is_publicly_funded=is_publicly_funded,
            is_green=is_green,
            open_access_color=open_access_color,
            rel_organization_id=rel_organization_id,
            rel_community_id=rel_community_id,
            rel_project_id=rel_project_id,
            rel_project_code=rel_project_code,
            has_project_rel=has_project_rel,
            rel_project_funding_short_name=rel_project_funding_short_name,
            rel_project_funding_stream_id=rel_project_funding_stream_id,
            rel_hosting_data_source_id=rel_hosting_data_source_id,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    def get_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResult:
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
        ApiResult
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.research_products.get_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_by_id(id, request_options=request_options)
        return _response.data

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
    ) -> ResearchProductsSearchResponse:
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
        ResearchProductsSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.research_products.search1()
        """
        _response = self._raw_client.search1(
            logical_operator=logical_operator,
            search=search,
            main_title=main_title,
            description=description,
            id=id,
            pid=pid,
            original_id=original_id,
            ror_id=ror_id,
            type=type,
            from_publication_date=from_publication_date,
            to_publication_date=to_publication_date,
            subjects=subjects,
            country_code=country_code,
            author_full_name=author_full_name,
            author_orcid=author_orcid,
            publisher=publisher,
            best_open_access_right_label=best_open_access_right_label,
            influence_class=influence_class,
            popularity_class=popularity_class,
            impulse_class=impulse_class,
            citation_count_class=citation_count_class,
            instance_type=instance_type,
            sdg=sdg,
            fos=fos,
            is_peer_reviewed=is_peer_reviewed,
            is_in_diamond_journal=is_in_diamond_journal,
            is_publicly_funded=is_publicly_funded,
            is_green=is_green,
            open_access_color=open_access_color,
            rel_organization_id=rel_organization_id,
            rel_community_id=rel_community_id,
            rel_project_id=rel_project_id,
            rel_project_code=rel_project_code,
            has_project_rel=has_project_rel,
            rel_project_funding_short_name=rel_project_funding_short_name,
            rel_project_funding_stream_id=rel_project_funding_stream_id,
            rel_hosting_data_source_id=rel_hosting_data_source_id,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    def get_by_id1(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GraphResult:
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
        GraphResult
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.research_products.get_by_id1(
            id="id",
        )
        """
        _response = self._raw_client.get_by_id1(id, request_options=request_options)
        return _response.data

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
    ) -> SearchResponseRelation:
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
        SearchResponseRelation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.research_products.get_links()
        """
        _response = self._raw_client.get_links(
            target_pid=target_pid,
            target_publisher=target_publisher,
            target_type=target_type,
            source_pid=source_pid,
            source_publisher=source_publisher,
            source_type=source_type,
            relation=relation,
            from_date=from_date,
            to_date=to_date,
            page=page,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def get_relations_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Retrieve information about available relation types from scholexplorer

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.research_products.get_relations_info()
        """
        _response = self._raw_client.get_relations_info(request_options=request_options)
        return _response.data


class AsyncResearchProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawResearchProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawResearchProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawResearchProductsClient
        """
        return self._raw_client

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
    ) -> ResearchProductsSearchResponseV2:
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
        ResearchProductsSearchResponseV2
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.research_products.search()


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            logical_operator=logical_operator,
            search=search,
            main_title=main_title,
            description=description,
            id=id,
            pid=pid,
            original_id=original_id,
            ror_id=ror_id,
            type=type,
            from_publication_date=from_publication_date,
            to_publication_date=to_publication_date,
            subjects=subjects,
            country_code=country_code,
            author_full_name=author_full_name,
            author_orcid=author_orcid,
            publisher=publisher,
            best_open_access_right_label=best_open_access_right_label,
            influence_class=influence_class,
            popularity_class=popularity_class,
            impulse_class=impulse_class,
            citation_count_class=citation_count_class,
            instance_type=instance_type,
            sdg=sdg,
            fos=fos,
            is_peer_reviewed=is_peer_reviewed,
            is_in_diamond_journal=is_in_diamond_journal,
            is_publicly_funded=is_publicly_funded,
            is_green=is_green,
            open_access_color=open_access_color,
            rel_organization_id=rel_organization_id,
            rel_community_id=rel_community_id,
            rel_project_id=rel_project_id,
            rel_project_code=rel_project_code,
            has_project_rel=has_project_rel,
            rel_project_funding_short_name=rel_project_funding_short_name,
            rel_project_funding_stream_id=rel_project_funding_stream_id,
            rel_hosting_data_source_id=rel_hosting_data_source_id,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    async def get_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResult:
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
        ApiResult
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.research_products.get_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id(id, request_options=request_options)
        return _response.data

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
    ) -> ResearchProductsSearchResponse:
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
        ResearchProductsSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.research_products.search1()


        asyncio.run(main())
        """
        _response = await self._raw_client.search1(
            logical_operator=logical_operator,
            search=search,
            main_title=main_title,
            description=description,
            id=id,
            pid=pid,
            original_id=original_id,
            ror_id=ror_id,
            type=type,
            from_publication_date=from_publication_date,
            to_publication_date=to_publication_date,
            subjects=subjects,
            country_code=country_code,
            author_full_name=author_full_name,
            author_orcid=author_orcid,
            publisher=publisher,
            best_open_access_right_label=best_open_access_right_label,
            influence_class=influence_class,
            popularity_class=popularity_class,
            impulse_class=impulse_class,
            citation_count_class=citation_count_class,
            instance_type=instance_type,
            sdg=sdg,
            fos=fos,
            is_peer_reviewed=is_peer_reviewed,
            is_in_diamond_journal=is_in_diamond_journal,
            is_publicly_funded=is_publicly_funded,
            is_green=is_green,
            open_access_color=open_access_color,
            rel_organization_id=rel_organization_id,
            rel_community_id=rel_community_id,
            rel_project_id=rel_project_id,
            rel_project_code=rel_project_code,
            has_project_rel=has_project_rel,
            rel_project_funding_short_name=rel_project_funding_short_name,
            rel_project_funding_stream_id=rel_project_funding_stream_id,
            rel_hosting_data_source_id=rel_hosting_data_source_id,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    async def get_by_id1(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GraphResult:
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
        GraphResult
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.research_products.get_by_id1(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id1(id, request_options=request_options)
        return _response.data

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
    ) -> SearchResponseRelation:
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
        SearchResponseRelation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.research_products.get_links()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_links(
            target_pid=target_pid,
            target_publisher=target_publisher,
            target_type=target_type,
            source_pid=source_pid,
            source_publisher=source_publisher,
            source_type=source_type,
            relation=relation,
            from_date=from_date,
            to_date=to_date,
            page=page,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def get_relations_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Retrieve information about available relation types from scholexplorer

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.research_products.get_relations_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_relations_info(request_options=request_options)
        return _response.data
