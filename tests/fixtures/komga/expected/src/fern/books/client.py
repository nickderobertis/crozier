

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.author_update_dto import AuthorUpdateDto
from ..types.book_dto import BookDto
from ..types.book_metadata_update_dto import BookMetadataUpdateDto
from ..types.page_book_dto import PageBookDto
from ..types.read_list_dto import ReadListDto
from ..types.search_condition_book import SearchConditionBook
from ..types.streaming_response_body import StreamingResponseBody
from ..types.web_link_update_dto import WebLinkUpdateDto
from .raw_client import AsyncRawBooksClient, RawBooksClient
from .types.get_all_books_deprecated_request_media_status_item import GetAllBooksDeprecatedRequestMediaStatusItem
from .types.get_all_books_deprecated_request_read_status_item import GetAllBooksDeprecatedRequestReadStatusItem


OMIT = typing.cast(typing.Any, ...)


class BooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBooksClient
        """
        return self._raw_client

    def get_all_books_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        media_status: typing.Optional[
            typing.Union[
                GetAllBooksDeprecatedRequestMediaStatusItem,
                typing.Sequence[GetAllBooksDeprecatedRequestMediaStatusItem],
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetAllBooksDeprecatedRequestReadStatusItem, typing.Sequence[GetAllBooksDeprecatedRequestReadStatusItem]
            ]
        ] = None,
        released_after: typing.Optional[dt.date] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Use POST /api/v1/books/list instead. Deprecated since 1.19.0.

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        media_status : typing.Optional[typing.Union[GetAllBooksDeprecatedRequestMediaStatusItem, typing.Sequence[GetAllBooksDeprecatedRequestMediaStatusItem]]]

        read_status : typing.Optional[typing.Union[GetAllBooksDeprecatedRequestReadStatusItem, typing.Sequence[GetAllBooksDeprecatedRequestReadStatusItem]]]

        released_after : typing.Optional[dt.date]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

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
        client.books.get_all_books_deprecated()
        """
        _response = self._raw_client.get_all_books_deprecated(
            search=search,
            library_id=library_id,
            media_status=media_status,
            read_status=read_status,
            released_after=released_after,
            tag=tag,
            unpaged=unpaged,
            page=page,
            size=size,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    def get_books_duplicates(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Return books that have the same file hash.

        Required role: **ADMIN**

        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

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
        client.books.get_books_duplicates()
        """
        _response = self._raw_client.get_books_duplicates(
            unpaged=unpaged, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_books_latest(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Return newly added or updated books.

        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

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
        client.books.get_books_latest()
        """
        _response = self._raw_client.get_books_latest(
            unpaged=unpaged, page=page, size=size, request_options=request_options
        )
        return _response.data

    def get_books(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        condition: typing.Optional[SearchConditionBook] = OMIT,
        full_text_search: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
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

        condition : typing.Optional[SearchConditionBook]

        full_text_search : typing.Optional[str]

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
        client.books.get_books()
        """
        _response = self._raw_client.get_books(
            unpaged=unpaged,
            page=page,
            size=size,
            sort=sort,
            condition=condition,
            full_text_search=full_text_search,
            request_options=request_options,
        )
        return _response.data

    def update_book_metadata_by_batch(
        self,
        *,
        request: typing.Dict[str, BookMetadataUpdateDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set a field to null to unset the metadata. You can omit fields you don't want to update.

        Required role: **ADMIN**

        Parameters
        ----------
        request : typing.Dict[str, BookMetadataUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import BookMetadataUpdateDto, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.books.update_book_metadata_by_batch(
            request={"key": BookMetadataUpdateDto()},
        )
        """
        _response = self._raw_client.update_book_metadata_by_batch(request=request, request_options=request_options)
        return _response.data

    def get_books_on_deck(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Return first unread book of series with at least one book read and no books in progress.

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

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
        client.books.get_books_on_deck()
        """
        _response = self._raw_client.get_books_on_deck(
            library_id=library_id, page=page, size=size, request_options=request_options
        )
        return _response.data

    def get_book_by_id(self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BookDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BookDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.books.get_book_by_id(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_by_id(book_id, request_options=request_options)
        return _response.data

    def book_analyze(self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

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
        client.books.book_analyze(
            book_id="bookId",
        )
        """
        _response = self._raw_client.book_analyze(book_id, request_options=request_options)
        return _response.data

    def download_book_file(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamingResponseBody:
        """
        Download the book file.

        Required role: **FILE_DOWNLOAD**

        Parameters
        ----------
        book_id : str

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
        client.books.download_book_file(
            book_id="bookId",
        )
        """
        _response = self._raw_client.download_book_file(book_id, request_options=request_options)
        return _response.data

    def delete_book_file(self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

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
        client.books.delete_book_file(
            book_id="bookId",
        )
        """
        _response = self._raw_client.delete_book_file(book_id, request_options=request_options)
        return _response.data

    def download_book_file1(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamingResponseBody:
        """
        Download the book file.

        Required role: **FILE_DOWNLOAD**

        Parameters
        ----------
        book_id : str

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
        client.books.download_book_file1(
            book_id="bookId",
        )
        """
        _response = self._raw_client.download_book_file1(book_id, request_options=request_options)
        return _response.data

    def update_book_metadata(
        self,
        book_id: str,
        *,
        authors: typing.Optional[typing.Sequence[AuthorUpdateDto]] = OMIT,
        authors_lock: typing.Optional[bool] = OMIT,
        isbn: typing.Optional[str] = OMIT,
        isbn_lock: typing.Optional[bool] = OMIT,
        links: typing.Optional[typing.Sequence[WebLinkUpdateDto]] = OMIT,
        links_lock: typing.Optional[bool] = OMIT,
        number: typing.Optional[str] = OMIT,
        number_lock: typing.Optional[bool] = OMIT,
        number_sort: typing.Optional[float] = OMIT,
        number_sort_lock: typing.Optional[bool] = OMIT,
        release_date: typing.Optional[dt.date] = OMIT,
        release_date_lock: typing.Optional[bool] = OMIT,
        summary: typing.Optional[str] = OMIT,
        summary_lock: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tags_lock: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        title_lock: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set a field to null to unset the metadata. You can omit fields you don't want to update.

        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

        authors : typing.Optional[typing.Sequence[AuthorUpdateDto]]

        authors_lock : typing.Optional[bool]

        isbn : typing.Optional[str]

        isbn_lock : typing.Optional[bool]

        links : typing.Optional[typing.Sequence[WebLinkUpdateDto]]

        links_lock : typing.Optional[bool]

        number : typing.Optional[str]

        number_lock : typing.Optional[bool]

        number_sort : typing.Optional[float]

        number_sort_lock : typing.Optional[bool]

        release_date : typing.Optional[dt.date]

        release_date_lock : typing.Optional[bool]

        summary : typing.Optional[str]

        summary_lock : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        tags_lock : typing.Optional[bool]

        title : typing.Optional[str]

        title_lock : typing.Optional[bool]

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
        client.books.update_book_metadata(
            book_id="bookId",
        )
        """
        _response = self._raw_client.update_book_metadata(
            book_id,
            authors=authors,
            authors_lock=authors_lock,
            isbn=isbn,
            isbn_lock=isbn_lock,
            links=links,
            links_lock=links_lock,
            number=number,
            number_lock=number_lock,
            number_sort=number_sort,
            number_sort_lock=number_sort_lock,
            release_date=release_date,
            release_date_lock=release_date_lock,
            summary=summary,
            summary_lock=summary_lock,
            tags=tags,
            tags_lock=tags_lock,
            title=title,
            title_lock=title_lock,
            request_options=request_options,
        )
        return _response.data

    def book_refresh_metadata(self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

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
        client.books.book_refresh_metadata(
            book_id="bookId",
        )
        """
        _response = self._raw_client.book_refresh_metadata(book_id, request_options=request_options)
        return _response.data

    def get_book_sibling_next(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BookDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BookDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.books.get_book_sibling_next(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_sibling_next(book_id, request_options=request_options)
        return _response.data

    def get_book_sibling_previous(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BookDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BookDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.books.get_book_sibling_previous(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_sibling_previous(book_id, request_options=request_options)
        return _response.data

    def delete_book_read_progress(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mark book as unread

        Parameters
        ----------
        book_id : str

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
        client.books.delete_book_read_progress(
            book_id="bookId",
        )
        """
        _response = self._raw_client.delete_book_read_progress(book_id, request_options=request_options)
        return _response.data

    def mark_book_read_progress(
        self,
        book_id: str,
        *,
        completed: typing.Optional[bool] = OMIT,
        page: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Mark book as read and/or change page progress.

        Parameters
        ----------
        book_id : str

        completed : typing.Optional[bool]

        page : typing.Optional[int]

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
        client.books.mark_book_read_progress(
            book_id="bookId",
        )
        """
        _response = self._raw_client.mark_book_read_progress(
            book_id, completed=completed, page=page, request_options=request_options
        )
        return _response.data

    def get_read_lists_by_book_id(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ReadListDto]:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReadListDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.books.get_read_lists_by_book_id(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_read_lists_by_book_id(book_id, request_options=request_options)
        return _response.data


class AsyncBooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBooksClient
        """
        return self._raw_client

    async def get_all_books_deprecated(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        media_status: typing.Optional[
            typing.Union[
                GetAllBooksDeprecatedRequestMediaStatusItem,
                typing.Sequence[GetAllBooksDeprecatedRequestMediaStatusItem],
            ]
        ] = None,
        read_status: typing.Optional[
            typing.Union[
                GetAllBooksDeprecatedRequestReadStatusItem, typing.Sequence[GetAllBooksDeprecatedRequestReadStatusItem]
            ]
        ] = None,
        released_after: typing.Optional[dt.date] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Use POST /api/v1/books/list instead. Deprecated since 1.19.0.

        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        media_status : typing.Optional[typing.Union[GetAllBooksDeprecatedRequestMediaStatusItem, typing.Sequence[GetAllBooksDeprecatedRequestMediaStatusItem]]]

        read_status : typing.Optional[typing.Union[GetAllBooksDeprecatedRequestReadStatusItem, typing.Sequence[GetAllBooksDeprecatedRequestReadStatusItem]]]

        released_after : typing.Optional[dt.date]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

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
            await client.books.get_all_books_deprecated()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_books_deprecated(
            search=search,
            library_id=library_id,
            media_status=media_status,
            read_status=read_status,
            released_after=released_after,
            tag=tag,
            unpaged=unpaged,
            page=page,
            size=size,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    async def get_books_duplicates(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Return books that have the same file hash.

        Required role: **ADMIN**

        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

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
            await client.books.get_books_duplicates()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_books_duplicates(
            unpaged=unpaged, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_books_latest(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Return newly added or updated books.

        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

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
            await client.books.get_books_latest()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_books_latest(
            unpaged=unpaged, page=page, size=size, request_options=request_options
        )
        return _response.data

    async def get_books(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        condition: typing.Optional[SearchConditionBook] = OMIT,
        full_text_search: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
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

        condition : typing.Optional[SearchConditionBook]

        full_text_search : typing.Optional[str]

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
            await client.books.get_books()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_books(
            unpaged=unpaged,
            page=page,
            size=size,
            sort=sort,
            condition=condition,
            full_text_search=full_text_search,
            request_options=request_options,
        )
        return _response.data

    async def update_book_metadata_by_batch(
        self,
        *,
        request: typing.Dict[str, BookMetadataUpdateDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set a field to null to unset the metadata. You can omit fields you don't want to update.

        Required role: **ADMIN**

        Parameters
        ----------
        request : typing.Dict[str, BookMetadataUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BookMetadataUpdateDto

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.books.update_book_metadata_by_batch(
                request={"key": BookMetadataUpdateDto()},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_book_metadata_by_batch(
            request=request, request_options=request_options
        )
        return _response.data

    async def get_books_on_deck(
        self,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Return first unread book of series with at least one book read and no books in progress.

        Parameters
        ----------
        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

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
            await client.books.get_books_on_deck()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_books_on_deck(
            library_id=library_id, page=page, size=size, request_options=request_options
        )
        return _response.data

    async def get_book_by_id(self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BookDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BookDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.books.get_book_by_id(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_by_id(book_id, request_options=request_options)
        return _response.data

    async def book_analyze(self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

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
            await client.books.book_analyze(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.book_analyze(book_id, request_options=request_options)
        return _response.data

    async def download_book_file(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamingResponseBody:
        """
        Download the book file.

        Required role: **FILE_DOWNLOAD**

        Parameters
        ----------
        book_id : str

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
            await client.books.download_book_file(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_book_file(book_id, request_options=request_options)
        return _response.data

    async def delete_book_file(self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

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
            await client.books.delete_book_file(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_book_file(book_id, request_options=request_options)
        return _response.data

    async def download_book_file1(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamingResponseBody:
        """
        Download the book file.

        Required role: **FILE_DOWNLOAD**

        Parameters
        ----------
        book_id : str

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
            await client.books.download_book_file1(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_book_file1(book_id, request_options=request_options)
        return _response.data

    async def update_book_metadata(
        self,
        book_id: str,
        *,
        authors: typing.Optional[typing.Sequence[AuthorUpdateDto]] = OMIT,
        authors_lock: typing.Optional[bool] = OMIT,
        isbn: typing.Optional[str] = OMIT,
        isbn_lock: typing.Optional[bool] = OMIT,
        links: typing.Optional[typing.Sequence[WebLinkUpdateDto]] = OMIT,
        links_lock: typing.Optional[bool] = OMIT,
        number: typing.Optional[str] = OMIT,
        number_lock: typing.Optional[bool] = OMIT,
        number_sort: typing.Optional[float] = OMIT,
        number_sort_lock: typing.Optional[bool] = OMIT,
        release_date: typing.Optional[dt.date] = OMIT,
        release_date_lock: typing.Optional[bool] = OMIT,
        summary: typing.Optional[str] = OMIT,
        summary_lock: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tags_lock: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        title_lock: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set a field to null to unset the metadata. You can omit fields you don't want to update.

        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

        authors : typing.Optional[typing.Sequence[AuthorUpdateDto]]

        authors_lock : typing.Optional[bool]

        isbn : typing.Optional[str]

        isbn_lock : typing.Optional[bool]

        links : typing.Optional[typing.Sequence[WebLinkUpdateDto]]

        links_lock : typing.Optional[bool]

        number : typing.Optional[str]

        number_lock : typing.Optional[bool]

        number_sort : typing.Optional[float]

        number_sort_lock : typing.Optional[bool]

        release_date : typing.Optional[dt.date]

        release_date_lock : typing.Optional[bool]

        summary : typing.Optional[str]

        summary_lock : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        tags_lock : typing.Optional[bool]

        title : typing.Optional[str]

        title_lock : typing.Optional[bool]

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
            await client.books.update_book_metadata(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_book_metadata(
            book_id,
            authors=authors,
            authors_lock=authors_lock,
            isbn=isbn,
            isbn_lock=isbn_lock,
            links=links,
            links_lock=links_lock,
            number=number,
            number_lock=number_lock,
            number_sort=number_sort,
            number_sort_lock=number_sort_lock,
            release_date=release_date,
            release_date_lock=release_date_lock,
            summary=summary,
            summary_lock=summary_lock,
            tags=tags,
            tags_lock=tags_lock,
            title=title,
            title_lock=title_lock,
            request_options=request_options,
        )
        return _response.data

    async def book_refresh_metadata(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

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
            await client.books.book_refresh_metadata(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.book_refresh_metadata(book_id, request_options=request_options)
        return _response.data

    async def get_book_sibling_next(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BookDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BookDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.books.get_book_sibling_next(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_sibling_next(book_id, request_options=request_options)
        return _response.data

    async def get_book_sibling_previous(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BookDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BookDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.books.get_book_sibling_previous(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_sibling_previous(book_id, request_options=request_options)
        return _response.data

    async def delete_book_read_progress(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mark book as unread

        Parameters
        ----------
        book_id : str

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
            await client.books.delete_book_read_progress(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_book_read_progress(book_id, request_options=request_options)
        return _response.data

    async def mark_book_read_progress(
        self,
        book_id: str,
        *,
        completed: typing.Optional[bool] = OMIT,
        page: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Mark book as read and/or change page progress.

        Parameters
        ----------
        book_id : str

        completed : typing.Optional[bool]

        page : typing.Optional[int]

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
            await client.books.mark_book_read_progress(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_book_read_progress(
            book_id, completed=completed, page=page, request_options=request_options
        )
        return _response.data

    async def get_read_lists_by_book_id(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ReadListDto]:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReadListDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.books.get_read_lists_by_book_id(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_read_lists_by_book_id(book_id, request_options=request_options)
        return _response.data
