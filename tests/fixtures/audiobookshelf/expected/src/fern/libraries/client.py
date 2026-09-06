

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.library import Library
from ..types.library_display_order import LibraryDisplayOrder
from ..types.library_folders import LibraryFolders
from ..types.library_icon import LibraryIcon
from ..types.library_id import LibraryId
from ..types.library_media_type import LibraryMediaType
from ..types.library_name import LibraryName
from ..types.library_provider import LibraryProvider
from ..types.library_settings import LibrarySettings
from ..types.series_id import SeriesId
from ..types.series_with_progress_and_rss import SeriesWithProgressAndRss
from .raw_client import AsyncRawLibrariesClient, RawLibrariesClient
from .types.get_libraries_response import GetLibrariesResponse
from .types.get_library_authors_response import GetLibraryAuthorsResponse
from .types.get_library_items_response import GetLibraryItemsResponse
from .types.get_library_series_by_id_request_sort import GetLibrarySeriesByIdRequestSort
from .types.get_library_series_request_sort import GetLibrarySeriesRequestSort
from .types.get_library_series_response import GetLibrarySeriesResponse


OMIT = typing.cast(typing.Any, ...)


class LibrariesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLibrariesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLibrariesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLibrariesClient
        """
        return self._raw_client

    def get_libraries(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetLibrariesResponse:
        """
        Get all libraries on server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibrariesResponse
            getLibraries OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.get_libraries()
        """
        _response = self._raw_client.get_libraries(request_options=request_options)
        return _response.data

    def create_library(
        self,
        *,
        name: LibraryName,
        folders: LibraryFolders,
        display_order: typing.Optional[LibraryDisplayOrder] = OMIT,
        icon: typing.Optional[LibraryIcon] = OMIT,
        media_type: typing.Optional[LibraryMediaType] = OMIT,
        provider: typing.Optional[LibraryProvider] = OMIT,
        settings: typing.Optional[LibrarySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Library:
        """
        Create a new library on server.

        Parameters
        ----------
        name : LibraryName

        folders : LibraryFolders

        display_order : typing.Optional[LibraryDisplayOrder]

        icon : typing.Optional[LibraryIcon]

        media_type : typing.Optional[LibraryMediaType]

        provider : typing.Optional[LibraryProvider]

        settings : typing.Optional[LibrarySettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Library
            Library found.

        Examples
        --------
        from fern import FernApi, Folder

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.create_library(
            name="My Audiobooks",
            folders=[Folder()],
        )
        """
        _response = self._raw_client.create_library(
            name=name,
            folders=folders,
            display_order=display_order,
            icon=icon,
            media_type=media_type,
            provider=provider,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    def get_library_by_id(
        self,
        id: LibraryId,
        *,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Library:
        """
        Get a single library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        include : typing.Optional[str]

        minified : typing.Optional[int]
            Return minified items if true

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Library
            Library found.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.get_library_by_id(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            minified=1,
        )
        """
        _response = self._raw_client.get_library_by_id(
            id, include=include, minified=minified, request_options=request_options
        )
        return _response.data

    def delete_library_by_id(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Library:
        """
        Delete a single library by ID on server and return the deleted object.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Library
            Library found.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.delete_library_by_id(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.delete_library_by_id(id, request_options=request_options)
        return _response.data

    def update_library_by_id(
        self,
        id: LibraryId,
        *,
        name: typing.Optional[LibraryName] = OMIT,
        folders: typing.Optional[LibraryFolders] = OMIT,
        display_order: typing.Optional[LibraryDisplayOrder] = OMIT,
        icon: typing.Optional[LibraryIcon] = OMIT,
        media_type: typing.Optional[LibraryMediaType] = OMIT,
        provider: typing.Optional[LibraryProvider] = OMIT,
        settings: typing.Optional[LibrarySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Library:
        """
        Update a single library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        name : typing.Optional[LibraryName]

        folders : typing.Optional[LibraryFolders]

        display_order : typing.Optional[LibraryDisplayOrder]

        icon : typing.Optional[LibraryIcon]

        media_type : typing.Optional[LibraryMediaType]

        provider : typing.Optional[LibraryProvider]

        settings : typing.Optional[LibrarySettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Library
            Library found.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.update_library_by_id(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.update_library_by_id(
            id,
            name=name,
            folders=folders,
            display_order=display_order,
            icon=icon,
            media_type=media_type,
            provider=provider,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    def get_library_authors(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLibraryAuthorsResponse:
        """
        Get all authors in a library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibraryAuthorsResponse
            getLibraryAuthors OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.get_library_authors(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.get_library_authors(id, request_options=request_options)
        return _response.data

    def get_library_items(
        self,
        id: LibraryId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        collapse_series: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLibraryItemsResponse:
        """
        Get items in a library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[str]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        minified : typing.Optional[int]
            Return minified items if true

        collapse_series : typing.Optional[int]
            Whether to collapse series into a single cover

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibraryItemsResponse
            getLibraryItems OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.get_library_items(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            sort="numBooks",
            filter="media.metadata.title",
            include="rssfeed",
            minified=1,
        )
        """
        _response = self._raw_client.get_library_items(
            id,
            limit=limit,
            page=page,
            sort=sort,
            desc=desc,
            filter=filter,
            include=include,
            minified=minified,
            collapse_series=collapse_series,
            request_options=request_options,
        )
        return _response.data

    def delete_library_issues(self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Delete all items with issues in a library by library ID on the server. This only removes the items from the ABS database and does not delete media files.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            deleteLibraryIssues OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.delete_library_issues(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.delete_library_issues(id, request_options=request_options)
        return _response.data

    def get_library_series(
        self,
        id: LibraryId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[GetLibrarySeriesRequestSort] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLibrarySeriesResponse:
        """
        Get series in a library. Filtering and sorting can be applied.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[GetLibrarySeriesRequestSort]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        minified : typing.Optional[int]
            Return minified items if true

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibrarySeriesResponse
            getLibrarySeries OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.get_library_series(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            filter="media.metadata.title",
            include="rssfeed",
            minified=1,
        )
        """
        _response = self._raw_client.get_library_series(
            id,
            limit=limit,
            page=page,
            sort=sort,
            desc=desc,
            filter=filter,
            include=include,
            minified=minified,
            request_options=request_options,
        )
        return _response.data

    def get_library_series_by_id(
        self,
        id: LibraryId,
        series_id: SeriesId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[GetLibrarySeriesByIdRequestSort] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SeriesWithProgressAndRss:
        """
        Get a single series in a library by ID on server. This endpoint is deprecated and `/api/series/{id}` should be used instead.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        series_id : SeriesId
            The ID of the series.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[GetLibrarySeriesByIdRequestSort]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        minified : typing.Optional[int]
            Return minified items if true

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeriesWithProgressAndRss
            getLibrarySeriesById OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.libraries.get_library_series_by_id(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            series_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            filter="media.metadata.title",
            minified=1,
            include="rssfeed",
        )
        """
        _response = self._raw_client.get_library_series_by_id(
            id,
            series_id,
            limit=limit,
            page=page,
            sort=sort,
            desc=desc,
            filter=filter,
            minified=minified,
            include=include,
            request_options=request_options,
        )
        return _response.data


class AsyncLibrariesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLibrariesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLibrariesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLibrariesClient
        """
        return self._raw_client

    async def get_libraries(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetLibrariesResponse:
        """
        Get all libraries on server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibrariesResponse
            getLibraries OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.get_libraries()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_libraries(request_options=request_options)
        return _response.data

    async def create_library(
        self,
        *,
        name: LibraryName,
        folders: LibraryFolders,
        display_order: typing.Optional[LibraryDisplayOrder] = OMIT,
        icon: typing.Optional[LibraryIcon] = OMIT,
        media_type: typing.Optional[LibraryMediaType] = OMIT,
        provider: typing.Optional[LibraryProvider] = OMIT,
        settings: typing.Optional[LibrarySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Library:
        """
        Create a new library on server.

        Parameters
        ----------
        name : LibraryName

        folders : LibraryFolders

        display_order : typing.Optional[LibraryDisplayOrder]

        icon : typing.Optional[LibraryIcon]

        media_type : typing.Optional[LibraryMediaType]

        provider : typing.Optional[LibraryProvider]

        settings : typing.Optional[LibrarySettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Library
            Library found.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Folder

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.create_library(
                name="My Audiobooks",
                folders=[Folder()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_library(
            name=name,
            folders=folders,
            display_order=display_order,
            icon=icon,
            media_type=media_type,
            provider=provider,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    async def get_library_by_id(
        self,
        id: LibraryId,
        *,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Library:
        """
        Get a single library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        include : typing.Optional[str]

        minified : typing.Optional[int]
            Return minified items if true

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Library
            Library found.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.get_library_by_id(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                minified=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_library_by_id(
            id, include=include, minified=minified, request_options=request_options
        )
        return _response.data

    async def delete_library_by_id(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Library:
        """
        Delete a single library by ID on server and return the deleted object.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Library
            Library found.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.delete_library_by_id(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_library_by_id(id, request_options=request_options)
        return _response.data

    async def update_library_by_id(
        self,
        id: LibraryId,
        *,
        name: typing.Optional[LibraryName] = OMIT,
        folders: typing.Optional[LibraryFolders] = OMIT,
        display_order: typing.Optional[LibraryDisplayOrder] = OMIT,
        icon: typing.Optional[LibraryIcon] = OMIT,
        media_type: typing.Optional[LibraryMediaType] = OMIT,
        provider: typing.Optional[LibraryProvider] = OMIT,
        settings: typing.Optional[LibrarySettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Library:
        """
        Update a single library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        name : typing.Optional[LibraryName]

        folders : typing.Optional[LibraryFolders]

        display_order : typing.Optional[LibraryDisplayOrder]

        icon : typing.Optional[LibraryIcon]

        media_type : typing.Optional[LibraryMediaType]

        provider : typing.Optional[LibraryProvider]

        settings : typing.Optional[LibrarySettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Library
            Library found.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.update_library_by_id(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_library_by_id(
            id,
            name=name,
            folders=folders,
            display_order=display_order,
            icon=icon,
            media_type=media_type,
            provider=provider,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    async def get_library_authors(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLibraryAuthorsResponse:
        """
        Get all authors in a library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibraryAuthorsResponse
            getLibraryAuthors OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.get_library_authors(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_library_authors(id, request_options=request_options)
        return _response.data

    async def get_library_items(
        self,
        id: LibraryId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        collapse_series: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLibraryItemsResponse:
        """
        Get items in a library by ID on server.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[str]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        minified : typing.Optional[int]
            Return minified items if true

        collapse_series : typing.Optional[int]
            Whether to collapse series into a single cover

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibraryItemsResponse
            getLibraryItems OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.get_library_items(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                sort="numBooks",
                filter="media.metadata.title",
                include="rssfeed",
                minified=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_library_items(
            id,
            limit=limit,
            page=page,
            sort=sort,
            desc=desc,
            filter=filter,
            include=include,
            minified=minified,
            collapse_series=collapse_series,
            request_options=request_options,
        )
        return _response.data

    async def delete_library_issues(
        self, id: LibraryId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Delete all items with issues in a library by library ID on the server. This only removes the items from the ABS database and does not delete media files.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            deleteLibraryIssues OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.delete_library_issues(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_library_issues(id, request_options=request_options)
        return _response.data

    async def get_library_series(
        self,
        id: LibraryId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[GetLibrarySeriesRequestSort] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLibrarySeriesResponse:
        """
        Get series in a library. Filtering and sorting can be applied.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[GetLibrarySeriesRequestSort]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        minified : typing.Optional[int]
            Return minified items if true

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLibrarySeriesResponse
            getLibrarySeries OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.get_library_series(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                filter="media.metadata.title",
                include="rssfeed",
                minified=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_library_series(
            id,
            limit=limit,
            page=page,
            sort=sort,
            desc=desc,
            filter=filter,
            include=include,
            minified=minified,
            request_options=request_options,
        )
        return _response.data

    async def get_library_series_by_id(
        self,
        id: LibraryId,
        series_id: SeriesId,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort: typing.Optional[GetLibrarySeriesByIdRequestSort] = None,
        desc: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        minified: typing.Optional[int] = None,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SeriesWithProgressAndRss:
        """
        Get a single series in a library by ID on server. This endpoint is deprecated and `/api/series/{id}` should be used instead.

        Parameters
        ----------
        id : LibraryId
            The ID of the library.

        series_id : SeriesId
            The ID of the series.

        limit : typing.Optional[int]
            The number of items to return. This the size of a single page for the optional `page` query.

        page : typing.Optional[int]
            The page number (zero indexed) to return. If no limit is specified, then page will have no effect.

        sort : typing.Optional[GetLibrarySeriesByIdRequestSort]
            The field to sort by from the request.

        desc : typing.Optional[int]
            Return items in reversed order if true.

        filter : typing.Optional[str]
            The filter for the library.

        minified : typing.Optional[int]
            Return minified items if true

        include : typing.Optional[str]
            The fields to include in the response. The only current option is `rssfeed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeriesWithProgressAndRss
            getLibrarySeriesById OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.libraries.get_library_series_by_id(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                series_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                filter="media.metadata.title",
                minified=1,
                include="rssfeed",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_library_series_by_id(
            id,
            series_id,
            limit=limit,
            page=page,
            sort=sort,
            desc=desc,
            filter=filter,
            minified=minified,
            include=include,
            request_options=request_options,
        )
        return _response.data
