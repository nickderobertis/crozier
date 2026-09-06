

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
from ..types.author_dto import AuthorDto
from ..types.library_update_dto_scan_interval import LibraryUpdateDtoScanInterval
from ..types.library_update_dto_series_cover import LibraryUpdateDtoSeriesCover
from ..types.validation_error_response import ValidationErrorResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDeprecatedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_age_ratings1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/age-ratings",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_authors_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[str] = None,
        collection_id: typing.Optional[str] = None,
        series_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[AuthorDto]]:
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
        HttpResponse[typing.List[AuthorDto]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/authors",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AuthorDto],
                    parse_obj_as(
                        type_=typing.List[AuthorDto],
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

    def get_authors_names1(
        self, *, search: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Use GET /v2/authors/names instead. Deprecated since 1.26.0

        Parameters
        ----------
        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/authors/names",
            method="GET",
            params={
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_authors_roles1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Use GET /v2/authors/roles instead. Deprecated since 1.26.0

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/authors/roles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_genres1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/genres",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_languages1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/languages",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}",
            method="PUT",
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

    def get_publishers1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/publishers",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_series_release_dates(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/series/release-dates",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_sharing_labels1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/sharing-labels",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_tags1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/tags",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_book_tags(
        self,
        *,
        series_id: typing.Optional[str] = None,
        readlist_id: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/tags/book",
            method="GET",
            params={
                "series_id": series_id,
                "readlist_id": readlist_id,
                "library_id": library_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def get_series_tags(
        self,
        *,
        library_id: typing.Optional[str] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/tags/series",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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


class AsyncRawDeprecatedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_age_ratings1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/age-ratings",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_authors_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[str] = None,
        collection_id: typing.Optional[str] = None,
        series_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[AuthorDto]]:
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
        AsyncHttpResponse[typing.List[AuthorDto]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/authors",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "series_id": series_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AuthorDto],
                    parse_obj_as(
                        type_=typing.List[AuthorDto],
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

    async def get_authors_names1(
        self, *, search: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Use GET /v2/authors/names instead. Deprecated since 1.26.0

        Parameters
        ----------
        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/authors/names",
            method="GET",
            params={
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_authors_roles1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Use GET /v2/authors/roles instead. Deprecated since 1.26.0

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/authors/roles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_genres1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/genres",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_languages1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/languages",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/libraries/{encode_path_param(library_id)}",
            method="PUT",
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

    async def get_publishers1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/publishers",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_series_release_dates(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/series/release-dates",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_sharing_labels1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/sharing-labels",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_tags1(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/tags",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_book_tags(
        self,
        *,
        series_id: typing.Optional[str] = None,
        readlist_id: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/tags/book",
            method="GET",
            params={
                "series_id": series_id,
                "readlist_id": readlist_id,
                "library_id": library_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def get_series_tags(
        self,
        *,
        library_id: typing.Optional[str] = None,
        collection_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/tags/series",
            method="GET",
            params={
                "library_id": library_id,
                "collection_id": collection_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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
