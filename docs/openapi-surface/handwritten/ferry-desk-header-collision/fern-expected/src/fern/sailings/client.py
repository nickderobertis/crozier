

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.booking import Booking
from ..types.sailing import Sailing
from .raw_client import AsyncRawSailingsClient, RawSailingsClient


OMIT = typing.cast(typing.Any, ...)


class SailingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSailingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSailingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSailingsClient
        """
        return self._raw_client

    def list_sailings(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Sailing]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Sailing]
            The sailings.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sailings.list_sailings()
        """
        _response = self._raw_client.list_sailings(request_options=request_options)
        return _response.data

    def book_vehicle(
        self,
        sailing_id: str,
        *,
        registration: str,
        deck: typing.Optional[str] = None,
        book_vehicle_request_deck: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Booking:
        """
        Parameters
        ----------
        sailing_id : str

        registration : str
            The vehicle's number plate.

        deck : typing.Optional[str]
            The deck the desk prefers to fill first.

        book_vehicle_request_deck : typing.Optional[str]
            The deck the driver asked for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Booking
            The booking.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sailings.book_vehicle(
            sailing_id="sailingId",
            registration="registration",
        )
        """
        _response = self._raw_client.book_vehicle(
            sailing_id,
            registration=registration,
            deck=deck,
            book_vehicle_request_deck=book_vehicle_request_deck,
            request_options=request_options,
        )
        return _response.data


class AsyncSailingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSailingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSailingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSailingsClient
        """
        return self._raw_client

    async def list_sailings(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Sailing]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Sailing]
            The sailings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sailings.list_sailings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sailings(request_options=request_options)
        return _response.data

    async def book_vehicle(
        self,
        sailing_id: str,
        *,
        registration: str,
        deck: typing.Optional[str] = None,
        book_vehicle_request_deck: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Booking:
        """
        Parameters
        ----------
        sailing_id : str

        registration : str
            The vehicle's number plate.

        deck : typing.Optional[str]
            The deck the desk prefers to fill first.

        book_vehicle_request_deck : typing.Optional[str]
            The deck the driver asked for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Booking
            The booking.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sailings.book_vehicle(
                sailing_id="sailingId",
                registration="registration",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.book_vehicle(
            sailing_id,
            registration=registration,
            deck=deck,
            book_vehicle_request_deck=book_vehicle_request_deck,
            request_options=request_options,
        )
        return _response.data
