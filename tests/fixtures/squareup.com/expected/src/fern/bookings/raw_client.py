

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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


OMIT = typing.cast(typing.Any, ...)


class RawBookingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_booking(
        self,
        *,
        booking: Booking,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateBookingResponse]:
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
        HttpResponse[CreateBookingResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bookings",
            method="POST",
            json={
                "booking": convert_and_respect_annotation_metadata(
                    object_=booking, annotation=Booking, direction="write"
                ),
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateBookingResponse,
                    parse_obj_as(
                        type_=CreateBookingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_availability(
        self, *, query: SearchAvailabilityQuery, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SearchAvailabilityResponse]:
        """
        Searches for availabilities for booking.

        Parameters
        ----------
        query : SearchAvailabilityQuery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchAvailabilityResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bookings/availability/search",
            method="POST",
            json={
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchAvailabilityQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchAvailabilityResponse,
                    parse_obj_as(
                        type_=SearchAvailabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_business_booking_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveBusinessBookingProfileResponse]:
        """
        Retrieves a seller's booking profile.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveBusinessBookingProfileResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bookings/business-booking-profile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveBusinessBookingProfileResponse,
                    parse_obj_as(
                        type_=RetrieveBusinessBookingProfileResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_team_member_booking_profiles(
        self,
        *,
        bookable_only: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTeamMemberBookingProfilesResponse]:
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
        HttpResponse[ListTeamMemberBookingProfilesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bookings/team-member-booking-profiles",
            method="GET",
            params={
                "bookable_only": bookable_only,
                "limit": limit,
                "cursor": cursor,
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTeamMemberBookingProfilesResponse,
                    parse_obj_as(
                        type_=ListTeamMemberBookingProfilesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_team_member_booking_profile(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveTeamMemberBookingProfileResponse]:
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
        HttpResponse[RetrieveTeamMemberBookingProfileResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bookings/team-member-booking-profiles/{jsonable_encoder(team_member_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveTeamMemberBookingProfileResponse,
                    parse_obj_as(
                        type_=RetrieveTeamMemberBookingProfileResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_booking(
        self, booking_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveBookingResponse]:
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
        HttpResponse[RetrieveBookingResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bookings/{jsonable_encoder(booking_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveBookingResponse,
                    parse_obj_as(
                        type_=RetrieveBookingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_booking(
        self,
        booking_id: str,
        *,
        booking: Booking,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateBookingResponse]:
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
        HttpResponse[UpdateBookingResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bookings/{jsonable_encoder(booking_id)}",
            method="PUT",
            json={
                "booking": convert_and_respect_annotation_metadata(
                    object_=booking, annotation=Booking, direction="write"
                ),
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateBookingResponse,
                    parse_obj_as(
                        type_=UpdateBookingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_booking(
        self,
        booking_id: str,
        *,
        booking_version: typing.Optional[int] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CancelBookingResponse]:
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
        HttpResponse[CancelBookingResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bookings/{jsonable_encoder(booking_id)}/cancel",
            method="POST",
            json={
                "booking_version": booking_version,
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelBookingResponse,
                    parse_obj_as(
                        type_=CancelBookingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawBookingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_booking(
        self,
        *,
        booking: Booking,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateBookingResponse]:
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
        AsyncHttpResponse[CreateBookingResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bookings",
            method="POST",
            json={
                "booking": convert_and_respect_annotation_metadata(
                    object_=booking, annotation=Booking, direction="write"
                ),
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateBookingResponse,
                    parse_obj_as(
                        type_=CreateBookingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_availability(
        self, *, query: SearchAvailabilityQuery, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SearchAvailabilityResponse]:
        """
        Searches for availabilities for booking.

        Parameters
        ----------
        query : SearchAvailabilityQuery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchAvailabilityResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bookings/availability/search",
            method="POST",
            json={
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchAvailabilityQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchAvailabilityResponse,
                    parse_obj_as(
                        type_=SearchAvailabilityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_business_booking_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveBusinessBookingProfileResponse]:
        """
        Retrieves a seller's booking profile.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveBusinessBookingProfileResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bookings/business-booking-profile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveBusinessBookingProfileResponse,
                    parse_obj_as(
                        type_=RetrieveBusinessBookingProfileResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_team_member_booking_profiles(
        self,
        *,
        bookable_only: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTeamMemberBookingProfilesResponse]:
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
        AsyncHttpResponse[ListTeamMemberBookingProfilesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bookings/team-member-booking-profiles",
            method="GET",
            params={
                "bookable_only": bookable_only,
                "limit": limit,
                "cursor": cursor,
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTeamMemberBookingProfilesResponse,
                    parse_obj_as(
                        type_=ListTeamMemberBookingProfilesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_team_member_booking_profile(
        self, team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveTeamMemberBookingProfileResponse]:
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
        AsyncHttpResponse[RetrieveTeamMemberBookingProfileResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bookings/team-member-booking-profiles/{jsonable_encoder(team_member_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveTeamMemberBookingProfileResponse,
                    parse_obj_as(
                        type_=RetrieveTeamMemberBookingProfileResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_booking(
        self, booking_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveBookingResponse]:
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
        AsyncHttpResponse[RetrieveBookingResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bookings/{jsonable_encoder(booking_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveBookingResponse,
                    parse_obj_as(
                        type_=RetrieveBookingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_booking(
        self,
        booking_id: str,
        *,
        booking: Booking,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateBookingResponse]:
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
        AsyncHttpResponse[UpdateBookingResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bookings/{jsonable_encoder(booking_id)}",
            method="PUT",
            json={
                "booking": convert_and_respect_annotation_metadata(
                    object_=booking, annotation=Booking, direction="write"
                ),
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateBookingResponse,
                    parse_obj_as(
                        type_=UpdateBookingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_booking(
        self,
        booking_id: str,
        *,
        booking_version: typing.Optional[int] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CancelBookingResponse]:
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
        AsyncHttpResponse[CancelBookingResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bookings/{jsonable_encoder(booking_id)}/cancel",
            method="POST",
            json={
                "booking_version": booking_version,
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelBookingResponse,
                    parse_obj_as(
                        type_=CancelBookingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
