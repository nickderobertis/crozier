

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMarkersClient, RawMarkersClient
from .types.place_marker_request_marker import PlaceMarkerRequestMarker
from .types.place_marker_response import PlaceMarkerResponse


OMIT = typing.cast(typing.Any, ...)


class MarkersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMarkersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMarkersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMarkersClient
        """
        return self._raw_client

    def place_marker(
        self, *, marker: PlaceMarkerRequestMarker, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaceMarkerResponse:
        """
        A union-typed property's declared example.

        Parameters
        ----------
        marker : PlaceMarkerRequestMarker

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaceMarkerResponse
            Placed

        Examples
        --------
        from fern import BuoyMarker, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.markers.place_marker(
            marker=BuoyMarker(
                colour="colour",
                shape="shape",
            ),
        )
        """
        _response = self._raw_client.place_marker(marker=marker, request_options=request_options)
        return _response.data


class AsyncMarkersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMarkersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMarkersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMarkersClient
        """
        return self._raw_client

    async def place_marker(
        self, *, marker: PlaceMarkerRequestMarker, request_options: typing.Optional[RequestOptions] = None
    ) -> PlaceMarkerResponse:
        """
        A union-typed property's declared example.

        Parameters
        ----------
        marker : PlaceMarkerRequestMarker

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlaceMarkerResponse
            Placed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BuoyMarker

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.markers.place_marker(
                marker=BuoyMarker(
                    colour="colour",
                    shape="shape",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.place_marker(marker=marker, request_options=request_options)
        return _response.data
