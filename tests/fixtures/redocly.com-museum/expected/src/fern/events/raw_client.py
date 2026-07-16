

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.event_dates import EventDates
from ..types.event_description import EventDescription
from ..types.event_id import EventId
from ..types.event_location import EventLocation
from ..types.event_name import EventName
from ..types.event_price import EventPrice
from ..types.special_event import SpecialEvent
from ..types.special_event_collection import SpecialEventCollection


OMIT = typing.cast(typing.Any, ...)


class RawEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_special_events(
        self,
        *,
        start_date: typing.Optional[dt.date] = None,
        end_date: typing.Optional[dt.date] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SpecialEventCollection]:
        """
        Return a list of upcoming special events at the museum.

        Parameters
        ----------
        start_date : typing.Optional[dt.date]
            Starting date to retrieve future operating hours from. Defaults to today's date.

        end_date : typing.Optional[dt.date]
            End of a date range to retrieve special events for. Defaults to 7 days after `startDate`.

        page : typing.Optional[int]
            Page number to retrieve.

        limit : typing.Optional[int]
            Number of days per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SpecialEventCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "special-events",
            method="GET",
            params={
                "startDate": str(start_date) if start_date is not None else None,
                "endDate": str(end_date) if end_date is not None else None,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpecialEventCollection,
                    parse_obj_as(
                        type_=SpecialEventCollection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_special_event(
        self,
        *,
        name: EventName,
        location: EventLocation,
        event_description: EventDescription,
        dates: EventDates,
        price: EventPrice,
        event_id: typing.Optional[EventId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SpecialEvent]:
        """
        Creates a new special event for the museum.

        Parameters
        ----------
        name : EventName

        location : EventLocation

        event_description : EventDescription

        dates : EventDates

        price : EventPrice

        event_id : typing.Optional[EventId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SpecialEvent]
            Created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "special-events",
            method="POST",
            json={
                "eventId": event_id,
                "name": name,
                "location": location,
                "eventDescription": event_description,
                "dates": dates,
                "price": price,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpecialEvent,
                    parse_obj_as(
                        type_=SpecialEvent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_special_event(
        self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SpecialEvent]:
        """
        Get details about a special event.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SpecialEvent]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"special-events/{jsonable_encoder(event_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpecialEvent,
                    parse_obj_as(
                        type_=SpecialEvent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_special_event(
        self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a special event from the collection. Allows museum to cancel planned events.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"special-events/{jsonable_encoder(event_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_special_event(
        self,
        event_id: str,
        *,
        name: typing.Optional[EventName] = OMIT,
        location: typing.Optional[EventLocation] = OMIT,
        event_description: typing.Optional[EventDescription] = OMIT,
        dates: typing.Optional[EventDates] = OMIT,
        price: typing.Optional[EventPrice] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SpecialEvent]:
        """
        Update the details of a special event.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        name : typing.Optional[EventName]

        location : typing.Optional[EventLocation]

        event_description : typing.Optional[EventDescription]

        dates : typing.Optional[EventDates]

        price : typing.Optional[EventPrice]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SpecialEvent]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"special-events/{jsonable_encoder(event_id)}",
            method="PATCH",
            json={
                "name": name,
                "location": location,
                "eventDescription": event_description,
                "dates": dates,
                "price": price,
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
                    SpecialEvent,
                    parse_obj_as(
                        type_=SpecialEvent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_special_events(
        self,
        *,
        start_date: typing.Optional[dt.date] = None,
        end_date: typing.Optional[dt.date] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SpecialEventCollection]:
        """
        Return a list of upcoming special events at the museum.

        Parameters
        ----------
        start_date : typing.Optional[dt.date]
            Starting date to retrieve future operating hours from. Defaults to today's date.

        end_date : typing.Optional[dt.date]
            End of a date range to retrieve special events for. Defaults to 7 days after `startDate`.

        page : typing.Optional[int]
            Page number to retrieve.

        limit : typing.Optional[int]
            Number of days per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SpecialEventCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "special-events",
            method="GET",
            params={
                "startDate": str(start_date) if start_date is not None else None,
                "endDate": str(end_date) if end_date is not None else None,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpecialEventCollection,
                    parse_obj_as(
                        type_=SpecialEventCollection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_special_event(
        self,
        *,
        name: EventName,
        location: EventLocation,
        event_description: EventDescription,
        dates: EventDates,
        price: EventPrice,
        event_id: typing.Optional[EventId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SpecialEvent]:
        """
        Creates a new special event for the museum.

        Parameters
        ----------
        name : EventName

        location : EventLocation

        event_description : EventDescription

        dates : EventDates

        price : EventPrice

        event_id : typing.Optional[EventId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SpecialEvent]
            Created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "special-events",
            method="POST",
            json={
                "eventId": event_id,
                "name": name,
                "location": location,
                "eventDescription": event_description,
                "dates": dates,
                "price": price,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpecialEvent,
                    parse_obj_as(
                        type_=SpecialEvent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_special_event(
        self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SpecialEvent]:
        """
        Get details about a special event.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SpecialEvent]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"special-events/{jsonable_encoder(event_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpecialEvent,
                    parse_obj_as(
                        type_=SpecialEvent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_special_event(
        self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a special event from the collection. Allows museum to cancel planned events.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"special-events/{jsonable_encoder(event_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_special_event(
        self,
        event_id: str,
        *,
        name: typing.Optional[EventName] = OMIT,
        location: typing.Optional[EventLocation] = OMIT,
        event_description: typing.Optional[EventDescription] = OMIT,
        dates: typing.Optional[EventDates] = OMIT,
        price: typing.Optional[EventPrice] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SpecialEvent]:
        """
        Update the details of a special event.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        name : typing.Optional[EventName]

        location : typing.Optional[EventLocation]

        event_description : typing.Optional[EventDescription]

        dates : typing.Optional[EventDates]

        price : typing.Optional[EventPrice]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SpecialEvent]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"special-events/{jsonable_encoder(event_id)}",
            method="PATCH",
            json={
                "name": name,
                "location": location,
                "eventDescription": event_description,
                "dates": dates,
                "price": price,
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
                    SpecialEvent,
                    parse_obj_as(
                        type_=SpecialEvent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
