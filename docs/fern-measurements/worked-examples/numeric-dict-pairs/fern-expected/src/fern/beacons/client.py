

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBeaconsClient, RawBeaconsClient


OMIT = typing.cast(typing.Any, ...)


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

    def place_beacon(
        self,
        *,
        position: typing.Dict[str, float],
        labels: typing.Dict[str, str],
        toggles: typing.Dict[str, bool],
        offset: typing.Dict[str, int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        position : typing.Dict[str, float]
            Two numeric pairs.

        labels : typing.Dict[str, str]
            Two string pairs.

        toggles : typing.Dict[str, bool]
            Two boolean pairs.

        offset : typing.Dict[str, int]
            One numeric pair (control).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.beacons.place_beacon(
            position={"lat": 41.5, "lon": -70.25},
            labels={"north": "tall", "south": "squat"},
            toggles={"lamp": True, "horn": False},
            offset={"dx": 3},
        )
        """
        _response = self._raw_client.place_beacon(
            position=position, labels=labels, toggles=toggles, offset=offset, request_options=request_options
        )
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

    async def place_beacon(
        self,
        *,
        position: typing.Dict[str, float],
        labels: typing.Dict[str, str],
        toggles: typing.Dict[str, bool],
        offset: typing.Dict[str, int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        position : typing.Dict[str, float]
            Two numeric pairs.

        labels : typing.Dict[str, str]
            Two string pairs.

        toggles : typing.Dict[str, bool]
            Two boolean pairs.

        offset : typing.Dict[str, int]
            One numeric pair (control).

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
            await client.beacons.place_beacon(
                position={"lat": 41.5, "lon": -70.25},
                labels={"north": "tall", "south": "squat"},
                toggles={"lamp": True, "horn": False},
                offset={"dx": 3},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.place_beacon(
            position=position, labels=labels, toggles=toggles, offset=offset, request_options=request_options
        )
        return _response.data
