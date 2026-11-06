

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.coordinates import Coordinates
from ..types.location import Location
from ..types.location_id import LocationId
from ..types.location_search_result import LocationSearchResult
from ..types.location_type import LocationType
from .raw_client import AsyncRawLocationsClient, RawLocationsClient


class LocationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLocationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLocationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLocationsClient
        """
        return self._raw_client

    def get_locations_by_coordinates(
        self,
        *,
        coordinates: Coordinates,
        type: typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Location]:
        """
        Searches for locations in the given range.

        Parameters
        ----------
        coordinates : Coordinates
            Latitude and Longitude

        type : typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]]
            Location Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Location]
            Success

        Examples
        --------
        from fern import Coordinates, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.locations.get_locations_by_coordinates(
            coordinates=Coordinates(
                latitude=1.1,
                longitude=1.1,
            ),
        )
        """
        _response = self._raw_client.get_locations_by_coordinates(
            coordinates=coordinates, type=type, request_options=request_options
        )
        return _response.data

    def get_location_by_id(
        self, id: LocationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Location:
        """
        Get details for a specific location.

        Parameters
        ----------
        id : LocationId
            id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.locations.get_location_by_id(
            id=73621836,
        )
        """
        _response = self._raw_client.get_location_by_id(id, request_options=request_options)
        return _response.data

    def search_locations(
        self,
        query: str,
        *,
        coordinates: typing.Optional[Coordinates] = None,
        type: typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LocationSearchResult:
        """
        Returns the Coordinate and Locations around the 'Search Query'.

        Parameters
        ----------
        query : str
            Search query

        coordinates : typing.Optional[Coordinates]
            Latitude and Longitude

        type : typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]]
            Location Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LocationSearchResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.locations.search_locations(
            query="query",
        )
        """
        _response = self._raw_client.search_locations(
            query, coordinates=coordinates, type=type, request_options=request_options
        )
        return _response.data


class AsyncLocationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLocationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLocationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLocationsClient
        """
        return self._raw_client

    async def get_locations_by_coordinates(
        self,
        *,
        coordinates: Coordinates,
        type: typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Location]:
        """
        Searches for locations in the given range.

        Parameters
        ----------
        coordinates : Coordinates
            Latitude and Longitude

        type : typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]]
            Location Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Location]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Coordinates

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.get_locations_by_coordinates(
                coordinates=Coordinates(
                    latitude=1.1,
                    longitude=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_locations_by_coordinates(
            coordinates=coordinates, type=type, request_options=request_options
        )
        return _response.data

    async def get_location_by_id(
        self, id: LocationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Location:
        """
        Get details for a specific location.

        Parameters
        ----------
        id : LocationId
            id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.get_location_by_id(
                id=73621836,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_location_by_id(id, request_options=request_options)
        return _response.data

    async def search_locations(
        self,
        query: str,
        *,
        coordinates: typing.Optional[Coordinates] = None,
        type: typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LocationSearchResult:
        """
        Returns the Coordinate and Locations around the 'Search Query'.

        Parameters
        ----------
        query : str
            Search query

        coordinates : typing.Optional[Coordinates]
            Latitude and Longitude

        type : typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]]
            Location Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LocationSearchResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.search_locations(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_locations(
            query, coordinates=coordinates, type=type, request_options=request_options
        )
        return _response.data
