

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.library_dto import LibraryDto
from ..types.library_update_dto_scan_interval import LibraryUpdateDtoScanInterval
from ..types.library_update_dto_series_cover import LibraryUpdateDtoSeriesCover
from .raw_client import AsyncRawLibrariesClient, RawLibrariesClient
from .types.library_creation_dto_scan_interval import LibraryCreationDtoScanInterval
from .types.library_creation_dto_series_cover import LibraryCreationDtoSeriesCover


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

    def get_libraries(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[LibraryDto]:
        """
        The libraries are filtered based on the current user's permissions

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LibraryDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.libraries.get_libraries()
        """
        _response = self._raw_client.get_libraries(request_options=request_options)
        return _response.data

    def add_library(
        self,
        *,
        analyze_dimensions: bool,
        convert_to_cbz: bool,
        empty_trash_after_scan: bool,
        hash_files: bool,
        hash_koreader: bool,
        hash_pages: bool,
        import_barcode_isbn: bool,
        import_comic_info_book: bool,
        import_comic_info_collection: bool,
        import_comic_info_read_list: bool,
        import_comic_info_series: bool,
        import_comic_info_series_append_volume: bool,
        import_epub_book: bool,
        import_epub_series: bool,
        import_local_artwork: bool,
        import_mylar_series: bool,
        name: str,
        repair_extensions: bool,
        root: str,
        scan_cbx: bool,
        scan_directory_exclusions: typing.Sequence[str],
        scan_epub: bool,
        scan_force_modified_time: bool,
        scan_interval: LibraryCreationDtoScanInterval,
        scan_on_startup: bool,
        scan_pdf: bool,
        series_cover: LibraryCreationDtoSeriesCover,
        oneshots_directory: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LibraryDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        analyze_dimensions : bool

        convert_to_cbz : bool

        empty_trash_after_scan : bool

        hash_files : bool

        hash_koreader : bool

        hash_pages : bool

        import_barcode_isbn : bool

        import_comic_info_book : bool

        import_comic_info_collection : bool

        import_comic_info_read_list : bool

        import_comic_info_series : bool

        import_comic_info_series_append_volume : bool

        import_epub_book : bool

        import_epub_series : bool

        import_local_artwork : bool

        import_mylar_series : bool

        name : str

        repair_extensions : bool

        root : str

        scan_cbx : bool

        scan_directory_exclusions : typing.Sequence[str]

        scan_epub : bool

        scan_force_modified_time : bool

        scan_interval : LibraryCreationDtoScanInterval

        scan_on_startup : bool

        scan_pdf : bool

        series_cover : LibraryCreationDtoSeriesCover

        oneshots_directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryDto
            OK

        Examples
        --------
        from fern.libraries import (
            LibraryCreationDtoScanInterval,
            LibraryCreationDtoSeriesCover,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.libraries.add_library(
            analyze_dimensions=True,
            convert_to_cbz=True,
            empty_trash_after_scan=True,
            hash_files=True,
            hash_koreader=True,
            hash_pages=True,
            import_barcode_isbn=True,
            import_comic_info_book=True,
            import_comic_info_collection=True,
            import_comic_info_read_list=True,
            import_comic_info_series=True,
            import_comic_info_series_append_volume=True,
            import_epub_book=True,
            import_epub_series=True,
            import_local_artwork=True,
            import_mylar_series=True,
            name="name",
            repair_extensions=True,
            root="root",
            scan_cbx=True,
            scan_directory_exclusions=["scanDirectoryExclusions"],
            scan_epub=True,
            scan_force_modified_time=True,
            scan_interval=LibraryCreationDtoScanInterval.DISABLED,
            scan_on_startup=True,
            scan_pdf=True,
            series_cover=LibraryCreationDtoSeriesCover.FIRST,
        )
        """
        _response = self._raw_client.add_library(
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
            oneshots_directory=oneshots_directory,
            request_options=request_options,
        )
        return _response.data

    def get_library_by_id(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LibraryDto:
        """
        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.libraries.get_library_by_id(
            library_id="libraryId",
        )
        """
        _response = self._raw_client.get_library_by_id(library_id, request_options=request_options)
        return _response.data

    def delete_library_by_id(self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

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
        client.libraries.delete_library_by_id(
            library_id="libraryId",
        )
        """
        _response = self._raw_client.delete_library_by_id(library_id, request_options=request_options)
        return _response.data

    def update_library_by_id(
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
        You can omit fields you don't want to update

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
        client.libraries.update_library_by_id(
            library_id="libraryId",
        )
        """
        _response = self._raw_client.update_library_by_id(
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

    def library_analyze(self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

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
        client.libraries.library_analyze(
            library_id="libraryId",
        )
        """
        _response = self._raw_client.library_analyze(library_id, request_options=request_options)
        return _response.data

    def library_empty_trash(self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

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
        client.libraries.library_empty_trash(
            library_id="libraryId",
        )
        """
        _response = self._raw_client.library_empty_trash(library_id, request_options=request_options)
        return _response.data

    def library_refresh_metadata(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

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
        client.libraries.library_refresh_metadata(
            library_id="libraryId",
        )
        """
        _response = self._raw_client.library_refresh_metadata(library_id, request_options=request_options)
        return _response.data

    def library_scan(
        self,
        library_id: str,
        *,
        deep: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        deep : typing.Optional[bool]

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
        client.libraries.library_scan(
            library_id="libraryId",
        )
        """
        _response = self._raw_client.library_scan(library_id, deep=deep, request_options=request_options)
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

    async def get_libraries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LibraryDto]:
        """
        The libraries are filtered based on the current user's permissions

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LibraryDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.libraries.get_libraries()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_libraries(request_options=request_options)
        return _response.data

    async def add_library(
        self,
        *,
        analyze_dimensions: bool,
        convert_to_cbz: bool,
        empty_trash_after_scan: bool,
        hash_files: bool,
        hash_koreader: bool,
        hash_pages: bool,
        import_barcode_isbn: bool,
        import_comic_info_book: bool,
        import_comic_info_collection: bool,
        import_comic_info_read_list: bool,
        import_comic_info_series: bool,
        import_comic_info_series_append_volume: bool,
        import_epub_book: bool,
        import_epub_series: bool,
        import_local_artwork: bool,
        import_mylar_series: bool,
        name: str,
        repair_extensions: bool,
        root: str,
        scan_cbx: bool,
        scan_directory_exclusions: typing.Sequence[str],
        scan_epub: bool,
        scan_force_modified_time: bool,
        scan_interval: LibraryCreationDtoScanInterval,
        scan_on_startup: bool,
        scan_pdf: bool,
        series_cover: LibraryCreationDtoSeriesCover,
        oneshots_directory: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LibraryDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        analyze_dimensions : bool

        convert_to_cbz : bool

        empty_trash_after_scan : bool

        hash_files : bool

        hash_koreader : bool

        hash_pages : bool

        import_barcode_isbn : bool

        import_comic_info_book : bool

        import_comic_info_collection : bool

        import_comic_info_read_list : bool

        import_comic_info_series : bool

        import_comic_info_series_append_volume : bool

        import_epub_book : bool

        import_epub_series : bool

        import_local_artwork : bool

        import_mylar_series : bool

        name : str

        repair_extensions : bool

        root : str

        scan_cbx : bool

        scan_directory_exclusions : typing.Sequence[str]

        scan_epub : bool

        scan_force_modified_time : bool

        scan_interval : LibraryCreationDtoScanInterval

        scan_on_startup : bool

        scan_pdf : bool

        series_cover : LibraryCreationDtoSeriesCover

        oneshots_directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryDto
            OK

        Examples
        --------
        import asyncio

        from fern.libraries import (
            LibraryCreationDtoScanInterval,
            LibraryCreationDtoSeriesCover,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.libraries.add_library(
                analyze_dimensions=True,
                convert_to_cbz=True,
                empty_trash_after_scan=True,
                hash_files=True,
                hash_koreader=True,
                hash_pages=True,
                import_barcode_isbn=True,
                import_comic_info_book=True,
                import_comic_info_collection=True,
                import_comic_info_read_list=True,
                import_comic_info_series=True,
                import_comic_info_series_append_volume=True,
                import_epub_book=True,
                import_epub_series=True,
                import_local_artwork=True,
                import_mylar_series=True,
                name="name",
                repair_extensions=True,
                root="root",
                scan_cbx=True,
                scan_directory_exclusions=["scanDirectoryExclusions"],
                scan_epub=True,
                scan_force_modified_time=True,
                scan_interval=LibraryCreationDtoScanInterval.DISABLED,
                scan_on_startup=True,
                scan_pdf=True,
                series_cover=LibraryCreationDtoSeriesCover.FIRST,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_library(
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
            oneshots_directory=oneshots_directory,
            request_options=request_options,
        )
        return _response.data

    async def get_library_by_id(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LibraryDto:
        """
        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LibraryDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.libraries.get_library_by_id(
                library_id="libraryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_library_by_id(library_id, request_options=request_options)
        return _response.data

    async def delete_library_by_id(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

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
            await client.libraries.delete_library_by_id(
                library_id="libraryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_library_by_id(library_id, request_options=request_options)
        return _response.data

    async def update_library_by_id(
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
        You can omit fields you don't want to update

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
            await client.libraries.update_library_by_id(
                library_id="libraryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_library_by_id(
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

    async def library_analyze(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

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
            await client.libraries.library_analyze(
                library_id="libraryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.library_analyze(library_id, request_options=request_options)
        return _response.data

    async def library_empty_trash(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

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
            await client.libraries.library_empty_trash(
                library_id="libraryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.library_empty_trash(library_id, request_options=request_options)
        return _response.data

    async def library_refresh_metadata(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

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
            await client.libraries.library_refresh_metadata(
                library_id="libraryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.library_refresh_metadata(library_id, request_options=request_options)
        return _response.data

    async def library_scan(
        self,
        library_id: str,
        *,
        deep: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        deep : typing.Optional[bool]

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
            await client.libraries.library_scan(
                library_id="libraryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.library_scan(library_id, deep=deep, request_options=request_options)
        return _response.data
