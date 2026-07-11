

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.search_result import SearchResult
from .raw_client import AsyncRawInlinedClient, RawInlinedClient
from .types.inlined_index_response import InlinedIndexResponse
from .types.inlined_search_request_filter import InlinedSearchRequestFilter
from .types.inlined_search_response import InlinedSearchResponse


OMIT = typing.cast(typing.Any, ...)


class InlinedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInlinedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInlinedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInlinedClient
        """
        return self._raw_client

    def search(
        self,
        *,
        query: str,
        limit: typing.Optional[int] = OMIT,
        filter: typing.Optional[InlinedSearchRequestFilter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlinedSearchResponse:
        """
        Parameters
        ----------
        query : str

        limit : typing.Optional[int]

        filter : typing.Optional[InlinedSearchRequestFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlinedSearchResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inlined.search(
            query="query",
        )
        """
        _response = self._raw_client.search(query=query, limit=limit, filter=filter, request_options=request_options)
        return _response.data

    def index(
        self, *, document: SearchResult, request_options: typing.Optional[RequestOptions] = None
    ) -> InlinedIndexResponse:
        """
        Parameters
        ----------
        document : SearchResult

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlinedIndexResponse


        Examples
        --------
        from fern import FernApi, SearchResult

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inlined.index(
            document=SearchResult(
                id="id",
                score=1.1,
            ),
        )
        """
        _response = self._raw_client.index(document=document, request_options=request_options)
        return _response.data


class AsyncInlinedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInlinedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInlinedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInlinedClient
        """
        return self._raw_client

    async def search(
        self,
        *,
        query: str,
        limit: typing.Optional[int] = OMIT,
        filter: typing.Optional[InlinedSearchRequestFilter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlinedSearchResponse:
        """
        Parameters
        ----------
        query : str

        limit : typing.Optional[int]

        filter : typing.Optional[InlinedSearchRequestFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlinedSearchResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inlined.search(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            query=query, limit=limit, filter=filter, request_options=request_options
        )
        return _response.data

    async def index(
        self, *, document: SearchResult, request_options: typing.Optional[RequestOptions] = None
    ) -> InlinedIndexResponse:
        """
        Parameters
        ----------
        document : SearchResult

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlinedIndexResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SearchResult

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inlined.index(
                document=SearchResult(
                    id="id",
                    score=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.index(document=document, request_options=request_options)
        return _response.data
