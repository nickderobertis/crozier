

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stored_location import StoredLocation
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

    def returns_a_list_with_the_registered_locations_of_the_underlying_infrastructure(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[StoredLocation]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[StoredLocation]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.locations.returns_a_list_with_the_registered_locations_of_the_underlying_infrastructure()
        """
        _response = self._raw_client.returns_a_list_with_the_registered_locations_of_the_underlying_infrastructure(
            request_options=request_options
        )
        return _response.data

    def defines_a_location_for_the_platform(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.locations.defines_a_location_for_the_platform()
        """
        _response = self._raw_client.defines_a_location_for_the_platform(request_options=request_options)
        return _response.data

    def return_info_about_a_specific_location(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StoredLocation:
        """
        Parameters
        ----------
        id : str
            ID of location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoredLocation
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.locations.return_info_about_a_specific_location(
            id="id",
        )
        """
        _response = self._raw_client.return_info_about_a_specific_location(id, request_options=request_options)
        return _response.data

    def add_or_update_a_location(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str
            ID of location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.locations.add_or_update_a_location(
            id="id",
        )
        """
        _response = self._raw_client.add_or_update_a_location(id, request_options=request_options)
        return _response.data

    def delete_a_base_slice_descriptor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            ID of location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.locations.delete_a_base_slice_descriptor(
            id="id",
        )
        """
        _response = self._raw_client.delete_a_base_slice_descriptor(id, request_options=request_options)
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

    async def returns_a_list_with_the_registered_locations_of_the_underlying_infrastructure(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[StoredLocation]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[StoredLocation]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.locations.returns_a_list_with_the_registered_locations_of_the_underlying_infrastructure()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.returns_a_list_with_the_registered_locations_of_the_underlying_infrastructure(
                request_options=request_options
            )
        )
        return _response.data

    async def defines_a_location_for_the_platform(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.locations.defines_a_location_for_the_platform()


        asyncio.run(main())
        """
        _response = await self._raw_client.defines_a_location_for_the_platform(request_options=request_options)
        return _response.data

    async def return_info_about_a_specific_location(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StoredLocation:
        """
        Parameters
        ----------
        id : str
            ID of location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoredLocation
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.locations.return_info_about_a_specific_location(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_info_about_a_specific_location(id, request_options=request_options)
        return _response.data

    async def add_or_update_a_location(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            ID of location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.locations.add_or_update_a_location(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_or_update_a_location(id, request_options=request_options)
        return _response.data

    async def delete_a_base_slice_descriptor(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            ID of location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.locations.delete_a_base_slice_descriptor(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_base_slice_descriptor(id, request_options=request_options)
        return _response.data
