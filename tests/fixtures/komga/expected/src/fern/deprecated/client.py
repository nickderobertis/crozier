

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.author_dto import AuthorDto
from ..types.library_update_dto_scan_interval import LibraryUpdateDtoScanInterval
from ..types.library_update_dto_series_cover import LibraryUpdateDtoSeriesCover
from .raw_client import AsyncRawDeprecatedClient, RawDeprecatedClient


OMIT = typing.cast(typing.Any, ...)


class DeprecatedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeprecatedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeprecatedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeprecatedClient
        """
        return self._raw_client

    def get_age_ratings1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/age-ratings instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_age_ratings1()
        """
        _response = self._raw_client.get_age_ratings1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    def get_authors_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[str] = None,
        collection_id: typing.Optional[str] = None,
        series_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AuthorDto]:
        """
        Use GET /api/v2/authors instead. Deprecated since 1.20.0.

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[str]

        collection_id : typing.Optional[str]

        series_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AuthorDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_authors_deprecated()
        """
        _response = self._raw_client.get_authors_deprecated(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            request_options=request_options,
        )
        return _response.data

    def get_authors_names1(
        self, *, search: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Use GET /v2/authors/names instead. Deprecated since 1.26.0

        Parameters
        ----------
        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_authors_names1()
        """
        _response = self._raw_client.get_authors_names1(search=search, request_options=request_options)
        return _response.data

    def get_authors_roles1(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Use GET /v2/authors/roles instead. Deprecated since 1.26.0

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_authors_roles1()
        """
        _response = self._raw_client.get_authors_roles1(request_options=request_options)
        return _response.data

    def get_genres1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/genres instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_genres1()
        """
        _response = self._raw_client.get_genres1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    def get_languages1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/languages instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_languages1()
        """
        _response = self._raw_client.get_languages1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    def update_library_by_id_deprecated(
        self,
        library_id: str,
        *,
        analyze_dimensions: typing.Optional[bool] = OMIT,
        convert_to_cbz: typing.Optional[bool] = OMIT,
        empty_trash_after_scan: typing.Optional[bool] = OMIT,
        hash_files: typing.Optional[bool] = OMIT,
        hash_koreader: typing.Optional[bool] = OMIT,
        hash_pages: typing.Optional[bool] = OMIT,
        import_barcode_isbn: typing.Optional[bool] = OMIT,
        import_comic_info_book: typing.Optional[bool] = OMIT,
        import_comic_info_collection: typing.Optional[bool] = OMIT,
        import_comic_info_read_list: typing.Optional[bool] = OMIT,
        import_comic_info_series: typing.Optional[bool] = OMIT,
        import_comic_info_series_append_volume: typing.Optional[bool] = OMIT,
        import_epub_book: typing.Optional[bool] = OMIT,
        import_epub_series: typing.Optional[bool] = OMIT,
        import_local_artwork: typing.Optional[bool] = OMIT,
        import_mylar_series: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        oneshots_directory: typing.Optional[str] = OMIT,
        repair_extensions: typing.Optional[bool] = OMIT,
        root: typing.Optional[str] = OMIT,
        scan_cbx: typing.Optional[bool] = OMIT,
        scan_directory_exclusions: typing.Optional[typing.Sequence[str]] = OMIT,
        scan_epub: typing.Optional[bool] = OMIT,
        scan_force_modified_time: typing.Optional[bool] = OMIT,
        scan_interval: typing.Optional[LibraryUpdateDtoScanInterval] = OMIT,
        scan_on_startup: typing.Optional[bool] = OMIT,
        scan_pdf: typing.Optional[bool] = OMIT,
        series_cover: typing.Optional[LibraryUpdateDtoSeriesCover] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Use PATCH /api/v1/libraries/{libraryId} instead. Deprecated since 1.3.0.

        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        analyze_dimensions : typing.Optional[bool]

        convert_to_cbz : typing.Optional[bool]

        empty_trash_after_scan : typing.Optional[bool]

        hash_files : typing.Optional[bool]

        hash_koreader : typing.Optional[bool]

        hash_pages : typing.Optional[bool]

        import_barcode_isbn : typing.Optional[bool]

        import_comic_info_book : typing.Optional[bool]

        import_comic_info_collection : typing.Optional[bool]

        import_comic_info_read_list : typing.Optional[bool]

        import_comic_info_series : typing.Optional[bool]

        import_comic_info_series_append_volume : typing.Optional[bool]

        import_epub_book : typing.Optional[bool]

        import_epub_series : typing.Optional[bool]

        import_local_artwork : typing.Optional[bool]

        import_mylar_series : typing.Optional[bool]

        name : typing.Optional[str]

        oneshots_directory : typing.Optional[str]

        repair_extensions : typing.Optional[bool]

        root : typing.Optional[str]

        scan_cbx : typing.Optional[bool]

        scan_directory_exclusions : typing.Optional[typing.Sequence[str]]

        scan_epub : typing.Optional[bool]

        scan_force_modified_time : typing.Optional[bool]

        scan_interval : typing.Optional[LibraryUpdateDtoScanInterval]

        scan_on_startup : typing.Optional[bool]

        scan_pdf : typing.Optional[bool]

        series_cover : typing.Optional[LibraryUpdateDtoSeriesCover]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.update_library_by_id_deprecated(
            library_id="libraryId",
        )
        """
        _response = self._raw_client.update_library_by_id_deprecated(
            library_id,
            analyze_dimensions=analyze_dimensions,
            convert_to_cbz=convert_to_cbz,
            empty_trash_after_scan=empty_trash_after_scan,
            hash_files=hash_files,
            hash_koreader=hash_koreader,
            hash_pages=hash_pages,
            import_barcode_isbn=import_barcode_isbn,
            import_comic_info_book=import_comic_info_book,
            import_comic_info_collection=import_comic_info_collection,
            import_comic_info_read_list=import_comic_info_read_list,
            import_comic_info_series=import_comic_info_series,
            import_comic_info_series_append_volume=import_comic_info_series_append_volume,
            import_epub_book=import_epub_book,
            import_epub_series=import_epub_series,
            import_local_artwork=import_local_artwork,
            import_mylar_series=import_mylar_series,
            name=name,
            oneshots_directory=oneshots_directory,
            repair_extensions=repair_extensions,
            root=root,
            scan_cbx=scan_cbx,
            scan_directory_exclusions=scan_directory_exclusions,
            scan_epub=scan_epub,
            scan_force_modified_time=scan_force_modified_time,
            scan_interval=scan_interval,
            scan_on_startup=scan_on_startup,
            scan_pdf=scan_pdf,
            series_cover=series_cover,
            request_options=request_options,
        )
        return _response.data

    def get_publishers1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/publishers instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_publishers1()
        """
        _response = self._raw_client.get_publishers1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    def get_series_release_dates(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/series/release-years instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_series_release_dates()
        """
        _response = self._raw_client.get_series_release_dates(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    def get_sharing_labels1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/sharing-labels instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_sharing_labels1()
        """
        _response = self._raw_client.get_sharing_labels1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    def get_tags1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/tags instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_tags1()
        """
        _response = self._raw_client.get_tags1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    def get_book_tags(
        self,
        *,
        series_id: typing.Optional[str] = None,
        readlist_id: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/tags instead. Deprecated since 1.26.0

        Parameters
        ----------
        series_id : typing.Optional[str]

        readlist_id : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_book_tags()
        """
        _response = self._raw_client.get_book_tags(
            series_id=series_id, readlist_id=readlist_id, library_id=library_id, request_options=request_options
        )
        return _response.data

    def get_series_tags(
        self,
        *,
        library_id: typing.Optional[str] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/tags instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[str]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deprecated.get_series_tags()
        """
        _response = self._raw_client.get_series_tags(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data


class AsyncDeprecatedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeprecatedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeprecatedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeprecatedClient
        """
        return self._raw_client

    async def get_age_ratings1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/age-ratings instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_age_ratings1()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_age_ratings1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    async def get_authors_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[str] = None,
        collection_id: typing.Optional[str] = None,
        series_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AuthorDto]:
        """
        Use GET /api/v2/authors instead. Deprecated since 1.20.0.

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[str]

        collection_id : typing.Optional[str]

        series_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AuthorDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_authors_deprecated()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authors_deprecated(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            series_id=series_id,
            request_options=request_options,
        )
        return _response.data

    async def get_authors_names1(
        self, *, search: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Use GET /v2/authors/names instead. Deprecated since 1.26.0

        Parameters
        ----------
        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_authors_names1()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authors_names1(search=search, request_options=request_options)
        return _response.data

    async def get_authors_roles1(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Use GET /v2/authors/roles instead. Deprecated since 1.26.0

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_authors_roles1()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authors_roles1(request_options=request_options)
        return _response.data

    async def get_genres1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/genres instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_genres1()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_genres1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    async def get_languages1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/languages instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_languages1()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_languages1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    async def update_library_by_id_deprecated(
        self,
        library_id: str,
        *,
        analyze_dimensions: typing.Optional[bool] = OMIT,
        convert_to_cbz: typing.Optional[bool] = OMIT,
        empty_trash_after_scan: typing.Optional[bool] = OMIT,
        hash_files: typing.Optional[bool] = OMIT,
        hash_koreader: typing.Optional[bool] = OMIT,
        hash_pages: typing.Optional[bool] = OMIT,
        import_barcode_isbn: typing.Optional[bool] = OMIT,
        import_comic_info_book: typing.Optional[bool] = OMIT,
        import_comic_info_collection: typing.Optional[bool] = OMIT,
        import_comic_info_read_list: typing.Optional[bool] = OMIT,
        import_comic_info_series: typing.Optional[bool] = OMIT,
        import_comic_info_series_append_volume: typing.Optional[bool] = OMIT,
        import_epub_book: typing.Optional[bool] = OMIT,
        import_epub_series: typing.Optional[bool] = OMIT,
        import_local_artwork: typing.Optional[bool] = OMIT,
        import_mylar_series: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        oneshots_directory: typing.Optional[str] = OMIT,
        repair_extensions: typing.Optional[bool] = OMIT,
        root: typing.Optional[str] = OMIT,
        scan_cbx: typing.Optional[bool] = OMIT,
        scan_directory_exclusions: typing.Optional[typing.Sequence[str]] = OMIT,
        scan_epub: typing.Optional[bool] = OMIT,
        scan_force_modified_time: typing.Optional[bool] = OMIT,
        scan_interval: typing.Optional[LibraryUpdateDtoScanInterval] = OMIT,
        scan_on_startup: typing.Optional[bool] = OMIT,
        scan_pdf: typing.Optional[bool] = OMIT,
        series_cover: typing.Optional[LibraryUpdateDtoSeriesCover] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Use PATCH /api/v1/libraries/{libraryId} instead. Deprecated since 1.3.0.

        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        analyze_dimensions : typing.Optional[bool]

        convert_to_cbz : typing.Optional[bool]

        empty_trash_after_scan : typing.Optional[bool]

        hash_files : typing.Optional[bool]

        hash_koreader : typing.Optional[bool]

        hash_pages : typing.Optional[bool]

        import_barcode_isbn : typing.Optional[bool]

        import_comic_info_book : typing.Optional[bool]

        import_comic_info_collection : typing.Optional[bool]

        import_comic_info_read_list : typing.Optional[bool]

        import_comic_info_series : typing.Optional[bool]

        import_comic_info_series_append_volume : typing.Optional[bool]

        import_epub_book : typing.Optional[bool]

        import_epub_series : typing.Optional[bool]

        import_local_artwork : typing.Optional[bool]

        import_mylar_series : typing.Optional[bool]

        name : typing.Optional[str]

        oneshots_directory : typing.Optional[str]

        repair_extensions : typing.Optional[bool]

        root : typing.Optional[str]

        scan_cbx : typing.Optional[bool]

        scan_directory_exclusions : typing.Optional[typing.Sequence[str]]

        scan_epub : typing.Optional[bool]

        scan_force_modified_time : typing.Optional[bool]

        scan_interval : typing.Optional[LibraryUpdateDtoScanInterval]

        scan_on_startup : typing.Optional[bool]

        scan_pdf : typing.Optional[bool]

        series_cover : typing.Optional[LibraryUpdateDtoSeriesCover]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.update_library_by_id_deprecated(
                library_id="libraryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_library_by_id_deprecated(
            library_id,
            analyze_dimensions=analyze_dimensions,
            convert_to_cbz=convert_to_cbz,
            empty_trash_after_scan=empty_trash_after_scan,
            hash_files=hash_files,
            hash_koreader=hash_koreader,
            hash_pages=hash_pages,
            import_barcode_isbn=import_barcode_isbn,
            import_comic_info_book=import_comic_info_book,
            import_comic_info_collection=import_comic_info_collection,
            import_comic_info_read_list=import_comic_info_read_list,
            import_comic_info_series=import_comic_info_series,
            import_comic_info_series_append_volume=import_comic_info_series_append_volume,
            import_epub_book=import_epub_book,
            import_epub_series=import_epub_series,
            import_local_artwork=import_local_artwork,
            import_mylar_series=import_mylar_series,
            name=name,
            oneshots_directory=oneshots_directory,
            repair_extensions=repair_extensions,
            root=root,
            scan_cbx=scan_cbx,
            scan_directory_exclusions=scan_directory_exclusions,
            scan_epub=scan_epub,
            scan_force_modified_time=scan_force_modified_time,
            scan_interval=scan_interval,
            scan_on_startup=scan_on_startup,
            scan_pdf=scan_pdf,
            series_cover=series_cover,
            request_options=request_options,
        )
        return _response.data

    async def get_publishers1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/publishers instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_publishers1()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_publishers1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    async def get_series_release_dates(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/series/release-years instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_series_release_dates()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_release_dates(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    async def get_sharing_labels1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/sharing-labels instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_sharing_labels1()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sharing_labels1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    async def get_tags1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/tags instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_tags1()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tags1(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data

    async def get_book_tags(
        self,
        *,
        series_id: typing.Optional[str] = None,
        readlist_id: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/tags instead. Deprecated since 1.26.0

        Parameters
        ----------
        series_id : typing.Optional[str]

        readlist_id : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_book_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_tags(
            series_id=series_id, readlist_id=readlist_id, library_id=library_id, request_options=request_options
        )
        return _response.data

    async def get_series_tags(
        self,
        *,
        library_id: typing.Optional[str] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Use GET /v2/tags instead. Deprecated since 1.26.0

        Parameters
        ----------
        library_id : typing.Optional[str]

        collection_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deprecated.get_series_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_tags(
            library_id=library_id, collection_id=collection_id, request_options=request_options
        )
        return _response.data
