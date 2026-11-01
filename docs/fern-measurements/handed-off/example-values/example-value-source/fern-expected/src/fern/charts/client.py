

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChartsClient, RawChartsClient
from .types.upload_chart_response import UploadChartResponse


OMIT = typing.cast(typing.Any, ...)


class ChartsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChartsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChartsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChartsClient
        """
        return self._raw_client

    def upload_chart(
        self,
        *,
        sheet: core.File,
        title: str,
        revision: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadChartResponse:
        """
        A multipart text part's own example.

        Parameters
        ----------
        sheet : core.File
            See core.File for more documentation

        title : str

        revision : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadChartResponse
            Uploaded

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.charts.upload_chart(
            title="title",
        )
        """
        _response = self._raw_client.upload_chart(
            sheet=sheet, title=title, revision=revision, request_options=request_options
        )
        return _response.data

    def print_chart(
        self, chart_id: str, *, scale: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        A binary download's query parameter example.

        Parameters
        ----------
        chart_id : str

        scale : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The sheet

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.charts.print_chart(
            chart_id="chartId",
            scale="scale",
        )
        """
        with self._raw_client.print_chart(chart_id, scale=scale, request_options=request_options) as r:
            yield from r.data

    def bundle_charts(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        A top-level array body's media-type example on a binary download.

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The bundle
        """
        with self._raw_client.bundle_charts(request=request, request_options=request_options) as r:
            yield from r.data


class AsyncChartsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChartsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChartsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChartsClient
        """
        return self._raw_client

    async def upload_chart(
        self,
        *,
        sheet: core.File,
        title: str,
        revision: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadChartResponse:
        """
        A multipart text part's own example.

        Parameters
        ----------
        sheet : core.File
            See core.File for more documentation

        title : str

        revision : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadChartResponse
            Uploaded

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.charts.upload_chart(
                title="title",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_chart(
            sheet=sheet, title=title, revision=revision, request_options=request_options
        )
        return _response.data

    async def print_chart(
        self, chart_id: str, *, scale: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        A binary download's query parameter example.

        Parameters
        ----------
        chart_id : str

        scale : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The sheet

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.charts.print_chart(
                chart_id="chartId",
                scale="scale",
            )


        asyncio.run(main())
        """
        async with self._raw_client.print_chart(chart_id, scale=scale, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def bundle_charts(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        A top-level array body's media-type example on a binary download.

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The bundle
        """
        async with self._raw_client.bundle_charts(request=request, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
