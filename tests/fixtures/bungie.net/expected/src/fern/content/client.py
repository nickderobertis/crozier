

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawContentClient, RawContentClient
from .types.content_get_content_by_id_response import ContentGetContentByIdResponse
from .types.content_get_content_by_tag_and_type_response import ContentGetContentByTagAndTypeResponse
from .types.content_get_content_type_response import ContentGetContentTypeResponse
from .types.content_rss_news_articles_response import ContentRssNewsArticlesResponse
from .types.content_search_content_by_tag_and_type_response import ContentSearchContentByTagAndTypeResponse
from .types.content_search_content_with_text_response import ContentSearchContentWithTextResponse
from .types.content_search_help_articles_response import ContentSearchHelpArticlesResponse


class ContentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContentClient
        """
        return self._raw_client

    def getcontentbyid(
        self,
        id: int,
        locale: str,
        *,
        head: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentGetContentByIdResponse:
        """
        Returns a content item referenced by id

        Parameters
        ----------
        id : int


        locale : str


        head : typing.Optional[bool]
            false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentGetContentByIdResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content.getcontentbyid(
            id=1000000,
            locale="locale",
        )
        """
        _response = self._raw_client.getcontentbyid(id, locale, head=head, request_options=request_options)
        return _response.data

    def getcontentbytagandtype(
        self,
        tag: str,
        type: str,
        locale: str,
        *,
        head: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentGetContentByTagAndTypeResponse:
        """
        Returns the newest item that matches a given tag and Content Type.

        Parameters
        ----------
        tag : str


        type : str


        locale : str


        head : typing.Optional[bool]
            Not used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentGetContentByTagAndTypeResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content.getcontentbytagandtype(
            tag="tag",
            type="type",
            locale="locale",
        )
        """
        _response = self._raw_client.getcontentbytagandtype(
            tag, type, locale, head=head, request_options=request_options
        )
        return _response.data

    def getcontenttype(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentGetContentTypeResponse:
        """
        Gets an object describing a particular variant of content.

        Parameters
        ----------
        type : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentGetContentTypeResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content.getcontenttype(
            type="type",
        )
        """
        _response = self._raw_client.getcontenttype(type, request_options=request_options)
        return _response.data

    def rssnewsarticles(
        self,
        page_token: str,
        *,
        categoryfilter: typing.Optional[str] = None,
        includebody: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentRssNewsArticlesResponse:
        """
        Returns a JSON string response that is the RSS feed for news articles.

        Parameters
        ----------
        page_token : str
            Zero-based pagination token for paging through result sets.

        categoryfilter : typing.Optional[str]
            Optionally filter response to only include news items in a certain category.

        includebody : typing.Optional[bool]
            Optionally include full content body for each news item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentRssNewsArticlesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content.rssnewsarticles(
            page_token="pageToken",
        )
        """
        _response = self._raw_client.rssnewsarticles(
            page_token, categoryfilter=categoryfilter, includebody=includebody, request_options=request_options
        )
        return _response.data

    def searchcontentwithtext(
        self,
        locale: str,
        *,
        ctype: typing.Optional[str] = None,
        currentpage: typing.Optional[int] = None,
        head: typing.Optional[bool] = None,
        searchtext: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentSearchContentWithTextResponse:
        """
        Gets content based on querystring information passed in. Provides basic search and text search capabilities.

        Parameters
        ----------
        locale : str


        ctype : typing.Optional[str]
            Content type tag: Help, News, etc. Supply multiple ctypes separated by space.

        currentpage : typing.Optional[int]
            Page number for the search results, starting with page 1.

        head : typing.Optional[bool]
            Not used.

        searchtext : typing.Optional[str]
            Word or phrase for the search.

        source : typing.Optional[str]
            For analytics, hint at the part of the app that triggered the search. Optional.

        tag : typing.Optional[str]
            Tag used on the content to be searched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSearchContentWithTextResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content.searchcontentwithtext(
            locale="locale",
        )
        """
        _response = self._raw_client.searchcontentwithtext(
            locale,
            ctype=ctype,
            currentpage=currentpage,
            head=head,
            searchtext=searchtext,
            source=source,
            tag=tag,
            request_options=request_options,
        )
        return _response.data

    def searchcontentbytagandtype(
        self,
        tag: str,
        type: str,
        locale: str,
        *,
        currentpage: typing.Optional[int] = None,
        head: typing.Optional[bool] = None,
        itemsperpage: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentSearchContentByTagAndTypeResponse:
        """
        Searches for Content Items that match the given Tag and Content Type.

        Parameters
        ----------
        tag : str


        type : str


        locale : str


        currentpage : typing.Optional[int]
            Page number for the search results starting with page 1.

        head : typing.Optional[bool]
            Not used.

        itemsperpage : typing.Optional[int]
            Not used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSearchContentByTagAndTypeResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content.searchcontentbytagandtype(
            tag="tag",
            type="type",
            locale="locale",
        )
        """
        _response = self._raw_client.searchcontentbytagandtype(
            tag,
            type,
            locale,
            currentpage=currentpage,
            head=head,
            itemsperpage=itemsperpage,
            request_options=request_options,
        )
        return _response.data

    def searchhelparticles(
        self, searchtext: str, size: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSearchHelpArticlesResponse:
        """
        Search for Help Articles.

        Parameters
        ----------
        searchtext : str


        size : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSearchHelpArticlesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.content.searchhelparticles(
            searchtext="searchtext",
            size="size",
        )
        """
        _response = self._raw_client.searchhelparticles(searchtext, size, request_options=request_options)
        return _response.data


class AsyncContentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContentClient
        """
        return self._raw_client

    async def getcontentbyid(
        self,
        id: int,
        locale: str,
        *,
        head: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentGetContentByIdResponse:
        """
        Returns a content item referenced by id

        Parameters
        ----------
        id : int


        locale : str


        head : typing.Optional[bool]
            false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentGetContentByIdResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content.getcontentbyid(
                id=1000000,
                locale="locale",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentbyid(id, locale, head=head, request_options=request_options)
        return _response.data

    async def getcontentbytagandtype(
        self,
        tag: str,
        type: str,
        locale: str,
        *,
        head: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentGetContentByTagAndTypeResponse:
        """
        Returns the newest item that matches a given tag and Content Type.

        Parameters
        ----------
        tag : str


        type : str


        locale : str


        head : typing.Optional[bool]
            Not used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentGetContentByTagAndTypeResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content.getcontentbytagandtype(
                tag="tag",
                type="type",
                locale="locale",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentbytagandtype(
            tag, type, locale, head=head, request_options=request_options
        )
        return _response.data

    async def getcontenttype(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentGetContentTypeResponse:
        """
        Gets an object describing a particular variant of content.

        Parameters
        ----------
        type : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentGetContentTypeResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content.getcontenttype(
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontenttype(type, request_options=request_options)
        return _response.data

    async def rssnewsarticles(
        self,
        page_token: str,
        *,
        categoryfilter: typing.Optional[str] = None,
        includebody: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentRssNewsArticlesResponse:
        """
        Returns a JSON string response that is the RSS feed for news articles.

        Parameters
        ----------
        page_token : str
            Zero-based pagination token for paging through result sets.

        categoryfilter : typing.Optional[str]
            Optionally filter response to only include news items in a certain category.

        includebody : typing.Optional[bool]
            Optionally include full content body for each news item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentRssNewsArticlesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content.rssnewsarticles(
                page_token="pageToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rssnewsarticles(
            page_token, categoryfilter=categoryfilter, includebody=includebody, request_options=request_options
        )
        return _response.data

    async def searchcontentwithtext(
        self,
        locale: str,
        *,
        ctype: typing.Optional[str] = None,
        currentpage: typing.Optional[int] = None,
        head: typing.Optional[bool] = None,
        searchtext: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentSearchContentWithTextResponse:
        """
        Gets content based on querystring information passed in. Provides basic search and text search capabilities.

        Parameters
        ----------
        locale : str


        ctype : typing.Optional[str]
            Content type tag: Help, News, etc. Supply multiple ctypes separated by space.

        currentpage : typing.Optional[int]
            Page number for the search results, starting with page 1.

        head : typing.Optional[bool]
            Not used.

        searchtext : typing.Optional[str]
            Word or phrase for the search.

        source : typing.Optional[str]
            For analytics, hint at the part of the app that triggered the search. Optional.

        tag : typing.Optional[str]
            Tag used on the content to be searched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSearchContentWithTextResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content.searchcontentwithtext(
                locale="locale",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.searchcontentwithtext(
            locale,
            ctype=ctype,
            currentpage=currentpage,
            head=head,
            searchtext=searchtext,
            source=source,
            tag=tag,
            request_options=request_options,
        )
        return _response.data

    async def searchcontentbytagandtype(
        self,
        tag: str,
        type: str,
        locale: str,
        *,
        currentpage: typing.Optional[int] = None,
        head: typing.Optional[bool] = None,
        itemsperpage: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContentSearchContentByTagAndTypeResponse:
        """
        Searches for Content Items that match the given Tag and Content Type.

        Parameters
        ----------
        tag : str


        type : str


        locale : str


        currentpage : typing.Optional[int]
            Page number for the search results starting with page 1.

        head : typing.Optional[bool]
            Not used.

        itemsperpage : typing.Optional[int]
            Not used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSearchContentByTagAndTypeResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content.searchcontentbytagandtype(
                tag="tag",
                type="type",
                locale="locale",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.searchcontentbytagandtype(
            tag,
            type,
            locale,
            currentpage=currentpage,
            head=head,
            itemsperpage=itemsperpage,
            request_options=request_options,
        )
        return _response.data

    async def searchhelparticles(
        self, searchtext: str, size: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSearchHelpArticlesResponse:
        """
        Search for Help Articles.

        Parameters
        ----------
        searchtext : str


        size : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSearchHelpArticlesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.content.searchhelparticles(
                searchtext="searchtext",
                size="size",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.searchhelparticles(searchtext, size, request_options=request_options)
        return _response.data
