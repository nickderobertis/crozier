

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.book_import_dto import BookImportDto
from ..types.transient_book_dto import TransientBookDto
from .raw_client import AsyncRawImportClient, RawImportClient
from .types.book_import_batch_dto_copy_mode import BookImportBatchDtoCopyMode


OMIT = typing.cast(typing.Any, ...)


class ImportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImportClient
        """
        return self._raw_client

    def books(
        self,
        *,
        books: typing.Sequence[BookImportDto],
        copy_mode: BookImportBatchDtoCopyMode,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        books : typing.Sequence[BookImportDto]

        copy_mode : BookImportBatchDtoCopyMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.import_ import BookImportBatchDtoCopyMode

        from fern import BookImportDto, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.import_.books(
            books=[
                BookImportDto(
                    series_id="seriesId",
                    source_file="sourceFile",
                )
            ],
            copy_mode=BookImportBatchDtoCopyMode.MOVE,
        )
        """
        _response = self._raw_client.books(books=books, copy_mode=copy_mode, request_options=request_options)
        return _response.data

    def scan_transient_books(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransientBookDto]:
        """
        Scan provided folder for transient books.

        Required role: **ADMIN**

        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransientBookDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.import_.scan_transient_books(
            path="path",
        )
        """
        _response = self._raw_client.scan_transient_books(path=path, request_options=request_options)
        return _response.data

    def analyze_transient_book(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransientBookDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransientBookDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.import_.analyze_transient_book(
            id="id",
        )
        """
        _response = self._raw_client.analyze_transient_book(id, request_options=request_options)
        return _response.data

    def get_page_by_transient_book_id(
        self, id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
        client.import_.get_page_by_transient_book_id(
            id="id",
            page_number=1,
        )
        """
        _response = self._raw_client.get_page_by_transient_book_id(id, page_number, request_options=request_options)
        return _response.data


class AsyncImportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImportClient
        """
        return self._raw_client

    async def books(
        self,
        *,
        books: typing.Sequence[BookImportDto],
        copy_mode: BookImportBatchDtoCopyMode,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        books : typing.Sequence[BookImportDto]

        copy_mode : BookImportBatchDtoCopyMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.import_ import BookImportBatchDtoCopyMode

        from fern import AsyncFernApi, BookImportDto

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.import_.books(
                books=[
                    BookImportDto(
                        series_id="seriesId",
                        source_file="sourceFile",
                    )
                ],
                copy_mode=BookImportBatchDtoCopyMode.MOVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.books(books=books, copy_mode=copy_mode, request_options=request_options)
        return _response.data

    async def scan_transient_books(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TransientBookDto]:
        """
        Scan provided folder for transient books.

        Required role: **ADMIN**

        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TransientBookDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.import_.scan_transient_books(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.scan_transient_books(path=path, request_options=request_options)
        return _response.data

    async def analyze_transient_book(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransientBookDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransientBookDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.import_.analyze_transient_book(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analyze_transient_book(id, request_options=request_options)
        return _response.data

    async def get_page_by_transient_book_id(
        self, id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
            await client.import_.get_page_by_transient_book_id(
                id="id",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_page_by_transient_book_id(
            id, page_number, request_options=request_options
        )
        return _response.data
