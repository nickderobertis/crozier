

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.data_source_search_response import DataSourceSearchResponse
from ..types.datasource import Datasource
from .raw_client import AsyncRawDataSourcesClient, RawDataSourcesClient
from .types.search5request_logical_operator import Search5RequestLogicalOperator


class DataSourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataSourcesClient
        """
        return self._raw_client

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
    ) -> DataSourceSearchResponse:
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
        DataSourceSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.data_sources.search5()
        """
        _response = self._raw_client.search5(
            logical_operator=logical_operator,
            search=search,
            official_name=official_name,
            english_name=english_name,
            legal_short_name=legal_short_name,
            id=id,
            pid=pid,
            subjects=subjects,
            data_source_type_name=data_source_type_name,
            content_types=content_types,
            rel_organization_id=rel_organization_id,
            rel_community_id=rel_community_id,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    def get_by_id5(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Datasource:
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
        Datasource
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.data_sources.get_by_id5(
            id="id",
        )
        """
        _response = self._raw_client.get_by_id5(id, request_options=request_options)
        return _response.data


class AsyncDataSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataSourcesClient
        """
        return self._raw_client

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
    ) -> DataSourceSearchResponse:
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
        DataSourceSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.data_sources.search5()


        asyncio.run(main())
        """
        _response = await self._raw_client.search5(
            logical_operator=logical_operator,
            search=search,
            official_name=official_name,
            english_name=english_name,
            legal_short_name=legal_short_name,
            id=id,
            pid=pid,
            subjects=subjects,
            data_source_type_name=data_source_type_name,
            content_types=content_types,
            rel_organization_id=rel_organization_id,
            rel_community_id=rel_community_id,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    async def get_by_id5(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Datasource:
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
        Datasource
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.data_sources.get_by_id5(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id5(id, request_options=request_options)
        return _response.data
