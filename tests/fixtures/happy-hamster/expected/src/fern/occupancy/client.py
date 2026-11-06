

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.location import Location
from ..types.location_id import LocationId
from .raw_client import AsyncRawOccupancyClient, RawOccupancyClient
from .types.occupancy_report_client_type import OccupancyReportClientType


OMIT = typing.cast(typing.Any, ...)


class OccupancyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOccupancyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOccupancyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOccupancyClient
        """
        return self._raw_client

    def add_occupancy(
        self,
        id: LocationId,
        *,
        occupancy: float,
        client_type: OccupancyReportClientType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Location:
        """
        Add or remove current capacity.

        Parameters
        ----------
        id : LocationId
            id of the place

        occupancy : float
            Occupancy

        client_type : OccupancyReportClientType
            Type of the client which reported the occupancy

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Success

        Examples
        --------
        from fern.occupancy import OccupancyReportClientType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.occupancy.add_occupancy(
            id=73621836,
            occupancy=0.75,
            client_type=OccupancyReportClientType.IOT,
        )
        """
        _response = self._raw_client.add_occupancy(
            id, occupancy=occupancy, client_type=client_type, request_options=request_options
        )
        return _response.data


class AsyncOccupancyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOccupancyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOccupancyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOccupancyClient
        """
        return self._raw_client

    async def add_occupancy(
        self,
        id: LocationId,
        *,
        occupancy: float,
        client_type: OccupancyReportClientType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Location:
        """
        Add or remove current capacity.

        Parameters
        ----------
        id : LocationId
            id of the place

        occupancy : float
            Occupancy

        client_type : OccupancyReportClientType
            Type of the client which reported the occupancy

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Success

        Examples
        --------
        import asyncio

        from fern.occupancy import OccupancyReportClientType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.occupancy.add_occupancy(
                id=73621836,
                occupancy=0.75,
                client_type=OccupancyReportClientType.IOT,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_occupancy(
            id, occupancy=occupancy, client_type=client_type, request_options=request_options
        )
        return _response.data
