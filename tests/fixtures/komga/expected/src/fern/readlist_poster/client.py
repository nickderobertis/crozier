

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.thumbnail_read_list_dto import ThumbnailReadListDto
from .raw_client import AsyncRawReadlistPosterClient, RawReadlistPosterClient


OMIT = typing.cast(typing.Any, ...)


class ReadlistPosterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReadlistPosterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReadlistPosterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReadlistPosterClient
        """
        return self._raw_client

    def get_read_list_thumbnail(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        id : str

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
        client.readlist_poster.get_read_list_thumbnail(
            id="id",
        )
        """
        with self._raw_client.get_read_list_thumbnail(id, request_options=request_options) as r:
            yield from r.data

    def get_read_list_thumbnails(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThumbnailReadListDto]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThumbnailReadListDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.readlist_poster.get_read_list_thumbnails(
            id="id",
        )
        """
        _response = self._raw_client.get_read_list_thumbnails(id, request_options=request_options)
        return _response.data

    def add_user_uploaded_read_list_thumbnail(
        self,
        id: str,
        *,
        file: core.File,
        selected: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThumbnailReadListDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        file : core.File
            See core.File for more documentation

        selected : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThumbnailReadListDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.readlist_poster.add_user_uploaded_read_list_thumbnail(
            id="id",
        )
        """
        _response = self._raw_client.add_user_uploaded_read_list_thumbnail(
            id, file=file, selected=selected, request_options=request_options
        )
        return _response.data

    def get_read_list_thumbnail_by_id(
        self, id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        id : str

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
        client.readlist_poster.get_read_list_thumbnail_by_id(
            id="id",
            thumbnail_id="thumbnailId",
        )
        """
        with self._raw_client.get_read_list_thumbnail_by_id(id, thumbnail_id, request_options=request_options) as r:
            yield from r.data

    def delete_user_uploaded_read_list_thumbnail(
        self, id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
        client.readlist_poster.delete_user_uploaded_read_list_thumbnail(
            id="id",
            thumbnail_id="thumbnailId",
        )
        """
        _response = self._raw_client.delete_user_uploaded_read_list_thumbnail(
            id, thumbnail_id, request_options=request_options
        )
        return _response.data

    def mark_read_list_thumbnail_selected(
        self, id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
        client.readlist_poster.mark_read_list_thumbnail_selected(
            id="id",
            thumbnail_id="thumbnailId",
        )
        """
        _response = self._raw_client.mark_read_list_thumbnail_selected(
            id, thumbnail_id, request_options=request_options
        )
        return _response.data


class AsyncReadlistPosterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReadlistPosterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReadlistPosterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReadlistPosterClient
        """
        return self._raw_client

    async def get_read_list_thumbnail(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        id : str

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
            await client.readlist_poster.get_read_list_thumbnail(
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_read_list_thumbnail(id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_read_list_thumbnails(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThumbnailReadListDto]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThumbnailReadListDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.readlist_poster.get_read_list_thumbnails(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_read_list_thumbnails(id, request_options=request_options)
        return _response.data

    async def add_user_uploaded_read_list_thumbnail(
        self,
        id: str,
        *,
        file: core.File,
        selected: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThumbnailReadListDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        file : core.File
            See core.File for more documentation

        selected : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThumbnailReadListDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.readlist_poster.add_user_uploaded_read_list_thumbnail(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_user_uploaded_read_list_thumbnail(
            id, file=file, selected=selected, request_options=request_options
        )
        return _response.data

    async def get_read_list_thumbnail_by_id(
        self, id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        id : str

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
            await client.readlist_poster.get_read_list_thumbnail_by_id(
                id="id",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_read_list_thumbnail_by_id(
            id, thumbnail_id, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def delete_user_uploaded_read_list_thumbnail(
        self, id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
            await client.readlist_poster.delete_user_uploaded_read_list_thumbnail(
                id="id",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_uploaded_read_list_thumbnail(
            id, thumbnail_id, request_options=request_options
        )
        return _response.data

    async def mark_read_list_thumbnail_selected(
        self, id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
            await client.readlist_poster.mark_read_list_thumbnail_selected(
                id="id",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_read_list_thumbnail_selected(
            id, thumbnail_id, request_options=request_options
        )
        return _response.data
