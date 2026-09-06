

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.thumbnail_series_dto import ThumbnailSeriesDto
from .raw_client import AsyncRawSeriesPosterClient, RawSeriesPosterClient


OMIT = typing.cast(typing.Any, ...)


class SeriesPosterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSeriesPosterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSeriesPosterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSeriesPosterClient
        """
        return self._raw_client

    def get_series_thumbnail(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        series_id : str

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
        client.series_poster.get_series_thumbnail(
            series_id="seriesId",
        )
        """
        with self._raw_client.get_series_thumbnail(series_id, request_options=request_options) as r:
            yield from r.data

    def get_series_thumbnails(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThumbnailSeriesDto]:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThumbnailSeriesDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series_poster.get_series_thumbnails(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.get_series_thumbnails(series_id, request_options=request_options)
        return _response.data

    def add_user_uploaded_series_thumbnail(
        self,
        series_id: str,
        *,
        file: core.File,
        selected: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThumbnailSeriesDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        file : core.File
            See core.File for more documentation

        selected : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThumbnailSeriesDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.series_poster.add_user_uploaded_series_thumbnail(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.add_user_uploaded_series_thumbnail(
            series_id, file=file, selected=selected, request_options=request_options
        )
        return _response.data

    def get_series_thumbnail_by_id(
        self, series_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        series_id : str

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
        client.series_poster.get_series_thumbnail_by_id(
            series_id="seriesId",
            thumbnail_id="thumbnailId",
        )
        """
        with self._raw_client.get_series_thumbnail_by_id(series_id, thumbnail_id, request_options=request_options) as r:
            yield from r.data

    def delete_user_uploaded_series_thumbnail(
        self, series_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

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
        client.series_poster.delete_user_uploaded_series_thumbnail(
            series_id="seriesId",
            thumbnail_id="thumbnailId",
        )
        """
        _response = self._raw_client.delete_user_uploaded_series_thumbnail(
            series_id, thumbnail_id, request_options=request_options
        )
        return _response.data

    def mark_series_thumbnail_selected(
        self, series_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

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
        client.series_poster.mark_series_thumbnail_selected(
            series_id="seriesId",
            thumbnail_id="thumbnailId",
        )
        """
        _response = self._raw_client.mark_series_thumbnail_selected(
            series_id, thumbnail_id, request_options=request_options
        )
        return _response.data


class AsyncSeriesPosterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSeriesPosterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSeriesPosterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSeriesPosterClient
        """
        return self._raw_client

    async def get_series_thumbnail(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        series_id : str

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
            await client.series_poster.get_series_thumbnail(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_series_thumbnail(series_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_series_thumbnails(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThumbnailSeriesDto]:
        """
        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThumbnailSeriesDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series_poster.get_series_thumbnails(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series_thumbnails(series_id, request_options=request_options)
        return _response.data

    async def add_user_uploaded_series_thumbnail(
        self,
        series_id: str,
        *,
        file: core.File,
        selected: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThumbnailSeriesDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

        file : core.File
            See core.File for more documentation

        selected : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThumbnailSeriesDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.series_poster.add_user_uploaded_series_thumbnail(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_user_uploaded_series_thumbnail(
            series_id, file=file, selected=selected, request_options=request_options
        )
        return _response.data

    async def get_series_thumbnail_by_id(
        self, series_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        series_id : str

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
            await client.series_poster.get_series_thumbnail_by_id(
                series_id="seriesId",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_series_thumbnail_by_id(
            series_id, thumbnail_id, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def delete_user_uploaded_series_thumbnail(
        self, series_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

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
            await client.series_poster.delete_user_uploaded_series_thumbnail(
                series_id="seriesId",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_uploaded_series_thumbnail(
            series_id, thumbnail_id, request_options=request_options
        )
        return _response.data

    async def mark_series_thumbnail_selected(
        self, series_id: str, thumbnail_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        series_id : str

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
            await client.series_poster.mark_series_thumbnail_selected(
                series_id="seriesId",
                thumbnail_id="thumbnailId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_series_thumbnail_selected(
            series_id, thumbnail_id, request_options=request_options
        )
        return _response.data
