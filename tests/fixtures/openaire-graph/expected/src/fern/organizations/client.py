

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_organization import ApiOrganization
from ..types.organization_search_response import OrganizationSearchResponse
from .raw_client import AsyncRawOrganizationsClient, RawOrganizationsClient
from .types.search4request_logical_operator import Search4RequestLogicalOperator


class OrganizationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationsClient
        """
        return self._raw_client

    def search4(
        self,
        *,
        logical_operator: typing.Optional[Search4RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        legal_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        legal_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        country_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationSearchResponse:
        """
        Explore organizations exploiting various filter parameters

        Parameters
        ----------
        logical_operator : typing.Optional[Search4RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        legal_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The legal name of the organization. Logical operator: *OR*

        legal_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The legal name of the organization in short form. Logical operator: *OR*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the organization. Logical operator: *OR*

        pid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The persistent identifier of the organization. Logical operator: *OR*

        country_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The country code of the organization. Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve organizations connected to the community (with OpenAIRE id). Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve organizations collected from the data source (with OpenAIRE id). Logical operator: *OR*

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
        OrganizationSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.organizations.search4()
        """
        _response = self._raw_client.search4(
            logical_operator=logical_operator,
            search=search,
            legal_name=legal_name,
            legal_short_name=legal_short_name,
            id=id,
            pid=pid,
            country_code=country_code,
            rel_community_id=rel_community_id,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    def get_by_id4(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiOrganization:
        """
        Get a organization object by specifying its id.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiOrganization
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.organizations.get_by_id4(
            id="id",
        )
        """
        _response = self._raw_client.get_by_id4(id, request_options=request_options)
        return _response.data


class AsyncOrganizationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationsClient
        """
        return self._raw_client

    async def search4(
        self,
        *,
        logical_operator: typing.Optional[Search4RequestLogicalOperator] = None,
        search: typing.Optional[str] = None,
        legal_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        legal_short_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        country_code: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_community_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        rel_collected_from_datasource_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationSearchResponse:
        """
        Explore organizations exploiting various filter parameters

        Parameters
        ----------
        logical_operator : typing.Optional[Search4RequestLogicalOperator]
            Logical operator used to combine field-level queries. Default value: *AND* </br>
            Use it when specifying multiple fields in the search. </br>
            *example: (mainTitle=geography) AND (description=19th century)*

        search : typing.Optional[str]
            Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
            Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
            Use parentheses `()` to group conditions and control evaluation order. </br>
            *example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*

        legal_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The legal name of the organization. Logical operator: *OR*

        legal_short_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The legal name of the organization in short form. Logical operator: *OR*

        id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The OpenAIRE id of the organization. Logical operator: *OR*

        pid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The persistent identifier of the organization. Logical operator: *OR*

        country_code : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The country code of the organization. Logical operator: *OR*

        rel_community_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve organizations connected to the community (with OpenAIRE id). Logical operator: *OR*

        rel_collected_from_datasource_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Retrieve organizations collected from the data source (with OpenAIRE id). Logical operator: *OR*

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
        OrganizationSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.organizations.search4()


        asyncio.run(main())
        """
        _response = await self._raw_client.search4(
            logical_operator=logical_operator,
            search=search,
            legal_name=legal_name,
            legal_short_name=legal_short_name,
            id=id,
            pid=pid,
            country_code=country_code,
            rel_community_id=rel_community_id,
            rel_collected_from_datasource_id=rel_collected_from_datasource_id,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    async def get_by_id4(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiOrganization:
        """
        Get a organization object by specifying its id.

        Parameters
        ----------
        id : str
            The OpenAIRE id of the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiOrganization
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.organizations.get_by_id4(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id4(id, request_options=request_options)
        return _response.data
