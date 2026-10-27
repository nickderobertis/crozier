

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.beacon import Beacon
from .raw_client import AsyncRawBeaconsClient, RawBeaconsClient


class BeaconsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBeaconsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBeaconsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBeaconsClient
        """
        return self._raw_client

    def get_beacon(self, beacon_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Beacon:
        """
        Returns the beacon's lamp and its schedule. The lamp is lit at dusk.
        A beacon that was retired answers 404.

        Parameters
        ----------
        beacon_id : str
            The beacon's identifier, as #registered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Beacon
            The beacon

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.beacons.get_beacon(
            beacon_id="beaconId",
        )
        """
        _response = self._raw_client.get_beacon(beacon_id, request_options=request_options)
        return _response.data


class AsyncBeaconsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBeaconsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBeaconsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBeaconsClient
        """
        return self._raw_client

    async def get_beacon(self, beacon_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Beacon:
        """
        Returns the beacon's lamp and its schedule. The lamp is lit at dusk.
        A beacon that was retired answers 404.

        Parameters
        ----------
        beacon_id : str
            The beacon's identifier, as #registered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Beacon
            The beacon

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.beacons.get_beacon(
                beacon_id="beaconId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_beacon(beacon_id, request_options=request_options)
        return _response.data
