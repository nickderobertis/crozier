

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSearchClient, RawSearchClient
from .types.get_search_response import GetSearchResponse


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

    def send_search_terms_to_receive_the_most_relevant_companies_along_with_text_snippets(
        self, *, terms: str, page: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSearchResponse:
        """
        Parameters
        ----------
        terms : str
            We provide information about related companies based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/search?link=cloud+computing,enterprise,security

        page : typing.Optional[str]
            Page number of search results. Ex. https://api.byautomata.io/search?page=0&link=cloud+computing,enterprise,security

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSearchResponse
            A successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search.send_search_terms_to_receive_the_most_relevant_companies_along_with_text_snippets(
            terms="terms",
        )
        """
        _response = self._raw_client.send_search_terms_to_receive_the_most_relevant_companies_along_with_text_snippets(
            terms=terms, page=page, request_options=request_options
        )
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

    async def send_search_terms_to_receive_the_most_relevant_companies_along_with_text_snippets(
        self, *, terms: str, page: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSearchResponse:
        """
        Parameters
        ----------
        terms : str
            We provide information about related companies based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/search?link=cloud+computing,enterprise,security

        page : typing.Optional[str]
            Page number of search results. Ex. https://api.byautomata.io/search?page=0&link=cloud+computing,enterprise,security

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSearchResponse
            A successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search.send_search_terms_to_receive_the_most_relevant_companies_along_with_text_snippets(
                terms="terms",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.send_search_terms_to_receive_the_most_relevant_companies_along_with_text_snippets(
                terms=terms, page=page, request_options=request_options
            )
        )
        return _response.data
