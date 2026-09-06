

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alternate_title_update_dto import AlternateTitleUpdateDto
from ..types.collection_dto import CollectionDto
from ..types.group_count_dto import GroupCountDto
from ..types.page_book_dto import PageBookDto
from ..types.page_series_dto import PageSeriesDto
from ..types.search_condition_series import SearchConditionSeries
from ..types.series_dto import SeriesDto
from ..types.streaming_response_body import StreamingResponseBody
from ..types.web_link_update_dto import WebLinkUpdateDto
from .raw_client import AsyncRawSeriesClient, RawSeriesClient
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


OMIT = typing.cast(typing.Any, ...)


class SeriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSeriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSeriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSeriesClient
        """
        return self._raw_client

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_series_deprecated()
        """
        _response = self._raw_client.get_series_deprecated(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            status=status,
            read_status=read_status,
            publisher=publisher,
            language=language,
            genre=genre,
            tag=tag,
            age_rating=age_rating,
            release_year=release_year,
            sharing_label=sharing_label,
            deleted=deleted,
            complete=complete,
            oneshot=oneshot,
            unpaged=unpaged,
            search_regex=search_regex,
            page=page,
            size=size,
            sort=sort,
            author=author,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[GroupCountDto]:
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
        typing.List[GroupCountDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_series_alphabetical_groups_deprecated()
        """
        _response = self._raw_client.get_series_alphabetical_groups_deprecated(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            status=status,
            read_status=read_status,
            publisher=publisher,
            language=language,
            genre=genre,
            tag=tag,
            age_rating=age_rating,
            release_year=release_year,
            sharing_label=sharing_label,
            deleted=deleted,
            complete=complete,
            oneshot=oneshot,
            search_regex=search_regex,
            author=author,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_series_latest()
        """
        _response = self._raw_client.get_series_latest(
            library_id=library_id,
            deleted=deleted,
            oneshot=oneshot,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_series()
        """
        _response = self._raw_client.get_series(
            unpaged=unpaged,
            page=page,
            size=size,
            sort=sort,
            condition=condition,
            full_text_search=full_text_search,
            request_options=request_options,
        )
        return _response.data

    def get_series_alphabetical_groups(
        self,
        *,
        condition: typing.Optional[SearchConditionSeries] = OMIT,
        full_text_search: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GroupCountDto]:
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
        typing.List[GroupCountDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_series_alphabetical_groups()
        """
        _response = self._raw_client.get_series_alphabetical_groups(
            condition=condition, full_text_search=full_text_search, request_options=request_options
        )
        return _response.data

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_series_new()
        """
        _response = self._raw_client.get_series_new(
            library_id=library_id,
            deleted=deleted,
            oneshot=oneshot,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_series_updated()
        """
        _response = self._raw_client.get_series_updated(
            library_id=library_id,
            deleted=deleted,
            oneshot=oneshot,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def get_series_by_id(self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SeriesDto:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeriesDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_series_by_id(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.get_series_by_id(series_id, request_options=request_options)
        return _response.data

    def analyze(self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

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
        client.series.analyze(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.analyze(series_id, request_options=request_options)
        return _response.data

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
    ) -> PageBookDto:
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
        PageBookDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_books_by_series_id(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.get_books_by_series_id(
            series_id,
            media_status=media_status,
            read_status=read_status,
            tag=tag,
            deleted=deleted,
            unpaged=unpaged,
            page=page,
            size=size,
            sort=sort,
            author=author,
            request_options=request_options,
        )
        return _response.data

    def get_collections_by_series_id(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CollectionDto]:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CollectionDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.get_collections_by_series_id(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.get_collections_by_series_id(series_id, request_options=request_options)
        return _response.data

    def download_series_as_zip(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamingResponseBody:
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
        StreamingResponseBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.download_series_as_zip(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.download_series_as_zip(series_id, request_options=request_options)
        return _response.data

    def delete_series_file(self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.delete_series_file(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.delete_series_file(series_id, request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series.update_series_metadata(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.update_series_metadata(
            series_id,
            age_rating=age_rating,
            age_rating_lock=age_rating_lock,
            alternate_titles=alternate_titles,
            alternate_titles_lock=alternate_titles_lock,
            genres=genres,
            genres_lock=genres_lock,
            language=language,
            language_lock=language_lock,
            links=links,
            links_lock=links_lock,
            publisher=publisher,
            publisher_lock=publisher_lock,
            reading_direction=reading_direction,
            reading_direction_lock=reading_direction_lock,
            sharing_labels=sharing_labels,
            sharing_labels_lock=sharing_labels_lock,
            status=status,
            status_lock=status_lock,
            summary=summary,
            summary_lock=summary_lock,
            tags=tags,
            tags_lock=tags_lock,
            title=title,
            title_lock=title_lock,
            title_sort=title_sort,
            title_sort_lock=title_sort_lock,
            total_book_count=total_book_count,
            total_book_count_lock=total_book_count_lock,
            request_options=request_options,
        )
        return _response.data

    def refresh_metadata(self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

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
        client.series.refresh_metadata(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.refresh_metadata(series_id, request_options=request_options)
        return _response.data

    def mark_series_as_read(self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Mark all book for series as read

        Parameters
        ----------
        series_id : str

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
        client.series.mark_series_as_read(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.mark_series_as_read(series_id, request_options=request_options)
        return _response.data

    def mark_series_as_unread(self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Mark all book for series as unread

        Parameters
        ----------
        series_id : str

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
        client.series.mark_series_as_unread(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.mark_series_as_unread(series_id, request_options=request_options)
        return _response.data


class AsyncSeriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSeriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSeriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSeriesClient
        """
        return self._raw_client

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_series_deprecated()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_deprecated(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            status=status,
            read_status=read_status,
            publisher=publisher,
            language=language,
            genre=genre,
            tag=tag,
            age_rating=age_rating,
            release_year=release_year,
            sharing_label=sharing_label,
            deleted=deleted,
            complete=complete,
            oneshot=oneshot,
            unpaged=unpaged,
            search_regex=search_regex,
            page=page,
            size=size,
            sort=sort,
            author=author,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[GroupCountDto]:
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
        typing.List[GroupCountDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_series_alphabetical_groups_deprecated()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_alphabetical_groups_deprecated(
            search=search,
            library_id=library_id,
            collection_id=collection_id,
            status=status,
            read_status=read_status,
            publisher=publisher,
            language=language,
            genre=genre,
            tag=tag,
            age_rating=age_rating,
            release_year=release_year,
            sharing_label=sharing_label,
            deleted=deleted,
            complete=complete,
            oneshot=oneshot,
            search_regex=search_regex,
            author=author,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_series_latest()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_latest(
            library_id=library_id,
            deleted=deleted,
            oneshot=oneshot,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_series()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series(
            unpaged=unpaged,
            page=page,
            size=size,
            sort=sort,
            condition=condition,
            full_text_search=full_text_search,
            request_options=request_options,
        )
        return _response.data

    async def get_series_alphabetical_groups(
        self,
        *,
        condition: typing.Optional[SearchConditionSeries] = OMIT,
        full_text_search: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GroupCountDto]:
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
        typing.List[GroupCountDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_series_alphabetical_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_alphabetical_groups(
            condition=condition, full_text_search=full_text_search, request_options=request_options
        )
        return _response.data

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_series_new()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_new(
            library_id=library_id,
            deleted=deleted,
            oneshot=oneshot,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PageSeriesDto:
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
        PageSeriesDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_series_updated()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_updated(
            library_id=library_id,
            deleted=deleted,
            oneshot=oneshot,
            unpaged=unpaged,
            page=page,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def get_series_by_id(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SeriesDto:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeriesDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_series_by_id(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_by_id(series_id, request_options=request_options)
        return _response.data

    async def analyze(self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

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
            await client.series.analyze(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analyze(series_id, request_options=request_options)
        return _response.data

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
    ) -> PageBookDto:
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
        PageBookDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_books_by_series_id(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_books_by_series_id(
            series_id,
            media_status=media_status,
            read_status=read_status,
            tag=tag,
            deleted=deleted,
            unpaged=unpaged,
            page=page,
            size=size,
            sort=sort,
            author=author,
            request_options=request_options,
        )
        return _response.data

    async def get_collections_by_series_id(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CollectionDto]:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CollectionDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.get_collections_by_series_id(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collections_by_series_id(series_id, request_options=request_options)
        return _response.data

    async def download_series_as_zip(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamingResponseBody:
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
        StreamingResponseBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.download_series_as_zip(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_series_as_zip(series_id, request_options=request_options)
        return _response.data

    async def delete_series_file(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.delete_series_file(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_series_file(series_id, request_options=request_options)
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series.update_series_metadata(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_series_metadata(
            series_id,
            age_rating=age_rating,
            age_rating_lock=age_rating_lock,
            alternate_titles=alternate_titles,
            alternate_titles_lock=alternate_titles_lock,
            genres=genres,
            genres_lock=genres_lock,
            language=language,
            language_lock=language_lock,
            links=links,
            links_lock=links_lock,
            publisher=publisher,
            publisher_lock=publisher_lock,
            reading_direction=reading_direction,
            reading_direction_lock=reading_direction_lock,
            sharing_labels=sharing_labels,
            sharing_labels_lock=sharing_labels_lock,
            status=status,
            status_lock=status_lock,
            summary=summary,
            summary_lock=summary_lock,
            tags=tags,
            tags_lock=tags_lock,
            title=title,
            title_lock=title_lock,
            title_sort=title_sort,
            title_sort_lock=title_sort_lock,
            total_book_count=total_book_count,
            total_book_count_lock=total_book_count_lock,
            request_options=request_options,
        )
        return _response.data

    async def refresh_metadata(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

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
            await client.series.refresh_metadata(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_metadata(series_id, request_options=request_options)
        return _response.data

    async def mark_series_as_read(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mark all book for series as read

        Parameters
        ----------
        series_id : str

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
            await client.series.mark_series_as_read(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_series_as_read(series_id, request_options=request_options)
        return _response.data

    async def mark_series_as_unread(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mark all book for series as unread

        Parameters
        ----------
        series_id : str

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
            await client.series.mark_series_as_unread(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_series_as_unread(series_id, request_options=request_options)
        return _response.data
