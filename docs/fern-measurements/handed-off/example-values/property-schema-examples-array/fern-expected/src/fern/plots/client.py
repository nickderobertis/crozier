

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPlotsClient, RawPlotsClient
from .types.plot_course_response import PlotCourseResponse


OMIT = typing.cast(typing.Any, ...)


class PlotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlotsClient
        """
        return self._raw_client

    def plot_course(
        self,
        *,
        waypoints: typing.Sequence[str],
        vessel: str,
        legs: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlotCourseResponse:
        """
        Parameters
        ----------
        waypoints : typing.Sequence[str]

        vessel : str

        legs : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlotCourseResponse
            Plotted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plots.plot_course(
            waypoints=[
                "50.1N 5.0W",
                'hold at "Wolf Rock"',
                'log\tthen "sound" at C:\\charts',
                "50.3N 4.8W",
            ],
            vessel="Morwenna",
            legs=4,
        )
        """
        _response = self._raw_client.plot_course(
            waypoints=waypoints, vessel=vessel, legs=legs, request_options=request_options
        )
        return _response.data


class AsyncPlotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlotsClient
        """
        return self._raw_client

    async def plot_course(
        self,
        *,
        waypoints: typing.Sequence[str],
        vessel: str,
        legs: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlotCourseResponse:
        """
        Parameters
        ----------
        waypoints : typing.Sequence[str]

        vessel : str

        legs : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlotCourseResponse
            Plotted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plots.plot_course(
                waypoints=[
                    "50.1N 5.0W",
                    'hold at "Wolf Rock"',
                    'log\tthen "sound" at C:\\charts',
                    "50.3N 4.8W",
                ],
                vessel="Morwenna",
                legs=4,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.plot_course(
            waypoints=waypoints, vessel=vessel, legs=legs, request_options=request_options
        )
        return _response.data
