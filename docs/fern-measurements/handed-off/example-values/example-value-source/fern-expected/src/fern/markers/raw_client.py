

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.place_marker_request_marker import PlaceMarkerRequestMarker
from .types.place_marker_response import PlaceMarkerResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMarkersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def place_marker(
        self, *, marker: PlaceMarkerRequestMarker, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PlaceMarkerResponse]:
        """
        A union-typed property's declared example.

        Parameters
        ----------
        marker : PlaceMarkerRequestMarker

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PlaceMarkerResponse]
            Placed
        """
        _response = self._client_wrapper.httpx_client.request(
            "markers",
            method="POST",
            json={
                "marker": convert_and_respect_annotation_metadata(
                    object_=marker, annotation=PlaceMarkerRequestMarker, direction="write"
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
                    PlaceMarkerResponse,
                    parse_obj_as(
                        type_=PlaceMarkerResponse,
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


class AsyncRawMarkersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def place_marker(
        self, *, marker: PlaceMarkerRequestMarker, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PlaceMarkerResponse]:
        """
        A union-typed property's declared example.

        Parameters
        ----------
        marker : PlaceMarkerRequestMarker

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PlaceMarkerResponse]
            Placed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "markers",
            method="POST",
            json={
                "marker": convert_and_respect_annotation_metadata(
                    object_=marker, annotation=PlaceMarkerRequestMarker, direction="write"
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
                    PlaceMarkerResponse,
                    parse_obj_as(
                        type_=PlaceMarkerResponse,
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
