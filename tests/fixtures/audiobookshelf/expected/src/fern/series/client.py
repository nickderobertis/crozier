

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.series import Series
from ..types.series_description import SeriesDescription
from ..types.series_id import SeriesId
from ..types.series_name import SeriesName
from ..types.series_with_progress_and_rss import SeriesWithProgressAndRss
from .raw_client import AsyncRawSeriesClient, RawSeriesClient


OMIT = typing.cast(typing.Any, ...)


class SeriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSeriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSeriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSeriesClient
        """
        return self._raw_client

    def get_series(
        self, id: SeriesId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SeriesWithProgressAndRss:
        """
        Get a series by ID.

        Parameters
        ----------
        id : SeriesId
            The ID of the series.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeriesWithProgressAndRss
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.series.get_series(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.get_series(id, request_options=request_options)
        return _response.data

    def update_series(
        self,
        id: SeriesId,
        *,
        name: typing.Optional[SeriesName] = OMIT,
        description: typing.Optional[SeriesDescription] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Series:
        """
        Update a series by ID.

        Parameters
        ----------
        id : SeriesId
            The ID of the series.

        name : typing.Optional[SeriesName]

        description : typing.Optional[SeriesDescription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Series
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.series.update_series(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.update_series(
            id, name=name, description=description, request_options=request_options
        )
        return _response.data


class AsyncSeriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSeriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSeriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSeriesClient
        """
        return self._raw_client

    async def get_series(
        self, id: SeriesId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SeriesWithProgressAndRss:
        """
        Get a series by ID.

        Parameters
        ----------
        id : SeriesId
            The ID of the series.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeriesWithProgressAndRss
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.series.get_series(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_series(id, request_options=request_options)
        return _response.data

    async def update_series(
        self,
        id: SeriesId,
        *,
        name: typing.Optional[SeriesName] = OMIT,
        description: typing.Optional[SeriesDescription] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Series:
        """
        Update a series by ID.

        Parameters
        ----------
        id : SeriesId
            The ID of the series.

        name : typing.Optional[SeriesName]

        description : typing.Optional[SeriesDescription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Series
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.series.update_series(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_series(
            id, name=name, description=description, request_options=request_options
        )
        return _response.data
