

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_location_response import CreateLocationResponse
from ..types.list_locations_response import ListLocationsResponse
from ..types.location import Location
from ..types.retrieve_location_response import RetrieveLocationResponse
from ..types.update_location_response import UpdateLocationResponse
from .raw_client import AsyncRawLocationsClient, RawLocationsClient


OMIT = typing.cast(typing.Any, ...)


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

    def list_locations(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListLocationsResponse:
        """
        Provides information of all locations of a business.

        Many Square API endpoints require a `location_id` parameter.
        The `id` field of the [`Location`](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) objects returned by this
        endpoint correspond to that `location_id` parameter.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLocationsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.locations.list_locations()
        """
        _response = self._raw_client.list_locations(request_options=request_options)
        return _response.data

    def create_location(
        self, *, location: typing.Optional[Location] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateLocationResponse:
        """
        Creates a location.

        Parameters
        ----------
        location : typing.Optional[Location]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLocationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.locations.create_location()
        """
        _response = self._raw_client.create_location(location=location, request_options=request_options)
        return _response.data

    def retrieve_location(
        self, location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveLocationResponse:
        """
        Retrieves details of a location. You can specify "main"
        as the location ID to retrieve details of the
        main location.

        Parameters
        ----------
        location_id : str
            The ID of the location to retrieve. If you specify the string "main",
            then the endpoint returns the main location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveLocationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.locations.retrieve_location(
            location_id="location_id",
        )
        """
        _response = self._raw_client.retrieve_location(location_id, request_options=request_options)
        return _response.data

    def update_location(
        self,
        location_id: str,
        *,
        location: typing.Optional[Location] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateLocationResponse:
        """
        Updates a location.

        Parameters
        ----------
        location_id : str
            The ID of the location to update.

        location : typing.Optional[Location]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLocationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.locations.update_location(
            location_id="location_id",
        )
        """
        _response = self._raw_client.update_location(location_id, location=location, request_options=request_options)
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

    async def list_locations(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListLocationsResponse:
        """
        Provides information of all locations of a business.

        Many Square API endpoints require a `location_id` parameter.
        The `id` field of the [`Location`](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) objects returned by this
        endpoint correspond to that `location_id` parameter.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLocationsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.list_locations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_locations(request_options=request_options)
        return _response.data

    async def create_location(
        self, *, location: typing.Optional[Location] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateLocationResponse:
        """
        Creates a location.

        Parameters
        ----------
        location : typing.Optional[Location]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLocationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.create_location()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_location(location=location, request_options=request_options)
        return _response.data

    async def retrieve_location(
        self, location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveLocationResponse:
        """
        Retrieves details of a location. You can specify "main"
        as the location ID to retrieve details of the
        main location.

        Parameters
        ----------
        location_id : str
            The ID of the location to retrieve. If you specify the string "main",
            then the endpoint returns the main location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveLocationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.retrieve_location(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_location(location_id, request_options=request_options)
        return _response.data

    async def update_location(
        self,
        location_id: str,
        *,
        location: typing.Optional[Location] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateLocationResponse:
        """
        Updates a location.

        Parameters
        ----------
        location_id : str
            The ID of the location to update.

        location : typing.Optional[Location]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLocationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.update_location(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_location(
            location_id, location=location, request_options=request_options
        )
        return _response.data
