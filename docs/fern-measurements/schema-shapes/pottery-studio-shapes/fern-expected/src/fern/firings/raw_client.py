

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.firing_booking import FiringBooking
from ..types.firing_booking_ending import FiringBookingEnding
from ..types.firing_booking_shelf import FiringBookingShelf
from ..types.target_cone import TargetCone
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFiringsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def book_firing(
        self,
        *,
        potter: str,
        cone: TargetCone,
        shelf: FiringBookingShelf,
        ending: FiringBookingEnding,
        palette: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FiringBooking]:
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
        HttpResponse[FiringBooking]
            The booked firing.
        """
        _response = self._client_wrapper.httpx_client.request(
            "firings",
            method="POST",
            json={
                "potter": potter,
                "cone": cone,
                "shelf": convert_and_respect_annotation_metadata(
                    object_=shelf, annotation=FiringBookingShelf, direction="write"
                ),
                "ending": convert_and_respect_annotation_metadata(
                    object_=ending, annotation=FiringBookingEnding, direction="write"
                ),
                "palette": palette,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FiringBooking,
                    parse_obj_as(
                        type_=FiringBooking,
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


class AsyncRawFiringsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def book_firing(
        self,
        *,
        potter: str,
        cone: TargetCone,
        shelf: FiringBookingShelf,
        ending: FiringBookingEnding,
        palette: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FiringBooking]:
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
        AsyncHttpResponse[FiringBooking]
            The booked firing.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "firings",
            method="POST",
            json={
                "potter": potter,
                "cone": cone,
                "shelf": convert_and_respect_annotation_metadata(
                    object_=shelf, annotation=FiringBookingShelf, direction="write"
                ),
                "ending": convert_and_respect_annotation_metadata(
                    object_=ending, annotation=FiringBookingEnding, direction="write"
                ),
                "palette": palette,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FiringBooking,
                    parse_obj_as(
                        type_=FiringBooking,
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
