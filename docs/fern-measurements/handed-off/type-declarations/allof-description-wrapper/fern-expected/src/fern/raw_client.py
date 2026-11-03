

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.booking import Booking
from .types.booking_backup import BookingBackup
from .types.booking_booked_by import BookingBookedBy
from .types.telescope import Telescope
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_telescope(
        self, name: str, *, night: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Telescope]:
        """
        Parameters
        ----------
        name : str
            Telescope dome name.

        night : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Telescope]
            The telescope
        """
        _response = self._client_wrapper.httpx_client.request(
            f"telescopes/{encode_path_param(name)}",
            method="GET",
            params={
                "night": night,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Telescope,
                    parse_obj_as(
                        type_=Telescope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retire_telescope(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"telescopes/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_booking(
        self,
        *,
        dome: str,
        booked_by: typing.Optional[BookingBookedBy] = OMIT,
        backup: typing.Optional[BookingBackup] = OMIT,
        slot: typing.Optional[str] = OMIT,
        nights: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Booking]:
        """
        Parameters
        ----------
        dome : str
            Dome booked.

        booked_by : typing.Optional[BookingBookedBy]
            Who booked the time.

        backup : typing.Optional[BookingBackup]

        slot : typing.Optional[str]
            Identifier of an observing slot.

        nights : typing.Optional[int]
            Nights requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Booking]
            The booking
        """
        _response = self._client_wrapper.httpx_client.request(
            "bookings",
            method="POST",
            json={
                "dome": dome,
                "bookedBy": convert_and_respect_annotation_metadata(
                    object_=booked_by, annotation=BookingBookedBy, direction="write"
                ),
                "backup": convert_and_respect_annotation_metadata(
                    object_=backup, annotation=typing.Optional[BookingBackup], direction="write"
                ),
                "slot": slot,
                "nights": nights,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Booking,
                    parse_obj_as(
                        type_=Booking,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_telescope(
        self, name: str, *, night: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Telescope]:
        """
        Parameters
        ----------
        name : str
            Telescope dome name.

        night : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Telescope]
            The telescope
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"telescopes/{encode_path_param(name)}",
            method="GET",
            params={
                "night": night,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Telescope,
                    parse_obj_as(
                        type_=Telescope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retire_telescope(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"telescopes/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_booking(
        self,
        *,
        dome: str,
        booked_by: typing.Optional[BookingBookedBy] = OMIT,
        backup: typing.Optional[BookingBackup] = OMIT,
        slot: typing.Optional[str] = OMIT,
        nights: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Booking]:
        """
        Parameters
        ----------
        dome : str
            Dome booked.

        booked_by : typing.Optional[BookingBookedBy]
            Who booked the time.

        backup : typing.Optional[BookingBackup]

        slot : typing.Optional[str]
            Identifier of an observing slot.

        nights : typing.Optional[int]
            Nights requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Booking]
            The booking
        """
        _response = await self._client_wrapper.httpx_client.request(
            "bookings",
            method="POST",
            json={
                "dome": dome,
                "bookedBy": convert_and_respect_annotation_metadata(
                    object_=booked_by, annotation=BookingBookedBy, direction="write"
                ),
                "backup": convert_and_respect_annotation_metadata(
                    object_=backup, annotation=typing.Optional[BookingBackup], direction="write"
                ),
                "slot": slot,
                "nights": nights,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Booking,
                    parse_obj_as(
                        type_=Booking,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
