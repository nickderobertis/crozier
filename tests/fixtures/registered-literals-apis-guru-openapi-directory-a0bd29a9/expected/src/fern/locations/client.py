

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.location_info_result import LocationInfoResult
from ..types.locations_result import LocationsResult
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

    def get_api_v1locations(self, *, request_options: typing.Optional[RequestOptions] = None) -> LocationsResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LocationsResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.locations.get_api_v1locations()
        """
        _response = self._raw_client.get_api_v1locations(request_options=request_options)
        return _response.data

    def get_api_v1locations_location(
        self,
        location: str,
        *,
        plan_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LocationInfoResult:
        """
        Parameters
        ----------
        location : str

        plan_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LocationInfoResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.locations.get_api_v1locations_location(
            location="location",
        )
        """
        _response = self._raw_client.get_api_v1locations_location(
            location, plan_id=plan_id, request_options=request_options
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

    async def get_api_v1locations(self, *, request_options: typing.Optional[RequestOptions] = None) -> LocationsResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LocationsResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.get_api_v1locations()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1locations(request_options=request_options)
        return _response.data

    async def get_api_v1locations_location(
        self,
        location: str,
        *,
        plan_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LocationInfoResult:
        """
        Parameters
        ----------
        location : str

        plan_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LocationInfoResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.get_api_v1locations_location(
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1locations_location(
            location, plan_id=plan_id, request_options=request_options
        )
        return _response.data
