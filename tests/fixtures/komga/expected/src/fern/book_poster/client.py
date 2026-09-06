

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.thumbnail_book_dto import ThumbnailBookDto
from .raw_client import AsyncRawBookPosterClient, RawBookPosterClient


OMIT = typing.cast(typing.Any, ...)


class BookPosterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBookPosterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBookPosterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBookPosterClient
        """
        return self._raw_client

    def books_regenerate_thumbnails(
        self,
        *,
        for_bigger_result_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        for_bigger_result_only : typing.Optional[bool]

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
        client.book_poster.books_regenerate_thumbnails()
        """
        _response = self._raw_client.books_regenerate_thumbnails(
            for_bigger_result_only=for_bigger_result_only, request_options=request_options
        )
        return _response.data

    def get_book_thumbnail(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        book_id : str

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
        client.book_poster.get_book_thumbnail(
            book_id="bookId",
        )
        """
        with self._raw_client.get_book_thumbnail(book_id, request_options=request_options) as r:
            yield from r.data

    def get_book_thumbnails(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThumbnailBookDto]:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThumbnailBookDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.book_poster.get_book_thumbnails(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_thumbnails(book_id, request_options=request_options)
        return _response.data

    def add_user_uploaded_book_thumbnail(
        self,
        book_id: str,
        *,
        file: core.File,
        selected: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThumbnailBookDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

        file : core.File
            See core.File for more documentation

        selected : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThumbnailBookDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.book_poster.add_user_uploaded_book_thumbnail(
            book_id="bookId",
        )
        """
        _response = self._raw_client.add_user_uploaded_book_thumbnail(
            book_id, file=file, selected=selected, request_options=request_options
        )
        return _response.data

    def get_book_thumbnail_by_id(
        self, book_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        book_id : str

        thumbnail_id : str

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
        client.book_poster.get_book_thumbnail_by_id(
            book_id="bookId",
            thumbnail_id="thumbnailId",
        )
        """
        with self._raw_client.get_book_thumbnail_by_id(book_id, thumbnail_id, request_options=request_options) as r:
            yield from r.data

    def delete_user_uploaded_book_thumbnail(
        self, book_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Only uploaded posters can be deleted.

        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

        thumbnail_id : str

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
        client.book_poster.delete_user_uploaded_book_thumbnail(
            book_id="bookId",
            thumbnail_id="thumbnailId",
        )
        """
        _response = self._raw_client.delete_user_uploaded_book_thumbnail(
            book_id, thumbnail_id, request_options=request_options
        )
        return _response.data

    def mark_book_thumbnail_selected(
        self, book_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

        thumbnail_id : str

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
        client.book_poster.mark_book_thumbnail_selected(
            book_id="bookId",
            thumbnail_id="thumbnailId",
        )
        """
        _response = self._raw_client.mark_book_thumbnail_selected(
            book_id, thumbnail_id, request_options=request_options
        )
        return _response.data


class AsyncBookPosterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBookPosterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBookPosterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBookPosterClient
        """
        return self._raw_client

    async def books_regenerate_thumbnails(
        self,
        *,
        for_bigger_result_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        for_bigger_result_only : typing.Optional[bool]

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
            await client.book_poster.books_regenerate_thumbnails()


        asyncio.run(main())
        """
        _response = await self._raw_client.books_regenerate_thumbnails(
            for_bigger_result_only=for_bigger_result_only, request_options=request_options
        )
        return _response.data

    async def get_book_thumbnail(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        book_id : str

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
            await client.book_poster.get_book_thumbnail(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_book_thumbnail(book_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_book_thumbnails(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThumbnailBookDto]:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThumbnailBookDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.book_poster.get_book_thumbnails(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_thumbnails(book_id, request_options=request_options)
        return _response.data

    async def add_user_uploaded_book_thumbnail(
        self,
        book_id: str,
        *,
        file: core.File,
        selected: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThumbnailBookDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

        file : core.File
            See core.File for more documentation

        selected : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThumbnailBookDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.book_poster.add_user_uploaded_book_thumbnail(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_user_uploaded_book_thumbnail(
            book_id, file=file, selected=selected, request_options=request_options
        )
        return _response.data

    async def get_book_thumbnail_by_id(
        self, book_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        book_id : str

        thumbnail_id : str

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
            await client.book_poster.get_book_thumbnail_by_id(
                book_id="bookId",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_book_thumbnail_by_id(
            book_id, thumbnail_id, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def delete_user_uploaded_book_thumbnail(
        self, book_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Only uploaded posters can be deleted.

        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

        thumbnail_id : str

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
            await client.book_poster.delete_user_uploaded_book_thumbnail(
                book_id="bookId",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_uploaded_book_thumbnail(
            book_id, thumbnail_id, request_options=request_options
        )
        return _response.data

    async def mark_book_thumbnail_selected(
        self, book_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_id : str

        thumbnail_id : str

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
            await client.book_poster.mark_book_thumbnail_selected(
                book_id="bookId",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_book_thumbnail_selected(
            book_id, thumbnail_id, request_options=request_options
        )
        return _response.data
