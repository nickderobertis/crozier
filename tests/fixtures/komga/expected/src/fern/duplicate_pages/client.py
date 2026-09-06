

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.page_page_hash_known_dto import PagePageHashKnownDto
from ..types.page_page_hash_match_dto import PagePageHashMatchDto
from ..types.page_page_hash_unknown_dto import PagePageHashUnknownDto
from .raw_client import AsyncRawDuplicatePagesClient, RawDuplicatePagesClient
from .types.get_known_page_hashes_request_action_item import GetKnownPageHashesRequestActionItem
from .types.page_hash_creation_dto_action import PageHashCreationDtoAction


OMIT = typing.cast(typing.Any, ...)


class DuplicatePagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDuplicatePagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDuplicatePagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDuplicatePagesClient
        """
        return self._raw_client

    def get_known_page_hashes(
        self,
        *,
        action: typing.Optional[
            typing.Union[GetKnownPageHashesRequestActionItem, typing.Sequence[GetKnownPageHashesRequestActionItem]]
        ] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePageHashKnownDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        action : typing.Optional[typing.Union[GetKnownPageHashesRequestActionItem, typing.Sequence[GetKnownPageHashesRequestActionItem]]]

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
        PagePageHashKnownDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.duplicate_pages.get_known_page_hashes()
        """
        _response = self._raw_client.get_known_page_hashes(
            action=action, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def create_or_update_known_page_hash(
        self,
        *,
        action: PageHashCreationDtoAction,
        hash: str,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        action : PageHashCreationDtoAction

        hash : str

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.duplicate_pages import PageHashCreationDtoAction

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.duplicate_pages.create_or_update_known_page_hash(
            action=PageHashCreationDtoAction.DELETE_AUTO,
            hash="hash",
        )
        """
        _response = self._raw_client.create_or_update_known_page_hash(
            action=action, hash=hash, size=size, request_options=request_options
        )
        return _response.data

    def get_unknown_page_hashes(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePageHashUnknownDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
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
        PagePageHashUnknownDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.duplicate_pages.get_unknown_page_hashes()
        """
        _response = self._raw_client.get_unknown_page_hashes(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_unknown_page_hash_thumbnail(
        self,
        page_hash: str,
        *,
        resize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

        resize : typing.Optional[int]

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
        client.duplicate_pages.get_unknown_page_hash_thumbnail(
            page_hash="pageHash",
        )
        """
        with self._raw_client.get_unknown_page_hash_thumbnail(
            page_hash, resize=resize, request_options=request_options
        ) as r:
            yield from r.data

    def get_page_hash_matches(
        self,
        page_hash: str,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePageHashMatchDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

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
        PagePageHashMatchDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.duplicate_pages.get_page_hash_matches(
            page_hash="pageHash",
        )
        """
        _response = self._raw_client.get_page_hash_matches(
            page_hash, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def delete_duplicate_pages_by_page_hash(
        self, page_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

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
        client.duplicate_pages.delete_duplicate_pages_by_page_hash(
            page_hash="pageHash",
        )
        """
        _response = self._raw_client.delete_duplicate_pages_by_page_hash(page_hash, request_options=request_options)
        return _response.data

    def delete_single_match_by_page_hash(
        self,
        page_hash: str,
        *,
        book_id: str,
        file_name: str,
        file_size: int,
        media_type: str,
        page_number: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

        book_id : str

        file_name : str

        file_size : int

        media_type : str

        page_number : int

        url : str

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
        client.duplicate_pages.delete_single_match_by_page_hash(
            page_hash="pageHash",
            book_id="bookId",
            file_name="fileName",
            file_size=1000000,
            media_type="mediaType",
            page_number=1,
            url="url",
        )
        """
        _response = self._raw_client.delete_single_match_by_page_hash(
            page_hash,
            book_id=book_id,
            file_name=file_name,
            file_size=file_size,
            media_type=media_type,
            page_number=page_number,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def get_known_page_hash_thumbnail(
        self, page_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

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
        client.duplicate_pages.get_known_page_hash_thumbnail(
            page_hash="pageHash",
        )
        """
        with self._raw_client.get_known_page_hash_thumbnail(page_hash, request_options=request_options) as r:
            yield from r.data


class AsyncDuplicatePagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDuplicatePagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDuplicatePagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDuplicatePagesClient
        """
        return self._raw_client

    async def get_known_page_hashes(
        self,
        *,
        action: typing.Optional[
            typing.Union[GetKnownPageHashesRequestActionItem, typing.Sequence[GetKnownPageHashesRequestActionItem]]
        ] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePageHashKnownDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        action : typing.Optional[typing.Union[GetKnownPageHashesRequestActionItem, typing.Sequence[GetKnownPageHashesRequestActionItem]]]

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
        PagePageHashKnownDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.duplicate_pages.get_known_page_hashes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_known_page_hashes(
            action=action, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def create_or_update_known_page_hash(
        self,
        *,
        action: PageHashCreationDtoAction,
        hash: str,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        action : PageHashCreationDtoAction

        hash : str

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.duplicate_pages import PageHashCreationDtoAction

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.duplicate_pages.create_or_update_known_page_hash(
                action=PageHashCreationDtoAction.DELETE_AUTO,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update_known_page_hash(
            action=action, hash=hash, size=size, request_options=request_options
        )
        return _response.data

    async def get_unknown_page_hashes(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePageHashUnknownDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
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
        PagePageHashUnknownDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.duplicate_pages.get_unknown_page_hashes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_unknown_page_hashes(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_unknown_page_hash_thumbnail(
        self,
        page_hash: str,
        *,
        resize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

        resize : typing.Optional[int]

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
            await client.duplicate_pages.get_unknown_page_hash_thumbnail(
                page_hash="pageHash",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_unknown_page_hash_thumbnail(
            page_hash, resize=resize, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_page_hash_matches(
        self,
        page_hash: str,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePageHashMatchDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

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
        PagePageHashMatchDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.duplicate_pages.get_page_hash_matches(
                page_hash="pageHash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_page_hash_matches(
            page_hash, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def delete_duplicate_pages_by_page_hash(
        self, page_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

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
            await client.duplicate_pages.delete_duplicate_pages_by_page_hash(
                page_hash="pageHash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_duplicate_pages_by_page_hash(
            page_hash, request_options=request_options
        )
        return _response.data

    async def delete_single_match_by_page_hash(
        self,
        page_hash: str,
        *,
        book_id: str,
        file_name: str,
        file_size: int,
        media_type: str,
        page_number: int,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

        book_id : str

        file_name : str

        file_size : int

        media_type : str

        page_number : int

        url : str

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
            await client.duplicate_pages.delete_single_match_by_page_hash(
                page_hash="pageHash",
                book_id="bookId",
                file_name="fileName",
                file_size=1000000,
                media_type="mediaType",
                page_number=1,
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_single_match_by_page_hash(
            page_hash,
            book_id=book_id,
            file_name=file_name,
            file_size=file_size,
            media_type=media_type,
            page_number=page_number,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def get_known_page_hash_thumbnail(
        self, page_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page_hash : str

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
            await client.duplicate_pages.get_known_page_hash_thumbnail(
                page_hash="pageHash",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_known_page_hash_thumbnail(page_hash, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
