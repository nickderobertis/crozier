

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawArticlesClient, RawArticlesClient


class ArticlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArticlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArticlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArticlesClient
        """
        return self._raw_client

    def get_articles(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        exclude_featured: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

        offset : typing.Optional[int]

        query : typing.Optional[str]
            What's being searched for

        exclude_featured : typing.Optional[int]
            Number of featured articles to exclude

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.articles.get_articles()
        """
        _response = self._raw_client.get_articles(
            page=page,
            per_page=per_page,
            offset=offset,
            query=query,
            exclude_featured=exclude_featured,
            request_options=request_options,
        )
        return _response.data

    def list_of_all_article_categories(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of all article categories

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.articles.list_of_all_article_categories()
        """
        _response = self._raw_client.list_of_all_article_categories(request_options=request_options)
        return _response.data


class AsyncArticlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArticlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArticlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArticlesClient
        """
        return self._raw_client

    async def get_articles(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        exclude_featured: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

        offset : typing.Optional[int]

        query : typing.Optional[str]
            What's being searched for

        exclude_featured : typing.Optional[int]
            Number of featured articles to exclude

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.articles.get_articles()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_articles(
            page=page,
            per_page=per_page,
            offset=offset,
            query=query,
            exclude_featured=exclude_featured,
            request_options=request_options,
        )
        return _response.data

    async def list_of_all_article_categories(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of all article categories

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.articles.list_of_all_article_categories()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_all_article_categories(request_options=request_options)
        return _response.data
