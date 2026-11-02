

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.list_tiles_request_zoom import ListTilesRequestZoom
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tiles(
        self,
        *,
        corners: typing.Optional[
            typing.Union[typing.Dict[str, typing.Any], typing.Sequence[typing.Dict[str, typing.Any]]]
        ] = None,
        zoom: typing.Optional[ListTilesRequestZoom] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        corners : typing.Optional[typing.Union[typing.Dict[str, typing.Any], typing.Sequence[typing.Dict[str, typing.Any]]]]
            Two or three corner objects bounding the tiles.

        zoom : typing.Optional[ListTilesRequestZoom]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            The tiles.
        """
        _response = self._client_wrapper.httpx_client.request(
            "tiles",
            method="GET",
            params={
                "corners": ",".join(map(str, corners)) if isinstance(corners, (list, tuple, set)) else corners,
                "zoom": convert_and_respect_annotation_metadata(
                    object_=zoom, annotation=ListTilesRequestZoom, direction="write"
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_tiles(
        self,
        *,
        corners: typing.Optional[
            typing.Union[typing.Dict[str, typing.Any], typing.Sequence[typing.Dict[str, typing.Any]]]
        ] = None,
        zoom: typing.Optional[ListTilesRequestZoom] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        corners : typing.Optional[typing.Union[typing.Dict[str, typing.Any], typing.Sequence[typing.Dict[str, typing.Any]]]]
            Two or three corner objects bounding the tiles.

        zoom : typing.Optional[ListTilesRequestZoom]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            The tiles.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tiles",
            method="GET",
            params={
                "corners": ",".join(map(str, corners)) if isinstance(corners, (list, tuple, set)) else corners,
                "zoom": convert_and_respect_annotation_metadata(
                    object_=zoom, annotation=ListTilesRequestZoom, direction="write"
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
