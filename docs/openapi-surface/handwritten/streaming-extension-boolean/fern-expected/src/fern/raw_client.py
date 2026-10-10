

import contextlib
import json
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.log_line import LogLine
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def tail_logs(
        self, *, service: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[LogLine]]]:
        """
        Parameters
        ----------
        service : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[LogLine]]]
            Log lines.
        """
        with self._client_wrapper.httpx_client.stream(
            "logs/tail",
            method="GET",
            params={
                "service": service,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[LogLine]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            for _text in _response.iter_lines():
                                try:
                                    if len(_text) == 0:
                                        continue
                                    yield typing.cast(
                                        LogLine,
                                        parse_obj_as(
                                            type_=LogLine,
                                            object_=json.loads(_text),
                                        ),
                                    )
                                except Exception:
                                    pass
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
    async def tail_logs(
        self, *, service: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[LogLine]]]:
        """
        Parameters
        ----------
        service : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[LogLine]]]
            Log lines.
        """
        async with self._client_wrapper.httpx_client.stream(
            "logs/tail",
            method="GET",
            params={
                "service": service,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[LogLine]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            async for _text in _response.aiter_lines():
                                try:
                                    if len(_text) == 0:
                                        continue
                                    yield typing.cast(
                                        LogLine,
                                        parse_obj_as(
                                            type_=LogLine,
                                            object_=json.loads(_text),
                                        ),
                                    )
                                except Exception:
                                    pass
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
