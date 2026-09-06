

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.alternate_title_update_dto import AlternateTitleUpdateDto
from ..types.collection_dto import CollectionDto
from ..types.group_count_dto import GroupCountDto
from ..types.page_book_dto import PageBookDto
from ..types.page_series_dto import PageSeriesDto
from ..types.search_condition_series import SearchConditionSeries
from ..types.series_dto import SeriesDto
from ..types.streaming_response_body import StreamingResponseBody
from ..types.validation_error_response import ValidationErrorResponse
from ..types.web_link_update_dto import WebLinkUpdateDto
from .types.get_books_by_series_id_request_media_status_item import GetBooksBySeriesIdRequestMediaStatusItem
from .types.get_books_by_series_id_request_read_status_item import GetBooksBySeriesIdRequestReadStatusItem
from .types.get_series_alphabetical_groups_deprecated_request_read_status_item import (
    GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem,
)
from .types.get_series_alphabetical_groups_deprecated_request_status_item import (
    GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem,
)
from .types.get_series_deprecated_request_read_status_item import GetSeriesDeprecatedRequestReadStatusItem
from .types.get_series_deprecated_request_status_item import GetSeriesDeprecatedRequestStatusItem
from .types.series_metadata_update_dto_reading_direction import SeriesMetadataUpdateDtoReadingDirection
from .types.series_metadata_update_dto_status import SeriesMetadataUpdateDtoStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSeriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_series_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[
            typing.Union[GetSeriesDeprecatedRequestStatusItem, typing.Sequence[GetSeriesDeprecatedRequestStatusItem]]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetSeriesDeprecatedRequestReadStatusItem, typing.Sequence[GetSeriesDeprecatedRequestReadStatusItem]
            ]
        ] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        language: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        genre: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        age_rating: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        release_year: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sharing_label: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        complete: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        search_regex: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageSeriesDto]:
        """
        Use POST /api/v1/series/list instead. Deprecated since 1.19.0.

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        status : typing.Optional[typing.Union[GetSeriesDeprecatedRequestStatusItem, typing.Sequence[GetSeriesDeprecatedRequestStatusItem]]]

        read_status : typing.Optional[typing.Union[GetSeriesDeprecatedRequestReadStatusItem, typing.Sequence[GetSeriesDeprecatedRequestReadStatusItem]]]

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        language : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        genre : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        age_rating : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        release_year : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sharing_label : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        complete : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        search_regex : typing.Optional[str]
            Search by regex criteria, in the form: regex,field. Supported fields are TITLE and TITLE_SORT.

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageSeriesDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/series",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "status": status,
                "read_status": read_status,
                "publisher": publisher,
                "language": language,
                "genre": genre,
                "tag": tag,
                "age_rating": age_rating,
                "release_year": release_year,
                "sharing_label": sharing_label,
                "deleted": deleted,
                "complete": complete,
                "oneshot": oneshot,
                "unpaged": unpaged,
                "search_regex": search_regex,
                "page": page,
                "size": size,
                "sort": sort,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    def get_series_alphabetical_groups_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[
            typing.Union[
                GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem,
                typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem],
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem,
                typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem],
            ]
        ] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        language: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        genre: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        age_rating: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        release_year: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sharing_label: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        complete: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        search_regex: typing.Optional[str] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GroupCountDto]]:
        """
        Use POST /api/v1/series/list/alphabetical-groups instead. Deprecated since 1.19.0.

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        status : typing.Optional[typing.Union[GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem, typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem]]]

        read_status : typing.Optional[typing.Union[GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem, typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem]]]

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        language : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        genre : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        age_rating : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        release_year : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sharing_label : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        complete : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        search_regex : typing.Optional[str]
            Search by regex criteria, in the form: regex,field. Supported fields are TITLE and TITLE_SORT.

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GroupCountDto]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/series/alphabetical-groups",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "status": status,
                "read_status": read_status,
                "publisher": publisher,
                "language": language,
                "genre": genre,
                "tag": tag,
                "age_rating": age_rating,
                "release_year": release_year,
                "sharing_label": sharing_label,
                "deleted": deleted,
                "complete": complete,
                "oneshot": oneshot,
                "search_regex": search_regex,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GroupCountDto],
                    parse_obj_as(
                        type_=typing.List[GroupCountDto],
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

    def get_series_latest(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageSeriesDto]:
        """
        Return recently added or updated series.

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageSeriesDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/series/latest",
            method="GET",
            params={
                "library_id": library_id,
                "deleted": deleted,
                "oneshot": oneshot,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    def get_series(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        condition: typing.Optional[SearchConditionSeries] = OMIT,
        full_text_search: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageSeriesDto]:
        """
        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        condition : typing.Optional[SearchConditionSeries]

        full_text_search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageSeriesDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/series/list",
            method="POST",
            params={
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "sort": sort,
            },
            json={
                "condition": convert_and_respect_annotation_metadata(
                    object_=condition, annotation=SearchConditionSeries, direction="write"
                ),
                "fullTextSearch": full_text_search,
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
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    def get_series_alphabetical_groups(
        self,
        *,
        condition: typing.Optional[SearchConditionSeries] = OMIT,
        full_text_search: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GroupCountDto]]:
        """
        List series grouped by the first character of their sort title.

        Parameters
        ----------
        condition : typing.Optional[SearchConditionSeries]

        full_text_search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GroupCountDto]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/series/list/alphabetical-groups",
            method="POST",
            json={
                "condition": convert_and_respect_annotation_metadata(
                    object_=condition, annotation=SearchConditionSeries, direction="write"
                ),
                "fullTextSearch": full_text_search,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GroupCountDto],
                    parse_obj_as(
                        type_=typing.List[GroupCountDto],
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

    def get_series_new(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageSeriesDto]:
        """
        Return newly added series.

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageSeriesDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/series/new",
            method="GET",
            params={
                "library_id": library_id,
                "deleted": deleted,
                "oneshot": oneshot,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    def get_series_updated(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageSeriesDto]:
        """
        Return recently updated series, but not newly added ones.

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageSeriesDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/series/updated",
            method="GET",
            params={
                "library_id": library_id,
                "deleted": deleted,
                "oneshot": oneshot,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    def get_series_by_id(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SeriesDto]:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SeriesDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeriesDto,
                    parse_obj_as(
                        type_=SeriesDto,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def analyze(self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/analyze",
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

    def get_books_by_series_id(
        self,
        series_id: str,
        *,
        media_status: typing.Optional[
            typing.Union[
                GetBooksBySeriesIdRequestMediaStatusItem, typing.Sequence[GetBooksBySeriesIdRequestMediaStatusItem]
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetBooksBySeriesIdRequestReadStatusItem, typing.Sequence[GetBooksBySeriesIdRequestReadStatusItem]
            ]
        ] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageBookDto]:
        """
        Use POST /api/v1/books/list instead. Deprecated since 1.19.0.

        Parameters
        ----------
        series_id : str

        media_status : typing.Optional[typing.Union[GetBooksBySeriesIdRequestMediaStatusItem, typing.Sequence[GetBooksBySeriesIdRequestMediaStatusItem]]]

        read_status : typing.Optional[typing.Union[GetBooksBySeriesIdRequestReadStatusItem, typing.Sequence[GetBooksBySeriesIdRequestReadStatusItem]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageBookDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/books",
            method="GET",
            params={
                "media_status": media_status,
                "read_status": read_status,
                "tag": tag,
                "deleted": deleted,
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "sort": sort,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageBookDto,
                    parse_obj_as(
                        type_=PageBookDto,
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

    def get_collections_by_series_id(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[CollectionDto]]:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CollectionDto]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CollectionDto],
                    parse_obj_as(
                        type_=typing.List[CollectionDto],
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

    def download_series_as_zip(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StreamingResponseBody]:
        """
        Download the whole series as a ZIP file.

        Required role: **FILE_DOWNLOAD**

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StreamingResponseBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/file",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamingResponseBody,
                    parse_obj_as(
                        type_=StreamingResponseBody,
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

    def delete_series_file(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete all of the series' books files on disk.

        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/file",
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

    def update_series_metadata(
        self,
        series_id: str,
        *,
        age_rating: typing.Optional[int] = OMIT,
        age_rating_lock: typing.Optional[bool] = OMIT,
        alternate_titles: typing.Optional[typing.Sequence[AlternateTitleUpdateDto]] = OMIT,
        alternate_titles_lock: typing.Optional[bool] = OMIT,
        genres: typing.Optional[typing.Sequence[str]] = OMIT,
        genres_lock: typing.Optional[bool] = OMIT,
        language: typing.Optional[str] = OMIT,
        language_lock: typing.Optional[bool] = OMIT,
        links: typing.Optional[typing.Sequence[WebLinkUpdateDto]] = OMIT,
        links_lock: typing.Optional[bool] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        publisher_lock: typing.Optional[bool] = OMIT,
        reading_direction: typing.Optional[SeriesMetadataUpdateDtoReadingDirection] = OMIT,
        reading_direction_lock: typing.Optional[bool] = OMIT,
        sharing_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        sharing_labels_lock: typing.Optional[bool] = OMIT,
        status: typing.Optional[SeriesMetadataUpdateDtoStatus] = OMIT,
        status_lock: typing.Optional[bool] = OMIT,
        summary: typing.Optional[str] = OMIT,
        summary_lock: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tags_lock: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        title_lock: typing.Optional[bool] = OMIT,
        title_sort: typing.Optional[str] = OMIT,
        title_sort_lock: typing.Optional[bool] = OMIT,
        total_book_count: typing.Optional[int] = OMIT,
        total_book_count_lock: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        age_rating : typing.Optional[int]

        age_rating_lock : typing.Optional[bool]

        alternate_titles : typing.Optional[typing.Sequence[AlternateTitleUpdateDto]]

        alternate_titles_lock : typing.Optional[bool]

        genres : typing.Optional[typing.Sequence[str]]

        genres_lock : typing.Optional[bool]

        language : typing.Optional[str]

        language_lock : typing.Optional[bool]

        links : typing.Optional[typing.Sequence[WebLinkUpdateDto]]

        links_lock : typing.Optional[bool]

        publisher : typing.Optional[str]

        publisher_lock : typing.Optional[bool]

        reading_direction : typing.Optional[SeriesMetadataUpdateDtoReadingDirection]

        reading_direction_lock : typing.Optional[bool]

        sharing_labels : typing.Optional[typing.Sequence[str]]

        sharing_labels_lock : typing.Optional[bool]

        status : typing.Optional[SeriesMetadataUpdateDtoStatus]

        status_lock : typing.Optional[bool]

        summary : typing.Optional[str]

        summary_lock : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        tags_lock : typing.Optional[bool]

        title : typing.Optional[str]

        title_lock : typing.Optional[bool]

        title_sort : typing.Optional[str]

        title_sort_lock : typing.Optional[bool]

        total_book_count : typing.Optional[int]

        total_book_count_lock : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/metadata",
            method="PATCH",
            json={
                "ageRating": age_rating,
                "ageRatingLock": age_rating_lock,
                "alternateTitles": convert_and_respect_annotation_metadata(
                    object_=alternate_titles, annotation=typing.Sequence[AlternateTitleUpdateDto], direction="write"
                ),
                "alternateTitlesLock": alternate_titles_lock,
                "genres": genres,
                "genresLock": genres_lock,
                "language": language,
                "languageLock": language_lock,
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=typing.Sequence[WebLinkUpdateDto], direction="write"
                ),
                "linksLock": links_lock,
                "publisher": publisher,
                "publisherLock": publisher_lock,
                "readingDirection": reading_direction,
                "readingDirectionLock": reading_direction_lock,
                "sharingLabels": sharing_labels,
                "sharingLabelsLock": sharing_labels_lock,
                "status": status,
                "statusLock": status_lock,
                "summary": summary,
                "summaryLock": summary_lock,
                "tags": tags,
                "tagsLock": tags_lock,
                "title": title,
                "titleLock": title_lock,
                "titleSort": title_sort,
                "titleSortLock": title_sort_lock,
                "totalBookCount": total_book_count,
                "totalBookCountLock": total_book_count_lock,
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

    def refresh_metadata(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/metadata/refresh",
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

    def mark_series_as_read(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Mark all book for series as read

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/read-progress",
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

    def mark_series_as_unread(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Mark all book for series as unread

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/read-progress",
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


class AsyncRawSeriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_series_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[
            typing.Union[GetSeriesDeprecatedRequestStatusItem, typing.Sequence[GetSeriesDeprecatedRequestStatusItem]]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetSeriesDeprecatedRequestReadStatusItem, typing.Sequence[GetSeriesDeprecatedRequestReadStatusItem]
            ]
        ] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        language: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        genre: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        age_rating: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        release_year: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sharing_label: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        complete: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        search_regex: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageSeriesDto]:
        """
        Use POST /api/v1/series/list instead. Deprecated since 1.19.0.

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        status : typing.Optional[typing.Union[GetSeriesDeprecatedRequestStatusItem, typing.Sequence[GetSeriesDeprecatedRequestStatusItem]]]

        read_status : typing.Optional[typing.Union[GetSeriesDeprecatedRequestReadStatusItem, typing.Sequence[GetSeriesDeprecatedRequestReadStatusItem]]]

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        language : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        genre : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        age_rating : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        release_year : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sharing_label : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        complete : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        search_regex : typing.Optional[str]
            Search by regex criteria, in the form: regex,field. Supported fields are TITLE and TITLE_SORT.

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageSeriesDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/series",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "status": status,
                "read_status": read_status,
                "publisher": publisher,
                "language": language,
                "genre": genre,
                "tag": tag,
                "age_rating": age_rating,
                "release_year": release_year,
                "sharing_label": sharing_label,
                "deleted": deleted,
                "complete": complete,
                "oneshot": oneshot,
                "unpaged": unpaged,
                "search_regex": search_regex,
                "page": page,
                "size": size,
                "sort": sort,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    async def get_series_alphabetical_groups_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        collection_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[
            typing.Union[
                GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem,
                typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem],
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem,
                typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem],
            ]
        ] = None,
        publisher: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        language: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        genre: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        age_rating: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        release_year: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sharing_label: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        complete: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        search_regex: typing.Optional[str] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GroupCountDto]]:
        """
        Use POST /api/v1/series/list/alphabetical-groups instead. Deprecated since 1.19.0.

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        collection_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        status : typing.Optional[typing.Union[GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem, typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem]]]

        read_status : typing.Optional[typing.Union[GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem, typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem]]]

        publisher : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        language : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        genre : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        age_rating : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        release_year : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sharing_label : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        complete : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        search_regex : typing.Optional[str]
            Search by regex criteria, in the form: regex,field. Supported fields are TITLE and TITLE_SORT.

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GroupCountDto]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/series/alphabetical-groups",
            method="GET",
            params={
                "search": search,
                "library_id": library_id,
                "collection_id": collection_id,
                "status": status,
                "read_status": read_status,
                "publisher": publisher,
                "language": language,
                "genre": genre,
                "tag": tag,
                "age_rating": age_rating,
                "release_year": release_year,
                "sharing_label": sharing_label,
                "deleted": deleted,
                "complete": complete,
                "oneshot": oneshot,
                "search_regex": search_regex,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GroupCountDto],
                    parse_obj_as(
                        type_=typing.List[GroupCountDto],
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

    async def get_series_latest(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageSeriesDto]:
        """
        Return recently added or updated series.

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageSeriesDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/series/latest",
            method="GET",
            params={
                "library_id": library_id,
                "deleted": deleted,
                "oneshot": oneshot,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    async def get_series(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        condition: typing.Optional[SearchConditionSeries] = OMIT,
        full_text_search: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageSeriesDto]:
        """
        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        condition : typing.Optional[SearchConditionSeries]

        full_text_search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageSeriesDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/series/list",
            method="POST",
            params={
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "sort": sort,
            },
            json={
                "condition": convert_and_respect_annotation_metadata(
                    object_=condition, annotation=SearchConditionSeries, direction="write"
                ),
                "fullTextSearch": full_text_search,
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
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    async def get_series_alphabetical_groups(
        self,
        *,
        condition: typing.Optional[SearchConditionSeries] = OMIT,
        full_text_search: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GroupCountDto]]:
        """
        List series grouped by the first character of their sort title.

        Parameters
        ----------
        condition : typing.Optional[SearchConditionSeries]

        full_text_search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GroupCountDto]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/series/list/alphabetical-groups",
            method="POST",
            json={
                "condition": convert_and_respect_annotation_metadata(
                    object_=condition, annotation=SearchConditionSeries, direction="write"
                ),
                "fullTextSearch": full_text_search,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GroupCountDto],
                    parse_obj_as(
                        type_=typing.List[GroupCountDto],
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

    async def get_series_new(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageSeriesDto]:
        """
        Return newly added series.

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageSeriesDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/series/new",
            method="GET",
            params={
                "library_id": library_id,
                "deleted": deleted,
                "oneshot": oneshot,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    async def get_series_updated(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        oneshot: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageSeriesDto]:
        """
        Return recently updated series, but not newly added ones.

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        oneshot : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageSeriesDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/series/updated",
            method="GET",
            params={
                "library_id": library_id,
                "deleted": deleted,
                "oneshot": oneshot,
                "unpaged": unpaged,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageSeriesDto,
                    parse_obj_as(
                        type_=PageSeriesDto,
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

    async def get_series_by_id(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SeriesDto]:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SeriesDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SeriesDto,
                    parse_obj_as(
                        type_=SeriesDto,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def analyze(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/analyze",
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

    async def get_books_by_series_id(
        self,
        series_id: str,
        *,
        media_status: typing.Optional[
            typing.Union[
                GetBooksBySeriesIdRequestMediaStatusItem, typing.Sequence[GetBooksBySeriesIdRequestMediaStatusItem]
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetBooksBySeriesIdRequestReadStatusItem, typing.Sequence[GetBooksBySeriesIdRequestReadStatusItem]
            ]
        ] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        deleted: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageBookDto]:
        """
        Use POST /api/v1/books/list instead. Deprecated since 1.19.0.

        Parameters
        ----------
        series_id : str

        media_status : typing.Optional[typing.Union[GetBooksBySeriesIdRequestMediaStatusItem, typing.Sequence[GetBooksBySeriesIdRequestMediaStatusItem]]]

        read_status : typing.Optional[typing.Union[GetBooksBySeriesIdRequestReadStatusItem, typing.Sequence[GetBooksBySeriesIdRequestReadStatusItem]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        deleted : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        author : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Author criteria in the format: name,role. Multiple author criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageBookDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/books",
            method="GET",
            params={
                "media_status": media_status,
                "read_status": read_status,
                "tag": tag,
                "deleted": deleted,
                "unpaged": unpaged,
                "page": page,
                "size": size,
                "sort": sort,
                "author": author,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageBookDto,
                    parse_obj_as(
                        type_=PageBookDto,
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

    async def get_collections_by_series_id(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[CollectionDto]]:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CollectionDto]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CollectionDto],
                    parse_obj_as(
                        type_=typing.List[CollectionDto],
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

    async def download_series_as_zip(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StreamingResponseBody]:
        """
        Download the whole series as a ZIP file.

        Required role: **FILE_DOWNLOAD**

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StreamingResponseBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/file",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StreamingResponseBody,
                    parse_obj_as(
                        type_=StreamingResponseBody,
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

    async def delete_series_file(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete all of the series' books files on disk.

        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/file",
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

    async def update_series_metadata(
        self,
        series_id: str,
        *,
        age_rating: typing.Optional[int] = OMIT,
        age_rating_lock: typing.Optional[bool] = OMIT,
        alternate_titles: typing.Optional[typing.Sequence[AlternateTitleUpdateDto]] = OMIT,
        alternate_titles_lock: typing.Optional[bool] = OMIT,
        genres: typing.Optional[typing.Sequence[str]] = OMIT,
        genres_lock: typing.Optional[bool] = OMIT,
        language: typing.Optional[str] = OMIT,
        language_lock: typing.Optional[bool] = OMIT,
        links: typing.Optional[typing.Sequence[WebLinkUpdateDto]] = OMIT,
        links_lock: typing.Optional[bool] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        publisher_lock: typing.Optional[bool] = OMIT,
        reading_direction: typing.Optional[SeriesMetadataUpdateDtoReadingDirection] = OMIT,
        reading_direction_lock: typing.Optional[bool] = OMIT,
        sharing_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        sharing_labels_lock: typing.Optional[bool] = OMIT,
        status: typing.Optional[SeriesMetadataUpdateDtoStatus] = OMIT,
        status_lock: typing.Optional[bool] = OMIT,
        summary: typing.Optional[str] = OMIT,
        summary_lock: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tags_lock: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        title_lock: typing.Optional[bool] = OMIT,
        title_sort: typing.Optional[str] = OMIT,
        title_sort_lock: typing.Optional[bool] = OMIT,
        total_book_count: typing.Optional[int] = OMIT,
        total_book_count_lock: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        age_rating : typing.Optional[int]

        age_rating_lock : typing.Optional[bool]

        alternate_titles : typing.Optional[typing.Sequence[AlternateTitleUpdateDto]]

        alternate_titles_lock : typing.Optional[bool]

        genres : typing.Optional[typing.Sequence[str]]

        genres_lock : typing.Optional[bool]

        language : typing.Optional[str]

        language_lock : typing.Optional[bool]

        links : typing.Optional[typing.Sequence[WebLinkUpdateDto]]

        links_lock : typing.Optional[bool]

        publisher : typing.Optional[str]

        publisher_lock : typing.Optional[bool]

        reading_direction : typing.Optional[SeriesMetadataUpdateDtoReadingDirection]

        reading_direction_lock : typing.Optional[bool]

        sharing_labels : typing.Optional[typing.Sequence[str]]

        sharing_labels_lock : typing.Optional[bool]

        status : typing.Optional[SeriesMetadataUpdateDtoStatus]

        status_lock : typing.Optional[bool]

        summary : typing.Optional[str]

        summary_lock : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        tags_lock : typing.Optional[bool]

        title : typing.Optional[str]

        title_lock : typing.Optional[bool]

        title_sort : typing.Optional[str]

        title_sort_lock : typing.Optional[bool]

        total_book_count : typing.Optional[int]

        total_book_count_lock : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/metadata",
            method="PATCH",
            json={
                "ageRating": age_rating,
                "ageRatingLock": age_rating_lock,
                "alternateTitles": convert_and_respect_annotation_metadata(
                    object_=alternate_titles, annotation=typing.Sequence[AlternateTitleUpdateDto], direction="write"
                ),
                "alternateTitlesLock": alternate_titles_lock,
                "genres": genres,
                "genresLock": genres_lock,
                "language": language,
                "languageLock": language_lock,
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=typing.Sequence[WebLinkUpdateDto], direction="write"
                ),
                "linksLock": links_lock,
                "publisher": publisher,
                "publisherLock": publisher_lock,
                "readingDirection": reading_direction,
                "readingDirectionLock": reading_direction_lock,
                "sharingLabels": sharing_labels,
                "sharingLabelsLock": sharing_labels_lock,
                "status": status,
                "statusLock": status_lock,
                "summary": summary,
                "summaryLock": summary_lock,
                "tags": tags,
                "tagsLock": tags_lock,
                "title": title,
                "titleLock": title_lock,
                "titleSort": title_sort,
                "titleSortLock": title_sort_lock,
                "totalBookCount": total_book_count,
                "totalBookCountLock": total_book_count_lock,
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

    async def refresh_metadata(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/metadata/refresh",
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

    async def mark_series_as_read(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Mark all book for series as read

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/read-progress",
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

    async def mark_series_as_unread(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Mark all book for series as unread

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/series/{encode_path_param(series_id)}/read-progress",
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
