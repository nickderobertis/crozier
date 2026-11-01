

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.list_broadcasts_request_after import ListBroadcastsRequestAfter
from .types.list_broadcasts_request_window import ListBroadcastsRequestWindow
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_broadcasts(
        self,
        station: str,
        *,
        after: typing.Optional[ListBroadcastsRequestAfter] = None,
        window: typing.Optional[ListBroadcastsRequestWindow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        station : str

        after : typing.Optional[ListBroadcastsRequestAfter]
            Only list broadcasts after this local time.

        window : typing.Optional[ListBroadcastsRequestWindow]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            The broadcasts
        """
        _response = self._client_wrapper.httpx_client.request(
            f"broadcasts/{encode_path_param(station)}",
            method="GET",
            params={
                "after": convert_and_respect_annotation_metadata(
                    object_=after, annotation=typing.Optional[ListBroadcastsRequestAfter], direction="write"
                ),
                "window": convert_and_respect_annotation_metadata(
                    object_=window, annotation=typing.Optional[ListBroadcastsRequestWindow], direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def tag_broadcast(
        self,
        station: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Parameters
        ----------
        station : str

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Tags applied
        """
        _response = self._client_wrapper.httpx_client.request(
            f"broadcasts/{encode_path_param(station)}/tags",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    async def list_broadcasts(
        self,
        station: str,
        *,
        after: typing.Optional[ListBroadcastsRequestAfter] = None,
        window: typing.Optional[ListBroadcastsRequestWindow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        station : str

        after : typing.Optional[ListBroadcastsRequestAfter]
            Only list broadcasts after this local time.

        window : typing.Optional[ListBroadcastsRequestWindow]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            The broadcasts
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"broadcasts/{encode_path_param(station)}",
            method="GET",
            params={
                "after": convert_and_respect_annotation_metadata(
                    object_=after, annotation=typing.Optional[ListBroadcastsRequestAfter], direction="write"
                ),
                "window": convert_and_respect_annotation_metadata(
                    object_=window, annotation=typing.Optional[ListBroadcastsRequestWindow], direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def tag_broadcast(
        self,
        station: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Parameters
        ----------
        station : str

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Tags applied
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"broadcasts/{encode_path_param(station)}/tags",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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
