

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.page_author_dto import PageAuthorDto
from ..types.page_integer import PageInteger
from ..types.page_string import PageString
from .raw_client import AsyncRawReferentialMetadataClient, RawReferentialMetadataClient
from .types.get_tags_request_include import GetTagsRequestInclude


class ReferentialMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReferentialMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReferentialMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReferentialMetadataClient
        """
        return self._raw_client

    def get_age_ratings(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageInteger:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageInteger
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_age_ratings()
        """
        _response = self._raw_client.get_age_ratings(
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_authors(
        self,
        *,
        search: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageAuthorDto:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        role : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageAuthorDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_authors()
        """
        _response = self._raw_client.get_authors(
            search=search,
            role=role,
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            readlist_id=readlist_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_authors_names(
        self,
        *,
        search: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        role : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_authors_names()
        """
        _response = self._raw_client.get_authors_names(
            search=search,
            role=role,
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            readlist_id=readlist_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_authors_roles(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_authors_roles()
        """
        _response = self._raw_client.get_authors_roles(
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            readlist_id=readlist_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_genres(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_genres()
        """
        _response = self._raw_client.get_genres(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_languages(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_languages()
        """
        _response = self._raw_client.get_languages(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_publishers(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_publishers()
        """
        _response = self._raw_client.get_publishers(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_series_release_years(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_series_release_years()
        """
        _response = self._raw_client.get_series_release_years(
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_sharing_labels(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_sharing_labels()
        """
        _response = self._raw_client.get_sharing_labels(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_tags(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include: typing.Optional[GetTagsRequestInclude] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        include : typing.Optional[GetTagsRequestInclude]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.referential_metadata.get_tags()
        """
        _response = self._raw_client.get_tags(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            readlist_id=readlist_id,
            include=include,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data


class AsyncReferentialMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReferentialMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReferentialMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReferentialMetadataClient
        """
        return self._raw_client

    async def get_age_ratings(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageInteger:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageInteger
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_age_ratings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_age_ratings(
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_authors(
        self,
        *,
        search: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageAuthorDto:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        role : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageAuthorDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_authors()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authors(
            search=search,
            role=role,
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            readlist_id=readlist_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_authors_names(
        self,
        *,
        search: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        role : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_authors_names()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authors_names(
            search=search,
            role=role,
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            readlist_id=readlist_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_authors_roles(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_authors_roles()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authors_roles(
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            readlist_id=readlist_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_genres(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_genres()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_genres(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_languages(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_languages()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_languages(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_publishers(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_publishers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_publishers(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_series_release_years(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_series_release_years()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_release_years(
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_sharing_labels(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_sharing_labels()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sharing_labels(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_tags(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        series_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        readlist_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        include: typing.Optional[GetTagsRequestInclude] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageString:
        """
        Can be filtered by various criteria

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        series_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        readlist_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        include : typing.Optional[GetTagsRequestInclude]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.referential_metadata.get_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tags(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            readlist_id=readlist_id,
            include=include,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data
