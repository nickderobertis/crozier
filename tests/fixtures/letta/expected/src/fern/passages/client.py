

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.passage_search_result import PassageSearchResult
from .raw_client import AsyncRawPassagesClient, RawPassagesClient
from .types.passage_search_request_tag_match_mode import PassageSearchRequestTagMatchMode


OMIT = typing.cast(typing.Any, ...)


class PassagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPassagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPassagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPassagesClient
        """
        return self._raw_client

    def search_passages(
        self,
        *,
        query: str,
        agent_id: typing.Optional[str] = OMIT,
        archive_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tag_match_mode: typing.Optional[PassageSearchRequestTagMatchMode] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PassageSearchResult]:
        """
        Search passages across the organization with optional agent and archive filtering.
        Returns passages with relevance scores.

        This endpoint supports semantic search through passages:
        - If neither agent_id nor archive_id is provided, searches ALL passages in the organization
        - If agent_id is provided, searches passages across all archives attached to that agent
        - If archive_id is provided, searches passages within that specific archive
        - If both are provided, agent_id takes precedence

        Parameters
        ----------
        query : str
            Text query for semantic search

        agent_id : typing.Optional[str]
            Filter passages by agent ID

        archive_id : typing.Optional[str]
            Filter passages by archive ID

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of tags to filter search results

        tag_match_mode : typing.Optional[PassageSearchRequestTagMatchMode]
            How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter results to passages created after this datetime

        end_date : typing.Optional[dt.datetime]
            Filter results to passages created before this datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PassageSearchResult]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.passages.search_passages(
            query="query",
        )
        """
        _response = self._raw_client.search_passages(
            query=query,
            agent_id=agent_id,
            archive_id=archive_id,
            tags=tags,
            tag_match_mode=tag_match_mode,
            limit=limit,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data


class AsyncPassagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPassagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPassagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPassagesClient
        """
        return self._raw_client

    async def search_passages(
        self,
        *,
        query: str,
        agent_id: typing.Optional[str] = OMIT,
        archive_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tag_match_mode: typing.Optional[PassageSearchRequestTagMatchMode] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PassageSearchResult]:
        """
        Search passages across the organization with optional agent and archive filtering.
        Returns passages with relevance scores.

        This endpoint supports semantic search through passages:
        - If neither agent_id nor archive_id is provided, searches ALL passages in the organization
        - If agent_id is provided, searches passages across all archives attached to that agent
        - If archive_id is provided, searches passages within that specific archive
        - If both are provided, agent_id takes precedence

        Parameters
        ----------
        query : str
            Text query for semantic search

        agent_id : typing.Optional[str]
            Filter passages by agent ID

        archive_id : typing.Optional[str]
            Filter passages by archive ID

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of tags to filter search results

        tag_match_mode : typing.Optional[PassageSearchRequestTagMatchMode]
            How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter results to passages created after this datetime

        end_date : typing.Optional[dt.datetime]
            Filter results to passages created before this datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PassageSearchResult]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.passages.search_passages(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_passages(
            query=query,
            agent_id=agent_id,
            archive_id=archive_id,
            tags=tags,
            tag_match_mode=tag_match_mode,
            limit=limit,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data
