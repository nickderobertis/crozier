

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStationsClient, RawStationsClient
from .types.follow_levels_response import FollowLevelsResponse


class StationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStationsClient
        """
        return self._raw_client

    def follow_levels(
        self, station_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[FollowLevelsResponse]:
        """
        Parameters
        ----------
        station_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[FollowLevelsResponse]
            Water level readings as the tide turns.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.stations.follow_levels(
            station_id="stationId",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.follow_levels(station_id, request_options=request_options) as r:
            yield from r.data


class AsyncStationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStationsClient
        """
        return self._raw_client

    async def follow_levels(
        self, station_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[FollowLevelsResponse]:
        """
        Parameters
        ----------
        station_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[FollowLevelsResponse]
            Water level readings as the tide turns.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.stations.follow_levels(
                station_id="stationId",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.follow_levels(station_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
