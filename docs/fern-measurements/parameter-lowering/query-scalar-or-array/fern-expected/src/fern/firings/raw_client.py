

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.list_cooling_firings_request_atmosphere import ListCoolingFiringsRequestAtmosphere
from .types.list_cooling_firings_request_pyrometer import ListCoolingFiringsRequestPyrometer
from .types.list_firings_request_glaze import ListFiringsRequestGlaze
from .types.list_firings_request_shelf import ListFiringsRequestShelf
from pydantic import ValidationError


class RawFiringsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_firings(
        self,
        *,
        shelf: ListFiringsRequestShelf,
        glaze: ListFiringsRequestGlaze,
        cone: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        shelf : ListFiringsRequestShelf

        glaze : ListFiringsRequestGlaze

        cone : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Scheduled firings.
        """
        _response = self._client_wrapper.httpx_client.request(
            "firings",
            method="GET",
            params={
                "cone": cone,
                "shelf": convert_and_respect_annotation_metadata(
                    object_=shelf, annotation=ListFiringsRequestShelf, direction="write"
                ),
                "glaze": convert_and_respect_annotation_metadata(
                    object_=glaze, annotation=ListFiringsRequestGlaze, direction="write"
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

    def list_cooling_firings(
        self,
        *,
        kiln: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        batch: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        atmosphere: typing.Optional[ListCoolingFiringsRequestAtmosphere] = None,
        pyrometer: typing.Optional[ListCoolingFiringsRequestPyrometer] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        kiln : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        batch : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        atmosphere : typing.Optional[ListCoolingFiringsRequestAtmosphere]

        pyrometer : typing.Optional[ListCoolingFiringsRequestPyrometer]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Firings that are cooling.
        """
        _response = self._client_wrapper.httpx_client.request(
            "firings/cooling",
            method="GET",
            params={
                "kiln": kiln,
                "batch": batch,
                "atmosphere": convert_and_respect_annotation_metadata(
                    object_=atmosphere, annotation=ListCoolingFiringsRequestAtmosphere, direction="write"
                ),
                "pyrometer": convert_and_respect_annotation_metadata(
                    object_=pyrometer, annotation=typing.Optional[ListCoolingFiringsRequestPyrometer], direction="write"
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


class AsyncRawFiringsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_firings(
        self,
        *,
        shelf: ListFiringsRequestShelf,
        glaze: ListFiringsRequestGlaze,
        cone: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        shelf : ListFiringsRequestShelf

        glaze : ListFiringsRequestGlaze

        cone : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Scheduled firings.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "firings",
            method="GET",
            params={
                "cone": cone,
                "shelf": convert_and_respect_annotation_metadata(
                    object_=shelf, annotation=ListFiringsRequestShelf, direction="write"
                ),
                "glaze": convert_and_respect_annotation_metadata(
                    object_=glaze, annotation=ListFiringsRequestGlaze, direction="write"
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

    async def list_cooling_firings(
        self,
        *,
        kiln: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        batch: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        atmosphere: typing.Optional[ListCoolingFiringsRequestAtmosphere] = None,
        pyrometer: typing.Optional[ListCoolingFiringsRequestPyrometer] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        kiln : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        batch : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        atmosphere : typing.Optional[ListCoolingFiringsRequestAtmosphere]

        pyrometer : typing.Optional[ListCoolingFiringsRequestPyrometer]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Firings that are cooling.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "firings/cooling",
            method="GET",
            params={
                "kiln": kiln,
                "batch": batch,
                "atmosphere": convert_and_respect_annotation_metadata(
                    object_=atmosphere, annotation=ListCoolingFiringsRequestAtmosphere, direction="write"
                ),
                "pyrometer": convert_and_respect_annotation_metadata(
                    object_=pyrometer, annotation=typing.Optional[ListCoolingFiringsRequestPyrometer], direction="write"
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
