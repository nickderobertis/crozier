

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.page_read_list_dto import PageReadListDto
from ..types.read_list_dto import ReadListDto
from ..types.streaming_response_body import StreamingResponseBody
from .raw_client import AsyncRawReadlistsClient, RawReadlistsClient


OMIT = typing.cast(typing.Any, ...)


class ReadlistsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReadlistsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReadlistsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReadlistsClient
        """
        return self._raw_client

    def get_read_lists(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageReadListDto:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageReadListDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.readlists.get_read_lists()
        """
        _response = self._raw_client.get_read_lists(
            search=search, library_id=library_id, unpaged=unpaged, page=page, size=size, request_options=request_options
        )
        return _response.data

    def create_read_list(
        self,
        *,
        book_ids: typing.Sequence[str],
        name: str,
        ordered: bool,
        summary: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReadListDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_ids : typing.Sequence[str]

        name : str

        ordered : bool

        summary : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadListDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.readlists.create_read_list(
            book_ids=["bookIds"],
            name="name",
            ordered=True,
            summary="summary",
        )
        """
        _response = self._raw_client.create_read_list(
            book_ids=book_ids, name=name, ordered=ordered, summary=summary, request_options=request_options
        )
        return _response.data

    def get_read_list_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ReadListDto:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadListDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.readlists.get_read_list_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_read_list_by_id(id, request_options=request_options)
        return _response.data

    def delete_read_list_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
        client.readlists.delete_read_list_by_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_read_list_by_id(id, request_options=request_options)
        return _response.data

    def update_read_list_by_id(
        self,
        id: str,
        *,
        book_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        ordered: typing.Optional[bool] = OMIT,
        summary: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        book_ids : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        ordered : typing.Optional[bool]

        summary : typing.Optional[str]

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
        client.readlists.update_read_list_by_id(
            id="id",
        )
        """
        _response = self._raw_client.update_read_list_by_id(
            id, book_ids=book_ids, name=name, ordered=ordered, summary=summary, request_options=request_options
        )
        return _response.data

    def download_read_list_as_zip(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamingResponseBody:
        """
        Download the whole readlist as a ZIP file.

        Required role: **FILE_DOWNLOAD**

        Parameters
        ----------
        id : str

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
        client.readlists.download_read_list_as_zip(
            id="id",
        )
        """
        _response = self._raw_client.download_read_list_as_zip(id, request_options=request_options)
        return _response.data


class AsyncReadlistsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReadlistsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReadlistsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReadlistsClient
        """
        return self._raw_client

    async def get_read_lists(
        self,
        *,
        search: typing.Optional[str] = None,
        library_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageReadListDto:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        library_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageReadListDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.readlists.get_read_lists()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_read_lists(
            search=search, library_id=library_id, unpaged=unpaged, page=page, size=size, request_options=request_options
        )
        return _response.data

    async def create_read_list(
        self,
        *,
        book_ids: typing.Sequence[str],
        name: str,
        ordered: bool,
        summary: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReadListDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        book_ids : typing.Sequence[str]

        name : str

        ordered : bool

        summary : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadListDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.readlists.create_read_list(
                book_ids=["bookIds"],
                name="name",
                ordered=True,
                summary="summary",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_read_list(
            book_ids=book_ids, name=name, ordered=ordered, summary=summary, request_options=request_options
        )
        return _response.data

    async def get_read_list_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReadListDto:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadListDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.readlists.get_read_list_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_read_list_by_id(id, request_options=request_options)
        return _response.data

    async def delete_read_list_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
            await client.readlists.delete_read_list_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_read_list_by_id(id, request_options=request_options)
        return _response.data

    async def update_read_list_by_id(
        self,
        id: str,
        *,
        book_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        ordered: typing.Optional[bool] = OMIT,
        summary: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        book_ids : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        ordered : typing.Optional[bool]

        summary : typing.Optional[str]

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
            await client.readlists.update_read_list_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_read_list_by_id(
            id, book_ids=book_ids, name=name, ordered=ordered, summary=summary, request_options=request_options
        )
        return _response.data

    async def download_read_list_as_zip(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamingResponseBody:
        """
        Download the whole readlist as a ZIP file.

        Required role: **FILE_DOWNLOAD**

        Parameters
        ----------
        id : str

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
            await client.readlists.download_read_list_as_zip(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_read_list_as_zip(id, request_options=request_options)
        return _response.data
