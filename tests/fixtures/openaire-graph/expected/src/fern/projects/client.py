

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.project_search_response import ProjectSearchResponse
from ..types.search_response import SearchResponse
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.search2request_logical_operator import Search2RequestLogicalOperator
from .types.search8request_format import Search8RequestFormat


class ProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectsClient
        """
        return self._raw_client

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
    ) -> SearchResponse:
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
        SearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.search2()
        """
        _response = self._raw_client.search2(
            logical_operator=logical_operator,
            search=search,
            title=title,
            keywords=keywords,
            id=id,
            code=code,
            acronym=acronym,
            call_identifier=call_identifier,
            funding_short_name=funding_short_name,
            funding_stream_id=funding_stream_id,
            from_start_date=from_start_date,
            to_start_date=to_start_date,
            from_end_date=from_end_date,
            to_end_date=to_end_date,
            rel_organization_name=rel_organization_name,
            rel_organization_id=rel_organization_id,
            rel_community_id=rel_community_id,
            rel_organization_country_code=rel_organization_country_code,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    def get_by_id2(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ProjectSearchResponse:
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
        ProjectSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.get_by_id2(
            id="id",
        )
        """
        _response = self._raw_client.get_by_id2(id, request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.projects.search8()
        """
        _response = self._raw_client.search8(
            format=format,
            keywords=keywords,
            name=name,
            acronym=acronym,
            grant_id=grant_id,
            call_id=call_id,
            funder=funder,
            funding_stream=funding_stream,
            openaire_publication_id=openaire_publication_id,
            participant_countries=participant_countries,
            participant_acronyms=participant_acronyms,
            has_ec_funding=has_ec_funding,
            has_wt_funding=has_wt_funding,
            start_year=start_year,
            end_year=end_year,
            sort_by=sort_by,
            page=page,
            size=size,
            cursor_mark=cursor_mark,
            request_options=request_options,
        )
        return _response.data


class AsyncProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectsClient
        """
        return self._raw_client

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
    ) -> SearchResponse:
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
        SearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.search2()


        asyncio.run(main())
        """
        _response = await self._raw_client.search2(
            logical_operator=logical_operator,
            search=search,
            title=title,
            keywords=keywords,
            id=id,
            code=code,
            acronym=acronym,
            call_identifier=call_identifier,
            funding_short_name=funding_short_name,
            funding_stream_id=funding_stream_id,
            from_start_date=from_start_date,
            to_start_date=to_start_date,
            from_end_date=from_end_date,
            to_end_date=to_end_date,
            rel_organization_name=rel_organization_name,
            rel_organization_id=rel_organization_id,
            rel_community_id=rel_community_id,
            rel_organization_country_code=rel_organization_country_code,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    async def get_by_id2(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectSearchResponse:
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
        ProjectSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.get_by_id2(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id2(id, request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.projects.search8()


        asyncio.run(main())
        """
        _response = await self._raw_client.search8(
            format=format,
            keywords=keywords,
            name=name,
            acronym=acronym,
            grant_id=grant_id,
            call_id=call_id,
            funder=funder,
            funding_stream=funding_stream,
            openaire_publication_id=openaire_publication_id,
            participant_countries=participant_countries,
            participant_acronyms=participant_acronyms,
            has_ec_funding=has_ec_funding,
            has_wt_funding=has_wt_funding,
            start_year=start_year,
            end_year=end_year,
            sort_by=sort_by,
            page=page,
            size=size,
            cursor_mark=cursor_mark,
            request_options=request_options,
        )
        return _response.data
