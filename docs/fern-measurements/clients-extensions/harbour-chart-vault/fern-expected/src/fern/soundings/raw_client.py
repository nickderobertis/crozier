

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawSoundingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def export_soundings(
        self, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Exports one survey's raw soundings.
        
        Survey logs are archived under G:\\
        
        Parameters
        ----------
        survey_id : str
            The survey whose soundings to export.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
        
        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The raw soundings.
        """
        with self._client_wrapper.httpx_client.stream(
            f"soundings/{encode_path_param(survey_id)}/export",
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


class AsyncRawSoundingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def export_soundings(
        self, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Exports one survey's raw soundings.
        
        Survey logs are archived under G:\\
        
        Parameters
        ----------
        survey_id : str
            The survey whose soundings to export.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
        
        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The raw soundings.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"soundings/{encode_path_param(survey_id)}/export",
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
