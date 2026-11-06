

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.location_type import LocationType
from .raw_client import AsyncRawLocationTypesClient, RawLocationTypesClient


class LocationTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLocationTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLocationTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLocationTypesClient
        """
        return self._raw_client

    def list_location_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Optional[LocationType]]:
        """
        Location Types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Optional[LocationType]]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.location_types.list_location_types()
        """
        _response = self._raw_client.list_location_types(request_options=request_options)
        return _response.data


class AsyncLocationTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLocationTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLocationTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLocationTypesClient
        """
        return self._raw_client

    async def list_location_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Optional[LocationType]]:
        """
        Location Types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Optional[LocationType]]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.location_types.list_location_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_location_types(request_options=request_options)
        return _response.data
