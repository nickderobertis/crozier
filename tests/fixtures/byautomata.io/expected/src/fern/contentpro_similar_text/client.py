

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawContentproSimilarTextClient, RawContentproSimilarTextClient
from .types.post_contentpro_similar_text_response import PostContentproSimilarTextResponse


OMIT = typing.cast(typing.Any, ...)


class ContentproSimilarTextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContentproSimilarTextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContentproSimilarTextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContentproSimilarTextClient
        """
        return self._raw_client

    def the_contentpro_similar_text_endpoint_accepts_and_arbitrary_piece_of_text_and_returns_similar_articles_and_blogs_written_by_companies(
        self, *, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostContentproSimilarTextResponse:
        """
        Parameters
        ----------
        text : str
            Any piece of text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostContentproSimilarTextResponse
            A successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.contentpro_similar_text.the_contentpro_similar_text_endpoint_accepts_and_arbitrary_piece_of_text_and_returns_similar_articles_and_blogs_written_by_companies(
            text="text",
        )
        """
        _response = self._raw_client.the_contentpro_similar_text_endpoint_accepts_and_arbitrary_piece_of_text_and_returns_similar_articles_and_blogs_written_by_companies(
            text=text, request_options=request_options
        )
        return _response.data


class AsyncContentproSimilarTextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContentproSimilarTextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContentproSimilarTextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContentproSimilarTextClient
        """
        return self._raw_client

    async def the_contentpro_similar_text_endpoint_accepts_and_arbitrary_piece_of_text_and_returns_similar_articles_and_blogs_written_by_companies(
        self, *, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostContentproSimilarTextResponse:
        """
        Parameters
        ----------
        text : str
            Any piece of text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostContentproSimilarTextResponse
            A successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.contentpro_similar_text.the_contentpro_similar_text_endpoint_accepts_and_arbitrary_piece_of_text_and_returns_similar_articles_and_blogs_written_by_companies(
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.the_contentpro_similar_text_endpoint_accepts_and_arbitrary_piece_of_text_and_returns_similar_articles_and_blogs_written_by_companies(
            text=text, request_options=request_options
        )
        return _response.data
