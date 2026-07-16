

import contextlib
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
from ..types.date import Date
from ..types.email import Email
from ..types.error import Error
from ..types.event_id import EventId
from ..types.museum_tickets_confirmation import MuseumTicketsConfirmation
from ..types.ticket_id import TicketId
from ..types.ticket_type import TicketType


OMIT = typing.cast(typing.Any, ...)


class RawTicketsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def buy_museum_tickets(
        self,
        *,
        ticket_date: Date,
        ticket_type: TicketType,
        email: typing.Optional[Email] = OMIT,
        ticket_id: typing.Optional[TicketId] = OMIT,
        event_id: typing.Optional[EventId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MuseumTicketsConfirmation]:
        """
        Purchase museum tickets for general entry or special events.

        Parameters
        ----------
        ticket_date : Date
            Date when this ticket can be used for museum entry.

        ticket_type : TicketType

        email : typing.Optional[Email]

        ticket_id : typing.Optional[TicketId]

        event_id : typing.Optional[EventId]
            Unique identifier for a special event. Required if purchasing tickets for the museum's special events.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MuseumTicketsConfirmation]
            Created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "tickets",
            method="POST",
            json={
                "email": email,
                "ticketId": ticket_id,
                "ticketDate": ticket_date,
                "ticketType": ticket_type,
                "eventId": event_id,
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
                    MuseumTicketsConfirmation,
                    parse_obj_as(
                        type_=MuseumTicketsConfirmation,
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

    @contextlib.contextmanager
    def get_ticket_code(
        self, ticket_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Return an image of your ticket with scannable QR code. Used for event entry.

        Parameters
        ----------
        ticket_id : str
            Identifier for a ticket to a museum event. Used to generate ticket image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Scannable event ticket in image format.
        """
        with self._client_wrapper.httpx_client.stream(
            f"tickets/{jsonable_encoder(ticket_id)}/qr",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawTicketsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def buy_museum_tickets(
        self,
        *,
        ticket_date: Date,
        ticket_type: TicketType,
        email: typing.Optional[Email] = OMIT,
        ticket_id: typing.Optional[TicketId] = OMIT,
        event_id: typing.Optional[EventId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MuseumTicketsConfirmation]:
        """
        Purchase museum tickets for general entry or special events.

        Parameters
        ----------
        ticket_date : Date
            Date when this ticket can be used for museum entry.

        ticket_type : TicketType

        email : typing.Optional[Email]

        ticket_id : typing.Optional[TicketId]

        event_id : typing.Optional[EventId]
            Unique identifier for a special event. Required if purchasing tickets for the museum's special events.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MuseumTicketsConfirmation]
            Created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tickets",
            method="POST",
            json={
                "email": email,
                "ticketId": ticket_id,
                "ticketDate": ticket_date,
                "ticketType": ticket_type,
                "eventId": event_id,
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
                    MuseumTicketsConfirmation,
                    parse_obj_as(
                        type_=MuseumTicketsConfirmation,
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

    @contextlib.asynccontextmanager
    async def get_ticket_code(
        self, ticket_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Return an image of your ticket with scannable QR code. Used for event entry.

        Parameters
        ----------
        ticket_id : str
            Identifier for a ticket to a museum event. Used to generate ticket image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Scannable event ticket in image format.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"tickets/{jsonable_encoder(ticket_id)}/qr",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
