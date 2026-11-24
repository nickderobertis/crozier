

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..types.nullable_color import NullableColor
from ..types.shade import Shade
from .types.encode_value_request_x_inline_nullable_enum import EncodeValueRequestXInlineNullableEnum
from pydantic import ValidationError


class RawSimpleEncodingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def encode_value(
        self,
        *,
        nullable_enum: typing.Optional[NullableColor] = None,
        inline_nullable_enum: typing.Optional[EncodeValueRequestXInlineNullableEnum] = None,
        wrapped_nullable_enum: typing.Optional[Shade] = None,
        plain_enum: typing.Optional[Shade] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        nullable_enum : typing.Optional[NullableColor]

        inline_nullable_enum : typing.Optional[EncodeValueRequestXInlineNullableEnum]

        wrapped_nullable_enum : typing.Optional[Shade]

        plain_enum : typing.Optional[Shade]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "encode",
            method="GET",
            headers={
                "X-Nullable-Enum": str(nullable_enum) if nullable_enum is not None else None,
                "X-Inline-Nullable-Enum": str(inline_nullable_enum) if inline_nullable_enum is not None else None,
                "X-Wrapped-Nullable-Enum": str(wrapped_nullable_enum) if wrapped_nullable_enum is not None else None,
                "X-Plain-Enum": str(plain_enum) if plain_enum is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "ping",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSimpleEncodingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def encode_value(
        self,
        *,
        nullable_enum: typing.Optional[NullableColor] = None,
        inline_nullable_enum: typing.Optional[EncodeValueRequestXInlineNullableEnum] = None,
        wrapped_nullable_enum: typing.Optional[Shade] = None,
        plain_enum: typing.Optional[Shade] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        nullable_enum : typing.Optional[NullableColor]

        inline_nullable_enum : typing.Optional[EncodeValueRequestXInlineNullableEnum]

        wrapped_nullable_enum : typing.Optional[Shade]

        plain_enum : typing.Optional[Shade]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "encode",
            method="GET",
            headers={
                "X-Nullable-Enum": str(nullable_enum) if nullable_enum is not None else None,
                "X-Inline-Nullable-Enum": str(inline_nullable_enum) if inline_nullable_enum is not None else None,
                "X-Wrapped-Nullable-Enum": str(wrapped_nullable_enum) if wrapped_nullable_enum is not None else None,
                "X-Plain-Enum": str(plain_enum) if plain_enum is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ping",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
