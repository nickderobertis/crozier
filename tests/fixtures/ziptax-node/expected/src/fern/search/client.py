

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tic_recommend_response import TicRecommendResponse
from ..types.tic_search_response import TicSearchResponse
from .raw_client import AsyncRawSearchClient, RawSearchClient


OMIT = typing.cast(typing.Any, ...)


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchClient
        """
        return self._raw_client

    def get_tic_search_schema(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the JSON Schema describing the TIC search response body. Public; no authentication required.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search.get_tic_search_schema()
        """
        _response = self._raw_client.get_tic_search_schema(request_options=request_options)
        return _response.data

    def search_tic(self, *, query: str, request_options: typing.Optional[RequestOptions] = None) -> TicSearchResponse:
        """
        Searches Taxability Information Codes (TIC) by free-text product description and returns ranked matches. Requires authentication via the X-API-KEY header or key query parameter.

        Parameters
        ----------
        query : str
            Free-text product description to match against TIC codes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search.search_tic(
            query="Ceramic & Pottery Kilns",
        )
        """
        _response = self._raw_client.search_tic(query=query, request_options=request_options)
        return _response.data

    def recommend_tic(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TicRecommendResponse:
        """
        Returns a recommended Taxability Information Code (TIC) for a free-text product description using a machine-learning model. Requires authentication via the X-API-KEY header or key query parameter.

        Parameters
        ----------
        query : str
            Free-text product description to get a recommended TIC for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicRecommendResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search.recommend_tic(
            query="wireless bluetooth headphones",
        )
        """
        _response = self._raw_client.recommend_tic(query=query, request_options=request_options)
        return _response.data


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchClient
        """
        return self._raw_client

    async def get_tic_search_schema(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the JSON Schema describing the TIC search response body. Public; no authentication required.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search.get_tic_search_schema()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tic_search_schema(request_options=request_options)
        return _response.data

    async def search_tic(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TicSearchResponse:
        """
        Searches Taxability Information Codes (TIC) by free-text product description and returns ranked matches. Requires authentication via the X-API-KEY header or key query parameter.

        Parameters
        ----------
        query : str
            Free-text product description to match against TIC codes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search.search_tic(
                query="Ceramic & Pottery Kilns",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_tic(query=query, request_options=request_options)
        return _response.data

    async def recommend_tic(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TicRecommendResponse:
        """
        Returns a recommended Taxability Information Code (TIC) for a free-text product description using a machine-learning model. Requires authentication via the X-API-KEY header or key query parameter.

        Parameters
        ----------
        query : str
            Free-text product description to get a recommended TIC for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicRecommendResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search.recommend_tic(
                query="wireless bluetooth headphones",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recommend_tic(query=query, request_options=request_options)
        return _response.data
