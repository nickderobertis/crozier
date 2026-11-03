

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStationsClient, RawStationsClient
from .types.station_mount import StationMount


OMIT = typing.cast(typing.Any, ...)


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

    def register_station(
        self,
        *,
        name: str,
        mount: typing.Optional[StationMount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        mount : typing.Optional[StationMount]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stations.register_station(
            name="name",
        )
        """
        _response = self._raw_client.register_station(name=name, mount=mount, request_options=request_options)
        return _response.data


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

    async def register_station(
        self,
        *,
        name: str,
        mount: typing.Optional[StationMount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        mount : typing.Optional[StationMount]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stations.register_station(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_station(name=name, mount=mount, request_options=request_options)
        return _response.data
