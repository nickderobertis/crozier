

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.http_sse._api import EventSource
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as, parse_sse_obj
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.apis_v1components_error_response import ApisV1ComponentsErrorResponse
from ..types.watch_event import WatchEvent
from ..types.watch_event_filters import WatchEventFilters
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def watch_events(
        self,
        *,
        filters: typing.Optional[WatchEventFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[WatchEvent]]]:
        """
        Parameters
        ----------
        filters : typing.Optional[WatchEventFilters]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[WatchEvent]]]
            Server-Sent Events stream. Each data field contains one serialized
            CloudEvents 1.0 event. Comment fields are connection heartbeats.
        """
        with self._client_wrapper.httpx_client.stream(
            "v1/events/watch",
            method="POST",
            json={
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=WatchEventFilters, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[WatchEvent]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        WatchEvent,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=WatchEvent,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 415:
                        raise UnsupportedMediaTypeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
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


class AsyncRawEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def watch_events(
        self,
        *,
        filters: typing.Optional[WatchEventFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[WatchEvent]]]:
        """
        Parameters
        ----------
        filters : typing.Optional[WatchEventFilters]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[WatchEvent]]]
            Server-Sent Events stream. Each data field contains one serialized
            CloudEvents 1.0 event. Comment fields are connection heartbeats.
        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/events/watch",
            method="POST",
            json={
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=WatchEventFilters, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[WatchEvent]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        WatchEvent,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=WatchEvent,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 415:
                        raise UnsupportedMediaTypeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApisV1ComponentsErrorResponse,
                                parse_obj_as(
                                    type_=ApisV1ComponentsErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
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
