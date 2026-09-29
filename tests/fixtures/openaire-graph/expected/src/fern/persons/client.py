

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_person import ApiPerson
from ..types.graph_result import GraphResult
from .raw_client import AsyncRawPersonsClient, RawPersonsClient
from .types.search3request_logical_operator import Search3RequestLogicalOperator


class PersonsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPersonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPersonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPersonsClient
        """
        return self._raw_client

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
    ) -> ApiPerson:
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
        ApiPerson
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.persons.search3()
        """
        _response = self._raw_client.search3(
            logical_operator=logical_operator,
            search=search,
            id=id,
            original_id=original_id,
            given_name=given_name,
            last_name=last_name,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    def get_by_id3(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GraphResult:
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
        GraphResult
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.persons.get_by_id3(
            id="id",
        )
        """
        _response = self._raw_client.get_by_id3(id, request_options=request_options)
        return _response.data


class AsyncPersonsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPersonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPersonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPersonsClient
        """
        return self._raw_client

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
    ) -> ApiPerson:
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
        ApiPerson
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.persons.search3()


        asyncio.run(main())
        """
        _response = await self._raw_client.search3(
            logical_operator=logical_operator,
            search=search,
            id=id,
            original_id=original_id,
            given_name=given_name,
            last_name=last_name,
            page=page,
            page_size=page_size,
            cursor=cursor,
            sort_by=sort_by,
            request_options=request_options,
        )
        return _response.data

    async def get_by_id3(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GraphResult:
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
        GraphResult
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.persons.get_by_id3(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id3(id, request_options=request_options)
        return _response.data
