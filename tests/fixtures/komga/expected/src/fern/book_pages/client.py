

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.media_type import MediaType
from ..types.page_dto import PageDto
from .raw_client import AsyncRawBookPagesClient, RawBookPagesClient
from .types.get_book_page_by_number_request_convert import GetBookPageByNumberRequestConvert


class BookPagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBookPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBookPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBookPagesClient
        """
        return self._raw_client

    def get_book_pages(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PageDto]:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PageDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.book_pages.get_book_pages(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_pages(book_id, request_options=request_options)
        return _response.data

    def get_book_page_by_number(
        self,
        book_id: str,
        page_number: int,
        *,
        convert: typing.Optional[GetBookPageByNumberRequestConvert] = None,
        zero_based: typing.Optional[bool] = None,
        content_negotiation: typing.Optional[bool] = None,
        accept: typing.Optional[typing.Sequence[MediaType]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Required role: **PAGE_STREAMING**

        Parameters
        ----------
        book_id : str

        page_number : int

        convert : typing.Optional[GetBookPageByNumberRequestConvert]
            Convert the image to the provided format.

        zero_based : typing.Optional[bool]
            If set to true, pages will start at index 0. If set to false, pages will start at index 1.

        content_negotiation : typing.Optional[bool]

        accept : typing.Optional[typing.Sequence[MediaType]]
            Some very limited server driven content negotiation is handled. If a book is a PDF book, and the Accept header contains 'application/pdf' as a more specific type than other 'image/' types, a raw PDF page will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.book_pages.get_book_page_by_number(
            book_id="bookId",
            page_number=1,
        )
        """
        with self._raw_client.get_book_page_by_number(
            book_id,
            page_number,
            convert=convert,
            zero_based=zero_based,
            content_negotiation=content_negotiation,
            accept=accept,
            request_options=request_options,
        ) as r:
            yield from r.data

    def get_book_page_raw_by_number(
        self, book_id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the book page in raw format, without content negotiation.

        Required role: **PAGE_STREAMING**

        Parameters
        ----------
        book_id : str

        page_number : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.book_pages.get_book_page_raw_by_number(
            book_id="bookId",
            page_number=1,
        )
        """
        _response = self._raw_client.get_book_page_raw_by_number(book_id, page_number, request_options=request_options)
        return _response.data

    def get_book_page_thumbnail_by_number(
        self, book_id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        The image is resized to 300px on the largest dimension.

        Parameters
        ----------
        book_id : str

        page_number : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.book_pages.get_book_page_thumbnail_by_number(
            book_id="bookId",
            page_number=1,
        )
        """
        with self._raw_client.get_book_page_thumbnail_by_number(
            book_id, page_number, request_options=request_options
        ) as r:
            yield from r.data


class AsyncBookPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBookPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBookPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBookPagesClient
        """
        return self._raw_client

    async def get_book_pages(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PageDto]:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PageDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.book_pages.get_book_pages(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_pages(book_id, request_options=request_options)
        return _response.data

    async def get_book_page_by_number(
        self,
        book_id: str,
        page_number: int,
        *,
        convert: typing.Optional[GetBookPageByNumberRequestConvert] = None,
        zero_based: typing.Optional[bool] = None,
        content_negotiation: typing.Optional[bool] = None,
        accept: typing.Optional[typing.Sequence[MediaType]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Required role: **PAGE_STREAMING**

        Parameters
        ----------
        book_id : str

        page_number : int

        convert : typing.Optional[GetBookPageByNumberRequestConvert]
            Convert the image to the provided format.

        zero_based : typing.Optional[bool]
            If set to true, pages will start at index 0. If set to false, pages will start at index 1.

        content_negotiation : typing.Optional[bool]

        accept : typing.Optional[typing.Sequence[MediaType]]
            Some very limited server driven content negotiation is handled. If a book is a PDF book, and the Accept header contains 'application/pdf' as a more specific type than other 'image/' types, a raw PDF page will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.book_pages.get_book_page_by_number(
                book_id="bookId",
                page_number=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_book_page_by_number(
            book_id,
            page_number,
            convert=convert,
            zero_based=zero_based,
            content_negotiation=content_negotiation,
            accept=accept,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_book_page_raw_by_number(
        self, book_id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the book page in raw format, without content negotiation.

        Required role: **PAGE_STREAMING**

        Parameters
        ----------
        book_id : str

        page_number : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.book_pages.get_book_page_raw_by_number(
                book_id="bookId",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_page_raw_by_number(
            book_id, page_number, request_options=request_options
        )
        return _response.data

    async def get_book_page_thumbnail_by_number(
        self, book_id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        The image is resized to 300px on the largest dimension.

        Parameters
        ----------
        book_id : str

        page_number : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.book_pages.get_book_page_thumbnail_by_number(
                book_id="bookId",
                page_number=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_book_page_thumbnail_by_number(
            book_id, page_number, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
