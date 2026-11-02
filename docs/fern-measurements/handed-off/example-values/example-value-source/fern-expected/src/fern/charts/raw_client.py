

import contextlib
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from .types.set_chart_layers_request_layers_item import SetChartLayersRequestLayersItem
from .types.set_chart_layers_response import SetChartLayersResponse
from .types.upload_chart_response import UploadChartResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChartsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload_chart(
        self,
        *,
        sheet: core.File,
        title: str,
        revision: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadChartResponse]:
        """
        A multipart text part's own example.

        Parameters
        ----------
        sheet : core.File
            See core.File for more documentation

        title : str

        revision : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadChartResponse]
            Uploaded
        """
        _response = self._client_wrapper.httpx_client.request(
            "charts/upload",
            method="POST",
            data={
                "title": title,
                "revision": revision,
            },
            files={
                "sheet": sheet,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadChartResponse,
                    parse_obj_as(
                        type_=UploadChartResponse,
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
    def print_chart(
        self, chart_id: str, *, scale: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        A binary download's query parameter example.

        Parameters
        ----------
        chart_id : str

        scale : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The sheet
        """
        with self._client_wrapper.httpx_client.stream(
            f"charts/{encode_path_param(chart_id)}/print",
            method="GET",
            params={
                "scale": scale,
            },
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
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
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

    @contextlib.contextmanager
    def bundle_charts(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        A top-level array body's media-type example on a binary download.

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The bundle
        """
        with self._client_wrapper.httpx_client.stream(
            "charts/bundle",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
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

    def set_chart_layers(
        self,
        chart_id: str,
        *,
        layers: typing.Sequence[SetChartLayersRequestLayersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SetChartLayersResponse]:
        """
        A scalar-or-list union property's declared example inside an array item.

        Parameters
        ----------
        chart_id : str

        layers : typing.Sequence[SetChartLayersRequestLayersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SetChartLayersResponse]
            Set
        """
        _response = self._client_wrapper.httpx_client.request(
            f"charts/{encode_path_param(chart_id)}/layers",
            method="PUT",
            json={
                "layers": convert_and_respect_annotation_metadata(
                    object_=layers, annotation=typing.Sequence[SetChartLayersRequestLayersItem], direction="write"
                ),
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
                    SetChartLayersResponse,
                    parse_obj_as(
                        type_=SetChartLayersResponse,
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


class AsyncRawChartsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload_chart(
        self,
        *,
        sheet: core.File,
        title: str,
        revision: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadChartResponse]:
        """
        A multipart text part's own example.

        Parameters
        ----------
        sheet : core.File
            See core.File for more documentation

        title : str

        revision : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadChartResponse]
            Uploaded
        """
        _response = await self._client_wrapper.httpx_client.request(
            "charts/upload",
            method="POST",
            data={
                "title": title,
                "revision": revision,
            },
            files={
                "sheet": sheet,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadChartResponse,
                    parse_obj_as(
                        type_=UploadChartResponse,
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
    async def print_chart(
        self, chart_id: str, *, scale: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        A binary download's query parameter example.

        Parameters
        ----------
        chart_id : str

        scale : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The sheet
        """
        async with self._client_wrapper.httpx_client.stream(
            f"charts/{encode_path_param(chart_id)}/print",
            method="GET",
            params={
                "scale": scale,
            },
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
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
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

    @contextlib.asynccontextmanager
    async def bundle_charts(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        A top-level array body's media-type example on a binary download.

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The bundle
        """
        async with self._client_wrapper.httpx_client.stream(
            "charts/bundle",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
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

    async def set_chart_layers(
        self,
        chart_id: str,
        *,
        layers: typing.Sequence[SetChartLayersRequestLayersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SetChartLayersResponse]:
        """
        A scalar-or-list union property's declared example inside an array item.

        Parameters
        ----------
        chart_id : str

        layers : typing.Sequence[SetChartLayersRequestLayersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SetChartLayersResponse]
            Set
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"charts/{encode_path_param(chart_id)}/layers",
            method="PUT",
            json={
                "layers": convert_and_respect_annotation_metadata(
                    object_=layers, annotation=typing.Sequence[SetChartLayersRequestLayersItem], direction="write"
                ),
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
                    SetChartLayersResponse,
                    parse_obj_as(
                        type_=SetChartLayersResponse,
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
