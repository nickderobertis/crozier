

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.thumbnail_series_collection_dto import ThumbnailSeriesCollectionDto
from .raw_client import AsyncRawCollectionPosterClient, RawCollectionPosterClient


OMIT = typing.cast(typing.Any, ...)


class CollectionPosterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionPosterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionPosterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionPosterClient
        """
        return self._raw_client

    def get_collection_thumbnail(
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
        client.collection_poster.get_collection_thumbnail(
            id="id",
        )
        """
        with self._raw_client.get_collection_thumbnail(id, request_options=request_options) as r:
            yield from r.data

    def get_collection_thumbnails(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThumbnailSeriesCollectionDto]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThumbnailSeriesCollectionDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collection_poster.get_collection_thumbnails(
            id="id",
        )
        """
        _response = self._raw_client.get_collection_thumbnails(id, request_options=request_options)
        return _response.data

    def add_user_uploaded_collection_thumbnail(
        self,
        id: str,
        *,
        file: core.File,
        selected: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThumbnailSeriesCollectionDto:
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
        ThumbnailSeriesCollectionDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.collection_poster.add_user_uploaded_collection_thumbnail(
            id="id",
        )
        """
        _response = self._raw_client.add_user_uploaded_collection_thumbnail(
            id, file=file, selected=selected, request_options=request_options
        )
        return _response.data

    def get_collection_thumbnail_by_id(
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
        client.collection_poster.get_collection_thumbnail_by_id(
            id="id",
            thumbnail_id="thumbnailId",
        )
        """
        with self._raw_client.get_collection_thumbnail_by_id(id, thumbnail_id, request_options=request_options) as r:
            yield from r.data

    def delete_user_uploaded_collection_thumbnail(
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
        client.collection_poster.delete_user_uploaded_collection_thumbnail(
            id="id",
            thumbnail_id="thumbnailId",
        )
        """
        _response = self._raw_client.delete_user_uploaded_collection_thumbnail(
            id, thumbnail_id, request_options=request_options
        )
        return _response.data

    def mark_collection_thumbnail_selected(
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
        client.collection_poster.mark_collection_thumbnail_selected(
            id="id",
            thumbnail_id="thumbnailId",
        )
        """
        _response = self._raw_client.mark_collection_thumbnail_selected(
            id, thumbnail_id, request_options=request_options
        )
        return _response.data


class AsyncCollectionPosterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionPosterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionPosterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionPosterClient
        """
        return self._raw_client

    async def get_collection_thumbnail(
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
            await client.collection_poster.get_collection_thumbnail(
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_collection_thumbnail(id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_collection_thumbnails(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThumbnailSeriesCollectionDto]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThumbnailSeriesCollectionDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collection_poster.get_collection_thumbnails(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection_thumbnails(id, request_options=request_options)
        return _response.data

    async def add_user_uploaded_collection_thumbnail(
        self,
        id: str,
        *,
        file: core.File,
        selected: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThumbnailSeriesCollectionDto:
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
        ThumbnailSeriesCollectionDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.collection_poster.add_user_uploaded_collection_thumbnail(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_user_uploaded_collection_thumbnail(
            id, file=file, selected=selected, request_options=request_options
        )
        return _response.data

    async def get_collection_thumbnail_by_id(
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
            await client.collection_poster.get_collection_thumbnail_by_id(
                id="id",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_collection_thumbnail_by_id(
            id, thumbnail_id, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def delete_user_uploaded_collection_thumbnail(
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
            await client.collection_poster.delete_user_uploaded_collection_thumbnail(
                id="id",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_uploaded_collection_thumbnail(
            id, thumbnail_id, request_options=request_options
        )
        return _response.data

    async def mark_collection_thumbnail_selected(
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
            await client.collection_poster.mark_collection_thumbnail_selected(
                id="id",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_collection_thumbnail_selected(
            id, thumbnail_id, request_options=request_options
        )
        return _response.data
