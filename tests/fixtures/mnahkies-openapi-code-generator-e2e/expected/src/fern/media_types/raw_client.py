

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.product_order import ProductOrder
from ..types.product_order_address import ProductOrderAddress
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMediaTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_media_types_text(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Rendered as HTML
        """
        _response = self._client_wrapper.httpx_client.request(
            "media-types/text",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_media_types_x_www_form_urlencoded(
        self,
        *,
        sku: typing.Optional[str] = OMIT,
        quantity: typing.Optional[float] = OMIT,
        address: typing.Optional[ProductOrderAddress] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProductOrder]:
        """
        Parameters
        ----------
        sku : typing.Optional[str]

        quantity : typing.Optional[float]

        address : typing.Optional[ProductOrderAddress]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProductOrder]
            Echoed back as JSON
        """
        _response = self._client_wrapper.httpx_client.request(
            "media-types/x-www-form-urlencoded",
            method="POST",
            data={
                "sku": sku,
                "quantity": quantity,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=ProductOrderAddress, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProductOrder,
                    parse_obj_as(
                        type_=ProductOrder,
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
    def post_media_types_octet_stream(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            ok
        """
        with self._client_wrapper.httpx_client.stream(
            "media-types/octet-stream",
            method="POST",
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
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


class AsyncRawMediaTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_media_types_text(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Rendered as HTML
        """
        _response = await self._client_wrapper.httpx_client.request(
            "media-types/text",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_media_types_x_www_form_urlencoded(
        self,
        *,
        sku: typing.Optional[str] = OMIT,
        quantity: typing.Optional[float] = OMIT,
        address: typing.Optional[ProductOrderAddress] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProductOrder]:
        """
        Parameters
        ----------
        sku : typing.Optional[str]

        quantity : typing.Optional[float]

        address : typing.Optional[ProductOrderAddress]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProductOrder]
            Echoed back as JSON
        """
        _response = await self._client_wrapper.httpx_client.request(
            "media-types/x-www-form-urlencoded",
            method="POST",
            data={
                "sku": sku,
                "quantity": quantity,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=ProductOrderAddress, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProductOrder,
                    parse_obj_as(
                        type_=ProductOrder,
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
    async def post_media_types_octet_stream(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            ok
        """
        async with self._client_wrapper.httpx_client.stream(
            "media-types/octet-stream",
            method="POST",
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
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
