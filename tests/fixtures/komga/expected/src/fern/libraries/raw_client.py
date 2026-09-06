

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.library_dto import LibraryDto
from ..types.library_update_dto_scan_interval import LibraryUpdateDtoScanInterval
from ..types.library_update_dto_series_cover import LibraryUpdateDtoSeriesCover
from ..types.validation_error_response import ValidationErrorResponse
from .types.library_creation_dto_scan_interval import LibraryCreationDtoScanInterval
from .types.library_creation_dto_series_cover import LibraryCreationDtoSeriesCover
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLibrariesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_libraries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[LibraryDto]]:
        """
        The libraries are filtered based on the current user's permissions

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LibraryDto]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/libraries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LibraryDto],
                    parse_obj_as(
                        type_=typing.List[LibraryDto],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[LibraryDto]:
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
        HttpResponse[LibraryDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/libraries",
            method="POST",
            json={
                "analyzeDimensions": analyze_dimensions,
                "convertToCbz": convert_to_cbz,
                "emptyTrashAfterScan": empty_trash_after_scan,
                "hashFiles": hash_files,
                "hashKoreader": hash_koreader,
                "hashPages": hash_pages,
                "importBarcodeIsbn": import_barcode_isbn,
                "importComicInfoBook": import_comic_info_book,
                "importComicInfoCollection": import_comic_info_collection,
                "importComicInfoReadList": import_comic_info_read_list,
                "importComicInfoSeries": import_comic_info_series,
                "importComicInfoSeriesAppendVolume": import_comic_info_series_append_volume,
                "importEpubBook": import_epub_book,
                "importEpubSeries": import_epub_series,
                "importLocalArtwork": import_local_artwork,
                "importMylarSeries": import_mylar_series,
                "name": name,
                "oneshotsDirectory": oneshots_directory,
                "repairExtensions": repair_extensions,
                "root": root,
                "scanCbx": scan_cbx,
                "scanDirectoryExclusions": scan_directory_exclusions,
                "scanEpub": scan_epub,
                "scanForceModifiedTime": scan_force_modified_time,
                "scanInterval": scan_interval,
                "scanOnStartup": scan_on_startup,
                "scanPdf": scan_pdf,
                "seriesCover": series_cover,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LibraryDto,
                    parse_obj_as(
                        type_=LibraryDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_library_by_id(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LibraryDto]:
        """
        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LibraryDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LibraryDto,
                    parse_obj_as(
                        type_=LibraryDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_library_by_id(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}",
            method="PATCH",
            json={
                "analyzeDimensions": analyze_dimensions,
                "convertToCbz": convert_to_cbz,
                "emptyTrashAfterScan": empty_trash_after_scan,
                "hashFiles": hash_files,
                "hashKoreader": hash_koreader,
                "hashPages": hash_pages,
                "importBarcodeIsbn": import_barcode_isbn,
                "importComicInfoBook": import_comic_info_book,
                "importComicInfoCollection": import_comic_info_collection,
                "importComicInfoReadList": import_comic_info_read_list,
                "importComicInfoSeries": import_comic_info_series,
                "importComicInfoSeriesAppendVolume": import_comic_info_series_append_volume,
                "importEpubBook": import_epub_book,
                "importEpubSeries": import_epub_series,
                "importLocalArtwork": import_local_artwork,
                "importMylarSeries": import_mylar_series,
                "name": name,
                "oneshotsDirectory": oneshots_directory,
                "repairExtensions": repair_extensions,
                "root": root,
                "scanCbx": scan_cbx,
                "scanDirectoryExclusions": scan_directory_exclusions,
                "scanEpub": scan_epub,
                "scanForceModifiedTime": scan_force_modified_time,
                "scanInterval": scan_interval,
                "scanOnStartup": scan_on_startup,
                "scanPdf": scan_pdf,
                "seriesCover": series_cover,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def library_analyze(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}/analyze",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def library_empty_trash(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}/empty-trash",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def library_refresh_metadata(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}/metadata/refresh",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def library_scan(
        self,
        library_id: str,
        *,
        deep: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}/scan",
            method="POST",
            params={
                "deep": deep,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawLibrariesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_libraries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[LibraryDto]]:
        """
        The libraries are filtered based on the current user's permissions

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LibraryDto]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/libraries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LibraryDto],
                    parse_obj_as(
                        type_=typing.List[LibraryDto],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[LibraryDto]:
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
        AsyncHttpResponse[LibraryDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/libraries",
            method="POST",
            json={
                "analyzeDimensions": analyze_dimensions,
                "convertToCbz": convert_to_cbz,
                "emptyTrashAfterScan": empty_trash_after_scan,
                "hashFiles": hash_files,
                "hashKoreader": hash_koreader,
                "hashPages": hash_pages,
                "importBarcodeIsbn": import_barcode_isbn,
                "importComicInfoBook": import_comic_info_book,
                "importComicInfoCollection": import_comic_info_collection,
                "importComicInfoReadList": import_comic_info_read_list,
                "importComicInfoSeries": import_comic_info_series,
                "importComicInfoSeriesAppendVolume": import_comic_info_series_append_volume,
                "importEpubBook": import_epub_book,
                "importEpubSeries": import_epub_series,
                "importLocalArtwork": import_local_artwork,
                "importMylarSeries": import_mylar_series,
                "name": name,
                "oneshotsDirectory": oneshots_directory,
                "repairExtensions": repair_extensions,
                "root": root,
                "scanCbx": scan_cbx,
                "scanDirectoryExclusions": scan_directory_exclusions,
                "scanEpub": scan_epub,
                "scanForceModifiedTime": scan_force_modified_time,
                "scanInterval": scan_interval,
                "scanOnStartup": scan_on_startup,
                "scanPdf": scan_pdf,
                "seriesCover": series_cover,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LibraryDto,
                    parse_obj_as(
                        type_=LibraryDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_library_by_id(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LibraryDto]:
        """
        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LibraryDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LibraryDto,
                    parse_obj_as(
                        type_=LibraryDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_library_by_id(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}",
            method="PATCH",
            json={
                "analyzeDimensions": analyze_dimensions,
                "convertToCbz": convert_to_cbz,
                "emptyTrashAfterScan": empty_trash_after_scan,
                "hashFiles": hash_files,
                "hashKoreader": hash_koreader,
                "hashPages": hash_pages,
                "importBarcodeIsbn": import_barcode_isbn,
                "importComicInfoBook": import_comic_info_book,
                "importComicInfoCollection": import_comic_info_collection,
                "importComicInfoReadList": import_comic_info_read_list,
                "importComicInfoSeries": import_comic_info_series,
                "importComicInfoSeriesAppendVolume": import_comic_info_series_append_volume,
                "importEpubBook": import_epub_book,
                "importEpubSeries": import_epub_series,
                "importLocalArtwork": import_local_artwork,
                "importMylarSeries": import_mylar_series,
                "name": name,
                "oneshotsDirectory": oneshots_directory,
                "repairExtensions": repair_extensions,
                "root": root,
                "scanCbx": scan_cbx,
                "scanDirectoryExclusions": scan_directory_exclusions,
                "scanEpub": scan_epub,
                "scanForceModifiedTime": scan_force_modified_time,
                "scanInterval": scan_interval,
                "scanOnStartup": scan_on_startup,
                "scanPdf": scan_pdf,
                "seriesCover": series_cover,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def library_analyze(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}/analyze",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def library_empty_trash(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}/empty-trash",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def library_refresh_metadata(
        self, library_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        library_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}/metadata/refresh",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def library_scan(
        self,
        library_id: str,
        *,
        deep: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}/scan",
            method="POST",
            params={
                "deep": deep,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
