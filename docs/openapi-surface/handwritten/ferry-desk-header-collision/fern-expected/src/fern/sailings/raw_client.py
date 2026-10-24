

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.booking import Booking
from ..types.sailing import Sailing
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSailingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_sailings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Sailing]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Sailing]]
            The sailings.
        """
        _response = self._client_wrapper.httpx_client.request(
            "sailings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Sailing],
                    parse_obj_as(
                        type_=typing.List[Sailing],
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

    def book_vehicle(
        self,
        sailing_id: str,
        *,
        registration: str,
        deck: typing.Optional[str] = None,
        book_vehicle_request_deck: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Booking]:
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
        HttpResponse[Booking]
            The booking.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sailings/{encode_path_param(sailing_id)}/bookings",
            method="POST",
            json={
                "registration": registration,
                "deck": book_vehicle_request_deck,
            },
            headers={
                "content-type": "application/json",
                "deck": str(deck) if deck is not None else None,
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


class AsyncRawSailingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_sailings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Sailing]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Sailing]]
            The sailings.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sailings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Sailing],
                    parse_obj_as(
                        type_=typing.List[Sailing],
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

    async def book_vehicle(
        self,
        sailing_id: str,
        *,
        registration: str,
        deck: typing.Optional[str] = None,
        book_vehicle_request_deck: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Booking]:
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
        AsyncHttpResponse[Booking]
            The booking.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sailings/{encode_path_param(sailing_id)}/bookings",
            method="POST",
            json={
                "registration": registration,
                "deck": book_vehicle_request_deck,
            },
            headers={
                "content-type": "application/json",
                "deck": str(deck) if deck is not None else None,
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
