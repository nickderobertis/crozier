

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_beacons_request_range import ListBeaconsRequestRange
from ..types.list_beacons_request_weight import ListBeaconsRequestWeight
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

    def list_beacons(
        self,
        *,
        range: typing.Optional[ListBeaconsRequestRange] = None,
        weight: typing.Optional[ListBeaconsRequestWeight] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        range : typing.Optional[ListBeaconsRequestRange]
            A range label, or a range in metres.

        weight : typing.Optional[ListBeaconsRequestWeight]
            A weight label, or a weight in grams.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The beacons.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.beacons.list_beacons()
        """
        _response = self._raw_client.list_beacons(range=range, weight=weight, request_options=request_options)
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

    async def list_beacons(
        self,
        *,
        range: typing.Optional[ListBeaconsRequestRange] = None,
        weight: typing.Optional[ListBeaconsRequestWeight] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        range : typing.Optional[ListBeaconsRequestRange]
            A range label, or a range in metres.

        weight : typing.Optional[ListBeaconsRequestWeight]
            A weight label, or a weight in grams.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The beacons.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.beacons.list_beacons()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_beacons(range=range, weight=weight, request_options=request_options)
        return _response.data
