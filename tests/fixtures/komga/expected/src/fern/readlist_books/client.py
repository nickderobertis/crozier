

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.book_dto import BookDto
from ..types.page_book_dto import PageBookDto
from .raw_client import AsyncRawReadlistBooksClient, RawReadlistBooksClient
from .types.get_books_by_read_list_id_request_media_status_item import GetBooksByReadListIdRequestMediaStatusItem
from .types.get_books_by_read_list_id_request_read_status_item import GetBooksByReadListIdRequestReadStatusItem


class ReadlistBooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReadlistBooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReadlistBooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReadlistBooksClient
        """
        return self._raw_client

    def get_books_by_read_list_id(
        self,
        id: str,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        read_status: typing.Optional[
            typing.Union[
                GetBooksByReadListIdRequestReadStatusItem, typing.Sequence[GetBooksByReadListIdRequestReadStatusItem]
            ]
        ] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        media_status: typing.Optional[
            typing.Union[
                GetBooksByReadListIdRequestMediaStatusItem, typing.Sequence[GetBooksByReadListIdRequestMediaStatusItem]
            ]
        ] = None,
        deleted: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Parameters
        ----------
        id : str

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        read_status : typing.Optional[typing.Union[GetBooksByReadListIdRequestReadStatusItem, typing.Sequence[GetBooksByReadListIdRequestReadStatusItem]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        media_status : typing.Optional[typing.Union[GetBooksByReadListIdRequestMediaStatusItem, typing.Sequence[GetBooksByReadListIdRequestMediaStatusItem]]]

        deleted : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

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
        client.readlist_books.get_books_by_read_list_id(
            id="id",
        )
        """
        _response = self._raw_client.get_books_by_read_list_id(
            id,
            library_id=library_id,
            read_status=read_status,
            tag=tag,
            media_status=media_status,
            deleted=deleted,
            unpaged=unpaged,
            page=page,
            size=size,
            author=author,
            request_options=request_options,
        )
        return _response.data

    def get_book_sibling_next_in_read_list(
        self, id: str, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BookDto:
        """
        Parameters
        ----------
        id : str

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
        client.readlist_books.get_book_sibling_next_in_read_list(
            id="id",
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_sibling_next_in_read_list(id, book_id, request_options=request_options)
        return _response.data

    def get_book_sibling_previous_in_read_list(
        self, id: str, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BookDto:
        """
        Parameters
        ----------
        id : str

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
        client.readlist_books.get_book_sibling_previous_in_read_list(
            id="id",
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_sibling_previous_in_read_list(
            id, book_id, request_options=request_options
        )
        return _response.data


class AsyncReadlistBooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReadlistBooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReadlistBooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReadlistBooksClient
        """
        return self._raw_client

    async def get_books_by_read_list_id(
        self,
        id: str,
        *,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        read_status: typing.Optional[
            typing.Union[
                GetBooksByReadListIdRequestReadStatusItem, typing.Sequence[GetBooksByReadListIdRequestReadStatusItem]
            ]
        ] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        media_status: typing.Optional[
            typing.Union[
                GetBooksByReadListIdRequestMediaStatusItem, typing.Sequence[GetBooksByReadListIdRequestMediaStatusItem]
            ]
        ] = None,
        deleted: typing.Optional[bool] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        author: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageBookDto:
        """
        Parameters
        ----------
        id : str

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        read_status : typing.Optional[typing.Union[GetBooksByReadListIdRequestReadStatusItem, typing.Sequence[GetBooksByReadListIdRequestReadStatusItem]]]

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        media_status : typing.Optional[typing.Union[GetBooksByReadListIdRequestMediaStatusItem, typing.Sequence[GetBooksByReadListIdRequestMediaStatusItem]]]

        deleted : typing.Optional[bool]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

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
            await client.readlist_books.get_books_by_read_list_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_books_by_read_list_id(
            id,
            library_id=library_id,
            read_status=read_status,
            tag=tag,
            media_status=media_status,
            deleted=deleted,
            unpaged=unpaged,
            page=page,
            size=size,
            author=author,
            request_options=request_options,
        )
        return _response.data

    async def get_book_sibling_next_in_read_list(
        self, id: str, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BookDto:
        """
        Parameters
        ----------
        id : str

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
            await client.readlist_books.get_book_sibling_next_in_read_list(
                id="id",
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_sibling_next_in_read_list(
            id, book_id, request_options=request_options
        )
        return _response.data

    async def get_book_sibling_previous_in_read_list(
        self, id: str, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BookDto:
        """
        Parameters
        ----------
        id : str

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
            await client.readlist_books.get_book_sibling_previous_in_read_list(
                id="id",
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_sibling_previous_in_read_list(
            id, book_id, request_options=request_options
        )
        return _response.data
