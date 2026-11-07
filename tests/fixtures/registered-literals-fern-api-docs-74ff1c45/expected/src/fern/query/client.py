

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_query_response import CreateQueryResponse
from ..types.get_queries_response import GetQueriesResponse
from ..types.query_status import QueryStatus
from ..types.resolution_filter import ResolutionFilter
from .raw_client import AsyncRawQueryClient, RawQueryClient


OMIT = typing.cast(typing.Any, ...)


class QueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueryClient
        """
        return self._raw_client

    def create_query(
        self,
        *,
        domain: str,
        query_id: str,
        conversation_id: str,
        query_domain: str,
        text: str,
        role: str,
        source: str,
        created_at: dt.datetime,
        time_to_first_token: typing.Optional[float] = OMIT,
        subqueries: typing.Optional[typing.Sequence[str]] = OMIT,
        status: typing.Optional[QueryStatus] = OMIT,
        origin_page: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateQueryResponse:
        """
        Parameters
        ----------
        domain : str

        query_id : str

        conversation_id : str

        query_domain : str

        text : str

        role : str

        source : str

        created_at : dt.datetime

        time_to_first_token : typing.Optional[float]

        subqueries : typing.Optional[typing.Sequence[str]]

        status : typing.Optional[QueryStatus]

        origin_page : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateQueryResponse
            Successful Response

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.query.create_query(
            domain="domain",
            query_id="query_id",
            conversation_id="conversation_id",
            query_domain="domain",
            text="text",
            role="role",
            source="source",
            created_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.create_query(
            domain=domain,
            query_id=query_id,
            conversation_id=conversation_id,
            query_domain=query_domain,
            text=text,
            role=role,
            source=source,
            created_at=created_at,
            time_to_first_token=time_to_first_token,
            subqueries=subqueries,
            status=status,
            origin_page=origin_page,
            request_options=request_options,
        )
        return _response.data

    def get_recent_queries(
        self,
        domain: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        cutoff_time: typing.Optional[dt.datetime] = None,
        include_assistant: typing.Optional[bool] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        resolution: typing.Optional[ResolutionFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetQueriesResponse:
        """
        Parameters
        ----------
        domain : str

        page : typing.Optional[int]
            The page number for pagination

        limit : typing.Optional[int]
            The number of queries per page

        cutoff_time : typing.Optional[dt.datetime]
            Only return queries after this time

        include_assistant : typing.Optional[bool]
            Whether to include assistant responses in the results

        start_date : typing.Optional[dt.datetime]
            The start date of the period to retrieve analytics for

        end_date : typing.Optional[dt.datetime]
            The end date of the period to retrieve analytics for

        resolution : typing.Optional[ResolutionFilter]
            Only return queries whose conversation was resolved or unresolved. Conversations that have not been scored yet are excluded from both filters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQueriesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.query.get_recent_queries(
            domain="domain",
        )
        """
        _response = self._raw_client.get_recent_queries(
            domain,
            page=page,
            limit=limit,
            cutoff_time=cutoff_time,
            include_assistant=include_assistant,
            start_date=start_date,
            end_date=end_date,
            resolution=resolution,
            request_options=request_options,
        )
        return _response.data


class AsyncQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueryClient
        """
        return self._raw_client

    async def create_query(
        self,
        *,
        domain: str,
        query_id: str,
        conversation_id: str,
        query_domain: str,
        text: str,
        role: str,
        source: str,
        created_at: dt.datetime,
        time_to_first_token: typing.Optional[float] = OMIT,
        subqueries: typing.Optional[typing.Sequence[str]] = OMIT,
        status: typing.Optional[QueryStatus] = OMIT,
        origin_page: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateQueryResponse:
        """
        Parameters
        ----------
        domain : str

        query_id : str

        conversation_id : str

        query_domain : str

        text : str

        role : str

        source : str

        created_at : dt.datetime

        time_to_first_token : typing.Optional[float]

        subqueries : typing.Optional[typing.Sequence[str]]

        status : typing.Optional[QueryStatus]

        origin_page : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateQueryResponse
            Successful Response

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.query.create_query(
                domain="domain",
                query_id="query_id",
                conversation_id="conversation_id",
                query_domain="domain",
                text="text",
                role="role",
                source="source",
                created_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_query(
            domain=domain,
            query_id=query_id,
            conversation_id=conversation_id,
            query_domain=query_domain,
            text=text,
            role=role,
            source=source,
            created_at=created_at,
            time_to_first_token=time_to_first_token,
            subqueries=subqueries,
            status=status,
            origin_page=origin_page,
            request_options=request_options,
        )
        return _response.data

    async def get_recent_queries(
        self,
        domain: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        cutoff_time: typing.Optional[dt.datetime] = None,
        include_assistant: typing.Optional[bool] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        resolution: typing.Optional[ResolutionFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetQueriesResponse:
        """
        Parameters
        ----------
        domain : str

        page : typing.Optional[int]
            The page number for pagination

        limit : typing.Optional[int]
            The number of queries per page

        cutoff_time : typing.Optional[dt.datetime]
            Only return queries after this time

        include_assistant : typing.Optional[bool]
            Whether to include assistant responses in the results

        start_date : typing.Optional[dt.datetime]
            The start date of the period to retrieve analytics for

        end_date : typing.Optional[dt.datetime]
            The end date of the period to retrieve analytics for

        resolution : typing.Optional[ResolutionFilter]
            Only return queries whose conversation was resolved or unresolved. Conversations that have not been scored yet are excluded from both filters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQueriesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.query.get_recent_queries(
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_recent_queries(
            domain,
            page=page,
            limit=limit,
            cutoff_time=cutoff_time,
            include_assistant=include_assistant,
            start_date=start_date,
            end_date=end_date,
            resolution=resolution,
            request_options=request_options,
        )
        return _response.data
