

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
from .types.surge import Surge
from .types.surge_update import SurgeUpdate
from .types.tide_table import TideTable
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tides(
        self, *, port: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TideTable]]:
        """
        Lists the tide tables the harbour publishes.
        
        Archived tables are filed under C:\\
        
        Parameters
        ----------
        port : typing.Optional[str]
            The port whose tables to list.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[typing.List[TideTable]]
            The tide tables.
        """
        _response = self._client_wrapper.httpx_client.request(
            "tides",
            method="GET",
            params={
                "port": port,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TideTable],
                    parse_obj_as(
                        type_=typing.List[TideTable],
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

    @contextlib.contextmanager
    def forecast_surge_stream(
        self, *, port: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[SurgeUpdate]]]:
        """
        Forecasts a storm surge for one port.
        
        Raw readings are filed under D:\\
        
        Parameters
        ----------
        port : str
            The port to forecast for.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[SurgeUpdate]]]
            
        """
        with self._client_wrapper.httpx_client.stream(
            "surges",
            method="POST",
            json={
                "port": port,
                "stream": True,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[SurgeUpdate]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            for _text in _response.iter_lines():
                                try:
                                    if len(_text) == 0:
                                        continue
                                    yield typing.cast(
                                        SurgeUpdate,
                                        parse_obj_as(
                                            type_=SurgeUpdate,
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

    def forecast_surge(
        self, *, port: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Surge]:
        """
        Forecasts a storm surge for one port.
        
        Raw readings are filed under D:\\
        
        Parameters
        ----------
        port : str
            The port to forecast for.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[Surge]
            
        """
        _response = self._client_wrapper.httpx_client.request(
            "surges",
            method="POST",
            json={
                "port": port,
                "stream": False,
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
                    Surge,
                    parse_obj_as(
                        type_=Surge,
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

    async def list_tides(
        self, *, port: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TideTable]]:
        """
        Lists the tide tables the harbour publishes.
        
        Archived tables are filed under C:\\
        
        Parameters
        ----------
        port : typing.Optional[str]
            The port whose tables to list.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[typing.List[TideTable]]
            The tide tables.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tides",
            method="GET",
            params={
                "port": port,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TideTable],
                    parse_obj_as(
                        type_=typing.List[TideTable],
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

    @contextlib.asynccontextmanager
    async def forecast_surge_stream(
        self, *, port: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[SurgeUpdate]]]:
        """
        Forecasts a storm surge for one port.
        
        Raw readings are filed under D:\\
        
        Parameters
        ----------
        port : str
            The port to forecast for.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[SurgeUpdate]]]
            
        """
        async with self._client_wrapper.httpx_client.stream(
            "surges",
            method="POST",
            json={
                "port": port,
                "stream": True,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[SurgeUpdate]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            async for _text in _response.aiter_lines():
                                try:
                                    if len(_text) == 0:
                                        continue
                                    yield typing.cast(
                                        SurgeUpdate,
                                        parse_obj_as(
                                            type_=SurgeUpdate,
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

    async def forecast_surge(
        self, *, port: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Surge]:
        """
        Forecasts a storm surge for one port.
        
        Raw readings are filed under D:\\
        
        Parameters
        ----------
        port : str
            The port to forecast for.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[Surge]
            
        """
        _response = await self._client_wrapper.httpx_client.request(
            "surges",
            method="POST",
            json={
                "port": port,
                "stream": False,
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
                    Surge,
                    parse_obj_as(
                        type_=Surge,
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
