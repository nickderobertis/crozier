

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...types.caption_media_request_speed import CaptionMediaRequestSpeed
from .types.caption_media_request_dialect import CaptionMediaRequestDialect
from .types.caption_media_response import CaptionMediaResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMediaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def caption_url(
        self,
        *,
        url: str,
        dialect: typing.Optional[CaptionMediaRequestDialect] = None,
        speed: typing.Optional[CaptionMediaRequestSpeed] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaptionMediaResponse]:
        """
        Parameters
        ----------
        url : str

        dialect : typing.Optional[CaptionMediaRequestDialect]

        speed : typing.Optional[CaptionMediaRequestSpeed]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaptionMediaResponse]
            The captions
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/caption",
            method="POST",
            params={
                "dialect": dialect,
                "speed": speed,
            },
            json={
                "url": url,
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
                    CaptionMediaResponse,
                    parse_obj_as(
                        type_=CaptionMediaResponse,
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

    def caption_file(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        dialect: typing.Optional[CaptionMediaRequestDialect] = None,
        speed: typing.Optional[CaptionMediaRequestSpeed] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaptionMediaResponse]:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        dialect : typing.Optional[CaptionMediaRequestDialect]

        speed : typing.Optional[CaptionMediaRequestSpeed]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaptionMediaResponse]
            The captions
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/caption",
            method="POST",
            params={
                "dialect": dialect,
                "speed": speed,
            },
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaptionMediaResponse,
                    parse_obj_as(
                        type_=CaptionMediaResponse,
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


class AsyncRawMediaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def caption_url(
        self,
        *,
        url: str,
        dialect: typing.Optional[CaptionMediaRequestDialect] = None,
        speed: typing.Optional[CaptionMediaRequestSpeed] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaptionMediaResponse]:
        """
        Parameters
        ----------
        url : str

        dialect : typing.Optional[CaptionMediaRequestDialect]

        speed : typing.Optional[CaptionMediaRequestSpeed]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaptionMediaResponse]
            The captions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/caption",
            method="POST",
            params={
                "dialect": dialect,
                "speed": speed,
            },
            json={
                "url": url,
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
                    CaptionMediaResponse,
                    parse_obj_as(
                        type_=CaptionMediaResponse,
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

    async def caption_file(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        dialect: typing.Optional[CaptionMediaRequestDialect] = None,
        speed: typing.Optional[CaptionMediaRequestSpeed] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaptionMediaResponse]:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        dialect : typing.Optional[CaptionMediaRequestDialect]

        speed : typing.Optional[CaptionMediaRequestSpeed]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaptionMediaResponse]
            The captions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/caption",
            method="POST",
            params={
                "dialect": dialect,
                "speed": speed,
            },
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaptionMediaResponse,
                    parse_obj_as(
                        type_=CaptionMediaResponse,
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
