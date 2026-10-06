

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.book_name import BookName
from ..types.protoform_conformance_v1book import ProtoformConformanceV1Book
from ..types.protoform_conformance_v1list_books_response import ProtoformConformanceV1ListBooksResponse
from ..types.publisher_name import PublisherName
from .raw_client import AsyncRawLibraryRpcClient, RawLibraryRpcClient


OMIT = typing.cast(typing.Any, ...)


class LibraryRpcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLibraryRpcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLibraryRpcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLibraryRpcClient
        """
        return self._raw_client

    def protoform_conformance_v1library_service_list_books(
        self,
        *,
        parent: PublisherName,
        page_size: typing.Optional[int] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProtoformConformanceV1ListBooksResponse:
        """
        Parameters
        ----------
        parent : PublisherName

        page_size : typing.Optional[int]

        page_token : typing.Optional[str]

        filter : typing.Optional[str]
            Case-insensitive title or ISBN substring.

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtoformConformanceV1ListBooksResponse
            Books in the temporary library

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.library_rpc.protoform_conformance_v1library_service_list_books(
            parent="publishers/demo-library",
        )
        """
        _response = self._raw_client.protoform_conformance_v1library_service_list_books(
            parent=parent,
            page_size=page_size,
            page_token=page_token,
            filter=filter,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def protoform_conformance_v1library_service_get_book(
        self, *, name: BookName, request_options: typing.Optional[RequestOptions] = None
    ) -> ProtoformConformanceV1Book:
        """
        Parameters
        ----------
        name : BookName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtoformConformanceV1Book
            The requested book

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.library_rpc.protoform_conformance_v1library_service_get_book(
            name="publishers/demo-library/books/protoform-guide",
        )
        """
        _response = self._raw_client.protoform_conformance_v1library_service_get_book(
            name=name, request_options=request_options
        )
        return _response.data

    def protoform_conformance_v1library_service_create_book(
        self,
        *,
        parent: PublisherName,
        book: ProtoformConformanceV1Book,
        book_id: str,
        request_id: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProtoformConformanceV1Book:
        """
        Parameters
        ----------
        parent : PublisherName

        book : ProtoformConformanceV1Book

        book_id : str

        request_id : typing.Optional[str]

        validate_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtoformConformanceV1Book
            The created book

        Examples
        --------
        from fern import FernApi, ProtoformConformanceV1Book

        client = FernApi()
        client.library_rpc.protoform_conformance_v1library_service_create_book(
            parent="publishers/demo-library",
            book=ProtoformConformanceV1Book(
                display_name="The Protoform Guide",
                isbn="9783161484100",
            ),
            book_id="protoform-guide",
        )
        """
        _response = self._raw_client.protoform_conformance_v1library_service_create_book(
            parent=parent,
            book=book,
            book_id=book_id,
            request_id=request_id,
            validate_only=validate_only,
            request_options=request_options,
        )
        return _response.data

    def protoform_conformance_v1library_service_update_book(
        self,
        *,
        book: ProtoformConformanceV1Book,
        update_mask: str,
        request_id: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        allow_missing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProtoformConformanceV1Book:
        """
        Parameters
        ----------
        book : ProtoformConformanceV1Book

        update_mask : str
            Protobuf JSON FieldMask, such as displayName,note.

        request_id : typing.Optional[str]

        validate_only : typing.Optional[bool]

        allow_missing : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtoformConformanceV1Book
            The updated book with a new etag

        Examples
        --------
        from fern import FernApi, ProtoformConformanceV1Book

        client = FernApi()
        client.library_rpc.protoform_conformance_v1library_service_update_book(
            book=ProtoformConformanceV1Book(
                display_name="The Protoform Guide",
                isbn="9783161484100",
            ),
            update_mask="displayName,note",
        )
        """
        _response = self._raw_client.protoform_conformance_v1library_service_update_book(
            book=book,
            update_mask=update_mask,
            request_id=request_id,
            validate_only=validate_only,
            allow_missing=allow_missing,
            request_options=request_options,
        )
        return _response.data

    def protoform_conformance_v1library_service_delete_book(
        self,
        *,
        name: BookName,
        request_id: typing.Optional[str] = OMIT,
        etag: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a book by resource name and etag. The server validates optimistic concurrency, returns a structured Connect error when the version is stale, and responds with an empty protobuf message after successful deletion.

        Parameters
        ----------
        name : BookName

        request_id : typing.Optional[str]

        etag : typing.Optional[str]
            Last observed book etag.

        validate_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Empty protobuf response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.library_rpc.protoform_conformance_v1library_service_delete_book(
            name="publishers/demo-library/books/protoform-guide",
        )
        """
        _response = self._raw_client.protoform_conformance_v1library_service_delete_book(
            name=name, request_id=request_id, etag=etag, validate_only=validate_only, request_options=request_options
        )
        return _response.data


class AsyncLibraryRpcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLibraryRpcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLibraryRpcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLibraryRpcClient
        """
        return self._raw_client

    async def protoform_conformance_v1library_service_list_books(
        self,
        *,
        parent: PublisherName,
        page_size: typing.Optional[int] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        filter: typing.Optional[str] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProtoformConformanceV1ListBooksResponse:
        """
        Parameters
        ----------
        parent : PublisherName

        page_size : typing.Optional[int]

        page_token : typing.Optional[str]

        filter : typing.Optional[str]
            Case-insensitive title or ISBN substring.

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtoformConformanceV1ListBooksResponse
            Books in the temporary library

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.library_rpc.protoform_conformance_v1library_service_list_books(
                parent="publishers/demo-library",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protoform_conformance_v1library_service_list_books(
            parent=parent,
            page_size=page_size,
            page_token=page_token,
            filter=filter,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def protoform_conformance_v1library_service_get_book(
        self, *, name: BookName, request_options: typing.Optional[RequestOptions] = None
    ) -> ProtoformConformanceV1Book:
        """
        Parameters
        ----------
        name : BookName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtoformConformanceV1Book
            The requested book

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.library_rpc.protoform_conformance_v1library_service_get_book(
                name="publishers/demo-library/books/protoform-guide",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protoform_conformance_v1library_service_get_book(
            name=name, request_options=request_options
        )
        return _response.data

    async def protoform_conformance_v1library_service_create_book(
        self,
        *,
        parent: PublisherName,
        book: ProtoformConformanceV1Book,
        book_id: str,
        request_id: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProtoformConformanceV1Book:
        """
        Parameters
        ----------
        parent : PublisherName

        book : ProtoformConformanceV1Book

        book_id : str

        request_id : typing.Optional[str]

        validate_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtoformConformanceV1Book
            The created book

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProtoformConformanceV1Book

        client = AsyncFernApi()


        async def main() -> None:
            await client.library_rpc.protoform_conformance_v1library_service_create_book(
                parent="publishers/demo-library",
                book=ProtoformConformanceV1Book(
                    display_name="The Protoform Guide",
                    isbn="9783161484100",
                ),
                book_id="protoform-guide",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protoform_conformance_v1library_service_create_book(
            parent=parent,
            book=book,
            book_id=book_id,
            request_id=request_id,
            validate_only=validate_only,
            request_options=request_options,
        )
        return _response.data

    async def protoform_conformance_v1library_service_update_book(
        self,
        *,
        book: ProtoformConformanceV1Book,
        update_mask: str,
        request_id: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        allow_missing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProtoformConformanceV1Book:
        """
        Parameters
        ----------
        book : ProtoformConformanceV1Book

        update_mask : str
            Protobuf JSON FieldMask, such as displayName,note.

        request_id : typing.Optional[str]

        validate_only : typing.Optional[bool]

        allow_missing : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtoformConformanceV1Book
            The updated book with a new etag

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProtoformConformanceV1Book

        client = AsyncFernApi()


        async def main() -> None:
            await client.library_rpc.protoform_conformance_v1library_service_update_book(
                book=ProtoformConformanceV1Book(
                    display_name="The Protoform Guide",
                    isbn="9783161484100",
                ),
                update_mask="displayName,note",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protoform_conformance_v1library_service_update_book(
            book=book,
            update_mask=update_mask,
            request_id=request_id,
            validate_only=validate_only,
            allow_missing=allow_missing,
            request_options=request_options,
        )
        return _response.data

    async def protoform_conformance_v1library_service_delete_book(
        self,
        *,
        name: BookName,
        request_id: typing.Optional[str] = OMIT,
        etag: typing.Optional[str] = OMIT,
        validate_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a book by resource name and etag. The server validates optimistic concurrency, returns a structured Connect error when the version is stale, and responds with an empty protobuf message after successful deletion.

        Parameters
        ----------
        name : BookName

        request_id : typing.Optional[str]

        etag : typing.Optional[str]
            Last observed book etag.

        validate_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Empty protobuf response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.library_rpc.protoform_conformance_v1library_service_delete_book(
                name="publishers/demo-library/books/protoform-guide",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protoform_conformance_v1library_service_delete_book(
            name=name, request_id=request_id, etag=etag, validate_only=validate_only, request_options=request_options
        )
        return _response.data
