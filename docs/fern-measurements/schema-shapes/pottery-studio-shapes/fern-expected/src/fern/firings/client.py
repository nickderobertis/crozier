

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.firing_booking import FiringBooking
from ..types.firing_booking_ending import FiringBookingEnding
from ..types.firing_booking_shelf import FiringBookingShelf
from ..types.target_cone import TargetCone
from .raw_client import AsyncRawFiringsClient, RawFiringsClient


OMIT = typing.cast(typing.Any, ...)


class FiringsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFiringsClient
        """
        return self._raw_client

    def book_firing(
        self,
        *,
        potter: str,
        cone: TargetCone,
        shelf: FiringBookingShelf,
        ending: FiringBookingEnding,
        palette: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FiringBooking:
        """
            Books a slot on the shared kiln.
            The slot is held for one hour before it lapses.

        Parameters
        ----------
        potter : str

        cone : TargetCone

        shelf : FiringBookingShelf

        ending : FiringBookingEnding

        palette : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FiringBooking
            The booked firing.

        Examples
        --------
        from fern import (
            FernApi,
            FiringBookingEnding_Cooled,
            FiringBookingShelf,
            FiringBookingShelfLevel,
        )

        client = FernApi()
        client.firings.book_firing(
            potter="potter",
            cone=1,
            shelf=FiringBookingShelf(
                level=FiringBookingShelfLevel.UPPER,
                slot=1,
            ),
            ending=FiringBookingEnding_Cooled(
                hours=1,
            ),
            palette=["palette"],
        )
        """
        _response = self._raw_client.book_firing(
            potter=potter, cone=cone, shelf=shelf, ending=ending, palette=palette, request_options=request_options
        )
        return _response.data


class AsyncFiringsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFiringsClient
        """
        return self._raw_client

    async def book_firing(
        self,
        *,
        potter: str,
        cone: TargetCone,
        shelf: FiringBookingShelf,
        ending: FiringBookingEnding,
        palette: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FiringBooking:
        """
            Books a slot on the shared kiln.
            The slot is held for one hour before it lapses.

        Parameters
        ----------
        potter : str

        cone : TargetCone

        shelf : FiringBookingShelf

        ending : FiringBookingEnding

        palette : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FiringBooking
            The booked firing.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            FiringBookingEnding_Cooled,
            FiringBookingShelf,
            FiringBookingShelfLevel,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.book_firing(
                potter="potter",
                cone=1,
                shelf=FiringBookingShelf(
                    level=FiringBookingShelfLevel.UPPER,
                    slot=1,
                ),
                ending=FiringBookingEnding_Cooled(
                    hours=1,
                ),
                palette=["palette"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.book_firing(
            potter=potter, cone=cone, shelf=shelf, ending=ending, palette=palette, request_options=request_options
        )
        return _response.data
