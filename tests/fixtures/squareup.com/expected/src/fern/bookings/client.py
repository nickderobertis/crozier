

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.booking import Booking
from ..types.cancel_booking_response import CancelBookingResponse
from ..types.create_booking_response import CreateBookingResponse
from ..types.list_team_member_booking_profiles_response import ListTeamMemberBookingProfilesResponse
from ..types.retrieve_booking_response import RetrieveBookingResponse
from ..types.retrieve_business_booking_profile_response import RetrieveBusinessBookingProfileResponse
from ..types.retrieve_team_member_booking_profile_response import RetrieveTeamMemberBookingProfileResponse
from ..types.search_availability_query import SearchAvailabilityQuery
from ..types.search_availability_response import SearchAvailabilityResponse
from ..types.update_booking_response import UpdateBookingResponse
from .raw_client import AsyncRawBookingsClient, RawBookingsClient


OMIT = typing.cast(typing.Any, ...)


class BookingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBookingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBookingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBookingsClient
        """
        return self._raw_client

    def create_booking(
        self,
        *,
        booking: Booking,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateBookingResponse:
        """
        Creates a booking.

        Parameters
        ----------
        booking : Booking

        idempotency_key : typing.Optional[str]
            A unique key to make this request an idempotent operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBookingResponse
            Success

        Examples
        --------
        from fern import AppointmentSegment, Booking, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bookings.create_booking(
            booking=Booking(
                appointment_segments=[
                    AppointmentSegment(
                        duration_minutes=60,
                        service_variation_id="RU3PBTZTK7DXZDQFCJHOK2MC",
                        service_variation_version=1599775456731,
                        team_member_id="TMXUrsBWWcHTt79t",
                    )
                ],
                customer_id="EX2QSVGTZN4K1E5QE1CBFNVQ8M",
                location_id="LEQHH0YY8B42M",
                start_at="2020-11-26T13:00:00Z",
            ),
        )
        """
        _response = self._raw_client.create_booking(
            booking=booking, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def search_availability(
        self, *, query: SearchAvailabilityQuery, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchAvailabilityResponse:
        """
        Searches for availabilities for booking.

        Parameters
        ----------
        query : SearchAvailabilityQuery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchAvailabilityResponse
            Success

        Examples
        --------
        from fern import (
            FernApi,
            FilterValue,
            SearchAvailabilityFilter,
            SearchAvailabilityQuery,
            SegmentFilter,
            TimeRange,
        )

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bookings.search_availability(
            query=SearchAvailabilityQuery(
                filter=SearchAvailabilityFilter(
                    location_id="LEQHH0YY8B42M",
                    segment_filters=[
                        SegmentFilter(
                            service_variation_id="RU3PBTZTK7DXZDQFCJHOK2MC",
                            team_member_id_filter=FilterValue(
                                any=["TMXUrsBWWcHTt79t", "TMaJcbiRqPIGZuS9"],
                            ),
                        )
                    ],
                    start_at_range=TimeRange(
                        end_at="2020-11-27T13:00:00Z",
                        start_at="2020-11-26T13:00:00Z",
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.search_availability(query=query, request_options=request_options)
        return _response.data

    def retrieve_business_booking_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveBusinessBookingProfileResponse:
        """
        Retrieves a seller's booking profile.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveBusinessBookingProfileResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bookings.retrieve_business_booking_profile()
        """
        _response = self._raw_client.retrieve_business_booking_profile(request_options=request_options)
        return _response.data

    def list_team_member_booking_profiles(
        self,
        *,
        bookable_only: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTeamMemberBookingProfilesResponse:
        """
        Lists booking profiles for team members.

        Parameters
        ----------
        bookable_only : typing.Optional[bool]
            Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`).

        limit : typing.Optional[int]
            The maximum number of results to return.

        cursor : typing.Optional[str]
            The cursor for paginating through the results.

        location_id : typing.Optional[str]
            Indicates whether to include only team members enabled at the given location in the returned result.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTeamMemberBookingProfilesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bookings.list_team_member_booking_profiles()
        """
        _response = self._raw_client.list_team_member_booking_profiles(
            bookable_only=bookable_only,
            limit=limit,
            cursor=cursor,
            location_id=location_id,
            request_options=request_options,
        )
        return _response.data

    def retrieve_team_member_booking_profile(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveTeamMemberBookingProfileResponse:
        """
        Retrieves a team member's booking profile.

        Parameters
        ----------
        team_member_id : str
            The ID of the team member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveTeamMemberBookingProfileResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bookings.retrieve_team_member_booking_profile(
            team_member_id="team_member_id",
        )
        """
        _response = self._raw_client.retrieve_team_member_booking_profile(
            team_member_id, request_options=request_options
        )
        return _response.data

    def retrieve_booking(
        self, booking_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveBookingResponse:
        """
        Retrieves a booking.

        Parameters
        ----------
        booking_id : str
            The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-retrieved booking.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveBookingResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bookings.retrieve_booking(
            booking_id="booking_id",
        )
        """
        _response = self._raw_client.retrieve_booking(booking_id, request_options=request_options)
        return _response.data

    def update_booking(
        self,
        booking_id: str,
        *,
        booking: Booking,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateBookingResponse:
        """
        Updates a booking.

        Parameters
        ----------
        booking_id : str
            The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-updated booking.

        booking : Booking

        idempotency_key : typing.Optional[str]
            A unique key to make this request an idempotent operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateBookingResponse
            Success

        Examples
        --------
        from fern import Booking, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bookings.update_booking(
            booking_id="booking_id",
            booking=Booking(
                customer_note="I would like to sit near the window please",
                version=1,
            ),
        )
        """
        _response = self._raw_client.update_booking(
            booking_id, booking=booking, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def cancel_booking(
        self,
        booking_id: str,
        *,
        booking_version: typing.Optional[int] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CancelBookingResponse:
        """
        Cancels an existing booking.

        Parameters
        ----------
        booking_id : str
            The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-cancelled booking.

        booking_version : typing.Optional[int]
            The revision number for the booking used for optimistic concurrency.

        idempotency_key : typing.Optional[str]
            A unique key to make this request an idempotent operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelBookingResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.bookings.cancel_booking(
            booking_id="booking_id",
            booking_version=1,
        )
        """
        _response = self._raw_client.cancel_booking(
            booking_id,
            booking_version=booking_version,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return _response.data


class AsyncBookingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBookingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBookingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBookingsClient
        """
        return self._raw_client

    async def create_booking(
        self,
        *,
        booking: Booking,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateBookingResponse:
        """
        Creates a booking.

        Parameters
        ----------
        booking : Booking

        idempotency_key : typing.Optional[str]
            A unique key to make this request an idempotent operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBookingResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AppointmentSegment, AsyncFernApi, Booking

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bookings.create_booking(
                booking=Booking(
                    appointment_segments=[
                        AppointmentSegment(
                            duration_minutes=60,
                            service_variation_id="RU3PBTZTK7DXZDQFCJHOK2MC",
                            service_variation_version=1599775456731,
                            team_member_id="TMXUrsBWWcHTt79t",
                        )
                    ],
                    customer_id="EX2QSVGTZN4K1E5QE1CBFNVQ8M",
                    location_id="LEQHH0YY8B42M",
                    start_at="2020-11-26T13:00:00Z",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_booking(
            booking=booking, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def search_availability(
        self, *, query: SearchAvailabilityQuery, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchAvailabilityResponse:
        """
        Searches for availabilities for booking.

        Parameters
        ----------
        query : SearchAvailabilityQuery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchAvailabilityResponse
            Success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            FilterValue,
            SearchAvailabilityFilter,
            SearchAvailabilityQuery,
            SegmentFilter,
            TimeRange,
        )

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bookings.search_availability(
                query=SearchAvailabilityQuery(
                    filter=SearchAvailabilityFilter(
                        location_id="LEQHH0YY8B42M",
                        segment_filters=[
                            SegmentFilter(
                                service_variation_id="RU3PBTZTK7DXZDQFCJHOK2MC",
                                team_member_id_filter=FilterValue(
                                    any=["TMXUrsBWWcHTt79t", "TMaJcbiRqPIGZuS9"],
                                ),
                            )
                        ],
                        start_at_range=TimeRange(
                            end_at="2020-11-27T13:00:00Z",
                            start_at="2020-11-26T13:00:00Z",
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_availability(query=query, request_options=request_options)
        return _response.data

    async def retrieve_business_booking_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveBusinessBookingProfileResponse:
        """
        Retrieves a seller's booking profile.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveBusinessBookingProfileResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bookings.retrieve_business_booking_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_business_booking_profile(request_options=request_options)
        return _response.data

    async def list_team_member_booking_profiles(
        self,
        *,
        bookable_only: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTeamMemberBookingProfilesResponse:
        """
        Lists booking profiles for team members.

        Parameters
        ----------
        bookable_only : typing.Optional[bool]
            Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`).

        limit : typing.Optional[int]
            The maximum number of results to return.

        cursor : typing.Optional[str]
            The cursor for paginating through the results.

        location_id : typing.Optional[str]
            Indicates whether to include only team members enabled at the given location in the returned result.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTeamMemberBookingProfilesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bookings.list_team_member_booking_profiles()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_team_member_booking_profiles(
            bookable_only=bookable_only,
            limit=limit,
            cursor=cursor,
            location_id=location_id,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_team_member_booking_profile(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveTeamMemberBookingProfileResponse:
        """
        Retrieves a team member's booking profile.

        Parameters
        ----------
        team_member_id : str
            The ID of the team member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveTeamMemberBookingProfileResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bookings.retrieve_team_member_booking_profile(
                team_member_id="team_member_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_team_member_booking_profile(
            team_member_id, request_options=request_options
        )
        return _response.data

    async def retrieve_booking(
        self, booking_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveBookingResponse:
        """
        Retrieves a booking.

        Parameters
        ----------
        booking_id : str
            The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-retrieved booking.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveBookingResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bookings.retrieve_booking(
                booking_id="booking_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_booking(booking_id, request_options=request_options)
        return _response.data

    async def update_booking(
        self,
        booking_id: str,
        *,
        booking: Booking,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateBookingResponse:
        """
        Updates a booking.

        Parameters
        ----------
        booking_id : str
            The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-updated booking.

        booking : Booking

        idempotency_key : typing.Optional[str]
            A unique key to make this request an idempotent operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateBookingResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Booking

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bookings.update_booking(
                booking_id="booking_id",
                booking=Booking(
                    customer_note="I would like to sit near the window please",
                    version=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_booking(
            booking_id, booking=booking, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def cancel_booking(
        self,
        booking_id: str,
        *,
        booking_version: typing.Optional[int] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CancelBookingResponse:
        """
        Cancels an existing booking.

        Parameters
        ----------
        booking_id : str
            The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-cancelled booking.

        booking_version : typing.Optional[int]
            The revision number for the booking used for optimistic concurrency.

        idempotency_key : typing.Optional[str]
            A unique key to make this request an idempotent operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelBookingResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bookings.cancel_booking(
                booking_id="booking_id",
                booking_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_booking(
            booking_id,
            booking_version=booking_version,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return _response.data
