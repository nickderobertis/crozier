

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawContentproSearchClient, RawContentproSearchClient
from .types.get_contentpro_search_response import GetContentproSearchResponse


class ContentproSearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContentproSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContentproSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContentproSearchClient
        """
        return self._raw_client

    def send_search_terms_to_receive_the_most_relevant_articles_and_companies(
        self, *, terms: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetContentproSearchResponse:
        """
        Parameters
        ----------
        terms : str
            We provide information about related companies and articles based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/contentpro-search?terms=cloud+computing,enterprise,security

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContentproSearchResponse
            A successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.contentpro_search.send_search_terms_to_receive_the_most_relevant_articles_and_companies(
            terms="terms",
        )
        """
        _response = self._raw_client.send_search_terms_to_receive_the_most_relevant_articles_and_companies(
            terms=terms, request_options=request_options
        )
        return _response.data


class AsyncContentproSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContentproSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContentproSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContentproSearchClient
        """
        return self._raw_client

    async def send_search_terms_to_receive_the_most_relevant_articles_and_companies(
        self, *, terms: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetContentproSearchResponse:
        """
        Parameters
        ----------
        terms : str
            We provide information about related companies and articles based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/contentpro-search?terms=cloud+computing,enterprise,security

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContentproSearchResponse
            A successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.contentpro_search.send_search_terms_to_receive_the_most_relevant_articles_and_companies(
                terms="terms",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_search_terms_to_receive_the_most_relevant_articles_and_companies(
            terms=terms, request_options=request_options
        )
        return _response.data
