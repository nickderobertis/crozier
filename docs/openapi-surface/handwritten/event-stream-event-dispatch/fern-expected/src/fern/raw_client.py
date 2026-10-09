

import contextlib
import json
import typing
from json.decoder import JSONDecodeError
from logging import warning

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.http_sse._api import EventSource
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.arrival import Arrival
from .types.departure import Departure
from .types.gangway_change import GangwayChange
from .types.lowered import Lowered
from .types.movement import Movement
from .types.raised import Raised
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def watch_movements(
        self, route_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[Movement]]]:
        """
        Parameters
        ----------
        route_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[Movement]]]
            Departures and arrivals on the route.
        """
        with self._client_wrapper.httpx_client.stream(
            f"routes/{encode_path_param(route_id)}/movements",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[Movement]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                if _sse.event == "departed":
                                    try:
                                        yield typing.cast(
                                            Departure,
                                            parse_obj_as(
                                                type_=Departure,
                                                object_=json.loads(_sse.data),
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'departed': {e}, sse: {_sse!r}")
                                elif _sse.event == "arrived":
                                    try:
                                        yield typing.cast(
                                            Arrival,
                                            parse_obj_as(
                                                type_=Arrival,
                                                object_=json.loads(_sse.data),
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'arrived': {e}, sse: {_sse!r}")
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    @contextlib.contextmanager
    def watch_gangway(
        self, terminal_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[GangwayChange]]]:
        """
        Parameters
        ----------
        terminal_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[GangwayChange]]]
            The gangway lowering and rising at the terminal.
        """
        with self._client_wrapper.httpx_client.stream(
            f"terminals/{encode_path_param(terminal_id)}/gangway",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[GangwayChange]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                if _sse.event == "lowered":
                                    try:
                                        yield typing.cast(
                                            Lowered,
                                            parse_obj_as(
                                                type_=Lowered,
                                                object_=json.loads(_sse.data),
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'lowered': {e}, sse: {_sse!r}")
                                elif _sse.event == "raised":
                                    try:
                                        yield typing.cast(
                                            Raised,
                                            parse_obj_as(
                                                type_=Raised,
                                                object_=json.loads(_sse.data),
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'raised': {e}, sse: {_sse!r}")
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def watch_movements(
        self, route_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[Movement]]]:
        """
        Parameters
        ----------
        route_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[Movement]]]
            Departures and arrivals on the route.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"routes/{encode_path_param(route_id)}/movements",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[Movement]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                if _sse.event == "departed":
                                    try:
                                        yield typing.cast(
                                            Departure,
                                            parse_obj_as(
                                                type_=Departure,
                                                object_=json.loads(_sse.data),
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'departed': {e}, sse: {_sse!r}")
                                elif _sse.event == "arrived":
                                    try:
                                        yield typing.cast(
                                            Arrival,
                                            parse_obj_as(
                                                type_=Arrival,
                                                object_=json.loads(_sse.data),
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'arrived': {e}, sse: {_sse!r}")
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    @contextlib.asynccontextmanager
    async def watch_gangway(
        self, terminal_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[GangwayChange]]]:
        """
        Parameters
        ----------
        terminal_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[GangwayChange]]]
            The gangway lowering and rising at the terminal.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"terminals/{encode_path_param(terminal_id)}/gangway",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[GangwayChange]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                if _sse.event == "lowered":
                                    try:
                                        yield typing.cast(
                                            Lowered,
                                            parse_obj_as(
                                                type_=Lowered,
                                                object_=json.loads(_sse.data),
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'lowered': {e}, sse: {_sse!r}")
                                elif _sse.event == "raised":
                                    try:
                                        yield typing.cast(
                                            Raised,
                                            parse_obj_as(
                                                type_=Raised,
                                                object_=json.loads(_sse.data),
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'raised': {e}, sse: {_sse!r}")
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
